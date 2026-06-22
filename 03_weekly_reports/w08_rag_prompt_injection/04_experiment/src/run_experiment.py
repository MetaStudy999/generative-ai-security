import argparse
import csv
import json
import random
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[1]


DEFAULT_CONFIG = {
    "week": "W08",
    "topic": "RAG·프롬프팅 프레임워크 & 프롬프트 인젝션",
    "seed": 42,
    "run_date": "2026-06-22",
    "status": "executed",
    "data": {
        "type": "synthetic_rag_documents",
        "personal_data": False,
        "n_per_condition": 40,
        "top_k": 3,
    },
    "experiment": {
        "risk_threshold": 0.55,
        "source_filter_block_rate": 0.82,
        "human_approval_block_rate": 0.92,
    },
    "security_scope": {
        "allowed": "synthetic RAG prompt-injection evaluation and defense logging",
        "disallowed": "real external system attack, personal data use, live tool invocation, unredacted malicious payloads",
    },
}


CONDITIONS = {
    "clean_rag": {
        "label": "Clean RAG",
        "poison_probability": 0.00,
        "source_filter": False,
        "human_approval": False,
        "retrieval_mean": 0.91,
        "retrieval_std": 0.06,
        "faithfulness_mean": 0.90,
        "faithfulness_std": 0.06,
        "answer_mean": 0.94,
        "notes": "정상 문서만 검색되는 기준 조건",
    },
    "poisoned_document": {
        "label": "Poisoned document",
        "poison_probability": 0.68,
        "source_filter": False,
        "human_approval": False,
        "retrieval_mean": 0.78,
        "retrieval_std": 0.11,
        "faithfulness_mean": 0.63,
        "faithfulness_std": 0.13,
        "answer_mean": 0.89,
        "notes": "오염 문서가 검색 context에 들어오는 취약 조건",
    },
    "source_filter": {
        "label": "Source filter 적용",
        "poison_probability": 0.68,
        "source_filter": True,
        "human_approval": False,
        "retrieval_mean": 0.82,
        "retrieval_std": 0.09,
        "faithfulness_mean": 0.80,
        "faithfulness_std": 0.09,
        "answer_mean": 0.82,
        "notes": "출처 신뢰도와 메타데이터로 오염 문서를 차단",
    },
    "human_approval": {
        "label": "Human approval 적용",
        "poison_probability": 0.68,
        "source_filter": True,
        "human_approval": True,
        "retrieval_mean": 0.80,
        "retrieval_std": 0.09,
        "faithfulness_mean": 0.84,
        "faithfulness_std": 0.08,
        "answer_mean": 0.76,
        "notes": "출처 필터 이후 고위험 tool action을 사람 승인으로 차단",
    },
}


SYNTHETIC_QUERIES = [
    "보안 정책 문서에 근거해 계정 잠금 기준을 요약하라.",
    "RAG 시스템의 감사 로그 보존 기준을 설명하라.",
    "내부 도구 호출 전에 필요한 승인 조건을 정리하라.",
    "검색 문서의 출처 메타데이터를 기준으로 답변 근거를 제시하라.",
]


