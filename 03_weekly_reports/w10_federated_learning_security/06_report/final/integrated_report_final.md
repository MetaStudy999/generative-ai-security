# W10 연합학습(FL) & FL 위협·방어·정책 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W10 |
| 주제 | 연합학습(FL) & FL 위협·방어·정책 |
| 문서 상태 | 제출용 최종 초안, 사람 검토 필요 |
| 작성/보완일 | 2026-06-22, 2026-06-23 |
| 실험 근거 | `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md` |
| 안전 범위 | synthetic federated binary classification 기반 안전 toy 실험 |

## 1. 한 문장 요약

연합학습은 raw data를 중앙 서버로 보내지 않지만 local update와 aggregation 과정에서 privacy·integrity 위험이 남으므로, FL 보안 평가는 global accuracy만이 아니라 global F1, ASR, Privacy Leakage Proxy, aggregation type, communication bytes, reproducibility evidence를 함께 기록해야 한다[1][2].

## 2. 학습 배경과 주차 목표

### 2.1 이번 주 주제의 위치

W10은 W01-W09에서 다룬 AI 보안 평가축을 분산 학습 시스템으로 확장하는 주차다. W09가 보상 기반 자동 방어 에이전트를 다루었다면, W10은 여러 client가 local data로 학습한 update를 server가 aggregation하여 global model을 만드는 FL 구조를 다룬다. FL은 raw data를 중앙 서버로 보내지 않는 장점이 있지만, local update, aggregation rule, malicious client, privacy leakage, poisoning/backdoor 위험이 남는다. 따라서 clean accuracy, ASR, privacy leakage proxy, aggregation type, reproducibility evidence를 함께 기록해야 한다.

### 2.2 강의계획서상 학습목표

- Federated Learning, FedAvg, aggregation taxonomy, personalization, non-IID data를 정리한다.
- FL의 gradient leakage, membership inference, poisoning, model poisoning, backdoor 위협을 분류한다.
- Secure aggregation과 robust aggregation의 차이를 설명한다.
- Malicious client rate와 aggregation rule이 clean utility와 ASR에 미치는 영향을 평가한다.

### 2.3 이번 주 핵심 질문

1. FL은 raw data를 중앙화하지 않지만 왜 privacy와 integrity 위험이 남는가?
2. Malicious client 비율이 증가할 때 clean accuracy와 ASR은 어떻게 달라지는가?
3. FedAvg와 coordinate median은 poisoned update에 대해 어떤 차이를 보이는가?
4. Privacy Leakage Proxy는 실제 privacy attack과 어떤 차이가 있는가?
5. W10의 synthetic FL 실험을 KCI 또는 SCI 논문 주제로 발전시키려면 어떤 연구문제가 적절한가?

## 3. AI 원리 70% 정리

표 1. W10 핵심 개념과 보안 연결

| 개념 | AI 원리 | 보안 연결 |
|---|---|---|
| Federated Learning | client가 local data로 update를 학습하고 server가 global model을 갱신한다 | raw data 비공유만으로 privacy가 자동 보장되지는 않는다 |
| FedAvg | client update를 평균해 global model을 갱신한다 | 악성 update가 평균에 섞이면 model integrity가 흔들릴 수 있다 |
| Non-IID data | client별 데이터 분포가 다르다 | 정상 update와 악성 update 구분이 어려워질 수 있다 |
| Secure aggregation | 서버가 개별 update를 보지 못하게 한다 | confidentiality 강화, anomaly inspection 제약 가능 |
| Robust aggregation | 악성 또는 이상 update의 영향을 줄인다 | integrity 강화, 완전 방어는 아님 |

연합학습은 client의 local update를 server가 aggregation하여 global model을 갱신하는 분산 학습 구조다[1]. Secure aggregation은 개별 update의 노출을 줄이는 confidentiality 중심 방어이고, robust aggregation은 malicious update가 집계 결과에 미치는 영향을 낮추는 integrity 중심 방어다.

## 4. 보안 이슈 30% 정리

FL은 raw data를 중앙 서버로 보내지 않지만 poisoning, inference attack, privacy leakage와 같은 보안·프라이버시 위험이 남는다[2]. W10의 핵심 보안 이슈는 gradient leakage, membership inference, data/model poisoning, backdoor, malicious client, update integrity, privacy policy다. 실제 개인정보, 실제 FL 서비스 침해, 무단 클라이언트 접속, 실제 공격 payload, 실제 gradient inversion, 실제 membership inference 공격 절차는 본 주차 범위에서 제외한다.

