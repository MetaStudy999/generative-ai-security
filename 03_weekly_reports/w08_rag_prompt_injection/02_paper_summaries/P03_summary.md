# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Prompting Frameworks for Large Language Models: A Survey |
| 저자 | Xiaoxia Liu, Jingyi Wang, Xiaohan Yuan, Jun Sun, Guoliang Dong, Peng Di, Wenhai Wang, Dongxia Wang |
| 학술지/학회 | ACM Computing Surveys |
| 연도 | 2026 |
| DOI/URL | https://doi.org/10.1145/3789253 |
| 권호/Article | ACM Computing Surveys 58(10), Article 255, 38 pages |
| PDF 파일명 | 03_Liu_et_al_2026_Prompting_Frameworks_for_LLMs.pdf |
| 강의계획서 표기 | X. Liu et al., "Prompting Frameworks for Large Language Models" |
| 로컬 PDF/DOI 표기 | Xiaoxia Liu et al., "Prompting Frameworks for Large Language Models: A Survey" |
| 검증 상태 | DOI/Crossref와 PDF 첫 페이지 확인. X. Liu는 Xiaoxia Liu로 해석 가능하나 제목의 ": A Survey" 포함을 공식 서지로 기록 |

## 2. 한 문장 요약

> 이 논문은 LLM을 효과적으로 사용하기 위한 prompting framework를 data, base, execute, service level의 계층형 생명주기로 정리하며, prompt와 tool 기반 LLM application의 공학적 구조를 설명한다.

## 3. 연구문제

LLM의 강력한 능력은 prompt, external tool, framework, service orchestration을 통해 실제 업무로 연결된다. 그러나 prompt 관련 용어와 도구 생태계가 빠르게 변하면서 표준화된 분류가 부족하다. 이 논문은 prompting framework라는 개념으로 이를 체계화한다.

## 4. 핵심 개념

| 개념 | 설명 | W08 연결 |
|---|---|---|
| Prompting Framework | LLM과 상호작용을 관리·단순화·자동화하는 framework |
| Data Level | 데이터, 문서, 예시, context를 준비하는 층 |
| Base Level | prompt template, chain, memory 등 기본 구성 |
| Execute Level | tool use, agent action, workflow execution |
| Service Level | API, application, 운영 서비스와 사용자 접점 |

## 5. 방법론

survey 방식으로 prompting tool과 framework를 수집하고, 생명주기 계층을 제안한다. LLM이 외부 도구와 연결될 때 prompt가 어떤 역할을 하는지 공학적 관점으로 정리한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Prompted Conditional Generation |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$p_\theta(y\mid p,x)=\prod_t p_\theta(y_t\mid y_{<t},p,x)$$ |
| 기호·입력·출력 | \(p\): prompt/instruction, \(x\): task input 또는 retrieved context, \(y_t\): 출력 token |
| 직관적 의미 | Prompted Conditional Generation는 RAG·Prompt Injection 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | RAG·Prompt Injection 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | utility, refusal quality, injection ASR, groundedness |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

Prompting framework는 단순 prompt 작성법이 아니라 데이터 준비, prompt 구성, 실행, 서비스 운영까지 포함한다. 이 구조는 W08 보안 분석에서 system prompt, user prompt, tool instruction, retrieved context의 경계를 구분하는 기준이 된다.

## 7. 보안 관점 분석

Prompting framework의 계층이 늘어날수록 trust boundary도 늘어난다. Data level의 오염 문서, base level의 template 취약성, execute level의 tool misuse, service level의 audit gap은 서로 다른 방어를 요구한다. W08 실험의 human approval gate는 execute level 통제로 볼 수 있다.

## 8. 한계와 오픈문제

이 논문은 framework 생태계와 용어 정리에 초점이 있으며, prompt injection 공격 성공률이나 방어 효과를 직접 측정하지는 않는다. 보안 연구에서는 각 계층별 권한, 로그, 승인 정책을 추가해야 한다.

강의계획서의 축약 표기인 X. Liu et al.과 로컬 DOI 기준 Xiaoxia Liu et al.은 동일 저자 표기로 볼 수 있으나, 제출 참고문헌에는 DOI 기준 정식 제목인 "Prompting Frameworks for Large Language Models: A Survey"를 사용한다.

## 9. 기말 논문에 반영할 부분

기말 논문에서는 P03의 계층형 prompting framework를 RAG·agent pipeline 위협모형의 뼈대로 사용한다.
