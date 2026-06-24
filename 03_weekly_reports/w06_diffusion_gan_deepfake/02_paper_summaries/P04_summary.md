# P04 Summary

## The Creation and Detection of Deepfakes: A Survey — Yisroel Mirsky, Wenke Lee, ACM Computing Surveys, 2021/2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W06 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| 논문명 | The Creation and Detection of Deepfakes: A Survey |
| 저자 | Yisroel Mirsky, Wenke Lee |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 54, No. 1, pp. 1–41, online 2021-01-02, print issue 2022-01-31 |
| DOI | https://doi.org/10.1145/3425780 |
| 보조 URL | https://arxiv.org/abs/2004.11138 |
| 로컬 PDF | `01_papers/pdf/04_Mirsky_Lee_2021_Creation_Detection_Deepfakes.pdf` |
| 검증 상태 | W06 `paper_list.md` 기준 DOI/URL 확인. 로컬 PDF는 arXiv/ACM preprint 양식이며 참고문헌에는 ACM DOI 우선 사용 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W06에서 deepfake 생성·검출 taxonomy와 보안적 함의를 직접 제공하는 핵심 문헌 |

---

## 1. 한 문장 요약

이 논문은 딥페이크의 생성과 검출을 **face swap, face reenactment, expression transfer, lip-sync, audio/visual manipulation, detector artifact, biological signal, temporal inconsistency, forensic cue, social impact** 관점에서 체계화하며, W06의 핵심 보안 위협모형과 검출 평가 기준을 제공하는 중심 survey 문헌이다.

---

## 2. 핵심 연구문제

> 딥페이크는 어떤 생성 파이프라인으로 만들어지고, 방어자는 어떤 artifact·생체 신호·시간축 일관성·metadata/provenance 단서를 사용해 검출하며, 이 기술이 사회적 신뢰와 보안에 어떤 위험을 만드는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | 딥페이크 생성은 face swap, face reenactment, expression transfer, lip-sync, voice cloning 등 어떤 범주로 나눌 수 있는가? |
| RQ2 | GAN·autoencoder·3D face model·audio-visual synthesis 등 생성기법은 어떤 조작 능력과 한계를 갖는가? |
| RQ3 | 딥페이크 검출기는 spatial artifact, temporal inconsistency, physiological signal, frequency artifact, metadata/provenance를 어떻게 활용하는가? |
| RQ4 | Compression, resizing, re-encoding, platform upload, adversarial post-processing은 검출 성능을 어떻게 약화시키는가? |
| RQ5 | 딥페이크 탐지는 기술적 정확도뿐 아니라 명예훼손, 사기, 여론조작, 허위 증거, 개인정보 침해 등 사회적 피해를 어떻게 고려해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W06 연결 |
|---|---|---|
| Deepfake creation taxonomy | face swap, reenactment, lip-sync, synthesis 등 생성 방식을 분류 | W06의 딥페이크 공격면 정의 |
| Deepfake detection taxonomy | artifact 기반, physiological cue 기반, temporal cue 기반 검출을 정리 | 검출 평가 지표 설계 |
| Threat and impact discussion | 개인·사회·정치·법적 피해를 논의 | 보안적 함의 장 반영 |
| Attack-defense arms race | 생성기와 검출기의 경쟁적 발전을 설명 | P01/P02/P03 생성모형과 연결 |
| Practical limitation 정리 | dataset bias, compression, cross-dataset generalization 한계 제시 | W06 reliability 평가와 P05 연결 |

---

## 4. 핵심 이론 및 수식

> 아래 수식은 딥페이크 생성·검출 문제를 W06 보고서에서 계량화하기 위해 표준화한 표현이다. 공격 절차를 제공하기 위한 것이 아니라, 평가 지표와 위협모형을 설명하기 위한 정식화다.

### 4.1 Binary Deepfake Detection

딥페이크 검출은 입력 이미지·영상·음성-영상 clip이 real인지 fake인지 분류하는 문제로 정식화할 수 있다.

$$
\hat{y}=f_\theta(x), \qquad \hat{y}\in\{real, fake\}
$$

