# W03 발표 예상 질문과 답변

## 기준

| 항목 | 내용 |
|---|---|
| 주제 | 컴퓨터비전 표현학습 & 비전 대적공격 |
| 발표 파일 | `presentation_report.md`, `presentation_slides.md` |
| 실험 근거 | `04_experiment/outputs/run_log.md` |
| 주의 | DOI/URL은 확인되었으나 원문 세부 수치, PDF 보관 정책, 실제 시스템 일반화는 확정 표현 금지 |

## Q1. 왜 실제 CNN이나 ViT가 아니라 toy nearest-centroid 실험을 사용했나요?

이번 주차의 목적은 최고 성능 모델을 만드는 것이 아니라, clean performance, attack impact, reproducibility를 분리해 기록하는 평가 구조를 확인하는 것입니다. synthetic 8x8 데이터와 단순 모델을 사용하면 개인정보나 운영 서비스 공격 없이 안전하게 공격 조건과 로그 구조를 검증할 수 있습니다.

근거 파일: `04_experiment/experiment_report.md`, `04_experiment/outputs/run_log.md`

## Q2. Accuracy가 1.0 또는 0.0으로 극단적인데, 이 결과를 일반화할 수 있나요?

일반화하면 안 됩니다. 이 값은 synthetic 2-class toy 데이터에서 결정 경계 전환을 보여주는 결과입니다. 실제 CNN/ViT, 자연 이미지, 2D/3D 입력의 강건성을 주장하려면 별도 데이터셋, 모델, 공격 설정, 반복 실험이 필요합니다.

근거 파일: `09_presentation/presentation_slides.md`, `06_report/final/integrated_report_final.md`

## Q3. Feature squeezing은 실제 방어라고 볼 수 있나요?

이번 실험에서는 방어 성능을 확정하기보다 “방어/점검 조건도 별도 지표로 기록해야 한다”는 예시로 사용했습니다. Feature squeezing eps 0.30 결과는 accuracy 1.000000, ASR 0.000000이지만, 이는 toy 설정의 관찰값이며 실제 방어 효과로 일반화하지 않습니다.

근거 파일: `04_experiment/outputs/run_log.md`

## Q4. 왜 ASR을 accuracy와 따로 기록해야 하나요?

Accuracy는 전체 예측 정답률을 보여주지만, 공격이 성공했는지 직접 설명하지 못할 수 있습니다. ASR은 공격 조건에서 원래 맞던 샘플이 공격 후 실패했는지를 보여주므로, 보안 관점의 공격 영향도를 별도로 설명하는 데 필요합니다.

근거 파일: `03_theory_notes/evaluation_protocol.md`, `04_experiment/experiment_report.md`

## Q5. White-box와 black-box 공격은 발표에서 어떻게 구분하면 되나요?

White-box는 공격자가 모델 구조, 파라미터, gradient 등 내부 정보를 알고 있다고 가정합니다. Black-box는 내부 정보 없이 제한된 질의나 transfer를 통해 공격한다고 봅니다. W03 발표에서는 이 구분을 공격자 능력의 차이로 설명하고, 평가 지표는 robust accuracy, ASR, attack impact로 연결하면 됩니다.

근거 파일: `02_security_notes/threat_model.md`, `09_presentation/presentation_slides.md`

## Q6. W03 결과는 기말논문에 어떻게 반영되나요?

W03는 기말논문의 관련연구, 위협모형, 평가방법, 분석/실험 장에 연결됩니다. 특히 clean 성능, 공격 조건 성능, 재현성 산출물을 분리하는 형식은 AI 보안 평가 프레임워크의 핵심 사례로 사용할 수 있습니다.

근거 파일: `08_final_paper_bridge/final_paper_bridge.md`, `09_presentation/presentation_report.md`

## Q7. DOI/URL이나 원문 세부 내용은 모두 검증되었나요?

P01-P05 DOI/URL은 Crossref/DOI 기준으로 확인되었습니다. 다만 발표에서는 원문 세부 실험 수치, PDF 보관 정책, 실제 모델 일반화 가능성은 사람이 최종 검토해야 한다고 말합니다.

근거 파일: `01_papers/doi_check.md`, `07_week_submission/submit_checklist.md`

## Q8. 다음 실험으로 확장한다면 무엇을 해야 하나요?

다음 단계는 실제 이미지 데이터셋, CNN 또는 ViT 모델, 복수 epsilon, 반복 seed, 더 명시적인 공격 알고리즘을 포함하는 것입니다. 다만 확장 후에도 실행 로그, config, CSV/JSON, 한계 기록을 함께 남겨야 합니다.

근거 파일: `00_management/progress_log.md`, `04_experiment/configs/config.yaml`

## Q9. 이 발표에서 피해야 할 표현은 무엇인가요?

“W03 실험으로 실제 비전 모델 방어가 검증되었다” 또는 “feature squeezing이 보편적으로 효과적이다” 같은 표현은 피해야 합니다. 정확한 표현은 “toy/synthetic 조건에서 평가 지표 분리와 로그 재현성 구조를 확인했다”입니다.

근거 파일: `09_presentation/speaker_notes.md`, `04_experiment/outputs/run_log.md`
