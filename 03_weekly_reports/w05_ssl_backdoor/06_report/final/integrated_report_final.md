# W05 자기지도학습·파운데이션 모델 & Poisoning/Backdoor 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W05 |
| 주제 | 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 최종 초안, 최종 제출 확정 아님 |
| 핵심 산출물 | 논문 검증표, 논문 요약, synthetic toy 실험, KCI/SCI 전환 섹션, 발표자료 |
| 안전 범위 | 공개 문헌과 synthetic/toy data만 사용. 실제 개인정보, 실제 운영 서비스, 무단 API 질의, 악성코드 실행, 실제 공격 절차 없음 |

## 1. 한 문장 요약

W05는 자기지도학습과 파운데이션 모델의 pretraining representation을 보안 자산으로 보고, poisoning/backdoor가 clean accuracy와 별도로 ASR, representation shift, detection rate, clean FPR을 어떻게 변화시키는지 안전한 toy protocol로 정리한다.

## 2. 학습 배경과 주차 목표

### 2.1 이번 주 주제의 위치

W05는 W01의 ML 생명주기 보안 평가, W02의 데이터 오염, W03의 표현공간과 입력 교란, W04의 Transformer/NLP 보안 논의를 자기지도학습과 파운데이션 모델의 pretraining 단계로 확장하는 주차다. W05의 핵심은 라벨이 없는 사전학습 환경에서도 데이터 수집, augmentation, positive/negative pair 구성, pretraining corpus, representation space가 보안 자산이 된다는 점이다. 이후 W06 생성모형/딥페이크, W07 LLM 보안, W10 연합학습 poisoning, W13 모델 도난 및 워터마킹과 연결된다.

### 2.2 강의계획서상 학습목표

- Self-supervised learning의 contrastive, masked, predictive 문제정의를 정리한다.
- 비디오 SSL의 사전학습-전이학습 평가 구조를 이해한다.
- Poisoning/backdoor가 representation space에 미치는 영향을 측정하는 평가축을 설계한다.

### 2.3 이번 주 핵심 질문

1. 자기지도학습은 라벨 없이 어떤 supervision signal을 만드는가?
2. Pretraining corpus와 augmentation 과정은 어떤 공격면을 만드는가?
3. Poisoning/backdoor는 downstream classifier보다 representation space를 어떻게 먼저 왜곡할 수 있는가?
4. Clean accuracy가 유지되더라도 ASR과 representation shift가 크면 왜 보안적으로 실패인가?
5. W05의 synthetic representation 실험을 KCI 또는 SCI 논문 주제로 발전시키려면 어떤 연구문제가 적절한가?

## 3. AI 원리 70% 정리

자기지도학습은 라벨 없이 contrastive, generative, predictive objective를 통해 표현을 학습한다[1]. SSL 응용 도메인에서는 사용자-아이템 표현이나 도메인별 데이터 구조가 보안 평가의 대상이 될 수 있다[2]. 비디오 SSL은 시간적 일관성과 cross-modal signal을 활용하므로 temporal trigger와 augmentation poisoning 가능성을 고려해야 한다[3].

**표 1. W05 핵심 개념과 보안 연결**

| 개념 | AI 원리 | 보안 연결 |
|---|---|---|
| Contrastive learning | positive pair는 가깝게, negative pair는 멀게 표현을 학습한다 | pair 오염, false positive pair, poisoned negative sampling |
| Masked/generative learning | 입력 일부를 복원하거나 미래/문맥을 예측한다 | corpus contamination, memorization, hidden target behavior |
| Representation learning | pretraining encoder가 downstream task에 전이 가능한 embedding을 만든다 | representation shift, trigger-induced target movement |
| Foundation model pretraining | 대규모 corpus와 반복 학습으로 범용 표현을 만든다 | 데이터 거버넌스, 출처 검증, reproducibility evidence |

## 4. 보안 이슈 30% 정리

