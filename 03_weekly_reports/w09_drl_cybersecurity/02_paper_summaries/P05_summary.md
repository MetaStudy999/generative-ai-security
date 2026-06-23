# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Deep Reinforcement Learning Verification: A Survey |
| 저자 | Matthew Landers; Afsaneh Doryab |
| 학술지/학회 | ACM Computing Surveys, Vol. 55, No. 14s, Article 330, pp. 1-31 |
| 연도 | 2023 |
| DOI/URL | https://doi.org/10.1145/3596444 |
| PDF 파일명 | 05_Landers_Doryab_2023_DRL_Verification_Survey.pdf |
| 검증 상태 | DOI 확인 완료 / 강의계획서 지정 저자 동일 여부 확인 필요: 공식 DOI 저자명은 `Matthew Landers; Afsaneh Doryab`, 강의계획서 저자명은 `H. Yan et al.` |

## 2. 한 문장 요약

> 이 논문은 DRL 시스템의 안전성, 안정성, 강건성 보증을 위한 verification 방법을 분류하며, 보상 최적화만으로는 안전중요 AI 시스템을 정당화할 수 없다는 점을 강조한다.

## 3. 연구문제

DRL 정책이 무한하거나 큰 입력공간에서 안전 속성을 만족하는지 어떻게 보증할 수 있는가가 핵심 질문이다. 특히 stochastic environment와 sequential decision 때문에 일반 DNN verification보다 DRL verification이 더 어렵다는 점을 다룬다.

## 4. 핵심 개념

| 개념 | 설명 | W09 연결 |
|---|---|---|
| Specification | 시스템이 지켜야 할 안전·강건성 속성을 명시한다. | safety violation 정의 |
| Reachability | 가능한 상태/출력 집합이 위험 영역에 닿는지 본다. | perturbed alert 평가 |
| Counterexample | 명세 위반 사례를 찾아 정책 실패를 설명한다. | 샘플 로그 해석 |
| Probabilistic behavior | 환경의 확률성과 정책의 확률성을 고려한다. | synthetic stochastic event |

## 5. 방법론

DRL verification의 foundations, taxonomy, stochasticity 처리, specification 작성, 테스트 환경과 metric을 survey한다. DNN verification과 MDP/RL verification의 교차 지점도 함께 설명한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | DRL Policy Verification Constraint |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$\forall s\in\mathcal{S}_{safe}:\ \pi(s)\in\mathcal{A}_{allowed}$$ |
| 기호·입력·출력 | \(\mathcal{S}_{safe}\): 안전 상태 집합, \(\mathcal{A}_{allowed}\): 허용 행동 집합 |
| 직관적 의미 | DRL Policy Verification Constraint는 DRL 사이버보안 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | DRL 사이버보안 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | constraint satisfaction rate, violation count, certified region |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

DRL은 높은 성능을 보이더라도 safety, robustness, stability를 별도로 보증해야 한다. 검증 방법은 specification 품질과 scalability에 크게 좌우되며, 복잡한 환경에서는 완전한 보증보다 체계적 testing과 제한된 formal check를 조합해야 한다.

## 7. 보안 관점 분석

W09의 보상조작 실험은 완전한 formal verification은 아니지만, 명세 기반 사고를 적용한다. 즉 “공격 이벤트를 monitor로 넘기지 않을 것”, “정상 이벤트를 isolate하지 않을 것” 같은 safety violation을 명시하고 정책을 평가한다.

## 8. 한계와 오픈문제

Verification survey는 실제 cyber-defense IDS benchmark를 제공하지 않는다. 기말 논문에서는 toy 실험, 문헌분석, 명세 기반 체크리스트를 결합하는 현실적인 범위로 제한해야 한다. 공식 DOI 메타데이터는 `Matthew Landers; Afsaneh Doryab`를 저자로 확인하지만, 강의계획서의 `H. Yan et al.` 표기와 불일치하므로 지정문헌 동일성 판단은 확인 필요 항목으로 유지한다.

주의: W09의 P05는 강의계획서 지정 저자명 `H. Yan et al.`과 현재 로컬 PDF 기준 `Matthew Landers; Afsaneh Doryab`가 다르므로, 동일 논문 여부와 최종 ACM 출판정보를 확인 필요 상태로 유지한다.

## 9. 기말 논문에 반영할 부분

기말 논문의 보안적 함의와 평가방법 장에서 DRL 정책 검증, safety specification, perturbation 기반 robustness 평가를 설명하는 근거로 사용한다.