## 5. 논문 5편 요약

표 2. 관련 문헌 5편 요약

| ID | 논문 | 핵심 역할 | DOI/URL 상태 |
|---|---|---|---|
| P01 | Arbaoui et al., Federated Learning Survey | aggregation taxonomy와 FL 원리 | DOI 10.1145/3678182 확인. 수업자료 CSUR 표기와 공식 TIST 표기 차이 있음 |
| P02 | Mothukuri et al., A survey on security and privacy of federated learning | FL security/privacy threat taxonomy | DOI 10.1016/j.future.2020.10.007 확인 |
| P03 | Rodriguez-Barroso et al., Survey on federated learning threats | attack-defense taxonomy와 experimental challenge | DOI 10.1016/j.inffus.2022.09.011, arXiv:2201.08135 확인 |
| P04 | Zhao et al., The Federation Strikes Back | privacy attack, defense, application, policy landscape | DOI 10.1145/3724113 확인. Article 번호 추가 확인 필요 |
| P05 | Nguyen et al., Backdoor attacks and defenses in federated learning | FL backdoor와 ASR 평가 | DOI 10.1016/j.engappai.2023.107166, arXiv:2303.02213 확인 |

FL threat taxonomy는 공격과 방어를 client, server, aggregation, privacy 관점에서 분류한다[3]. FL privacy attack과 policy landscape는 기술적 방어뿐 아니라 적용 도메인과 규제 환경을 함께 고려해야 함을 보여준다[4]. FL backdoor 연구는 clean accuracy가 유지되어도 ASR이 상승할 수 있음을 보여준다[5].

## 6. 논문 5편 비교표

| 논문 | 차별성 | W10 활용 |
|---|---|---|
| P01 | aggregation taxonomy와 FL 원리 중심 | FedAvg와 coordinate median 비교 축 |
| P02 | FL security/privacy 위험 전반 | confidentiality, integrity, privacy 분류 |
| P03 | 공격-방어 taxonomy와 실험 과제 | malicious client rate와 defense 지표 설계 |
| P04 | privacy attack, application, policy landscape | Privacy Leakage Proxy와 정책 함의 |
| P05 | backdoor 공격·방어 특화 | ASR와 clean accuracy 동시 평가 |

P01은 aggregation taxonomy와 AI 원리 문헌이고, P02/P03은 FL security/privacy와 attack-defense taxonomy 문헌이다. P04는 FL privacy attack과 policy landscape 문헌이며, P05는 FL backdoor 공격·방어 특화 문헌이다.

## 7. Research Track 분석

표 3. W10 Research Track 요약

| 요소 | 내용 |
|---|---|
| 연구문제 | malicious client 비율과 aggregation rule이 clean utility와 ASR에 미치는 영향 |
| 대상 시스템 | FL 기반 분산 학습 시스템 |
| 보호 자산 | client data, local update, global model, aggregation result, training log |
| 위협 | poisoning, model poisoning, backdoor, privacy leakage |
| 평가 지표 | Global Accuracy, Global F1, ASR, Privacy Leakage Proxy, Mean Update Norm, Communication Bytes |
| 재현성 근거 | seed, config, code, metrics_summary.csv, results.json, run_log.md |

## 8. 실습 보고서

표 4. W10 실습 설계

| 항목 | 내용 |
|---|---|
| Dataset | Synthetic federated binary classification |
| Clients | 10 |
| Samples per client | 80 |
| Test samples | 600 |
| Non-IID skew | 0.70 |
| Model | Toy logistic regression |
| Rounds | 25 |
| Local epochs | 3 |
| Aggregation | FedAvg, coordinate median |
| Conditions | Clean FL, poisoned FL 10%, poisoned FL 20%, robust aggregation 20% |
| Seed | 42 |

표 5. W10 실습 결과

| 조건 | Malicious Client Rate | Aggregation | Global Accuracy | Global F1 | ASR | Privacy Leakage Proxy | Mean Update Norm | Communication Bytes |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| Clean FL | 0% | fedavg | 0.960000 | 0.958042 | 0.136076 | 0.442597 | 0.637927 | 12000 |
| Poisoned FL 10% | 10% | fedavg | 0.953333 | 0.951557 | 0.297468 | 0.428377 | 0.839220 | 12000 |
| Poisoned FL 20% | 20% | fedavg | 0.950000 | 0.948630 | 0.496835 | 0.486591 | 1.024448 | 12000 |
| Robust aggregation 20% | 20% | coordinate_median | 0.955000 | 0.953368 | 0.237342 | 0.439875 | 0.929979 | 12000 |

