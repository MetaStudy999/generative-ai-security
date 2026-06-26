# W13 제출용 단일 보고서

## 모델 지식재산(IP)·모델 도난·모델 추출·워터마킹

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W13 |
| 보고서 제목 | 모델 지식재산(IP)·모델 도난·모델 추출·워터마킹 |
| 과목 범위 | AI 보안 |
| 작성자 | 박영세 |
| 학번 | 26200122 |
| 작성일 | 2026-06-26 |
| 문서 상태 | 주차별 단일 제출용 보고서 |
| 원본 관리 파일 | `03_weekly_reports/w13_model_stealing_watermarking/07_week_submission/w13_submission_report.md` |
| Word/PDF 제출본 권장 위치 | `03_weekly_reports/w13_model_stealing_watermarking/07_week_submission/exports/` |
| 관련 산출물 위치 | `03_weekly_reports/w13_model_stealing_watermarking/` |
| 안전 범위 | 실제 상용 API 공격, 무단 대량 질의, 실제 모델 탈취, 개인정보 기반 모델 추출, 악용 가능한 공격 절차 제외 |
| PDF 검토 상태 | P01~P05 로컬 PDF blob 존재 확인. 제출 본문은 공식 DOI/URL, `paper_list.md`, 논문별 summary, 실험 보고서 기준으로 작성 |
| 제출 전 주의 | P02/P05는 로컬 PDF가 지정 논문과 다른 관련 보조 문헌 상태다. P03은 강의계획서 표기와 공식 DOI 기준 제목·저자 차이가 있으므로 최종 제출 전 원문 또는 출판사 페이지 재확인 필요 |

---

## 초록

본 보고서는 W13 주차의 모델 지식재산(IP), 모델 도난, 모델 추출, 워터마킹, 핑거프린팅, 생성모형 보안을 하나의 제출용 보고서로 통합한다. 모델은 파라미터와 구조뿐 아니라 학습 데이터, 출력 행동, 결정경계, 워터마크, fingerprint, 생성물 provenance를 포함하는 경제적·기술적 자산이다. 공개 API 또는 제한된 인터페이스에서도 query-response 정보가 반복적으로 수집되면 대체 모델이 원 모델의 행동을 근사할 수 있으며, 이는 extraction fidelity와 query budget으로 평가할 수 있다. 워터마킹과 fingerprinting은 소유권 검증 수단이 될 수 있지만, detection rate만으로 충분하지 않고 false positive rate, false negative, utility accuracy, query budget, 통계적 대조군, 재현성 증거가 함께 필요하다. 본 보고서는 W13 논문 5편을 바탕으로 model stealing taxonomy, LLM watermark/fingerprint 관련 문헌, DNN watermarking, ModelShield, GAN attack/defense 관련 문헌을 연결하고, synthetic binary classification과 toy logistic victim model, query-response 1NN substitute model을 사용한 안전한 toy protocol로 extraction fidelity, substitute accuracy, watermark detection, false positive rate, utility accuracy, query budget, reproducibility evidence를 분리 기록하였다. 실험 결과는 실제 상용 API, 실제 LLM, 실제 모델 탈취, 소유권 분쟁 증거로 일반화하지 않는다.

**키워드:** model stealing, model extraction, model IP, watermarking, fingerprinting, ownership verification, query budget, extraction fidelity, false positive rate, utility accuracy, reproducibility

---

## 1. 한 문장 요약

W13은 모델 추출 위험은 query budget과 extraction fidelity로, 워터마크 기반 소유권 검증은 watermark detection과 false positive rate를 함께 보고해야 함을 보여주는 주차다.

---

## 2. 학습 배경과 주차 목표

### 2.1 이번 주 주제의 위치

W13은 W01~W12에서 다룬 AI 보안 평가축을 모델 지식재산과 소유권 검증 문제로 확장한다. W12가 모델의 강건성·설명안정성·공정성을 다뤘다면, W13은 모델 자체가 보호해야 할 자산이라는 점을 다룬다. 모델 추출은 공격자가 공개 API나 제한된 query interface를 통해 원 모델의 입력-출력 행동을 수집하고, 이를 바탕으로 대체 모델을 학습하거나 원 모델의 결정경계를 근사하는 문제다. 모델 워터마킹과 fingerprinting은 추출 이후에도 소유권을 검증하려는 기술이지만, 검출률이 높더라도 false positive가 높으면 법적·기술적 증거력이 약해질 수 있다.

