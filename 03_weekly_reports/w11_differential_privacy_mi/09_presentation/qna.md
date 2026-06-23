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

답변: 부분 완료입니다. P01, P02, P04, P05의 DOI는 확인했습니다. P02는 강의자료의 저자명/권호 표기가 공식 메타데이터와 달라 최종 대조가 필요합니다. P03은 DOI가 Neurocomputing 지정 논문으로 연결되지만 강의자료 저자명 표기와 로컬 대체 PDF 상태가 남아 있습니다. P03/P05는 지정 원문 PDF 확보가 필요합니다.

근거 파일: `01_papers/doi_check.md`

## Q7. 다음 실험으로 확장한다면 무엇이 필요하나요?

답변: 정식 DP-SGD 라이브러리, privacy accountant, 반복 seed, confidence/loss 기반 MI 평가, formal epsilon/delta 기록이 필요합니다.

근거 파일: `04_experiment/experiment_report.md`

<!-- formula-visual-qna:start -->
## 수식·그래프·그림 보강 Q&A

### Q. 그래프 수치는 어디에서 온 것인가?

A. `04_experiment/outputs/metrics_summary.csv`의 기존 수치만 사용했다. CSV에 없는 값, 실행하지 않은 실험, 외부 논문 실험 수치는 추가하지 않았다.

### Q. 이 수식은 해당 논문의 원문 수식인가?

A. 발표 보강용 수식은 표준 정의식 또는 검증 가능한 평가식이다. 논문별 원문 절·쪽·그림 번호가 필요한 경우 최종 제출 전 사람 검토로 확인한다.

### Q. 다이어그램은 실험 결과인가?

A. 아니다. `DP-SGD and MI audit flow` 다이어그램은 AI-assisted conceptual diagram이며 threat model과 pipeline 설명을 위한 보조 그림이다.

### Q. 보안적으로 가장 조심해야 할 해석은 무엇인가?

A. `epsilon_proxy`는 formal DP accountant 값이 아니며 formal DP guarantee로 쓰지 않는다. 또한 모든 실습은 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 범위로만 해석한다.
<!-- formula-visual-qna:end -->