20% poisoned FedAvg는 clean accuracy 0.950000을 유지했지만 ASR 0.496835를 보였다. 같은 20% 조건에서 coordinate median은 ASR을 0.237342로 낮췄다. 단, 이 결과는 synthetic federated binary classification 기반 toy 실험의 평가 형식 검증용 수치이며, 실제 FL framework, 실제 secure aggregation, differential privacy, gradient inversion, membership inference, 실제 서비스 보안성으로 일반화하지 않는다.

그림 1. 연합학습 보안 평가 흐름

```text
Client Local Data
        ↓
Local Training / Local Update
        ↓
Aggregation Server
        ↓
FedAvg or Coordinate Median
        ↓
Global Model
        ↓
Clean Evaluation --> Global Accuracy, Global F1
        ↓
Triggered Evaluation --> ASR
        ↓
Update Exposure Check --> Privacy Leakage Proxy
        ↓
Reproducibility Evidence --> seed, config, outputs, run_log
```

Privacy Leakage Proxy는 실제 gradient inversion 또는 membership inference 성공률이 아니라 update norm 기반 대용 지표다. W10 toy 실험은 실제 FL framework, secure aggregation, DP, gradient inversion을 구현하지 않은 synthetic logistic regression 실험이다.

## 9. AI 도구 활용 기록

Codex를 사용해 공통 지침 확인, W10 프롬프트 확인, 로컬 PDF 메타데이터 대조, DOI/arXiv/Crossref 기반 서지정보 확인 보조, synthetic toy 실험 코드 작성·실행, 결과 로그 기반 보고서·제출본·발표자료 작성을 수행했다. AI 산출물은 초안으로 취급하며, 최종 제출 전 사람이 인용·수치·저작권·연구윤리 책임을 확인해야 한다.

## 10. 토론 질문

1. FL에서 secure aggregation과 robust aggregation은 서로 보완적인가, 운영상 충돌하는가?
2. Clean accuracy가 유지되는 backdoor 위험을 운영 환경에서 어떻게 발견할 수 있는가?
3. Privacy Leakage Proxy를 실제 privacy attack 평가로 확장하려면 어떤 안전·윤리 조건이 필요한가?
4. Public GitHub 저장소에서 논문 PDF 원문을 관리할 때 어떤 저작권 정책이 필요한가?

## 11. 기말논문 연결

W10는 기말 논문의 관련연구, 위협모형, 평가방법, 보안적 함의 장에 연결된다. 특히 "AI 보안 평가는 일반 성능, 공격 성공률, 프라이버시 노출, 재현성 로그를 동시에 요구한다"는 주장에 활용할 수 있다. 단, W10 결과는 toy protocol이므로 기말논문에서 실제 FL 보안 성능 근거로 과장하지 않는다.

## 12. KCI 논문 형식 전환

### 12.1 KCI형 제목 후보

표 6. KCI 논문 제목 후보

| 번호 | 국문 제목 후보 | 영문 제목 후보 | 대상 시스템 | 보안 위협 | 연구방법 | 예상 기여 |
|---:|---|---|---|---|---|---|
| 1 | 연합학습 환경에서 악성 클라이언트 비율과 집계 방식이 Backdoor ASR에 미치는 영향 분석 | An Analysis of the Impact of Malicious Client Rate and Aggregation Rule on Backdoor ASR in Federated Learning | FL 시스템 | malicious client, backdoor, poisoned update | 문헌분석 + synthetic FL 실험 | clean accuracy와 ASR 분리 평가 |
| 2 | 연합학습 보안 평가를 위한 Utility·ASR·Privacy Leakage·재현성 통합 프레임워크 연구 | A Unified Evaluation Framework for Utility, ASR, Privacy Leakage, and Reproducibility in Federated Learning Security | FL 기반 분산 학습 | gradient leakage, poisoning, backdoor | toy experiment + 체크리스트 | 다중지표 평가표 |
| 3 | FedAvg와 Coordinate Median 기반 연합학습 Robust Aggregation의 보안성 비교 연구 | A Comparative Study of FedAvg and Coordinate Median Robust Aggregation in Federated Learning Security | FL aggregation | model poisoning, backdoor | synthetic logistic regression | aggregation rule별 ASR 비교 |

### 12.2 추천 최종 제목

- 국문: 연합학습 환경에서 악성 클라이언트 비율과 집계 방식이 Backdoor ASR에 미치는 영향 분석
- 영문: An Analysis of the Impact of Malicious Client Rate and Aggregation Rule on Backdoor ASR in Federated Learning

