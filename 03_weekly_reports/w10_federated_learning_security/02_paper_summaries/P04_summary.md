# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | The Federation Strikes Back: A Survey of Federated Learning Privacy Attacks, Defenses, Applications, and Policy Landscape |
| 저자 | Joshua C. Zhao et al. |
| 학술지/학회 | ACM Computing Surveys |
| 연도 | 2025 |
| DOI/URL | 10.1145/3724113 |
| PDF 파일명 | 04_Zhao_et_al_2025_Federation_Strikes_Back.pdf |
| 검증 상태 | 로컬 PDF에서 제목과 DOI 확인 |

## 2. 한 문장 요약

> 이 논문은 FL privacy attack, defense, application, policy landscape를 함께 검토하며, 모델 업데이트 공유가 항상 privacy-preserving이라는 전제가 깨질 수 있음을 정리한다.

## 3. 연구문제

이 논문에서 기말 연구와 연결되는 질문은 FL 모델 업데이트에서 어떤 privacy attack이 가능한지, 어떤 방어와 정책 조건이 필요한지다. W10에서는 privacy leakage를 실제 gradient inversion이 아니라 update exposure proxy로 제한해 기록한다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Privacy attack | 모델 업데이트에서 학습 데이터 단서를 추론하는 위협 | privacy leakage proxy |
| Defense method | 업데이트 보호, secure aggregation, DP 등 | 방어 비교 |
| Application lesson | 실제 산업 적용에서 얻은 운영상 제약 | 정책·운영 함의 |
| Policy landscape | 개인정보 보호 규제와 FL 운영 책임 | 기말 논문 보안 함의 |

## 5. 방법론

이 문헌은 privacy attack과 defense를 문헌 기반으로 정리하고, 실제 적용과 정책 환경까지 연결한다. 본 보고서는 이를 privacy 지표를 독립 항목으로 분리해야 하는 근거로 사용한다.

## 6. 주요 결과

FL의 privacy 전제는 업데이트가 private data를 역추론할 수 없을 때만 성립한다. W10 실험은 실제 역추론을 수행하지 않고, update norm 기반 proxy로 위험 신호만 기록한다.

## 7. 보안 관점 분석

이 논문은 Gradient leakage, poisoning, backdoor, privacy attack을 이해하기 위한 배경 문헌으로 활용된다. 공격자의 능력, 방어자의 관측 가능성, 평가 데이터의 한계, 재현성 조건을 함께 정리해야 실제 보안 연구로 이어질 수 있다.

## 8. 한계와 오픈문제

원문 정밀 독해 전에는 세부 실험 설정, 데이터셋, DOI, 인용 관계를 확정할 수 없다. 또한 survey 성격의 문헌은 실제 재현 실험보다는 분류체계와 연구 공백 파악에 더 적합하므로, 기말 논문에서는 별도 평가 프로토콜로 보완해야 한다.

## 9. 기말 논문에 반영할 부분

P04는 FL privacy와 policy landscape를 기말 논문의 보안적 함의 장에 연결한다. 특히 기술적 방어만으로 부족하고 규제·책임성·검증 로그가 함께 필요하다는 논거가 된다.
