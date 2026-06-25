# P04 Summary

## ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack — Kaiyi Pang et al., IEEE TIFS, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W13 Model Stealing & Watermarking |
| 논문명 | ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack |
| 저자 | Kaiyi Pang et al. |
| 공식 출판 정보 | IEEE Transactions on Information Forensics and Security, Vol. 20, pp. 1767–1782, 2025 |
| DOI | https://doi.org/10.1109/TIFS.2025.3530691 |
| 보조 URL | arXiv `2405.02365` |
| 로컬 PDF | `01_papers/pdf/04_Pang_et_al_2025_ModelShield.pdf` |
| 검증 상태 | W13 `paper_list.md`와 `download_source.md` 기준 arXiv판과 IEEE TIFS 출판판의 제목·저자 일치 확인, 권호/쪽/DOI 확인 완료 |
| PDF 확인 메모 | repo의 PDF 폴더에 P04 관련 PDF blob이 존재함을 확인했다. 최종 인용은 IEEE DOI 기준으로 정리하고, arXiv v4는 사전판으로 병기한다. |
| 핵심 근거 사용 가능 여부 | 가능. W13에서 model extraction 이후에도 유지되는 adaptive robust watermark, ownership proof, trigger set robustness, watermark accuracy, extraction fidelity, clean utility trade-off를 설명하는 핵심 방어 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 model extraction attack 이후에도 소유권 검증이 가능한 **adaptive and robust watermark** 방어기법인 ModelShield를 제안·평가하며, **black-box extraction, surrogate model, trigger set, adaptive watermark embedding, watermark transferability, extraction fidelity, watermark accuracy, clean utility, robustness under fine-tuning/pruning/distillation, ownership verification** 관점에서 W13의 model stealing 방어를 실험적으로 설명하는 핵심 문헌이다.

---

## 2. 핵심 연구문제

> 기존 DNN watermark는 원본 모델에서는 검증 가능하더라도, 공격자가 black-box query로 surrogate model을 학습하거나 모델을 fine-tuning·pruning·distillation하면 watermark가 약화될 수 있다. ModelShield의 핵심 문제는 모델 추출 이후에도 watermark evidence가 유지되도록 watermark를 어떻게 설계하고, clean utility와 소유권 검증 안정성을 어떻게 동시에 확보할 것인가이다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Model extraction 이후 surrogate/stolen model에서도 watermark가 유지되도록 설계할 수 있는가? |
| RQ2 | Adaptive watermark는 공격자가 victim model의 API output을 이용해 surrogate를 학습하는 상황을 어떻게 고려하는가? |
| RQ3 | Watermark accuracy, clean accuracy, extraction fidelity, utility drop 사이의 trade-off를 어떻게 평가해야 하는가? |
| RQ4 | Fine-tuning, pruning, distillation, model extraction, output perturbation 같은 변형 후에도 ownership verification이 가능한가? |
| RQ5 | 기말논문에서 watermark 검증 결과를 법적 소유권 확정이 아니라 기술적 evidence chain으로 어떻게 제한해 표현해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W13 연결 |
|---|---|---|
| Adaptive robust watermark 제안 | model extraction 공격을 고려해 watermark가 surrogate model에도 남도록 설계 | W13 P04 핵심 기술 |
| Model stealing 방어 실험화 | P01의 model stealing threat를 실제 watermark defense 평가로 연결 | 공격-방어 연결 |
| Ownership verification 강화 | trigger set 또는 watermark behavior로 도난 모델의 소유권 증거를 제시 | P03 DNN watermarking 확장 |
| Trade-off 평가 | watermark accuracy, clean accuracy, extraction fidelity, utility drop을 함께 평가 | 기말논문 metric 설계 |
| 실전 공격 내성 고려 | fine-tuning, pruning, distillation, extraction 후 watermark 유지성을 검토 | robustness evidence chain |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | Model extraction attack은 API 질의로 victim model을 복제할 수 있으며, 기존 watermark는 추출 이후 약화될 수 있다. | AI 모델이 도난당한 뒤에도 “이 모델은 내 모델에서 나온 것”이라고 증명해야 한다. |
| 2. Background | DNN watermark, model extraction, black-box query, surrogate training, ownership verification 개념을 설명한다. | 공격자는 모델에 질문을 많이 해서 비슷한 모델을 만들고, 방어자는 표식이 남아 있는지 확인한다. |
| 3. Threat Model | 공격자는 victim model 내부를 직접 보지 못하지만 API output을 통해 surrogate model을 학습할 수 있다. | 모델 내부를 몰라도 API 답변만으로 복제가 가능하다. |
| 4. ModelShield Design | watermark가 원본 모델뿐 아니라 추출된 모델에도 보존되도록 adaptive trigger/behavior를 설계한다. | 도난 모델에도 따라가는 소유권 표식을 만드는 방식이다. |
| 5. Training and Embedding | watermark objective와 clean task objective 사이 균형을 잡아 watermark와 정상 성능을 동시에 유지한다. | 표식을 넣되 모델 성능을 망치지 않도록 학습한다. |
| 6. Evaluation | clean accuracy, watermark accuracy, extraction fidelity, robustness after extraction, utility drop을 평가한다. | 모델이 잘 작동하는지, 표식이 남는지, 도난 후에도 검증되는지를 같이 본다. |
| 7. Robustness Analysis | fine-tuning, pruning, distillation, extraction 같은 변형에도 watermark 검증이 가능한지 분석한다. | 훔친 사람이 모델을 고쳐도 표식이 남는지 확인한다. |
| 8. Limitations | adaptive attacker, trigger secrecy, key management, false positive, legal evidence 한계가 남는다. | 워터마크는 강한 증거지만, 열쇠 관리와 오탐 문제도 중요하다. |
| 9. Conclusion | ModelShield는 model extraction 위협에 대한 watermark defense의 실험적 근거를 제공한다. | 모델 도난 방어는 탐지·검증·성능을 함께 봐야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 ModelShield류 watermark defense 평가를 W13 보고서에서 설명하기 위한 표준화된 표현이다. 실제 공격 구현 절차가 아니라 방어·검증·감사 지표 중심으로 정리한다.

