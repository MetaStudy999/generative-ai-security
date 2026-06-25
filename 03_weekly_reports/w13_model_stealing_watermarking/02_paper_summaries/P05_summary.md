# P05 Summary

## Generative Adversarial Networks: A Survey on Attack and Defense Perspective — Chenhan Zhang et al., ACM Computing Surveys, 2023/2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W13 Model Stealing & Watermarking |
| 공식 논문명 | Generative Adversarial Networks: A Survey on Attack and Defense Perspective |
| 공식 저자 | Chenhan Zhang et al. |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 56, Issue 4, pp. 1–35, online 2023-11-10, print 2024-04-30 |
| DOI | https://doi.org/10.1145/3615336 |
| 로컬 PDF | `01_papers/pdf/05_RELATED_Cai_et_al_2021_GAN_Private_Secure_Applications.pdf` |
| 로컬 PDF 상태 | W13 `paper_list.md`와 `download_source.md` 기준 로컬 PDF는 Zhipeng Cai et al., `Generative Adversarial Networks: A Survey Towards Private and Secure Applications`, arXiv:2106.03785v1 관련 보조 문헌이다. 공식 P05 DOI 논문과 동일 문헌으로 단정하지 않는다. |
| 검증 상태 | W13 `paper_list.md` 기준 지정 제목과 매우 유사한 ACM CSUR 논문 DOI `10.1145/3615336` 확인. 강의자료의 `Cheng/Chenhan Zhang et al.` 표기와 로컬 PDF 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P05 관련 PDF blob이 존재함을 확인했다. 다만 로컬 PDF는 공식 P05 지정 논문과 다른 GAN privacy/security application 보조 문헌이므로, summary는 공식 DOI 기준 P05를 중심으로 작성하고 로컬 PDF는 W06 deepfake·W13 watermark/provenance 연결 보조 문헌으로만 해석한다. |
| 핵심 근거 사용 가능 여부 | 가능. W13에서 GAN attack/defense, synthetic artifact risk, generated content provenance, watermark robustness, model IP, privacy/security application을 연결하는 관련 문헌으로 사용 |

---

## 1. 한 문장 요약

공식 P05 논문은 GAN을 **공격 생성 도구와 방어 도구라는 양면성, generator-discriminator adversarial learning, privacy leakage, data synthesis risk, adversarial example generation, poisoning/backdoor, deepfake/misuse, detection/forensics, watermarking, provenance, model ownership, synthetic data governance** 관점에서 정리하며, W13에서 model stealing·watermarking을 생성모형의 산출물 출처 추적과 private/secure GAN application 문제로 확장하는 핵심 관련 문헌이다.

---

## 2. 핵심 연구문제