### 2.2 강의계획서상 학습목표

- Model IP, model stealing, model extraction, query-response leakage 개념을 정리한다.
- Query budget, extraction fidelity, substitute accuracy를 분리해 평가한다.
- DNN watermarking과 LLM watermark/fingerprint의 목적, 검출 지표, 한계를 이해한다.
- Watermark detection과 false positive rate를 동시에 보고해야 하는 이유를 설명한다.
- 소유권 검증에서 대조군, 통계적 유의성, 재현성 증거가 필요한 이유를 정리한다.

### 2.3 이번 주 핵심 질문

1. 공개 API의 query-response만으로 모델 행동이 어느 정도 모방될 수 있는가?
2. Extraction fidelity와 substitute accuracy는 어떻게 다르며, 어떤 지표가 더 직접적인 추출 위험을 보여주는가?
3. Watermark detection이 높아도 false positive rate가 높으면 왜 소유권 증거가 약한가?
4. Model watermark는 utility accuracy, robustness, capacity, stealthiness와 어떤 trade-off를 가지는가?
5. W13 toy protocol을 실제 model IP protection 연구로 확장하려면 어떤 윤리·안전 조건이 필요한가?

---

## 3. 논문 5편의 서술형 종합 요약

### 3.1 P01. I Know What You Trained Last Summer: A Survey on Stealing Machine Learning Models and Defences

P01은 model stealing과 model extraction의 공격·방어 taxonomy를 정리하는 핵심 문헌이다. 모델 추출은 공격자가 원 모델 내부 파라미터에 직접 접근하지 못하더라도 query-response 쌍을 수집하여 원 모델의 decision boundary나 output behavior를 근사하는 방식이다. 공격자는 query budget, query distribution, output label 또는 confidence, substitute model architecture를 이용해 모방 모델을 만들 수 있다.

보안 관점에서 P01은 W13의 핵심 위협모형 근거다. 모델 API는 단순 서비스 인터페이스가 아니라 모델 행동이 노출되는 채널이다. 따라서 API monitoring, query rate limit, anomaly detection, output restriction, watermark/fingerprint verification, legal/policy controls가 함께 필요하다. 제출 서지는 공식 ACM DOI 기준으로 정리한다.

### 3.2 P02. Securing Large Language Models: A Survey of Watermarking and Fingerprinting Techniques

P02는 최종 반영표 기준 LLM watermarking과 fingerprinting 관련 문헌으로 정리한다. LLM watermarking은 생성 텍스트나 모델 행동에 검출 가능한 신호를 남겨 생성물 출처 또는 모델 소유권을 확인하려는 접근이다. Fingerprinting은 특정 query set이나 behavioral signature를 통해 모델의 고유성을 식별하려는 방식이다.

보안 관점에서 P02는 W13의 LLM/생성형 AI 확장 축을 담당한다. LLM watermark는 paraphrase, translation, sampling, fine-tuning, model distillation에 대해 robust해야 하며, 동시에 정상 텍스트 품질을 과도하게 해치지 않아야 한다. 다만 현재 로컬 PDF는 Yuqing Liang et al.의 LLM watermarking survey로, 강의자료 지정 문헌과 차이가 있다. 보고서에서는 공식 최종 반영표의 DOI 기준 문헌을 우선하고, 로컬 PDF는 보조 배경으로만 취급한다.

### 3.3 P03. A survey of Deep Neural Network watermarking techniques

P03은 DNN watermarking 기법을 정리하는 핵심 문헌이다. DNN watermarking은 모델 내부 파라미터, activation, trigger set, output behavior에 소유권 신호를 삽입하고, 나중에 해당 신호를 검출해 모델 소유권 또는 무단 복제를 주장하는 방식이다. 주요 요구사항은 fidelity, robustness, capacity, security, stealthiness, efficiency다.

