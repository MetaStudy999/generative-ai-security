# P02 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 강의계획서 지정 논문 | Y. Ye et al., A Survey of Watermarking and Fingerprinting Techniques for Deep Learning Models, ACM Computing Surveys, 2024 |
| 현재 로컬 PDF | Yuqing Liang, Jiancheng Xiao, Wensheng Gan, Philip S. Yu, Watermarking Techniques for Large Language Models: A Survey |
| 로컬 PDF URL | `https://arxiv.org/abs/2409.00089`, arXiv:2409.00089v1 |
| 공식 후보 메모 | Peigen Ye et al., "Securing Large Language Models: A Survey of Watermarking and Fingerprinting Techniques", ACM CSUR 2026, DOI `10.1145/3773028`가 확인되지만, 지정 P02와 동일하다고 확정할 수 없다. |
| 검증 상태 | `SUBSTITUTE` PDF. 지정 논문 원문 확보 필요. |

## 2. 필수 주의문

주의: W13의 P02는 지정 논문과 로컬 PDF가 불일치한다. 현재 로컬 PDF는 Yuqing Liang et al.의 LLM watermarking survey이므로, 최종 제출 전 Y. Ye et al.의 deep learning model watermarking/fingerprinting 지정 논문 원문 또는 공식 출판 페이지를 확보해야 한다.

## 3. 한 문장 요약

현재 로컬 PDF는 LLM 워터마킹을 전통적 디지털 워터마킹, 텍스트/멀티모달 생성물 추적, IP 보호, 오남용 추적 관점에서 정리하며, W13의 watermarking/fingerprinting 논의를 LLM 출력 추적 문제로 확장하는 보조 문헌이다[2].

## 4. 연구문제

LLM이 생성한 텍스트, 이미지, 오디오 등에서 출처 추적과 저작권 보호를 어떻게 수행할 수 있는가를 다룬다. 특히 text watermarking의 robustness, semantic invariance, security vulnerability, system consumption 문제가 핵심 한계로 제시된다.

## 5. 핵심 개념

| 개념 | 설명 | W13 연결 |
|---|---|---|
| LLM watermarking | 생성물 또는 모델 출력에 식별 가능한 신호를 삽입하는 기술 | 생성형 AI IP 보호 |
| Traceability | 생성물의 출처 모델을 추적하는 기능 | 책임성 평가 |
| Semantic invariance | 워터마크가 의미 품질을 망가뜨리지 않아야 하는 조건 | utility-protection trade-off |
| Robustness | paraphrasing, clipping, semantic shift에도 검출되는 성질 | false positive/FNR 지표 필요 |

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Watermark Detection TPR/FPR |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$TPR=\frac{TP}{TP+FN},\qquad FPR=\frac{FP}{FP+TN}$$ |
| 기호·입력·출력 | TP: 워터마크 검출, FN: 워터마크 미검출, FP: 비워터마크 오탐, TN: 정상 비검출 |
| 직관적 의미 | Watermark Detection TPR/FPR는 Model Stealing·Watermarking 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Model Stealing·Watermarking 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | watermark detection, false positive rate, utility accuracy |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 참고만 |

## 6. W13 활용

로컬 P02는 지정 논문처럼 인용하지 않는다. W13에서는 LLM watermarking 보조 배경, semantic shift, paraphrasing 공격, detection/FPR 동시 보고 필요성을 설명하는 범위로만 사용한다.

## 7. 한계와 검토 필요

지정 논문 원문 또는 공식 페이지 확보가 필요하다. 최종 제출 전 지정 논문이 확보되지 않으면 참고문헌 표에서 `대체 PDF 상태`와 `원문 확보 필요`를 유지한다.
