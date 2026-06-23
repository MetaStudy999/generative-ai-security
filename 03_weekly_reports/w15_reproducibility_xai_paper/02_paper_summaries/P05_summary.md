# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Concept-based Explainable Artificial Intelligence: A Survey |
| 저자 | Eleonora Poeta, Gabriele Ciravegna, Eliana Pastor, Tania Cerquitelli, Elena Baralis |
| 학술지/학회 | arXiv preprint / ACM Computing Surveys online publication |
| 연도 | arXiv 2023, ACM online publication 2025 |
| DOI/URL | `https://doi.org/10.1145/3774643`, `https://arxiv.org/abs/2312.12936` |
| PDF 파일명 | `05_Poeta_et_al_2025_Concept_Based_XAI_Survey.pdf` |
| 검증 상태 | 로컬 PDF 첫 페이지의 arXiv identifier와 arXiv/Crossref metadata에서 최종 DOI 확인. 권호/issue는 ACM 페이지에서 최종 재확인 필요 |

## 2. 한 문장 요약

> 이 논문은 feature-level 설명의 한계를 보완하기 위해 concept-based XAI 방법을 정의·분류하고, 개념 기반 설명의 평가 지표와 활용 지침을 제시한다.

## 3. 연구문제

사람이 이해 가능한 concept를 모델 설명의 기본 단위로 사용할 때 어떤 concept 유형, 설명 유형, 학습 방식, 평가 지표가 필요한가가 핵심 질문이다. 기말논문에서는 XAI 설명을 보안 평가 증거로 사용할 때 concept-level 안정성과 정보노출 위험을 함께 점검한다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Concept | 색, 객체, 속성, 텍스트 개념처럼 사람이 해석 가능한 추상화 | human review |
| C-XAI | concept를 이용해 모델 결정이나 내부 표현을 설명하는 방법 | XAI 평가축 |
| Concept bottleneck | concept layer를 통해 예측을 구성하는 explainable-by-design 접근 | 설명-성능 trade-off |
| Concept intervention | concept 값을 수정해 예측 변화를 확인하는 평가 방식 | 안정성·안전성 분석 |

## 5. 방법론

Concept-based XAI 문헌을 정리해 concept 유형, explanation 유형, post-hoc/설계기반 접근, taxonomy, 평가 지표, human evaluation, dataset 사용을 비교한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Concept Completeness Proxy |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$Completeness=Acc(f)-Acc(f_{without\ concepts})$$ |
| 기호·입력·출력 | \(f\): 전체 모델, \(f_{without\ concepts}\): concept 정보를 제거한 비교 모델 |
| 직관적 의미 | Concept Completeness Proxy는 Reproducibility·XAI 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Reproducibility·XAI 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | concept completeness, stability, human agreement, robustness |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 참고만 |

## 6. 주요 결과

Concept-based explanation은 pixel/feature 수준보다 사용자 이해에 가까운 설명을 제공할 수 있다. 하지만 concept 정의, annotation, concept completeness, concept leakage, human evaluation 비용이 중요한 한계로 남는다.

## 7. 보안 관점 분석

Concept는 설명을 쉽게 만들지만, 공격자가 어떤 concept가 의사결정에 중요한지 알면 우회나 조작에 활용할 수 있다. 반대로 concept drift와 spurious concept를 탐지하면 모델 오동작과 편향을 조기에 발견할 수 있다.

## 8. 한계와 오픈문제

로컬 PDF는 arXiv preprint 기준이며 최종 DOI는 `10.1145/3774643`으로 확인했다. 다만 권호/issue와 최종 formatted PDF는 ACM 페이지에서 사람이 재확인해야 한다. Concept annotation과 human evaluation은 비용이 크고, 보안 도메인에서는 concept 공개 범위가 민감할 수 있다.

## 9. 기말 논문에 반영할 부분

기말논문의 XAI 평가 항목에 explanation stability, concept completeness, disclosure risk를 포함하는 근거로 활용한다. 본문 인용번호 `[5]`에는 권호/issue 최종 확인 필요 메모를 함께 남긴다.
