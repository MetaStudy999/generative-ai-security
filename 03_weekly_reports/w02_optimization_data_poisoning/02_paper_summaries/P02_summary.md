# P02 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better |
| 저자 | Gaurav Menghani |
| 학술지/학회 | ACM Computing Surveys |
| 권호/쪽 | 55(12), 1-37 |
| 연도 | 2023 |
| DOI/URL | DOI: `10.1145/3578938`; arXiv: `https://arxiv.org/abs/2106.08962` |
| PDF 파일명 | `02_Menghani_2023_Efficient_Deep_Learning_Survey.pdf` |
| 검증 상태 | ACM 최종판 DOI 확인 완료. Article 번호는 ACM 원문 페이지에서 확인 필요 |

## 2. 판본 메모

- arXiv 판본은 2021년 `arXiv:2106.08962`로 확인된다.
- ACM Computing Surveys 최종판은 DOI `10.1145/3578938`, 55(12), 1-37, 2023으로 확인했다.
- 강의계획서의 `Gulzar Menghani` 표기는 출판 정보 기준 저자명 `Gaurav Menghani`와 다르므로 최종 제출 전 강의자료 오탈자 여부를 사람이 확인한다.

## 3. 한 문장 요약

이 논문은 딥러닝 모델을 작고 빠르고 효율적으로 만들기 위한 압축, 아키텍처, 학습, 시스템, 하드웨어 기법을 정리하며, 정확도-비용-속도 trade-off를 보안 평가와 함께 기록해야 함을 시사한다[2].

## 4. 연구문제

딥러닝 모델은 성능이 좋아질수록 파라미터 수, 지연시간, 메모리, 학습 비용이 증가한다. 이 논문은 품질 지표뿐 아니라 footprint metric을 함께 고려해 모델 효율성을 어떻게 개선할 수 있는지를 다룬다.

## 5. 핵심 개념

| 개념 | 설명 | W02 연결 |
|---|---|---|
| Model efficiency | 정확도와 함께 지연시간, 메모리, 연산량, 에너지 비용을 줄이는 목표 | 효율화가 보안 검증 예산과 모니터링 범위에 영향 |
| Compression | pruning, quantization, distillation 등 모델 크기 축소 기법 | 방어 모델 또는 탐지기의 경량화와 연결 |
| Efficient training | 학습 시간과 자원 사용량을 줄이는 기법 | poisoning 탐지와 재학습 비용 산정에 필요 |
| Deployment constraint | edge, mobile, cloud 등 환경 제약 | 방어 기법이 실제 배포 가능한지 평가 |
| Quality-footprint trade-off | 품질과 비용 사이의 균형 | clean accuracy만으로 모델 선택 불가 |

## 6. 방법론

논문은 효율적 딥러닝 기술을 survey 형태로 묶고, 모델링 기법부터 하드웨어 지원까지 넓은 범위를 정리한다. 본 보고서에서는 모델 효율화 자체보다 "효율화된 모델이 poisoning/backdoor 방어에 어떤 제약을 만드는가"에 초점을 둔다.

## 7. 주요 결과

효율성은 단순히 모델 크기를 줄이는 문제가 아니라 모델 구조, 학습 과정, 추론 시스템, 하드웨어까지 포함한 다층 문제다. 따라서 보안 평가도 정확도와 공격 성공률만이 아니라 방어 비용, 탐지 지연시간, 재학습 가능성, 배포 환경을 함께 기록해야 한다.

## 8. 보안 관점 분석

효율화는 양면적이다. 작은 모델은 배포와 반복 평가가 쉬워질 수 있지만, pruning이나 quantization이 backdoor trigger의 잔존 여부, 이상 탐지 민감도, robust accuracy에 영향을 줄 수 있다. 또한 방어자는 무제한 자원을 가진 것이 아니므로 poisoning 탐지와 재학습 비용을 평가 프로토콜에 포함해야 한다.

## 9. 한계와 오픈문제

이 논문은 효율적 딥러닝 전반을 다루므로 poisoning과 backdoor에 특화된 정량 결과는 제한적이다. 기말 연구에서는 압축/경량화 조건에서 clean accuracy와 ASR이 어떻게 함께 변하는지 별도 실험 또는 문헌 대조가 필요하다.

## 10. 기말 논문에 반영할 부분

P02는 기말 논문의 평가 지표 확장에 반영한다. 구체적으로 accuracy, ASR, detection rate 외에 model size, inference latency, retraining cost, audit cost를 함께 기록하는 다중지표 평가표의 근거로 사용한다.
