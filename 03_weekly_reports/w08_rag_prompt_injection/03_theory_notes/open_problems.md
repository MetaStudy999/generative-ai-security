# 한계와 오픈문제

## 1. 문헌 검증 한계

- P01은 arXiv ID는 확인했지만 DOI가 placeholder로 표시되어 DOI 확정 인용은 보류한다.
- P02-P05는 PDF 첫 페이지의 DOI를 확인했지만, 최종 제출 전 공식 출판사 페이지와 한 번 더 대조하는 것이 좋다.
- Survey 문헌의 정량값은 연구별 모델, 데이터셋, 방어조건이 달라 직접 비교가 어렵다.

## 2. 실험 한계

- W08 실험은 실제 LLM/API를 호출하지 않는 synthetic toy evaluator다.
- 산출된 ASR, faithfulness, tool misuse rate는 평가표 검증용이며 실제 배포 시스템 보안성으로 일반화할 수 없다.
- 오염 문서와 방어 정책은 abstract flag와 확률 모델로 표현했기 때문에 실제 RAG parser, retriever, LLM decoder의 복잡성을 반영하지 않는다.

## 3. 연구 오픈문제

| 질문 | 후속 연구 방향 |
|---|---|
| GraphRAG의 node/edge provenance를 어떻게 검증할 것인가 | graph element 단위 metadata, signed source, edge trust score |
| Indirect injection과 정상 instruction을 어떻게 구분할 것인가 | structured prompt, instruction/data boundary, model-side classifier |
| ASR과 utility의 균형을 어떻게 잡을 것인가 | answer rate, over-blocking, faithfulness를 함께 측정 |
| Agent tool misuse를 어떻게 감사할 것인가 | permission policy, approval log, replayable audit trail |
| Safety-critical domain에 필요한 추가 통제는 무엇인가 | domain expert review, regulatory evidence, redacted adversarial test |

## 4. 기말논문 연결

기말 논문에서는 W08을 RAG 보안 평가 프레임워크의 중심 주차로 삼고, W07의 LLM 보안 평가 지표와 W14의 MLOps 공급망 통제를 함께 연결할 수 있다.
