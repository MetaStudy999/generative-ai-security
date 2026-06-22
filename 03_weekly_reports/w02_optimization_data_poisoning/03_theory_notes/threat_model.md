# W02 위협모형

## 1. 기본 표

| 항목 | 내용 |
|---|---|
| 대상 시스템 | 지도학습 기반 이미지/표 형식 분류 모델, 예시는 scikit-learn digits 분류 모델 |
| 보호 자산 | 학습 데이터, 라벨, 모델 파라미터, 검증셋, 예측 결과, 학습 로그 |
| 공격자 | 외부 데이터 제공자, 악의적 라벨러, 내부 데이터 파이프라인 접근자, 공급망 기여자 |
| 공격자의 지식 | Black-box, gray-box, white-box로 구분 |
| 공격자의 능력 | 일부 학습데이터 라벨 조작, trigger 삽입, 오염 데이터 업로드, 데이터 provenance 은닉 |
| 공격 경로 | 데이터 수집, 라벨링, 전처리, 학습, fine-tuning, 모델 업데이트 |
| 공격 성공 조건 | clean accuracy 저하 또는 trigger 조건부 목표 오분류 |
| 방어자 가정 | 데이터 검증, 실험 로그 보존, clean/trigger 평가셋 구성, Docker 재실행 가능 |
| 제외 범위 | 실제 운영 시스템 침해, 실제 개인정보 사용, 무단 API 질의, 악성코드 실행, 실제 공격 절차 상세화 |

## 2. 공격 시나리오

| 시나리오 | 공격 목표 | 관찰 지표 | 실습 반영 |
|---|---|---|---|
| Label-flipping poisoning | 전체 성능 또는 특정 클래스 성능 저하 | accuracy drop, macro F1 | 오염률 5%, 10%, 20% 설계 |
| Targeted label manipulation | 특정 클래스를 목표 클래스로 오분류 | targeted error rate | 분석 후보로 기록 |
| Backdoor trigger | 정상 성능 유지, trigger 조건에서 목표 오분류 | clean accuracy, ASR | digits 하단 픽셀 trigger 설계 |
| Data provenance failure | 오염 출처 추적 실패 | 검수 로그, 데이터 해시, 라벨 기록 | 보고서 체크리스트 반영 |

## 3. 방어자 관측 가능성

방어자는 모든 공격 의도를 알 수 없다고 가정한다. 대신 데이터 출처, 라벨 변경 이력, 학습 seed, config, 모델 성능표, trigger 테스트 결과를 관찰할 수 있다. 이 가정은 공격 성공률만 보여주는 실험보다 제출 가능한 보안 평가 프로토콜을 만드는 데 더 적합하다.

## 4. 안전한 toy protocol 경계

W02 실습의 label-flipping과 toy backdoor는 공개 `sklearn.datasets.load_digits` 데이터셋에서 평가 지표를 설명하기 위한 제한된 모의실험이다. 본 문서는 실제 서비스 침해, 무단 API 질의, 개인정보 처리, 악성코드 실행, 운영 환경 공격 절차를 포함하지 않는다. 실험 결과는 실제 공격 성능이 아니라 clean accuracy, macro F1, ASR, 재현성 증거를 분리 기록하는 방법을 보여주는 예시로 해석한다.
