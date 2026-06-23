from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.generate_formula_visual_supplements import BASE, WEEKS, write_text  # noqa: E402


REPORT_PATH = ROOT / "reports" / "presentation_visual_audit.md"
COMMON_CSS = ROOT / "02_report_templates" / "nature_research_slide_style.css"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def pass_fail(condition: bool) -> str:
    return "PASS" if condition else "FAIL"


def pass_warn(condition: bool) -> str:
    return "PASS" if condition else "WARN"


def count_sections(html: str) -> int:
    return len(re.findall(r"<section\b", html, flags=re.IGNORECASE))


def has_chart(html: str, presentation_dir: Path) -> bool:
    assets = presentation_dir / "assets"
    asset_charts = list(assets.glob("**/*.svg")) + list(assets.glob("**/*.png"))
    return bool(
        re.search(r"<svg\b|<canvas\b|assets/[^\"']+\.(?:svg|png)|chart|figure", html, flags=re.IGNORECASE)
        or asset_charts
    )


def has_diagram(html: str, presentation_dir: Path) -> bool:
    assets = presentation_dir / "assets"
    asset_diagrams = list((assets / "diagrams").glob("*.svg"))
    return bool(
        re.search(r"diagram|pipeline|threat-map|flow|<svg\b", html, flags=re.IGNORECASE)
        or asset_diagrams
    )


def nav_right_bottom(html: str, css: str) -> bool:
    combined = f"{html}\n{css}"
    return all(
        [
            ".slide-nav" in combined,
            re.search(r"right\s*:\s*24px", combined),
            re.search(r"bottom\s*:\s*24px", combined),
            "prevSlide" in html,
            "nextSlide" in html,
            "slideCounter" in html,
            "keydown" in html,
        ]
    )


def notes_bundle_status(presentation_dir: Path) -> str:
    required = ["speaker_notes.md", "qna.md", "one_page_handout.md"]
    if all((presentation_dir / name).exists() for name in required):
        return "PASS"
    return "FAIL"


def nature_style_status(html: str) -> tuple[str, list[str]]:
    checks = {
        "header": "journal-kicker" in html or "slide-header" in html,
        "caption": "figure-caption" in html,
        "panel": "panel-label" in html or "figure-panel" in html,
        "question": "research-question" in html,
        "limitation": "limitation" in html.lower() or "검증 상태" in html,
    }
    warnings: list[str] = []
    if not all(checks.values()):
        missing = ", ".join(name for name, ok in checks.items() if not ok)
        warnings.append(f"Nature-style missing: {missing}")

    for idx, section in enumerate(re.findall(r"<section\b.*?</section>", html, flags=re.DOTALL | re.IGNORECASE), start=1):
        bullets = len(re.findall(r"<li\b", section, flags=re.IGNORECASE))
        if bullets > 5:
            warnings.append(f"Slide {idx} has {bullets} bullet items")

    if re.search(r"Nature\s+logo|nature\.com|official\s+Nature", html, flags=re.IGNORECASE):
        warnings.append("Possible Nature trademark/logo reference")

    return ("PASS" if not warnings else "WARN"), warnings


def audit_week(config: dict[str, object]) -> dict[str, object]:
    week = str(config["week"])
    slug = str(config["slug"])
    week_dir = BASE / slug
    presentation_dir = week_dir / "09_presentation"
    html_path = presentation_dir / "presentation_slides.html"
    html = read(html_path)
    css = read(COMMON_CSS)
    metrics_path = week_dir / "04_experiment" / "outputs" / "metrics_summary.csv"

    slides = count_sections(html)
    formula = bool(re.search(r"MathJax|formula-card|\\\[|\\\(|\$\$", html))
    table = "<table" in html.lower()
    chart = has_chart(html, presentation_dir)
    diagram = has_diagram(html, presentation_dir)
    nav = nav_right_bottom(html, css)
    notes = notes_bundle_status(presentation_dir)
    nature, nature_warnings = nature_style_status(html)

    warnings: list[str] = []
    warnings.extend(nature_warnings)
    if metrics_path.exists() and not chart:
        warnings.append("metrics_summary.csv exists but chart was not found")
    if not metrics_path.exists() and chart:
        warnings.append("chart-like asset exists without metrics_summary.csv; verify design_only status")

    core_fail = [
        html_path.exists(),
        slides >= 10,
        formula,
        table,
        diagram,
        nav,
        notes == "PASS",
    ]
    if not all(core_fail):
        status = "FAIL"
    elif warnings:
        status = "WARN"
    else:
        status = "PASS"

    return {
        "week": week,
        "slides": slides,
        "formula": pass_fail(formula),
        "table": pass_fail(table),
        "chart": "PASS" if chart else ("FAIL" if metrics_path.exists() else "WARN"),
        "diagram": pass_fail(diagram),
        "nature": nature,
        "nav": pass_fail(nav),
        "notes": notes,
        "status": status,
        "warnings": warnings,
    }


def make_report(results: list[dict[str, object]]) -> str:
    lines = [
        "# Presentation Visual Audit",
        "",
        "| Week | Slides | Formula | Table | Chart | Diagram | Nature-style | Nav Right-Bottom | Notes/QNA/Handout | Status |",
        "|---|---:|---|---|---|---|---|---|---|---|",
    ]
    for result in results:
        lines.append(
            "| {week} | {slides} | {formula} | {table} | {chart} | {diagram} | {nature} | {nav} | {notes} | {status} |".format(
                **result
            )
        )
    warning_lines = []
    for result in results:
        for warning in result["warnings"]:
            warning_lines.append(f"- {result['week']}: {warning}")
    lines.extend(["", "## Warnings", ""])
    if warning_lines:
        lines.extend(warning_lines)
    else:
        lines.append("- 없음")
    lines.extend(
        [
            "",
            "## Audit Rules",
            "",
            "- `presentation_slides.html` exists and has at least 10 sections.",
            "- Formula, table, chart/figure, diagram/pipeline, right-bottom `.slide-nav`, keyboard navigation, and support files are present.",
            "- If `metrics_summary.csv` exists, chart assets or chart references must exist.",
            "- Nature-style checks require research question, figure caption, panel label, and limitation/verification state.",
            "- The audit flags possible external Nature trademark/logo references instead of requiring any such asset.",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    results = [audit_week(config) for config in WEEKS]
    write_text(REPORT_PATH, make_report(results))
    print("Presentation visual audit")
    for result in results:
        print(
            "{week}: slides={slides} formula={formula} table={table} chart={chart} diagram={diagram} nav={nav} status={status}".format(
                **result
            )
        )
    print(f"Report: {REPORT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