### 12.3 국문초록 초안

본 연구는 연합학습 환경에서 악성 클라이언트 비율과 집계 방식이 global utility와 backdoor attack success rate에 미치는 영향을 평가하기 위한 다중지표 프레임워크를 제안한다. 선행연구 비교를 통해 global accuracy, global F1, attack success rate, privacy leakage proxy, mean update norm, communication bytes, reproducibility evidence의 평가축을 도출한다. 또한 실제 개인정보나 실제 FL 서비스를 사용하지 않고 synthetic federated binary classification 기반 toy logistic regression 실험을 수행하여 clean FL, poisoned FL 10%, poisoned FL 20%, robust aggregation 20% 조건을 비교한다. 본 연구는 실제 FL 보안 성능을 주장하지 않고, FL 보안 평가에서 clean utility와 backdoor ASR을 분리해 기록해야 함을 보이는 데 목적이 있다.

### 12.4 키워드와 점검표

| 구분 | 키워드 |
|---|---|
| 국문 | 연합학습, FedAvg, Robust Aggregation, 악성 클라이언트, Backdoor, ASR, Privacy Leakage |
| 영문 | Federated Learning, FedAvg, Robust Aggregation, Malicious Client, Backdoor, Attack Success Rate, Privacy Leakage |

| 점검 항목 | 상태 |
|---|---|
| 국문·영문 제목 후보 | 완료 |
| 국문초록 초안 | 완료 |
| 연구문제·연구방법 | 완료 |
| 국내 참고문헌 3편 이상 | 확인 필요 |
| AI 활용 고지 | 완료, 사람 검토 필요 |
| PDF 저작권 상태 | 확인 필요, PDF 추적 중 |

## 13. SCI 논문 형식 전환

### 13.1 SCI 제목 후보

A Multi-Metric Evaluation Framework for Backdoor Robustness and Privacy Exposure in Federated Learning Under Malicious Client Participation

### 13.2 Structured Abstract

#### Background

Federated learning enables distributed model training without centralizing raw client data, but privacy and integrity risks remain in local updates, aggregation, and global model behavior.

#### Problem

Clean accuracy alone may hide backdoor risks in federated learning. Malicious clients can submit poisoned updates that preserve global utility while increasing attack success rate. At the same time, update statistics may expose privacy-relevant signals.

#### Method

This study synthesizes five representative studies on federated learning aggregation, FL security and privacy, FL threat taxonomy, privacy attacks and policy landscape, and FL backdoor attacks. A safe synthetic toy experiment is used to compare clean FedAvg, poisoned FedAvg under 10% and 20% malicious clients, and coordinate-median robust aggregation under 20% malicious clients.

#### Results

The W10 toy experiment shows that clean accuracy can remain high under poisoned FedAvg while ASR increases substantially. Coordinate median reduces ASR compared with FedAvg under the same malicious client rate, but does not eliminate backdoor risk. These results should not be interpreted as real-world FL security performance.

#### Contribution

The main contribution is a multi-metric evaluation structure that separates global accuracy, global F1, ASR, privacy leakage proxy, aggregation rule, communication cost, and reproducibility evidence.

#### Implications

The framework can be extended to secure aggregation, differential privacy, gradient inversion evaluation, non-IID benchmark studies, MLOps federated model governance, and privacy-preserving distributed AI systems.

### 13.3 SCI 구성 초안

표 7. SCI Related Work 축

| 연구축 | 대표 논문 | 역할 |
|---|---|---|
| FL aggregation taxonomy | Arbaoui et al. | FedAvg, aggregation, personalization, heterogeneity |
| FL security and privacy | Mothukuri et al. | poisoning, inference, privacy risk taxonomy |
| FL threats and defenses | Rodriguez-Barroso et al. | attack-defense mapping and experimental challenges |
| FL privacy and policy | Zhao et al. | privacy attacks, defenses, applications, policy landscape |
| FL backdoor attacks | Nguyen et al. | backdoor ASR, malicious clients, defense challenges |

SCI 논문은 Introduction, Related Work, Threat Model, Methodology, Experimental Setup, Results, Discussion, Limitations and Threats to Validity, Conclusion 순서로 확장할 수 있다. Threat model은 actual FL service compromise, personal data use, live client intrusion, real gradient inversion, real membership inference를 제외해야 한다.

## 14. 발표용 요약

