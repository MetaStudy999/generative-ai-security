import argparse
import csv
import json
import random
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[1]


DEFAULT_CONFIG = {
    "week": "W09",
    "topic": "심층강화학습(DRL) & 사이버보안 적용·보상조작",
    "seed": 42,
    "run_date": "2026-06-22",
    "status": "executed",
    "data": {
        "type": "synthetic_toy_cyber_defense",
        "personal_data": False,
        "train_steps": 5000,
        "eval_steps": 600,
    },
    "experiment": {
        "algorithm": "tabular_q_learning",
        "learning_rate": 0.18,
        "discount": 0.90,
        "epsilon_start": 0.35,
        "epsilon_end": 0.04,
    },
    "security_scope": {
        "allowed": "toy cyber-defense state/action/reward simulation",
        "disallowed": "actual system compromise, personal data use, live network traffic, unauthorized attack automation",
    },
}


ACTIONS = ["monitor", "isolate", "patch", "escalate"]


CONDITIONS = {
    "normal_reward": {
        "label": "Normal reward",
        "notes": "탐지 성능과 운영 비용을 균형 있게 둔 기준 보상",
    },
    "manipulated_reward": {
        "label": "Manipulated reward",
        "notes": "공격 이벤트 미대응 패널티가 약화되고 자동 격리 비용이 과장된 조작 보상",
    },
    "robust_reward_design": {
        "label": "Robust reward design",
        "notes": "보상 클리핑, 안전 위반 패널티, 불확실 상태의 escalation을 포함한 보상",
    },
}


