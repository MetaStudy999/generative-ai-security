# W06 제출용 단일 보고서

## 확률생성모형(Diffusion/GAN) & 딥페이크 검출

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W06 |
| 보고서 제목 | 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| 과목 범위 | AI 보안 |
| 작성자 | 박영세 |
| 학번 | 26200122 |
| 작성일 | 2026-06-26 |
| 문서 상태 | 주차별 단일 제출용 보고서 |
| 원본 관리 파일 | `03_weekly_reports/w06_diffusion_gan_deepfake/07_week_submission/w06_submission_report.md` |
| Word/PDF 제출본 권장 위치 | `03_weekly_reports/w06_diffusion_gan_deepfake/07_week_submission/exports/` |
| 관련 산출물 위치 | `03_weekly_reports/w06_diffusion_gan_deepfake/` |
| 안전 범위 | 실제 딥페이크 생성, 실제 개인정보, 실제 서비스 질의, 악용 가능한 생성·우회 절차 제외 |
| PDF 검토 상태 | P01~P05 로컬 PDF blob 존재 확인. 제출 본문은 DOI/URL, `paper_list.md`, 논문별 summary, 실험 보고서 기준으로 작성 |
| 제출 전 주의 | P02는 강의계획서 지정 `Ananya Högele et al.` 논문과 현재 `Zhen Xing et al.` 논문 동일성 확인 필요. P03/P05는 강의계획서 저자 표기 차이 확인 필요 |

---

## 초록

본 보고서는 W06 주차의 확률생성모형과 딥페이크 탐지 신뢰성 평가를 하나의 제출용 보고서로 통합한다. Diffusion model은 forward noising과 reverse denoising을 통해 데이터 분포를 복원하는 생성모형이고, video diffusion은 시간적 일관성과 조건부 생성을 함께 고려한다. GAN은 generator와 discriminator의 경쟁 학습을 통해 사실적인 시각 샘플을 생성하지만, 생성 품질과 탐지 신뢰성은 별도의 평가 문제다. 본 보고서는 W06 논문 5편을 바탕으로 diffusion, video diffusion, GAN, deepfake creation/detection, deepfake detector reliability를 연결하고, 실제 딥페이크 생성 없이 synthetic real/fake detector score distribution 기반 안전 toy protocol로 accuracy, F1, FPR, FNR, AUROC, ECE, auto coverage, review rate, reproducibility evidence를 분리 기록하였다. 실험 결과는 실제 포렌식 성능이나 법적 증거능력 주장이 아니라 평가 구조를 설명하기 위한 안전한 예시로 한정한다.

**키워드:** diffusion model, video diffusion, GAN, deepfake detection, reliability, FPR, FNR, AUROC, calibration, review-band triage, 재현성

---

## 1. 한 문장 요약

W06는 생성모형의 품질 평가와 딥페이크 탐지기의 포렌식 신뢰성 평가를 분리하고, in-domain 성능뿐 아니라 cross-domain reliability, FPR/FNR, calibration, human review routing을 함께 기록해야 함을 보여주는 주차다.

---

## 2. 학습 배경과 주차 목표

### 2.1 이번 주 주제의 위치

W06는 W05의 파운데이션 모델·표현학습 논의를 확률생성모형과 합성미디어 보안으로 확장하는 주차다. W01은 AI 보안 평가의 생명주기 프레임을 세웠고, W02는 학습 데이터 오염, W03은 비전 대적공격, W04는 Transformer/NLP 프라이버시, W05는 표현공간 backdoor를 다루었다. W06는 diffusion, video diffusion, GAN, deepfake detection을 연결하여 생성모형의 품질과 포렌식 탐지 신뢰성을 분리해 평가한다.

### 2.2 강의계획서상 학습목표

- Diffusion model의 forward noising, reverse denoising, denoising objective를 이해한다.
- Video diffusion에서 temporal consistency, identity consistency, provenance coverage를 정리한다.
- GAN의 minimax objective와 generator-detector arms race를 이해한다.
- Deepfake creation/detection taxonomy와 detector reliability 문제를 분리한다.
- In-domain과 cross-domain 조건에서 FPR, FNR, AUROC, ECE, review rate를 함께 기록한다.

