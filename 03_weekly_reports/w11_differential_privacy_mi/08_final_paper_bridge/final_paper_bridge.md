# W11 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | AI 보안 연구에서 privacy claim을 검증하기 위한 다중지표 평가 프레임워크 | ML/DL 학습 시스템 | Membership inference, privacy leakage, DP misuse | 문헌분석 + toy 실험 + 체크리스트 | 높음 |
| 2 | DP-SGD/DP-like 방어의 utility-privacy trade-off 보고 기준 연구 | DP 적용 모델 | 과도한 epsilon, accountant 누락, utility degradation | accuracy/MI/leakage/accounting 표준 보고 | 높음 |
| 3 | 멤버십 추론 관점의 AI privacy risk threat model | 모델 API와 평가 로그 | membership information 노출 | 위협모형 + synthetic evaluation protocol | 높음 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | AI 모델 학습에서 privacy protection과 utility trade-off를 동시에 평가해야 하는 문제의식 |
| 관련연구 | DP misuse, centralized DP-DL, MI attack/defense survey, FL 확장 관련 보조 문헌. 단 P03/P05는 지정 논문 원문 확보 전까지 관련 논문 PDF로 분리 |
| 연구문제 | privacy claim 검증을 위한 utility, MI risk, leakage, accounting, reproducibility의 결합 |
| 연구방법 | synthetic toy 실험, threat model, DOI/PDF 검증표, seed/config/output log |
| 분석/실험 | outputs 기준 baseline accuracy 0.956250, DP-like high utility drop 0.006250, medium leakage score 0.011769 비교 |
| 보안적 함의 | DP claim accountability, 실제 개인정보/운영 API 제외 원칙 |
| 결론 | 재현 가능한 privacy evaluation reporting checklist 제안 |

## 3. W11에서 바로 가져갈 표

| 평가 항목 | W11 지표 | 기말논문 활용 |
|---|---|---|
| Utility | Accuracy, Utility Drop | 모델 효용 손실 분석 |
| Membership Risk | MI Attack Accuracy | privacy risk proxy |
| Leakage | Privacy Leakage Score | confidence gap 기반 leakage 해석 |
| Privacy Claim | Epsilon Proxy / formal epsilon 구분 | `epsilon_proxy`가 formal accountant 값이 아님을 명시 |
| Reproducibility | seed, config, CSV/JSON/log | 실험 재현성 장 |

## 4. 최종 논문 전환 시 검증 필요

- P03/P05 지정 논문 원문 PDF 또는 공식 출판 페이지를 확보한다.
- public GitHub 저장소에 PDF 원문을 올릴 경우 저작권 위험을 검토하고, 원칙적으로 DOI/URL과 서지정보만 남긴다.
- W11 toy 결과는 formal DP-SGD나 실제 개인정보 보호 수준으로 일반화하지 않는다.

<!-- AUTO-WEEKLY-BRIDGE-CHECK:start -->
## 자동 보완: 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: 차등프라이버시(DP) & 멤버십 추론 공격·방어의 핵심 개념을 LLM/RAG 시스템 생명주기별 위협·통제 항목으로 반영한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: 주차별 실험표, metrics_summary.csv 기반 그래프, config/seed/run_log 재현성 증거를 표·그림 후보로 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: 문서 오염, 프롬프트/컨텍스트 변조, 모델·운영 로그 감사 항목을 분리하는 LLM 보안 감사 체크포인트와 연결된다.
<!-- AUTO-WEEKLY-BRIDGE-CHECK:end -->
