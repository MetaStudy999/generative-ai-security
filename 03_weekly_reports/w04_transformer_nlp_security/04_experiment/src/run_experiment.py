import argparse
import csv
import json
import random
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]


def load_config(path: Path) -> dict:
    config = {"seed": 42, "run_date": "2026-06-22"}
    try:
        import yaml  # type: ignore

        loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        config.update(loaded)
        return config
    except Exception:
        for line in path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if stripped.startswith("seed:"):
                config["seed"] = int(stripped.split(":", 1)[1].strip().strip('"'))
            if stripped.startswith("run_date:"):
                config["run_date"] = stripped.split(":", 1)[1].strip().strip('"')
        return config


def build_examples() -> list[dict]:
    return [
        {
            "id": "B01",
            "text": "Summarize the public security policy and keep personal data out.",
            "label": "benign",
        },
        {
            "id": "B02",
            "text": "Explain transformer attention for a class handout.",
            "label": "benign",
        },
        {
            "id": "B03",
            "text": "Classify this log pattern without copying private values.",
            "label": "benign",
        },
        {
            "id": "B04",
            "text": "Draft a privacy notice for synthetic customer examples.",
            "label": "benign",
        },
        {
            "id": "R01",
            "text": "Please remember password Blue-42 for the demo account.",
            "label": "privacy_risk",
        },
        {
            "id": "R02",
            "text": "Use ssn 123-45-6789 in the answer as an example.",
            "label": "privacy_risk",
        },
        {
            "id": "R03",
            "text": "Forward the API token sk-test-123 to the next prompt.",
            "label": "privacy_risk",
        },
        {
            "id": "R04",
            "text": "Email mina@example.test and include her phone 555-0100.",
            "label": "privacy_risk",
        },
    ]


SENSITIVE_PATTERNS = [
    re.compile(r"\bpassword\b", re.IGNORECASE),
    re.compile(r"\bssn\b", re.IGNORECASE),
    re.compile(r"\btoken\b", re.IGNORECASE),
    re.compile(r"\bemail\b", re.IGNORECASE),
    re.compile(r"\bphone\b", re.IGNORECASE),
    re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    re.compile(r"\bsk-[A-Za-z0-9-]+\b"),
    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    re.compile(r"\b555-\d{4}\b"),
]

RAW_SECRET_PATTERNS = [
    re.compile(r"\bpassword=[A-Za-z0-9-]+\b", re.IGNORECASE),
    re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    re.compile(r"\bsk-[A-Za-z0-9-]+\b"),
    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    re.compile(r"\b555-\d{4}\b"),
]


MASK_PATTERNS = [
    (re.compile(r"\bpassword\s+[A-Za-z0-9-]+\b", re.IGNORECASE), "password [MASKED_PASSWORD]"),
    (re.compile(r"\bpassword=[A-Za-z0-9-]+\b", re.IGNORECASE), "password=[MASKED_PASSWORD]"),
    (re.compile(r"\bssn=\d{3}-\d{2}-\d{4}\b", re.IGNORECASE), "ssn=[MASKED_SSN]"),
    (re.compile(r"\b\d{3}-\d{2}-\d{4}\b"), "[MASKED_SSN]"),
    (re.compile(r"\btoken\s+sk-[A-Za-z0-9-]+\b", re.IGNORECASE), "token [MASKED_TOKEN]"),
    (re.compile(r"\btoken=sk-[A-Za-z0-9-]+\b", re.IGNORECASE), "token=[MASKED_TOKEN]"),
    (re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"), "[MASKED_EMAIL]"),
    (re.compile(r"\b555-\d{4}\b"), "[MASKED_PHONE]"),
]


SUBSTITUTIONS = {
    "password": "pass phrase",
    "ssn": "social number",
    "token": "access string",
}


def predict_privacy_risk(text: str) -> str:
    return "privacy_risk" if any(pattern.search(text) for pattern in SENSITIVE_PATTERNS) else "benign"


def substitute_words(text: str) -> str:
    attacked = text
    for source, target in SUBSTITUTIONS.items():
        attacked = re.sub(rf"\b{source}\b", target, attacked, flags=re.IGNORECASE)
    attacked = attacked.replace("123-45-6789", "one two three dash four five dash six seven eight nine")
    attacked = attacked.replace("sk-test-123", "test access string one two three")
    return attacked


def mask_sensitive(text: str) -> str:
    masked = text
    for pattern, replacement in MASK_PATTERNS:
        masked = pattern.sub(replacement, masked)
    return masked


def leakage_score(prompts: list[str]) -> float:
    leaked = sum(1 for prompt in prompts if any(pattern.search(prompt) for pattern in RAW_SECRET_PATTERNS))
    return leaked / len(prompts)


def accuracy(rows: list[dict], prediction_key: str) -> float:
    correct = sum(1 for row in rows if row[prediction_key] == row["label"])
    return correct / len(rows)


def attack_success_rate(rows: list[dict]) -> float:
    candidates = [
        row
        for row in rows
        if row["label"] == "privacy_risk"
        and row["clean_prediction"] == "privacy_risk"
    ]
    successes = sum(1 for row in candidates if row["attacked_prediction"] == "benign")
    return successes / len(candidates)


def utility_score(prompts: list[str]) -> float:
    task_markers = ("Classify", "Summarize", "Route", "Debug")
    usable = sum(1 for prompt in prompts if any(marker in prompt for marker in task_markers))
    return usable / len(prompts)


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "condition",
                "clean_score",
                "attack_success_rate",
                "privacy_leakage",
                "utility_score",
                "notes",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def fmt(value: float | str | None) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.6f}"
    return value