### 2.3 이번 주 핵심 질문

1. Diffusion/GAN 생성 품질이 높다는 사실이 딥페이크 탐지 신뢰성을 보장하는가?
2. In-domain 성능이 높은 detector가 cross-domain 또는 platform shift 조건에서도 신뢰할 수 있는가?
3. FPR과 FNR은 딥페이크 포렌식에서 어떤 다른 사회적 피해를 만드는가?
4. Review-band triage는 자동판정률과 human review 부담을 어떻게 trade-off하는가?
5. W06의 synthetic detector score 실험을 기말논문 평가 프레임워크로 확장하려면 어떤 지표가 필요한가?

---

## 3. 논문 5편의 서술형 종합 요약

### 3.1 P01. Diffusion Models: A Comprehensive Survey of Methods and Applications

P01은 diffusion model의 기본 원리와 응용을 정리하는 핵심 문헌이다. Diffusion model은 실제 데이터에 noise를 점진적으로 추가하는 forward process와, noise가 섞인 샘플에서 원래 데이터 분포를 복원하는 reverse denoising process로 구성된다. 이 구조는 이미지, 텍스트-이미지 생성, 조건부 생성, 복원, editing 등 다양한 생성 작업으로 확장된다.

보안 관점에서 diffusion model은 고품질 synthetic media를 만들 수 있기 때문에 provenance, watermark, 생성물 탐지, misuse risk가 중요해진다. W06에서는 diffusion을 단순 생성모형이 아니라 합성미디어 신뢰성과 탐지기 일반화 문제의 배경 기술로 해석한다.

### 3.2 P02. A Survey on Video Diffusion Models

P02는 video diffusion model을 정리한다. Video diffusion은 단일 이미지 생성과 달리 frame 간 temporal consistency, motion coherence, identity consistency, text-to-video conditioning, long video generation 문제를 함께 다룬다. 비디오 생성에서는 한 프레임의 품질만이 아니라 시간축 전체의 자연스러움과 정체성 유지가 중요하다.

보안 관점에서 video diffusion은 영상 딥페이크, 장면 조작, identity manipulation, provenance loss와 연결된다. 특히 frame-level artifact가 줄어들수록 기존 image-level detector만으로는 탐지가 어려워질 수 있다. 다만 현재 P02는 강의계획서 지정 논문과 저자·제목 표기가 달라 최종 제출 전 동일성 확인이 필요하다.

### 3.3 P03. Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy

P03은 GAN을 computer vision 관점에서 체계화한다. GAN은 generator와 discriminator가 경쟁하는 minimax game으로 학습된다. Generator는 실제와 유사한 샘플을 만들고, discriminator는 real/fake를 구분한다. 이 경쟁 구조는 image synthesis, image-to-image translation, super-resolution, style transfer, face synthesis 등으로 확장된다.

보안 관점에서 GAN은 deepfake generation과 detector arms race의 이론적 배경이다. 생성기가 더 자연스러운 이미지를 만들수록 탐지기는 더 미세한 artifact를 찾아야 한다. 따라서 W06에서는 GAN 품질 지표와 deepfake detector 신뢰성 지표를 분리해 해석한다. P03도 강의계획서 저자명 표기와 현재 로컬 PDF/ACM 저자명이 달라 확인 메모를 유지한다.

### 3.4 P04. The Creation and Detection of Deepfakes: A Survey

P04는 딥페이크 생성과 탐지의 전반적인 위협모형을 정리한다. Deepfake는 얼굴 교체, 표정 조작, 음성·영상 합성, identity manipulation, 정치·사회적 허위정보, 사칭, 증거 조작 등으로 확장된다. 탐지 방법은 artifact 기반, biological signal 기반, frequency 기반, learning-based detector 등으로 구분할 수 있다.

