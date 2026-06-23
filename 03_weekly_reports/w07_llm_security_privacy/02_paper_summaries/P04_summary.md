# 논문 요약: P04

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문명 | A survey on multimodal large language models |
| 저자 | Shukang Yin, Chaoyou Fu, Sirui Zhao, Ke Li, Xing Sun, Tong Xu, Enhong Chen |
| 출판정보 | National Science Review, 11(12), Article nwae403, 2024 |
| DOI/URL | `https://doi.org/10.1093/nsr/nwae403`; arXiv `https://arxiv.org/abs/2306.13549` |
| 검증 상태 | NSR 2024 공식판 확인. 강의계획서의 `Yongtao Yin et al.` 표기는 공식 저자 목록과 표기가 달라 확인 필요 |

## 2. 한 문장 요약

Multimodal LLM은 image-text alignment, instruction tuning, multimodal benchmark, hallucination 문제가 결합되어 텍스트 LLM보다 더 넓은 공격면을 갖는다[4].

## 3. 연구문제

MLLM의 구조, 학습 전략, 평가 방법, multimodal hallucination, multimodal reasoning 기술을 어떻게 체계화할 수 있는가를 다룬다.

## 4. 핵심 개념

- Architecture: modality encoder, connector, LLM, optional generator.
- Training: alignment pretraining, instruction tuning, multimodal data construction.
- Evaluation: visual QA, hallucination benchmark, multimodal robustness.
- Risk: multimodal prompt injection, visual context leakage, hallucination-driven unsafe answer.

## 5. 보안 관점 분석

P04는 W07의 LLM 보안 평가를 RAG와 multimodal context로 확장하는 연결부다. 이미지, 문서, OCR, GUI context가 prompt와 결합되면 기존 text-only prompt injection보다 검증과 logging이 어려워진다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Multimodal Conditional Generation |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$p_\theta(y\mid x_{text},x_{image})=\prod_t p_\theta(y_t\mid y_{<t},x_{text},x_{image})$$ |
| 기호·입력·출력 | \(x_{text}\): 텍스트 입력, \(x_{image}\): 이미지 입력, \(y_t\): 출력 token |
| 직관적 의미 | Multimodal Conditional Generation는 LLM 보안·프라이버시 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | LLM 보안·프라이버시 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | groundedness, hallucination rate, multimodal ASR |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 참고만 |

## 6. 검증 메모

로컬 PDF 첫 페이지에는 IEEE TPAMI 표기 원고/arXiv가 포함되어 있으나, DOI 기준 공식 출판판은 National Science Review 11(12), Article nwae403이다. `Yongtao Yin` 표기는 확인되지 않았으므로 최종 제출 전 강의계획서 원문 확인이 필요하다.

## 7. 기말 논문 활용

RAG 문서뿐 아니라 이미지·문서·GUI context가 들어오는 AI 시스템의 privacy leakage, hallucination, context injection 위험을 설명할 때 활용한다.
