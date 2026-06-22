# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions |
| 저자 | Thuy Dung Nguyen et al. |
| 학술지/학회 | Engineering Applications of Artificial Intelligence |
| 연도 | 2024 |
| DOI/URL | arXiv:2303.02213, 출판사 DOI 확인 필요 |
| PDF 파일명 | 05_Nguyen_et_al_2024_FL_Backdoor_Attacks_Defenses.pdf |
| 검증 상태 | 로컬 PDF 첫 페이지에서 arXiv preprint 확인, 출판본 DOI는 최종 대조 필요 |

## 2. 한 문장 요약

> 이 논문은 FL backdoor attack과 defense 연구를 survey하며, 악성 클라이언트 업데이트가 글로벌 모델의 특정 입력 행동을 바꿀 수 있는 위험과 방어 과제를 정리한다.

## 3. 연구문제

이 논문에서 기말 연구와 연결되는 질문은 FL에서 backdoor가 왜 중앙집중 학습보다 검증하기 어려운지, 방어는 clean accuracy와 ASR을 어떻게 동시에 평가해야 하는지다. W10 toy 실험의 ASR 지표는 이 문헌을 직접 반영한다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Backdoor attack | 특정 trigger 입력에서 목표 오동작을 유도하는 공격 | ASR 지표 |
| Malicious client | poisoned update를 제출하는 FL 참여자 | 악성 비율 실험 |
| Stealthiness | clean 성능을 크게 떨어뜨리지 않으면서 backdoor를 유지하는 특성 | clean accuracy와 ASR 동시 해석 |
| Backdoor defense | robust aggregation, update inspection 등 | coordinate median 비교 |

## 5. 방법론

이 문헌은 FL backdoor 공격과 방어를 survey하고, 악성 클라이언트, non-IID 분포, 서버 검증 한계를 함께 논의한다. 본 보고서에서는 악용 가능한 세부 절차 대신 synthetic trigger와 지표 정의만 사용한다.

## 6. 주요 결과

Backdoor 위험은 clean accuracy만으로 드러나지 않는다. W10 실험에서 20% poisoned FedAvg의 clean accuracy는 0.950000으로 비교적 높지만 ASR은 0.496835로 상승한다는 점이 이 문헌의 문제의식과 맞닿아 있다.

## 7. 보안 관점 분석

이 논문은 Gradient leakage, poisoning, backdoor, privacy attack을 이해하기 위한 배경 문헌으로 활용된다. 공격자의 능력, 방어자의 관측 가능성, 평가 데이터의 한계, 재현성 조건을 함께 정리해야 실제 보안 연구로 이어질 수 있다.

## 8. 한계와 오픈문제

원문 정밀 독해 전에는 세부 실험 설정, 데이터셋, DOI, 인용 관계를 확정할 수 없다. 또한 survey 성격의 문헌은 실제 재현 실험보다는 분류체계와 연구 공백 파악에 더 적합하므로, 기말 논문에서는 별도 평가 프로토콜로 보완해야 한다.

## 9. 기말 논문에 반영할 부분

P05는 backdoor threat model과 ASR 평가 지표를 기말 논문의 방법론 장에 연결한다. 특히 defense 비교에서는 clean accuracy만이 아니라 ASR 감소를 함께 기록해야 한다는 근거로 사용한다.
