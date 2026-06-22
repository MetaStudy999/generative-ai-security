# W07 발표자 노트

## 1. 표지

오늘 발표는 LLM 학습·정렬·평가 원리를 보안·프라이버시 평가로 연결하는 내용입니다. 핵심 메시지는 LLM 보안을 ASR 하나로 판단하면 안 되고 utility, leakage, refusal, code risk, 재현성을 함께 봐야 한다는 점입니다.

## 2. 왜 중요한가

LLM은 모델 파일 하나가 아닙니다. Prompt, context window, output, log, benchmark가 이어진 시스템입니다. 그래서 어느 한 지점이 오염되거나 노출되면 평가 결과와 보안 판단이 함께 흔들립니다.

## 3. AI 원리

Pretraining은 데이터에서 언어 패턴을 학습하는 단계이고, instruction tuning과 alignment는 지시 따르기와 안전 정책 적합성을 강화하는 단계입니다. Context window는 입력과 검색 문서가 함께 들어가는 공간이라 보안 경계로 봐야 합니다.

## 4. 평가 원리

Benchmark는 필요하지만 충분하지 않습니다. 평가셋 오염, hidden test leakage, prompt sensitivity가 있으면 점수 해석이 어려워집니다. 그래서 seed, config, prompt set, output log를 같이 남겨야 합니다.

## 5. 보안 이슈

대표 위협은 data extraction, prompt injection, prompt leakage, privacy leakage, insecure code generation입니다. 오늘은 공격 절차를 재현하지 않고 평가 항목과 기록 방식을 다룹니다.

## 6. 논문 5편

P01은 평가, P02와 P03은 보안·프라이버시 분류, P04는 멀티모달 LLM, P05는 소프트웨어 보안 접점을 맡습니다. 이 다섯 편을 연결하면 LLM 보안 평가는 여러 축을 동시에 봐야 한다는 결론이 나옵니다.

## 7. 위협모형

흐름은 user prompt가 context window를 거쳐 LLM response, logs, code, benchmark로 이어지는 구조입니다. 보호 자산은 학습데이터, system prompt, context, output, code, logs, benchmark입니다.

## 8. 평가 프로토콜

평가 항목은 utility, ASR, privacy leakage, refusal quality, over-refusal, code vulnerability rate입니다. 특히 refusal quality와 over-refusal은 함께 봐야 합니다. 위험 요청을 잘 거절해도 정상 요청을 지나치게 막으면 운영 품질이 떨어집니다.

## 9. Toy 실험

실험은 synthetic prompt category만 사용했습니다. 실제 LLM을 호출하지 않고 toy guard score를 만들었습니다. 목적은 보안 공격 재현이 아니라 지표와 로그 구조 확인입니다.

## 10. 결과

Clean prompts의 utility는 0.866746이고 answer rate는 1.000000입니다. Prompt attack simulation의 ASR은 0.150000, refusal quality는 0.850000입니다. Privacy-risk prompts의 leakage는 0.025000입니다.

## 11. 해석

Code security prompts에서는 code vulnerability rate가 0.200000이고 over-refusal이 0.350000입니다. 이 값은 실제 코드 모델 성능이 아니라 “취약 코드 위험과 과차단을 한 표에 같이 기록해야 한다”는 구조를 보여주는 toy 결과입니다. 모든 수치는 outputs 파일 기준입니다.

## 12. 기말논문 연결

기말논문에서는 LLM/RAG 기반 AI 시스템의 보안·프라이버시·재현성 평가 프레임워크로 연결할 수 있습니다. W07은 관련연구, 위협모형, 평가방법, 재현성 장에 바로 들어갑니다.

## 13. 결론

마지막으로 네 가지를 강조합니다. LLM 보안 평가는 다중지표 문제이고, ASR 단독 평가는 부족하며, utility 단독 평가도 위험합니다. 그리고 수치는 실행 로그가 있을 때만 주장해야 합니다.
