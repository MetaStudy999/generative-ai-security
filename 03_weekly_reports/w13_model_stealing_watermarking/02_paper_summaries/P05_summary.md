# P05 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 강의계획서 지정 논문 | Cheng/Chenhan Zhang et al., Generative Adversarial Networks: A Survey on Attack and Defense, ACM Computing Surveys, 2023 |
| 공식 지정 후보 | Chenhan Zhang, Shui Yu, Zhiyi Tian, James J. Q. Yu, "Generative Adversarial Networks: A Survey on Attack and Defense Perspective" |
| 공식 후보 DOI/출판정보 | DOI `10.1145/3615336`, ACM Computing Surveys, Vol. 56, Issue 4, pp. 1-35, online 2023-11-10, print 2024-04-30 |
| 현재 로컬 PDF | Zhipeng Cai, Zuobin Xiong, Honghui Xu, Peng Wang, Wei Li, Yi Pan, "Generative Adversarial Networks: A Survey Towards Private and Secure Applications", arXiv:2106.03785v1 |
| 검증 상태 | 관련 논문 PDF. 지정 후보 공식 DOI는 확인했지만 로컬 PDF와 표기 차이. |

## 2. 필수 주의문

주의: W13의 P05는 지정 논문과 로컬 PDF가 표기 차이가 있다. 현재 로컬 PDF는 Zhipeng Cai et al.의 GAN privacy/security application survey이므로, 최종 제출 전 Cheng/Chenhan Zhang et al.의 GAN attack/defense 지정 논문 원문 또는 공식 출판 페이지를 확보해야 한다.

## 3. 한 문장 요약

현재 로컬 PDF는 GAN의 game-theoretic generation 구조가 privacy/security 응용과 공격면에 어떻게 연결되는지 정리하며, W13에서는 생성모형 IP 보호와 misuse 위험을 보조적으로 설명하는 관련 보조 문헌 역할을 한다[5].

## 4. 연구문제

GAN이 데이터 생성, 개인정보 보호, 보안 응용에 어떤 가능성을 제공하는지와 동시에 어떤 공격·오용 가능성을 갖는지를 다룬다. W13의 중심인 모델 추출/워터마킹과 직접 일치하지는 않지만 생성모형 보호 자산을 넓히는 배경으로 쓸 수 있다.

## 5. 핵심 개념

| 개념 | 설명 | W13 연결 |
|---|---|---|
| GAN | generator와 discriminator의 경쟁적 학습 구조 | 생성모형 배경 |
| Privacy/security applications | 합성 데이터, 보안 데이터 생성, 탐지 보조 등 | synthetic 실습 근거 |
| Attack surface | 생성모형의 오용, 데이터 누출, 보안 우회 가능성 | 보안적 함의 |
| Provenance | 생성물 출처 추적과 책임성 | watermark/fingerprint 논의 |

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | GAN Security Utility Objective |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$Risk=\alpha PrivacyLeakage+\beta AttackSuccess+\gamma UtilityLoss$$ |
| 기호·입력·출력 | PrivacyLeakage: 민감정보 노출 위험, AttackSuccess: 안전 실패율, UtilityLoss: 품질/성능 손실 |
| 직관적 의미 | GAN Security Utility Objective는 Model Stealing·Watermarking 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Model Stealing·Watermarking 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | FID, privacy risk, attack success, detection rate |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 참고만 |

## 6. W13 활용

로컬 P05는 지정 논문처럼 인용하지 않는다. W13에서는 생성모형도 모델 IP, provenance, privacy/security risk 관리 대상이라는 보조 배경으로만 사용한다.

## 7. 한계와 검토 필요

로컬 PDF의 ACM/JACM placeholder DOI는 공식 인용에 사용하지 않는다. 최종 제출에서는 지정 후보 DOI `10.1145/3615336`와 강의계획서의 `Cheng Zhang` 표기 차이를 사람이 확인해야 한다.
