# P04 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack |
| 저자 | Kaiyi Pang, Tao Qi, Chuhan Wu, Minhao Bai, Minghu Jiang, Yongfeng Huang |
| 학술지 | IEEE Transactions on Information Forensics and Security |
| 공식 출판정보 | Vol. 20, pp. 1767-1782, 2025 |
| DOI/URL | `10.1109/TIFS.2025.3530691`, `https://ieeexplore.ieee.org/document/10843740/`, `https://arxiv.org/abs/2405.02365` |
| arXiv판 | arXiv:2405.02365v4, last revised 2025-01-12 |
| 검증 상태 | IEEE TIFS DOI/권호/쪽/연도 확인 완료. arXiv판과 출판판 제목·저자 일치. |

## 2. arXiv판과 출판판 대조

| 항목 | arXiv v4 | IEEE TIFS 출판판 |
|---|---|---|
| 제목 | ModelShield: Adaptive and Robust Watermark against Model Extraction Attack | ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack |
| 저자 | Kaiyi Pang 외 5인 | Kaiyi Pang 외 5인 |
| 연도 | 2024 최초 제출, v4 2025-01-12 | 2025 |
| DOI | `10.48550/arXiv.2405.02365` | `10.1109/TIFS.2025.3530691` |

## 3. 한 문장 요약

ModelShield는 LLM model extraction으로 생성된 imitation model에 워터마크 신호가 남도록 self-watermarking과 robust detection을 결합해, 추출 이후 ownership check를 가능하게 하려는 접근이다[4].

## 4. 연구문제

LMaaS 환경에서 공격자가 victim LLM의 출력을 모아 imitation model을 학습할 때, 원 모델의 IP 침해를 나중에 어떻게 검출할 수 있는가가 중심 질문이다. 또한 워터마크가 생성 품질을 떨어뜨리지 않고 adversarial editing/dilution에도 남는지가 중요하다.

## 5. 핵심 개념

| 개념 | 설명 | W13 연결 |
|---|---|---|
| Model extraction attack | victim 출력으로 imitation model을 학습하는 공격 | query-response 학습 |
| Self-watermarking | LLM이 출력 생성 과정에서 watermark를 자체 삽입하도록 유도 | adaptive watermark 배경 |
| Robust detection | 편집·희석 공격 후에도 신호를 탐지하는 검출 | detection after extraction |
| False positive control | 무관 모델까지 소유 모델로 판단하지 않도록 하는 대조군 | W13 FPR 해석 |

## 6. W13 활용

본 보고서의 toy 실험은 ModelShield의 아이디어를 binary trigger-set ownership check로 단순화한다. 이 단순화는 실제 LLM watermarking scheme이 아니므로, `watermark detection = 1.000000`을 소유권 확정으로 해석하지 않는다.

## 7. 한계와 검토 필요

LLM 워터마크가 법적 소유권 증거로 충분한지, 공격자가 워터마크 신호를 제거하거나 희석할 때 검출 기준을 어떻게 정할지는 계속 남는 문제다. W13은 이 한계를 false positive proxy 0.600000으로 명시한다.