- 핵심 메시지: FL 보안 평가는 clean accuracy만으로 충분하지 않다.
- 핵심 그림: Client Local Data -> Local Update -> Aggregation Server -> Global Model -> Clean/Triggered/Exposure/Reproducibility evaluation.
- 핵심 수치: 20% poisoned FedAvg는 ASR 0.496835, coordinate median 20%는 ASR 0.237342.
- 주의 문장: 이 수치는 synthetic toy protocol의 평가 형식 검증 결과이며 실제 FL 제품 공격 성공률이나 방어 보증이 아니다.

## 15. 참고문헌 검증표

| 번호 | 참고문헌 | DOI/URL | 상태 |
|---|---|---|---|
| [1] | Arbaoui, M., Brahmia, M.-E.-A., Rahmoun, A., and Zghal, M. Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights, and Future Frontiers. ACM Transactions on Intelligent Systems and Technology, 15(6), 1-69, 2024. | https://doi.org/10.1145/3678182 | 확인. 수업자료 CSUR 표기 차이 있음 |
| [2] | Mothukuri, V., Parizi, R. M., Pouriyeh, S., Huang, Y., Dehghantanha, A., and Srivastava, G. A survey on security and privacy of federated learning. Future Generation Computer Systems, 115, 619-640, 2021. | https://doi.org/10.1016/j.future.2020.10.007 | 확인 |
| [3] | Rodriguez-Barroso, N., Jimenez-Lopez, D., Luzon, M. V., Herrera, F., and Martinez-Camara, E. Survey on federated learning threats: Concepts, taxonomy on attacks and defences, experimental study and challenges. Information Fusion, 90, 148-173, 2023. | https://doi.org/10.1016/j.inffus.2022.09.011; https://arxiv.org/abs/2201.08135 | 확인 |
| [4] | Zhao, J. C. et al. The Federation Strikes Back: A Survey of Federated Learning Privacy Attacks, Defenses, Applications, and Policy Landscape. ACM Computing Surveys, 57(9), 1-37, 2025. | https://doi.org/10.1145/3724113 | 확인. Article 번호 추가 확인 필요 |
| [5] | Nguyen, T. D., Nguyen, T., Nguyen, P. L., Pham, H. H., Doan, K. D., and Wong, K.-S. Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions. Engineering Applications of Artificial Intelligence, 127, Article 107166, 2024. | https://doi.org/10.1016/j.engappai.2023.107166; https://arxiv.org/abs/2303.02213 | 확인 |

## 16. 자기 점검표

| 점검 항목 | 상태 | 비고 |
|---|---|---|
| 1장 한 문장 요약 작성 | 완료 |  |
| 2장 학습 배경과 주차 목표 작성 | 완료 |  |
| AI 원리 70% 정리 | 완료 |  |
| 보안 이슈 30% 정리 | 완료 |  |
| 논문 5편 요약 | 완료 |  |
| 논문 5편 비교표 보완 | 완료 | P01/P04 Article 표기 추가 검토 |
| Research Track 5요소 작성 | 완료 | 연구문제, 위협모형, 평가방법, 재현성, 오픈문제 |
| P01 DOI/URL 검증 | 완료 / 확인 필요 | DOI 확인, 수업자료 CSUR 표기 차이 사람 확인 필요 |
| P02 DOI/URL 검증 | 완료 |  |
| P03 출판 DOI 검증 | 완료 | arXiv와 Information Fusion DOI 확인 |
| P04 DOI/URL 검증 | 완료 / 확인 필요 | DOI 확인, Article 번호 확인 필요 |
| P05 출판 DOI 검증 | 완료 | arXiv와 EAAI DOI 확인 |
| 실험 outputs 파일 존재 확인 | 완료 | CSV/JSON/run_log 존재 |
| 실험 결과와 보고서 수치 일치 | 완료 | outputs 기준 |
| KCI 논문 형식 전환 작성 | 완료 | 초안 |
| SCI 논문 형식 전환 작성 | 완료 | 초안 |
| 본문 인용과 참고문헌 대응 | 완료 | [1]-[5] 대응 |
| 표·그림 번호 정리 | 완료 | 표 1-7, 그림 1 |
| AI 활용 고지 작성 | 완료 | `05_ai_worklog/ai_disclosure_draft.md` |
| PDF 저작권 위험 점검 | 완료 / 확인 필요 | PDF tracked 상태, 삭제는 미수행 |
| Docker/pyproject/config/code 정합성 점검 | 완료 | pyproject 의존성 `pyyaml`로 최소화. 로컬 실행, Docker build, docker compose run 확인 |
| 최종 사람이 검토할 항목 표시 | 완료 | 제출 확정 아님 |
