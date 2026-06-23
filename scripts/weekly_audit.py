#!/usr/bin/env python3
"""Automated structural audit for W01-W15 weekly report folders.

This audit intentionally checks only machine-verifiable repository facts:
folder/file existence, local relative links, simple document features, and
zero-byte files. It does not validate reference truth, paper quality, PDF
visual integrity, or scholarly correctness.
"""

from __future__ import annotations

import csv
import json
import re
import shutil
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
WEEKLY_ROOT = ROOT / "03_weekly_reports"
STATUS_MD = WEEKLY_ROOT / "WEEKLY_STATUS.md"
STATUS_CSV = WEEKLY_ROOT / "WEEKLY_STATUS.csv"
STATUS_JSON = WEEKLY_ROOT / "WEEKLY_STATUS.json"
AUDIT_REPORT = ROOT / "AUDIT_REPORT_WEEKLY_SUBMISSIONS.md"
AUDIT_BACKUP = ROOT / "AUDIT_REPORT_WEEKLY_SUBMISSIONS.backup.md"

KST = timezone(timedelta(hours=9))
GENERATED_AT = datetime.now(KST).strftime("%Y-%m-%d %H:%M:%S KST")
README_MARKER = "<!-- AUTO-GENERATED-WEEKLY-AUDIT-README -->"

REQUIRED_SUBDIRS = [
    "00_management",
    "01_papers",
    "02_paper_summaries",
    "03_theory_notes",
    "04_experiment",
    "05_ai_worklog",
    "06_report",
    "07_week_submission",
    "08_final_paper_bridge",
    "09_presentation",
]

WEEKS = [
    ("W01", "w01_deep_learning_ml_security", "딥러닝 패러다임 & ML 보안 분류학"),
    ("W02", "w02_optimization_data_poisoning", "대규모 최적화 & 데이터 오염 위협"),
    ("W03", "w03_computer_vision_adversarial", "컴퓨터비전 표현학습 & 비전 대적공격"),
    ("W04", "w04_transformer_nlp_security", "Transformer 변형 & NLP 대적공격·프라이버시"),
    ("W05", "w05_ssl_backdoor", "자기지도학습·파운데이션 모델 & Poisoning/Backdoor"),
    ("W06", "w06_diffusion_gan_deepfake", "확률생성모형(Diffusion/GAN) & 딥페이크 검출"),
    ("W07", "w07_llm_security_privacy", "LLM 학습·정렬·평가 & LLM 보안·프라이버시"),
    ("W08", "w08_rag_prompt_injection", "RAG·프롬프팅 프레임워크 & 프롬프트 인젝션"),
    ("W09", "w09_drl_cybersecurity", "심층강화학습(DRL) & 사이버보안 적용·보상조작"),
    ("W10", "w10_federated_learning_security", "연합학습(FL) & FL 위협·방어·정책"),
    ("W11", "w11_differential_privacy_mi", "차등프라이버시(DP) & 멤버십 추론 공격·방어"),
    ("W12", "w12_nn_verification_xai", "신경망 검증·정형방법 & 대적방어·XAI·강건성 트레이드오프"),
    ("W13", "w13_model_stealing_watermarking", "모델 지식재산(IP)·모델 도난·모델 추출 위협"),
    ("W14", "w14_mlops_supply_chain", "MLOps/DevOps·데이터/모델 파이프라인·공급망 보안"),
    ("W15", "w15_reproducibility_xai_paper", "연구평가·재현성·설명가능성(XAI)·논문 구성"),
]

TEXT_EXTS = {
    ".md",
    ".markdown",
    ".html",
    ".htm",
    ".txt",
    ".csv",
    ".json",
    ".yaml",
    ".yml",
    ".tex",
}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
PRESENTATION_EXTS = {".md", ".markdown", ".html", ".htm"}
REPORT_EXTS = {".md", ".markdown", ".html", ".htm", ".docx", ".pdf"}
RESULT_EXTS = {
    ".csv",
    ".json",
    ".jsonl",
    ".md",
    ".txt",
    ".log",
    ".png",
    ".jpg",
    ".jpeg",
    ".svg",
    ".npz",
    ".npy",
    ".pkl",
    ".parquet",
}

