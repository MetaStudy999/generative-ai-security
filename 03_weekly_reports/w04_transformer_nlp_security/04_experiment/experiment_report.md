# 실험 보고서

## 1. 실험 목표

W04 실습은 실제 Transformer 또는 LLM 공격 재현이 아니라 W04의 핵심인 프롬프트 프라이버시 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. synthetic 프라이버시 위험 프롬프트와 keyword privacy-risk detector를 사용해 clean score, attack success rate, privacy leakage, utility score, reproducibility evidence를 분리 기록한다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker |
| Python | 3.11 기준, 호스트 검증은 Python 3로 실행 |
| Seed | 42 |
| 데이터 | synthetic privacy-risk prompts |
| 분류기 | keyword privacy-risk detector |
| 결과 상태 | outputs 파일 생성 확인 |

## 3. 실행 절차

| 단계 | 설계 내용 | 결과 기록 |
|---|---|---|
| Clean baseline | keyword privacy-risk detector로 정상 synthetic 입력 평가 | Clean Score 1.000000 |
| Word substitution | `password`, `ssn`, `token` 표현을 우회 표현으로 치환 | Attack Success Rate 0.750000 |
| 공격 후 clean score 비교 | 정상 입력과 공격 입력을 분리 평가 | 공격 후 Clean Score 0.625000 |
| Prompt masking | synthetic password, ssn, email, phone, token 예시를 정규식 마스킹 | Privacy Leakage 0.000000 |
| Privacy-preserving prompt wrapper | 마스킹된 입력에 정책 지시문 결합 | Privacy Leakage 0.000000 |
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

- `configs/config.yaml`에 seed, run date, 데이터, 실험 조건, 실행 상태, 안전 범위를 기록했다.
- PyYAML이 설치되어 있으면 코드가 YAML 전체를 읽어 `results.json`에 중첩 설정까지 보존한다. PyYAML이 없으면 `seed`와 `run_date`만 fallback으로 읽는다.
- `pyproject.toml`은 현재 코드가 실제 사용하는 `pyyaml`만 의존성으로 둔다.
- `docker-compose.yml` 기본 command는 `bash`이며, 실험 자동 실행은 `docker compose run --rm w04-transformer-nlp-security python src/run_experiment.py --config configs/config.yaml` 명령을 사용한다.
- 현재 호스트에서는 `python` 명령이 없어 `python3 src/run_experiment.py --config configs/config.yaml`로 로컬 실행을 확인했고, Docker Compose 실행도 성공했다.
- 결과값은 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`에 같은 값으로 저장했다.

## 7. 한계

이 결과는 synthetic toy 실험의 평가 형식 검증용 수치이며, 실제 Transformer, LLM, 상용 NLP 시스템의 강건성 또는 프라이버시 보호 성능으로 일반화하지 않는다. Prompt masking leakage 0.000000은 synthetic regex check에서 원시 민감값 패턴이 남지 않았다는 의미일 뿐 실제 개인정보보호 보증이 아니다.
