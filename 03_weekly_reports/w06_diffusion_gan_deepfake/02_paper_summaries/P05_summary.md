# P05 Summary

## Deepfake Detection: A Comprehensive Survey from the Reliability Perspective — Tianyi Wang et al., ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W06 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| 논문명 | Deepfake Detection: A Comprehensive Survey from the Reliability Perspective |
| 저자 | Tianyi Wang, Xin Liao, Kam Pui Chow, Xiaodong Lin, Yinglong Wang |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 57, No. 3, pp. 1–35, online 2024-11-11, print issue 2025-03-31 |
| DOI | https://doi.org/10.1145/3699710 |
| 보조 URL | https://arxiv.org/abs/2211.10881 |
| 로컬 PDF | `01_papers/pdf/05_Wang_et_al_2024_Deepfake_Detection_Reliability_Survey.pdf` |
| 검증 상태 | W06 `paper_list.md` 기준 DOI/URL 확인. 강의계획서의 `J. Wang et al.` 표기는 축약 또는 오기 가능성이 있어 추가 확인 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W06에서 deepfake detection을 단순 분류 성능이 아닌 reliability 관점으로 확장하는 핵심 문헌 |

---

## 1. 한 문장 요약

이 논문은 딥페이크 검출을 단순한 real/fake 이진분류 문제가 아니라 **generalization, robustness, interpretability, calibration, fairness, open-set detection, benchmark reliability, deployment reliability**가 결합된 신뢰성 평가 문제로 재정의하며, W06에서 딥페이크 검출기를 실제 운영환경에 적용하기 위한 핵심 평가 기준을 제공한다.

---

## 2. 핵심 연구문제

> 딥페이크 검출기가 특정 데이터셋에서 높은 성능을 보이더라도, 생성기 변화·데이터셋 변화·압축·후처리·플랫폼 환경·집단별 편차·새로운 조작 방식에 대해 신뢰할 수 있는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Deepfake detector의 높은 in-domain 성능이 실제 환경 신뢰성을 보장하지 않는 이유는 무엇인가? |
| RQ2 | Cross-dataset, cross-manipulation, cross-generator 환경에서 검출 성능은 어떻게 변하는가? |
| RQ3 | Compression, resizing, blur, noise, crop, re-encoding, social-media upload는 검출 강건성을 어떻게 약화시키는가? |
| RQ4 | Detector confidence가 실제 정확도와 일치하지 않을 때 어떤 운영 리스크가 발생하는가? |
| RQ5 | Interpretability, fairness, open-set detection, human review, provenance evidence를 딥페이크 검출 평가에 어떻게 결합해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W06 연결 |
|---|---|---|
| Reliability perspective 제시 | 딥페이크 검출을 accuracy 중심이 아니라 신뢰성 중심으로 재분류 | W06의 deepfake detection reliability 핵심 |
| Generalization 문제 정리 | 다른 데이터셋·생성기·조작 유형에서 성능이 떨어지는 문제 제시 | cross-dataset/cross-generator 평가 지표 연결 |
| Robustness 문제 정리 | 압축·노이즈·크롭·후처리·adversarial perturbation에 대한 취약성 정리 | 실사용 플랫폼 환경 평가 |
| Interpretability·calibration·fairness 포함 | 검출 근거, confidence 신뢰성, 집단별 성능 차이를 평가축에 포함 | 보안적 함의와 책임성 연결 |
| Future direction 제시 | open-set, deployment, human-in-the-loop, provenance 기반 검증 필요성 제기 | W14/W15 evidence chain 연결 |

---

## 4. 핵심 이론 및 수식

> 아래 수식은 딥페이크 검출 reliability 문제를 W06 보고서에서 설명하기 위한 표준화된 평가 표현이다. 원문 수식 직접 전사가 아니라, 논문의 관점을 보고서용 지표로 정리한 것이다.

### 4.1 Reliability-Aware Detection Risk

딥페이크 검출의 운영 리스크는 미탐, 오탐, calibration error, 검토 비용을 함께 고려해야 한다.

$$
Risk_{det}=\alpha FN+\beta FP+\gamma ECE+\lambda Cost
$$

| 기호 | 의미 |
|---|---|
| $FN$ | fake를 real로 놓치는 미탐 |
| $FP$ | real을 fake로 오탐 |
| $ECE$ | Expected Calibration Error |
| $Cost$ | 검출 지연, human review, 운영 비용 |
| $\alpha,\beta,\gamma,\lambda$ | 위험 항목의 상대 가중치 |

