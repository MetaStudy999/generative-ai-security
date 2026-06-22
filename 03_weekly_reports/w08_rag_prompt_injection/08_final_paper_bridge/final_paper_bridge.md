# W08 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | RAG 기반 생성형 AI 시스템에서 간접 프롬프트 인젝션 대응 방안 연구 | RAG 시스템 | Indirect prompt injection | 문헌분석, synthetic document 모의실험, 방어정책 설계 | 높음 |
| 2 | 보안형 RAG 시스템에서 문서·graph 출처 검증 메타데이터 설계 연구 | RAG + Vector DB + Graph DB | 문서 오염, edge/path 오염, 출처 위조 | 프레임워크 설계, 체크리스트 | 높음 |
| 3 | LLM 에이전트의 tool 권한 오남용 방지를 위한 human approval gate 연구 | Agentic RAG | Tool misuse, context hijacking | toy 실험, 정책 설계, audit log 분석 | 높음 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | RAG와 agentic AI 확산으로 retrieved context와 tool action이 새로운 공격면이 됨 |
| 관련연구 | GraphRAG survey, graph-based RAG survey, prompting framework survey, prompt injection survey, 의료 LLM 취약성 연구 |
| 연구문제 | 간접 프롬프트 인젝션, 출처 검증, human approval gate의 방어 효과 |
| 연구방법 | synthetic document 기반 모의실험, source filter, approval gate, 재현성 로그 |
| 분석/실험 | ASR, source verification, tool misuse rate, faithfulness, answer rate 비교 |
| 보안적 함의 | 기밀성, 무결성, 안전성, 책임성 관점에서 RAG 통제 필요 |
| 결론 | 보안형 RAG 평가·통제 프레임워크 제안 |

## 3. W08 실험에서 얻은 근거

| 조건 | ASR | Source Verification | Tool Misuse Rate | 해석 |
|---|---:|---:|---:|---|
| Clean RAG | 0.000000 | 1.000000 | 0.000000 | 정상 기준 조건 |
| Poisoned document | 0.575000 | 0.275000 | 0.125000 | 오염 문서 유입 시 위험 증가 |
| Source filter 적용 | 0.050000 | 1.000000 | 0.025000 | 출처 검증으로 공격 성공률 감소 |
| Human approval 적용 | 0.025000 | 1.000000 | 0.000000 | 승인 게이트로 tool misuse 차단 |

## 4. 최종 추천 주제

최종 추천 주제는 “RAG 기반 생성형 AI 시스템에서 간접 프롬프트 인젝션 대응을 위한 출처 검증·승인 게이트 평가 프레임워크”다. 문헌분석, 안전한 synthetic 실험, 체크리스트 설계를 결합할 수 있어 박사과정 세미나 보고서에서 기말논문으로 확장하기 적합하다.