### 5.1 Watermark Accuracy

Watermark trigger set에서 기대한 watermark response가 나오는 비율이다.

$$
WatermarkAcc=\frac{1}{|T_w|}\sum_{(x,y)\in T_w}\mathbf{1}[f(x)=y]
$$

| 기호 | 의미 |
|---|---|
| $T_w$ | watermark trigger set |
| $f$ | 검증 대상 모델 |
| $y$ | watermark 검증용 기대 label 또는 response |

### 보안적 의미

WatermarkAcc가 높으면 소유권 표식이 모델 행동에 안정적으로 남아 있다는 뜻이다. 단, 정상 task accuracy와 분리해서 보고해야 한다.

---

### 5.2 Clean Utility Drop

Watermark 삽입으로 정상 성능이 얼마나 손실되는지 측정한다.

$$
UtilityDrop=Acc_{clean}^{base}-Acc_{clean}^{wm}
$$

| 기호 | 의미 |
|---|---|
| $Acc_{clean}^{base}$ | watermark 없는 기준 모델 성능 |
| $Acc_{clean}^{wm}$ | watermark 삽입 모델 성능 |

### 보안적 의미

강한 watermark가 clean utility를 크게 낮추면 실서비스 적용이 어렵다. ModelShield 평가에는 watermark strength와 clean utility가 함께 필요하다.

---

### 5.3 Extraction Fidelity

추출된 모델이 victim model의 예측과 얼마나 일치하는지 측정한다.

$$
Fidelity_{ext}=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[f_{victim}(x_i)=f_{stolen}(x_i)]
$$

### 보안적 의미

Fidelity가 높으면 model extraction이 성공적이라는 뜻이다. watermark defense는 fidelity가 높은 stolen model에서도 ownership evidence가 남는지 확인해야 한다.

---

### 5.4 Watermark Transfer to Stolen Model

추출된 모델에서 watermark가 유지되는 비율이다.

$$
Transfer_{wm}=\frac{WatermarkAcc(f_{stolen},T_w)}{WatermarkAcc(f_{victim},T_w)}
$$

### 보안적 의미

ModelShield의 핵심은 watermark가 victim model에만 있는 것이 아니라 stolen/surrogate model에도 검증 가능한지다.

---

### 5.5 Robustness after Transformation

모델 변형 후 watermark가 유지되는 정도다.

$$
Robustness_{wm}=\frac{N_{verified\ after\ transformation}}{N_{verified\ before\ transformation}}
$$

### 보안적 의미

fine-tuning, pruning, distillation 후에도 watermark가 유지되어야 실전 방어 가치가 있다.

---

### 5.6 Ownership Verification Decision