### 보안적 의미

미탐은 허위 영상 유포를 허용하고, 오탐은 실제 영상의 신뢰를 훼손한다. 또한 detector confidence가 과신되면 운영자가 잘못된 판단을 내릴 수 있다.

---

### 4.2 Expected Calibration Error

Detector의 confidence가 실제 정확도와 얼마나 일치하는지 측정한다.

$$
ECE=\sum_{m=1}^{M}\frac{|B_m|}{n}\left|acc(B_m)-conf(B_m)\right|
$$

| 기호 | 의미 |
|---|---|
| $B_m$ | confidence bin |
| $acc(B_m)$ | 해당 bin의 실제 정확도 |
| $conf(B_m)$ | 해당 bin의 평균 confidence |
| $n$ | 전체 sample 수 |

### 보안적 의미

AUC가 높아도 calibration이 나쁘면 detector가 잘못된 확신을 줄 수 있다. 고위험 영상 검토에서는 confidence calibration과 human review가 필요하다.

---

### 4.3 Cross-dataset Generalization Drop

한 데이터셋에서 학습한 detector가 다른 데이터셋에서 성능이 떨어지는 정도를 측정한다.

$$
GenDrop=AUC_{in\text{-}domain}-AUC_{cross\text{-}domain}
$$

| 기호 | 의미 |
|---|---|
| $AUC_{in\text{-}domain}$ | 학습/검증 환경과 유사한 데이터셋에서의 AUC |
| $AUC_{cross\text{-}domain}$ | 다른 생성기·데이터셋·플랫폼 조건에서의 AUC |

### 보안적 의미

딥페이크 검출기가 특정 benchmark에 과적합되면 실제 인터넷 영상이나 새로운 생성모델에 대해 실패할 수 있다. 따라서 cross-dataset, cross-generator 평가가 필수다.

---

### 4.4 Robustness Drop

압축·크롭·노이즈·재인코딩 같은 후처리 후 성능 하락을 측정한다.

$$
RobustnessDrop=AUC_{clean}-AUC_{transformed}
$$

| 기호 | 의미 |
|---|---|
| $AUC_{clean}$ | 원본 또는 기준 영상에서의 검출 AUC |
| $AUC_{transformed}$ | 압축·노이즈·크롭 등 변환 후 AUC |

### 보안적 의미

SNS 업로드, 메신저 재압축, 화면 녹화, crop 등은 실제 환경에서 흔하다. detector가 이런 변환에 취약하면 실사용 신뢰성이 낮다.

---

### 4.5 Subgroup Reliability Gap

집단별 성능 편차를 측정한다.

$$
ReliabilityGap=\max_g Metric_g-\min_g Metric_g
$$

| 기호 | 의미 |
|---|---|
| $g$ | 얼굴 속성, 조명, 화질, 압축 수준, 인종·성별 등 subgroup |
| $Metric_g$ | 특정 subgroup에서의 AUC, F1, FPR, FNR 등 |

### 보안적 의미

전체 성능이 높아도 특정 집단이나 특정 품질 조건에서 성능이 낮으면 사회적·법적 문제가 발생할 수 있다.

---

### 4.6 Open-set Detection Risk

새로운 생성 방식이 등장했을 때 unknown으로 처리하지 못하면 false trust가 발생한다.

$$
OpenSetRisk=\frac{N_{unknown\ accepted\ as\ real}}{N_{unknown}}
$$

### 보안적 의미

딥페이크 생성기술은 빠르게 변한다. 검출기는 학습한 조작 유형만 맞히는 closed-set classifier가 아니라, 미지의 생성 방식에 대한 불확실성을 표시할 수 있어야 한다.

---

## 5. Reliability 평가축

