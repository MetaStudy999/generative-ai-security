# W07 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | LLM 기반 QA, RAG 시스템, code generation LLM, multimodal LLM |
| 보호 자산 | training data, system prompt, user prompt, retrieval context, model output, code artifact, logs, benchmark set |
| 공격자 | 외부 사용자, 악의적 문서 제공자, prompt/context 관찰자, log 관찰자, 내부자, 공급망 참여자 |
| 공격자의 지식 | black-box, gray-box, prompt observer, log observer 조건을 구분 |
| 공격자의 능력 | prompt manipulation, context injection, repeated queries, sensitive request formulation, unsafe code request |
| 공격 경로 | 데이터 수집, pretraining, instruction tuning, alignment, retrieval, inference, code generation, logging, benchmark evaluation |
| 공격 성공 조건 | unsafe answer, privacy leakage, prompt leakage, insecure code generation, benchmark contamination, audit failure |
| 방어/점검 | refusal policy, input/output filtering, code review, log audit, evaluation dataset governance, seed/config/output 보존 |
| 제외 범위 | actual jailbreak reproduction, personal data extraction, unauthorized service probing, exploit instruction generation |

## W07 안전 범위

- 실제 LLM/API 호출은 수행하지 않는다.
- 실제 개인정보 추출, 실제 jailbreak 재현, 무단 서비스 질의, exploit instruction은 포함하지 않는다.
- 실험은 synthetic prompt category와 rule-based toy guard score simulator로 평가 형식만 검증한다.
- ASR, privacy leakage, code vulnerability rate는 실제 공격 성공률이나 실제 모델 위험 확률이 아니라 toy score 기반 기록값이다.

## 연구문제 후보

RQ1. LLM/RAG 기반 AI 시스템에서 prompt, context, output, code artifact, log, benchmark를 보호 자산으로 함께 볼 때 최소 위협모형은 어떻게 구성되는가?

RQ2. Prompt attack simulation과 privacy-risk prompt 조건에서 ASR, privacy leakage, refusal quality는 어떤 trade-off를 보이는가?

RQ3. Code security prompts에서 code vulnerability rate와 over-refusal을 동시에 기록해야 하는 이유는 무엇인가?