> GAN은 실제와 유사한 데이터를 생성해 데이터 증강·방어·프라이버시 보호에 활용될 수 있지만, 동시에 deepfake, synthetic misinformation, training data leakage, model IP 침해, watermark 제거, provenance 위조 같은 공격면을 만든다. 따라서 생성모형 보안에서는 모델 자체의 소유권뿐 아니라 생성물의 출처, 워터마크, 탐지 가능성, 오남용 가능성을 함께 평가해야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | GAN은 공격 관점에서 adversarial sample, deepfake, synthetic phishing, data poisoning, privacy leakage에 어떻게 활용될 수 있는가? |
| RQ2 | GAN은 방어 관점에서 data augmentation, anomaly detection, privacy-preserving synthesis, adversarial training, forensics에 어떻게 활용되는가? |
| RQ3 | 생성물 watermarking과 provenance는 synthetic artifact misuse와 model ownership dispute를 어떻게 줄일 수 있는가? |
| RQ4 | GAN 기반 생성물의 위험은 detection rate, FPR/FNR, watermark robustness, provenance coverage, privacy risk로 어떻게 평가해야 하는가? |
| RQ5 | 로컬 PDF가 공식 DOI 논문과 다른 관련 문헌일 때, GAN attack/defense summary와 참고문헌 인용을 어떻게 분리 관리해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W13 연결 |
|---|---|---|
| GAN attack/defense taxonomy | GAN이 공격 생성과 방어 데이터 생성에 모두 쓰이는 양면성을 정리 | W13 P05 핵심 관련 주제 |
| 생성물 보안 관점 | synthetic artifact, deepfake, provenance, watermarking, detection 문제를 연결 | W06 딥페이크와 W13 watermark 연결 |
| 프라이버시·보안 응용 연결 | GAN 기반 synthetic data와 privacy/security application의 위험과 효용을 함께 설명 | 로컬 PDF 보조 문헌 활용 범위 |
| 평가 지표 확장 | detection rate, provenance coverage, privacy risk, watermark robustness, generated artifact risk를 함께 고려 | 기말논문 metric 설계 |
| 참고문헌 검증 사례 | 공식 DOI 논문과 로컬 PDF가 다르므로 related paper 관리가 필요 | W15 reproducibility/reference audit 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | GAN은 현실적인 합성 데이터를 생성할 수 있어 보안 분야에서 공격과 방어 양쪽에 활용된다. | GAN은 가짜를 아주 진짜처럼 만들 수 있어 유용하지만 위험하다. |
| 2. GAN Background | Generator와 discriminator가 경쟁하며 데이터 분포를 학습하는 구조를 설명한다. | 생성자는 가짜를 만들고 판별자는 진짜와 가짜를 구분하며 서로 발전한다. |
| 3. Attack Perspective | GAN은 deepfake, adversarial example, data poisoning, phishing content, privacy leakage, evasion에 활용될 수 있다. | 공격자는 GAN으로 속이기 쉬운 이미지·음성·텍스트·데이터를 만들 수 있다. |
| 4. Defense Perspective | GAN은 data augmentation, anomaly detection, adversarial training, privacy-preserving synthetic data, forensic detector 학습에 활용될 수 있다. | 방어자는 GAN으로 더 다양한 공격 예시를 만들어 탐지 모델을 훈련할 수 있다. |
| 5. Privacy and Security Applications | synthetic data가 privacy를 높일 수 있지만, memorization·membership leakage·attribute leakage 위험도 존재한다. | 가짜 데이터라고 해서 개인정보 위험이 자동으로 사라지는 것은 아니다. |
| 6. Watermarking and Provenance | 생성물과 생성모델의 출처를 추적하기 위해 watermark, fingerprint, detector, audit log가 필요하다. | AI가 만든 콘텐츠에는 출처 표시와 검증 기록이 필요하다. |
| 7. Evaluation Metrics | generated artifact quality, detection rate, FPR/FNR, privacy risk, watermark robustness, provenance coverage를 평가한다. | 생성물이 그럴듯한지뿐 아니라 위험하고 추적 가능한지도 봐야 한다. |
| 8. Challenges | adaptive misuse, watermark removal, detector generalization, domain shift, legal responsibility, open-source model governance가 과제로 남는다. | 공격자는 흔적을 지우려 하고, 탐지기는 새로운 가짜에 약할 수 있다. |
| 로컬 관련 PDF 메모 | 로컬 PDF는 Cai et al. 2021 GAN private/secure application survey로 보이며, official P05와 동일 문헌으로 인용하지 않는다. | PDF가 있다고 해서 공식 지정 논문으로 인용하면 안 된다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 GAN attack/defense와 generated artifact provenance 평가를 W13 보고서에서 설명하기 위한 표준화된 표현이다. 실제 악용 절차가 아니라 위험 평가와 방어·감사 지표 중심으로 정리한다.

### 5.1 GAN Minimax Objective

GAN은 generator $G$와 discriminator $D$가 다음 목적함수로 경쟁한다.

$$
\min_G\max_D \;\mathbb{E}_{x\sim p_{data}}[\log D(x)]+\mathbb{E}_{z\sim p_z}[\log(1-D(G(z)))]
$$