| 축 | 의미 | 대표 실패 사례 | 대표 지표 |
|---|---|---|---|
| Generalization | 보지 못한 데이터셋·생성기·조작 유형에서도 성능 유지 | benchmark에서는 높지만 실제 영상에서 실패 | cross-dataset AUC, GenDrop |
| Robustness | 압축·크롭·노이즈·후처리에도 성능 유지 | SNS 업로드 후 detector 성능 급락 | RobustnessDrop, transformed AUC |
| Interpretability | 검출 근거가 artifact·생체신호·시간축 단서인지 설명 가능 | 무의미한 배경/압축 패턴에 의존 | explanation consistency |
| Calibration | confidence가 실제 정확도와 일치 | 틀렸는데 높은 확신 | ECE, Brier score |
| Fairness | subgroup별 성능 편차가 낮음 | 특정 얼굴 속성·조명·화질에서 오탐 증가 | subgroup FPR/FNR, ReliabilityGap |
| Open-set | 새로운 생성 방식에 불확실성을 표시 | 새로운 모델 생성물을 real로 오판 | unknown detection rate |
| Deployment | 운영환경에서 로그·검토·롤백 가능 | threshold/버전 미기록으로 사고 분석 불가 | audit completeness, MTTR |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | detector 신뢰성, 검출 로그, real/fake 영상, threshold, calibration record, user rights, provenance evidence |
| 공격자 목표 | detector 회피, 압축·후처리로 검출률 저하, false accusation 유도, 새로운 생성기로 검출기 무력화 |
| 공격자 능력 | compression, resizing, blur, crop, noise, re-encoding, adversarial post-processing, 생성기 변경, platform upload |
| 공격 경로 | generated video/image → post-processing/compression → platform distribution → detector inference → human/automated decision |
| 방어자 능력 | cross-dataset test, robustness test, calibration, subgroup audit, open-set threshold, human review, provenance 확인 |
| 제외 범위 | 실제 딥페이크 배포, 개인 영상 수집, 검출기 우회 절차 제공, 유해 영상 제작 |

---

## 7. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W06/P05 활용 |
|---|---|---|---|
| 기본 성능 | AUC, accuracy, F1 | real/fake 분류 성능 | baseline detector 평가 |
| 오류 비용 | FPR, FNR | 오탐·미탐 비용 | high-stakes 판단 |
| 일반화 | cross-dataset AUC, cross-generator AUC, GenDrop | 보지 못한 환경에서 성능 유지 | detector overfitting 방지 |
| 강건성 | RobustnessDrop, transformed AUC | 압축·노이즈·크롭 후 성능 | 실사용 플랫폼 평가 |
| Calibration | ECE, Brier score | confidence 신뢰성 | human review 우선순위 설정 |
| Fairness | subgroup FPR/FNR, ReliabilityGap | 집단·품질 조건별 성능 편차 | 사회적 책임성 평가 |
| Interpretability | explanation consistency, artifact localization | 검출 근거의 안정성 | XAI 보안 연결 |
| Open-set | unknown detection rate, false-real acceptance | 새로운 생성기술 대응 | future-proof detector 평가 |
| Provenance | watermark/provenance coverage | 생성·편집 이력 확인 | W13/W14/W15 연결 |

---

## 8. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| 데이터셋 | real/fake dataset name, version, generator type, split, demographic/quality metadata |
| 조작 유형 | face swap, reenactment, lip-sync, diffusion/GAN-based generation 등 |
| 변환 조건 | compression codec, bitrate, resizing, blur, noise, crop, re-encoding setting |
| 모델 | detector architecture, checkpoint, preprocessing, threshold, calibration method |
| 평가 | AUC, F1, FPR/FNR, cross-dataset result, robustness result, ECE, subgroup result |
| 설명가능성 | explanation method, artifact localization, failure case |
| 운영 로그 | detector version, inference timestamp, output score, human review decision |
| provenance | watermark, metadata, source trace, output hash |
| 한계 | 실험실 데이터셋 성능을 실제 인터넷·수사·법적 판단 성능으로 과장하지 않음 |

---

## 9. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W06/P05에서의 의미 |
|---|---|---|
| Classification | real/fake 이진 또는 다중 분류 | 기본 detector 구조 |
| Domain generalization | 데이터셋·생성기 변화에 대한 일반화 | reliability 핵심 |
| Robust learning | 변환·압축·노이즈에 대한 강건성 | 플랫폼 환경 대응 |
| Calibration | confidence와 실제 정확도의 정합성 | 신뢰 가능한 운영 판단 |
| XAI/Interpretability | detector가 어떤 단서에 의존하는지 설명 | 허위 근거·shortcut 방지 |
| Fairness | subgroup별 detector 성능 편차 분석 | 사회적 책임성 |
| Open-set recognition | 미지 생성 방식 감지 | 빠르게 변하는 deepfake 대응 |
| Human-in-the-loop | 자동 검출 결과를 사람이 검토 | high-stakes decision support |