보안 관점에서 P04는 W06의 핵심 위협모형 문헌이다. 딥페이크 탐지는 단순 binary classification이 아니라 false accusation과 missed detection이라는 서로 다른 피해를 동반한다. 따라서 FPR과 FNR을 별도로 보고하고, human review 및 provenance evidence를 함께 다뤄야 한다.

### 3.5 P05. Deepfake Detection: A Comprehensive Survey from the Reliability Perspective

P05는 deepfake detection을 reliability 관점에서 정리한다. 딥페이크 탐지기는 특정 benchmark에서 높은 성능을 보일 수 있지만, 미지 생성기, 압축, 후처리, 플랫폼 변환, cross-dataset shift, unseen manipulation 조건에서는 성능이 떨어질 수 있다. 또한 calibration, interpretability, robustness, transferability가 중요하다.

보안 관점에서 P05는 W06 실험의 직접 근거다. In-domain accuracy만 높게 기록하면 실제 운영 조건의 위험을 과소평가할 수 있다. 따라서 cross-domain stress, FPR/FNR, AUROC, ECE, review-band triage, reproducibility evidence를 함께 보고해야 한다.

---

## 4. 논문 간 연결 관계

W06 논문 5편은 다음 흐름으로 연결된다.

```text
Diffusion 생성 원리
→ Video diffusion과 temporal synthetic media
→ GAN 생성모형과 detector arms race
→ Deepfake creation/detection threat model
→ Deepfake detection reliability 평가
```

P01과 P02는 diffusion 계열 생성모형의 원리와 비디오 확장을 제공한다. P03은 GAN의 생성-판별 경쟁 구조를 정리한다. P04는 딥페이크 생성·탐지 위협모형을 제공하고, P05는 detector reliability와 cross-domain generalization 문제를 정리한다. 이 다섯 문헌을 종합하면 W06의 핵심 메시지는 “생성 품질, 탐지 성능, 포렌식 신뢰성은 서로 다른 평가 문제”라는 것이다.

---

## 5. AI 원리 70% 정리

Diffusion model은 forward noising과 reverse denoising을 통해 데이터 분포를 학습한다. GAN은 generator와 discriminator가 경쟁하는 구조로 데이터 분포를 근사한다. Video diffusion은 단일 이미지가 아니라 시간축의 일관성과 identity consistency를 함께 학습해야 한다. 생성모형의 품질이 높아질수록 합성미디어는 더 자연스러워지지만, 탐지기 신뢰성은 더 어려운 문제가 된다.

### 5.1 핵심 수식

Forward diffusion은 원본 데이터 $x_0$에 단계적으로 noise를 추가한다.

$$
q(x_t\mid x_{t-1})=\mathcal{N}(x_t;\sqrt{1-\beta_t}x_{t-1},\beta_t I)
$$

Closed-form noising은 다음처럼 표현할 수 있다.

$$
q(x_t\mid x_0)=\mathcal{N}(x_t;\sqrt{\bar{\alpha}_t}x_0,(1-\bar{\alpha}_t)I)
$$

Denoising objective는 noise prediction error를 줄이는 방식으로 학습된다.

$$
L_{diff}=\mathbb{E}_{x_0,t,\epsilon}\left[\left\|\epsilon-\epsilon_{\theta}(x_t,t)\right\|_2^2\right]
$$

GAN의 minimax objective는 generator와 discriminator의 경쟁으로 표현된다.

$$
\min_G \max_D V(D,G)=\mathbb{E}_{x\sim p_{data}}[\log D(x)]+\mathbb{E}_{z\sim p_z}[\log(1-D(G(z)))]
$$

딥페이크 탐지 지표는 FPR과 FNR을 분리해 기록해야 한다.

$$
FPR=\frac{FP_r}{FP_r+TN_r}
$$

$$
FNR=\frac{FN_f}{FN_f+TP_f}
$$

Review-band triage에서는 자동판정 비율과 human review 비율을 함께 본다.

$$
AutoCoverage=\frac{N_{auto}}{N_{total}}
$$

$$
ReviewRate=\frac{N_{review}}{N_{total}}
$$

