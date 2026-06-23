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

### 5.1 핵심 수식 또는 알고리즘 설명

이 논문은 수식 자체보다 분류체계, 평가 항목, 운영 절차가 핵심인 survey/review 성격이 강하다. 따라서 원문 기준으로 직접 반영할 핵심 수식은 제한적이다. 대신 본 요약에서는 다음 평가 지표 또는 알고리즘 절차를 개념 수준으로 정리한다.

| 항목 | 내용 |
|---|---|
| 핵심 절차/지표 | Adaptive Watermark 평가 절차 |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 보안 관점 해석 | Model Stealing·Watermarking 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | watermark detection, FPR, extraction fidelity, utility accuracy |
| 기말 논문 반영 여부 | 반영 |
| 절차 요약 | 1. 기준 utility를 먼저 측정<br>2. 워터마크 검출 조건을 사전에 정의<br>3. extraction 또는 distillation 조건 후 검출률과 FPR 비교<br>4. utility loss와 query budget을 함께 기록 |
| 기호·입력·출력 | 입력: 모델 출력·검출 조건·평가셋, 출력: 검출률/FPR/utility loss |
| 직관적 의미 | Adaptive Watermark 평가 절차는 Model Stealing·Watermarking 평가에서 수식보다 분류·운영·검증 흐름을 명시하는 데 초점을 둔다. |
| 한계와 가정 | survey/review 성격의 절차 요약이며, 원문 분류표의 세부 절·쪽 번호는 확인 필요다. |

## 6. W13 활용

본 보고서의 toy 실험은 ModelShield의 아이디어를 binary trigger-set ownership check로 단순화한다. 이 단순화는 실제 LLM watermarking scheme이 아니므로, `watermark detection = 1.000000`을 소유권 확정으로 해석하지 않는다.

## 7. 한계와 검토 필요

LLM 워터마크가 법적 소유권 증거로 충분한지, 공격자가 워터마크 신호를 제거하거나 희석할 때 검출 기준을 어떻게 정할지는 계속 남는 문제다. W13은 이 한계를 false positive proxy 0.600000으로 명시한다.
