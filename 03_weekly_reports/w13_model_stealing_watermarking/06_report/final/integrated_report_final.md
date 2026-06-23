# W13 모델 지식재산(IP)·모델 도난·모델 추출 위협 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W13 |
| 주제 | 모델 지식재산(IP)·모델 도난·모델 추출 위협 |
| AI 원리 | Model IP, model stealing, model extraction, watermarking/fingerprinting |
| 보안 이슈 | query abuse, model extraction, ownership verification, false positive |
| 작성일 | 2026-06-23 |
| 문서 상태 | 제출용 최종 초안, 사람 검토 필요 |
| 실험 근거 | `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md` |
| 안전 범위 | 실제 API 공격, 실제 LLM 탈취, 무단 대량 질의, 개인정보 기반 평가는 제외 |

## 1. 한 문장 요약

W13는 query-response 기반 모델 추출 위험과 워터마크 기반 소유권 검증을 함께 다루며, 실험 결과는 watermark detection만이 아니라 false positive rate, utility accuracy, query budget, 재현성 근거를 함께 보고해야 함을 보여준다.

## 2. 학습 배경과 주차 목표

### 2.1 이번 주 주제의 위치

W13은 W01~W12에서 다룬 AI 보안 평가축을 모델 지식재산, 모델 도난, 모델 추출, 워터마킹, 핑거프린팅 문제로 확장하는 주차다. W12가 모델의 강건성·설명안정성·공정성을 다뤘다면, W13은 모델 자체가 경제적·기술적 자산이며, 공개 API의 query-response 정보만으로도 모델 행동이 모방될 수 있다는 점을 다룬다[1]. 또한 워터마킹은 소유권 검증 수단이 될 수 있지만, detection rate뿐 아니라 false positive, utility, robustness, query budget, 재현성을 함께 보고해야 한다[2][3][4].

### 2.2 강의계획서상 학습목표

- Model IP, model stealing, model extraction의 개념과 위협모형을 정리한다.
- Watermarking과 fingerprinting의 평가항목을 이해한다.
- Query budget과 extraction fidelity의 관계를 설명한다.
- Watermark detection과 false positive rate를 함께 기록해야 하는 이유를 설명한다.
- 모델 추출 이후 소유권 검증을 위한 다중지표 평가 프로토콜을 설계한다.

### 2.3 이번 주 핵심 질문

1. Query-response 정보만으로 모델 행동은 어느 정도 모방될 수 있는가?
2. Extraction fidelity와 substitute accuracy는 각각 무엇을 의미하는가?
3. Watermark detection이 높아도 false positive가 높으면 왜 소유권 증거가 약한가?
4. 모델 IP 보호에서 utility, detection, FPR, query cost는 어떤 trade-off를 만드는가?
5. W13의 synthetic toy 실험을 KCI 또는 SCI 논문 주제로 발전시키려면 어떤 연구문제가 적절한가?

## 3. AI 원리 70% 정리

표 1. W13 핵심 개념과 보안 연결

| 개념 | 설명 | 보안 연결 |
|---|---|---|
| Model IP | 모델 파라미터, 구조, 학습 데이터, 출력 행동, 생성물 출처에 담긴 경제적·기술적 가치 | 도난·복제·무단 상업화 위험 |
| Model stealing | 모델의 지식 또는 행동을 무단으로 복제하려는 공격군 | confidentiality와 accountability 약화 |
| Model extraction | query-response 쌍을 이용해 victim behavior 또는 decision boundary를 모방하는 절차 | extraction fidelity, query budget |
| Substitute model | 공격자가 수집한 응답으로 학습한 대체 모델 | substitute accuracy, utility |
| Watermarking | 모델 또는 생성물에 소유권 검증 신호를 삽입하는 기술 | detection, robustness, false positive |
| Fingerprinting | 모델 고유 행동 또는 경계 특성을 식별 신호로 사용하는 기술 | copy detection, provenance |

핵심 지표는 다음과 같다.

| 지표 | 계산/의미 | W13 값 |
|---|---|---|
| Extraction Fidelity | victim과 substitute의 출력 일치율 | 0.864000, 0.920000, 0.902000 |
| Substitute Accuracy | true label 기준 대체 모델 성능 | 0.812000, 0.840000, 0.822000 |
| Watermark Detection | trigger signature 일치율 | 0.700000, 1.000000, 1.000000 |
| False Positive Rate | clean control이 trigger와 우연히 일치한 비율 | 0.600000 |
| Utility Accuracy | victim clean accuracy | 0.868000 |

