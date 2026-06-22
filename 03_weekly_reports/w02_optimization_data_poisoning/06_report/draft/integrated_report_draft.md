# W02 통합보고서 초안

이 초안은 `06_report/final/integrated_report_final.md`의 작성 흐름을 보존하기 위한 문서다. 제출 기준은 final 문서를 따른다.

## 핵심 메시지

W02는 대규모 최적화와 데이터 오염 위협을 연결한다. 모델 학습은 데이터와 라벨이 만드는 손실함수를 따라 움직이므로, poisoning은 최적화 경로와 모델 신뢰성을 동시에 흔든다.

## 구성

1. 대규모 최적화, SGD, 일반화, 효율적 학습 정리
2. Data poisoning, label-flipping, backdoor, ASR 정리
3. 논문 5편의 역할 분리
4. 위협모형과 평가 프로토콜 도출
5. Docker 기반 digits toy evaluation 설계
6. 기말 논문 주제 후보 연결

## 초안 상태

| 항목 | 상태 |
|---|---|
| 문헌 요약 | final에 반영 |
| 이론노트 | final에 반영 |
| 실험 코드 | 작성 완료 |
| 정량 실험값 | Docker 실행 완료, `04_experiment/outputs/` 반영 |
| 발표자료 | 별도 `09_presentation/`에 작성 |
