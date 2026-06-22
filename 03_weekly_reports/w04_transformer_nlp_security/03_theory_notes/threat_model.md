# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | Transformer-based NLP model, LLM prompt system, keyword privacy-risk detector |
| 보호 자산 | prompt input, ICL examples, model output, logs, tool-call arguments, user intent |
| 공격자 | black-box attacker, gray-box attacker, prompt observer, log observer |
| 공격자의 지식 | 입력·출력 관찰, 일부 탐지 규칙 추정, 로그 접근 가능성으로 구분 |
| 공격자의 능력 | word substitution, paraphrasing, prompt reformatting, sensitive value insertion, output observation |
| 공격 경로 | 프롬프트 입력, ICL 예시, 모델 출력, 로그 저장, 외부 도구 호출 인자 |
| 공격 성공 조건 | privacy-risk prompt가 benign으로 분류되거나, 민감값이 prompt/output/log에 남는 경우 |
| 방어자 가정 | masking, prompt wrapper, policy control, config/seed/output log 보존 가능 |
| 제외 범위 | 실제 서비스 침해, 실제 개인정보 사용, 무단 API 질의, 악용 가능한 공격 절차 |

## 연구문제 후보

RQ1. 프롬프트 기반 AI 시스템에서 민감정보 보호를 평가하기 위한 최소 지표는 무엇인가?

RQ2. 단어 치환 공격은 keyword privacy-risk detector의 clean score와 attack success rate에 어떤 영향을 주는가?

RQ3. Prompt masking과 privacy-preserving prompt wrapper는 privacy leakage와 utility score를 어떻게 변화시키는가?

RQ4. Efficient Transformer의 비용·latency 관점은 프롬프트 보안 평가의 재현성과 배포 가능성에 어떤 영향을 주는가?