보안 관점에서 P03은 ownership verification의 지표 체계를 제공한다. 워터마크가 삽입된 모델은 원래 task utility를 유지해야 하고, fine-tuning, pruning, distillation, model extraction 이후에도 검출 가능해야 한다. 동시에 무관한 모델에서 false positive가 낮아야 한다. 강의계획서의 저자명·제목 표기와 공식 DOI 기준 논문 사이에 차이가 있으므로 최종 제출 전 표기 확인이 필요하다.

### 3.4 P04. ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack

P04는 모델 추출 공격 이후에도 워터마크를 이용해 소유권을 검증하려는 직접 관련 문헌이다. ModelShield는 model extraction 상황에서 대체 모델이 원 모델의 행동을 모방할 때 워터마크 신호가 얼마나 상속되거나 검출 가능한지, 그리고 adaptive/robust watermark가 어떤 조건에서 방어 근거가 되는지를 다룬다.

보안 관점에서 P04는 W13 실험의 직접 근거다. 모델 추출과 워터마킹은 별개 문제가 아니라 연결된 평가 문제다. 대체 모델의 extraction fidelity가 높아질수록 원 모델 행동과 함께 watermark behavior도 복제될 수 있고, 이때 watermark detection, false positive, utility accuracy, query budget을 함께 보고해야 한다. 최종 인용은 IEEE TIFS DOI 기준으로 정리한다.

### 3.5 P05. Generative Adversarial Networks: A Survey on Attack and Defense Perspective

P05는 최종 반영표 기준 GAN attack/defense perspective 문헌으로 정리한다. 생성모형은 모델 IP뿐 아니라 생성물 출처, privacy leakage, data memorization, misuse, provenance, watermarking과 연결된다. GAN 계열 모델은 공격·방어 양면성을 가지며, 생성물 품질과 보안 지표를 함께 고려해야 한다.

보안 관점에서 P05는 W13의 생성모형 IP와 provenance 확장 축을 담당한다. 생성모형의 결과물이 실제 데이터와 유사할수록 저작권, 학습 데이터 노출, 위조 콘텐츠, 모델 복제 위험이 커진다. 현재 로컬 PDF는 Cai et al.의 GAN private/security application survey로, 지정 문헌과 차이가 있다. 최종 제출 전 공식 Zhang et al. DOI 문헌 원문과 로컬 보조 문헌을 구분해야 한다.

---

## 4. 논문 간 연결 관계

W13 논문 5편은 다음 흐름으로 연결된다.

```text
Model stealing/extraction taxonomy
→ LLM watermarking/fingerprinting
→ DNN watermarking requirements
→ ModelShield ownership check after extraction
→ GAN attack/defense와 생성모형 provenance
```

P01은 model stealing과 extraction의 위협모형을 제공한다. P02는 LLM watermark/fingerprint 관련 배경을 제공한다. P03은 DNN watermarking의 요구조건과 trade-off를 정리한다. P04는 모델 추출 이후 워터마크 기반 ownership verification을 다루고, P05는 생성모형 IP와 provenance 위험을 확장한다. 이 다섯 문헌을 종합하면 W13의 핵심 메시지는 “모델 IP 보호는 extraction risk와 ownership verification reliability를 함께 평가해야 한다”는 것이다.

---

## 5. AI 원리 70% 정리

Model extraction은 query-response pairs를 이용해 원 모델의 decision function을 근사하는 문제다. Victim model의 입력-출력 행동을 수집하고, substitute model이 이를 모방하도록 학습한다. Watermarking은 모델 또는 출력 행동에 검출 가능한 signature를 심어 ownership evidence를 만들려는 접근이다. 그러나 watermark detection은 false positive, false negative, utility, robustness와 함께 평가해야 한다.

### 5.1 핵심 수식

Extraction fidelity는 victim model과 substitute model의 예측 일치율로 기록한다.

$$
Fidelity=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}\left[f_v(x_i)=f_s(x_i)\right]
$$

Substitute accuracy는 대체 모델이 ground-truth label을 맞힌 비율이다.

$$
SubAcc=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}\left[f_s(x_i)=y_i\right]
$$

Query budget은 모델 추출에 사용된 query 수다.

$$
QBudget=N_q
$$

