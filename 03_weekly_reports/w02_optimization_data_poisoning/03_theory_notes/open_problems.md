# 한계와 오픈문제

## 1. 문헌 측면

- P02와 P04는 로컬 PDF와 지시서 제목/연도/출판 정보가 일부 다르므로 최종 참고문헌 양식에서 출판 판본을 재확인해야 한다.
- Survey 문헌은 taxonomy를 제공하지만, 동일 조건의 재현 실험을 보장하지 않는다.
- LLM backdoor와 데이터 공급망 poisoning은 빠르게 변하는 영역이므로 최신 문헌 보강이 필요하다.

## 2. 실험 측면

- Digits toy 실험은 실제 대규모 모델의 데이터 파이프라인을 대표하지 않는다.
- Label-flipping은 이해하기 쉬운 공격이지만 clean-label poisoning과 공급망 공격의 은닉성을 충분히 설명하지 못한다.
- Backdoor trigger는 안전한 toy 패턴으로 제한되므로 실제 공격 성능으로 일반화할 수 없다.
- Docker 실행으로 정량 결과를 확정했지만, 공개 digits toy 실험의 범위를 넘는 일반화는 제한한다.

## 3. 평가 측면

- Clean accuracy, ASR, detection rate, stealthiness는 함께 봐야 하며 단일 지표로 안전성을 말하기 어렵다.
- 방어 기법은 오탐, 성능 저하, 재학습 비용을 동반할 수 있다.
- 모델 압축과 pruning이 backdoor 제거에 미치는 영향은 데이터셋과 공격 유형에 따라 달라진다.

## 4. 기말 연구로 남길 질문

RQ1. 오염률과 공격 유형이 clean accuracy, macro F1, ASR에 미치는 영향은 어떻게 다른가?

RQ2. Backdoor 방어 평가는 clean accuracy 유지율, ASR 감소, 탐지율, 비용 중 어떤 조합으로 보고해야 하는가?

RQ3. 모델 효율화와 방어 평가를 함께 고려하면 어떤 최소 재현성 패키지가 필요한가?
