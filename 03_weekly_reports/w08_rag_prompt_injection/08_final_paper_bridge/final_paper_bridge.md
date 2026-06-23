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

## 5. KCI/SCI 전환 방향

| 구분 | 전환 방향 | 보완 필요 |
|---|---|---|
| KCI형 | 국내 생성형 AI 보안·정보보호 맥락에서 RAG 출처 검증과 승인 게이트 평가 프레임워크를 제안한다. | 국내 참고문헌 3편 이상, 그림 1개 이상, 국내 제도·가이드라인 연결 |
| SCI형 | Multi-metric evaluation framework for indirect prompt injection defense in RAG-based LLM systems로 구성한다. | 공개 benchmark, 복수 LLM, 복수 seed, provenance schema, 독립 평가자 |
| 공통 | ASR, source verification, tool misuse, faithfulness, answer rate, reproducibility evidence를 분리 보고한다. | W08 toy 수치를 실제 제품 성능으로 일반화하지 않음 |

## 6. 최종 제출 전 검토 리스크

| 항목 | 상태 | 조치 |
|---|---|---|
| P01 DOI/출판정보 | 확인 필요 | arXiv 기준으로만 인용하고 ACM DOI는 확정하지 않는다. |
| P02 강의계획서 저자명 | 확인 필요 | DOI 기준 Zulun Zhu et al.과 Jianxiang Li et al. 표기 차이를 수업자료로 확인한다. |
| P04 저자명 | 확인 필요 | Tianlei/Tongcheng Geng 차이를 출판사 페이지로 재확인한다. |
| P05 제목 | 확인 필요 | 강의계획서 지정 제목과 JAMA DOI 기준 제목의 동일 여부를 확인한다. |
| PDF 원문 보관 | 위험 있음 | public GitHub에서는 PDF 원문 대신 DOI/URL과 요약만 남기는 방안을 검토한다. |

<!-- AUTO-WEEKLY-BRIDGE-CHECK:start -->
## 자동 보완: 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: RAG 검색 문서, prompt template, tool 권한, human approval gate를 문서 오염·간접 프롬프트 인젝션 통제 개념으로 반영한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: 주차별 실험표, metrics_summary.csv 기반 그래프, config/seed/run_log 재현성 증거를 표·그림 후보로 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: 오염 문서 유입, 출처 검증 실패, tool misuse를 직접 평가하는 핵심 주차로서 RAG 문서 오염 감사 프레임워크의 중심 근거가 된다.
<!-- AUTO-WEEKLY-BRIDGE-CHECK:end -->
