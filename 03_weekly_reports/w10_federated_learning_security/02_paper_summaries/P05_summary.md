# P05 Summary

## Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions — Thuy Dung Nguyen et al., Engineering Applications of Artificial Intelligence, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W10 Federated Learning Security |
| 논문명 | Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions |
| 저자 | Thuy Dung Nguyen et al. |
| 출판 정보 | Engineering Applications of Artificial Intelligence, 127, Article 107166, 2024 |
| DOI | https://doi.org/10.1016/j.engappai.2023.107166 |
| 보조 URL | https://arxiv.org/abs/2303.02213 |
| 검증 상태 | W10 `paper_list.md` 기준 arXiv 및 출판 DOI 확인 |

---

## 1. 한 문장 요약

이 논문은 federated learning의 backdoor 공격과 방어를 **malicious client, model replacement, trigger, aggregation bypass, clean accuracy 유지, ASR, robust aggregation, anomaly detection** 관점에서 정리하는 W10의 핵심 backdoor 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | FL backdoor는 중앙집중 backdoor와 어떤 점이 다른가? |
| RQ2 | 악성 client update는 aggregation을 통해 어떻게 global model에 trigger behavior를 삽입하는가? |
| RQ3 | Clean accuracy와 ASR을 분리해 평가해야 하는 이유는 무엇인가? |
| RQ4 | robust aggregation, anomaly detection, client reputation은 어떤 방어 효과와 한계를 갖는가? |

---

## 3. 핵심 수식

### 3.1 FL Backdoor ASR

$$
ASR=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[f_{w}(T(x_i))=y_t]
$$

### 3.2 Malicious Client Ratio

$$
MalClientRate=\frac{K_{mal}}{K_{total}}
$$

**보안 해석:** FL backdoor는 전체 clean accuracy를 유지하면서 특정 trigger에서만 목표 행동을 만들 수 있다. 악성 client 비율과 aggregation 정책을 함께 기록해야 한다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | global model, client update, aggregation process, trigger test set |
| 공격자 목표 | trigger 조건에서 target label 유도, clean 성능 유지, 방어 우회 |
| 공격자 능력 | malicious client 참여, local data poisoning, update scaling, model replacement |
| 지표 | clean accuracy, ASR, malicious client rate, detection rate, FPR, utility drop |
| 재현성 | malicious client id, trigger pattern, aggregation rule, round log 기록 |

---

## 5. 기말논문 연결

P05는 FL backdoor 평가의 직접 핵심 문헌이다. 기말논문에서는 분산 참여자가 있는 학습·검색·문서 업데이트 환경에서 hidden behavior와 악성 기여자를 탐지하는 평가표로 확장한다.

---

## 6. 최종 판단

P05는 W10의 backdoor 핵심 문헌이다. FL 보안 평가는 clean accuracy만으로 부족하고 ASR·client provenance·aggregation audit를 함께 봐야 한다.