| 기호 | 의미 |
|---|---|
| $x$ | 입력 이미지, 영상, audio-visual clip |
| $f_\theta$ | deepfake detector |
| $\hat{y}$ | real/fake 예측 |

### 보안적 의미

Real/fake 이진분류는 기본 구조이지만, 실제 환경에서는 threshold, compression, domain shift, 생성기 변화, human review가 성능을 크게 좌우한다.

---

### 4.2 Precision, Recall, F1

딥페이크 검출은 오탐과 미탐을 분리해 평가해야 한다.

$$
Precision=\frac{TP}{TP+FP}, \qquad Recall=\frac{TP}{TP+FN}
$$

$$
F1=\frac{2\cdot Precision\cdot Recall}{Precision+Recall}
$$

| 기호 | 의미 |
|---|---|
| $TP$ | fake를 fake로 올바르게 탐지 |
| $FP$ | real을 fake로 오탐 |
| $FN$ | fake를 real로 미탐 |

### 보안적 의미

미탐은 허위 영상 유포를 허용하고, 오탐은 실제 영상의 신뢰를 훼손한다. 따라서 accuracy 하나만으로 딥페이크 검출을 평가하면 부족하다.

---

### 4.3 False Positive Rate와 False Negative Rate

실제 운영에서는 FPR과 FNR의 사회적 비용이 다르다.

$$
FPR=\frac{FP}{FP+TN}, \qquad FNR=\frac{FN}{FN+TP}
$$

| 지표 | 의미 |
|---|---|
| FPR | 정상 영상을 fake로 잘못 판정한 비율 |
| FNR | fake 영상을 정상으로 놓친 비율 |

### 보안적 의미

뉴스, 법정 증거, 정치 영상, 의료 영상에서는 FPR/FNR 모두 큰 피해를 유발한다. 따라서 detector는 고위험 도메인에서 human review와 provenance 확인을 병행해야 한다.

---

### 4.4 Video-level Detection Score

영상은 여러 frame으로 구성되므로 frame-level score를 video-level score로 집계해야 한다.

$$
Score_{video}=Agg\left(\{s_i=f_\theta(x_i)\}_{i=1}^{T}\right)
$$

| 기호 | 의미 |
|---|---|
| $x_i$ | $i$번째 frame |
| $s_i$ | frame-level fake score |
| $Agg$ | 평균, 최대값, temporal model 등 집계 함수 |
| $T$ | frame 수 |

### 보안적 의미

몇 개 frame만 조작되거나, 압축·편집으로 artifact가 희석될 수 있다. 따라서 frame 단위와 video 단위 평가를 모두 기록해야 한다.

---

### 4.5 Temporal Consistency Score

딥페이크 영상은 frame 간 정체성·표정·조명·움직임의 불일치가 단서가 될 수 있다.

$$
TemporalInconsistency=\frac{1}{T-1}\sum_{i=1}^{T-1}\left\|\Phi(x_i)-\Phi(x_{i+1})\right\|_2
$$

| 기호 | 의미 |
|---|---|
| $\Phi$ | face embedding, optical-flow feature, physiological signal feature 등 |
| $x_i$ | $i$번째 frame |

### 보안적 의미

Temporal inconsistency는 video deepfake 검출의 중요한 단서다. 그러나 최신 video diffusion 또는 고품질 face reenactment는 이 단서를 약화시킬 수 있으므로 cross-model 평가가 필요하다.

---

## 5. Deepfake 생성 Taxonomy

| 생성 유형 | 설명 | 보안 위험 |
|---|---|---|
| Face Swap | 한 사람의 얼굴을 다른 사람 얼굴로 교체 | 신원 사칭, 명예훼손 |
| Face Reenactment | 표정·머리 움직임·입 모양을 다른 사람에게 전이 | 허위 발언 영상 생성 |
| Expression Transfer | 표정만 조작 | 정서·의도 왜곡 |
| Lip-sync | 음성과 입술 움직임을 맞춤 | 허위 발화·사회공학 |
| Voice Cloning | 음성 특성을 모방 | 보이스피싱, 인증 우회 |
| Full-body/Scene Synthesis | 인물과 배경을 함께 생성 | 허위 사건·증거 생성 |

---

## 6. Deepfake 검출 Taxonomy