Poisoning 공격은 학습 데이터 조작을 통해 모델의 최적화 경로와 최종 판단을 왜곡한다[4]. Backdoor 공격은 clean accuracy가 유지되더라도 trigger 조건에서 ASR이 높아질 수 있으므로 별도 평가가 필요하다[5]. 따라서 W05의 핵심은 정상 성능, 공격 조건 성능, 표현공간 이동, 탐지율, clean false positive를 한 표 안에서 분리하는 것이다.

**그림 1. 자기지도학습 기반 표현공간 보안 평가 흐름**

```text
Pretraining Data / Augmentation Pairs
        |
        v
Self-Supervised Representation Learning
        |
        v
Clean Representation Evaluation ---> Clean Accuracy
        |
        v
Poisoned Sample / Trigger Vector
        |
        v
Backdoor Representation Evaluation ---> Poisoned Clean Accuracy, ASR, Mean Shift
        |
        v
Consistency Defense Check ---> ASR after Defense, Detection Rate, Clean FPR
        |
        v
Reproducibility Evidence ---> seed, config, Docker, outputs, run_log
```

## 5. 논문 5편 요약

**표 2. 관련 문헌 5편 요약**

| 번호 | 문헌 | 출판 정보 | W05 역할 | 검증 상태 |
|---|---|---|---|---|
| [1] | Gui et al., A Survey on Self-Supervised Learning: Algorithms, Applications, and Future Trends | IEEE TPAMI 46(12), 9052-9071, 2024, DOI `10.1109/TPAMI.2024.3415112` | SSL 알고리즘과 응용 taxonomy | DOI 확인. 강의계획서 `Yan Gui` 표기 확인 필요 |
| [2] | Ren et al., A Comprehensive Survey on Self-Supervised Learning for Recommendation | ACM Computing Surveys 58(1), Article 22, 1-38, DOI `10.1145/3746280` | 추천 시스템 SSL 도메인 survey | DOI 확인. 강의계획서 지정 일반 SSL survey와 동일 여부 확인 필요 |
| [3] | Schiappa et al., Self-Supervised Learning for Videos: A Survey | ACM Computing Surveys 55(13s), 1-37, DOI `10.1145/3577925` | video SSL, temporal/cross-modal representation | DOI 확인. 강의계획서 제목 차이 및 Article 번호 확인 필요 |
| [4] | Wang et al., Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems | ACM Computing Surveys 55(7), Article 134, 1-36, DOI `10.1145/3538707` | training-time poisoning taxonomy | DOI 확인. 강의계획서 제목/저자 표기 차이 확인 필요 |
| [5] | Jin et al., A survey of backdoor attacks and defences: From deep neural networks to large language models | Journal of Electronic Science and Technology 23(3), Article 100326, DOI `10.1016/j.jnlest.2025.100326` | DNN-LLM backdoor taxonomy | DOI 확인. 강의계획서 `Z. Jin` 표기 확인 필요 |

주의: W05의 P02는 강의계획서 지정 일반 자기지도학습 종합 서베이와 동일 여부를 최종 확인해야 한다. 현재 로컬 PDF는 추천 시스템 분야의 Self-Supervised Learning survey로 범위가 좁으므로, 최종 제출 전 대체 문헌 사용 여부를 확인한다.

## 6. 논문 5편 비교표

| 논문 | 차별성 | 내 논문 활용 |
|---|---|---|
| P01 | 일반 SSL 알고리즘, 응용, future trends를 넓게 정리한다 | SSL/foundation model 원리 배경 |
| P02 | 현재 로컬 PDF 기준 추천 시스템 SSL에 특화되어 있다 | 사용자-아이템 표현 오염, 추천 편향, 데이터 거버넌스 연결 |
| P03 | temporal consistency와 cross-modal video SSL을 다룬다 | 영상 SSL과 temporal trigger/augmentation poisoning 확장 |
| P04 | training-time poisoning attack/defense taxonomy를 제공한다 | W05 위협모형과 공격면 분류 핵심 근거 |
| P05 | DNN부터 LLM까지 backdoor 공격과 방어를 연결한다 | clean accuracy와 ASR 분리 평가 핵심 근거 |