| 기호 | 의미 |
|---|---|
| $x_0$ | 원본 데이터 |
| $x_t$ | noise가 추가된 $t$단계 데이터 |
| $\beta_t$ | noise schedule |
| $G$ | generator |
| $D$ | discriminator 또는 detector |
| $FP_r$ | real을 fake로 오탐한 수 |
| $FN_f$ | fake를 real로 미탐한 수 |
| $N_{auto}$ | 자동판정 샘플 수 |
| $N_{review}$ | human review로 보낸 샘플 수 |

### 5.2 핵심 개념과 보안 연결

| 개념 | AI 원리 | 보안 연결 |
|---|---|---|
| Diffusion | score-based reverse sampling | 고품질 synthetic media와 provenance 필요 |
| Video diffusion | temporal consistency와 조건부 생성 | 영상 딥페이크와 identity consistency 위험 |
| GAN | generator-discriminator 경쟁 | 생성 품질과 detector arms race |
| Deepfake detection | real/fake score 기반 분류 | FPR/FNR, calibration, cross-domain reliability |
| Review-band triage | 불확실 score를 human review로 전송 | 자동판정 위험 감소, 검토 비용 증가 |
| Provenance | 생성물 출처·watermark·로그 관리 | 포렌식 신뢰성, 책임성 확보 |

---

## 6. 보안 이슈 30% 정리

Deepfake 생성과 탐지는 허위정보, 사칭, 증거 조작, 평판 훼손, 금융사기, 정치적 조작 등 사회적·보안적 위험과 연결된다. Deepfake detector reliability는 단순 accuracy가 아니라 transferability, robustness, interpretability, calibration을 함께 고려해야 한다. FPR은 실제 real media를 fake로 오탐해 false accusation을 만들고, FNR은 실제 조작물을 놓치는 missed detection 위험을 만든다.

| 보안 속성 | W06에서의 의미 | 대표 위협 | 평가 지표 |
|---|---|---|---|
| Integrity | 영상·이미지 증거의 무결성 훼손 | face swap, identity manipulation | FNR, missed detection |
| Confidentiality | 얼굴·음성·개인정보 기반 합성 위험 | identity misuse, privacy violation | provenance, consent evidence |
| Safety | 허위정보와 사칭으로 인한 사회적 피해 | deepfake misinformation | FPR/FNR, human review |
| Accountability | 생성물 출처·watermark·탐지 로그 필요 | provenance gap | audit log, watermark coverage |
| Reliability | 미지 생성기·압축·플랫폼 이동에서 탐지 실패 | cross-domain shift | AUROC, ECE, review rate |

---

## 7. Research Track 분석

### 7.1 연구문제

- RQ1. 딥페이크 탐지기는 in-domain 성능이 높을 때 cross-domain 조건에서도 신뢰할 수 있는가?
- RQ2. FPR과 FNR은 deepfake forensic workflow에서 어떤 다른 위험을 만드는가?
- RQ3. Review-band triage는 auto coverage와 review rate를 어떻게 trade-off하는가?
- RQ4. Diffusion/GAN 생성 품질 평가와 detector reliability 평가는 어떻게 분리되어야 하는가?

### 7.2 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 원본 이미지/영상, 신원 정보, synthetic media detector, detector score, threshold, review log, provenance metadata |
| 공격자 목표 | 허위 synthetic media 생성, 탐지 우회, FNR 증가, real media에 대한 false accusation 유도, provenance 제거 |
| 공격자 지식 | 생성기 종류 일부 지식, detector threshold 추정, platform compression/post-processing 활용 가능성 |
| 공격자 능력 | synthetic media 생성, 압축·후처리, platform shift 유도, detector score distribution 변화 유발 |
| 공격 경로 | media input → detector score → threshold decision → review routing → forensic decision |
| 방어자 능력 | cross-domain evaluation, calibration check, review-band triage, watermark/provenance, human review |
| 제외 범위 | 실제 딥페이크 생성, 실제 개인정보 얼굴·음성 사용, 탐지 우회 절차 제공, 무단 서비스 질의 |

