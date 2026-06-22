# 실험 보고서

## 1. 실험 목표

W07 실습은 LLM 보안·프라이버시 평가 프로토콜을 안전한 toy 환경에서 검증하는 것이다. 실제 LLM, 외부 API, 실제 개인정보, 실제 jailbreak 재현은 사용하지 않고 synthetic prompt category와 rule-based guard score simulator만 사용했다.

핵심 질문은 “LLM 시스템 평가에서 정상 유용성, 공격 성공률, privacy leakage, refusal quality, code security risk를 한 표에 함께 기록할 수 있는가”이다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker 사용 가능, 호스트 `python3` 실행 검증 |
| Python | 3.11 계열 또는 호스트 `python3` |
| Seed | 42 |
| 데이터 | synthetic prompt categories, no personal data |
| 실행 명령 | `python3 src/run_experiment.py --config configs/config.yaml` |
| 결과 상태 | 실행 완료 |

## 3. 실행 절차

| 단계 | 설계 내용 | 결과 기록 |
|---|---|---|
| Synthetic prompt category 생성 | clean, prompt attack simulation, privacy-risk, code security 조건별 40개 | 총 160개 synthetic sample |
| Guard score simulator 적용 | risk score가 0.55 이상이면 refusal 처리 | answer rate, over-refusal 기록 |
| 보안 조건 평가 | 공격 절차 없이 추상 카테고리로 ASR과 refusal quality 계산 | `metrics_summary.csv` 저장 |
| 프라이버시 조건 평가 | 실제 개인정보 없이 leakage flag를 모의 | privacy leakage rate 기록 |
| 코드 보안 조건 평가 | 취약 코드 생성 내용 없이 vulnerability risk flag만 모의 | code vulnerability rate 기록 |
| 결과 근거 보존 | CSV, JSON, run log 생성 | `outputs/`에 저장 |

## 4. 결과

정량값은 `outputs/run_log.md`, `outputs/metrics_summary.csv`, `outputs/results.json`과 일치한다.

| 조건 | Utility | Answer rate | ASR | Privacy Leakage | Refusal Quality | Over-refusal | Code vuln. rate | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Clean prompts | 0.866746 | 1.000000 | 0.000000 | 0.000000 | 해당 없음 | 0.000000 | 0.000000 | 정상 질의에서 유용성과 과차단이 양호함 |
| Prompt attack simulation | 0.400908 | 0.150000 | 0.150000 | 0.000000 | 0.850000 | 0.000000 | 0.000000 | 추상 공격 카테고리의 85%를 refusal 처리 |
| Privacy-risk prompts | 0.392926 | 0.100000 | 0.100000 | 0.025000 | 0.900000 | 0.000000 | 0.000000 | 민감정보 요청 카테고리의 leakage가 낮게 기록됨 |
| Code security prompts | 0.678267 | 0.650000 | 0.000000 | 0.000000 | 해당 없음 | 0.350000 | 0.200000 | 코드 보안 조건에서 취약 코드 위험과 과차단이 함께 나타남 |

## 5. 해석

Clean prompts에서는 utility가 0.866746이고 answer rate가 1.000000으로 정상 질의가 차단되지 않았다. 반대로 prompt attack simulation과 privacy-risk prompts에서는 refusal quality가 각각 0.850000, 0.900000으로 나타나 guard가 위험 조건을 대부분 차단하는 구조를 보였다.

Code security prompts에서는 code vulnerability rate가 0.200000이고 over-refusal rate가 0.350000이었다. 이는 코드 생성형 LLM 평가에서 “취약 코드 억제”와 “정상 보안 코딩 지원의 과차단”을 함께 봐야 함을 보여준다.

## 6. 재현성 점검

- `configs/config.yaml`에 seed, condition별 sample 수, guard threshold, 안전 범위를 기록했다.
- `src/run_experiment.py`는 CSV/JSON/run log를 모두 생성한다.
- 실행 산출물은 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`에 보존했다.
- 실제 jailbreak 문구, 실제 개인정보, 외부 API 질의, 무단 서비스 테스트는 포함하지 않았다.

## 7. 한계

본 실습은 LLM 보안 평가표와 재현성 기록 구조를 설명하기 위한 synthetic toy 실험이다. 실제 LLM의 보안 성능, 실제 prompt-injection 성공률, 실제 개인정보 누출 가능성, 실제 코드 보안 품질로 일반화하지 않는다.