P01-P03은 SSL/표현학습 원리와 응용 문헌이고, P04-P05는 poisoning/backdoor 보안 문헌이다. W05의 핵심 연결부는 pretraining representation이 보안 자산이 된다는 점이다. W05 toy 실험은 실제 SSL/foundation model 실험이 아니라 표현공간 평가축 설명용이다.

## 7. Research Track 분석

**표 3. W05 Research Track 요약**

| 항목 | 내용 |
|---|---|
| 연구문제 | SSL/foundation pretraining 표현공간에서 poisoning/backdoor 평가를 위한 최소 지표는 무엇인가 |
| 대상 시스템 | self-supervised representation learner, foundation pretraining pipeline, downstream classifier |
| 보호 자산 | pretraining corpus, augmentation pair, learned representation, downstream classifier, logs |
| 공격자 능력 | poisoned sample insertion, trigger injection, augmentation manipulation, corpus contamination |
| 평가 방법 | clean accuracy, poisoned clean accuracy, ASR, ASR after defense, mean shift, detection rate, clean FPR |
| 제외 범위 | 실제 서비스 침해, 개인정보 사용, 무단 공격, 운영 backdoor 배포 |
| 오픈 문제 | 실제 SSL encoder, multimodal data, adaptive trigger, threshold sensitivity, P02 지정 문헌 재확인 |

## 8. 실습 보고서

본 실습은 실제 SSL encoder 또는 파운데이션 모델 backdoor 공격 재현이 아니라 W05의 핵심인 표현공간 오염 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. 따라서 synthetic 2차원 표현공간 클러스터와 nearest-centroid representation classifier를 사용하되, 평가 구조는 이후 SSL encoder, 비디오 표현학습, LLM/foundation model pretraining에도 확장 가능하도록 clean accuracy, poisoned clean accuracy, ASR, mean representation shift, detection rate, clean FPR, reproducibility evidence로 분리하였다.

**표 4. W05 실습 설계**

| 항목 | 내용 |
|---|---|
| Dataset | Synthetic 2D representation clusters |
| Model/checker | Nearest-centroid representation classifier |
| Baseline | Clean representation baseline |
| Security scenario | Trigger vector shifts source embeddings toward target centroid |
| Defense/check | Paired-view consistency distance threshold |
| Seed | 42 |
| Outputs | `metrics_summary.csv`, `results.json`, `run_log.md` |

**표 5. W05 실습 결과**

| 조건 | Clean Acc. | Poisoned Clean Acc. | ASR | ASR after defense | Mean Shift | Detection Rate | Clean FPR |
|---|---:|---:|---:|---:|---:|---:|---:|
| Clean representation baseline | 1.000000 |  |  |  |  |  |  |
| Poisoned/backdoor representation |  | 1.000000 | 1.000000 |  | 2.418677 |  |  |
| Consistency defense check |  |  |  | 0.000000 | 0.090597 | 1.000000 | 0.000000 |

이 결과는 synthetic 2D representation toy 실험의 평가 형식 검증용 수치이며, 실제 SSL 모델, foundation model, 상용 시스템의 poisoning/backdoor 보안 성능으로 일반화하지 않는다.

## 9. AI 도구 활용 기록

Codex와 ChatGPT 계열 AI를 사용해 문헌 요약 보강, DOI/URL 검증 보조, 개념 설명, 문장 구조화, synthetic representation 실험 코드 작성, 발표자료 작성, KCI/SCI 섹션 보완을 수행했다. AI 산출물은 초안이며, 최종 제출자는 DOI/URL, 인용, 실험 수치, PDF 저작권 상태를 직접 확인해야 한다.

## 10. 토론 질문

