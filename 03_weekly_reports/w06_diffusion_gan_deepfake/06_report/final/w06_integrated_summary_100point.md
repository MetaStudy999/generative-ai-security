# W06 100점형 통합 Summary

## 확률생성모형(Diffusion/GAN) & 딥페이크 검출

## 0. 문서 목적

이 문서는 W06 개별 논문 summary 5개를 기말논문 작성용 연구 노트로 통합한 100점형 요약본이다. 생성모형의 수학적 원리와 딥페이크 검출의 보안·신뢰성 평가축을 연결하는 데 사용한다.

| 항목 | 내용 |
|---|---|
| 주차 | W06 |
| 주제 | Diffusion/GAN 생성모형 & 딥페이크 검출 |
| 주요 문헌 | P01–P05 |
| 핵심 프레임 | diffusion generation + video diffusion + GAN + deepfake taxonomy + reliability-aware detection |
| 주의사항 | P02/P03/P05의 강의계획서 표기 차이와 PDF 공개 저장소 저작권 위험 메모 유지 |

---

## 1. 한 문장 통합 요약

W06은 생성모형을 **diffusion denoising, video temporal consistency, GAN minimax generation**으로 이해하고, 딥페이크 보안 평가는 생성 품질뿐 아니라 detection AUC, cross-dataset generalization, compression robustness, calibration, provenance, watermark, human review를 함께 봐야 함을 정리하는 주차다.

---

## 2. 문헌 5편 통합 매트릭스

| ID | 논문 | 핵심 역할 | 주요 수식/지표 | 기말논문 반영 위치 |
|---|---|---|---|---|
| P01 | Yang et al., *Diffusion Models* | diffusion forward/reverse/denoising 원리 | forward diffusion, denoising loss | 생성모형 배경, provenance 평가 |
| P02 | Xing et al., *Video Diffusion Models* | video generation과 temporal consistency | video denoising, temporal consistency | 영상 딥페이크 위협모형 |
| P03 | Wang/She/Ward, *GANs in Computer Vision* | GAN 생성과 detector arms race | minimax objective, detection rate | GAN 기반 딥페이크 배경 |
| P04 | Mirsky & Lee, *Creation and Detection of Deepfakes* | 딥페이크 생성·검출 taxonomy | precision/recall/F1 | 딥페이크 위협모형 |
| P05 | Wang et al., *Deepfake Detection Reliability* | 검출 신뢰성·일반화·calibration | reliability risk, ECE | 운영 신뢰성 평가 |

---

## 3. 핵심 수식 묶음

### 3.1 Diffusion Forward Process

$$
q(x_t\mid x_{t-1})=\mathcal{N}\left(x_t;\sqrt{1-\beta_t}x_{t-1},\beta_t I\right)
$$

### 3.2 Denoising Loss

$$
\mathcal{L}_{simple}=\mathbb{E}_{t,x_0,\epsilon}\left[\left\|\epsilon-\epsilon_\theta(x_t,t)\right\|_2^2\right]
$$

### 3.3 GAN Objective

$$
\min_G \max_D V(D,G)=\mathbb{E}_{x\sim p_{data}}[\log D(x)] + \mathbb{E}_{z\sim p_z}[\log(1-D(G(z)))]
$$

### 3.4 Deepfake Detection Metrics

$$
Precision=\frac{TP}{TP+FP}, \qquad Recall=\frac{TP}{TP+FN}
$$

$$
ECE=\sum_{m=1}^{M}\frac{|B_m|}{n}\left|acc(B_m)-conf(B_m)\right|
$$

---

## 4. 통합 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 얼굴·음성·영상 원본성, 신원, 저작물, provenance, watermark, 검출 로그 |
| 공격자 목표 | 합성 이미지/영상 생성, 신원 사칭, 허위 증거 생성, 검출 우회 |
| 공격자 능력 | prompt 기반 생성, face swap, reenactment, lip-sync, post-processing, 압축 |
| 방어자 능력 | 딥페이크 검출, watermark/provenance 확인, cross-dataset 평가, human review |
| 제외 범위 | 실제 인물 사칭물 제작, 무단 개인정보 영상 사용, 유해 합성물 생성 |

---

## 5. 통합 평가 지표

| 평가축 | 대표 지표 | 해석 |
|---|---|---|
| 생성 품질 | FID, FVD, CLIP score | 합성물 품질·정합성 |
| 검출 성능 | AUC, F1, precision, recall | real/fake 구분 성능 |
| 일반화 | cross-dataset AUC | 다른 생성기·플랫폼에서 유지되는지 |
| 강건성 | compression robustness, robustness drop | 압축·크롭·재인코딩 후 성능 |
| 신뢰성 | ECE, threshold stability | confidence calibration |
| 책임성 | provenance coverage, watermark robustness | 생성·편집·검토 추적 가능성 |

---

## 6. 재현성 체크리스트

| 항목 | 필수 기록 |
|---|---|
| 생성모형 | model name, version, sampler, seed, prompt, guidance scale |
| 영상 조건 | frame rate, resolution, temporal sampling, compression setting |
| 검출모형 | detector checkpoint, threshold, preprocessing, dataset version |
| 결과 | AUC, F1, FPR/FNR, ECE, robustness drop, failure cases |
| 한계 | toy/문헌 기반 결과를 실제 인터넷 환경 신뢰성으로 과장하지 않음 |

---

## 7. 기말논문 연결 3문장

1. W06에서 기말논문에 반영할 개념: 생성형 AI 보안은 생성모형의 품질 경쟁만이 아니라 생성물 provenance, 딥페이크 검출 신뢰성, calibration, human review를 포함해야 한다.
2. 반영할 표·그림·실험: diffusion/GAN 수식, 생성-검출 pipeline, AUC/F1/ECE/robustness/provenance 평가표를 반영한다.
3. RAG/LLM 보안 연결: 합성 이미지·영상은 멀티모달 RAG의 오염된 근거 자료가 될 수 있으므로 생성물 출처와 검출 로그를 W08/W14 감사체계로 확장한다.

---

## 8. 최종 판단

W06은 생성형 AI의 공격 가능성과 검출 신뢰성을 함께 다루는 핵심 주차다. P01/P02/P03은 생성 원리, P04/P05는 딥페이크 검출과 reliability 평가를 담당한다.
