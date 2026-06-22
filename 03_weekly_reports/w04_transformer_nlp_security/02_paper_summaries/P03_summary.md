# P03 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A survey of transformers |
| 저자 | Tianyang Lin, Yuxin Wang, Xiangyang Liu, Xipeng Qiu |
| 출판 정보 | AI Open, Vol. 3, 2022, pp. 111-132 |
| DOI/URL | `10.1016/j.aiopen.2022.10.001`; https://www.sciencedirect.com/science/article/pii/S2666651022000146 |
| PDF 파일명 | 03_Lin_et_al_2022_Survey_of_Transformers.pdf |
| 검증 상태 | AI Open 출판 DOI/URL/권호/쪽 확인 |

## 2. 한 문장 요약

P03은 Transformer 구조, architectural modification, pre-training, NLP/CV/multimodal applications를 큰 taxonomy로 정리한 Transformer survey이다.

## 3. 연구문제

Transformer 계열 구조와 응용을 어떤 taxonomy로 분류할 수 있으며, vanilla Transformer 이후의 변형은 어떤 설계 방향으로 확장되었는가를 다룬다.

## 4. 핵심 개념

| 개념 | 설명 | W04 연결 |
|---|---|---|
| Vanilla Transformer | self-attention, Q/K/V, positional encoding, feed-forward block으로 구성된다. | W04 AI 원리 배경 |
| Architectural modification | attention, position, depth, memory 구조를 변경한다. | 공격면을 구조별로 분리 |
| Pre-training | 사전학습과 downstream adaptation을 다룬다. | LLM/ICL privacy 연결 |
| Applications | NLP, CV, audio, multimodal 응용으로 확장된다. | W03/W04/W07 연결 |

## 5. 방법론

문헌조사 기반 taxonomy survey이다. 특정 보안 공격을 재현하지 않고, Transformer 계열을 구조와 응용 관점으로 분류한다.

## 6. 주요 결과

Transformer는 NLP에 국한되지 않고 CV, audio, multimodal tasks로 확장된다. 보안 평가에서는 입력, attention 구조, 출력, 응용 시나리오별로 공격면을 분리해야 한다.

## 7. 보안 관점 분석

P03은 W04에서 위협모형의 대상 시스템을 정의하는 배경이다. 동일한 prompt privacy 문제라도 classifier, QA, summarization, RAG, multimodal pipeline에서 보호 자산과 로그 경로가 달라질 수 있다.

## 8. 한계와 오픈문제

보안 지표나 프라이버시 지표를 직접 제공하지 않는다. W04에서는 P04/P05의 보안 지표와 결합해 taxonomy 기반 위협모형을 구성한다.

## 9. 기말 논문에 반영할 부분

프롬프트 기반 NLP 시스템을 입력·모델·출력·로그·외부 도구 호출 단계로 나누는 기본 구조 설명에 활용한다.
