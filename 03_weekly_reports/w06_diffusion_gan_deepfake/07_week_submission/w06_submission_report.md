# W06 제출용 보고서

## 표지

| 항목 | 내용 |
|---|---|
| 주차 | W06 |
| 보고서 제목 | 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| 과목 범위 | AI 보안 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 통합본 |
| 관련 산출물 위치 | `03_weekly_reports/w06_diffusion_gan_deepfake/` |

## 초록

본 보고서는 diffusion model, score-based model, GAN, 조건부 생성의 원리를 정리하고, 딥페이크 탐지 모델의 신뢰성 문제를 보안 평가 관점에서 분석한다. 문헌 5편을 통해 생성모형 품질 평가와 포렌식 탐지 신뢰성 평가를 구분했다. 실습에서는 실제 딥페이크 생성 없이 synthetic real/fake detector score 분포를 사용해 in-domain 성능, cross-domain reliability stress, review-band triage를 비교했다. 결과적으로 in-domain accuracy는 1.000000이었지만 cross-domain accuracy는 0.816667로 낮아지고 FNR은 0.200000으로 증가했다. 불확실 구간을 human review로 넘기면 auto coverage는 0.641667이 되고 자동판정 영역의 FPR/FNR은 각각 0.050000/0.135135로 낮아졌다.

**키워드:** diffusion model, GAN, deepfake detection, reliability, FPR, FNR, cross-domain generalization, human review

## 1. AI 원리 70%

Diffusion model은 forward process에서 데이터에 노이즈를 더하고 reverse process에서 denoising을 통해 sample을 복원한다. Score-based model은 데이터 분포의 score를 추정해 sampling한다. 조건부 생성은 text, class, image 등 외부 조건을 이용해 생성 방향을 통제한다.

GAN은 generator와 discriminator의 경쟁 구조로 사실적인 sample을 만든다. 하지만 mode collapse, training instability, 생성 품질 지표의 한계가 있다. W06의 핵심은 생성 품질 지표가 딥페이크 탐지기의 실제 포렌식 신뢰성을 보장하지 않는다는 점이다.

## 2. 보안 이슈 30%

딥페이크는 허위정보, 사칭, 명예훼손, 협박, 증거 조작 위험을 만든다. 탐지기는 benchmark accuracy가 높아도 미지 생성기, 압축, 재인코딩, 플랫폼 후처리에서는 오탐과 미탐이 늘어날 수 있다.

| 관점 | 관련 위협 | W06 평가 연결 |
|---|---|---|
| Integrity | 합성미디어 기반 허위증거 | FPR/FNR 분리 기록 |
| Robustness | 압축·미지 도메인 score shift | cross-domain reliability stress |
| Safety | false accusation 또는 missed detection | review-band triage |
| Accountability | 판단 근거와 로그 부재 | CSV/JSON/run log 보존 |
| Governance | DOI/URL과 실험 근거 누락 | 검증표와 AI 활용 고지 |

## 3. 문헌 요약

| ID | 문헌 | DOI/URL 상태 | 활용 |
|---|---|---|---|
| P01 | Diffusion Models: A Comprehensive Survey of Methods and Applications | DOI `10.1145/3626235` | diffusion 원리와 조건부 생성 배경 |
| P02 | A Survey on Video Diffusion Models | arXiv DOI `10.48550/arXiv.2310.10647` | video diffusion과 temporal consistency |
| P03 | Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy | arXiv DOI `10.48550/arXiv.1906.01529` | GAN taxonomy와 생성 품질 지표 한계 |
| P04 | The Creation and Detection of Deepfakes: A Survey | DOI `10.1145/3425780` | 딥페이크 생성·탐지 위협모형 |
| P05 | Deepfake Detection: A Comprehensive Survey from the Reliability Perspective | DOI `10.1145/3699710` | transferability, interpretability, robustness |

## 4. Research Track

| 항목 | 내용 |
|---|---|
| 연구문제 | 딥페이크 탐지기는 in-domain 성능이 높을 때 cross-domain 조건에서도 신뢰할 수 있는가 |
| 대상 시스템 | Synthetic media detector, forensic review workflow |
| 위협 | 압축·미지 생성기·platform shift에 따른 FPR/FNR 증가 |
| 평가 지표 | accuracy, F1, FPR, FNR, AUROC, ECE, auto coverage, review rate |
| 재현성 | seed 42, config, script, CSV/JSON/run log 보존 |
| 제외 범위 | 실제 딥페이크 생성, 실제 개인정보, 무단 서비스 질의 |

## 5. 실습/실험 결과

실습 코드는 `04_experiment/src/run_experiment.py`에 작성했다. 실행 명령은 `python3 src/run_experiment.py --config configs/config.yaml`이며 결과는 `04_experiment/outputs/`에 저장했다.

| 조건 | Accuracy | F1 | FPR | FNR | AUROC | ECE | Auto coverage | Review rate | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| In-domain detector baseline | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 1.000000 | 0.216327 | 해당 없음 | 해당 없음 | 기준 도메인 score 분리 명확 |
| Cross-domain reliability stress | 0.816667 | 0.813559 | 0.166667 | 0.200000 | 0.899722 | 0.147949 | 해당 없음 | 해당 없음 | score margin 축소로 FPR/FNR 발생 |
| Review-band triage on shifted domain | 0.909091 | 0.901408 | 0.050000 | 0.135135 | 0.962162 | 0.174872 | 0.641667 | 0.358333 | 불확실 구간을 human review로 라우팅 |

이 결과는 synthetic toy 실험의 평가 형식 검증용 수치다. 실제 딥페이크 데이터셋, 실제 탐지 모델, 법적 포렌식 성능으로 일반화하지 않는다.

## 6. 발표자료 위치

| 파일 | 용도 |
|---|---|
| `09_presentation/presentation_report.md` | 발표용 보고서 |
| `09_presentation/presentation_slides.md` | 슬라이드 원본 |
| `09_presentation/presentation_slides.html` | 브라우저 발표용 슬라이드 |
| `09_presentation/speaker_notes.md` | 발표자 대본 |
| `09_presentation/qna.md` | 예상 질문과 답변 |
| `09_presentation/one_page_handout.md` | 1페이지 배포자료 |

## 7. 기말논문 연결

추천 주제는 “딥페이크 탐지기의 cross-domain reliability 평가 프레임워크”이다. 기여 후보는 diffusion/GAN 생성 원리와 딥페이크 탐지 신뢰성의 분리, FPR/FNR 중심 평가표, review-band triage, seed/config/output 기반 재현성 기록이다.

## 8. AI 활용 고지

Codex를 사용해 문헌 요약 구조화, DOI/URL 검증 보조, synthetic 실험 코드 작성과 실행, 제출용 보고서 및 발표자료 작성을 수행했다. 정량값은 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 사용했다. 상세 기록은 `05_ai_worklog/`에 있다.

## 9. 제출 전 점검표

| 점검 항목 | 상태 |
|---|---|
| 논문 요약 5편 | 완료 |
| 논문 비교표 | 완료 |
| AI 원리/보안 이슈 | 완료 |
| Research Track | 완료 |
| 실험 코드 | 완료 |
| 실험 결과 | 완료 |
| DOI/URL 검증표 | 부분 완료 |
| AI 활용 고지 | 완료 |
| 발표자료 | 완료 |