Watermark detection rate는 trigger set에서 signature가 검출된 비율이다.

$$
WMDetect=\frac{N_{wm}}{N_{trig}}
$$

False positive rate는 무관 모델 또는 clean control이 watermark로 잘못 판정된 비율이다.

$$
FPR=\frac{FP}{FP+TN}
$$

Utility accuracy는 watermarked model이 원래 task에서 유지하는 성능이다.

$$
UtilityAcc=\frac{N_{correct}}{N_{test}}
$$

| 기호 | 의미 |
|---|---|
| $f_v$ | victim model |
| $f_s$ | substitute model |
| $x_i$ | test input |
| $y_i$ | ground-truth label |
| $N_q$ | query 수 |
| $N_{trig}$ | watermark trigger set 크기 |
| $N_{wm}$ | watermark signature가 검출된 trigger 수 |
| $FP$ | 무관 모델을 watermark model로 오판한 수 |
| $TN$ | 무관 모델을 정상적으로 비소유 모델로 판정한 수 |

### 5.2 핵심 개념과 보안 연결

| 개념 | 의미 | 보안 연결 |
|---|---|---|
| Model IP | 모델 파라미터, 행동, 생성물 출처까지 포함한 자산 | 도난·복제·무단 사용 위험 |
| Model extraction | query-response로 원 모델 행동 모방 | fidelity, query budget, API monitoring |
| Watermarking | 모델/출력에 소유권 신호 삽입 | ownership verification, false positive risk |
| Fingerprinting | 고유 행동으로 모델 식별 | copy detection, model lineage |
| Trigger set | 소유권 검증용 특수 입력 집합 | detection과 FPR 동시 보고 필요 |
| Provenance | 모델·데이터·생성물 출처 기록 | 법적·운영 책임성 확보 |

---

## 6. 보안 이슈 30% 정리

모델 도난과 모델 추출은 query-response 정보를 통해 모델 행동이나 결정경계를 모방하려는 공격군이다. Watermarking과 fingerprinting은 모델 또는 생성물에 소유권 검증 신호를 남기는 접근이지만, detection rate와 false positive rate를 함께 보아야 한다. Detection rate가 높아도 FPR이 높으면 무관 모델까지 소유 모델로 잘못 판정할 수 있으므로 소유권 증거로는 약하다.

| 보안 속성 | W13에서의 의미 | 대표 위협 | 평가 지표 |
|---|---|---|---|
| Confidentiality | 모델 행동·결정경계 노출 | query-response extraction | extraction fidelity |
| Integrity | watermark 제거·위조·오검출 | watermark forgery, false ownership claim | watermark detection, FPR |
| Availability | API query abuse와 비용 증가 | automated query harvesting | query budget, rate limit |
| Accountability | 모델 소유권과 provenance 입증 필요 | ownership dispute | trigger-set log, p-value, controls |
| Utility | watermark가 원 task 성능을 해치지 않는가 | utility degradation | utility accuracy |

---

## 7. Research Track 분석

### 7.1 연구문제

- RQ1. Query budget 증가가 extraction fidelity와 substitute accuracy에 어떤 영향을 주는가?
- RQ2. Watermark detection rate와 false positive rate를 함께 볼 때 ownership verification 신뢰성은 어떻게 달라지는가?
- RQ3. Model extraction 이후 watermark signal이 substitute model에 어느 정도 상속되는가?
- RQ4. 모델 IP 보호를 위해 API monitoring, watermarking, legal evidence, reproducibility log를 어떻게 연결해야 하는가?

### 7.2 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 모델 파라미터, 출력 행동, 결정경계, 워터마크, fingerprint, API 로그, 생성물 provenance |
| 공격자 목표 | model behavior 모방, substitute model 생성, watermark 제거 또는 위조, 소유권 검증 무력화 |
| 공격자 지식 | API query-response 관찰, output label/confidence 접근 가능성, watermark trigger 일부 추정 가능성 |
| 공격자 능력 | 반복 query, synthetic query generation, substitute training, fine-tuning, pruning, distillation |
| 공격 경로 | victim model/API → query-response collection → substitute model → fidelity/ownership check |
| 방어자 능력 | rate limit, query monitoring, output restriction, watermarking, fingerprinting, ownership evidence logging |
| 제외 범위 | 실제 상용 API 공격, 무단 대량 질의, 실제 모델 탈취, 개인정보 기반 평가, 악용 가능한 절차 제공 |