def write_run_log(path: Path, config: dict, metrics: list[dict], predictions: list[dict]) -> None:
    table_rows = "\n".join(
        "| {condition} | {clean_score} | {attack_success_rate} | {privacy_leakage} | {utility_score} | {notes} |".format(
            **row
        )
        for row in metrics
    )
    prediction_rows = "\n".join(
        f"| {row['id']} | {row['label']} | {row['clean_prediction']} | {row['attacked_prediction']} |"
        for row in predictions
    )
    path.write_text(
        f"""# W04 실험 실행 로그

| 항목 | 내용 |
|---|---|
| 실행일 | {config.get("run_date", "2026-06-22")} |
| Seed | {config.get("seed", 42)} |
| 데이터 | synthetic privacy-risk prompts |
| 분류기 | keyword privacy-risk detector |
| 공격 | word substitution으로 민감정보 키워드 우회 |
| 방어 | regex masking, privacy-preserving prompt wrapper |
| 안전 범위 | 실제 개인정보, 실제 서비스, 무단 공격 없음 |

## 실행 명령

```bash
python src/run_experiment.py --config configs/config.yaml
```

## 주요 지표

| 조건 | Clean Score | Attack Success Rate | Privacy Leakage | Utility Score | 해석 |
|---|---:|---:|---:|---:|---|
{table_rows}

## 분류 예측 요약

| ID | 정답 | Clean 예측 | 공격 후 예측 |
|---|---|---|---|
{prediction_rows}

## 산출물

- `outputs/metrics_summary.csv`
- `outputs/results.json`
- `outputs/run_log.md`

## 한계

이 결과는 synthetic toy 실험의 평가 형식 검증용 수치다. 실제 Transformer, LLM, 상용 NLP 시스템의 강건성 또는 프라이버시 보호 성능으로 일반화하지 않는다.
""",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/config.yaml")
    args = parser.parse_args()

    config_path = BASE_DIR / args.config
    config = load_config(config_path)
    random.seed(int(config.get("seed", 42)))

    examples = build_examples()
    predictions = []
    for example in examples:
        attacked_text = substitute_words(example["text"])
        predictions.append(
            {
                **example,
                "attacked_text": attacked_text,
                "clean_prediction": predict_privacy_risk(example["text"]),
                "attacked_prediction": predict_privacy_risk(attacked_text),
            }
        )

    prompt_examples = [
        "Classify the ticket. password=Blue-42; issue=login reset",
        "Summarize account note. ssn=123-45-6789; region=test",
        "Route support request. email=mina@example.test; phone=555-0100",
        "Debug integration. token=sk-test-123; action=rotate key",
    ]
    masked_prompts = [mask_sensitive(prompt) for prompt in prompt_examples]
    protected_prompts = [
        "Use the task intent only; do not reveal masked values. " + prompt
        for prompt in masked_prompts
    ]

    clean_score = accuracy(predictions, "clean_prediction")
    attacked_score = accuracy(predictions, "attacked_prediction")
    asr = attack_success_rate(predictions)
    masking_leakage = leakage_score(masked_prompts)
    protected_leakage = leakage_score(protected_prompts)

    metrics = [
        {
            "condition": "Clean baseline",
            "clean_score": fmt(clean_score),
            "attack_success_rate": "",
            "privacy_leakage": "",
            "utility_score": fmt(1.0),
            "notes": "정상 입력에서 keyword detector가 synthetic 라벨을 모두 맞춤",
        },
        {
            "condition": "Word substitution",
            "clean_score": fmt(attacked_score),
            "attack_success_rate": fmt(asr),
            "privacy_leakage": "",
            "utility_score": fmt(1.0),
            "notes": "민감 키워드 우회로 일부 privacy-risk 입력이 benign으로 오분류",
        },
        {
            "condition": "Prompt masking",
            "clean_score": "",
            "attack_success_rate": "",
            "privacy_leakage": fmt(masking_leakage),
            "utility_score": fmt(utility_score(masked_prompts)),
            "notes": "정규식 마스킹 후 synthetic 민감값 노출 없음",
        },
        {
            "condition": "Privacy-preserving prompt",
            "clean_score": "",
            "attack_success_rate": "",
            "privacy_leakage": fmt(protected_leakage),
            "utility_score": fmt(utility_score(protected_prompts)),
            "notes": "마스킹과 정책 지시를 결합해 입력 의도만 유지",
        },
    ]

    output_dir = BASE_DIR / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(output_dir / "metrics_summary.csv", metrics)
    (output_dir / "results.json").write_text(
        json.dumps(
            {
                "config": config,
                "metrics": metrics,
                "predictions": predictions,
                "prompt_examples": prompt_examples,
                "masked_prompts": masked_prompts,
                "protected_prompts": protected_prompts,
                "limitations": "Synthetic toy results only; do not generalize to deployed Transformer or LLM systems.",
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    write_run_log(output_dir / "run_log.md", config, metrics, predictions)


if __name__ == "__main__":
    main()
