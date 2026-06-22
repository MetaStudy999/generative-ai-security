# W06 발표 예상 질문과 답변

## 기준

| 항목 | 내용 |
|---|---|
| 주제 | 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| 발표 파일 | `presentation_report.md`, `presentation_slides.md` |
| 실험 근거 | `04_experiment/outputs/run_log.md` |
| 주의 | synthetic toy 결과를 실제 딥페이크 탐지 모델 성능으로 일반화하지 않음 |

## Q1. 왜 실제 딥페이크 이미지나 비디오를 쓰지 않았나요?

이번 주차의 목적은 딥페이크 생성이나 공격 재현이 아니라, detector reliability 평가 지표를 안전하게 확인하는 것입니다. 실제 개인정보, 실제 인물 영상, 운영 서비스 질의 없이 synthetic detector score만 사용했습니다.

근거 파일: `04_experiment/experiment_report.md`, `04_experiment/outputs/run_log.md`

## Q2. In-domain accuracy 1.000000이면 detector가 좋은 것 아닌가요?

기준 도메인에서는 좋은 결과입니다. 하지만 cross-domain에서는 accuracy가 0.816667로 낮아지고 FNR이 0.200000으로 증가했습니다. 따라서 in-domain 성능만으로 실제 신뢰성을 판단할 수 없습니다.

근거 파일: `04_experiment/outputs/metrics_summary.csv`

## Q3. Cross-domain reliability stress는 무엇을 의미하나요?

압축, 재인코딩, 새로운 생성기, 플랫폼 후처리처럼 detector score 분포가 바뀌는 상황을 synthetic하게 줄인 것입니다. real score는 높아지고 fake score는 낮아져 threshold 주변 오류가 늘어나는 조건입니다.

근거 파일: `04_experiment/configs/config.yaml`, `04_experiment/src/run_experiment.py`

## Q4. Review-band triage가 실제 방어를 증명하나요?

아닙니다. 이 값은 score 0.40-0.60 구간을 자동판정하지 않고 human review로 보내는 workflow 예시입니다. 실제 방어 성능은 real benchmark와 사람 검토 프로토콜을 별도로 검증해야 합니다.

근거 파일: `04_experiment/outputs/run_log.md`

## Q5. FPR과 FNR 중 무엇이 더 중요한가요?

둘 다 중요합니다. FPR은 진짜 미디어를 가짜로 오판하는 위험이고, FNR은 실제 조작물을 놓치는 위험입니다. 포렌식과 법적 맥락에서는 두 오류의 비용이 모두 크므로 함께 보고해야 합니다.

근거 파일: `06_report/final/integrated_report_final.md`

## Q6. P02와 P03의 DOI 상태는 왜 부분 검증인가요?

P02의 ACM DOI `10.1145/3696415`와 P03의 ACM DOI `10.1145/3439723`은 확인했습니다. 다만 P02는 강의계획서의 `Ananya Högele et al., "Video Diffusion Models: A Survey"`와 현재 로컬 PDF `A Survey on Video Diffusion Models`의 동일 여부가 남아 있고, P03은 강의계획서의 `Tianqi Wang et al.` 표기와 출판사 저자명 `Zhengwei Wang et al.`이 달라 부분 검증으로 둡니다.

근거 파일: `01_papers/doi_check.md`

## Q7. 기말논문으로 발전시킨다면 무엇을 더 해야 하나요?

실제 공개 benchmark, 여러 생성기 유형, 압축 수준, 복수 seed, detector calibration, human reviewer agreement를 추가해야 합니다. 그래도 이번 주차의 FPR/FNR, review rate, 재현성 로그 구조는 그대로 사용할 수 있습니다.

근거 파일: `08_final_paper_bridge/final_paper_bridge.md`

## Q8. 발표에서 피해야 할 표현은 무엇인가요?

“딥페이크 탐지기를 검증했다” 또는 “review-band가 실제 방어를 보장한다”는 표현은 피해야 합니다. 정확한 표현은 “synthetic toy 조건에서 신뢰성 평가 지표와 기록 구조를 확인했다”입니다.

근거 파일: `09_presentation/speaker_notes.md`
