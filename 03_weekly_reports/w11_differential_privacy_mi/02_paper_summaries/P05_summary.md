# P05 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 지정 논문 제목 | Defenses to Membership Inference Attacks: A Survey |
| 지정 논문 저자 | Hongsheng Hu et al. |
| 지정 논문 학술지 | ACM Computing Surveys 56(7), Article 144 |
| 지정 논문 DOI | `10.1145/3620667` |
| 로컬 PDF 제목 | Membership Inference Attacks and Defenses in Federated Learning: A Survey |
| 로컬 PDF 저자 | Li Bai, Haibo Hu, Qingqing Ye, Haoyang Li, Leixia Wang, Jianliang Xu |
| PDF 파일명 | `05_SUBSTITUTE_Bai_et_al_2024_MIA_Attacks_Defenses_FL_Survey.pdf` |
| 검증 상태 | 지정 논문과 로컬 PDF 불일치. 제출본에서는 대체 문헌으로 명시 |

## 2. 한 문장 요약

> 지정 논문은 MI 방어 전반의 survey로, 현재 로컬 대체 PDF는 federated learning에서 MI 공격/방어가 training phase와 client/server 역할에 따라 달라진다는 보완 관점을 제공한다.

## 3. 연구문제

MI 방어가 regularization, output restriction, calibration, DP, FL protocol defense 중 어디에 위치하며, 어떤 utility cost와 남은 leakage를 동반하는지 묻는다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Output restriction | confidence/logit 노출을 줄여 MI 신호를 약화 | 방어 설계 |
| Regularization | overfitting gap을 줄여 MI 위험을 완화 | 실험 비교 |
| Calibration | confidence 과신을 줄여 공격 신호를 줄임 | 평가 해석 |
| DP defense | 학습 단계에서 noise/accounting으로 보호 수준을 주장 | W11 실험 조건 |

## 5. 방법론

지정 논문은 MI defense taxonomy로 사용하고, 로컬 대체 PDF는 FL 환경에서 attacker/defender role과 attack phase가 중앙학습과 달라지는 사례로만 활용한다.

## 6. 주요 결과

방어는 MI risk를 낮출 수 있지만 성능 저하, 출력 유용성 감소, 계산 비용, 잘못된 privacy claim이라는 부작용을 함께 평가해야 한다.

## 7. 보안 관점 분석

P05는 W11의 utility-privacy trade-off를 설명하는 핵심 문헌이다. 방어를 적용했다는 사실보다 방어 전후의 MI attack accuracy, leakage score, clean accuracy, reproducibility가 함께 제시되어야 한다.

## 8. 한계와 오픈문제

현재 로컬 PDF는 FL 특화 대체 문헌이다. 지정 논문 원문을 확보하기 전까지 세부 분류와 DOI는 최종 확정하지 않는다.

## 9. 기말 논문에 반영할 부분

기말 논문 분석/실험 장에서 `방어 효과`를 단일 값이 아니라 `utility`, `MI risk`, `leakage`, `cost`, `accounting completeness`의 묶음으로 보고하는 근거로 사용한다.