### 7.3 평가축

| 평가축 | 질문 | 대표 지표 또는 증거 |
|---|---|---|
| Extraction risk | substitute가 victim 행동을 모방하는가 | extraction fidelity |
| Substitute utility | substitute가 원 task에서 작동하는가 | substitute accuracy |
| Query cost | 추출에 필요한 질의 규모는 얼마인가 | query budget |
| Ownership signal | watermark가 검출되는가 | watermark detection |
| False ownership risk | 무관 모델도 오검출되는가 | false positive rate |
| Model utility | watermark가 원 모델 성능을 해치지 않는가 | utility accuracy |
| Reproducibility evidence | 동일 결과를 다시 만들 수 있는가 | seed, config, CSV, JSON, run log |

### 7.4 재현성

재현성을 위해 seed, synthetic data generation, victim model setting, trigger set, query budgets, substitute model rule, watermark detection rule, control model rule, CSV/JSON/Markdown log를 보존한다. W13 실습은 실제 API, 실제 LLM, 실제 개인정보, 실제 모델 탈취를 포함하지 않는다.

---

## 8. 실습 보고서 및 그래프 수치 검증

본 실습은 실제 상용 API나 실제 LLM을 대상으로 한 모델 추출 공격 재현이 아니라 W13의 핵심인 모델 IP 보안 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. Synthetic binary classification과 toy logistic victim model, query-response 1NN substitute model을 사용해 baseline victim model, substitute query 100/500/1000, watermarked ownership check 조건을 분리하였다.

### 8.1 실습 설계

| 항목 | 설정 |
|---|---|
| Dataset | Synthetic binary classification |
| Victim model | Toy logistic classifier with watermark trigger set |
| Substitute model | Query-response 1-nearest-neighbor classifier |
| Query budgets | 100, 500, 1000 |
| Watermark trigger set | 20 synthetic triggers and signature labels |
| False positive proxy | unrelated clean control model의 trigger 일치율 |
| Seed | 42 |
| Outputs | `metrics_summary.csv`, `results.json`, `run_log.md` |

### 8.2 실습 결과 수치

| 조건 | Query Budget | Watermark Queries Seen | Extraction Fidelity | Substitute Accuracy | Watermark Detection | False Positive Rate | Utility Accuracy | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Baseline victim model | 0 | 0 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 | 원 모델은 clean utility와 trigger signature를 유지 |
| Substitute query 100 | 100 | 5 | 0.864000 | 0.812000 | 0.700000 | 0.600000 | 해당 없음 | 적은 질의만으로도 행동 유사도가 높아짐 |
| Substitute query 500 | 500 | 20 | 0.920000 | 0.840000 | 1.000000 | 0.600000 | 해당 없음 | trigger가 모두 관측되며 검출률 상승 |
| Substitute query 1000 | 1000 | 20 | 0.902000 | 0.822000 | 1.000000 | 0.600000 | 해당 없음 | 1NN toy 특성상 fidelity가 단조 증가하지는 않음 |
| Watermarked ownership check | 0 | 20 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 | toy ownership check upper bound |

본 실험에서 watermark detection은 일부 조건에서 1.000000으로 나타났지만, false positive proxy도 0.600000으로 높게 나타났다. 이는 trigger-set 기반 소유권 검증이 detection rate만으로는 충분하지 않으며, clean control model, unrelated model, random trigger set, 복수 seed, 통계적 유의성 검정이 함께 필요함을 의미한다. 따라서 본 결과는 “소유권 검증 성공”이 아니라 “소유권 검증에는 detection rate와 false positive rate를 함께 기록해야 한다”는 교육용 근거로 해석한다.

### 8.3 그래프 수치 검증

