# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Explainable Artificial Intelligence (XAI): Concepts, Taxonomies, Opportunities and Challenges toward Responsible AI |
| 저자 | Alejandro Barredo Arrieta, Natalia Díaz-Rodríguez, Javier Del Ser, Adrien Bennetot, Siham Tabik, Alberto Barbado, Salvador Garcia, Sergio Gil-Lopez, Daniel Molina, Richard Benjamins, Raja Chatila, Francisco Herrera |
| 학술지/학회 | Information Fusion 58, 82-115 |
| 연도 | 2020 |
| DOI/URL | `https://doi.org/10.1016/j.inffus.2019.12.012` |
| PDF 파일명 | `04_Arrieta_et_al_2020_Explainable_AI_Concepts_Taxonomies.pdf` |
| 검증 상태 | ScienceDirect article page와 DOI/Crossref metadata에서 Information Fusion 58, 82-115 확인. 로컬 PDF는 arXiv preprint |

## 2. 한 문장 요약

> 이 논문은 XAI의 개념, taxonomy, 책임 있는 AI와의 관계를 체계화하며, 설명가능성이 보안·프라이버시·공정성·책임성 문제와 동시에 연결된다는 점을 보여준다.

## 3. 연구문제

black-box ML 모델을 실제 조직과 안전중요 도메인에 배포하려면 어떤 수준의 설명가능성, 투명성, 공정성, 책임성이 필요한가가 핵심 질문이다. 기말논문에서는 XAI를 단순한 시각화가 아니라 연구 책임성과 보안 평가의 한 축으로 다룬다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Interpretability | 모델 또는 의사결정 과정을 사람이 이해할 수 있는 정도 | XAI 평가 기준 |
| Transparency | 모델 자체가 이해 가능한 구조인지 여부 | 설명 방식 분류 |
| Post-hoc explanation | 학습된 black-box 모델의 결정을 사후 설명 | explanation misuse 위험 |
| Responsible AI | fairness, accountability, privacy, explainability를 함께 요구하는 접근 | 보안적 함의 |

## 5. 방법론

약 400개 XAI 기여를 검토하고, transparent model과 post-hoc explanation, deep learning explanation taxonomy를 정리한다. 또한 Responsible AI 관점에서 XAI의 사회적·윤리적 역할을 논의한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Explanation Stability |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$Stability=1-\frac{\lVert A(x)-A(x_{alt})\rVert_2}{\lVert x-x_{alt}\rVert_2+\epsilon_0}$$ |
| 기호·입력·출력 | \(A(x)\): 설명 벡터, \(x_{alt}\): 작은 변형 입력, \(\epsilon_0\): 0 나눗셈 방지 상수 |
| 직관적 의미 | Explanation Stability는 Reproducibility·XAI 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Reproducibility·XAI 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | stability, fidelity, robustness, user trust score |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

설명가능성은 모델의 신뢰를 높일 수 있지만, 설명의 대상 audience와 목적을 명확히 하지 않으면 잘못된 신뢰를 만들 수 있다. XAI는 privacy, confidentiality, robustness, fairness와 충돌하거나 보완될 수 있으므로 평가 프로토콜에 함께 포함해야 한다.

## 7. 보안 관점 분석

XAI는 adversarial perturbation, bias, spurious correlation을 발견하는 데 도움을 주지만, 동시에 모델 내부 단서나 민감정보를 노출할 수 있다. 따라서 설명을 공개할 범위, 설명 로그 보관, human review 절차가 필요하다.

## 8. 한계와 오픈문제

논문은 2020년 기준 taxonomy라 LLM/RAG 및 최신 agent 기반 시스템의 설명 문제는 별도 보완이 필요하다. 또한 설명 품질을 계량화하는 공통 지표는 아직 합의가 제한적이다.

## 9. 기말 논문에 반영할 부분

보안적 함의 장에서 XAI를 privacy, fairness, accountability와 함께 다루고, explanation stability와 disclosure scope를 평가 항목에 포함하는 근거로 활용한다.