MD_LINK_RE = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
MD_REF_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
HTML_LINK_RE = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
TABLE_SEPARATOR_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")
FORMULA_RE = re.compile(
    r"(\$\$.*?\$\$|\$[^$\n]{1,200}\$|\\\(|\\\[|\\frac|\\sum|\\prod|\\argmax|\\argmin|\\mathbb|\\mathbf|\\epsilon|<math\b)",
    re.DOTALL,
)
MERMAID_RE = re.compile(
    r"```mermaid|^\s*(graph|flowchart|sequenceDiagram|stateDiagram|classDiagram|erDiagram|gantt|timeline)\b",
    re.IGNORECASE | re.MULTILINE,
)


@dataclass
class LinkIssue:
    source: str
    line: int
    target: str


@dataclass
class WeekAudit:
    week: str
    folder: str
    topic: str
    path: str
    existed_before: bool
    exists_after: bool
    missing_required_before: list[str] = field(default_factory=list)
    missing_required_after: list[str] = field(default_factory=list)
    created_dirs: list[str] = field(default_factory=list)
    created_keep_files: list[str] = field(default_factory=list)
    readme_created: bool = False
    readme_updated: bool = False
    markdown_files: list[str] = field(default_factory=list)
    report_candidates: list[str] = field(default_factory=list)
    presentation_files: list[str] = field(default_factory=list)
    image_files: list[str] = field(default_factory=list)
    has_table: bool = False
    has_formula: bool = False
    has_mermaid_or_diagram_code: bool = False
    outputs_dir_exists: bool = False
    experiment_result_files: list[str] = field(default_factory=list)
    ai_disclosure_files: list[str] = field(default_factory=list)
    broken_links: list[LinkIssue] = field(default_factory=list)
    zero_byte_files: list[str] = field(default_factory=list)
    score: dict[str, int] = field(default_factory=dict)
    total_score: int = 0

    def to_json(self) -> dict[str, object]:
        return {
            "week": self.week,
            "folder": self.folder,
            "topic": self.topic,
            "path": self.path,
            "existed_before": self.existed_before,
            "exists_after": self.exists_after,
            "missing_required_before": self.missing_required_before,
            "missing_required_after": self.missing_required_after,
            "created_dirs": self.created_dirs,
            "created_keep_files": self.created_keep_files,
            "readme_created": self.readme_created,
            "readme_updated": self.readme_updated,
            "markdown_files": self.markdown_files,
            "report_candidates": self.report_candidates,
            "presentation_files": self.presentation_files,
            "image_files": self.image_files,
            "has_table": self.has_table,
            "has_formula": self.has_formula,
            "has_mermaid_or_diagram_code": self.has_mermaid_or_diagram_code,
            "outputs_dir_exists": self.outputs_dir_exists,
            "experiment_result_files": self.experiment_result_files,
            "ai_disclosure_files": self.ai_disclosure_files,
            "broken_links": [issue.__dict__ for issue in self.broken_links],
            "zero_byte_files": self.zero_byte_files,
            "score": self.score,
            "total_score": self.total_score,
        }


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def safe_read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def is_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTS


def strip_fenced_blocks(text: str) -> str:
    lines = []
    in_fence = False
    fence_marker = ""
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            lines.append("")
            continue
        lines.append("" if in_fence else line)
    return "\n".join(lines)


def has_markdown_table(text: str) -> bool:
    if "<table" in text.lower():
        return True
    lines = text.splitlines()
    for idx in range(len(lines) - 1):
        if "|" in lines[idx] and TABLE_SEPARATOR_RE.match(lines[idx + 1]):
            return True
    return False


def has_formula(text: str) -> bool:
    return FORMULA_RE.search(text) is not None