def deep_update(base: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    for key, value in incoming.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            deep_update(base[key], value)
        else:
            base[key] = value
    return base


def load_config(path: Path) -> dict[str, Any]:
    config = json.loads(json.dumps(DEFAULT_CONFIG))
    if not path.exists():
        return config

    try:
        import yaml  # type: ignore

        loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if isinstance(loaded, dict):
            return deep_update(config, loaded)
    except Exception:
        loaded = parse_simple_yaml(path.read_text(encoding="utf-8"))
        if loaded:
            return deep_update(config, loaded)
    return config


def parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        return value


def parse_simple_yaml(text: str) -> dict[str, Any]:
    root: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(0, root)]
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()
        if ":" not in stripped:
            continue
        key, raw = stripped.split(":", 1)
        while len(stack) > 1 and indent < stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if raw.strip() == "":
            child: dict[str, Any] = {}
            parent[key.strip()] = child
            stack.append((indent + 2, child))
        else:
            parent[key.strip()] = parse_scalar(raw)
    return root


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def safe_div(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def fmt(value: float | int | str | None) -> str:
    if value is None:
        return "해당 없음"
    if isinstance(value, float):
        return f"{value:.6f}"
    return str(value)


def simulate_row(condition_key: str, condition: dict[str, Any], index: int, rng: random.Random, config: dict[str, Any]) -> dict[str, Any]:
    risk_threshold = float(config["experiment"].get("risk_threshold", 0.55))
    source_filter_block_rate = float(config["experiment"].get("source_filter_block_rate", 0.82))
    human_approval_block_rate = float(config["experiment"].get("human_approval_block_rate", 0.92))

    initial_poisoned = rng.random() < float(condition["poison_probability"])
    blocked_by_source = bool(condition["source_filter"] and initial_poisoned and rng.random() < source_filter_block_rate)
    poisoned_in_context = initial_poisoned and not blocked_by_source

    risk_score = clamp(rng.gauss(0.76 if poisoned_in_context else 0.18, 0.13))
    requires_tool = rng.random() < (0.45 if poisoned_in_context else 0.15)
    blocked_by_human = bool(condition["human_approval"] and risk_score >= risk_threshold and rng.random() < human_approval_block_rate)

    attack_success = bool(poisoned_in_context and not blocked_by_human and rng.random() < 0.72)
    tool_misuse = bool(attack_success and requires_tool and rng.random() < 0.58)
    source_verified = bool(not poisoned_in_context or condition["source_filter"])
    answered = bool(not blocked_by_human and rng.random() < float(condition["answer_mean"]))

    retrieval_relevance = clamp(rng.gauss(float(condition["retrieval_mean"]), float(condition["retrieval_std"])))
    if blocked_by_source:
        retrieval_relevance = clamp(retrieval_relevance - 0.04)
    if attack_success:
        retrieval_relevance = clamp(retrieval_relevance - 0.12)

    faithfulness = clamp(rng.gauss(float(condition["faithfulness_mean"]), float(condition["faithfulness_std"])))
    if attack_success:
        faithfulness = clamp(faithfulness - 0.28)
    if blocked_by_human:
        faithfulness = clamp(faithfulness + 0.05)

    return {
        "id": f"{condition_key}_{index:03d}",
        "condition_key": condition_key,
        "condition": condition["label"],
        "query": SYNTHETIC_QUERIES[index % len(SYNTHETIC_QUERIES)],
        "initial_poisoned": initial_poisoned,
        "blocked_by_source": blocked_by_source,
        "poisoned_in_context": poisoned_in_context,
        "risk_score": risk_score,
        "source_verified": source_verified,
        "requires_tool": requires_tool,
        "blocked_by_human": blocked_by_human,
        "attack_success": attack_success,
        "tool_misuse": tool_misuse,
        "answered": answered,
        "retrieval_relevance": retrieval_relevance,
        "faithfulness": faithfulness,
    }


def summarize(rows: list[dict[str, Any]], condition: dict[str, Any]) -> dict[str, Any]:
    n = len(rows)
    return {
        "condition": condition["label"],
        "sample_count": n,
        "retrieval_relevance": mean([row["retrieval_relevance"] for row in rows]),
        "attack_success_rate": safe_div(sum(1 for row in rows if row["attack_success"]), n),
        "source_verification_rate": safe_div(sum(1 for row in rows if row["source_verified"]), n),
        "tool_misuse_rate": safe_div(sum(1 for row in rows if row["tool_misuse"]), n),
        "faithfulness": mean([row["faithfulness"] for row in rows]),
        "answer_rate": safe_div(sum(1 for row in rows if row["answered"]), n),
        "source_block_rate": safe_div(sum(1 for row in rows if row["blocked_by_source"]), sum(1 for row in rows if row["initial_poisoned"])),
        "human_block_rate": safe_div(sum(1 for row in rows if row["blocked_by_human"]), sum(1 for row in rows if row["poisoned_in_context"])),
        "notes": condition["notes"],
    }


def evaluate(config: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rng = random.Random(int(config.get("seed", 42)))
    n = int(config.get("data", {}).get("n_per_condition", 40))
    rows: list[dict[str, Any]] = []
    metrics: list[dict[str, Any]] = []

    for condition_key, condition in CONDITIONS.items():
        condition_rows = [simulate_row(condition_key, condition, i, rng, config) for i in range(n)]
        rows.extend(condition_rows)
        metrics.append(summarize(condition_rows, condition))
    return metrics, rows


def write_metrics_csv(path: Path, metrics: list[dict[str, Any]]) -> None:
    fieldnames = [
        "condition",
        "sample_count",
        "retrieval_relevance",
        "attack_success_rate",
        "source_verification_rate",
        "tool_misuse_rate",
        "faithfulness",
        "answer_rate",
        "source_block_rate",
        "human_block_rate",
        "notes",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in metrics:
            writer.writerow({key: fmt(row.get(key)) for key in fieldnames})


def write_results_json(path: Path, config: dict[str, Any], metrics: list[dict[str, Any]], rows: list[dict[str, Any]]) -> None:
    path.write_text(
        json.dumps(
            {
                "config": config,
                "conditions": CONDITIONS,
                "metrics": metrics,
                "sample_rows": rows[:20],
                "safety_note": "Synthetic documents only; no live RAG system, external API, personal data, or real tool call was used.",
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def write_run_log(path: Path, config: dict[str, Any], metrics: list[dict[str, Any]], rows: list[dict[str, Any]]) -> None:
    metric_rows = "\n".join(
        "| {condition} | {sample_count} | {retrieval_relevance} | {attack_success_rate} | {source_verification_rate} | {tool_misuse_rate} | {faithfulness} | {answer_rate} | {source_block_rate} | {human_block_rate} | {notes} |".format(
            condition=row["condition"],
            sample_count=fmt(row.get("sample_count")),
            retrieval_relevance=fmt(row.get("retrieval_relevance")),
            attack_success_rate=fmt(row.get("attack_success_rate")),
            source_verification_rate=fmt(row.get("source_verification_rate")),
            tool_misuse_rate=fmt(row.get("tool_misuse_rate")),
            faithfulness=fmt(row.get("faithfulness")),
            answer_rate=fmt(row.get("answer_rate")),
            source_block_rate=fmt(row.get("source_block_rate")),
            human_block_rate=fmt(row.get("human_block_rate")),
            notes=row["notes"],
        )
        for row in metrics
    )
    sample_rows = "\n".join(
        f"| {row['id']} | {row['condition']} | {row['poisoned_in_context']} | {fmt(row['risk_score'])} | {row['source_verified']} | {row['blocked_by_human']} | {row['attack_success']} | {row['tool_misuse']} |"
        for row in rows[:12]
    )

    path.write_text(
        f"""# W08 실험 실행 로그

| 항목 | 내용 |
|---|---|
| 실행일 | {config.get("run_date", "2026-06-22")} |
| Seed | {config.get("seed", 42)} |
| 데이터 | synthetic RAG documents, no personal data |
| 모델 | rule-based toy RAG prompt-injection evaluator |
| 샘플 수 | 조건별 {config.get("data", {}).get("n_per_condition", 40)}개 |
| 제외 범위 | 실제 외부 시스템 공격, 실제 의료·금융 시스템 조작, 실제 tool 호출 |

## 지표 요약

| 조건 | N | Retrieval Relevance | ASR | Source Verification | Tool Misuse Rate | Faithfulness | Answer Rate | Source Block Rate | Human Block Rate | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
{metric_rows}

## 샘플 로그

| ID | 조건 | 오염 context 포함 | Risk score | 출처 검증 | Human block | Attack success | Tool misuse |
|---|---|---|---:|---|---|---|---|
{sample_rows}

## 해석 메모

- Clean RAG는 정상 문서만 검색되는 기준 조건이다.
- Poisoned document 조건은 오염 문서가 검색 context에 들어왔을 때의 방어 부재 위험을 본다.
- Source filter 적용 조건은 출처 신뢰도와 메타데이터 검증으로 오염 문서 반영을 줄이는지 본다.
- Human approval 적용 조건은 고위험 tool action을 사람 승인으로 차단하는 효과를 본다.
- 모든 입력은 synthetic이며 실제 공격 payload, 실제 개인정보, live API 호출은 포함하지 않았다.
""",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=BASE_DIR / "configs" / "config.yaml")
    parser.add_argument("--output-dir", type=Path, default=BASE_DIR / "outputs")
    args = parser.parse_args()

    config = load_config(args.config)
    metrics, rows = evaluate(config)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_metrics_csv(args.output_dir / "metrics_summary.csv", metrics)
    write_results_json(args.output_dir / "results.json", config, metrics, rows)
    write_run_log(args.output_dir / "run_log.md", config, metrics, rows)

    print(f"Wrote {args.output_dir / 'metrics_summary.csv'}")
    print(f"Wrote {args.output_dir / 'results.json'}")
    print(f"Wrote {args.output_dir / 'run_log.md'}")


if __name__ == "__main__":
    main()