def deep_update(base: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    for key, value in incoming.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            deep_update(base[key], value)
        else:
            base[key] = value
    return base


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


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def variance(values: list[float]) -> float:
    avg = mean(values)
    return mean([(value - avg) ** 2 for value in values])


def safe_div(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def f1_score(tp: int, fp: int, fn: int) -> float:
    precision = safe_div(tp, tp + fp)
    recall = safe_div(tp, tp + fn)
    return safe_div(2 * precision * recall, precision + recall)


def fmt(value: float | int | str | bool | None) -> str:
    if value is None:
        return "해당 없음"
    if isinstance(value, float):
        return f"{value:.6f}"
    return str(value)


def sample_event(rng: random.Random, perturbed: bool = False) -> dict[str, Any]:
    asset_critical = 1 if rng.random() < 0.45 else 0
    vulnerable = 1 if rng.random() < 0.50 else 0
    attack_probability = 0.16 + (0.11 * asset_critical) + (0.12 * vulnerable)
    attack = rng.random() < attack_probability

    if attack:
        alert = 2 if rng.random() < 0.74 else 1
    else:
        alert = 1 if rng.random() < 0.24 else 0

    if perturbed:
        if attack and alert == 2 and rng.random() < 0.35:
            alert = 1
        elif attack and alert == 1 and rng.random() < 0.20:
            alert = 0
        elif not attack and alert == 0 and rng.random() < 0.15:
            alert = 1

    state = (alert, asset_critical, vulnerable)
    return {
        "state": state,
        "attack": attack,
        "alert": alert,
        "asset_critical": asset_critical,
        "vulnerable": vulnerable,
    }


def true_reward(event: dict[str, Any], action: str) -> float:
    attack = bool(event["attack"])
    critical = bool(event["asset_critical"])
    vulnerable = bool(event["vulnerable"])

    if attack:
        if action == "monitor":
            return -2.9 if critical else -2.2
        if action == "isolate":
            return 2.6 if critical else 2.0
        if action == "patch":
            return 1.6 if vulnerable else 0.5
        if action == "escalate":
            return 1.8 if critical else 1.3
    else:
        if action == "monitor":
            return 0.9
        if action == "isolate":
            return -1.4 if critical else -1.0
        if action == "patch":
            return 0.35 if vulnerable else -0.25
        if action == "escalate":
            return -0.15
    return 0.0


def observed_reward(event: dict[str, Any], action: str, condition_key: str) -> float:
    reward = true_reward(event, action)

    if condition_key == "normal_reward":
        return reward

    if condition_key == "manipulated_reward":
        if event["attack"]:
            if action == "monitor":
                return 0.4
            if action == "isolate":
                return 0.1
            if action == "patch":
                return 0.55
            if action == "escalate":
                return 0.0
        else:
            if action == "monitor":
                return 1.0
            if action == "isolate":
                return -2.4
            if action == "patch":
                return -0.2
            if action == "escalate":
                return -0.7

    if condition_key == "robust_reward_design":
        clipped = max(-2.5, min(2.5, reward))
        if safety_violation(event, action):
            clipped -= 1.2
        if event["alert"] == 1 and action == "escalate":
            clipped += 0.45
        if event["attack"] and action == "monitor":
            clipped -= 0.8
        return clipped

    return reward


def safety_violation(event: dict[str, Any], action: str) -> bool:
    if event["attack"] and action == "monitor":
        return True
    if not event["attack"] and action == "isolate":
        return True
    if event["attack"] and event["asset_critical"] and action == "patch" and event["alert"] == 2:
        return True
    return False


def choose_action(q_table: dict[tuple[int, int, int], list[float]], state: tuple[int, int, int], epsilon: float, rng: random.Random) -> int:
    if state not in q_table:
        q_table[state] = [0.0 for _ in ACTIONS]
    if rng.random() < epsilon:
        return rng.randrange(len(ACTIONS))
    values = q_table[state]
    best_value = max(values)
    best_actions = [i for i, value in enumerate(values) if value == best_value]
    return rng.choice(best_actions)


def train(condition_key: str, config: dict[str, Any], rng: random.Random) -> tuple[dict[tuple[int, int, int], list[float]], list[float]]:
    steps = int(config["data"].get("train_steps", 5000))
    alpha = float(config["experiment"].get("learning_rate", 0.18))
    gamma = float(config["experiment"].get("discount", 0.90))
    epsilon_start = float(config["experiment"].get("epsilon_start", 0.35))
    epsilon_end = float(config["experiment"].get("epsilon_end", 0.04))

    q_table: dict[tuple[int, int, int], list[float]] = {}
    rewards: list[float] = []
    current_event = sample_event(rng)

    for step in range(steps):
        progress = step / max(1, steps - 1)
        epsilon = epsilon_start + (epsilon_end - epsilon_start) * progress
        state = current_event["state"]
        action_index = choose_action(q_table, state, epsilon, rng)
        action = ACTIONS[action_index]
        reward = observed_reward(current_event, action, condition_key)
        rewards.append(reward)

        next_event = sample_event(rng)
        next_state = next_event["state"]
        if next_state not in q_table:
            q_table[next_state] = [0.0 for _ in ACTIONS]
        target = reward + gamma * max(q_table[next_state])
        q_table[state][action_index] += alpha * (target - q_table[state][action_index])
        current_event = next_event

    return q_table, rewards


def greedy_action(q_table: dict[tuple[int, int, int], list[float]], state: tuple[int, int, int]) -> str:
    values = q_table.get(state)
    if values is None:
        return "monitor"
    best_value = max(values)
    best_actions = [i for i, value in enumerate(values) if value == best_value]
    return ACTIONS[best_actions[0]]


def evaluate_policy(
    condition_key: str,
    q_table: dict[tuple[int, int, int], list[float]],
    config: dict[str, Any],
    rng: random.Random,
    perturbed: bool = False,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    steps = int(config["data"].get("eval_steps", 600))
    rows: list[dict[str, Any]] = []
    true_rewards: list[float] = []
    observed_rewards: list[float] = []
    tp = fp = fn = 0
    safety_count = 0

    for index in range(steps):
        event = sample_event(rng, perturbed=perturbed)
        action = greedy_action(q_table, event["state"])
        predicted_attack = action in {"isolate", "patch", "escalate"}
        actual_attack = bool(event["attack"])

        if predicted_attack and actual_attack:
            tp += 1
        elif predicted_attack and not actual_attack:
            fp += 1
        elif not predicted_attack and actual_attack:
            fn += 1

        violation = safety_violation(event, action)
        safety_count += int(violation)
        objective_reward = true_reward(event, action)
        learned_reward = observed_reward(event, action, condition_key)
        true_rewards.append(objective_reward)
        observed_rewards.append(learned_reward)

        if index < 20:
            rows.append(
                {
                    "id": f"{condition_key}_{'perturbed' if perturbed else 'clean'}_{index:03d}",
                    "condition_key": condition_key,
                    "condition": CONDITIONS[condition_key]["label"],
                    "state": str(event["state"]),
                    "attack": actual_attack,
                    "action": action,
                    "true_reward": objective_reward,
                    "observed_reward": learned_reward,
                    "safety_violation": violation,
                    "perturbed": perturbed,
                }
            )

    metrics = {
        "condition": CONDITIONS[condition_key]["label"],
        "sample_count": steps,
        "average_reward": mean(true_rewards),
        "observed_reward": mean(observed_rewards),
        "detection_f1": f1_score(tp, fp, fn),
        "safety_violation_rate": safe_div(safety_count, steps),
        "reward_variance": variance(true_rewards),
        "true_positive": tp,
        "false_positive": fp,
        "false_negative": fn,
        "notes": CONDITIONS[condition_key]["notes"],
    }
    return metrics, rows


def run_experiment(config: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    seed = int(config.get("seed", 42))
    metrics: list[dict[str, Any]] = []
    training: list[dict[str, Any]] = []
    sample_rows: list[dict[str, Any]] = []

    for offset, condition_key in enumerate(CONDITIONS):
        train_rng = random.Random(seed + offset * 100)
        eval_rng = random.Random(seed + offset * 100 + 1)
        perturb_rng = random.Random(seed + offset * 100 + 2)
        q_table, train_rewards = train(condition_key, config, train_rng)
        clean_metrics, rows = evaluate_policy(condition_key, q_table, config, eval_rng, perturbed=False)
        perturbed_metrics, perturbed_rows = evaluate_policy(condition_key, q_table, config, perturb_rng, perturbed=True)
        clean_metrics["policy_robustness"] = perturbed_metrics["average_reward"]
        clean_metrics["perturbed_detection_f1"] = perturbed_metrics["detection_f1"]
        clean_metrics["perturbed_safety_violation_rate"] = perturbed_metrics["safety_violation_rate"]
        metrics.append(clean_metrics)
        sample_rows.extend(rows[:8])
        sample_rows.extend(perturbed_rows[:4])
        training.append(
            {
                "condition": CONDITIONS[condition_key]["label"],
                "training_reward_mean": mean(train_rewards),
                "training_reward_variance": variance(train_rewards),
                "q_table": {"|".join(map(str, key)): value for key, value in sorted(q_table.items())},
            }
        )

    return metrics, training, sample_rows


def write_metrics_csv(path: Path, metrics: list[dict[str, Any]]) -> None:
    fieldnames = [
        "condition",
        "sample_count",
        "average_reward",
        "observed_reward",
        "detection_f1",
        "safety_violation_rate",
        "policy_robustness",
        "perturbed_detection_f1",
        "perturbed_safety_violation_rate",
        "reward_variance",
        "true_positive",
        "false_positive",
        "false_negative",
        "notes",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in metrics:
            writer.writerow({key: fmt(row.get(key)) for key in fieldnames})


def write_results_json(
    path: Path,
    config: dict[str, Any],
    metrics: list[dict[str, Any]],
    training: list[dict[str, Any]],
    sample_rows: list[dict[str, Any]],
) -> None:
    path.write_text(
        json.dumps(
            {
                "config": config,
                "actions": ACTIONS,
                "conditions": CONDITIONS,
                "metrics": metrics,
                "training": training,
                "sample_rows": sample_rows,
                "safety_note": "Synthetic toy environment only; no live network traffic, exploit execution, personal data, or real system action was used.",
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def write_run_log(path: Path, config: dict[str, Any], metrics: list[dict[str, Any]], sample_rows: list[dict[str, Any]]) -> None:
    metric_rows = "\n".join(
        "| {condition} | {sample_count} | {average_reward} | {detection_f1} | {safety_violation_rate} | {policy_robustness} | {perturbed_detection_f1} | {perturbed_safety_violation_rate} | {reward_variance} | {notes} |".format(
            condition=row["condition"],
            sample_count=fmt(row["sample_count"]),
            average_reward=fmt(row["average_reward"]),
            detection_f1=fmt(row["detection_f1"]),
            safety_violation_rate=fmt(row["safety_violation_rate"]),
            policy_robustness=fmt(row["policy_robustness"]),
            perturbed_detection_f1=fmt(row["perturbed_detection_f1"]),
            perturbed_safety_violation_rate=fmt(row["perturbed_safety_violation_rate"]),
            reward_variance=fmt(row["reward_variance"]),
            notes=row["notes"],
        )
        for row in metrics
    )
    sample_table_rows = "\n".join(
        f"| {row['id']} | {row['condition']} | {row['state']} | {row['attack']} | {row['action']} | {fmt(row['true_reward'])} | {fmt(row['observed_reward'])} | {row['safety_violation']} | {row['perturbed']} |"
        for row in sample_rows[:18]
    )

    path.write_text(
        f"""# W09 실험 실행 로그

| 항목 | 내용 |
|---|---|
| 실행일 | {config.get("run_date", "2026-06-22")} |
| Seed | {config.get("seed", 42)} |
| 데이터 | synthetic toy cyber-defense states, no personal data |
| 모델 | tabular Q-learning toy DRL agent |
| 학습 스텝 | 조건별 {config.get("data", {}).get("train_steps", 5000)} |
| 평가 샘플 | 조건별 {config.get("data", {}).get("eval_steps", 600)} |
| 제외 범위 | 실제 시스템 침해, 실제 네트워크 트래픽, 개인정보, 무단 공격 자동화 |

## 지표 요약

| 조건 | N | Average Reward | Detection F1 | Safety Violation Rate | Policy Robustness | Perturbed F1 | Perturbed Safety Violation | Reward Variance | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
{metric_rows}

## 샘플 로그

| ID | 조건 | 상태(alert, critical, vulnerable) | 공격 이벤트 | 선택 행동 | True Reward | Observed Reward | Safety Violation | Perturbed |
|---|---|---|---|---|---:|---:|---|---|
{sample_table_rows}

## 해석 메모

- Normal reward는 탐지 이익과 대응 비용을 균형 있게 반영한 기준 조건이다.
- Manipulated reward는 보상 신호가 왜곡될 때 정책이 낮은 비용 행동으로 치우치는지를 확인하는 조건이다.
- Robust reward design은 안전 위반 패널티와 불확실 상태의 escalation 보상을 추가해 보상조작 영향을 줄이는 조건이다.
- Perturbed 지표는 관측 alert가 일부 낮아지거나 높아지는 상태 조작 상황에서 같은 정책을 평가한 결과다.
- 모든 입력은 synthetic toy state이며 실제 공격 payload, 실제 개인정보, live network traffic은 포함하지 않았다.
""",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=BASE_DIR / "configs" / "config.yaml")
    parser.add_argument("--output-dir", type=Path, default=BASE_DIR / "outputs")
    args = parser.parse_args()

    config = load_config(args.config)
    metrics, training, sample_rows = run_experiment(config)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_metrics_csv(args.output_dir / "metrics_summary.csv", metrics)
    write_results_json(args.output_dir / "results.json", config, metrics, training, sample_rows)
    write_run_log(args.output_dir / "run_log.md", config, metrics, sample_rows)

    print(f"Wrote {args.output_dir / 'metrics_summary.csv'}")
    print(f"Wrote {args.output_dir / 'results.json'}")
    print(f"Wrote {args.output_dir / 'run_log.md'}")


if __name__ == "__main__":
    main()
