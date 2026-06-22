# 발표자 노트

## Slide 1

오늘은 RAG와 prompting framework를 보안 관점에서 보겠습니다. 핵심은 검색 문서가 근거이면서 동시에 공격면이 된다는 점입니다.

## Slide 2

세 질문을 중심으로 발표합니다. indirect injection 유입 위치, source verification 효과, human approval gate의 tool misuse 차단 효과입니다.

## Slide 3

RAG는 retrieval, reranking, generation을 거칩니다. Agentic RAG에서는 tool action까지 붙기 때문에 단순 검색 품질보다 권한 통제가 중요합니다.

## Slide 4

P01/P02는 GraphRAG 구조를, P03은 prompting framework를, P04/P05는 prompt injection과 safety-critical 위험을 보여줍니다.

## Slide 5

위협 경로는 오염 문서가 retrieved context로 들어오고, 모델 답변이나 tool action에 영향을 주는 흐름입니다. 실제 공격 payload는 다루지 않습니다.

## Slide 6

실험은 synthetic toy evaluator입니다. 실제 LLM/API 호출 없이 평가표와 로그 구조가 작동하는지 확인했습니다.

## Slide 7

Poisoned document 조건의 ASR은 0.575000입니다. Source filter 적용 후 0.050000으로 낮아지고, human approval 적용 후 0.025000이 됩니다.

## Slide 8

기말논문으로는 RAG indirect injection 대응을 위한 출처 검증과 승인 게이트 평가 프레임워크를 추천합니다.

## Slide 9

결론은 간단합니다. RAG 보안은 검색, 출처, prompt boundary, tool 권한, 로그가 모두 연결된 시스템 설계 문제입니다.