1. 자기지도학습에서 라벨이 없더라도 pretraining corpus와 augmentation pair가 공격면이 되는 이유는 무엇인가?
2. Clean accuracy가 유지되는 backdoor 조건에서 ASR과 representation shift 중 어떤 지표가 더 설득력 있는가?
3. Consistency defense check가 toy threshold 실험을 넘어 실제 SSL encoder 방어로 확장되려면 어떤 검증이 필요한가?
4. P02가 강의계획서 지정 일반 SSL survey가 아니라 추천 SSL survey라면, 최종 보고서에서 대체 문헌으로 사용할 수 있는가?

## 11. 기말논문 연결

추천 주제는 `표현학습 기반 AI 시스템의 poisoning/backdoor 평가 프레임워크`다. W05에서 얻은 기여 후보는 SSL/foundation pretraining 위협모형, representation shift 기반 toy 평가표, clean performance와 ASR의 분리 기록, seed/config/output 기반 재현성 체크리스트다.

## 12. KCI 논문 형식 전환

### 12.1 KCI형 제목 후보

**표 6. KCI 논문 제목 후보**

| 번호 | 국문 제목 후보 | 영문 제목 후보 | 대상 시스템 | 보안 위협 | 연구방법 | 예상 기여 |
|---:|---|---|---|---|---|---|
| 1 | 자기지도학습 기반 AI 시스템의 Poisoning/Backdoor 평가 프레임워크 연구 | A Study on a Poisoning and Backdoor Evaluation Framework for Self-Supervised AI Systems | SSL/foundation model | Poisoning, Backdoor | 문헌분석 + synthetic representation 실험 | representation shift 기반 평가표 |
| 2 | 표현학습 공간에서 Backdoor Trigger가 공격 성공률과 탐지율에 미치는 영향 분석 | An Analysis of the Impact of Backdoor Triggers on Attack Success Rate and Detection Rate in Representation Space | 표현학습 모델 | Trigger injection, representation shift | toy 실험 + 평가 프로토콜 | ASR·mean shift·detection rate 분리 |
| 3 | 파운데이션 모델 사전학습 단계의 데이터 오염 위협과 재현성 평가 연구 | A Study on Data Poisoning Threats and Reproducibility Evaluation in Foundation Model Pretraining | foundation/pretraining pipeline | corpus poisoning, data governance risk | 문헌분석 + 체크리스트 | pretraining governance 평가 |

### 12.2 추천 최종 제목

- 국문: 자기지도학습 기반 AI 시스템의 Poisoning/Backdoor 평가 프레임워크 연구
- 영문: A Study on a Poisoning and Backdoor Evaluation Framework for Self-Supervised AI Systems

### 12.3 국문초록 초안

본 연구는 자기지도학습과 파운데이션 모델의 사전학습 단계에서 발생할 수 있는 poisoning 및 backdoor 위협을 평가하기 위한 다중지표 프레임워크를 제안한다. 자기지도학습 알고리즘, 추천 및 비디오 SSL, poisoning 공격, backdoor 공격 관련 선행연구를 비교하고, clean accuracy, poisoned clean accuracy, attack success rate, representation shift, detection rate, clean false positive rate, reproducibility evidence의 평가축을 도출한다. 또한 synthetic 2D representation cluster 기반 안전 toy experiment를 통해 trigger vector가 source class embedding을 target class centroid 방향으로 이동시키는 상황과 consistency defense check 결과를 기록한다. 본 연구는 실제 SSL 또는 파운데이션 모델의 보안 성능을 주장하지 않고, 표현공간 오염과 backdoor 평가를 위한 재현 가능한 보고 구조를 제시하는 데 목적이 있다.

### 12.4 영문초록 초안