def has_mermaid_or_diagram_code(text: str) -> bool:
    return MERMAID_RE.search(text) is not None


def normalize_link_target(raw: str) -> str:
    target = raw.strip().strip("<>").strip()
    if " " in target and not Path(target).exists():
        target = target.split()[0]
    if target.startswith(("'", '"')) and target.endswith(("'", '"')):
        target = target[1:-1]
    return target


def is_external_or_nonfile(target: str) -> bool:
    lower = target.lower()
    return (
        not target
        or lower.startswith(("#", "http://", "https://", "mailto:", "tel:", "data:", "javascript:", "about:", "//"))
        or lower.startswith("{")
    )


def link_path_part(target: str) -> str:
    parts = urlsplit(target)
    path = parts.path if parts.scheme == "" else ""
    return unquote(path)


def extract_link_targets(text: str) -> Iterable[tuple[int, str]]:
    clean = strip_fenced_blocks(text)
    for line_number, line in enumerate(clean.splitlines(), start=1):
        for regex in (MD_LINK_RE, HTML_LINK_RE):
            for match in regex.finditer(line):
                yield line_number, normalize_link_target(match.group(1))
    for match in MD_REF_RE.finditer(clean):
        line_number = clean[: match.start()].count("\n") + 1
        yield line_number, normalize_link_target(match.group(1))


def check_broken_links(files: list[Path]) -> list[LinkIssue]:
    issues: list[LinkIssue] = []
    for source in files:
        if not is_text_file(source):
            continue
        text = safe_read_text(source)
        for line_number, target in extract_link_targets(text):
            if is_external_or_nonfile(target):
                continue
            path_part = link_path_part(target)
            if not path_part or path_part.startswith("/"):
                continue
            candidate = (source.parent / path_part).resolve()
            if not candidate.exists():
                issues.append(LinkIssue(rel(source), line_number, target))
    return issues


def find_report_candidates(files: list[Path], week_dir: Path) -> list[Path]:
    candidates = []
    for path in files:
        lower_name = path.name.lower()
        lower_rel = path.relative_to(week_dir).as_posix().lower()
        if path.suffix.lower() not in REPORT_EXTS:
            continue
        if "submit_checklist" in lower_name:
            continue
        if "06_report/" not in lower_rel and "07_week_submission/" not in lower_rel:
            continue
        if any(token in lower_name for token in ("integrated_report", "submission_report", "weekly_report", "report")):
            candidates.append(path)
    return sorted(candidates)


def find_presentation_files(files: list[Path], week_dir: Path) -> list[Path]:
    presentation_dir = week_dir / "09_presentation"
    return sorted(
        path
        for path in files
        if presentation_dir in path.parents and path.suffix.lower() in PRESENTATION_EXTS
    )


def find_experiment_result_files(files: list[Path], week_dir: Path) -> list[Path]:
    experiment_dir = week_dir / "04_experiment"
    result_files = []
    for path in files:
        if experiment_dir not in path.parents:
            continue
        lower_rel = path.relative_to(experiment_dir).as_posix().lower()
        lower_name = path.name.lower()
        if "/outputs/" in f"/{lower_rel}" or "/results/" in f"/{lower_rel}" or lower_rel.startswith(("outputs/", "results/")):
            if path.suffix.lower() in RESULT_EXTS:
                result_files.append(path)
                continue
        if lower_name in {"metrics_summary.csv", "results.json", "run_log.md", "experiment_report.md"}:
            result_files.append(path)
        elif any(token in lower_name for token in ("metric", "result", "run_log", "output")) and path.suffix.lower() in RESULT_EXTS:
            result_files.append(path)
    return sorted(set(result_files))


def find_ai_disclosure_files(files: list[Path], week_dir: Path) -> list[Path]:
    ai_dir = week_dir / "05_ai_worklog"
    result = []
    for path in files:
        if ai_dir not in path.parents or path.suffix.lower() not in {".md", ".txt"}:
            continue
        lower_name = path.name.lower()
        if "ai_disclosure" in lower_name or "ai_worklog" in lower_name:
            result.append(path)
            continue
        text = safe_read_text(path)
        if "AI 활용 고지" in text or "AI disclosure" in text:
            result.append(path)
    return sorted(set(result))


