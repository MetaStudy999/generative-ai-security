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

## 6. W13 활용

로컬 P02는 지정 논문처럼 인용하지 않는다. W13에서는 LLM watermarking 보조 배경, semantic shift, paraphrasing 공격, detection/FPR 동시 보고 필요성을 설명하는 범위로만 사용한다.

## 7. 한계와 검토 필요

지정 논문 원문 또는 공식 페이지 확보가 필요하다. 최종 제출 전 지정 논문이 확보되지 않으면 참고문헌 표에서 `대체 PDF 상태`와 `원문 확보 필요`를 유지한다.
