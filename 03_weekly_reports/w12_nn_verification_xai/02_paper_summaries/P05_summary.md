# P05 논문 요약

## 1. 서지와 검증 상태

| 항목 | 내용 |
|---|---|
| 강의 지정 제목 | The Triangular Trade-off between Robustness, Accuracy, and Fairness |
| 강의 지정 저자 | Chih-Hsiang Cheng et al. |
| 공식 DOI 후보 | 확인 필요 |
| 유사 공식 후보 | `10.1145/3645088`, "Triangular Trade-off between Robustness, Accuracy, and Fairness in Deep Neural Networks: A Survey" |
| 유사 후보 메타데이터 | Jingyang Li and Guoqiang Li, ACM Computing Surveys, Vol. 57, Issue 6, Article 140, pp. 1-40, published 2025-02-10 |
| 강의 표기와 차이 | 저자, 제목, 연도, Article 정보가 지정 P05와 일치하지 않아 DOI 최종 확인 전 보류 |
| 로컬 PDF | `05_RELATED_Singh_et_al_2021_Accuracy_Fairness_Robustness_Study.pdf` |
| 로컬 PDF 상태 | Singh et al. 2021 multi-dimensional trustworthy ML study. 지정 논문 원문 아님 |

주의: W12의 P05는 지정 논문과 로컬 PDF가 표기 차이가 있다. 현재 로컬 PDF는 Singh et al. 2021 accuracy/fairness/robustness 관련 보조 문헌이므로, 최종 제출 전 Chih-Hsiang Cheng et al. 지정 논문 원문 PDF 또는 공식 출판 페이지를 확보해야 한다.

## 2. 핵심 연구문제

P05는 robustness, accuracy, fairness가 동시에 최적화되기 어려운 trade-off 관계를 다룬다[5]. 보안 평가에서는 robust accuracy만 높이는 것이 충분하지 않다. 방어가 clean accuracy를 낮추거나 fairness gap을 키우는 경우를 함께 보고해야 한다.

## 3. W12에서의 역할

| 관점 | 요약 |
|---|---|
| AI 원리 | multi-objective evaluation, robustness-accuracy-fairness trade-off |
| 보안 연결 | robust defense가 group별 성능 격차를 키울 가능성 |
| 평가 지표 | clean accuracy, robust accuracy, fairness gap |
| 한계 | 지정 P05 공식 DOI는 확인 필요. 로컬 PDF는 Singh 관련 보조 문헌 |
| 내 논문 활용 | multi-metric 보안 평가표의 근거 |

## 4. 실습 연결

W12 실험은 `Clean Accuracy`, `Robust Accuracy`, `Certified Rate`, `Explanation Stability`, `Fairness Gap`, `Verification Cost`를 함께 기록한다. 예를 들어 robust defense 조건은 clean accuracy가 0.815625이고 fairness gap이 0.044823으로 기록되어, 성능과 공정성 지표를 함께 봐야 함을 보여준다.

## 5. 최종 제출 전 확인 항목

- Chih-Hsiang Cheng et al. 지정 논문이 실제 ACM Computing Surveys에 존재하는지 재확인한다.
- 유사 후보 DOI `10.1145/3645088`을 P05로 확정하지 않는다.
- Singh PDF는 관련 보조 문헌으로만 관리한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Robustness-Accuracy-Fairness Trade-off |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$Objective=Acc-\lambda_1(1-Robust)-\lambda_2FairGap$$ |
| 기호·입력·출력 | \(Acc\): 정상 정확도, \(Robust\): robust metric, \(FairGap\): 집단 간 성능 격차 |
| 직관적 의미 | Robustness-Accuracy-Fairness Trade-off는 Verification·XAI·Robustness 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Verification·XAI·Robustness 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | clean accuracy, robust accuracy, fairness gap, calibration |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |


