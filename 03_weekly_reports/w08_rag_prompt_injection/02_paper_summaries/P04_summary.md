# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Prompt Injection Attacks on Large Language Models: A Survey of Attack Methods, Root Causes, and Defense Strategies |
| 저자 | Tongcheng Geng, Zhiyuan Xu, Yubin Qu, W. Eric Wong |
| 학술지/학회 | Computers, Materials & Continua |
| 연도 | 2026 |
| DOI/URL | https://doi.org/10.32604/cmc.2025.074081 |
| 권호/페이지 | Computers, Materials & Continua 87(1), pp. 1-10 |
| PDF 파일명 | 04_Geng_et_al_2025_Prompt_Injection_Attacks_Survey.pdf |
| 강의계획서 표기 | Tianlei Geng et al. |
| 로컬 PDF/DOI 표기 | Tongcheng Geng et al. |
| 검증 상태 | DOI/Crossref와 PDF 첫 페이지 확인. Tianlei/Tongcheng 표기 차이는 확인 필요 |

## 2. 한 문장 요약

> 이 논문은 prompt injection 공격을 direct, indirect, multimodal 유형과 방어 계층으로 체계화하며, LLM이 instruction과 data를 안정적으로 구분하지 못하는 구조적 취약성을 핵심 원인으로 제시한다.

## 3. 연구문제

LLM application이 RAG, plugin, memory, tool use로 확장되면서 prompt injection은 단일 입력 우회가 아니라 외부 문서, 웹페이지, 이미지, agent action을 거치는 복합 공격면이 된다. 이 논문은 공격 방법, 근본 원인, 방어 전략을 하나의 survey로 통합한다.

## 4. 핵심 개념

| 개념 | 설명 | W08 연결 |
|---|---|---|
| Direct Injection | 사용자가 직접 악성 지시를 입력하는 형태 |
| Indirect Injection | 외부 문서나 웹페이지에 숨은 지시가 context로 들어오는 형태 |
| Multimodal Injection | 이미지·음성 등 비텍스트 입력을 통한 지시 조작 |
| Root Cause | instruction/data 경계 불명확성, attention 취약성, 학습 한계 |
| Defense-in-Depth | 입력, system architecture, model level 방어의 결합 |

## 5. 방법론

Kitchenham 방식의 systematic review를 따라 2022-2025년 연구 128편을 종합했다. 공격 분류, 근본 원인, 방어 전략, 평가 프레임워크 부족 문제를 정리한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Prompt-injection ASR |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$ASR_{PI}=\frac{N_{policy\ failure}}{N_{injection\ tests}}$$ |
| 기호·입력·출력 | \(N_{injection\ tests}\): synthetic injection 평가 수, \(N_{policy\ failure}\): 정책 실패 출력 수 |
| 직관적 의미 | Prompt-injection ASR는 RAG·Prompt Injection 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | RAG·Prompt Injection 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | ASR, groundedness, refusal quality, utility |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

원문은 보호되지 않은 시스템에서 prompt injection 성공률이 높게 보고된 연구들을 종합하고, input preprocessing, architecture-level defense, model-level defense의 효과와 한계를 비교한다. 또한 표준화된 평가 프로토콜이 부족하다는 점을 중요한 연구 공백으로 제시한다.

## 7. 보안 관점 분석

W08의 핵심 보안 문헌이다. 특히 RAG에서는 indirect injection이 검색 문서에서 context로 들어오므로 사용자가 악성 지시를 직접 입력하지 않아도 모델 행동이 바뀔 수 있다. Agentic RAG에서는 tool permission, memory, external action이 결합되므로 human approval gate와 audit log가 필요하다.

## 8. 한계와 오픈문제

Survey 문헌의 수치는 연구별 환경과 모델이 달라 직접 비교가 어렵다. 또한 공격 payload 세부를 재현하는 방향보다, 안전한 synthetic benchmark와 방어 지표 표준화로 확장해야 한다.

강의계획서의 Tianlei Geng 표기와 로컬 PDF·DOI 기준 Tongcheng Geng 표기가 다르므로, 최종 제출 전 수업자료 또는 출판사 페이지에서 저자명을 다시 확인한다. 현재 보고서에는 DOI 기준 Tongcheng Geng et al.을 사용한다.

## 9. 기말 논문에 반영할 부분

기말 논문 위협모형에는 direct/indirect/multimodal injection 구분을 반영하고, 평가방법에는 ASR, source verification, tool misuse rate, human approval effect를 넣는다.
