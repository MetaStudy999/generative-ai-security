# W06 발표용 보고서

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W06 |
| 주제 | 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| 발표 시간 | 8-10분 |
| 권장 슬라이드 수 | 10-14장 |
| 핵심 메시지 | 딥페이크 탐지 평가는 in-domain accuracy만으로 충분하지 않으며, cross-domain FPR/FNR과 human review routing을 함께 기록해야 한다. |
| 발표 근거 | `06_report/final/integrated_report_final.md`, `04_experiment/outputs/run_log.md` |

## 2. 한 문장 요약

W06는 diffusion/GAN 생성 원리와 딥페이크 탐지 신뢰성 문제를 연결하고, synthetic detector score 실험으로 domain shift와 review-band triage의 효과를 분리 평가한다.

## 3. 발표 흐름

| 순서 | 슬라이드 주제 | 핵심 내용 | 시간 |
|---:|---|---|---:|
| 1 | 표지 | W06 주제와 핵심 질문 | 0:30 |
| 2 | 왜 중요한가 | 생성 품질과 포렌식 신뢰성은 다른 문제 | 1:00 |
| 3 | AI 원리 | diffusion forward/reverse, score-based sampling | 1:10 |
| 4 | GAN 원리 | generator-discriminator와 안정성 문제 | 1:00 |
| 5 | 보안 이슈 | 딥페이크 피해와 FPR/FNR 위험 | 1:10 |
| 6 | 논문 5편 | 원리 문헌과 reliability 문헌 연결 | 1:00 |
| 7 | 위협모형 | detector score, domain shift, review workflow | 1:00 |
| 8 | 평가 프로토콜 | accuracy, F1, FPR, FNR, AUROC, ECE | 1:00 |
| 9 | Toy 실험 | synthetic detector score 분포 | 1:00 |
| 10 | 결과 | in-domain 1.000000, cross-domain 0.816667 | 1:00 |
| 11 | Review-band | review rate 0.358333, auto coverage 0.641667 | 0:50 |
| 12 | 기말 연결 | cross-domain reliability 평가 프레임워크 | 0:40 |
| 13 | 결론/Q&A | accuracy 단독 평가의 한계 | 0:20 |

## 4. 논문 5편의 발표 역할

| ID | 논문 | 발표에서 맡는 역할 | DOI/URL 상태 |
|---|---|---|---|
| P01 | Diffusion Models: A Comprehensive Survey of Methods and Applications | diffusion 원리와 조건부 생성 배경 | DOI 확인 |
| P02 | A Survey on Video Diffusion Models | video diffusion과 temporal consistency | ACM DOI 확인, 강의계획서 동일 여부 확인 필요 |
| P03 | Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy | GAN 구조와 생성 품질 지표 한계 | ACM DOI 확인, 강의계획서 저자명 차이 확인 필요 |
| P04 | The Creation and Detection of Deepfakes | 딥페이크 생성·탐지 위협모형 | DOI 확인 |
| P05 | Deepfake Detection from the Reliability Perspective | transferability, interpretability, robustness | DOI 확인 |

## 5. AI 원리 설명

- Diffusion model은 forward process와 reverse denoising process로 데이터 분포를 학습한다.
- Score-based model은 데이터 분포의 score를 추정해 sampling을 수행한다.
- GAN은 generator와 discriminator의 경쟁 구조로 sample을 생성한다.
- 조건부 생성은 text, image, class condition으로 synthetic media를 제어한다.

## 6. 보안 이슈 설명

| 항목 | 발표 내용 |
|---|---|
| 보호 자산 | 영상/이미지 증거, detector score, 판단 로그, 검토 기록 |
| 실패 조건 | 새로운 생성기, 압축, 재인코딩, 플랫폼 후처리 |
| 피해 | 허위정보, 사칭, false accusation, missed detection |
| 평가 지표 | accuracy, FPR, FNR, AUROC, ECE, review rate |
| 제외 범위 | 실제 딥페이크 생성, 실제 개인정보, 무단 서비스 질의 |

## 7. 실습/실험 결과

정량값은 `04_experiment/outputs/run_log.md` 기준이다.

| 조건 | Accuracy | F1 | FPR | FNR | AUROC | ECE | Auto coverage | Review rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| In-domain detector baseline | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 1.000000 | 0.216327 | 해당 없음 | 해당 없음 |
| Cross-domain reliability stress | 0.816667 | 0.813559 | 0.166667 | 0.200000 | 0.899722 | 0.147949 | 해당 없음 | 해당 없음 |
| Review-band triage | 0.909091 | 0.901408 | 0.050000 | 0.135135 | 0.962162 | 0.174872 | 0.641667 | 0.358333 |

## 8. 기말논문 연결

| 기말논문 장 | 발표에서 연결할 내용 |
|---|---|
| 서론 | 딥페이크 탐지 신뢰성 평가 필요성 |
| 관련연구 | diffusion/GAN 원리와 deepfake reliability survey |
| 연구문제 | in-domain 성능과 cross-domain 신뢰성의 차이 |
| 연구방법 | synthetic score 실험, FPR/FNR, review routing |
| 분석/실험 | threshold detector와 review-band triage |
| 보안적 함의 | false positive/false negative와 accountability |

## 9. 결론 메시지

1. 생성모형 품질과 탐지기 신뢰성은 분리해서 평가해야 한다.
2. In-domain accuracy 1.000000은 cross-domain 안전성을 보장하지 않는다.
3. FPR/FNR과 review rate를 함께 기록해야 포렌식 판단 위험을 설명할 수 있다.
4. 수치는 실행 로그와 config, CSV/JSON 근거가 있을 때만 주장한다.

## 10. 예상 질문과 답변

| 질문 | 답변 요지 | 근거 파일 |
|---|---|---|
| 왜 실제 딥페이크 데이터를 쓰지 않았나? | 목표는 공격·생성 재현이 아니라 신뢰성 지표 구조를 안전하게 검증하는 것이다. | `04_experiment/experiment_report.md` |
| Cross-domain accuracy 0.816667은 무엇을 뜻하나? | synthetic shifted score 조건에서 threshold detector가 120개 중 98개를 맞췄다는 뜻이다. | `04_experiment/outputs/results.json` |
| Review-band가 실제 방어인가? | 아니다. 불확실한 score를 자동판정에서 제외하는 workflow 예시다. | `04_experiment/outputs/run_log.md` |
| DOI는 모두 확정인가? | P01-P05 DOI는 확인했다. 다만 P02는 강의계획서 지정 논문과 현재 로컬 PDF 동일 여부, P03은 강의계획서 저자명 차이가 확인 필요다. | `01_papers/doi_check.md` |