### 7.3 평가축

| 평가축 | 질문 | 대표 지표 또는 증거 |
|---|---|---|
| In-domain performance | 기준 도메인에서 real/fake 분리가 잘 되는가 | accuracy, F1, FPR, FNR, AUROC |
| Cross-domain reliability | score shift 조건에서도 유지되는가 | accuracy drop, FPR/FNR increase, AUROC drop |
| Calibration | detector score가 신뢰도와 맞는가 | ECE |
| Human review routing | 자동판정과 검토 비율을 어떻게 나눌 것인가 | auto coverage, review rate |
| Reproducibility evidence | 같은 결과를 다시 만들 수 있는가 | seed, config, threshold, score distribution, CSV/JSON/run log |

### 7.4 재현성

재현성을 위해 seed, score distribution parameter, threshold, review band, detector decision rule, CSV/JSON/Markdown log를 보존한다. W06 실습은 synthetic detector score distribution을 사용하고, 실제 딥페이크 생성물이나 실제 개인정보 이미지를 사용하지 않는다.

---

## 8. 실습 보고서 및 그래프 수치 검증

본 실습은 실제 딥페이크 생성이나 실제 탐지 모델 평가가 아니라 W06의 핵심인 딥페이크 탐지 신뢰성 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. Synthetic real/fake detector score distribution과 threshold-based toy detector를 사용해 in-domain, cross-domain, review-band triage 조건을 분리한다.

### 8.1 실습 설계

| 항목 | 설정 |
|---|---|
| Dataset | synthetic real/fake detector score distributions |
| Detector | threshold-based toy deepfake detector |
| In-domain | real mean 0.22, fake mean 0.78, std 0.08 |
| Cross-domain | real mean 0.34, fake mean 0.61, std 0.16 |
| Threshold / review band | 0.50 / 0.40-0.60 |
| Seed | 42 |
| Outputs | `metrics_summary.csv`, `results.json`, `run_log.md` |

### 8.2 실습 결과 수치

| 조건 | Accuracy | F1 | FPR | FNR | AUROC | ECE | Auto coverage | Review rate | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| In-domain detector baseline | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 1.000000 | 0.216327 | 해당 없음 | 해당 없음 | 기준 도메인에서는 real/fake score 분리가 명확함 |
| Cross-domain reliability stress | 0.816667 | 0.813559 | 0.166667 | 0.200000 | 0.899722 | 0.147949 | 해당 없음 | 해당 없음 | score margin이 줄어 FPR/FNR trade-off 발생 |
| Review-band triage on shifted domain | 0.909091 | 0.901408 | 0.050000 | 0.135135 | 0.962162 | 0.174872 | 0.641667 | 0.358333 | 불확실 구간 35.8333%를 human review로 보내 자동판정 위험을 낮춤 |

In-domain accuracy가 1.000000이어도 cross-domain 조건에서는 accuracy가 0.816667로 떨어지고 FNR이 0.200000까지 증가했다. 이는 딥페이크 탐지에서 단일 benchmark 성능보다 transferability와 robustness를 분리해 기록해야 함을 보여준다. Review-band triage는 모든 샘플을 자동 판정하지 않고 0.40-0.60 불확실 구간을 human review로 보내 auto coverage를 0.641667로 낮추고, 자동판정 영역의 FPR을 0.050000, FNR을 0.135135로 낮춘다.

### 8.3 그래프 수치 검증

현재 제출 보고서의 그래프는 `assets/w06_metric_chart.png`를 참조한다. 확인 가능한 SVG 그래프에는 `accuracy`, `f1`, `false_positive_rate`, `false_negative_rate`, `auroc` 다섯 series가 표시되어 있다. ECE, auto coverage, review rate는 표에는 포함하지만 현재 그래프 series에는 포함되어 있지 않다.

