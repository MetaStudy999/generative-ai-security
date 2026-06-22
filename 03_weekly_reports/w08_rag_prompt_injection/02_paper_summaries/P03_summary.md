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

## 6. 주요 결과

Prompting framework는 단순 prompt 작성법이 아니라 데이터 준비, prompt 구성, 실행, 서비스 운영까지 포함한다. 이 구조는 W08 보안 분석에서 system prompt, user prompt, tool instruction, retrieved context의 경계를 구분하는 기준이 된다.

## 7. 보안 관점 분석

Prompting framework의 계층이 늘어날수록 trust boundary도 늘어난다. Data level의 오염 문서, base level의 template 취약성, execute level의 tool misuse, service level의 audit gap은 서로 다른 방어를 요구한다. W08 실험의 human approval gate는 execute level 통제로 볼 수 있다.

## 8. 한계와 오픈문제

이 논문은 framework 생태계와 용어 정리에 초점이 있으며, prompt injection 공격 성공률이나 방어 효과를 직접 측정하지는 않는다. 보안 연구에서는 각 계층별 권한, 로그, 승인 정책을 추가해야 한다.

강의계획서의 축약 표기인 X. Liu et al.과 로컬 DOI 기준 Xiaoxia Liu et al.은 동일 저자 표기로 볼 수 있으나, 제출 참고문헌에는 DOI 기준 정식 제목인 "Prompting Frameworks for Large Language Models: A Survey"를 사용한다.

## 9. 기말 논문에 반영할 부분

기말 논문에서는 P03의 계층형 prompting framework를 RAG·agent pipeline 위협모형의 뼈대로 사용한다.