This study proposes a multi-metric evaluation framework for poisoning and backdoor threats in self-supervised learning and foundation model pretraining. By reviewing studies on self-supervised learning, recommendation-oriented SSL, video SSL, poisoning attacks, and backdoor attacks, this report derives evaluation axes including clean accuracy, poisoned clean accuracy, attack success rate, representation shift, detection rate, clean false positive rate, and reproducibility evidence. A safe toy experiment using synthetic 2D representation clusters is used to illustrate how a trigger vector can move source-class embeddings toward the target-class centroid and how a consistency-based defense check can flag large representation shifts. The goal is not to claim real-world SSL or foundation model robustness, but to demonstrate a reproducible evaluation structure for representation-level poisoning and backdoor analysis.

### 12.5 키워드

| 구분 | 키워드 |
|---|---|
| 국문 | 자기지도학습, 표현학습, 파운데이션 모델, 데이터 오염, 백도어, ASR, 재현성 |
| 영문 | Self-Supervised Learning, Representation Learning, Foundation Model, Data Poisoning, Backdoor, Attack Success Rate, Reproducibility |

### 12.6 연구문제

- RQ1. 자기지도학습 기반 AI 시스템에서 poisoning/backdoor 평가를 위한 최소 지표는 무엇인가?
- RQ2. Trigger vector는 representation space의 mean shift와 attack success rate에 어떤 영향을 주는가?
- RQ3. Consistency defense check는 ASR after defense, detection rate, clean FPR을 어떻게 변화시키는가?

### 12.7 연구방법

문헌분석, 위협모형, synthetic 2D representation cluster 기반 모의실험, clean/poisoned/defense 지표 분리, 한계분석을 결합한다.

### 12.8 보안적 함의

Integrity, robustness, safety, accountability, governance, reproducibility 관점에서 pretraining corpus와 representation space를 보호 자산으로 관리해야 한다.

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
| 해외 참고문헌 5편 이상 | W05 기준 완료, P02/P03/P04 검증 필요 |
| AI 활용 고지 | 완료 |
| 실험 outputs 파일 존재 | 완료 |

## 13. SCI 논문 형식 전환

### 13.1 SCI 제목 후보

A Multi-Metric Evaluation Framework for Representation-Level Poisoning and Backdoor Threats in Self-Supervised Learning Systems

### 13.2 Structured Abstract

#### Background

Self-supervised learning and foundation models rely on large-scale pretraining data and learned representations, making the representation space itself a critical security asset.

#### Problem

Existing evaluations often report downstream clean accuracy without sufficiently separating representation shift, attack success rate, detection rate, clean false positive rate, and reproducibility evidence under poisoning and backdoor conditions.

#### Method

This study synthesizes five representative studies on self-supervised learning, recommendation-oriented SSL, video SSL, poisoning attacks, and backdoor attacks. A safe synthetic toy experiment is also used to illustrate separate reporting of clean representation baseline, poisoned/backdoor representation behavior, consistency-based defense check, and reproducibility evidence.

#### Results

The W05 toy experiment records clean representation accuracy, poisoned clean accuracy, attack success rate, mean representation shift, ASR after defense, trigger detection rate, and clean false positive rate. These results should not be interpreted as real-world SSL or foundation model security performance, but as an example of structured representation-level security reporting.

#### Contribution

The main contribution is a multi-metric evaluation structure that separates clean performance, poisoned performance, attack success rate, representation shift, defense effect, and reproducibility evidence.

#### Implications

The framework can be extended to later topics such as deepfake detection, LLM backdoors, federated learning poisoning, model stealing, watermarking, and MLOps data governance.

### 13.3 Introduction 구성

- SSL/foundation model에서 representation space가 보안 자산이 되는 이유
- Pretraining data와 augmentation pipeline의 공격면
- Clean accuracy 중심 평가의 한계
- ASR, representation shift, detection rate, clean FPR 분리 필요성
- 본 연구의 contribution

### 13.4 Related Work 축

**표 7. SCI Related Work 축**