| 검출 축 | 설명 | 대표 지표 |
|---|---|---|
| Spatial Artifact | 얼굴 경계, 피부 질감, 눈·치아·머리카락 artifact | AUC, F1 |
| Temporal Artifact | frame 간 flicker, identity drift, motion inconsistency | temporal consistency score |
| Biological Signal | blink, pulse, breathing, face physiology | signal consistency |
| Frequency Cue | 주파수 영역 artifact, compression trace | frequency detector AUC |
| Audio-visual Consistency | 음성과 입술·표정 정합성 | AV sync score |
| Metadata/Provenance | 생성·편집·압축 이력 확인 | provenance coverage |
| Human Review | 사람이 맥락·출처·의도를 검토 | human agreement |

---

## 7. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W06/P04에서의 의미 |
|---|---|---|
| 생성모형 | GAN, autoencoder, diffusion 등 합성 모델의 기반 | 딥페이크 생성 원리 |
| Representation Transfer | 신원·표정·동작·음성 특성의 분리와 전이 | face swap, reenactment 설명 |
| Detector Learning | real/fake 분류기 학습 | 검출 모델의 기본 구조 |
| Temporal Modeling | frame 간 관계와 동작 정합성 모델링 | video deepfake 검출 |
| Multimodal Alignment | audio, lip, face, text 정합성 | lip-sync deepfake 탐지 |
| Generalization | 보지 못한 생성기·데이터셋에서도 성능 유지 | detector reliability 핵심 |

---

## 8. 보안 이슈 30% 관점 분석

| 보안 항목 | Deepfake 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 얼굴·음성·개인 식별정보가 합성·재사용될 수 있음 | identity similarity, re-identification risk |
| 무결성 | 영상 증거·발언·행동 기록이 조작될 수 있음 | detection AUC, FNR |
| 가용성 | 대량 deepfake가 검토 시스템과 플랫폼 moderation을 압박 | review cost, throughput |
| 프라이버시 | 개인 얼굴·음성의 무단 사용과 2차 피해 발생 | consent/provenance check |
| 안전성 | 의료·정치·재난·법률 영상에서 잘못된 판단 유도 | high-stakes review flag |
| 책임성 | 생성·편집·유통 경로를 추적하지 못하면 책임소재 불명확 | watermark, provenance, audit completeness |

---

## 9. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 얼굴, 음성, 신원, 발언 기록, 영상 원본성, 사회적 신뢰, forensic evidence, provenance metadata |
| 공격자 목표 | 신원 사칭, 허위 발언 생성, 명예훼손, 사기, 여론조작, 증거 조작, 검출 회피 |
| 공격자 능력 | face swap, reenactment, lip-sync, voice cloning, post-processing, compression, platform upload |
| 공격 경로 | source media 수집 → 합성/편집 → 압축·재인코딩 → SNS/플랫폼 유포 → 탐지·검토 우회 |
| 방어자 능력 | deepfake detector, metadata/provenance 확인, watermark 검증, cross-dataset test, human review |
| 제외 범위 | 실제 인물 대상 deepfake 제작, 무단 얼굴·음성 데이터 사용, 악의적 배포, 탐지 우회 절차 제공 |

---

## 10. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W06/P04 활용 |
|---|---|---|---|
| 기본 검출 | AUC, accuracy, precision, recall, F1 | real/fake 분류 성능 | baseline detector 평가 |
| 오류 비용 | FPR, FNR | 오탐·미탐 위험 | high-stakes 판단 |
| 일반화 | cross-dataset AUC, cross-generator performance | 다른 생성기·데이터셋에서 유지되는지 | detector overfitting 방지 |
| 강건성 | compression robustness, resize/crop/noise robustness | 플랫폼 업로드 후 검출 유지 | 실사용 환경 평가 |
| 시간축 | temporal consistency score, frame/video agreement | video deepfake artifact 평가 | P02 video diffusion 연결 |
| 오디오-비디오 | lip-sync consistency, AV mismatch score | 음성·입술 정합성 평가 | multimodal deepfake 검출 |
| 포렌식 | frequency artifact, metadata check | 합성 흔적과 편집 이력 확인 | forensic 평가 |
| 책임성 | provenance coverage, watermark verification | 생성·편집·유통 추적 | W13/W14/W15 연결 |

