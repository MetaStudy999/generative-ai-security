# P05 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 지정 논문 제목 | Defenses to Membership Inference Attacks: A Survey |
| 지정 논문 저자 | 강의자료: Hongsheng Hu et al.; Crossref 공식 메타데이터: Li Hu, Anli Yan, Hongyang Yan, Jin Li, Teng Huang, Yingying Zhang, Changyu Dong, Chunsheng Yang |
| 지정 논문 학술지 | ACM Computing Surveys 56(4), pp. 1-34; online 2023-11-10, print 2024-04-30 |
| 지정 논문 DOI | `10.1145/3620667` |
| 로컬 PDF 제목 | Membership Inference Attacks and Defenses in Federated Learning: A Survey |
| 로컬 PDF 저자 | Li Bai, Haibo Hu, Qingqing Ye, Haoyang Li, Leixia Wang, Jianliang Xu |
| PDF 파일명 | `05_RELATED_Bai_et_al_2024_MIA_Attacks_Defenses_FL_Survey.pdf` |
| 검증 상태 | DOI `10.1145/3620667` 확인. 강의자료 저자명/권호 표기는 공식 메타데이터와 달라 최종 확인 필요. 로컬 PDF는 지정 논문과 표기 차이 |

## 2. 한 문장 요약

> 지정 논문은 MI 방어 전반의 survey로, 현재 로컬 관련 논문 PDF는 federated learning에서 MI 공격/방어가 training phase와 client/server 역할에 따라 달라진다는 보완 관점을 제공한다.

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

지정 논문은 MI defense taxonomy로 사용하고, 로컬 관련 논문 PDF는 FL 환경에서 attacker/defender role과 attack phase가 중앙학습과 달라지는 사례로만 활용한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | MI 방어 Utility-Privacy Trade-off |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$Tradeoff=(Utility_{base}-Utility_{def})+\lambda Adv_{MI}^{def}$$ |
| 기호·입력·출력 | \(Utility_{base}\): 방어 전 유용성, \(Utility_{def}\): 방어 후 유용성, \(Adv_{MI}^{def}\): 방어 후 MI advantage |
| 직관적 의미 | MI 방어 Utility-Privacy Trade-off는 Differential Privacy·Membership Inference 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Differential Privacy·Membership Inference 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | utility drop, MI advantage, calibration, epsilon 여부 |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

방어는 MI risk를 낮출 수 있지만 성능 저하, 출력 유용성 감소, 계산 비용, 잘못된 privacy claim이라는 부작용을 함께 평가해야 한다.

## 7. 보안 관점 분석

P05는 W11의 utility-privacy trade-off를 설명하는 핵심 문헌이다. 방어를 적용했다는 사실보다 방어 전후의 MI attack accuracy, leakage score, clean accuracy, reproducibility가 함께 제시되어야 한다.

## 8. 한계와 오픈문제

주의: W11의 P05는 지정 논문과 로컬 PDF가 표기 차이가 있다. 현재 로컬 PDF는 Bai et al.의 FL-MIA survey이므로, 최종 제출 전 `Defenses to Membership Inference Attacks: A Survey`의 지정 논문 원문 PDF 또는 공식 출판 페이지를 확보해야 한다. DOI `10.1145/3620667`은 확인되었으나 공식 메타데이터는 `Li Hu et al.` 및 ACM CSUR 56(4), pp. 1-34로 확인되어, 강의자료의 `Hongsheng Hu et al.` 표기는 최종 확인 필요 상태로 둔다.

## 9. 기말 논문에 반영할 부분

기말 논문 분석/실험 장에서 `방어 효과`를 단일 값이 아니라 `utility`, `MI risk`, `leakage`, `cost`, `accounting completeness`의 묶음으로 보고하는 근거로 사용한다.