def bool_mark(value: bool) -> str:
    return "O" if value else "X"


def md_link(path: Path, base: Path) -> str:
    label = path.name
    target = path.relative_to(base).as_posix()
    return f"[{label}]({target})"


def md_link_root(path: str) -> str:
    return f"[{path}]({path})"


def list_or_none(paths: list[Path], base: Path, limit: int = 8) -> str:
    if not paths:
        return "- 자동 점검 시 후보 파일 없음\n"
    lines = [f"- {md_link(path, base)}" for path in paths[:limit]]
    if len(paths) > limit:
        lines.append(f"- 외 {len(paths) - limit}개")
    return "\n".join(lines) + "\n"


def write_week_readme(week_dir: Path, audit: WeekAudit, raw_paths: dict[str, list[Path]]) -> tuple[bool, bool]:
    readme = week_dir / "README.md"
    exists = readme.exists()
    should_manage = not exists
    if exists:
        current = safe_read_text(readme)
        should_manage = current.startswith(README_MARKER)
    if not should_manage:
        return False, False

    report_paths = raw_paths["report_candidates"]
    presentation_paths = raw_paths["presentation_files"]
    experiment_paths = raw_paths["experiment_result_files"]
    bridge_dir = week_dir / "08_final_paper_bridge"
    bridge_paths = sorted(path for path in bridge_dir.glob("*.md") if path.is_file()) if bridge_dir.exists() else []
    important_paths = [
        week_dir / "00_management" / "week_info.md",
        week_dir / "01_papers" / "paper_list.md",
        week_dir / "02_paper_summaries" / "paper_matrix.md",
        week_dir / "03_theory_notes" / "threat_model.md",
        week_dir / "05_ai_worklog" / "ai_worklog.md",
    ]
    important_paths = [path for path in important_paths if path.exists()]

    content = f"""{README_MARKER}
# {audit.week} {audit.folder}

자동 생성 파일: `scripts/weekly_audit.py`

## 주차명

- {audit.week}: {audit.folder}

## 핵심 주제

- {audit.topic}

## 주요 파일 링크

{list_or_none(important_paths, week_dir)}
## 보고서 링크

{list_or_none(report_paths, week_dir)}
## 발표자료 링크

{list_or_none(presentation_paths, week_dir)}
## 실험/결과 링크

{list_or_none(experiment_paths, week_dir)}
## 기말논문 연결 메모

{list_or_none(bridge_paths, week_dir)}
## 자동 점검 메모

- 자동 점수: {audit.total_score}/100
- 표 포함: {bool_mark(audit.has_table)}
- 그림 파일 존재: {bool_mark(bool(audit.image_files))}
- 수식 표현 포함: {bool_mark(audit.has_formula)}
- Mermaid/diagram 코드 포함: {bool_mark(audit.has_mermaid_or_diagram_code)}
- 깨진 상대경로 링크: {len(audit.broken_links)}건
- 0바이트 파일: {len(audit.zero_byte_files)}건

이 README는 파일 존재와 구조를 자동으로 정리한 문서이며, 참고문헌 진위·논문 품질·PDF 시각 검수는 사람이 별도로 확인해야 한다.
"""
    if exists and safe_read_text(readme) == content:
        return False, False
    readme.write_text(content, encoding="utf-8")
    return not exists, exists


