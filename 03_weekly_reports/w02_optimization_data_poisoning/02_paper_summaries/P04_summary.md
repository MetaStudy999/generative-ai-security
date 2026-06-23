# P04 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 현재 로컬 논문 제목 | Wild Patterns Reloaded: A Survey of Machine Learning Security against Training Data Poisoning |
| 강의계획서 지정 제목 | Training Data Poisoning Attacks and Defenses: A Systematic Review |
| 저자 | Antonio Emanuele Cina, Kathrin Grosse, Ambra Demontis, Sebastiano Vascon, Werner Zellinger, Bernhard A. Moser, Alina Oprea, Battista Biggio, Marcello Pelillo, Fabio Roli |
| 학술지/학회 | ACM Computing Surveys |
| 권호/쪽 | 55(13s), 1-39 |
| 연도 | 2023 |
| DOI/URL | DOI: `10.1145/3585385`; arXiv: `https://arxiv.org/abs/2205.01992` |
| PDF 파일명 | `04_Cina_et_al_2023_Wild_Patterns_Reloaded_Poisoning_Survey.pdf` |
| 검증 상태 | DOI 기준 ACM 최종판 확인 완료. 단, 강의계획서 지정 제목과 동일 논문/이전 제목인지 최종 확인 필요 |

## 2. 판본 주의

주의: W02의 P04는 강의계획서 지정 논문인 "Training Data Poisoning Attacks and Defenses: A Systematic Review"와 현재 로컬 PDF "Wild Patterns Reloaded"의 동일 여부를 최종 확인해야 한다. 최종 제출 전 출판사 DOI와 판본을 재검증한다.

현재 확인 가능한 근거로는 `Wild Patterns Reloaded`가 Antonio Emanuele Cina et al.의 ACM Computing Surveys 2023 논문이며 DOI는 `10.1145/3585385`이다. 강의계획서 지정 제목과 완전히 같은 제목의 ACM CSUR 출판물은 확인하지 못했으므로, 본 보고서에서는 현재 P04를 대체/판본 확인 필요 문헌으로 표시한다.

## 3. 한 문장 요약

이 논문은 훈련 데이터 poisoning 공격과 방어를 threat model 중심으로 체계화하며, 공격 목표와 방어 위치를 구분해 실제 평가 프로토콜을 설계할 수 있게 해준다[4].

## 4. 연구문제

훈련 데이터는 모델 업데이트의 근거이기 때문에 공격자가 데이터 일부를 조작하면 모델의 성능, 무결성, 안전성이 흔들릴 수 있다. 이 논문은 poisoning 공격과 방어가 축적된 연구 흐름 속에서 어떻게 분류되는지, 어떤 한계와 공백이 남아 있는지를 정리한다.

## 5. 핵심 개념

| 개념 | 설명 | W02 연결 |
|---|---|---|
| Threat model | 공격자 목표, 지식, 능력, 제약을 명시하는 틀 | 기말 연구 위협모형 |
| Untargeted poisoning | 전체 모델 성능 저하를 목표로 하는 공격 | 오염률별 accuracy drop |
| Targeted poisoning | 특정 샘플/클래스 오분류를 목표로 하는 공격 | ASR 및 targeted success |
| Clean-label poisoning | 라벨을 바꾸지 않고 데이터 자체를 조작 | 탐지 난이도와 은닉성 |
| Defense taxonomy | 데이터 정제, robust learning, 검증, 모니터링 | 방어 평가표 |

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Label-flip 또는 Poisoning Rate |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$PoisonRate=\frac{\lvert D_{poison}\rvert}{\lvert D_{clean}\cup D_{poison}\rvert}$$ |
| 기호·입력·출력 | \(D_{poison}\): 오염 또는 라벨 변경 샘플, \(D_{clean}\): 정상 샘플 |
| 직관적 의미 | Label-flip 또는 Poisoning Rate는 최적화·데이터 오염 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | 최적화·데이터 오염 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | poison rate, accuracy drop, target failure rate, ASR |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 방법론

논문은 poisoning 연구를 공격 목표, 적용 도메인, 공격자 지식, 공격 비용, 방어 전략으로 정리한다. 본 보고서에서는 이 틀을 사용해 공격-방어 매트릭스를 만들고, 안전한 toy 실습은 label-flipping과 toy backdoor trigger 개념 수준으로 제한한다.

## 7. 주요 결과

Poisoning 방어는 모델 학습 후 성능만 보는 것으로 충분하지 않다. 데이터 수집 단계에서의 provenance, 라벨 검증, 이상치 탐지, 학습 중 모니터링, 배포 후 trigger 테스트가 함께 필요하다. 특히 정상 테스트셋에서 성능이 유지된다는 사실은 backdoor 부재를 보장하지 않는다.

## 8. 보안 관점 분석

P04는 W02의 실습 설계와 제출 보고서에서 가장 직접적인 보안 프레임을 제공한다. 공격을 실행 절차로 상세화하기보다, 공격 성공 조건과 방어자의 관측 가능성을 표로 정리하는 방식이 연구윤리와 과제 목적에 맞다.

## 9. 한계와 오픈문제

Survey가 주로 기존 연구의 taxonomy를 제공하므로, 특정 모델과 데이터셋에서 방어가 얼마나 안정적인지는 별도 실험이 필요하다. 또한 vision 중심 연구가 다른 모달리티, LLM, RAG 데이터 파이프라인으로 일반화되는지는 추가 검토가 필요하다. 추가로, 강의계획서 지정 제목과 현재 로컬 PDF 제목 표기 차이가 있어 최종 제출 전 문헌 패킷 판본 확인이 필요하다.

## 10. 기말 논문에 반영할 부분

P04는 기말 논문의 관련연구와 방법론 장에 반영한다. 특히 데이터 생명주기 기반 poisoning 방어 체크리스트와 clean accuracy-ASR-stealthiness-detection rate의 다중지표 평가체계로 연결한다.
