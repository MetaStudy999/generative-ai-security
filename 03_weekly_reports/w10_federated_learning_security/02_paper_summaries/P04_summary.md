# P04 Summary

## The Federation Strikes Back: A Survey of Federated Learning Privacy Attacks, Defenses, Applications, and Policy Landscape — Joshua C. Zhao et al., ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W10 Federated Learning Security |
| 논문명 | The Federation Strikes Back: A Survey of Federated Learning Privacy Attacks, Defenses, Applications, and Policy Landscape |
| 저자 | Joshua C. Zhao et al. |
| 출판 정보 | ACM Computing Surveys, 57(9), pp. 1–37, 2025 |
| DOI | https://doi.org/10.1145/3724113 |
| 검증 상태 | W10 `paper_list.md` 기준 DOI 확인. Article 번호 추가 대조 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 FL 프라이버시 공격과 방어를 **gradient leakage, membership inference, property inference, secure aggregation, differential privacy, applications, policy landscape** 관점에서 정리하며, W10에서 기술적 방어와 거버넌스 요구를 연결하는 핵심 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | FL은 원본 데이터를 공유하지 않아도 어떤 privacy attack에 취약한가? |
| RQ2 | Secure aggregation과 local/global DP는 어떤 보호와 한계를 갖는가? |
| RQ3 | Application domain과 policy landscape는 FL 보안 요구를 어떻게 바꾸는가? |
| RQ4 | 기말논문에서 FL privacy를 기술·정책·감사 관점으로 어떻게 통합할 수 있는가? |

---

## 3. 핵심 수식

### 3.1 Privacy Risk Score

$$
PrivacyRisk=w_1MI+w_2GI+w_3PI-w_4DefenseCoverage
$$

| 기호 | 의미 |
|---|---|
| $MI$ | membership inference 위험 |
| $GI$ | gradient inversion 위험 |
| $PI$ | property inference 위험 |
| $DefenseCoverage$ | secure aggregation/DP/정책 적용 범위 |

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | client update, gradient, participant identity, local data statistics |
| 공격자 목표 | membership inference, gradient reconstruction, property inference |
| 방어 | secure aggregation, DP, update clipping, access control, policy compliance |
| 지표 | leakage rate, MI advantage, utility drop, privacy budget, compliance evidence |

---

## 5. 기말논문 연결

P04는 FL privacy를 기술적 방어뿐 아니라 policy landscape와 연결한다. 기말논문에서는 분산 AI 시스템의 개인정보 보호 평가표와 감사 로그 설계 근거로 사용한다.

---

## 6. 최종 판단

P04는 W10의 privacy 핵심 문헌이다. P02/P03의 공격 taxonomy와 결합해 privacy-utility-governance 통합 평가축을 구성한다.