def audit_week(week: str, folder: str, topic: str) -> WeekAudit:
    week_dir = WEEKLY_ROOT / folder
    existed_before = week_dir.exists()
    missing_before = [
        subdir for subdir in REQUIRED_SUBDIRS if not (week_dir / subdir).is_dir()
    ] if existed_before else REQUIRED_SUBDIRS.copy()

    created_dirs = []
    created_keep_files = []
    if not week_dir.exists():
        week_dir.mkdir(parents=True)
        created_dirs.append(rel(week_dir))
    for subdir in REQUIRED_SUBDIRS:
        path = week_dir / subdir
        if not path.exists():
            path.mkdir(parents=True)
            created_dirs.append(rel(path))
            keep = path / ".gitkeep"
            keep.touch()
            created_keep_files.append(rel(keep))

    files_before_readme = sorted(path for path in week_dir.rglob("*") if path.is_file())
    raw_texts = [safe_read_text(path) for path in files_before_readme if is_text_file(path)]
    report_candidates = find_report_candidates(files_before_readme, week_dir)
    presentation_files = find_presentation_files(files_before_readme, week_dir)
    image_files = sorted(path for path in files_before_readme if path.suffix.lower() in IMAGE_EXTS)
    experiment_result_files = find_experiment_result_files(files_before_readme, week_dir)
    ai_disclosure_files = find_ai_disclosure_files(files_before_readme, week_dir)
    outputs_dir_exists = (week_dir / "04_experiment" / "outputs").is_dir() or any(
        path.is_dir() and path.name == "outputs"
        for path in (week_dir / "04_experiment").rglob("*")
        if (week_dir / "04_experiment").exists()
    )
    broken_links = check_broken_links(files_before_readme)
    zero_byte_files = sorted(rel(path) for path in files_before_readme if path.stat().st_size == 0)

    missing_after = [subdir for subdir in REQUIRED_SUBDIRS if not (week_dir / subdir).is_dir()]

    structure_score = round(20 * (len(REQUIRED_SUBDIRS) - len(missing_after)) / len(REQUIRED_SUBDIRS))
    visual_formula_score = (
        (5 if any(has_markdown_table(text) for text in raw_texts) else 0)
        + (5 if image_files else 0)
        + (5 if any(has_formula(text) for text in raw_texts) else 0)
    )
    integrity_score = (5 if not broken_links else 0) + (5 if not zero_byte_files else 0)

    audit = WeekAudit(
        week=week,
        folder=folder,
        topic=topic,
        path=rel(week_dir),
        existed_before=existed_before,
        exists_after=week_dir.exists(),
        missing_required_before=missing_before,
        missing_required_after=missing_after,
        created_dirs=created_dirs,
        created_keep_files=created_keep_files,
        markdown_files=sorted(rel(path) for path in files_before_readme if path.suffix.lower() in {".md", ".markdown"}),
        report_candidates=sorted(rel(path) for path in report_candidates),
        presentation_files=sorted(rel(path) for path in presentation_files),
        image_files=sorted(rel(path) for path in image_files),
        has_table=any(has_markdown_table(text) for text in raw_texts),
        has_formula=any(has_formula(text) for text in raw_texts),
        has_mermaid_or_diagram_code=any(has_mermaid_or_diagram_code(text) for text in raw_texts),
        outputs_dir_exists=outputs_dir_exists,
        experiment_result_files=sorted(rel(path) for path in experiment_result_files),
        ai_disclosure_files=sorted(rel(path) for path in ai_disclosure_files),
        broken_links=broken_links,
        zero_byte_files=zero_byte_files,
        score={
            "folder_structure": structure_score,
            "report_file": 20 if report_candidates else 0,
            "presentation_file": 15 if presentation_files else 0,
            "table_image_formula": visual_formula_score,
            "experiment_outputs": 10 if outputs_dir_exists or experiment_result_files else 0,
            "ai_disclosure": 10 if ai_disclosure_files else 0,
            "link_file_integrity": integrity_score,
        },
    )
    audit.total_score = sum(audit.score.values())

    readme_created, readme_updated = write_week_readme(
        week_dir,
        audit,
        {
            "report_candidates": report_candidates,
            "presentation_files": presentation_files,
            "experiment_result_files": experiment_result_files,
        },
    )
    audit.readme_created = readme_created
    audit.readme_updated = readme_updated
    if readme_created:
        audit.markdown_files.append(rel(week_dir / "README.md"))
        audit.markdown_files = sorted(set(audit.markdown_files))

    return audit


