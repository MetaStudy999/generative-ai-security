# P01 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Efficient Transformers: A Survey |
| 저자 | Yi Tay, Mostafa Dehghani, Dara Bahri, Donald Metzler |
| 출판 정보 | ACM Computing Surveys, Vol. 55, No. 6, 2022, pp. 1-28 |
| DOI/URL | ACM DOI `10.1145/3530811`; arXiv DOI `10.48550/arXiv.2009.06732`; https://arxiv.org/abs/2009.06732 |
| PDF 파일명 | 01_Tay_et_al_2022_Efficient_Transformers_Survey.pdf |
| 검증 상태 | ACM CSUR 출판 DOI 확인. Article 번호는 Crossref/BibTeX 응답에 미제공되어 확인 필요 |

## 2. 한 문장 요약

P01은 self-attention의 quadratic complexity 병목을 줄이기 위한 sparse, low-rank, kernelized, recurrence/memory 계열 X-former 접근을 체계화한 효율화 survey이다.

## 3. 연구문제

긴 시퀀스에서 attention 계산량과 메모리 사용량을 줄이면서 approximation quality와 task utility를 어느 수준까지 유지할 수 있는가를 묻는다.

## 4. 핵심 개념

| 개념 | 설명 | W04 연결 |
|---|---|---|
| Sparse attention | 모든 토큰 쌍을 보지 않고 선택된 연결만 계산한다. | 긴 프롬프트 처리 비용과 latency |
| Low-rank approximation | attention 행렬을 낮은 랭크 구조로 근사한다. | 보안 필터·감사 시스템의 비용 절감 |
| Kernelized attention | softmax attention을 kernel trick 또는 random feature로 근사한다. | 긴 입력 보안 평가의 확장성 |
| Memory/recurrence | 이전 문맥을 압축 저장하거나 재사용한다. | 로그·문맥 보존과 민감정보 노출면 |

## 5. 방법론

문헌조사와 taxonomy 기반 survey이다. 자체 공격 실험이 아니라 효율화 구조를 비교하고, 어떤 축에서 complexity, memory, latency, approximation quality를 볼지 정리한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Attention Complexity |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$Cost_{full}=O(n^2d),\qquad Cost_{sparse}\approx O(nkd)$$ |
| 기호·입력·출력 | \(n\): sequence length, \(d\): hidden dimension, \(k\): 제한된 key 수 |
| 직관적 의미 | Attention Complexity는 Transformer·NLP 보안 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Transformer·NLP 보안 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | latency, memory, context length, retrieval coverage, ASR |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

Efficient Transformer는 긴 입력 처리를 가능하게 하지만, 효율화 자체가 보안성을 보장하지 않는다. 오히려 긴 프롬프트와 긴 로그를 다루는 시스템에서는 민감정보 노출면, 방어 latency, 감사 비용을 함께 평가해야 한다.

## 7. 보안 관점 분석

P01은 보안 직접 문헌은 아니지만 W04의 비용 축을 제공한다. 긴 입력 LLM/RAG/ICL 시스템에서 프롬프트 마스킹, 로그 감사, 공격 탐지기를 적용하려면 latency와 memory overhead를 분리해 기록해야 한다.

## 8. 한계와 오픈문제

NLP 대적공격이나 prompt privacy를 직접 평가하지 않는다. W04 보고서에서는 P04/P05와 결합해 효율성-보안성-재현성의 연결 근거로만 사용한다.

## 9. 기말 논문에 반영할 부분

긴 입력 기반 프롬프트 보안 평가에서 비용, latency, auditability를 독립 평가축으로 두는 근거로 활용한다.
