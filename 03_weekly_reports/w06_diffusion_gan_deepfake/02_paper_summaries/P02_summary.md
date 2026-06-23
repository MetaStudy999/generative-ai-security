# P02 Summary

## A Survey on Video Diffusion Models — Zhen Xing et al., ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W06 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| 논문명 | A Survey on Video Diffusion Models |
| 저자 | Zhen Xing et al. |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 57, No. 2, pp. 1–42 |
| 연도 | online 2024 / print 2025 |
| DOI | https://doi.org/10.1145/3696415 |
| 보조 URL | https://arxiv.org/abs/2310.10647 |
| 로컬 PDF | `01_papers/pdf/02_Xing_et_al_2024_Video_Diffusion_Models_Survey.pdf` |
| 검증 상태 | W06 `paper_list.md` 기준 DOI 확인. 강의계획서 지정 P02와 제목·저자 차이 확인 필요 |

---

## 1. 한 문장 요약

이 논문은 video diffusion model을 **temporal consistency, spatial-temporal denoising, text-to-video generation, controllable generation, long video synthesis, evaluation** 관점에서 정리하며, W06에서 비디오 딥페이크와 생성 영상 검출·provenance 평가의 모델 배경을 제공한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | Image diffusion을 video diffusion으로 확장할 때 시간축 일관성은 어떻게 다루는가? |
| RQ2 | Text-to-video와 image-to-video 생성은 어떤 conditioning 구조를 사용하는가? |
| RQ3 | Frame flicker, temporal artifact, identity consistency는 검출 지표로 어떻게 활용되는가? |
| RQ4 | 생성 영상이 딥페이크·허위 증거·저작권·개인정보 위험을 어떻게 확대하는가? |

---

## 3. 핵심 수식

### 3.1 Video Denoising Objective

$$
\mathcal{L}_{video}=\mathbb{E}_{t,v_0,\epsilon}\left[\left\|\epsilon-\epsilon_\theta(v_t,t,c)\right\|_2^2\right]
$$

| 기호 | 의미 |
|---|---|
| $v_0$ | 원본 video clip |
| $v_t$ | noise가 추가된 video latent 또는 frame sequence |
| $c$ | text/image/control condition |
| $\epsilon_\theta$ | noise 예측 네트워크 |

### 3.2 Temporal Consistency

$$
\mathcal{L}_{temp}=\sum_{t}\left\|\Phi(\hat{v}_{t})-\Phi(\hat{v}_{t+1})\right\|_2^2
$$

**보안 해석:** 생성 영상은 단일 frame 품질뿐 아니라 시간적 정합성을 평가해야 한다. 딥페이크 검출도 frame-level artifact와 temporal artifact를 분리해야 한다.

---

## 4. AI 원리·보안 분석

| 항목 | 분석 |
|---|---|
| Temporal modeling | frame 간 일관성 유지가 핵심이다. |
| Conditioning | text, image, pose, motion condition이 영상 내용을 제어한다. |
| Long video | 긴 영상은 identity drift와 artifact 누적이 발생할 수 있다. |
| 보안 위험 | 인물 사칭, 허위 증거, 여론조작, 영상 워터마크 제거 위험이 있다. |
| 검출 단서 | flicker, temporal inconsistency, face identity drift, compression artifact가 단서가 될 수 있다. |

---

## 5. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 얼굴 영상, 음성-영상 정합성, identity, video provenance, watermark |
| 공격자 목표 | 조작 영상 생성, 신원 사칭, 검출 회피, 사회공학적 설득력 확보 |
| 공격자 능력 | text-to-video prompt, face reenactment, video editing, frame-level post-processing |
| 제외 범위 | 실제 인물 사칭 영상 제작, 무단 개인정보 영상 사용 |

---

## 6. 평가방법 및 지표

| 지표 | 의미 |
|---|---|
| FVD | video distribution quality |
| Temporal Consistency | frame 간 일관성 |
| Identity Consistency | 인물 정체성 유지 |
| Detection AUC/F1 | 합성 영상 검출 성능 |
| Robustness | 압축·재인코딩·크롭 후 검출 유지 |
| Provenance | 생성 로그·watermark·metadata 보존 |

---

## 7. 재현성·기말논문 연결

| 항목 | 반영 내용 |
|---|---|
| 재현성 | prompt, seed, model version, frame rate, sampler, output hash 기록 필요 |
| 한계 | toy 또는 문헌 기반 결과를 실제 딥페이크 탐지 성능으로 과장하지 않음 |
| 기말논문 | video deepfake threat model, temporal artifact, provenance/watermark 평가표에 반영 |

---

## 8. 최종 판단

P02는 W06에서 image diffusion을 video generation과 video deepfake 위험으로 확장하는 문헌이다. 단, 강의계획서 지정 문헌과 제목·저자 차이 메모는 유지해야 한다.