def write_status_json(audits: list[WeekAudit], changes: dict[str, object]) -> None:
    payload = {
        "generated_at": GENERATED_AT,
        "scope": "03_weekly_reports/w01-w15 only",
        "automatic_only": True,
        "excluded_manual_checks": [
            "reference authenticity",
            "paper quality",
            "PDF visual integrity",
            "final paper content edits",
        ],
        "changes": changes,
        "weeks": [audit.to_json() for audit in audits],
    }
    STATUS_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_status_csv(audits: list[WeekAudit]) -> None:
    with STATUS_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            [
                "week",
                "folder",
                "topic",
                "total_score",
                "folder_structure_score",
                "report_file_score",
                "presentation_file_score",
                "table_image_formula_score",
                "experiment_outputs_score",
                "ai_disclosure_score",
                "link_file_integrity_score",
                "markdown_files_count",
                "report_candidates_count",
                "presentation_files_count",
                "image_files_count",
                "has_table",
                "has_formula",
                "has_mermaid_or_diagram_code",
                "outputs_dir_exists",
                "experiment_result_files_count",
                "ai_disclosure_files_count",
                "broken_links_count",
                "zero_byte_files_count",
                "missing_required_before",
                "missing_required_after",
            ]
        )
        for audit in audits:
            writer.writerow(
                [
                    audit.week,
                    audit.folder,
                    audit.topic,
                    audit.total_score,
                    audit.score["folder_structure"],
                    audit.score["report_file"],
                    audit.score["presentation_file"],
                    audit.score["table_image_formula"],
                    audit.score["experiment_outputs"],
                    audit.score["ai_disclosure"],
                    audit.score["link_file_integrity"],
                    len(audit.markdown_files),
                    len(audit.report_candidates),
                    len(audit.presentation_files),
                    len(audit.image_files),
                    audit.has_table,
                    audit.has_formula,
                    audit.has_mermaid_or_diagram_code,
                    audit.outputs_dir_exists,
                    len(audit.experiment_result_files),
                    len(audit.ai_disclosure_files),
                    len(audit.broken_links),
                    len(audit.zero_byte_files),
                    ";".join(audit.missing_required_before),
                    ";".join(audit.missing_required_after),
                ]
            )


