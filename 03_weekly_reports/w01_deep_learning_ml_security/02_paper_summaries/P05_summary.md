# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A Survey of Privacy Attacks in Machine Learning |
| 저자 | Maria Rigaki, Sebastian Garcia |
| 학술지/학회 | ACM Computing Surveys |
| 연도 | 2023 |
| DOI/URL | https://doi.org/10.1145/3624010 |
| PDF 파일명 | 05_Rigaki_Garcia_2023_Survey_of_Privacy_Attacks_in_ML.pdf |
| 검증 상태 | arXiv v3와 related DOI 확인 |

## 2. 한 문장 요약

> 이 논문은 ML 시스템에서 발생하는 프라이버시 공격을 공격자 지식, 공격 대상 자산, 누출 원인, 방어책으로 분류해 보안 평가에 privacy leakage 축을 추가한다.

## 3. 연구문제

핵심 질문은 “모델 학습과 추론 과정에서 어떤 정보가 새어 나가며, 공격자는 어떤 지식과 인터페이스를 이용해 이를 추론하는가”이다. W01에서는 프라이버시 공격을 대적 예제와 별개의 축으로 두되, 같은 ML 생명주기 안에서 평가한다.

## 4. 핵심 개념

| 개념 | 설명 | 보안 연구 연결 |
|---|---|---|
| Membership inference | 특정 샘플이 학습 데이터에 포함됐는지 추론한다. | 학습 데이터 프라이버시와 overfitting 평가 |
| Model inversion | 모델 출력이나 confidence를 이용해 입력 특성을 복원한다. | 민감 속성 및 원본 데이터 노출 위험 |
| Property inference | 학습 데이터 전체의 숨은 속성을 추론한다. | 집단 수준 민감정보 보호 |
| Adversarial knowledge | 공격자가 데이터, 모델, 출력, 학습 절차에 대해 아는 정도이다. | white/gray/black-box privacy threat model |

## 5. 방법론

privacy attack 문헌을 공격 대상 자산과 공격자 지식 수준에 따라 분류하고, 공격이 가능한 원인과 방어책을 비교한다. 본 보고서에서는 프라이버시 공격의 세부 구현 절차보다 평가 지표와 위협모형의 구조를 추출했다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Membership Inference Advantage |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$Adv_{MI}=\Pr[A(z)=1\mid z\in D_{train}]-\Pr[A(z)=1\mid z\notin D_{train}]$$ |
| 기호·입력·출력 | \(A\): membership 판별자, \(z\): 평가 샘플, \(D_{train}\): 학습 데이터 |
| 직관적 의미 | Membership Inference Advantage는 딥러닝·ML 보안 기본 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | 딥러닝·ML 보안 기본 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | membership inference risk, privacy leakage, utility drop |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

프라이버시 공격은 모델 파라미터, confidence score, decision output, 학습 데이터 분포 등 다양한 신호를 이용할 수 있다. 방어는 differential privacy, 출력 제한, regularization, confidence masking, auditing 등으로 나뉘지만, 유틸리티와 프라이버시 보호 사이의 trade-off가 지속된다.

## 7. 보안 관점 분석

P05는 W01의 CIA 관점 중 기밀성(confidentiality)에 직접 연결된다. 대적 공격이 주로 무결성·가용성 위협이라면, privacy attack은 모델이 정상 동작하더라도 데이터가 새어 나갈 수 있음을 보여준다. 따라서 보안 평가는 정확도와 robust accuracy만으로 끝나지 않고 leakage risk를 별도 축으로 둬야 한다.

## 8. 한계와 오픈문제

프라이버시 위험은 데이터 민감도, 출력 인터페이스, 모델 복잡도, 학습 방식에 따라 달라서 단일 지표로 요약하기 어렵다. 또한 differential privacy 같은 방어는 이론적 보증을 제공할 수 있지만 실제 시스템에서는 epsilon 설정, 데이터 전처리, 모델 성능 감소를 함께 설명해야 한다.

## 9. 기말 논문에 반영할 부분

기말 논문에서는 P05를 privacy threat model과 AI 활용 윤리 장의 핵심 문헌으로 사용한다. 특히 membership inference와 model inversion을 “실험으로 직접 수행할 수도 있지만, 악용 가능성이 있으므로 toy/public data와 방어 중심 평가로 제한한다”는 범위 설정에 반영한다.