| 기호 | 의미 |
|---|---|
| $G$ | generator |
| $D$ | discriminator |
| $p_{data}$ | 실제 데이터 분포 |
| $p_z$ | latent noise 분포 |

### 보안적 의미

GAN은 실제와 유사한 합성물을 생성할 수 있으므로 deepfake·synthetic phishing·privacy-preserving data synthesis 양쪽에 모두 연결된다.

---

### 5.2 Generated Artifact Risk

합성물의 오남용·프라이버시·IP 위험을 요약하는 지표다.

$$
Risk_{gen}=w_1PrivacyRisk+w_2IPRisk+w_3MisuseRisk-w_4DefenseCoverage
$$

| 기호 | 의미 |
|---|---|
| $PrivacyRisk$ | 학습 데이터 memorization 또는 민감정보 노출 위험 |
| $IPRisk$ | 모델·생성물 소유권 침해 위험 |
| $MisuseRisk$ | deepfake, 사칭, 허위정보, 우회 공격 가능성 |
| $DefenseCoverage$ | watermark, detector, provenance, audit coverage |

### 보안적 의미

생성물이 고품질이어도 provenance와 detection이 부족하면 보안 위험이 커진다.

---

### 5.3 Detection Rate

GAN 생성물을 탐지기가 올바르게 식별한 비율이다.

$$
DetectionRate=\frac{TP}{TP+FN}
$$

### 보안적 의미

탐지율은 중요하지만, FPR이 높으면 정상 콘텐츠를 악성 또는 AI 생성물로 오판할 수 있다. DetectionRate와 FPR/FNR을 함께 보고해야 한다.

---

### 5.4 False Positive / False Negative Rate

탐지기의 오탐·미탐을 측정한다.

$$
FPR=\frac{FP}{FP+TN},\qquad FNR=\frac{FN}{FN+TP}
$$

### 보안적 의미

FPR은 false accusation, FNR은 missed synthetic artifact risk와 연결된다.

---

### 5.5 Provenance Coverage

생성물 중 출처 추적 정보가 유효하게 남아 있는 비율이다.

$$
ProvenanceCoverage=\frac{N_{traceable}}{N_{generated}}
$$

| 기호 | 의미 |
|---|---|
| $N_{traceable}$ | watermark·metadata·audit log로 출처 추적 가능한 생성물 수 |
| $N_{generated}$ | 전체 생성물 수 |

### 보안적 의미

ProvenanceCoverage가 낮으면 사후 책임 추적과 소유권 검증이 어렵다.

---

### 5.6 Watermark Robustness for Generated Artifacts

편집·압축·재생성 후 watermark가 유지되는 정도다.

$$
Robustness_{wm}=\frac{DetectionRate_{after\ transformation}}{DetectionRate_{before\ transformation}}
$$

### 보안적 의미

이미지 편집, 압축, 스타일 변환, paraphrase, re-generation 이후에도 watermark가 유지되어야 실전성이 있다.

---

### 5.7 Privacy Leakage from Synthetic Data

합성 데이터가 학습 데이터를 얼마나 노출할 수 있는지 membership 또는 nearest-neighbor 위험으로 평가할 수 있다.

$$
LeakageRisk=\alpha Adv_{MI}+\beta Similarity_{train}+\gamma AttributeLeakage
$$

### 보안적 의미

