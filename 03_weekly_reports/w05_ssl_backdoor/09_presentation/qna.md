# W05 발표 예상 질문과 답변

## 기준

| 항목 | 내용 |
|---|---|
| 주제 | 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| 발표 파일 | `presentation_report.md`, `presentation_slides.md` |
| 실험 근거 | `04_experiment/outputs/run_log.md` |
| 주의 | synthetic toy 결과를 실제 SSL/foundation model 보안 성능으로 일반화하지 않음 |

## Q1. 왜 실제 SSL 모델이나 이미지/텍스트 데이터를 쓰지 않았나요?

이번 주차의 목적은 최고 성능 모델을 만드는 것이 아니라, clean accuracy, ASR, representation shift, detection rate를 분리해 기록하는 평가 구조를 안전하게 확인하는 것입니다. 실제 개인정보, 운영 서비스, 악용 가능한 backdoor 제작 절차 없이 synthetic 2D representation만 사용했습니다.

근거 파일: `04_experiment/experiment_report.md`, `04_experiment/outputs/run_log.md`

## Q2. ASR 1.000000은 정확히 무엇인가요?

Toy source-class test embedding 16개가 trigger vector 적용 후 모두 target class centroid에 더 가깝게 분류됐다는 뜻입니다. 실제 모델이 100% 공격 성공이라는 뜻이 아니라, backdoor 조건 지표를 clean 성능과 분리해 기록하는 예시입니다.

근거 파일: `04_experiment/outputs/run_log.md`, `04_experiment/outputs/results.json`

## Q3. Clean accuracy가 1.000000이면 안전한 모델 아닌가요?

아닙니다. W05 toy 결과는 clean 조건에서는 정상 분류가 유지되어도 trigger 조건에서는 target behavior가 나타날 수 있음을 보여줍니다. 따라서 clean accuracy와 ASR은 함께 봐야 합니다.

근거 파일: `04_experiment/outputs/metrics_summary.csv`

## Q4. Consistency defense의 detection rate 1.000000은 실제 방어를 증명하나요?

증명하지 않습니다. 이 값은 synthetic paired-view distance threshold가 toy trigger shift를 모두 플래그했다는 관찰값입니다. 실제 SSL 모델에서는 augmentation, representation dimension, adaptive trigger, false positive trade-off를 별도로 검증해야 합니다.

근거 파일: `04_experiment/outputs/results.json`

## Q5. P02, P03, P04의 제목 차이는 문제가 되지 않나요?

최종 인용 전 반드시 대조해야 합니다. P01 TPAMI DOI는 확인했지만, P02는 현재 로컬 PDF가 추천 시스템 SSL survey라 지정 일반 SSL survey와 동일 여부가 남아 있습니다. P03/P04는 강의계획서 제목과 출판사 기준 제목 차이를 `doi_check.md`에 기록했고, 확정 인용에서는 출판사 기준 정식 제목을 우선해야 합니다.

근거 파일: `01_papers/doi_check.md`

## Q6. W05 결과는 기말논문에 어떻게 반영되나요?

기말논문의 관련연구, 위협모형, 평가방법, 분석/실험 장에 반영됩니다. 특히 표현학습 기반 AI 시스템에서 clean performance, ASR, representation shift, reproducibility를 함께 보는 평가표로 발전시킬 수 있습니다.

근거 파일: `08_final_paper_bridge/final_paper_bridge.md`, `07_week_submission/w05_submission_report.md`

## Q7. 다음 실험으로 확장한다면 무엇이 필요한가요?

공개 이미지/텍스트 데이터셋, 실제 SSL encoder, 여러 trigger type, 복수 seed, adaptive 공격자 가정, 방어 threshold sensitivity 분석이 필요합니다. 확장 후에도 CSV/JSON/run_log와 한계 기록을 함께 남겨야 합니다.

근거 파일: `04_experiment/configs/config.yaml`, `04_experiment/src/run_experiment.py`

## Q8. 발표에서 피해야 할 표현은 무엇인가요?

“실제 SSL 모델의 backdoor를 방어했다” 또는 “foundation model backdoor가 100% 성공한다” 같은 표현은 피해야 합니다. 정확한 표현은 “synthetic toy 조건에서 평가 지표 분리 구조를 확인했다”입니다.

근거 파일: `09_presentation/speaker_notes.md`

<!-- formula-visual-qna:start -->
## 수식·그래프·그림 보강 Q&A

### Q. 그래프 수치는 어디에서 온 것인가?

A. `04_experiment/outputs/metrics_summary.csv`의 기존 수치만 사용했다. CSV에 없는 값, 실행하지 않은 실험, 외부 논문 실험 수치는 추가하지 않았다.

### Q. 이 수식은 해당 논문의 원문 수식인가?

A. 발표 보강용 수식은 표준 정의식 또는 검증 가능한 평가식이다. 논문별 원문 절·쪽·그림 번호가 필요한 경우 최종 제출 전 사람 검토로 확인한다.

### Q. 다이어그램은 실험 결과인가?

A. 아니다. `SSL backdoor evaluation flow` 다이어그램은 AI-assisted conceptual diagram이며 threat model과 pipeline 설명을 위한 보조 그림이다.

### Q. 보안적으로 가장 조심해야 할 해석은 무엇인가?

A. trigger 관련 설명은 공개 toy/synthetic 범위이며 실제 악용 가능한 절차를 제공하지 않는다. 또한 모든 실습은 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 범위로만 해석한다.
<!-- formula-visual-qna:end -->