def score_table(audits: list[WeekAudit]) -> str:
    lines = [
        "| 주차 | 폴더 | 점수 | 구조 | 보고서 | 발표 | 표/그림/수식 | 실험 | AI 고지 | 무결성 | 깨진 링크 | 0바이트 |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for audit in audits:
        lines.append(
            "| {week} | `{folder}` | {total} | {structure} | {report} | {presentation} | {tif} | {experiment} | {ai} | {integrity} | {broken} | {zero} |".format(
                week=audit.week,
                folder=audit.folder,
                total=audit.total_score,
                structure=audit.score["folder_structure"],
                report=audit.score["report_file"],
                presentation=audit.score["presentation_file"],
                tif=audit.score["table_image_formula"],
                experiment=audit.score["experiment_outputs"],
                ai=audit.score["ai_disclosure"],
                integrity=audit.score["link_file_integrity"],
                broken=len(audit.broken_links),
                zero=len(audit.zero_byte_files),
            )
        )
    return "\n".join(lines)


def broken_links_section(audits: list[WeekAudit]) -> str:
    issues = [(audit.week, issue) for audit in audits for issue in audit.broken_links]
    if not issues:
        return "- 없음\n"
    lines = []
    for week, issue in issues:
        lines.append(f"- {week}: `{issue.source}:{issue.line}` -> `{issue.target}`")
    return "\n".join(lines) + "\n"


def zero_byte_section(audits: list[WeekAudit]) -> str:
    files = [(audit.week, path) for audit in audits for path in audit.zero_byte_files]
    if not files:
        return "- 없음\n"
    return "\n".join(f"- {week}: `{path}`" for week, path in files) + "\n"


def created_dirs_section(audits: list[WeekAudit]) -> str:
    dirs = [path for audit in audits for path in audit.created_dirs]
    if not dirs:
        return "- 없음\n"
    return "\n".join(f"- `{path}`" for path in dirs) + "\n"


def readme_changes_section(audits: list[WeekAudit]) -> str:
    changed = []
    for audit in audits:
        readme_path = f"03_weekly_reports/{audit.folder}/README.md"
        if audit.readme_created:
            changed.append(f"- 생성: `{readme_path}`")
        elif audit.readme_updated:
            changed.append(f"- 갱신: `{readme_path}`")
    if not changed:
        return "- 없음\n"
    return "\n".join(changed) + "\n"


def readme_inventory_section(audits: list[WeekAudit]) -> str:
    missing = []
    for audit in audits:
        path = ROOT / "03_weekly_reports" / audit.folder / "README.md"
        if not path.exists():
            missing.append(f"03_weekly_reports/{audit.folder}/README.md")
    if not missing:
        return "- W01-W15 주차별 루트 `README.md`가 모두 존재함\n"
    return "\n".join(f"- 누락: `{path}`" for path in missing) + "\n"


def write_status_md(audits: list[WeekAudit], changes: dict[str, object]) -> None:
    status_files = [
        rel(STATUS_MD),
        rel(STATUS_CSV),
        rel(STATUS_JSON),
    ]
    content = f"""# W01-W15 주차별 자동 점검 상태

생성일: {GENERATED_AT}

## 점검 범위

- 대상: `03_weekly_reports/w01`부터 `w15`까지의 주차별 보고서 폴더
- 제외: 참고문헌 진위 확인, 논문 질 평가, PDF 육안 확인, 기말논문 원고 편집
- 방식: 파일/폴더 존재, 문서 특징, 로컬 상대경로 링크, 0바이트 파일만 자동 점검

## 주차별 자동 점수

{score_table(audits)}

## 생성 또는 갱신된 상태 파일

{chr(10).join(f"- `{path}`" for path in status_files)}

## 주차별 README 변경

{readme_changes_section(audits)}
## 주차별 README 존재 상태

{readme_inventory_section(audits)}
## 누락 보완한 폴더

{created_dirs_section(audits)}
## 깨진 상대경로 링크

{broken_links_section(audits)}
## 0바이트 파일

{zero_byte_section(audits)}
## 사람이 직접 확인해야 할 항목

- 참고문헌 DOI/URL/출판사 페이지의 실제 존재와 강의 지정문헌 일치 여부
- 논문 선정 품질, 요약의 학술적 타당성, 비판적 해석의 적절성
- PDF 원문 파일의 열람 가능성, 페이지 깨짐, 서식 및 그림 가독성
- 실험 수치의 과학적 의미, 재현성, 데이터/코드 실행 결과의 타당성
- AI 활용 고지 내용의 사실관계와 최종 제출 전 연구윤리 책임 확인
"""
    STATUS_MD.write_text(content, encoding="utf-8")


def write_audit_report(audits: list[WeekAudit], changes: dict[str, object]) -> None:
    backup_note = changes.get("audit_backup", "생성하지 않음")
    content = f"""# W01-W15 주차별 보고서 자동 감사 보고서

감사 기준일: {GENERATED_AT}

## 1. 자동 감사 원칙

- 대상은 `03_weekly_reports/` 아래 W01-W15 주차별 보고서 폴더로 제한했다.
- `04_final_paper/`, `06_submission/`, 논문 제출용 구조는 이동하거나 편집하지 않았다.
- 참고문헌 진위 확인, 논문 질 평가, PDF 육안 확인은 자동 정상 처리하지 않았다.
- 점수는 구조와 파일 존재, 문서 특징, 상대경로 링크, 0바이트 파일 여부만 반영한다.

## 2. 변경 전후 기록

- 기존 감사 보고서 백업: `{backup_note}`
- 상태 파일 생성/갱신: `03_weekly_reports/WEEKLY_STATUS.md`, `03_weekly_reports/WEEKLY_STATUS.csv`, `03_weekly_reports/WEEKLY_STATUS.json`
- 주차별 README 변경:

{readme_changes_section(audits)}
## 3. 주차별 README 존재 상태

{readme_inventory_section(audits)}
## 4. 누락 보완한 폴더

{created_dirs_section(audits)}
## 5. 주차별 자동 점수

{score_table(audits)}

## 6. 깨진 상대경로 링크 목록

{broken_links_section(audits)}
## 7. 0바이트 파일 목록

{zero_byte_section(audits)}
## 8. 자동 점검 상세 기준

| 항목 | 배점 | 자동 판정 |
|---|---:|---|
| 폴더 구조 완성도 | 20 | 필수 하위폴더 10개 존재 비율 |
| 보고서 파일 존재 | 20 | `06_report/` 또는 `07_week_submission/`의 보고서 후보 존재 |
| 발표자료 존재 | 15 | `09_presentation/`의 HTML 또는 Markdown 존재 |
| 표/그림/수식 포함 | 15 | 표 5점, 이미지 파일 5점, 수식 표현 5점 |
| 실험/산출물 존재 | 10 | `04_experiment/outputs/` 또는 결과 파일 존재 |
| AI 활용 고지 존재 | 10 | `05_ai_worklog/`의 AI 고지/작업기록 후보 존재 |
| 링크/파일 무결성 | 10 | 깨진 상대경로 링크 5점, 0바이트 파일 5점 |

## 9. 사람이 직접 확인해야 할 항목

- 참고문헌이 실제 존재하는지, DOI/URL/출판사 페이지가 정확한지 확인
- 논문 품질과 주차 주제 적합성 평가
- PDF 파일의 시각적 깨짐, 누락 페이지, 서식 문제 확인
- 실험 결과의 학술적 해석, 재현 가능성, 데이터/코드 타당성 검토
- AI 활용 고지의 사실관계와 최종 책임 확인
"""
    AUDIT_REPORT.write_text(content, encoding="utf-8")


def backup_existing_audit() -> str:
    if not AUDIT_REPORT.exists():
        return "기존 감사 보고서 없음"
    if not AUDIT_BACKUP.exists():
        shutil.copy2(AUDIT_REPORT, AUDIT_BACKUP)
        return rel(AUDIT_BACKUP)
    return f"{rel(AUDIT_BACKUP)} (기존 백업 유지)"


def main() -> int:
    WEEKLY_ROOT.mkdir(exist_ok=True)
    backup_note = backup_existing_audit()
    audits = [audit_week(week, folder, topic) for week, folder, topic in WEEKS]
    changes: dict[str, object] = {
        "generated_at": GENERATED_AT,
        "audit_backup": backup_note,
        "created_dirs": [path for audit in audits for path in audit.created_dirs],
        "created_keep_files": [path for audit in audits for path in audit.created_keep_files],
        "readme_created": [f"03_weekly_reports/{audit.folder}/README.md" for audit in audits if audit.readme_created],
        "readme_updated": [f"03_weekly_reports/{audit.folder}/README.md" for audit in audits if audit.readme_updated],
    }
    write_status_csv(audits)
    write_status_json(audits, changes)
    write_status_md(audits, changes)
    write_audit_report(audits, changes)

    broken_count = sum(len(audit.broken_links) for audit in audits)
    zero_count = sum(len(audit.zero_byte_files) for audit in audits)
    print(f"Weekly audit completed: {len(audits)} weeks")
    print(f"Status: {rel(STATUS_MD)}, {rel(STATUS_CSV)}, {rel(STATUS_JSON)}")
    print(f"Audit report: {rel(AUDIT_REPORT)}")
    print(f"Audit backup: {backup_note}")
    print(f"Broken relative links: {broken_count}")
    print(f"Zero-byte files: {zero_count}")
    for audit in audits:
        print(f"{audit.week}: {audit.total_score}/100")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