현재 제출 보고서의 그래프는 `assets/w13_metric_chart.png`를 참조한다. 확인 가능한 SVG 그래프에는 `extraction_fidelity`, `substitute_accuracy`, `watermark_detection`, `false_positive_rate`, `utility_accuracy` 다섯 series가 표시되어 있다. Query budget과 watermark queries seen은 표에는 포함하지만 현재 그래프 series에는 포함되어 있지 않다.

| 조건 | 그래프 Fidelity | 표 Fidelity | 그래프 Substitute Acc. | 표 Substitute Acc. | 그래프 WM Detect | 표 WM Detect | 그래프 FPR | 표 FPR | 그래프 Utility | 표 Utility | 확인 결과 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Baseline victim model | 1.000000 | 1.000000 | 0.868000 | 0.868000 | 1.000000 | 1.000000 | 0.600000 | 0.600000 | 0.868000 | 0.868000 | 일치 |
| Substitute query 100 | 0.864000 | 0.864000 | 0.812000 | 0.812000 | 0.700000 | 0.700000 | 0.600000 | 0.600000 | 해당 없음 | 해당 없음 | 일치 |
| Substitute query 500 | 0.920000 | 0.920000 | 0.840000 | 0.840000 | 1.000000 | 1.000000 | 0.600000 | 0.600000 | 해당 없음 | 해당 없음 | 일치 |
| Substitute query 1000 | 0.902000 | 0.902000 | 0.822000 | 0.822000 | 1.000000 | 1.000000 | 0.600000 | 0.600000 | 해당 없음 | 해당 없음 | 일치 |
| Watermarked ownership check | 1.000000 | 1.000000 | 0.868000 | 0.868000 | 1.000000 | 1.000000 | 0.600000 | 0.600000 | 0.868000 | 0.868000 | 일치 |

<!-- submission-metric-chart:start -->
**그림 1. W13 metrics summary chart**

![W13 metrics summary chart](assets/w13_metric_chart.png)

출처: `04_experiment/outputs/metrics_summary.csv`. 이 그래프는 공개 toy/synthetic 산출물 기반이며 실제 공격 성능이나 운영 환경 성능으로 일반화하지 않는다. 현재 그래프는 extraction_fidelity, substitute_accuracy, watermark_detection, false_positive_rate, utility_accuracy를 시각화한다.
<!-- submission-metric-chart:end -->

### 8.4 False Positive 기반 ownership 검증 한계

| 검증 항목 | 단독 해석 위험 | 보완 지표 |
|---|---|---|
| Watermark Detection | 높으면 소유권 증거처럼 보일 수 있음 | FPR, FNR, p-value, 대조군 |
| False Positive Rate | 높으면 무관 모델도 소유 모델처럼 판단될 수 있음 | unrelated model control, random trigger control |
| Extraction Fidelity | 높으면 추출 위험을 보여주지만 ownership 증거는 아님 | query budget, utility, trigger inheritance |
| Utility Accuracy | 워터마크 삽입이 모델 성능을 해치지 않는지 확인 | clean accuracy, task score |
| Query Budget | 공격 비용과 위험 노출 범위 | rate limit, monitoring, logging |

---

## 9. 기말논문 연결

W13은 기말논문에서 “모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크 연구”로 확장할 수 있다. 핵심 기여는 query budget, extraction fidelity, substitute accuracy, watermark detection, false positive rate, utility accuracy, reproducibility evidence를 같은 표에서 보고하는 구조다.

| 기말논문 장 | W13 반영 내용 |
|---|---|
| 1장 서론 | 모델 자체가 보호해야 할 지식재산이라는 문제의식 |
| 2장 관련연구 | model stealing, watermarking, DNN watermark, ModelShield, GAN security 문헌 정리 |
| 3장 위협모형 | model behavior, API log, watermark, fingerprint, trigger set 보호 자산 정의 |
| 4장 연구방법 | extraction fidelity, query budget, detection, FPR, utility 설계 |
| 5장 분석 | query budget별 substitute model 결과와 ownership check 비교 |
| 6장 결론 | 모델 IP 보호는 추출 위험과 소유권 검증 신뢰성을 함께 평가해야 함 |

---

## 10. AI 도구 활용 기록