---

## 10. 보안 이슈 30% 관점 분석

| 보안 항목 | Reliability 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 영상 속 개인 식별정보와 검출 로그가 민감정보가 될 수 있음 | data governance, log privacy |
| 무결성 | 검출 결과가 잘못되면 영상 진위 판단과 증거 신뢰성이 훼손됨 | FPR/FNR, calibration |
| 가용성 | 대량 영상·후처리 영상으로 검출 시스템이 과부하될 수 있음 | throughput, latency, review cost |
| 프라이버시 | 특정 집단·개인의 얼굴 속성이 검출 성능 편차를 만들 수 있음 | subgroup performance |
| 안전성 | 정치·의료·법률 등 고위험 영상에서 오판은 사회적 피해로 이어짐 | high-stakes review flag |
| 책임성 | threshold, detector version, human review, provenance log가 없으면 사후 검증 불가 | audit completeness |

---

## 11. 논문의 고유 기여

1. 딥페이크 검출을 단순 성능 경쟁이 아니라 reliability 문제로 재정의한다.
2. Generalization, robustness, interpretability, calibration, fairness, open-set detection을 하나의 평가 프레임으로 묶는다.
3. 실험실 benchmark와 실제 플랫폼·사회적 환경 사이의 간극을 강조한다.
4. W06 P04의 deepfake taxonomy를 실제 운영 검출 신뢰성 관점으로 확장한다.
5. W14 MLOps와 W15 evidence chain에서 필요한 detector version, threshold, calibration, human review 로그의 근거를 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| Deepfake 생성기술 변화 | 새로운 생성기와 diffusion/video model이 계속 등장한다. | open-set, cross-generator 평가 포함 |
| Benchmark 과적합 | 특정 데이터셋에서만 높은 detector가 될 수 있다. | cross-dataset, cross-platform 평가 강조 |
| 변환 강건성 부족 | 압축·재인코딩·화면녹화 후 성능이 떨어질 수 있다. | platform-like transformation 평가 포함 |
| Calibration 미흡 | confidence가 실제 정확도와 다를 수 있다. | ECE와 threshold 분석 포함 |
| Fairness/책임성 | 특정 집단·영상 품질에서 오탐/미탐이 커질 수 있다. | subgroup FPR/FNR과 human review 병행 |
| 실제 운영 검증 어려움 | 법적·윤리적 고위험 환경에서 자동 검출만으로 판단하기 어렵다. | provenance, human-in-the-loop, limitation statement 명시 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 딥페이크 검출은 높은 accuracy가 아니라 운영 신뢰성 문제라는 문제의식 |
| 2장 관련연구 | reliability perspective deepfake detection survey 정리 |
| 3장 위협모형 | detector, threshold, calibration, platform transformation, provenance log 보호 자산 정의 |
| 4장 연구방법 | AUC, F1, GenDrop, RobustnessDrop, ECE, subgroup FPR/FNR, provenance coverage 지표 설계 |
| 5장 분석 | detector reliability evaluation table과 failure mode 분석 |
| 6장 보안적 함의 | high-stakes 영상 판단에서 human review, provenance, 책임성 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W06에서 기말논문에 반영할 개념: 딥페이크 검출은 real/fake 분류 정확도만으로 충분하지 않고, 일반화·강건성·calibration·fairness·open-set·provenance를 포함한 reliability 문제다.
2. W06에서 기말논문에 반영할 표·그림·실험: deepfake reliability 평가표, GenDrop/RobustnessDrop/ECE 수식, detector-human review-provenance workflow를 반영한다.
3. W06이 RAG/LLM 보안 감사 프레임워크와 연결되는 지점: 합성 이미지·영상이 멀티모달 RAG 근거로 들어갈 경우, detector score뿐 아니라 detector version, threshold, calibration, provenance log를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P05는 W06의 deepfake detection reliability 핵심 문헌이다. P04가 딥페이크 생성·검출 taxonomy를 제공한다면, P05는 실제 운영 환경에서 검출기를 신뢰할 수 있는지 평가하는 기준을 제공한다. 따라서 W06 기말논문 연결에서는 P05를 **검출 신뢰성·일반화·강건성·calibration·human-in-the-loop 평가의 중심 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