GAN 생성물이 실제 training sample과 지나치게 유사하면 synthetic data라도 privacy leakage 위험이 있다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W13/P05에서의 의미 |
|---|---|---|
| GAN | generator와 discriminator의 경쟁 학습 | 생성형 공격·방어의 기반 |
| Synthetic Data | 실제와 유사한 합성 데이터 | privacy/utility trade-off |
| Deepfake | 현실적인 가짜 콘텐츠 생성 | misuse risk |
| Detector | 생성물 또는 조작물 탐지 | defense mechanism |
| Watermark | 생성물 또는 모델에 출처 표식 삽입 | provenance 추적 |
| Provenance | 생성 출처와 처리 이력 | 책임성·감사 |
| Privacy Leakage | synthetic data가 학습 데이터를 노출하는 위험 | W11 DP/MIA 연결 |
| Secure Application | anomaly detection, data augmentation 등 방어 응용 | 공격·방어 양면성 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | GAN Attack/Defense 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 합성 데이터가 training data 특성을 노출할 수 있음 | Adv_MI, similarity to training data |
| 무결성 | deepfake와 synthetic artifact가 정보 신뢰성을 훼손 | detection rate, provenance coverage |
| 가용성 | 강한 탐지·워터마크 시스템이 비용과 지연을 만들 수 있음 | detection latency, generation overhead |
| 프라이버시 | private/secure GAN 응용도 memorization 위험을 완전히 제거하지 못함 | leakage risk, attribute leakage |
| 안전성 | 합성물 악용이 사칭·허위정보·보안 우회로 이어질 수 있음 | misuse risk, FNR |
| 책임성 | watermark, provenance, audit log가 있어야 사후 책임 추적 가능 | audit completeness, traceability |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 생성모델, synthetic artifact, 학습 데이터, watermark, provenance metadata, detector, model ownership, audit log |
| 공격자 목표 | 합성물 악용, deepfake 생성, watermark 제거, detector 회피, 모델/데이터 소유권 침해, provenance 부인 |
| 공격자 능력 | 생성모델 사용, synthetic artifact 편집·압축·재생성, watermark 제거 시도, detector probing, 공개 데이터 결합 |
| 공격 경로 | GAN 생성 → 합성물 배포/변형 → detector 회피 또는 provenance 제거 → misuse 또는 ownership dispute |
| 방어자 능력 | detector 학습, watermark/provenance 삽입, metadata 관리, synthetic data audit, privacy leakage test, evidence logging |
| 제외 범위 | deepfake 제작 절차, 탐지 우회 절차, watermark 제거 코드, 실제 개인·기관 사칭 지원, 악성 합성물 생성 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W13/P05 활용 |
|---|---|---|---|
| 생성 품질 | FID, IS, perceptual quality, task utility | 생성물 품질 | utility 평가 |
| 오남용 위험 | MisuseRisk, deepfake risk, artifact realism | 악용 가능성 | threat model |
| 탐지 성능 | DetectionRate, FPR, FNR, AUC | synthetic artifact 탐지 | defense 평가 |
| 출처 추적 | ProvenanceCoverage, watermark detection | 생성물 traceability | W13 watermark 연결 |
| 프라이버시 | Adv_MI, AttributeLeakage, Similarity_train | synthetic data leakage | W11 연결 |
| 워터마크 내성 | Robustness_wm under editing/compression/regeneration | 변형 후 표식 유지 | provenance robustness |
| 운영 비용 | detection latency, generation overhead, audit cost | 실서비스 비용 | MLOps 연결 |
| 서지 정확성 | official DOI match, local PDF mismatch flag | 참고문헌 정확성 | W15 reference audit |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | 공식 DOI 논문과 로컬 PDF 동일 여부, related flag |
| Model | GAN architecture, training dataset, checkpoint hash, generation seed |
| Artifact setting | output modality, resolution/text length, sampling setting, post-processing |
| Detector | detector architecture, threshold, version, calibration data |
| Watermark/provenance | watermark method, key ID, metadata schema, provenance log hash |
| Attack/robustness setting | editing, compression, regeneration, transformation 조건 |
| Metrics | DetectionRate, FPR/FNR, ProvenanceCoverage, Robustness_wm, LeakageRisk, utility |
| Privacy test | membership inference, nearest-neighbor similarity, attribute leakage check 여부 |
| Evidence | generated sample manifest, detector log, model hash, watermark verification log |
| 한계 | 로컬 PDF는 관련 문헌이고, GAN 탐지·워터마크 결과를 모든 생성모델에 대한 절대 보장으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. GAN을 공격과 방어 양쪽에서 사용하는 생성형 AI 보안 문헌으로 정리한다.
2. Synthetic artifact risk를 privacy, IP, misuse, provenance 관점으로 확장한다.
3. W13 model stealing/watermarking 논의를 생성물 provenance와 GAN 보안으로 연결한다.
4. W06 deepfake, W11 privacy leakage, W13 watermark/fingerprint, W14 supply chain, W15 evidence chain을 이어주는 교량 역할을 한다.
5. 로컬 PDF가 official P05와 다른 관련 문헌이므로, 참고문헌 검증표와 related-paper 관리의 중요성을 보여준다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 로컬 PDF 불일치 | P05 로컬 PDF는 official DOI 논문이 아니라 Cai et al. 2021 GAN private/secure application survey다. | 공식 DOI/관련 PDF를 분리 표기 |
| 탐지 일반화 한계 | detector가 특정 GAN이나 데이터셋에만 강할 수 있다. | domain shift와 cross-model test를 한계로 명시 |
| 워터마크 제거 가능성 | 편집·압축·재생성으로 watermark가 약화될 수 있다. | Robustness_wm 조건별 평가표 제시 |
| Synthetic data privacy | 합성 데이터도 training data memorization 위험을 가질 수 있다. | leakage test와 DP/MIA 연결 |
| 법적·윤리적 책임 | 생성물 provenance가 법적 책임을 자동 확정하지 않는다. | evidence chain과 법적 판단 분리 |
| 오남용 가능성 | GAN attack/defense 지식은 악용될 수 있다. | 공격 절차 대신 평가·방어 중심으로 기술 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 생성형 AI는 모델과 산출물 모두가 보안·프라이버시·IP 위험 자산이라는 문제의식 |
| 2장 관련연구 | 공식 P05 DOI 논문을 GAN attack/defense perspective 문헌으로 정리하고 로컬 PDF mismatch는 검증표에 기록 |
| 3장 위협모형 | 생성모델, synthetic artifact, watermark, provenance metadata, detector, audit log 보호 자산 정의 |
| 4장 연구방법 | Risk_gen, DetectionRate, FPR/FNR, ProvenanceCoverage, Robustness_wm, LeakageRisk 지표 설계 |
| 5장 분석 | GAN attack-defense-provenance matrix와 synthetic artifact risk table 제시 |
| 6장 보안적 함의 | deepfake, synthetic data privacy, watermark removal, provenance audit, reference verification 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W13에서 기말논문에 반영할 개념: GAN은 공격 생성과 방어 데이터 생성에 동시에 사용될 수 있으므로, 생성모형 보안은 생성 품질뿐 아니라 misuse risk, privacy leakage, provenance coverage를 함께 평가해야 한다.
2. W13에서 기말논문에 반영할 표·그림·실험: GAN minimax objective, Risk_gen, DetectionRate, FPR/FNR, ProvenanceCoverage, Robustness_wm, LeakageRisk 수식표와 GAN attack-defense-provenance matrix를 반영한다.
3. W13이 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: LLM/RAG 산출물도 GAN 생성물처럼 provenance, watermark, detector, audit log가 필요하며, 이 증거는 W14/W15 evidence chain과 연결해야 한다.

---

## 15. 최종 판단

P05는 W13에서 model stealing과 watermarking 논의를 GAN 기반 생성형 AI 보안으로 확장하는 관련 문헌이다. 다만 W13 `paper_list.md` 기준 로컬 PDF는 Cai et al.의 GAN private/security application survey이며, 공식 DOI 문헌인 Chenhan Zhang et al.의 ACM Computing Surveys 논문과 동일하다고 단정하면 안 된다. 기말논문에서는 P05를 **GAN attack/defense, synthetic artifact risk, generated provenance, watermark robustness, privacy/security application의 관련 근거 문헌**으로 사용하고, 공식 DOI·로컬 PDF 차이는 검증표에 유지하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