| 조건 | 그래프 Accuracy | 표 Accuracy | 그래프 F1 | 표 F1 | 그래프 FPR | 표 FPR | 그래프 FNR | 표 FNR | 그래프 AUROC | 표 AUROC | 확인 결과 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| In-domain detector baseline | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | 일치 |
| Cross-domain reliability stress | 0.816667 | 0.816667 | 0.813559 | 0.813559 | 0.166667 | 0.166667 | 0.200000 | 0.200000 | 0.899722 | 0.899722 | 일치 |
| Review-band triage on shifted domain | 0.909091 | 0.909091 | 0.901408 | 0.901408 | 0.050000 | 0.050000 | 0.135135 | 0.135135 | 0.962162 | 0.962162 | 일치 |

<!-- submission-metric-chart:start -->
**그림 1. W06 metrics summary chart**

![W06 metrics summary chart](assets/w06_metric_chart.png)

출처: `04_experiment/outputs/metrics_summary.csv`. 이 그래프는 공개 toy/synthetic 산출물 기반이며 실제 공격 성능이나 운영 환경 성능으로 일반화하지 않는다. 현재 그래프는 accuracy, F1, FPR, FNR, AUROC를 시각화한다.
<!-- submission-metric-chart:end -->

---

## 9. 기말논문 연결

W06는 기말논문에서 “딥페이크 탐지기의 cross-domain reliability 평가 프레임워크”로 확장할 수 있다. 핵심 기여 후보는 diffusion/GAN 생성 원리와 딥페이크 탐지 신뢰성의 분리, FPR/FNR 중심 평가표, review-band triage, seed/config/output 기반 재현성 기록이다.

| 기말논문 장 | W06 반영 내용 |
|---|---|
| 1장 서론 | 합성미디어 확산과 deepfake detector 과신 문제 제시 |
| 2장 관련연구 | diffusion, video diffusion, GAN, deepfake detection, reliability 문헌 정리 |
| 3장 위협모형 | synthetic media, detector score, threshold, platform shift, review workflow 공격면 정의 |
| 4장 연구방법 | FPR, FNR, AUROC, ECE, auto coverage, review rate 설계 |
| 5장 분석 | in-domain/cross-domain/review-band triage 결과 비교 |
| 6장 결론 | 생성 품질과 detector reliability는 분리해 평가해야 함 |

---

## 10. AI 도구 활용 기록

AI 도구는 문헌 요약, 코드 점검, 문장 구조화, 그래프 생성 보조에 사용하였다. 모든 DOI/URL, 실험 수치, 본문 인용, 결론은 작성자가 outputs 파일과 로컬 참고문헌 검증표를 대조하여 검증한다.

| 항목 | 내용 |
|---|---|
| 사용 도구명 | Codex, ChatGPT 계열 도구 |
| 사용 목적 | 문헌 요약 정리, 보고서 구조화, 안전한 toy/synthetic 실험 결과 표기 점검, 그래프 생성 보조, 제출 전 체크리스트 정리 |
| AI 산출물 반영 위치 | `07_week_submission/w06_submission_report.md`, `07_week_submission/assets/w06_metric_chart.png`, `05_ai_worklog/ai_disclosure_draft.md` |
| 본인 수정 내용 | 주차별 문헌 상태 확인, 실험 수치와 outputs 대조, 안전 범위와 한계 문장 확인, 최종 제출 전 미확정 문헌 분리 |
| 사실관계 검증 방법 | `01_papers/paper_list.md`, `01_papers/doi_check.md`, 강의계획서 문헌표 대조 |
| 실험결과 검증 방법 | `04_experiment/experiment_report.md`, `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md`의 수치와 보고서 표기 대조 |
| 최종 책임 확인 | AI 산출물은 초안 보조이며 최종 제출자는 원고 내용, 인용, 실험결과, 연구윤리 책임을 확인한다. |

---

## 11. 제출 전 자기 점검표