검증 점수가 threshold를 넘으면 소유권 증거가 있다고 판단한다.

$$
Verify(f,K)=\mathbf{1}[Score(f,K)>\tau]
$$

| 기호 | 의미 |
|---|---|
| $K$ | watermark key 또는 trigger set |
| $\tau$ | verification threshold |

### 보안적 의미

threshold는 FPR/FNR에 직접 영향을 준다. 법적·운영 환경에서는 threshold와 confidence interval을 기록해야 한다.

---

### 5.7 ModelShield Evaluation Score

watermark 검증력, clean utility, 추출 후 유지성, 오탐 위험을 함께 고려한다.

$$
Score_{MS}=\alpha WatermarkAcc+\beta Transfer_{wm}+\gamma Robustness_{wm}-\lambda UtilityDrop-\mu FPR
$$

### 보안적 의미

좋은 방어는 watermark 검증률만 높은 것이 아니라, 추출 후에도 유지되고, 정상 성능을 유지하며, 오탐 위험이 낮아야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W13/P04에서의 의미 |
|---|---|---|
| Model Extraction | API output으로 surrogate model을 학습 | 방어 대상 공격 |
| Adaptive Watermark | extraction 상황을 고려한 watermark 설계 | ModelShield 핵심 |
| Trigger Set | watermark 검증용 입력 집합 | ownership proof |
| Surrogate Model | 공격자가 만든 복제 모델 | watermark transfer 평가 대상 |
| Extraction Fidelity | victim과 stolen model의 행동 일치 | 공격 성공도 |
| Watermark Accuracy | trigger set에서 watermark response 유지 | 검증 성능 |
| Utility Drop | watermark가 정상 성능에 미치는 영향 | 실서비스 조건 |
| Robustness Evaluation | fine-tuning/pruning/distillation 후 유지성 | 방어 내성 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | ModelShield 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | watermark key와 trigger set이 노출되면 우회·위조 가능 | key leakage risk |
| 무결성 | 도난 모델이 소유권 표식을 제거하거나 위조할 수 있음 | WatermarkAcc, FPR/FNR |
| 가용성 | watermark 삽입이 clean accuracy와 inference cost를 악화시킬 수 있음 | UtilityDrop, latency |
| 프라이버시 | trigger set이나 검증 로그가 민감 데이터와 연결될 수 있음 | trigger privacy check |
| 안전성 | 도난 모델이 악성 서비스나 공격 준비에 재사용될 수 있음 | extraction fidelity, transferability |
| 책임성 | watermark key, trigger hash, model hash, verification log가 분쟁 증거가 됨 | evidence chain completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | watermarked model, trigger set, watermark key, ownership proof, API output, model hash, verification log |
| 공격자 목표 | model extraction 후 watermark 제거 또는 무력화, ownership 부인, stolen model 재배포 |
| 공격자 능력 | black-box query, surrogate training, fine-tuning, pruning, distillation, output observation, limited architecture prior |
| 공격 경로 | victim API query → surrogate training → stolen model 생성 → 모델 변형 → watermark verification 회피 또는 소유권 부인 |
| 방어자 능력 | adaptive watermark embedding, trigger secrecy, key management, watermark verification, extraction-aware evaluation, audit logging |
| 제외 범위 | 실제 타사 모델 추출, 공격 자동화 코드, watermark 제거 절차, trigger/key 탈취, 허위 소유권 주장 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W13/P04 활용 |
|---|---|---|---|
| Watermark 검증 | WatermarkAcc, Verify score | watermark 존재 확인 | 핵심 방어 평가 |
| 추출 후 유지성 | Transfer_wm, robustness after extraction | stolen model에서 표식 유지 | ModelShield 핵심 |
| 공격 성공도 | Fidelity_ext, stolen accuracy | 추출 모델의 유사성·성능 | P01 연결 |
| 정상 성능 | clean accuracy, UtilityDrop | 원래 task 성능 보존 | 실서비스 적용성 |
| 변형 내성 | fine-tuning/pruning/distillation 후 Robustness_wm | 공격 후 견고성 | 방어 강건성 |
| 오탐·미탐 | FPR, FNR | false ownership/missed theft 위험 | 법적·운영 리스크 |
| 운영 비용 | embedding cost, verification latency | 방어 비용 | MLOps 연결 |
| 재현성 | model hash, trigger hash, key ID, threshold | 감사 가능성 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | IEEE DOI, arXiv version, 로컬 PDF 판본 상태 |
| Victim model | architecture, dataset, model hash, clean accuracy |
| Watermark setup | trigger set hash, key ID, threshold, watermark objective |
| Extraction setting | query budget, surrogate architecture, output type, extraction condition |
| Transformation setting | fine-tuning, pruning, distillation, compression 조건 |
| Metrics | WatermarkAcc, Transfer_wm, Fidelity_ext, UtilityDrop, FPR/FNR |
| Baseline | non-watermarked model, 기존 watermark method와 비교 |
| Evidence | verification log, model hash, trigger hash, config, seed, result table |
| Legal/evidence note | watermark 검증은 기술적 증거이며 법적 소유권 확정은 별도 판단 필요 |
| 한계 | 특정 extraction setting에서의 robustness를 모든 공격자와 모든 모델 변형에 대한 절대 보장으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. Model extraction attack 이후에도 유지되는 adaptive robust watermark 방어를 제안한다.
2. 기존 DNN watermarking을 단순 원본 모델 검증에서 stolen/surrogate model 검증으로 확장한다.
3. Watermark accuracy, extraction fidelity, utility drop, 변형 내성을 함께 평가해야 함을 보여준다.
4. W13 P01의 model stealing 위협과 P03의 DNN watermarking taxonomy를 실험형 방어 논문으로 연결한다.
5. W13 기말논문에서 API extraction 위험과 ownership evidence chain을 설계하는 핵심 근거가 된다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 공격 설정 의존성 | extraction query budget, surrogate architecture, output type에 따라 결과가 달라진다. | extraction setting을 명시하고 일반화 한계 표시 |
| Adaptive attacker | 방어를 아는 공격자는 watermark를 약화시키는 변형을 시도할 수 있다. | adaptive risk를 한계로 명시 |
| Utility trade-off | watermark를 강하게 넣으면 clean accuracy가 낮아질 수 있다. | UtilityDrop과 clean accuracy 병기 |
| 오탐·미탐 위험 | threshold가 부적절하면 false ownership claim 또는 missed theft 발생 | FPR/FNR과 threshold 기록 |
| Key/trigger 관리 | trigger set과 key가 유출되면 위조·우회 가능 | key management와 trigger hash 기록 |
| 법적 증거 한계 | 기술적 verification이 법적 소유권을 자동 확정하지 않는다. | evidence chain과 법적 판단을 분리 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | model extraction 이후에도 소유권 검증 가능한 watermark defense가 필요하다는 문제의식 |
| 2장 관련연구 | ModelShield를 adaptive robust watermark against model extraction 핵심 방어 문헌으로 정리 |
| 3장 위협모형 | watermarked model, trigger set, watermark key, API output, stolen model 보호 자산 정의 |
| 4장 연구방법 | WatermarkAcc, Transfer_wm, Fidelity_ext, UtilityDrop, FPR/FNR, robustness after transformation 지표 설계 |
| 5장 분석 | model stealing-defense-evidence matrix와 ownership verification workflow 제시 |
| 6장 보안적 함의 | API extraction, watermark transfer, trigger/key management, ownership evidence chain, 법적 한계 해석 |

---

## 14. 기말논문 연결 3문장

1. W13에서 기말논문에 반영할 개념: ModelShield는 model extraction 이후에도 watermark가 stolen/surrogate model에 유지되도록 설계해 소유권 검증 가능성을 높이는 adaptive robust watermark 방어다.
2. W13에서 기말논문에 반영할 표·그림·실험: WatermarkAcc, Transfer_wm, Fidelity_ext, UtilityDrop, FPR/FNR 수식표와 model extraction 후 ownership verification workflow를 반영한다.
3. W13이 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: LLM/RAG 서비스에서도 API extraction 이후 prompt template, retrieval policy, embedding behavior, generated answer provenance에 fingerprint/watermark evidence를 남기고 W14/W15 evidence chain과 연결해야 한다.

---

## 15. 최종 판단

P04는 W13의 실험형 watermark defense 핵심 문헌이다. P01이 model stealing의 공격 배경을 제공하고 P03이 DNN watermarking taxonomy를 제공한다면, P04는 model extraction 이후에도 소유권 검증이 가능한 adaptive robust watermarking의 실험적 근거를 제공한다. 따라서 기말논문에서는 P04를 **ModelShield, extraction-aware watermark, watermark transfer, ownership verification, clean utility trade-off의 중심 방어 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