| 연구축 | 대표 논문 | 역할 |
|---|---|---|
| Self-supervised learning | Gui et al. | SSL 알고리즘과 응용 taxonomy |
| SSL for recommendation 또는 general SSL | Ren et al. | SSL 응용 도메인 또는 일반 SSL survey, P02 검증 필요 |
| Video SSL | Schiappa et al. | temporal/cross-modal representation learning |
| Poisoning attacks | Wang et al. | training-time poisoning threat model |
| Backdoor attacks | Jin et al. | DNN-LLM backdoor attack/defense taxonomy |

### 13.5 Threat Model

- Target system: self-supervised representation learner, foundation model pretraining pipeline, downstream classifier
- Protected assets: pretraining corpus, augmentation pairs, learned representation, downstream classifier, trigger behavior, logs
- Adversary knowledge: black-box, gray-box, white-box, data contributor
- Adversary capability: poisoned sample insertion, trigger injection, augmentation manipulation, corpus contamination
- Attack success condition: source-class representation moves toward target class, ASR increases, clean accuracy remains high
- Defense/check: representation consistency distance threshold, trigger shift detection
- Excluded scope: real-world system compromise, personal data use, unauthorized model attack, operational backdoor deployment

### 13.6 Methodology

Literature matrix construction, SSL/backdoor threat model design, synthetic 2D representation experiment, clean representation baseline, poisoned/backdoor representation evaluation, consistency defense check, reproducibility evidence collection을 사용한다.

### 13.7 Experimental Setup

| Item | Description |
|---|---|
| Dataset | Synthetic 2D representation clusters |
| Model/checker | Nearest-centroid representation classifier |
| Baseline | Clean representation baseline |
| Security scenario | Trigger vector shifts source embeddings toward target centroid |
| Defense/check | Paired-view consistency distance threshold |
| Metrics | Clean accuracy, poisoned clean accuracy, ASR, ASR after defense, mean shift, detection rate, clean FPR |
| Environment | Ubuntu 24.04 / Docker / Python 3.11 |
| Seed | 42 |
| Output files | metrics_summary.csv, results.json, run_log.md |

### 13.8 Results

Outputs 기준 수치는 표 5와 같다. Clean representation baseline은 1.000000, poisoned clean accuracy는 1.000000, ASR은 1.000000, ASR after defense는 0.000000, mean shift는 각각 2.418677과 0.090597, detection rate는 1.000000, clean FPR은 0.000000이다.

### 13.9 Discussion

SSL에서는 라벨이 없어도 representation space가 공격 대상이 된다. Clean accuracy와 ASR은 반드시 분리해 보고해야 한다. Representation shift는 backdoor stealthiness와 detection 가능성을 설명하는 보조 지표가 될 수 있다. Consistency defense check는 toy 검증일 뿐 실제 SSL 방어 성능으로 일반화할 수 없다.

### 13.10 Limitations and Threats to Validity

- Internal validity: nearest-centroid classifier는 실제 SSL encoder나 foundation model의 학습 dynamics를 대표하지 않는다.
- External validity: synthetic 2D clusters는 실제 이미지, 비디오, 텍스트, 멀티모달 pretraining corpus를 대표하지 않는다.
- Construct validity: trigger vector와 representation shift는 평가축 설명용 toy metric이다.
- Reproducibility: outputs 파일과 보고서 수치의 일치가 필요하다.
- Literature validity: P02 강의계획서 지정 논문 동일 여부와 P03/P04 제목 차이 검증이 필요하다.

### 13.11 Conclusion

W05는 자기지도학습과 파운데이션 모델의 representation space를 poisoning/backdoor 평가의 중심 자산으로 설정한다. 핵심 결론은 clean accuracy, poisoned clean accuracy, ASR, representation shift, detection rate, clean FPR, reproducibility evidence를 분리해 기록해야 한다는 것이다. 이 구조는 후속 W06 생성모형, W07 LLM 보안, W10 연합학습, W13 모델 IP 보호로 확장될 수 있다.

## 14. 발표용 요약