| 점검 항목 | 상태 | 비고 |
|---|---|---|
| 메타정보 작성 | 완료 | 작성일 2026-06-26 반영 |
| 초록 및 키워드 작성 | 완료 |  |
| AI 원리 70% 정리 | 완료 | 핵심 수식 추가 |
| 보안 이슈 30% 정리 | 완료 |  |
| 논문 5편 서술형 요약 | 완료 |  |
| 논문 간 연결 관계 작성 | 완료 |  |
| Research Track 5요소 작성 | 완료 | 연구문제, 위협모형, 평가방법, 재현성, 한계 |
| P01~P05 PDF blob 확인 | 완료 | GitHub 파일 존재 확인. 원문 PDF 저작권/배포 정책 별도 검토 필요 |
| P01~P05 DOI/URL 검증 | 완료 / 확인 필요 | P02/P03/P05는 강의계획서 표기 차이 확인 필요 |
| P02 지정 논문 동일 여부 | 확인 필요 | 강의계획서 `Ananya Högele et al.` 표기와 차이 |
| P03 강의계획서 저자명 | 확인 필요 | 강의계획서 `Tianqi Wang et al.` 표기와 차이 |
| P04 Article 번호 | 확인 필요 | DOI 확인, Article 번호 추가 확인 필요 |
| P05 강의계획서 저자 표기 | 확인 필요 | `J. Wang et al.` 표기 확인 필요 |
| 실험 outputs 파일 존재 확인 | 완료 | 실험 보고서 기준 CSV/JSON/run_log 존재 |
| 실험 결과와 보고서 수치 일치 | 완료 | 실험 보고서 수치 기준 반영 |
| 그래프 수치 확인 | 완료 | accuracy/F1/FPR/FNR/AUROC 기준 표와 일치 |
| AI 활용 고지 작성 | 완료 |  |
| DOCX/PDF 제출본 생성 | 필요 | `07_week_submission/exports/` 권장 |
| 최종 사람이 검토할 항목 표시 | 완료 | P02/P03/P05 동일성, PDF 보관 정책, Word/PDF 렌더링 |

---

## 12. 참고문헌 검증표

| 번호 | 참고문헌 | DOI/URL | 상태 | 비고 |
|---:|---|---|---|---|
| [1] | Ling Yang et al., “Diffusion Models: A Comprehensive Survey of Methods and Applications,” ACM Computing Surveys, 2024 | `https://doi.org/10.1145/3626235`; arXiv `https://arxiv.org/abs/2209.00796` | DOI 확인 | Article 105 확인 |
| [2] | Zhen Xing et al., “A Survey on Video Diffusion Models,” ACM Computing Surveys, 2024/2025 | `https://doi.org/10.1145/3696415`; arXiv `https://arxiv.org/abs/2310.10647` | DOI 확인 | 강의계획서 지정 P02 동일 여부와 Article 번호 확인 필요 |
| [3] | Zhengwei Wang, Qi She, Tomas E. Ward, “Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy,” ACM Computing Surveys, 2021/2022 | `https://doi.org/10.1145/3439723`; arXiv `https://arxiv.org/abs/1906.01529` | DOI 확인 | 강의계획서 저자명 차이 확인 필요 |
| [4] | Yisroel Mirsky, Wenke Lee, “The Creation and Detection of Deepfakes: A Survey,” ACM Computing Surveys, 2021/2022 | `https://doi.org/10.1145/3425780`; arXiv `https://arxiv.org/abs/2004.11138` | DOI 확인 | Article 번호 추가 확인 필요 |
| [5] | Tianyi Wang et al., “Deepfake Detection: A Comprehensive Survey from the Reliability Perspective,” ACM Computing Surveys, 2024/2025 | `https://doi.org/10.1145/3699710`; arXiv `https://arxiv.org/abs/2211.10881` | DOI 확인 | 강의계획서 `J. Wang et al.` 표기 확인 필요 |

---

## 13. 부록 A. KCI 논문 형식 전환 아이디어

### A.1 제목 후보

