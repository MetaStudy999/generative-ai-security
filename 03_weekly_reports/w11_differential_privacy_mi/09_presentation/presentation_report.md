# W11 발표용 보고서

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W11 |
| 주제 | 차등프라이버시(DP) & 멤버십 추론 공격·방어 |
| 발표 시간 | 8-10분 |
| 권장 슬라이드 수 | 12장 |
| 핵심 메시지 | DP 보장은 선언이 아니라 accounting, utility, MI risk, leakage, 재현성 로그로 검증해야 한다. |
| 발표 근거 | `06_report/final/integrated_report_final.md`, `04_experiment/outputs/run_log.md` |

## 2. 한 문장 요약

W11는 DP-SGD와 privacy budget의 원리를 membership inference 위협모형으로 연결하고, synthetic toy 실험으로 accuracy, MI attack accuracy, leakage, utility drop을 같은 표에서 비교한다.

## 3. 발표 흐름

| 순서 | 슬라이드 주제 | 핵심 내용 | 시간 |
|---:|---|---|---:|
| 1 | 표지 | DP claim을 어떻게 검증할 것인가 | 0:30 |
| 2 | 왜 중요한가 | 학습 포함 여부 자체가 privacy risk | 0:50 |
| 3 | AI 원리 | DP, epsilon/delta, DP-SGD, accounting | 1:20 |
| 4 | 보안 이슈 | MI, confidence leakage, overfitting | 1:00 |
| 5 | 논문 5편 | DP misuse, DP-DL, MI taxonomy, defense | 1:00 |
| 6 | 위협모형 | 보호 자산, 공격자 관측, 제외 범위 | 0:55 |
| 7 | 평가 프로토콜 | utility, MI risk, leakage, accounting, logs | 1:00 |
| 8 | 실험 설계 | synthetic toy logistic regression | 1:00 |
| 9 | 실험 결과 | 4개 조건 비교표 | 1:10 |
| 10 | 해석 | noise가 항상 단조 개선을 보장하지 않음 | 0:50 |
| 11 | 기말 연결 | privacy claim 다중지표 평가 프레임워크 | 0:45 |
| 12 | 결론/Q&A | 수치는 로그가 있을 때만 주장 | 0:30 |

## 4. 논문 5편의 발표 역할

| ID | 논문 | 발표에서 맡는 역할 | DOI/URL 상태 |
|---|---|---|---|
| P01 | A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning | DP misuse와 reporting 책임 | DOI `10.1145/3547139` 확인 |
| P02 | Recent Advances of Differential Privacy in Centralized Deep Learning | DP-DL auditing과 privacy-utility 개선 | DOI `10.1145/3712000` 확인, 강의자료 표기 대조 필요 |
| P03 | Differential Privacy in Deep Learning: A Literature Survey | DP 적용 위치와 보호 대상 | DOI `10.1016/j.neucom.2024.127663` 확인, 로컬 PDF 대체 |
| P04 | Membership Inference Attacks on Machine Learning | MI attack taxonomy | DOI `10.1145/3523273` 확인 |
| P05 | Defenses to Membership Inference Attacks | defense taxonomy와 trade-off | DOI `10.1145/3620667` 확인, 로컬 PDF 대체 |

## 5. AI 원리 설명

- DP는 한 레코드 포함 여부가 출력 분포에 과도하게 드러나지 않도록 하는 privacy 정의다.
- DP-SGD는 gradient clipping, noise injection, privacy accounting이 함께 있어야 의미가 있다.
- Privacy budget은 작은 값일수록 강한 보호를 뜻하지만, 모델 utility와 비용을 함께 봐야 한다.

## 6. 보안 이슈 설명

| 항목 | 발표 내용 |
|---|---|
| 보호 자산 | membership information, confidence score, model output, evaluation log |
| 실패 조건 | 학습 포함 여부 추론, confidence leakage, 잘못된 DP claim |
| 평가 지표 | Accuracy, MI Attack Accuracy, Privacy Leakage Score, Utility Drop |
| 제외 범위 | 실제 개인정보, 실제 개인 대상 추론, 운영 모델/API 무단 질의 |

## 7. 실습/실험 결과

정량값은 `04_experiment/outputs/run_log.md` 기준이다.

| 조건 | Accuracy | MI Attack Accuracy | Epsilon Proxy | Utility Drop | Privacy Leakage Score |
|---|---:|---:|---:|---:|---:|
| Non-DP baseline | 0.956250 | 0.515625 | 해당 없음 | 0.000000 | 0.014833 |
| DP-like noise low | 0.956250 | 0.515625 | 8.000000 | 0.000000 | 0.014494 |
| DP-like noise medium | 0.962500 | 0.512500 | 3.000000 | 0.000000 | 0.011769 |
| DP-like noise high | 0.950000 | 0.521875 | 1.000000 | 0.006250 | 0.016482 |

## 8. 기말논문 연결

| 기말논문 장 | 발표에서 연결할 내용 |
|---|---|
| 서론 | AI 학습에서 privacy claim 검증 필요성 |
| 관련연구 | DP misuse, DP-DL, MI attack/defense survey |
| 연구문제 | 다중지표 privacy evaluation protocol |
| 연구방법 | synthetic toy 실험, 위협모형, 로그 기반 재현성 |
| 분석/실험 | accuracy, MI risk, leakage, utility drop |
| 보안적 함의 | accountability와 reference integrity |

## 9. 결론 메시지

1. DP는 noise를 넣었다는 말이 아니라 보장 조건과 accounting을 요구한다.
2. MI 위험은 accuracy와 다른 축이므로 별도 지표로 기록해야 한다.
3. `epsilon_proxy`와 toy 결과는 실제 DP 보장이 아니다.
4. W11은 기말논문의 privacy claim 평가 프레임워크로 연결된다.
5. P03/P05는 관련 논문 PDF 상태이므로 원문 확보 전까지 지정 논문처럼 인용하지 않는다.

## 10. 예상 질문과 답변

| 질문 | 답변 요지 | 근거 파일 |
|---|---|---|
| 왜 `epsilon_proxy`라고 썼나? | 정식 accountant 산출값이 아니므로 실제 epsilon처럼 말하지 않기 위해서다. | `04_experiment/experiment_report.md` |
| high noise가 MI risk를 낮추지 않은 이유는? | toy 설정에서는 random noise가 confidence 분포를 단조롭게 개선하지 않았다. 그래서 반복 실험과 formal accounting이 필요하다. | `04_experiment/outputs/run_log.md` |
| P03/P05는 왜 관련 논문 PDF인가? | 로컬 파일명이 `RELATED`이고 첫 페이지가 지정 논문과 다르다. | `01_papers/doi_check.md` |
| 실제 개인정보 실험인가? | 아니다. synthetic binary classification만 사용했다. | `04_experiment/outputs/run_log.md` |
