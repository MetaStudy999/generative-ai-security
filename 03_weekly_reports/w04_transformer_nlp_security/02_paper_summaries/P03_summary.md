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

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Scaled Dot-Product Attention |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$ |
| 기호·입력·출력 | \(Q\): query, \(K\): key, \(V\): value, \(d_k\): scaling 차원 |
| 직관적 의미 | Scaled Dot-Product Attention는 Transformer·NLP 보안 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Transformer·NLP 보안 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | perplexity, utility, attack success, leakage rate |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

Transformer는 NLP에 국한되지 않고 CV, audio, multimodal tasks로 확장된다. 보안 평가에서는 입력, attention 구조, 출력, 응용 시나리오별로 공격면을 분리해야 한다.

## 7. 보안 관점 분석

P03은 W04에서 위협모형의 대상 시스템을 정의하는 배경이다. 동일한 prompt privacy 문제라도 classifier, QA, summarization, RAG, multimodal pipeline에서 보호 자산과 로그 경로가 달라질 수 있다.

## 8. 한계와 오픈문제

보안 지표나 프라이버시 지표를 직접 제공하지 않는다. W04에서는 P04/P05의 보안 지표와 결합해 taxonomy 기반 위협모형을 구성한다.

## 9. 기말 논문에 반영할 부분

프롬프트 기반 NLP 시스템을 입력·모델·출력·로그·외부 도구 호출 단계로 나누는 기본 구조 설명에 활용한다.
