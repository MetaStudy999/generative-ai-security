# W07 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | LLM/RAG 기반 AI 시스템의 보안·프라이버시·재현성 평가 프레임워크 | 질의응답 LLM, RAG, code LLM | prompt injection, privacy leakage, benchmark contamination | 문헌분석, synthetic prompt 평가표, 재현성 로그 | 높음 |
| 2 | LLM 보안 평가에서 refusal quality와 over-refusal의 균형 연구 | aligned LLM | jailbreak, 과차단, 정상 업무 저해 | toy guard score 실험 + 위협모형 | 높음 |
| 3 | Code LLM의 취약 코드 생성 위험과 재현성 평가체계 연구 | code LLM | insecure code generation, bug triage failure | 문헌분석 + synthetic/public code prompt 평가 | 높음 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | LLM/RAG 시스템은 prompt, context, output, code artifact, log, benchmark가 연결된 보안 평가 대상이라는 문제 제기 |
| 관련연구 | LLM evaluation, LLM security/privacy, MLLM, software security survey |
| 연구문제 | utility, ASR, privacy leakage, refusal quality, over-refusal, code risk, reproducibility를 통합한 평가 프로토콜 |
| 연구방법 | 문헌 비교표, 위협모형, synthetic prompt category, seed/config/output 로그 |
| 분석/실험 | W07 toy 결과를 방법론 예시로 사용하되 실제 모델 성능으로 일반화하지 않음 |
| 보안적 함의 | confidentiality, integrity, privacy, safety, accountability, reproducibility 관점 |
| 결론 | 재현 가능한 LLM/RAG 보안 평가체계 제안 |

## 3. W07에서 가져갈 contribution 후보

1. LLM 보안 평가를 utility와 security trade-off로 분리하지 않고 한 표에서 함께 기록한다.
2. Prompt/context/output/code/log/benchmark를 보호 자산으로 묶은 위협모형을 제시한다.
3. 실행 로그 없는 수치를 주장하지 않는 재현성 중심 작성 절차를 제시한다.
4. P02/P03/P04/P05처럼 강의계획서 지정 정보와 공식 DOI 기준 정보가 다른 문헌은 검증 상태를 분리해 기록한다.

## 4. KCI 전환 연결

- 추천 제목: LLM/RAG 기반 AI 시스템의 보안·프라이버시·재현성 평가 프레임워크 연구
- 연구방법: W07 문헌분석, LLM/RAG 위협모형, synthetic prompt category 기반 안전 toy 실험.
- 국내 논문화 보완점: 국내 KCI 학회지 양식, 국내 참고문헌 3편 이상, 그림 1개 이상, 연구윤리/AI 활용 고지.

## 5. SCI 전환 연결

- 추천 제목: A Multi-Metric Security, Privacy, and Reproducibility Evaluation Framework for LLM/RAG-Based AI Systems
- 핵심 기여: utility, answer rate, ASR, privacy leakage, refusal quality, over-refusal, code vulnerability rate, reproducibility evidence의 분리 기록.
- SCI 보완점: 실제 LLM/RAG/code LLM benchmark, human annotation protocol, statistical test, external validity 검증.

## 6. 검증 필요 항목

- P03 강의계획서 지정 AI Open 논문과 현재 HCC 논문의 동일 여부.
- P02/P04/P05 강의계획서 저자명 표기 차이.
- public GitHub 저장소에서 PDF 원문 제거 또는 이력 정리 필요 여부.
- W07 toy 수치를 실제 모델 성능처럼 해석하지 않도록 최종 원고 문장 재점검.

<!-- AUTO-WEEKLY-BRIDGE-CHECK:start -->
## 자동 보완: 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: LLM 학습·정렬·평가 과정의 보안·프라이버시 위협면을 기말논문 위협모형의 핵심 축으로 반영한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: 주차별 실험표, metrics_summary.csv 기반 그래프, config/seed/run_log 재현성 증거를 표·그림 후보로 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: 프롬프트, 파라미터, 학습데이터, 출력 로그에서 발생하는 개인정보·정렬 우회 위험을 RAG/LLM 감사 프레임워크의 상위 위협면으로 연결한다.
<!-- AUTO-WEEKLY-BRIDGE-CHECK:end -->
