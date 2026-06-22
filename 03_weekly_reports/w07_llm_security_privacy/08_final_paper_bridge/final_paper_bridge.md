# W07 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | LLM/RAG 기반 AI 시스템의 보안·프라이버시·재현성 평가 프레임워크 | 질의응답 LLM, RAG, code LLM | prompt injection, data leakage, benchmark contamination | 문헌분석, synthetic prompt 평가표, 재현성 로그 | 높음 |
| 2 | LLM 보안 평가에서 refusal quality와 over-refusal의 균형 연구 | aligned LLM | jailbreak, 과차단, 정상 업무 저해 | policy label 기반 평가 프로토콜 | 높음 |
| 3 | Code LLM의 취약 코드 생성 위험과 안전한 재작성 평가 연구 | 코드 생성 LLM | insecure code generation, bug triage failure | synthetic/public code prompt 평가 | 높음 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | LLM/RAG 시스템은 prompt, context, output, log, benchmark가 연결된 보안 평가 대상이라는 문제 제기 |
| 관련연구 | LLM evaluation, LLM security/privacy, MLLM, software security survey |
| 연구문제 | utility, ASR, privacy leakage, refusal quality, code risk, reproducibility를 통합한 평가 프로토콜 |
| 연구방법 | 문헌 비교표, 위협모형, synthetic prompt category, seed/config/output 로그 |
| 분석/실험 | W07 toy 결과를 방법론 예시로 사용하되 실제 모델 성능으로 일반화하지 않음 |
| 보안적 함의 | confidentiality, integrity, privacy, safety, accountability 관점 |
| 결론 | 재현 가능한 LLM/RAG 보안 평가체계 제안 |

## 3. W07에서 가져갈 contribution 후보

1. LLM 보안 평가를 utility와 security trade-off로 분리하지 않고 한 표에서 함께 기록한다.
2. Prompt/context/output/code/log/benchmark를 보호 자산으로 묶은 위협모형을 제시한다.
3. 실행 로그 없는 수치를 주장하지 않는 재현성 중심 작성 절차를 제시한다.
4. P02/P03/P04처럼 출판정보가 불명확한 문헌은 arXiv/PDF 확인과 공식 DOI 검증 상태를 분리해 기록한다.
