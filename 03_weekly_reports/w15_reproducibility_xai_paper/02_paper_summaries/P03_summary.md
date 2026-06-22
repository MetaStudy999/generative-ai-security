# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Explainable AI: Core Ideas, Techniques, and Solutions |
| 저자 | Vivek Dwivedi et al. |
| 학술지/학회 | ACM Computing Surveys |
| 연도 | 2023 |
| DOI/URL | 확인 필요 |
| PDF 파일명 | `03_SUBSTITUTE_Mersha_et_al_2024_Explainable_AI_Survey.pdf` |
| 검증 상태 | 로컬 PDF는 Mersha et al., "Explainable Artificial Intelligence: A Survey of Needs, Techniques, Applications, and Future Direction" arXiv:2409.00265 대체 파일이다. 지정 논문 원문 확보 필요 |

## 2. 한 문장 요약

> 지정 논문은 XAI의 핵심 아이디어와 기법을 정리하는 문헌으로 활용할 예정이며, 현재 로컬 대체 PDF는 XAI의 필요성, 기법 분류, 적용 영역, 평가 방법을 보완적으로 설명한다.

## 3. 연구문제

XAI가 어떤 사용자의 어떤 의사결정 문제를 설명해야 하는지, feature attribution, surrogate model, example-based explanation, visualization, human-grounded evaluation을 어떻게 구분할지 정리하는 것이 핵심이다. 현재 로컬 PDF는 안전중요 도메인에서 투명성, 책임성, 공정성이 필요한 이유를 잘 보완한다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Explainability need | black-box 모델을 안전중요 의사결정에 쓰기 위한 설명 요구 | 책임성·안전성 장 |
| XAI technique taxonomy | feature, example, model-specific, model-agnostic 설명 방식 분류 | 관련연구 비교 |
| XAI evaluation | 설명의 충실도, 안정성, 사용자 이해도 평가 | 평가방법 후보 |
| Stakeholder alignment | 개발자, 도메인 전문가, 규제자, 사용자별 설명 요구 차이 | AI 활용 고지와 human review |

## 5. 방법론

지정 논문은 출판사 원문 확보 후 최종 요약을 확정한다. 현재 단계에서는 대체 PDF의 arXiv 첫 페이지와 본문 목차를 바탕으로 XAI survey의 공통 구조를 정리하되, DOI와 세부 인용은 확정하지 않는다.

## 6. 주요 결과

XAI는 단순히 모델 내부를 보여주는 기능이 아니라 신뢰, 책임성, 공정성, 오류 발견, 규제 대응을 위한 평가 대상이다. 설명 품질은 모델 성능과 별도로 측정해야 하며, 설명이 그럴듯해도 실제 모델 원인과 맞지 않을 수 있다.

## 7. 보안 관점 분석

설명은 방어 도구이면서 공격면이다. 과도한 설명은 민감 feature, training sample, decision boundary를 노출할 수 있고, 부정확한 설명은 사용자의 과신을 유도할 수 있다. 따라서 XAI 결과도 leakage, stability, fidelity 관점에서 점검해야 한다.

## 8. 한계와 오픈문제

현재 로컬 PDF가 지정 논문과 일치하지 않으므로 최종 참고문헌으로 확정할 수 없다. 제출 전 Dwivedi et al. 원문을 확보하고 DOI, 권호, article number를 확인해야 한다.

## 9. 기말 논문에 반영할 부분

XAI를 보안 평가의 증거로 사용할 때 설명 충실도와 정보노출 위험을 함께 봐야 한다는 논거를 제공한다. 단, 최종 인용은 지정 논문 검증 후 반영한다.
