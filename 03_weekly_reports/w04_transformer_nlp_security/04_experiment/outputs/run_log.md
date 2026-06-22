# W04 실험 실행 로그

| 항목 | 내용 |
|---|---|
| 실행일 | 2026-06-22 |
| Seed | 42 |
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
| Clean baseline | 1.000000 |  |  | 1.000000 | 정상 입력에서 keyword detector가 synthetic 라벨을 모두 맞춤 |
| Word substitution | 0.625000 | 0.750000 |  | 1.000000 | 민감 키워드 우회로 일부 privacy-risk 입력이 benign으로 오분류 |
| Prompt masking |  |  | 0.000000 | 1.000000 | 정규식 마스킹 후 synthetic 민감값 노출 없음 |
| Privacy-preserving prompt |  |  | 0.000000 | 1.000000 | 마스킹과 정책 지시를 결합해 입력 의도만 유지 |

## 분류 예측 요약

| ID | 정답 | Clean 예측 | 공격 후 예측 |
|---|---|---|---|
| B01 | benign | benign | benign |
| B02 | benign | benign | benign |
| B03 | benign | benign | benign |
| B04 | benign | benign | benign |
| R01 | privacy_risk | privacy_risk | benign |
| R02 | privacy_risk | privacy_risk | benign |
| R03 | privacy_risk | privacy_risk | benign |
| R04 | privacy_risk | privacy_risk | privacy_risk |

## 산출물

- `outputs/metrics_summary.csv`
- `outputs/results.json`
- `outputs/run_log.md`

## 한계

이 결과는 synthetic toy 실험의 평가 형식 검증용 수치다. 실제 Transformer, LLM, 상용 NLP 시스템의 강건성 또는 프라이버시 보호 성능으로 일반화하지 않는다.