## 4. 보안 이슈 30% 정리

모델 도난과 모델 추출은 query-response 정보를 통해 모델 행동이나 결정경계를 모방하려는 공격군으로 분류된다[1]. Watermarking과 fingerprinting은 모델 또는 생성물에 소유권 검증 신호를 남기는 접근이지만 detection rate와 false positive를 함께 봐야 한다[2]. DNN watermarking 연구는 fidelity, robustness, capacity 사이의 trade-off를 핵심 요구조건으로 다룬다[3]. ModelShield는 모델 추출 이후에도 소유권 신호를 검출하기 위한 방어 접근을 제시한다[4]. 생성모형 보안 문헌은 모델 IP와 생성물 provenance, privacy/security risk가 함께 관리되어야 함을 보여준다[5].

| 보안 관점 | 관련 위협 | W13 평가 연결 |
|---|---|---|
| Confidentiality | 모델 행동·결정경계 유출 | extraction fidelity |
| Integrity | watermark removal, forgery | watermark detection |
| Availability | query abuse, API cost exhaustion | query budget |
| Privacy | 도난 모델을 통한 학습 데이터 추론 가능성 | 개인정보 제외 및 한계 표시 |
| Safety | 도난 생성모형 오용 | 생성물 traceability |
| Accountability | ownership verification failure | FPR, 대조군, run log |

## 5. 논문 5편 요약

표 2. 관련 문헌 5편 요약

| ID | 문헌 | 공식 검증 상태 | W13 역할 |
|---|---|---|---|
| P01 | Oliynyk, Mayer, Rauber, "I Know What You Trained Last Summer" | DOI `10.1145/3595292`, ACM CSUR 55(14s), 1-41 확인 | model stealing/extraction taxonomy |
| P02 | 지정: Ye et al. / 로컬: Liang et al., "Watermarking Techniques for Large Language Models" | 로컬은 arXiv:2409.00089v1 대체 PDF. 지정 논문 원문 확보 필요 | LLM watermarking 보조 배경 |
| P03 | Li, Wang, Barni, "A survey of Deep Neural Network watermarking techniques" | DOI `10.1016/j.neucom.2021.07.051`, Neurocomputing 461, 171-193 확인. 강의계획서 표기 차이 있음 | DNN watermarking trade-off |
| P04 | Pang et al., "ModelShield" | DOI `10.1109/TIFS.2025.3530691`, IEEE TIFS 20, 1767-1782 확인 | extraction 이후 ownership check |
| P05 | 지정 후보: Chenhan Zhang et al. / 로컬: Cai et al. | 지정 후보 DOI `10.1145/3615336` 확인. 로컬 PDF는 SUBSTITUTE | GAN attack/defense 또는 privacy/security 보조 배경 |

## 6. 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | AI 원리 기여 | 보안 위협 연결 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|---|
| P01 | 모델 도난·모델 추출 공격과 방어를 어떻게 체계화할 것인가 | model stealing taxonomy, attack goal, defense selection guideline | 문헌조사 | query-response learning, substitute model, fidelity | model extraction, query abuse, behavior leakage | extraction fidelity, query cost, attack goal | 최신 LLM/생성모형 방어는 추가 문헌 필요 | 위협모형과 query budget 지표 |
| P02 | Watermarking/fingerprinting 또는 LLM watermarking을 어떻게 분류할 것인가 | detection/robustness taxonomy | 현재 로컬 PDF는 LLM watermarking 대체 문헌 | watermark signal, fingerprint, traceability | watermark removal, paraphrasing, semantic shift | detection, robustness, quality, FPR | 지정 P02와 로컬 PDF 불일치 | 보조 배경, 지정 논문처럼 인용 금지 |
| P03 | DNN watermarking의 요구조건과 taxonomy는 무엇인가 | fidelity-robustness-capacity trade-off | Neurocomputing 문헌 | static/dynamic watermarking | watermark removal, forgery, ownership ambiguity | fidelity, robustness, capacity, FPR | 강의계획서 저자명·제목 차이 확인 필요 | 워터마크 평가 지표 정의 |
| P04 | 모델 추출 이후에도 소유권 신호를 안정적으로 검출할 수 있는가 | ModelShield, adaptive watermark, robust detection | IEEE TIFS/arXiv | watermark inheritance와 detection | imitation/model extraction | detection, robustness, utility, FPR | 법적 증거력·adaptive removal 기준 필요 | toy trigger-set 실험의 직접 배경 |
| P05 | GAN 또는 생성모형의 attack/defense와 privacy/security를 어떻게 분류할 것인가 | GAN security/privacy survey 또는 attack/defense survey | 현재 로컬 PDF는 대체 문헌 | generative model misuse, provenance | 데이터 누출, 생성물 출처 모호성 | application risk, privacy/security metric | 지정 P05와 로컬 PDF 불일치 | 생성모형 보호 자산 보조 배경 |