AI 도구는 문헌 요약, 코드 점검, 문장 구조화, 그래프 생성 보조에 사용하였다. 모든 DOI/URL, 실험 수치, 본문 인용, 결론은 작성자가 outputs 파일과 로컬 참고문헌 검증표를 대조하여 검증한다.

| 항목 | 내용 |
|---|---|
| 사용 도구명 | Codex, ChatGPT 계열 도구 |
| 사용 목적 | 문헌 요약 정리, 보고서 구조화, 안전한 toy/synthetic 실험 결과 표기 점검, 그래프 생성 보조, 제출 전 체크리스트 정리 |
| AI 산출물 반영 위치 | `07_week_submission/w13_submission_report.md`, `07_week_submission/assets/w13_metric_chart.png`, `05_ai_worklog/ai_disclosure_draft.md` |
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
| P01 공식 DOI 검증 | 완료 | DOI `10.1145/3595292` 기준 |
| P02 지정 논문 원문 확보 | 확인 필요 | 현재 로컬 PDF는 관련 보조 문헌 |
| P03 공식 DOI 검증 | 완료 / 확인 필요 | DOI 확인, 강의계획서 표기 차이 확인 필요 |
| P04 공식 DOI 검증 | 완료 | IEEE TIFS DOI 확인 |
| P05 지정 논문 원문 확보 | 확인 필요 | 현재 로컬 PDF는 관련 보조 문헌 |
| false positive 해석 보완 | 완료 | FPR 0.600000 한계 명시 |
| 실험 outputs 파일 존재 확인 | 완료 | 실험 보고서 기준 CSV/JSON/run_log 존재 |
| 실험 결과와 보고서 수치 일치 | 완료 | 실험 보고서 수치 기준 반영 |
| 그래프 수치 확인 | 완료 | fidelity/accuracy/detection/FPR/utility 기준 표와 일치 |
| AI 활용 고지 작성 | 완료 |  |
| DOCX/PDF 제출본 생성 | 필요 | `07_week_submission/exports/` 권장 |
| 최종 사람이 검토할 항목 표시 | 완료 | P02/P05 원문 확인, PDF 보관 정책, Word/PDF 렌더링 |

---

## 12. 참고문헌 검증표

| 번호 | 참고문헌 | DOI/URL | 상태 | 비고 |
|---:|---|---|---|---|
| [1] | Daria/Daryna Oliynyk et al., “I Know What You Trained Last Summer: A Survey on Stealing Machine Learning Models and Defences,” ACM Computing Surveys, 2023 | `https://doi.org/10.1145/3595292`; arXiv `https://arxiv.org/abs/2206.08451` | 공식 DOI 확인 | 로컬 PDF는 accepted/arXiv 계열 메타데이터 포함 |
| [2] | Peigen Ye et al., “Securing Large Language Models: A Survey of Watermarking and Fingerprinting Techniques,” ACM Computing Surveys, 2026 | `https://doi.org/10.1145/3773028` | 공식 DOI 확인 | 현재 로컬 PDF는 Liang et al. LLM watermarking 관련 보조 문헌 |
| [3] | Yue Li, Hongxia Wang, Mauro Barni, “A survey of Deep Neural Network watermarking techniques,” Neurocomputing, 2021 | `https://doi.org/10.1016/j.neucom.2021.07.051`; arXiv `https://arxiv.org/abs/2103.09274` | 공식 DOI 확인 | 강의계획서 저자명·제목 표기 차이 확인 필요 |
| [4] | Kaiyi Pang et al., “ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack,” IEEE TIFS, 2025 | `https://doi.org/10.1109/TIFS.2025.3530691`; arXiv `https://arxiv.org/abs/2405.02365` | 공식 DOI 확인 | arXiv v4는 사전판 |
| [5] | Chenhan Zhang et al., “Generative Adversarial Networks: A Survey on Attack and Defense Perspective,” ACM Computing Surveys, 2023/2024 | `https://doi.org/10.1145/3615336` | 공식 DOI 확인 | 현재 로컬 PDF는 Cai et al. GAN privacy/security 관련 보조 문헌 |

---

## 13. 부록 A. KCI 논문 형식 전환 아이디어

### A.1 제목 후보

