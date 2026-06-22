# W11 발표 예상 질문과 답변

## 기준

| 항목 | 내용 |
|---|---|
| 주차 | W11 |
| 주제 | 차등프라이버시(DP) & 멤버십 추론 공격·방어 |
| 발표 파일 | `presentation_report.md`, `presentation_slides.md` |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## Q1. 이번 주차의 핵심 질문은 무엇인가요?

답변: DP 보장을 주장할 때 어떤 평가 항목을 함께 보고해야 하는가입니다. W11은 accuracy, MI attack accuracy, leakage, epsilon/accounting, utility drop, reproducibility를 함께 묶습니다.

근거 파일: `06_report/final/integrated_report_final.md`

## Q2. 실습/실험 결과는 어디까지 주장할 수 있나요?

답변: synthetic toy 실험의 평가 형식과 기록 구조까지만 주장할 수 있습니다. 실제 DP-SGD 보장, 실제 개인정보 보호 수준, 실제 운영 모델의 MI 위험으로 일반화하지 않습니다.

근거 파일: `04_experiment/outputs/run_log.md`

## Q3. `epsilon_proxy`는 실제 epsilon인가요?

답변: 아닙니다. noise 강도별 비교를 위한 proxy이며 정식 privacy accountant로 계산한 epsilon이 아닙니다.

근거 파일: `04_experiment/experiment_report.md`

## Q4. 선택한 보안 지표는 왜 필요한가요?

답변: Accuracy는 utility를 보여주지만 membership leakage를 보여주지 않습니다. MI Attack Accuracy와 Privacy Leakage Score를 함께 기록해야 privacy risk를 별도 축으로 볼 수 있습니다.

근거 파일: `03_theory_notes/evaluation_protocol.md`

## Q5. 논문 5편은 각각 어떤 역할을 하나요?

답변: P01은 DP misuse, P02는 DP-DL auditing, P03은 DP 적용 위치, P04는 MI taxonomy, P05는 MI defense와 trade-off를 담당합니다.

근거 파일: `02_paper_summaries/paper_matrix.md`

## Q6. DOI/URL 또는 원문 검증은 완료되었나요?

답변: 부분 완료입니다. P01/P02/P04는 arXiv와 로컬 PDF를 확인했지만 ACM DOI 공식 확인이 필요합니다. P03/P05는 DOI 후보가 있으나 로컬 PDF가 대체 문헌입니다.

근거 파일: `01_papers/doi_check.md`

## Q7. 다음 실험으로 확장한다면 무엇이 필요하나요?

답변: 정식 DP-SGD 라이브러리, privacy accountant, 반복 seed, confidence/loss 기반 MI 평가, formal epsilon/delta 기록이 필요합니다.

근거 파일: `04_experiment/experiment_report.md`
