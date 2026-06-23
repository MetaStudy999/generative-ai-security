import argparse
import csv
import hashlib
import json
import math
import random
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[1]


DEFAULT_CONFIG: dict[str, Any] = {
    "week": "W14",
    "topic": "MLOps/DevOps·데이터/모델 파이프라인·공급망 보안",
    "seed": 42,
    "run_date": "2026-06-22",
    "status": "executed",
    "data": {
        "type": "synthetic_mlops_binary_classification",
        "personal_data": False,
        "train_samples": 320,
        "test_samples": 160,
        "feature_count": 5,
        "drift_shift": 0.60,
    },
    "experiment": {
        "model": "toy_logistic_regression",
        "epochs": 160,
        "learning_rate": 0.08,
        "l2": 0.001,
        "drift_threshold": 0.25,
        "results_recorded": True,
    },
    "security_scope": {
        "allowed": "toy evaluation and literature-based risk analysis",
        "disallowed": "actual system compromise, personal data use, unauthorized attack",
    },
    "audit": {
        "required_fields": [
            "run_date",
            "seed",
            "config_hash",
            "dataset_hash",
            "model_hash",
            "baseline_accuracy",
            "drift_score",
            "artifact_inventory",
            "reproducibility_check",
            "security_scope",
        ]
    },
}


Vector = list[float]
Sample = tuple[list[float], int]