| 번호 | 국문 제목 후보 | 영문 제목 후보 | 대상 시스템 | 보안 위협 | 연구방법 | 예상 기여 |
|---:|---|---|---|---|---|---|
| 1 | 모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크 연구 | A Multi-Metric Evaluation Framework for Ownership Verification After Model Extraction | ML/LLM API 모델 | model extraction, watermark forgery | 문헌분석 + synthetic toy 실험 | fidelity·detection·FPR 통합 평가표 |
| 2 | Query Budget이 모델 추출 유사도와 워터마크 검출률에 미치는 영향 분석 | An Analysis of the Impact of Query Budget on Model Extraction Fidelity and Watermark Detection | 공개 API 기반 모델 | query-response extraction | toy 대체 모델 실험 | query budget 기반 위험 평가 |
| 3 | 모델 워터마킹 기반 소유권 검증에서 False Positive Rate의 영향 연구 | A Study on the Impact of False Positive Rate in Model Watermark-Based Ownership Verification | watermarked ML model | false ownership claim, watermark forgery | trigger-set toy evaluation | FPR 중심 ownership 검증 한계 분석 |

추천 최종 제목은 “모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크 연구”이다. 국문초록은 모델 IP 보호와 소유권 검증을 위해 query budget, extraction fidelity, substitute accuracy, watermark detection, FPR, utility accuracy, reproducibility evidence를 통합하는 평가 프레임워크를 제안하는 방향으로 구성한다.

### A.2 연구문제

- RQ1. Query budget이 extraction fidelity와 substitute accuracy에 미치는 영향은 무엇인가?
- RQ2. Watermark detection과 false positive rate를 함께 고려할 때 소유권 검증 신뢰성은 어떻게 달라지는가?
- RQ3. Model extraction 이후 trigger-set 기반 watermark signal은 어떤 조건에서 소유권 증거로 약해지는가?

---

## 14. 부록 B. SCI 논문 형식 전환 아이디어

SCI 제목 후보는 “A Multi-Metric Evaluation Framework for Model Extraction Risk and Watermark-Based Ownership Verification”이다.

Structured abstract는 Background, Problem, Method, Results, Contribution, Implications로 구성한다. 결과 문장은 W13 toy evaluation이 query 500 조건에서 extraction fidelity 0.920000, watermark detection 1.000000을 기록했지만 false positive proxy도 0.600000으로 높게 나타났다는 수준으로 제한한다. 실제 상용 API 공격, 실제 모델 탈취, 실제 소유권 분쟁 증거로 일반화하지 않는다.

| 연구축 | 대표 논문 | 역할 |
|---|---|---|
| Model stealing taxonomy | Oliynyk et al. | model stealing/extraction 공격·방어 분류 |
| Watermarking/fingerprinting | Ye et al. | LLM/deep learning model watermarking/fingerprinting |
| DNN watermarking | Li, Wang, Barni | fidelity, robustness, capacity, ownership verification |
| ModelShield | Pang et al. | extraction 이후 adaptive robust watermark 검증 |
| GAN attack/defense | Zhang et al. | 생성모형 IP·privacy·misuse 보조 배경 |

---

## 15. 부록 C. 제출 파일 위치와 변환 권장

| 파일 | 설명 |
|---|---|
| `07_week_submission/w13_submission_report.md` | 본 제출용 보고서 원본 |
| `07_week_submission/assets/w13_metric_chart.png` | 제출 보고서 그래프 |
| `04_experiment/experiment_report.md` | 실험 근거 보고서 |
| `04_experiment/outputs/` | 실험 결과 근거 파일 위치 |
| `05_ai_worklog/ai_disclosure_draft.md` | AI 활용 고지 근거 |

Word 제출본은 다음 위치에 생성해 관리한다.

```text
03_weekly_reports/w13_model_stealing_watermarking/07_week_submission/exports/w13_submission_report.docx
```

PDF 제출본은 Word에서 최종 육안 검수 후 다음 위치에 저장한다.

```text
03_weekly_reports/w13_model_stealing_watermarking/07_week_submission/exports/w13_submission_report.pdf
```

수식은 GitHub와 Word 변환을 모두 고려하여 Markdown 표 안에 넣지 않고, `$$...$$` block math로 유지한다.