발표 핵심 메시지는 “표현학습 기반 모델의 보안 평가는 clean 성능 하나로 끝나지 않으며, trigger 조건의 ASR, representation shift, defense check, 재현성 근거를 분리해야 한다”이다. 발표자료는 `09_presentation/presentation_slides.md`, `presentation_report.md`, `speaker_notes.md`, `qna.md`, `one_page_handout.md`에 정리했다.

## 15. 참고문헌 검증표

| 번호 | 참고문헌 | DOI/URL | 상태 |
|---|---|---|---|
| [1] | Jie Gui et al., A Survey on Self-Supervised Learning: Algorithms, Applications, and Future Trends | `10.1109/TPAMI.2024.3415112`, `10.48550/arXiv.2301.05712` | DOI 확인, 강의계획서 저자 표기 확인 필요 |
| [2] | Xubin Ren et al., A Comprehensive Survey on Self-Supervised Learning for Recommendation | `10.1145/3746280` | DOI 확인, 지정 일반 SSL survey 동일 여부 확인 필요 |
| [3] | Madeline C. Schiappa et al., Self-Supervised Learning for Videos: A Survey | `10.1145/3577925` | DOI 확인, 제목 차이/Article 번호 확인 필요 |
| [4] | Zhibo Wang et al., Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems | `10.1145/3538707` | DOI 확인, 강의계획서 제목/저자 차이 확인 필요 |
| [5] | Ling-Xin Jin et al., A survey of backdoor attacks and defences: From deep neural networks to large language models | `10.1016/j.jnlest.2025.100326` | DOI 확인, 강의계획서 `Z. Jin` 표기 확인 필요 |

PDF 원문은 `01_papers/pdf/`에 존재하고 Git 추적 중이다. public GitHub 저장소에는 PDF 원문 대신 DOI/URL, 서지정보, 요약만 남기는 것이 안전하며, 삭제 또는 추적 해제는 사용자 승인 후 수행한다.

## 16. 자기 점검표

| 점검 항목 | 상태 | 비고 |
|---|---|---|
| 1장 한 문장 요약 작성 | 완료 |  |
| 2장 학습 배경과 주차 목표 작성 | 완료 |  |
| AI 원리 70% 정리 | 완료 |  |
| 보안 이슈 30% 정리 | 완료 |  |
| 논문 5편 요약 | 완료 |  |
| 논문 5편 비교표 보완 | 완료 / 확인 필요 | P01-P05 차별성 반영, P02/P03/P04 확인 필요 |
| Research Track 5요소 작성 | 완료 | 연구문제, 위협모형, 평가방법, 재현성, 오픈문제 |
| P01 IEEE TPAMI DOI 검증 | 완료 | `10.1109/TPAMI.2024.3415112` |
| P02 지정 논문 동일 여부 검증 | 확인 필요 | 현재 로컬 PDF는 recommendation survey |
| P03 제목/출판정보 검증 | 완료 / 확인 필요 | DOI 확인, Article 번호 확인 필요 |
| P04 제목/출판정보 검증 | 완료 / 확인 필요 | DOI 확인, 강의계획서 표기 확인 필요 |
| P05 DOI/URL 검증 | 완료 / 확인 필요 | DOI 확인, 강의계획서 저자 표기 확인 필요 |
| 실험 outputs 파일 존재 확인 | 완료 | 3개 파일 존재 |
| 실험 결과와 보고서 수치 일치 | 완료 | outputs 기준 |
| KCI 논문 형식 전환 작성 | 완료 |  |
| SCI 논문 형식 전환 작성 | 완료 |  |
| 본문 인용과 참고문헌 대응 | 완료 / 확인 필요 | P02/P03/P04 검증 메모 유지 |
| 표·그림 번호 정리 | 완료 | 표 1-7, 그림 1 |
| AI 활용 고지 작성 | 완료 |  |
| PDF 저작권 위험 점검 | 완료 / 확인 필요 | PDF 5개 Git 추적 중, 삭제는 미수행 |
| 최종 사람이 검토할 항목 표시 | 완료 | 최종 제출 확정 아님 |
