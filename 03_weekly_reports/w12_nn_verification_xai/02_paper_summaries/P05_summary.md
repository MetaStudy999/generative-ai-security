# P05 논문 요약

## 1. 서지와 검증 상태

| 항목 | 내용 |
|---|---|
| 강의 지정 제목 | The Triangular Trade-off between Robustness, Accuracy, and Fairness |
| 강의 지정 저자 | Chih-Hsiang Cheng et al. |
| 공식 DOI 후보 | 확인 필요 |
| 유사 공식 후보 | `10.1145/3645088`, "Triangular Trade-off between Robustness, Accuracy, and Fairness in Deep Neural Networks: A Survey" |
| 유사 후보 메타데이터 | Jingyang Li and Guoqiang Li, ACM Computing Surveys, Vol. 57, Issue 6, Article 140, pp. 1-40, published 2025-02-10 |
| 강의 표기와 차이 | 저자, 제목, 연도, Article 정보가 지정 P05와 일치하지 않아 DOI 확정 금지 |
| 로컬 PDF | `05_SUBSTITUTE_Singh_et_al_2021_Accuracy_Fairness_Robustness_Study.pdf` |
| 로컬 PDF 상태 | Singh et al. 2021 multi-dimensional trustworthy ML study. 지정 논문 원문 아님 |

주의: W12의 P05는 지정 논문과 로컬 PDF가 불일치한다. 현재 로컬 PDF는 Singh et al. 2021 accuracy/fairness/robustness 관련 대체 문헌이므로, 최종 제출 전 Chih-Hsiang Cheng et al. 지정 논문 원문 PDF 또는 공식 출판 페이지를 확보해야 한다.

## 2. 핵심 연구문제

P05는 robustness, accuracy, fairness가 동시에 최적화되기 어려운 trade-off 관계를 다룬다[5]. 보안 평가에서는 robust accuracy만 높이는 것이 충분하지 않다. 방어가 clean accuracy를 낮추거나 fairness gap을 키우는 경우를 함께 보고해야 한다.

## 3. W12에서의 역할

| 관점 | 요약 |
|---|---|
| AI 원리 | multi-objective evaluation, robustness-accuracy-fairness trade-off |
| 보안 연결 | robust defense가 group별 성능 격차를 키울 가능성 |
| 평가 지표 | clean accuracy, robust accuracy, fairness gap |
| 한계 | 지정 P05 공식 DOI는 확인 필요. 로컬 PDF는 Singh 대체 문헌 |
| 내 논문 활용 | multi-metric 보안 평가표의 근거 |

## 4. 실습 연결

W12 실험은 `Clean Accuracy`, `Robust Accuracy`, `Certified Rate`, `Explanation Stability`, `Fairness Gap`, `Verification Cost`를 함께 기록한다. 예를 들어 robust defense 조건은 clean accuracy가 0.815625이고 fairness gap이 0.044823으로 기록되어, 성능과 공정성 지표를 함께 봐야 함을 보여준다.

## 5. 최종 제출 전 확인 항목

- Chih-Hsiang Cheng et al. 지정 논문이 실제 ACM Computing Surveys에 존재하는지 재확인한다.
- 유사 후보 DOI `10.1145/3645088`을 P05로 확정하지 않는다.
- Singh PDF는 대체 문헌으로만 관리한다.
