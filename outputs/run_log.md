# Run Log

## Environment

- run_timestamp_utc: 2026-06-23T11:23:49.474378+00:00
- python: 3.12.3
- platform: Linux-6.18.33.1-microsoft-standard-WSL2-x86_64-with-glibc2.39
- os_name: posix
- seed: 42
- dataset: data/rag_security_dataset_100.csv
- data_policy: all records are synthetic; no real personal data or real credentials

## Commands

```bash
python3 experiments/run_baseline_no_filter.py
python3 experiments/run_baseline_keyword.py
python3 experiments/run_baseline_regex.py
python3 experiments/run_proposed_framework.py
python3 experiments/evaluate_metrics.py
```

## Dataset

- path: data/rag_security_dataset_100.csv
- rows: 100
- hallucination_trigger: 10
- indirect_prompt_injection: 20
- normal: 20
- outdated_policy: 15
- privacy_leakage: 20
- source_conflict: 15

## Metrics Summary

| method | precision | recall | f1_score | fpr | prevention | leakage | review |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline_no_filter | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 |
| baseline_keyword | 1.000000 | 0.500000 | 0.666667 | 0.000000 | 0.500000 | 0.000000 | 0.000000 |
| baseline_regex | 1.000000 | 0.250000 | 0.400000 | 0.000000 | 0.250000 | 0.000000 | 0.000000 |
| rag_docguard | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | 0.400000 |

## Interpretation Boundary

이 결과는 synthetic 문서와 규칙 기반 판정기로 생성한 재현성 검증용 수치이다. 실제 기업 RAG 시스템, 실제 LLM, 실제 개인정보, 실제 공격 성공률로 일반화하지 않는다.
