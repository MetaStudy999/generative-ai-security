# W01 예상 질문과 답변

## Q1. 왜 딥러닝 원리 발표에서 보안 이야기가 필요한가?

딥러닝의 표현학습, 역전파, 일반화는 보안 공격이 작동하는 기술적 배경이다. adversarial example은 입력 교란으로 결정 경계를 흔들고, privacy attack은 모델이 학습 데이터의 흔적을 얼마나 기억하는지 이용한다. 따라서 원리와 보안은 분리된 주제가 아니라 같은 시스템의 다른 관점이다.

## Q2. Accuracy가 높으면 보안적으로도 좋은 모델 아닌가?

아니다. Accuracy는 정상 조건 성능을 보여주지만, 공격 조건에서의 robust accuracy, 오탐/미탐 비용, privacy leakage 가능성을 설명하지 못한다. W01에서는 clean performance와 robust performance를 분리해서 기록해야 한다고 정리했다.

## Q3. synthetic toy evaluation 결과를 어느 정도까지 주장할 수 있는가?

이번 실습 결과는 실제 운영망 보안성을 대표하지 않는다. 주장할 수 있는 범위는 “평가축을 분리해 기록하는 방식의 예시”와 “라벨 노이즈 또는 입력 교란이 지표에 미치는 방향성 확인” 정도다. 실제 시스템 주장을 하려면 실제 데이터셋, 명확한 공격자 가정, 반복 실험이 필요하다.

## Q4. Privacy-safe audit과 membership inference의 차이는 무엇인가?

Privacy-safe audit은 synthetic data에서 train-test gap과 confidence 신호를 점검하는 안전한 절차다. Membership inference는 특정 샘플이 실제 학습 데이터에 포함됐는지 추론하는 공격이다. 이번 실습은 개인정보와 실제 데이터가 없으므로 membership inference 공격 결과로 해석하지 않는다.

## Q5. ML 생명주기 보증에서 가장 중요한 증거는 무엇인가?

최소 증거는 데이터 출처, 전처리 방식, seed, config, 학습 코드, 평가 코드, 결과 로그, 모델/데이터 버전이다. W01에서는 DOI/URL 검증표, 로컬 PDF 목록, Dockerfile, config, 실행 소스, 결과 파일을 재현성 증거로 보존했다.

## Q6. 기말논문으로 어떻게 이어지는가?

W01의 프레임은 각 주차의 공격과 방어를 데이터 관리, 모델 학습, 검증, 배포·운영 단계에 배치하는 기준이 된다. 기말논문에서는 이를 “ML 생명주기 기반 AI 보안 평가 프레임워크”로 확장할 수 있다.