---

## 11. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| 데이터셋 | real/fake dataset, 생성기 종류, 인물/장면 분포, train/test split |
| 생성 조건 | face swap/reenactment/lip-sync 등 조작 유형, post-processing 조건 |
| 압축 조건 | codec, bitrate, resize, platform-like compression |
| 모델 | detector architecture, checkpoint, preprocessing, threshold |
| 평가 | AUC, F1, FPR/FNR, cross-dataset result, failure case |
| provenance | source media 여부, metadata, watermark, output hash |
| human review | 판정 기준, 검토자 수, disagreement 사례 |
| 한계 | 특정 데이터셋 성능을 실제 인터넷 환경 성능으로 일반화하지 않음 |

---

## 12. 논문의 고유 기여

1. 딥페이크 생성과 검출을 하나의 survey 안에서 함께 정리한다.
2. 얼굴 교체, 표정 재연, lip-sync, 음성 조작 등 다양한 생성 공격면을 분류한다.
3. 검출 방법을 spatial, temporal, biological, audio-visual, forensic cue로 나누어 설명한다.
4. 딥페이크 문제를 단순 기술 문제가 아니라 사회적 피해·신뢰·책임성 문제로 확장한다.
5. W06의 diffusion/GAN 생성모형 문헌(P01~P03)과 detection reliability 문헌(P05)을 연결하는 중심 문헌이다.

---

## 13. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 생성기 변화 속도 | 새로운 diffusion/video model이 등장하면 기존 검출기가 약해질 수 있다. | cross-generator, cross-dataset 평가 강조 |
| 데이터셋 편향 | 공개 데이터셋이 실제 플랫폼 영상과 다를 수 있다. | compression, platform-like processing 조건 추가 |
| 압축·재인코딩 영향 | SNS 업로드 후 artifact가 변할 수 있다. | robustness test와 FPR/FNR 병기 |
| 오탐의 사회적 비용 | real 영상을 fake로 오탐하면 신뢰 훼손이 발생한다. | human review와 provenance 확인 병행 |
| 윤리적 제약 | 실제 인물 deepfake 생성 실험은 위험하다. | 문헌 기반 분석과 synthetic/toy 사례로 제한 |

---

## 14. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 딥페이크가 생성형 AI 보안의 대표적 합성미디어 위협이라는 문제의식 |
| 2장 관련연구 | deepfake creation/detection taxonomy 정리 |
| 3장 위협모형 | 얼굴·음성·신원·영상 원본성·provenance 보호 자산 정의 |
| 4장 연구방법 | AUC, F1, FPR/FNR, cross-dataset, compression robustness, temporal consistency 지표 설계 |
| 5장 분석 | 생성-검출-provenance pipeline과 실패 사례 분석 |
| 6장 보안적 함의 | 명예훼손, 사기, 여론조작, 허위 증거, human review 필요성 해석 |

---

## 15. 기말논문 연결 3문장

1. W06에서 기말논문에 반영할 개념: 딥페이크는 생성형 AI의 합성 능력이 사회적 신뢰와 증거 무결성을 직접 흔드는 대표적 보안 위협이다.
2. W06에서 기말논문에 반영할 표·그림·실험: deepfake 생성 taxonomy, 검출 taxonomy, FPR/FNR·AUC·temporal consistency 평가표, provenance 확인 workflow를 반영한다.
3. W06이 RAG/LLM 보안 감사 프레임워크와 연결되는 지점: 합성 영상이 멀티모달 RAG나 AI 에이전트의 입력 근거로 사용되면, 영상 출처·watermark·metadata·human review를 W14/W15 evidence chain으로 관리해야 한다.

---

## 16. 최종 판단

P04는 W06의 핵심 보안 문헌이다. P01/P02/P03이 diffusion/GAN 기반 생성 원리를 설명한다면, P04는 생성 기술이 실제 딥페이크 위협으로 전환되는 방식과 이를 검출하기 위한 평가 기준을 제공한다. 따라서 W06 기말논문 연결에서는 P04를 **합성미디어 위협모형과 deepfake detection 평가표의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 17. 변환 호환성 메모

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
