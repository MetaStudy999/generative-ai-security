# W05 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 자기지도학습/파운데이션 모델 및 Poisoning/Backdoor 생명주기 보안 평가 프레임워크 | AI/ML 시스템 | Self-supervised pretraining 단계의 공격면, 데이터 오염과 표현공간 왜곡 | 문헌분석 및 체크리스트 | 높음 |
| 2 | 자기지도학습/파운데이션 모델 및 Poisoning/Backdoor 환경의 공격-방어-평가 분류체계 | 모델/데이터/평가 파이프라인 | 표현공간 오염, poisoning, backdoor, 데이터 거버넌스 | 비교분석 | 높음 |
| 3 | 자기지도학습의 정의, Contrastive learning 기반 보안 재현성 평가 연구 | 공개 또는 synthetic 실험 | Self-supervised pretraining 단계의 공격면, 데이터 오염과 표현공간 왜곡 | toy 실험 설계 | 보통 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | 자기지도학습/파운데이션 모델 및 Poisoning/Backdoor의 보안 평가 필요성 |
| 관련연구 | 자기지도학습, contrastive learning, masked modeling, representation learning 및 표현공간 오염, poisoning, backdoor, 데이터 거버넌스 문헌 정리 |
| 연구문제 | 생명주기 기반 위협모형과 평가방법 필요성 |
| 연구방법 | 문헌 비교표, 위협모형, 평가 프로토콜 |
| 분석/실험 | synthetic 2D representation toy 실험 결과와 체크리스트 기반 평가 |
| 보안적 함의 | CIA, Privacy, Safety, Accountability 관점 |
| 결론 | 재현 가능한 AI 보안 평가체계 제안 |

## 3. 반영 가능한 실험 근거

| 근거 파일 | 반영 내용 |
|---|---|
| `04_experiment/outputs/run_log.md` | clean accuracy 1.000000, ASR 1.000000, ASR after defense 0.000000 |
| `04_experiment/outputs/metrics_summary.csv` | 제출 표에 사용할 정량 지표 |
| `04_experiment/outputs/results.json` | config, centroid, 예측 샘플, 방어 플래그 세부 기록 |

이 실험은 실제 SSL/foundation model 성능 주장이 아니라, 기말논문에서 평가 지표와 재현성 기록 형식을 설명하는 안전한 사례로만 활용한다.