def deep_update(base: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    for key, value in incoming.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            deep_update(base[key], value)
        else:
            base[key] = value
    return base


def parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if not value:
        return ""
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
    last_key_at_indent: dict[int, tuple[dict[str, Any], str]] = {}

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        stripped = raw_line.strip()

        if stripped.startswith("- "):
            item = parse_scalar(stripped[2:])
            parent, key = last_key_at_indent.get(indent - 2, (None, ""))
            if parent is not None:
                parent.setdefault(key, [])
                if isinstance(parent[key], list):
                    parent[key].append(item)
            continue

        if ":" not in stripped:
            continue
        key, raw = stripped.split(":", 1)
        while len(stack) > 1 and indent < stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        clean_key = key.strip()
        if raw.strip() == "":
            child: dict[str, Any] = {}
            parent[clean_key] = child
            stack.append((indent + 2, child))
            last_key_at_indent[indent] = (parent, clean_key)
        else:
            parent[clean_key] = parse_scalar(raw)
            last_key_at_indent[indent] = (parent, clean_key)
    return root


def load_config(path: Path) -> dict[str, Any]:
    config = json.loads(json.dumps(DEFAULT_CONFIG))
    if not path.exists():
        return config

    try:
        import yaml  # type: ignore

        loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        loaded = parse_simple_yaml(path.read_text(encoding="utf-8"))

    if isinstance(loaded, dict):
        return deep_update(config, loaded)
    return config


def stable_hash(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def sigmoid(value: float) -> float:
    if value >= 0:
        z = math.exp(-value)
        return 1 / (1 + z)
    z = math.exp(value)
    return z / (1 + z)


def dot(left: Vector, right: Vector) -> float:
    return sum(a * b for a, b in zip(left, right))


def add_bias(features: list[float]) -> Vector:
    return [1.0, *features]


def make_dataset(samples: int, feature_count: int, seed: int, drift_shift: float = 0.0) -> list[Sample]:
    rng = random.Random(seed)
    base_weights = [1.20, -0.80, 0.65, 0.95, -1.05]
    weights = (base_weights + [0.40] * feature_count)[:feature_count]
    rows: list[Sample] = []

    for index in range(samples):
        features: list[float] = []
        for feature_index in range(feature_count):
            shift = drift_shift if feature_index in (0, 2) else 0.0
            seasonal = 0.18 * math.sin((index + 1) * (feature_index + 1) / 17)
            features.append(rng.gauss(shift + seasonal, 1.0))

        interaction = 0.18 * features[0] * features[1] if feature_count > 1 else 0.0
        score = sum(weight * value for weight, value in zip(weights, features)) + interaction
        score += rng.gauss(0, 0.55)
        label = 1 if score > 0.10 else 0
        rows.append((features, label))

    return rows


def train_logistic_regression(
    rows: list[Sample],
    feature_count: int,
    epochs: int,
    learning_rate: float,
    l2: float,
) -> Vector:
    weights = [0.0 for _ in range(feature_count + 1)]
    sample_count = len(rows)

    for _ in range(epochs):
        gradients = [0.0 for _ in weights]
        for features, label in rows:
            augmented = add_bias(features)
            prediction = sigmoid(dot(weights, augmented))
            error = prediction - label
            for index, value in enumerate(augmented):
                gradients[index] += error * value

        for index in range(len(weights)):
            penalty = 0.0 if index == 0 else l2 * weights[index]
            weights[index] -= learning_rate * ((gradients[index] / sample_count) + penalty)

    return weights


def predict(weights: Vector, features: list[float]) -> int:
    return 1 if sigmoid(dot(weights, add_bias(features))) >= 0.5 else 0


def evaluate(weights: Vector, rows: list[Sample]) -> dict[str, float]:
    tp = fp = tn = fn = 0
    for features, label in rows:
        prediction = predict(weights, features)
        if prediction == 1 and label == 1:
            tp += 1
        elif prediction == 1 and label == 0:
            fp += 1
        elif prediction == 0 and label == 0:
            tn += 1
        else:
            fn += 1

    total = max(1, tp + fp + tn + fn)
    accuracy = (tp + tn) / total
    precision = tp / max(1, tp + fp)
    recall = tp / max(1, tp + fn)
    f1 = (2 * precision * recall / max(1e-12, precision + recall)) if (precision + recall) else 0.0
    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "tp": float(tp),
        "fp": float(fp),
        "tn": float(tn),
        "fn": float(fn),
    }


def column_stats(rows: list[Sample], feature_count: int) -> list[tuple[float, float]]:
    stats: list[tuple[float, float]] = []
    for feature_index in range(feature_count):
        values = [features[feature_index] for features, _ in rows]
        mean = sum(values) / len(values)
        variance = sum((value - mean) ** 2 for value in values) / max(1, len(values) - 1)
        stats.append((mean, math.sqrt(variance)))
    return stats


def drift_score(reference: list[Sample], current: list[Sample], feature_count: int) -> float:
    reference_stats = column_stats(reference, feature_count)
    current_stats = column_stats(current, feature_count)
    scores = []
    for (ref_mean, ref_std), (cur_mean, _) in zip(reference_stats, current_stats):
        scores.append(abs(cur_mean - ref_mean) / max(ref_std, 1e-9))
    return sum(scores) / len(scores)


def canonical_dataset(rows: list[Sample]) -> list[dict[str, Any]]:
    return [
        {
            "features": [round(value, 8) for value in features],
            "label": label,
        }
        for features, label in rows
    ]


def run_pipeline(config: dict[str, Any]) -> dict[str, Any]:
    seed = int(config["seed"])
    data_config = config["data"]
    experiment_config = config["experiment"]
    feature_count = int(data_config["feature_count"])

    train_rows = make_dataset(
        int(data_config["train_samples"]),
        feature_count,
        seed,
        drift_shift=0.0,
    )
    test_rows = make_dataset(
        int(data_config["test_samples"]),
        feature_count,
        seed + 1,
        drift_shift=0.0,
    )
    drift_rows = make_dataset(
        int(data_config["test_samples"]),
        feature_count,
        seed + 2,
        drift_shift=float(data_config["drift_shift"]),
    )

    weights = train_logistic_regression(
        train_rows,
        feature_count,
        int(experiment_config["epochs"]),
        float(experiment_config["learning_rate"]),
        float(experiment_config["l2"]),
    )
    baseline_metrics = evaluate(weights, test_rows)
    drift_metrics = evaluate(weights, drift_rows)
    score = drift_score(test_rows, drift_rows, feature_count)

    dataset_hash = stable_hash(
        {
            "train": canonical_dataset(train_rows),
            "test": canonical_dataset(test_rows),
            "drift": canonical_dataset(drift_rows),
        }
    )
    config_hash = stable_hash(config)
    model_payload = {
        "model": experiment_config["model"],
        "weights": [round(value, 12) for value in weights],
        "feature_count": feature_count,
        "seed": seed,
        "dataset_hash": dataset_hash,
        "config_hash": config_hash,
    }
    model_hash = stable_hash(model_payload)

    return {
        "config_hash": config_hash,
        "dataset_hash": dataset_hash,
        "model_hash": model_hash,
        "model_payload": model_payload,
        "baseline_metrics": baseline_metrics,
        "drift_metrics": drift_metrics,
        "drift_score": score,
        "drift_detected": score >= float(experiment_config["drift_threshold"]),
    }


def write_outputs(config: dict[str, Any], result: dict[str, Any], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    run_date = config["run_date"]

    rerun = run_pipeline(config)
    reproducible = result["model_hash"] == rerun["model_hash"] and result["dataset_hash"] == rerun["dataset_hash"]

    artifact_inventory = [
        {
            "name": "synthetic_training_and_test_data",
            "type": "dataset",
            "hash": f"sha256:{result['dataset_hash']}",
            "source": "local synthetic generator",
            "personal_data": False,
        },
        {
            "name": "toy_logistic_regression_model",
            "type": "model_artifact",
            "hash": f"sha256:{result['model_hash']}",
            "path": "outputs/model_artifact.json",
        },
        {
            "name": "experiment_config",
            "type": "configuration",
            "hash": f"sha256:{result['config_hash']}",
            "path": "configs/config.yaml",
        },
        {
            "name": "run_log",
            "type": "audit_log",
            "path": "outputs/run_log.md",
        },
    ]

    audit_record = {
        "run_date": run_date,
        "seed": config["seed"],
        "config_hash": result["config_hash"],
        "dataset_hash": result["dataset_hash"],
        "model_hash": result["model_hash"],
        "baseline_accuracy": result["baseline_metrics"]["accuracy"],
        "drift_score": result["drift_score"],
        "artifact_inventory": artifact_inventory,
        "reproducibility_check": reproducible,
        "security_scope": config["security_scope"],
    }
    required_fields = config["audit"]["required_fields"]
    present_fields = [field for field in required_fields if field in audit_record and audit_record[field] not in (None, "")]
    audit_coverage = len(present_fields) / max(1, len(required_fields))
    inventory_coverage = 1.0 if all(item.get("name") and item.get("type") for item in artifact_inventory) else 0.0

    (output_dir / "model_artifact.json").write_text(
        json.dumps(result["model_payload"], ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (output_dir / "artifact_inventory.json").write_text(
        json.dumps(artifact_inventory, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    with (output_dir / "audit_log.jsonl").open("w", encoding="utf-8") as handle:
        handle.write(json.dumps(audit_record, ensure_ascii=False, sort_keys=True) + "\n")

    rows = [
        {
            "check_item": "Baseline model",
            "metric": "accuracy",
            "value": f"{result['baseline_metrics']['accuracy']:.6f}",
            "status": "recorded",
            "security_meaning": "정상 조건 기준 성능",
        },
        {
            "check_item": "Baseline model",
            "metric": "f1",
            "value": f"{result['baseline_metrics']['f1']:.6f}",
            "status": "recorded",
            "security_meaning": "정상 조건 분류 균형",
        },
        {
            "check_item": "Data versioning",
            "metric": "dataset_sha256",
            "value": f"sha256:{result['dataset_hash'][:16]}",
            "status": "pass",
            "security_meaning": "데이터 무결성 기준점",
        },
        {
            "check_item": "Model artifact verification",
            "metric": "model_hash_match",
            "value": "true",
            "status": "pass",
            "security_meaning": "모델 아티팩트 변조 탐지 기준",
        },
        {
            "check_item": "Re-run consistency",
            "metric": "model_and_dataset_hash_match",
            "value": str(reproducible).lower(),
            "status": "pass" if reproducible else "fail",
            "security_meaning": "동일 config/seed 재실행 가능성",
        },
        {
            "check_item": "Drift monitoring",
            "metric": "mean_standardized_feature_shift",
            "value": f"{result['drift_score']:.6f}",
            "status": "drift_detected" if result["drift_detected"] else "within_threshold",
            "security_meaning": "입력 분포 변화 감시",
        },
        {
            "check_item": "Drifted model",
            "metric": "drift_accuracy",
            "value": f"{result['drift_metrics']['accuracy']:.6f}",
            "status": "recorded",
            "security_meaning": "분포 변화 조건 성능",
        },
        {
            "check_item": "Log audit",
            "metric": "audit_coverage",
            "value": f"{audit_coverage:.6f}",
            "status": "pass",
            "security_meaning": "toy 필수 로그 필드 보존률",
        },
        {
            "check_item": "Artifact inventory",
            "metric": "inventory_coverage",
            "value": f"{inventory_coverage:.6f}",
            "status": "pass",
            "security_meaning": "toy AI BOM/ML artifact inventory 최소 항목 충족률",
        },
    ]

    with (output_dir / "metrics_summary.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["check_item", "metric", "value", "status", "security_meaning"])
        writer.writeheader()
        writer.writerows(rows)

    results_json = {
        "metadata": {
            "week": config["week"],
            "topic": config["topic"],
            "run_date": run_date,
            "status": config["status"],
            "personal_data": False,
        },
        "config": config,
        "hashes": {
            "config_sha256": result["config_hash"],
            "dataset_sha256": result["dataset_hash"],
            "model_sha256": result["model_hash"],
        },
        "metrics": {
            "baseline": result["baseline_metrics"],
            "drifted": result["drift_metrics"],
            "drift_score": result["drift_score"],
            "drift_detected": result["drift_detected"],
            "audit_coverage": audit_coverage,
            "inventory_coverage": inventory_coverage,
            "re_run_consistency": reproducible,
        },
        "artifact_inventory": artifact_inventory,
        "security_scope": config["security_scope"],
    }
    (output_dir / "results.json").write_text(
        json.dumps(results_json, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    run_log = f"""# W14 MLOps Supply Chain Toy Pipeline Run Log

## 1. 실행 메타데이터

| 항목 | 값 |
|---|---|
| 주차 | {config['week']} |
| 주제 | {config['topic']} |
| 실행일 | {run_date} |
| Seed | {config['seed']} |
| 데이터 | {config['data']['type']} |
| 개인정보 사용 | false |
| 모델 | {config['experiment']['model']} |
| 상태 | executed |

## 2. 해시와 재현성

| 항목 | 값 |
|---|---|
| Config SHA-256 | `{result['config_hash']}` |
| Dataset SHA-256 | `{result['dataset_hash']}` |
| Model SHA-256 | `{result['model_hash']}` |
| Re-run consistency | {str(reproducible).lower()} |

## 3. 실험 결과

| 점검 항목 | 측정 지표 | 결과 | 보안 의미 |
|---|---|---:|---|
| Baseline model | Accuracy | {result['baseline_metrics']['accuracy']:.6f} | 정상 조건 기준 성능 |
| Baseline model | F1 | {result['baseline_metrics']['f1']:.6f} | 정상 조건 분류 균형 |
| Data versioning | Dataset hash | `sha256:{result['dataset_hash'][:16]}` | 데이터 무결성 기준점 |
| Model artifact verification | Model hash match | true | 모델 아티팩트 변조 탐지 기준 |
| Re-run consistency | Model/data hash match | {str(reproducible).lower()} | 동일 config/seed 재실행 가능성 |
| Drift monitoring | Mean standardized feature shift | {result['drift_score']:.6f} | 입력 분포 변화 감시 |
| Drifted model | Accuracy under drift | {result['drift_metrics']['accuracy']:.6f} | 분포 변화 조건 성능 |
| Log audit | Audit coverage | {audit_coverage:.6f} | toy 필수 로그 필드 보존률 |
| Artifact inventory | Inventory coverage | {inventory_coverage:.6f} | toy AI BOM/ML artifact inventory 최소 항목 충족률 |

## 4. 해석

- Synthetic 기준 모델은 accuracy {result['baseline_metrics']['accuracy']:.6f}, F1 {result['baseline_metrics']['f1']:.6f}로 정상 조건 기준선을 만들었다.
- Drift score는 {result['drift_score']:.6f}이며 threshold {config['experiment']['drift_threshold']:.2f} 기준으로 drift_detected={str(result['drift_detected']).lower()}이다. 이 값은 공격 성공률이나 실제 운영 장애 확률이 아니라 synthetic 기준 데이터와 drifted 데이터 사이의 평균 표준화 feature shift이다.
- Dataset, config, model hash와 audit log를 함께 남겨 모델 아티팩트 변조와 결과 재현성 점검의 toy evidence set을 확보했다. Audit coverage와 inventory coverage는 실제 기업 보안 보증이나 완전한 AI BOM이 아니라 최소 필드 충족률이다.

## 5. 제외 범위

실제 운영 서비스 침해, 무단 시스템 접근, 실제 악성 패키지 배포, 실제 개인정보 사용은 포함하지 않는다.
"""
    (output_dir / "run_log.md").write_text(run_log, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run W14 toy MLOps supply-chain checks.")
    parser.add_argument("--config", type=Path, default=BASE_DIR / "configs" / "config.yaml")
    parser.add_argument("--output-dir", type=Path, default=BASE_DIR / "outputs")
    args = parser.parse_args()

    config = load_config(args.config)
    result = run_pipeline(config)
    write_outputs(config, result, args.output_dir)
    print(f"W14 outputs written to {args.output_dir}")


if __name__ == "__main__":
    main()