| 번호 | 국문 제목 후보 | 영문 제목 후보 | 대상 시스템 | 보안 위협 | 연구방법 | 예상 기여 |
|---:|---|---|---|---|---|---|
| 1 | 딥페이크 탐지기의 Cross-Domain Reliability 평가 프레임워크 연구 | A Study on a Cross-Domain Reliability Evaluation Framework for Deepfake Detectors | Synthetic media detector | 미지 생성기, 압축, 플랫폼 shift | 문헌분석 + synthetic score 실험 | FPR/FNR·review routing 평가표 |
| 2 | 생성모형 품질 평가와 딥페이크 포렌식 탐지 신뢰성 평가의 분리 기준 연구 | A Study on Separating Generative Model Quality Evaluation from Deepfake Forensic Detection Reliability Evaluation | Diffusion/GAN 기반 합성미디어 | 탐지기 과신, 포렌식 오류 | 비교분석 + 체크리스트 | 생성 품질·탐지 신뢰성 분리 |
| 3 | Human Review Routing을 포함한 딥페이크 탐지 평가체계 연구 | A Deepfake Detection Evaluation Framework with Human Review Routing | Forensic review workflow | false accusation, missed detection | synthetic score 실험 + review-band triage | 자동판정률과 검토율 동시 평가 |

추천 제목은 “딥페이크 탐지기의 Cross-Domain Reliability 평가 프레임워크 연구”이다. 연구문제는 in-domain/cross-domain 지표 차이, FPR/FNR/AUROC/ECE의 설명력, review-band triage의 자동판정률과 검토율 변화로 구성한다.

### A.2 연구문제

- RQ1. In-domain benchmark 성능과 cross-domain reliability는 얼마나 다르게 나타나는가?
- RQ2. FPR과 FNR은 딥페이크 포렌식 워크플로우에서 어떤 다른 위험을 만드는가?
- RQ3. Review-band triage는 자동판정률과 human review 부담을 어떻게 조정하는가?

---

## 14. 부록 B. SCI 논문 형식 전환 아이디어

SCI 제목 후보는 “A Cross-Domain Reliability Evaluation Framework for Deepfake Detectors: Integrating FPR, FNR, Calibration, Review-Band Triage, and Reproducibility Evidence”이다.

Structured abstract는 Background, Problem, Method, Results, Contribution, Implications로 구성한다. 결과 문장은 W06 toy evaluation이 in-domain accuracy 1.000000, cross-domain accuracy 0.816667, cross-domain FNR 0.200000, review-band auto coverage 0.641667, review rate 0.358333을 기록했다는 수준으로 제한한다. 실제 딥페이크 detector 성능이나 법적 포렌식 증거능력으로 일반화하지 않는다.

| 연구축 | 대표 논문 | 역할 |
|---|---|---|
| Diffusion models | Yang et al. | diffusion/score-based model과 조건부 생성 원리 |
| Video diffusion models | Xing et al. | temporal synthetic media와 video generation |
| GANs in computer vision | Zhengwei Wang et al. | GAN 생성 구조와 품질 지표 |
| Deepfake creation/detection | Mirsky and Lee | 딥페이크 위협모형과 탐지 기술 |
| Deepfake detection reliability | Tianyi Wang et al. | robustness, transferability, interpretability, reliability |

---

## 15. 부록 C. 제출 파일 위치와 변환 권장

| 파일 | 설명 |
|---|---|
| `07_week_submission/w06_submission_report.md` | 본 제출용 보고서 원본 |
| `07_week_submission/assets/w06_metric_chart.png` | 제출 보고서 그래프 |
| `04_experiment/experiment_report.md` | 실험 근거 보고서 |
| `04_experiment/outputs/` | 실험 결과 근거 파일 위치 |
| `05_ai_worklog/ai_disclosure_draft.md` | AI 활용 고지 근거 |

Word 제출본은 다음 위치에 생성해 관리한다.

```text
03_weekly_reports/w06_diffusion_gan_deepfake/07_week_submission/exports/w06_submission_report.docx
```

PDF 제출본은 Word에서 최종 육안 검수 후 다음 위치에 저장한다.

```text
03_weekly_reports/w06_diffusion_gan_deepfake/07_week_submission/exports/w06_submission_report.pdf
```

수식은 GitHub와 Word 변환을 모두 고려하여 Markdown 표 안에 넣지 않고, `$$...$$` block math로 유지한다.
