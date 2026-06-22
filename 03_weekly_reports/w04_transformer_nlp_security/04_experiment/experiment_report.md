# 실험 보고서

## 1. 실험 목표

W04 실습은 Transformer 변형 및 NLP 대적공격/프라이버시의 보안 평가를 안전한 toy 환경에서 실행하고, 정상 입력 성능, 단어 치환 공격 영향, 프롬프트 마스킹 효과를 분리해 기록하는 것이다. 실제 시스템 침해나 실제 개인정보 사용은 제외한다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker |
| Python | 3.11 기준, 호스트 검증은 Python 3로 실행 |
| Seed | 42 |
| 데이터 | synthetic privacy-risk prompts |
| 결과 상태 | 실행 완료 |

## 3. 실행 절차

| 단계 | 설계 내용 | 결과 기록 |
|---|---|---|
| 간단한 텍스트 분류 예제 구성 | keyword privacy-risk detector | Clean Score 1.000000 |
| 단어 치환 공격 | `password`, `ssn`, `token` 표현을 우회 표현으로 치환 | Attack Success Rate 0.750000 |
| Clean score와 attack success rate 비교 | 정상 입력과 공격 입력을 분리 평가 | 공격 후 score 0.625000 |
| 프롬프트 프라이버시 위험 사례 정리 | synthetic password, ssn, email, phone, token 예시 | 실제 개인정보 없음 |
| 민감정보 마스킹 또는 프롬프트 정책 적용 전후 비교 | regex masking + privacy-preserving prompt wrapper | Privacy Leakage 0.000000 |
| 결과 파일 생성 | CSV, JSON, run log 저장 | `outputs/`에 보존 |

## 4. 결과

정량값은 `outputs/run_log.md`, `outputs/metrics_summary.csv`, `outputs/results.json` 기준이다.

| 조건 | Clean Score | Attack Success Rate | Privacy Leakage | Utility Score | 해석 |
|---|---:|---:|---:|---:|---|
| Clean baseline | 1.000000 | 해당 없음 | 해당 없음 | 1.000000 | 정상 입력에서 keyword detector가 synthetic 라벨을 모두 맞춤 |
| Word substitution | 0.625000 | 0.750000 | 해당 없음 | 1.000000 | 민감 키워드 우회로 일부 privacy-risk 입력이 benign으로 오분류 |
| Prompt masking | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 | 정규식 마스킹 후 synthetic 민감값 노출 없음 |
| Privacy-preserving prompt | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 | 마스킹과 정책 지시를 결합해 입력 의도만 유지 |

## 5. 예측 요약

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

## 6. 재현성 점검

- `configs/config.yaml`에 seed, 데이터, 실험 조건, 실행 상태를 기록했다.
- `src/run_experiment.py`는 synthetic 데이터만 사용하며, `python src/run_experiment.py --config configs/config.yaml`로 재실행할 수 있다.
- Dockerfile 내부 uv sync와 pyproject.toml로 컨테이너 실행 환경을 고정했다.
- 결과값은 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`에 같은 값으로 저장했다.

## 7. 한계

본 실습은 학습 목적의 synthetic toy 실험이다. 실제 Transformer, LLM, 상용 NLP 시스템의 강건성 또는 프라이버시 보호 성능으로 일반화하지 않는다. 실제 서비스, 실제 개인정보, 무단 공격 절차는 포함하지 않는다.