## 7. Research Track 분석

표 3. W13 Research Track 요약

| 항목 | 내용 |
|---|---|
| 연구문제 | query-response 기반 모델 추출 위험과 워터마크 기반 소유권 검증 신뢰성을 어떻게 함께 평가할 것인가 |
| 대상 시스템 | 공개 API 또는 제한 인터페이스로 제공되는 ML/LLM/생성모형 서비스 |
| 보호 자산 | 모델 파라미터, 출력 행동, 결정경계, 워터마크, fingerprint, 생성물 출처, API 로그 |
| 공격자 능력 | 반복 질의, query-response 수집, substitute model 학습, watermark removal 또는 imitation |
| 평가 지표 | extraction fidelity, substitute accuracy, query budget, watermark detection, false positive, utility accuracy |
| 제외 범위 | 실제 상용 API extraction, 무단 대량 질의, 개인정보 사용, live model theft |

그림 1. 모델 추출 및 워터마크 기반 소유권 검증 평가 흐름

```text
Victim Model / Public API
        |
        v
Query-Response Collection
        |
        v
Substitute Model Training
        |
        v
Extraction Evaluation
        |-- Extraction Fidelity
        |-- Substitute Accuracy
        `-- Query Budget
        |
        v
Watermark / Trigger-Set Check
        |-- Watermark Detection
        |-- False Positive Rate
        `-- Utility Accuracy
        |
        v
Ownership Verification Report
        `-- seed, config, outputs, run_log, controls
