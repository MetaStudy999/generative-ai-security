# W07 발표 예상 질문과 답변

## 기준

| 항목 | 내용 |
|---|---|
| 주제 | LLM 학습·정렬·평가 & LLM 보안·프라이버시 |
| 발표 파일 | `presentation_report.md`, `presentation_slides.md` |
| 실험 근거 | `04_experiment/outputs/run_log.md` |
| 주의 | synthetic toy 결과를 실제 LLM 보안 성능으로 일반화하지 않음 |

## Q1. 왜 실제 LLM이나 API를 쓰지 않았나요?

이번 주차의 목표는 공격 재현이나 외부 서비스 테스트가 아니라 평가 프로토콜과 재현성 기록 구조를 안전하게 확인하는 것입니다. 그래서 synthetic prompt category와 toy guard score만 사용했습니다.

근거 파일: `04_experiment/experiment_report.md`, `04_experiment/outputs/run_log.md`

## Q2. ASR 0.150000은 실제 prompt injection 성공률인가요?

아닙니다. 실제 공격 성공률이 아니라 synthetic risky category에서 toy guard가 차단하지 못한 비율입니다. 발표에서는 “실제 공격 성공률”이 아니라 “평가표 검증용 toy ASR”로 설명해야 합니다.

근거 파일: `04_experiment/src/run_experiment.py`, `04_experiment/outputs/results.json`

## Q3. Refusal quality와 over-refusal을 왜 함께 보나요?

위험 요청을 잘 거절하는 것만으로 충분하지 않습니다. 정상 요청까지 과도하게 차단하면 유용성이 떨어집니다. 그래서 W07은 refusal quality와 over-refusal rate를 함께 기록합니다.

근거 파일: `06_report/final/integrated_report_final.md`

## Q4. Code vulnerability rate 0.200000은 어떤 뜻인가요?

Code security prompt 조건에서 toy vulnerability risk flag가 켜진 비율입니다. 취약 코드 예시를 직접 생성하거나 실행한 것이 아니라, 코드 보안 평가 항목을 표에 넣는 방식을 모의한 값입니다.

근거 파일: `04_experiment/outputs/metrics_summary.csv`

## Q5. P02, P03, P04는 왜 재검증 필요인가요?

로컬 PDF에는 arXiv 식별자 또는 출판 전/출판 표기가 있고, 프롬프트에 적힌 학술지 정보와 일부 차이가 있습니다. 최종 논문 인용 전 공식 출판사 페이지에서 권호와 DOI를 다시 확인해야 합니다.

근거 파일: `01_papers/doi_check.md`

## Q5-1. Code security의 over-refusal 0.350000은 왜 함께 보여주나요?

Code security 조건에서 toy guard가 정상 보안 코딩 지원까지 막은 비율입니다. 취약 코드 위험만 낮추면 실제 운영에서는 정상 보안 업무 지원성이 떨어질 수 있으므로, code vulnerability rate 0.200000과 함께 해석해야 합니다.

근거 파일: `04_experiment/outputs/metrics_summary.csv`

## Q6. 기말논문으로 발전시키려면 무엇이 더 필요한가요?

실제 공개 benchmark, 복수 LLM, 복수 seed, 정책 라벨, 사람이 검토한 정답표, 평가자 간 agreement가 필요합니다. 이번 주차의 가치는 그 확장 실험을 담을 평가표와 로그 구조를 만든 데 있습니다.

근거 파일: `08_final_paper_bridge/final_paper_bridge.md`

## Q7. 발표에서 피해야 할 표현은 무엇인가요?

“실제 LLM 보안을 검증했다”, “prompt injection 방어 성능을 입증했다”는 표현은 피해야 합니다. 정확한 표현은 “synthetic toy 조건에서 LLM 보안 평가 지표와 재현성 기록 구조를 확인했다”입니다.

근거 파일: `09_presentation/speaker_notes.md`

<!-- formula-visual-qna:start -->
## 수식·그래프·그림 보강 Q&A

### Q. 그래프 수치는 어디에서 온 것인가?

A. `04_experiment/outputs/metrics_summary.csv`의 기존 수치만 사용했다. CSV에 없는 값, 실행하지 않은 실험, 외부 논문 실험 수치는 추가하지 않았다.

### Q. 이 수식은 해당 논문의 원문 수식인가?

A. 발표 보강용 수식은 표준 정의식 또는 검증 가능한 평가식이다. 논문별 원문 절·쪽·그림 번호가 필요한 경우 최종 제출 전 사람 검토로 확인한다.

### Q. 다이어그램은 실험 결과인가?

A. 아니다. `LLM privacy/safety evaluation flow` 다이어그램은 AI-assisted conceptual diagram이며 threat model과 pipeline 설명을 위한 보조 그림이다.

### Q. 보안적으로 가장 조심해야 할 해석은 무엇인가?

A. privacy leakage는 toy/proxy metric이며 실제 개인정보 추출 실험으로 해석하지 않는다. 또한 모든 실습은 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 범위로만 해석한다.
<!-- formula-visual-qna:end -->
