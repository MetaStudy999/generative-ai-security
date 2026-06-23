# P04 Summary

## The Creation and Detection of Deepfakes: A Survey — Yisroel Mirsky, Wenke Lee, ACM Computing Surveys, 2021

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W06 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| 논문명 | The Creation and Detection of Deepfakes: A Survey |
| 저자 | Yisroel Mirsky, Wenke Lee |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 54, No. 1, pp. 1–41 |
| DOI | https://doi.org/10.1145/3425780 |
| 보조 URL | https://arxiv.org/abs/2004.11138 |
| 로컬 PDF | `01_papers/pdf/04_Mirsky_Lee_2021_Creation_Detection_Deepfakes.pdf` |
| 검증 상태 | W06 `paper_list.md` 기준 DOI/URL 확인. 로컬 PDF는 preprint 양식 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 딥페이크의 생성과 검출을 **face swap, reenactment, lip-sync, audio/visual manipulation, detection artifact, forensic cues, social impact** 관점에서 정리하며, W06의 핵심 보안 위협모형과 검출 평가 기준을 제공한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | 딥페이크는 얼굴 교체, 표정 재연, 음성·입술 동기화 등 어떤 방식으로 생성되는가? |
| RQ2 | 검출기는 spatial artifact, temporal inconsistency, physiological cue를 어떻게 활용하는가? |
| RQ3 | 압축·재인코딩·소셜미디어 업로드는 검출 성능을 어떻게 약화시키는가? |
| RQ4 | 딥페이크 탐지는 기술 지표와 사회적 피해 평가를 어떻게 함께 고려해야 하는가? |

---

## 3. 핵심 수식

### 3.1 Binary Deepfake Detection

$$
\hat{y}=f_\theta(x), \qquad \hat{y}\in\{real, fake\}
$$

### 3.2 검출 지표

$$
Precision=\frac{TP}{TP+FP}, \qquad Recall=\frac{TP}{TP+FN}
$$

$$
F1=\frac{2\cdot Precision\cdot Recall}{Precision+Recall}
$$

**보안 해석:** 딥페이크 검출에서는 fake를 놓치는 FN과 real을 fake로 오탐하는 FP가 모두 사회적 비용을 갖는다. 따라서 accuracy 하나로 평가하면 부족하다.

---

## 4. 생성·검출 Taxonomy

| 축 | 내용 |
|---|---|
| 생성 | face swap, face reenactment, expression transfer, lip-sync, voice cloning |
| 검출 | spatial artifact, temporal artifact, biological signal, frequency cue, metadata/provenance |
| 공격면 | post-processing, compression, adversarial perturbation, detector overfitting |
| 피해 | 명예훼손, 사기, 여론조작, 증거 조작, 개인정보 침해 |

---

## 5. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 얼굴·음성·정체성·영상 원본성·사회적 신뢰 |
| 공격자 목표 | 신원 사칭, 허위 영상 배포, 검출 회피, 사회공학 공격 |
| 공격자 능력 | 합성도구 사용, post-processing, compression, 플랫폼 업로드 |
| 방어자 능력 | 검출 모델, metadata 확인, provenance/watermark, human review |
| 제외 범위 | 실제 인물 대상 딥페이크 제작, 악의적 배포, 무단 데이터 수집 |

---

## 6. 평가방법 및 지표

| 지표 | 의미 |
|---|---|
| AUC | threshold 독립 검출 성능 |
| Precision/Recall/F1 | 오탐·미탐 균형 |
| Cross-dataset Performance | 생성기·데이터셋 변화 일반화 |
| Compression Robustness | 재인코딩 후 검출 유지 |
| Temporal Consistency Score | frame 간 artifact 평가 |
| Human Review Agreement | 사람 검토와 모델 검출 일치성 |

---

## 7. 재현성·기말논문 연결

| 항목 | 반영 내용 |
|---|---|
| 재현성 | 데이터셋, 생성기, 압축 조건, detector version, threshold 기록 필요 |
| 한계 | 특정 데이터셋 성능을 실제 인터넷 환경 성능으로 일반화하지 않음 |
| 기말논문 | 딥페이크 위협모형, 검출 지표, 사회적 피해·책임성 장에 반영 |

---

## 8. 최종 판단

P04는 W06의 핵심 보안 문헌이다. 생성기 원리는 P01/P03이 제공하고, 딥페이크 위협·검출·사회적 함의는 P04가 담당한다.