```

## 8. 실습 보고서

표 4. W13 실습 설계

| Item | Description |
|---|---|
| Dataset | Synthetic binary classification |
| Victim model | Toy logistic classifier with watermark trigger set |
| Substitute model | Query-response 1-nearest-neighbor classifier |
| Query budgets | 100, 500, 1000 |
| Watermark triggers | 20 |
| Watermark fraction | 0.05 |
| Trigger radius | 0.03 |
| Metrics | Extraction fidelity, substitute accuracy, watermark detection, false positive rate, utility accuracy |
| Seed | 42 |
| Output files | `metrics_summary.csv`, `results.json`, `run_log.md` |

표 5. W13 실습 결과

| 조건 | Query Budget | Extraction Fidelity | Substitute Accuracy | Watermark Detection | False Positive Rate | Utility Accuracy |
|---|---:|---:|---:|---:|---:|---:|
| Baseline victim model | 0 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 |
| Substitute query 100 | 100 | 0.864000 | 0.812000 | 0.700000 | 0.600000 |  |
| Substitute query 500 | 500 | 0.920000 | 0.840000 | 1.000000 | 0.600000 |  |
| Substitute query 1000 | 1000 | 0.902000 | 0.822000 | 1.000000 | 0.600000 |  |
| Watermarked ownership check | 0 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 |

### False Positive 해석 보완

본 실험에서 watermark detection은 일부 조건에서 1.000000으로 나타났지만, false positive proxy도 0.600000으로 높게 나타났다. 이는 trigger-set 기반 소유권 검증이 detection rate만으로는 충분하지 않으며, clean control model, unrelated model, random trigger set, 복수 seed, 통계적 유의성 검정이 함께 필요함을 의미한다. 따라서 본 결과는 “소유권 검증 성공”이 아니라 “소유권 검증에는 detection rate와 false positive rate를 함께 기록해야 한다”는 교육용 근거로 해석한다.

표 6. False Positive 기반 ownership 검증 한계

| 검증 항목 | 단독 해석 위험 | 보완 지표 |
|---|---|---|
| Watermark Detection | 높으면 소유권 증거처럼 보일 수 있음 | FPR, FNR, p-value, 대조군 |
| False Positive Rate | 높으면 무관 모델도 소유 모델처럼 판단될 수 있음 | unrelated model control, random trigger control |
| Extraction Fidelity | 높으면 추출 위험을 보여주지만 ownership 증거는 아님 | query budget, utility, trigger inheritance |
| Utility Accuracy | 워터마크 삽입이 모델 성능을 해치지 않는지 확인 | clean accuracy, task score |
| Query Budget | 공격 비용과 위험 노출 범위 | rate limit, monitoring, logging |

이 결과는 synthetic binary classification 기반 toy 실험의 평가 형식 검증용 수치이며, 실제 상용 API, 실제 LLM, 실제 모델 탈취, 무단 대량 질의, 개인정보 기반 모델 추출 또는 소유권 분쟁 증거로 일반화하지 않는다.

## 9. AI 도구 활용 기록

Codex를 사용해 지시문 분해, 문헌 검증표 보완, SUBSTITUTE PDF 표시, 실험 코드/설정 정합성 점검, false positive 해석 보완, KCI/SCI 전환 섹션 작성, 제출용 Markdown/HTML 정리를 수행했다. AI가 생성한 문장은 초안으로 취급하며, 최종 제출자는 인용, DOI, 실험결과, 연구윤리 책임을 직접 확인해야 한다.

## 10. 토론 질문

1. Watermark detection이 1.000000이어도 false positive가 0.600000이면 소유권 검증 기준은 어떻게 설계해야 하는가?
2. Query budget과 fidelity를 보고할 때 공격 재현성과 악용 방지 사이의 균형은 어디에 둘 것인가?
3. 프롬프트 지정 문헌과 로컬 PDF가 다를 때 제출물에서 어떻게 투명하게 표시할 것인가?
4. ModelShield류 접근이 법적 소유권 분쟁에서 쓰이려면 어떤 대조군과 통계 검정이 필요한가?

## 11. 기말논문 연결

추천 주제는 “모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크 연구”이다. W13은 관련연구, 위협모형, 평가방법, 보안적 함의 장에 직접 연결된다. 핵심 기여 후보는 query budget, extraction fidelity, substitute accuracy, watermark detection, false positive rate, utility accuracy, reproducibility evidence를 같은 표에서 보고하는 구조다.

## 12. KCI 논문 형식 전환

### 12.1 KCI형 제목 후보

표 7. KCI 논문 제목 후보

| 번호 | 국문 제목 후보 | 영문 제목 후보 | 대상 시스템 | 보안 위협 | 연구방법 | 예상 기여 |
|---:|---|---|---|---|---|---|
| 1 | 모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크 연구 | A Multi-Metric Evaluation Framework for Ownership Verification After Model Extraction | ML/LLM API 모델 | model extraction, watermark forgery | 문헌분석 + synthetic toy 실험 | fidelity·detection·FPR 통합 평가표 |
| 2 | Query Budget이 모델 추출 유사도와 워터마크 검출률에 미치는 영향 분석 | An Analysis of the Impact of Query Budget on Model Extraction Fidelity and Watermark Detection | 공개 API 기반 모델 | query-response extraction | toy substitute model 실험 | query budget 기반 위험 평가 |
| 3 | 모델 워터마킹 기반 소유권 검증에서 False Positive Rate의 영향 연구 | A Study on the Impact of False Positive Rate in Model Watermark-Based Ownership Verification | watermarked ML model | false ownership claim, watermark forgery | trigger-set toy evaluation | FPR 중심 ownership 검증 한계 분석 |

### 12.2 추천 최종 제목

- 국문: 모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크 연구
- 영문: A Multi-Metric Evaluation Framework for Ownership Verification After Model Extraction

### 12.3 국문초록 초안

본 연구는 모델 지식재산 보호와 모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크를 제안한다. Model stealing, model extraction, DNN/LLM watermarking, ModelShield, 생성모형 privacy/security 관련 선행연구를 비교하고, query budget, extraction fidelity, substitute accuracy, watermark detection, false positive rate, utility accuracy, reproducibility evidence의 평가축을 도출한다. 또한 실제 API나 상용 모델을 사용하지 않고 synthetic binary classification과 toy logistic classifier, query-response 1-nearest-neighbor substitute model을 활용하여 query budget별 모델 행동 유사도와 watermark detection 변화를 기록한다. 본 연구는 false positive proxy가 높을 경우 watermark detection만으로 소유권을 단정할 수 없음을 보이며, 소유권 검증에서 detection rate와 false positive rate를 함께 보고해야 함을 제안한다.

### 12.4 영문초록 초안

This study proposes a multi-metric evaluation framework for model intellectual property protection and ownership verification after model extraction. By reviewing studies on model stealing, model extraction, DNN/LLM watermarking, ModelShield, and generative model privacy and security, this report derives evaluation axes including query budget, extraction fidelity, substitute accuracy, watermark detection, false positive rate, utility accuracy, and reproducibility evidence. A safe toy experiment using synthetic binary classification, a toy logistic classifier, and a query-response 1-nearest-neighbor substitute model is used to examine how query budgets affect behavior mimicry and watermark detection. The goal is not to reproduce real model theft, but to demonstrate that watermark detection must be interpreted together with false positive rate and utility.

### 12.5 키워드

| 구분 | 키워드 |
|---|---|
| 국문 | 모델 도난, 모델 추출, 모델 워터마킹, 소유권 검증, Query Budget, False Positive |
| 영문 | Model Stealing, Model Extraction, Model Watermarking, Ownership Verification, Query Budget, False Positive |

### 12.6 연구문제

- RQ1. Query budget이 증가할 때 extraction fidelity와 substitute accuracy는 어떻게 변화하는가?
- RQ2. 모델 추출 이후 watermark detection은 소유권 검증에 어떤 정보를 제공하는가?
- RQ3. False positive rate가 높을 때 watermark detection 결과는 어떻게 해석해야 하는가?
- RQ4. 소유권 검증 평가에서 utility accuracy와 query cost는 어떤 역할을 하는가?

### 12.7 연구방법

문헌분석은 W13 논문 5편을 model stealing, watermarking/fingerprinting, DNN watermarking, ModelShield, GAN privacy/security 축으로 비교한다. 위협모형은 model parameters, output behavior, decision boundary, watermark, fingerprint, generation provenance, API logs를 보호 자산으로 설정한다. 모의실험은 synthetic binary classification 기반 toy logistic classifier와 query-response 1NN substitute model을 사용한다.

### 12.8 보안적 함의

Confidentiality는 query-response behavior가 모델 결정경계와 모델 IP를 노출할 수 있음을 뜻한다. Integrity는 watermark removal, forgery, false ownership claim이 소유권 검증을 흔들 수 있음을 뜻한다. Accountability 측면에서는 ownership claim에 detection rate, FPR, 대조군, seed, run log가 필요하다.

### 12.9 KCI 제출 가능성 점검표

| 점검 항목 | 상태 |
|---|---|
| 국문·영문 제목 후보 작성 | 완료 |
| 국문초록 초안 작성 | 완료 |
| 영문초록 초안 작성 | 완료 |
| 키워드 작성 | 완료 |
| 연구문제 작성 | 완료 |
| 연구방법 작성 | 완료 |
| 표 1개 이상 포함 | 완료 |
| 그림 1개 이상 포함 | 완료 |
| 국내 참고문헌 3편 이상 | 확인 필요 |
| 해외 참고문헌 5편 이상 | W13 기준 완료, 단 P02/P05 대체 PDF 상태 확인 필요 |
| AI 활용 고지 | 보완 완료, 사람 검토 필요 |
| 실험 outputs 파일 존재 | 완료 |
| false positive 해석 보완 | 완료 |

## 13. SCI 논문 형식 전환

### 13.1 SCI 제목 후보

A Multi-Metric Evaluation Framework for Model Extraction Risk and Watermark-Based Ownership Verification

### 13.2 Structured Abstract

#### Background

Machine learning models are valuable intellectual property assets. Public model APIs expose query-response behavior that can be used to approximate model decision boundaries, while watermarking and fingerprinting techniques are used to support ownership verification.

#### Problem

High watermark detection alone is insufficient for ownership claims when false positive rates are high. Existing evaluations often report extraction fidelity or watermark detection separately, without jointly considering query budget, utility, false positives, and reproducibility evidence.

#### Method

This study synthesizes five representative studies on model stealing, model watermarking, DNN watermarking, ModelShield, and generative model privacy and security. A safe synthetic toy experiment is used to compare query budgets and ownership checks using a toy victim classifier and a query-response substitute model.

#### Results

The W13 toy experiment shows that substitute models can reach high extraction fidelity from query-response pairs, while watermark detection can be high under larger query budgets. However, the false positive proxy is also high, showing that trigger-set detection alone is insufficient for strong ownership verification.

#### Contribution

The main contribution is a multi-metric reporting structure that integrates query budget, extraction fidelity, substitute accuracy, watermark detection, false positive rate, utility accuracy, and reproducibility evidence.

#### Implications

The framework can be extended to model IP governance, API abuse monitoring, LLM watermarking, extraction defense, ownership dispute evaluation, and MLOps audit logging.

### 13.3 Introduction 구성

모델 IP와 모델 도난 위협의 배경, 공개 API와 query-response 기반 model extraction 위험, watermarking/fingerprinting 기반 ownership verification의 필요성, detection rate 단독 평가의 한계, false positive rate와 utility accuracy의 중요성, 본 연구의 contribution을 순서대로 배치한다.

### 13.4 Related Work 축

표 8. SCI Related Work 축

| 연구축 | 대표 논문 | 역할 |
|---|---|---|
| Model stealing taxonomy | Oliynyk et al. | model stealing/extraction 공격·방어 분류 |
| Watermarking/fingerprinting | Ye et al. 또는 현재 P02 지정 논문 | deep learning model watermarking/fingerprinting, 원문 확보 필요 |
| DNN watermarking | Li, Wang, Barni 또는 현재 P03 | fidelity, robustness, capacity, ownership verification |
| ModelShield | Pang et al. | extraction 이후 adaptive robust watermark 검증 |
| GAN attack/defense 또는 private/security GAN | Zhang et al. 또는 현재 P05 지정 논문 | 생성모형 IP·privacy·misuse 보조 배경 |

### 13.5 Threat Model

Target system은 public 또는 restricted API를 통해 노출된 ML/LLM/generative model이다. Protected assets는 model parameters, model behavior, decision boundary, watermark, fingerprint, output provenance, API logs다. Excluded scope는 real commercial API extraction, unauthorized mass querying, personal data use, live model theft다.

### 13.6 Methodology

Literature matrix construction, model IP threat model design, synthetic binary classification experiment, toy victim model training, trigger-set watermark construction, query-response substitute model construction, extraction fidelity measurement, watermark detection and false positive proxy measurement, reproducibility evidence collection으로 구성한다.

### 13.7 Experimental Setup

| Item | Description |
|---|---|
| Dataset | Synthetic binary classification |
| Victim model | Toy logistic classifier with watermark trigger set |
| Substitute model | Query-response 1-nearest-neighbor classifier |
| Query budgets | 100, 500, 1000 |
| Watermark triggers | 20 |
| Watermark fraction | 0.05 |
| Trigger radius | 0.03 |
| Metrics | Extraction fidelity, substitute accuracy, watermark detection, false positive rate, utility accuracy |
| Seed | 42 |
| Output files | metrics_summary.csv, results.json, run_log.md |

### 13.8 Results

보고서 8장의 표 5와 동일하며, outputs 파일 기준으로 정리했다. outputs 파일은 모두 존재한다.

### 13.9 Discussion

Query-response pairs can approximate model behavior in a toy setting. Query budget is a risk and cost variable, not merely an experiment parameter. Watermark detection must be interpreted with false positive rate. A false positive proxy of 0.600000 means trigger-set evidence is weak unless additional controls are added. Ownership verification requires unrelated model controls, random trigger controls, multiple seeds, and statistical testing. Synthetic toy results are not legal evidence of ownership or real extraction success.

### 13.10 Limitations and Threats to Validity

Internal validity: 1NN substitute model is a toy approximation, not a real extraction attack on commercial APIs. External validity: synthetic binary classification does not represent LLMs, vision models, or generative models. Construct validity: trigger-set watermark is a deterministic toy signal, not a production-grade watermarking scheme. Legal validity: watermark detection does not establish legal ownership by itself. Literature validity: P02 and P05 are SUBSTITUTE PDFs and cannot be cited as the specified papers unless verified. Reproducibility: outputs file and report numbers match.

### 13.11 Conclusion

W13 defines model IP protection as a multi-metric security evaluation problem. The key conclusion is that model extraction risk and ownership verification must be reported using query budget, extraction fidelity, substitute accuracy, watermark detection, false positive rate, utility accuracy, and reproducibility evidence together.

## 14. 발표용 요약

발표 메시지는 세 문장으로 압축된다. 첫째, API 뒤의 모델도 query-response 정보로 행동이 모방될 수 있다. 둘째, watermark detection이 높아도 false positive가 높으면 소유권 증거는 약하다. 셋째, 모델 IP 보호는 fidelity, detection, FPR, utility, query budget, reproducibility를 함께 보고하는 평가 문제다.

## 15. 참고문헌 검증표

| 번호 | 참고문헌 | DOI/URL | 상태 |
|---|---|---|---|
| [1] | Daryna Oliynyk, Rudolf Mayer, Andreas Rauber, "I Know What You Trained Last Summer: A Survey on Stealing Machine Learning Models and Defences" | `10.1145/3595292` | 확인 완료 |
| [2] | Ye et al., "A Survey of Watermarking and Fingerprinting Techniques for Deep Learning Models" | 지정 DOI 확인 필요 | 지정 논문 원문 확인 필요. 현재 P02는 Liang et al. SUBSTITUTE PDF |
| [3] | Yue Li, Hongxia Wang, Mauro Barni, "A survey of Deep Neural Network watermarking techniques" | `10.1016/j.neucom.2021.07.051` | DOI 확인 완료, 강의계획서 표기 차이 확인 필요 |
| [4] | Kaiyi Pang et al., "ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack" | `10.1109/TIFS.2025.3530691` | 확인 완료 |
| [5] | Chenhan Zhang et al., "Generative Adversarial Networks: A Survey on Attack and Defense Perspective" / 로컬 Cai et al. substitute | `10.1145/3615336` 후보 확인 | 지정 후보 확인, 로컬 PDF 불일치 |

PDF 5개는 이미 git 추적 대상이다. 공개 GitHub 저장소에는 원칙적으로 PDF 원문 대신 DOI/URL, 서지정보, 요약만 남기는 것이 안전하다. 사용자 승인 없이 삭제하지 않았으며, 공개 전 삭제 또는 비공개 보관 전환 검토가 필요하다.

## 16. 자기 점검표

| 점검 항목 | 상태 | 비고 |
|---|---|---|
| 1장 한 문장 요약 작성 | 완료 |  |
| 2장 학습 배경과 주차 목표 작성 | 완료 |  |
| AI 원리 70% 정리 | 완료 |  |
| 보안 이슈 30% 정리 | 완료 |  |
| 논문 5편 요약 | 완료 / 확인 필요 | P02/P05 원문 확보 필요 |
| 논문 5편 비교표 보완 | 완료 / 확인 필요 | 대체 PDF 상태 반영 |
| Research Track 5요소 작성 | 완료 | 연구문제, 위협모형, 평가방법, 재현성, 오픈문제 |
| P01 공식 DOI 검증 | 완료 | DOI `10.1145/3595292` |
| P02 지정 논문 원문 확보 | 확인 필요 | 현재 SUBSTITUTE PDF |
| P03 DOI/URL 검증 | 완료 / 확인 필요 | DOI 확인, 강의계획서 표기 차이 |
| P04 IEEE TIFS DOI 검증 | 완료 | DOI `10.1109/TIFS.2025.3530691` |
| P05 지정 논문 원문 확보 | 확인 필요 | 지정 후보 DOI 확인, 로컬 PDF 불일치 |
| 실험 outputs 파일 존재 확인 | 완료 | CSV/JSON/run log |
| 실험 결과와 보고서 수치 일치 | 완료 | outputs 기준 |
| false positive 해석 보완 | 완료 | 0.600000 한계 명시 |
| KCI 논문 형식 전환 작성 | 완료 |  |
| SCI 논문 형식 전환 작성 | 완료 |  |
| 본문 인용과 참고문헌 대응 | 완료 / 확인 필요 | P02/P05 원문 확인 필요 |
| 표·그림 번호 정리 | 완료 | 표 1-8, 그림 1 |
| AI 활용 고지 작성 | 완료 | 별도 고지서 보완 |
| PDF 저작권 위험 점검 | 완료 / 조치 필요 | 삭제는 미수행 |
| 최종 사람이 검토할 항목 표시 | 완료 | 제출 확정 아님 |
