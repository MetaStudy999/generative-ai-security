# W05 위협모형

## 1. 대상 시스템

| 항목 | 내용 |
|---|---|
| Target system | self-supervised representation learner, foundation model pretraining pipeline, downstream classifier |
| Protected assets | pretraining corpus, augmentation pairs, learned representation, downstream classifier, trigger behavior, config/log/output evidence |
| Security objective | clean performance와 별도로 trigger 조건의 ASR, representation shift, detection rate, clean FPR을 분리해 기록한다 |
| 안전 범위 | 공개 데이터 또는 synthetic/toy data만 사용한다 |

## 2. 공격자 모델

| 항목 | 내용 |
|---|---|
| 공격자 지식 | black-box, gray-box, white-box, data contributor |
| 공격자 능력 | poisoned sample insertion, trigger injection, augmentation manipulation, corpus contamination |
| 공격 대상 | pretraining data, augmentation/pair construction, representation space, downstream decision boundary |
| 공격 성공 조건 | source-class representation이 target class 방향으로 이동하고 ASR이 증가하되 clean accuracy는 유지될 수 있음 |

## 3. 방어자 가정

| 항목 | 내용 |
|---|---|
| 관측 가능성 | seed, config, outputs, run log, evaluation set, representation distance를 기록할 수 있음 |
| 점검 방식 | representation consistency distance threshold, detection rate, clean false positive rate 분리 보고 |
| 재현성 근거 | `configs/config.yaml`, `src/run_experiment.py`, `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md` |

## 4. 제외 범위

- 실제 서비스 침해
- 실제 개인정보 사용
- 무단 API 대량 질의
- 실제 운영 모델 대상 backdoor 배포
- 악용 가능한 공격 절차의 단계별 구현 설명
- 상용 SSL/foundation model의 보안 성능 일반화 주장

## 5. 연구문제 후보

RQ1. 자기지도학습 기반 AI 시스템에서 poisoning/backdoor 평가를 위한 최소 지표는 무엇인가?

RQ2. Trigger vector는 representation space의 mean shift와 attack success rate에 어떤 영향을 주는가?

RQ3. Consistency defense check는 ASR after defense, detection rate, clean FPR을 어떻게 변화시키는가?

RQ4. P01-P03의 SSL 원리 문헌과 P04-P05의 보안 문헌을 하나의 pretraining lifecycle 위협모형으로 어떻게 연결할 수 있는가?
