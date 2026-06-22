# W05 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 자기지도학습 기반 AI 시스템의 Poisoning/Backdoor 평가 프레임워크 연구 | SSL/foundation model | Poisoning, Backdoor | 문헌분석 + synthetic representation toy 실험 | 높음 |
| 2 | 표현학습 공간에서 Backdoor Trigger가 공격 성공률과 탐지율에 미치는 영향 분석 | 표현학습 모델 | Trigger injection, representation shift | toy 실험 + 평가 프로토콜 | 보통 |
| 3 | 파운데이션 모델 사전학습 단계의 데이터 오염 위협과 재현성 평가 연구 | foundation/pretraining pipeline | corpus poisoning, data governance risk | 문헌분석 + 체크리스트 | 높음 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | SSL/foundation pretraining에서 representation space가 보안 자산이 되는 이유 |
| 관련연구 | P01-P03 SSL 원리 문헌과 P04-P05 poisoning/backdoor 보안 문헌 연결 |
| 연구문제 | clean accuracy, ASR, representation shift, detection rate, clean FPR 분리 필요성 |
| 위협모형 | pretraining corpus, augmentation pair, learned representation, downstream classifier |
| 연구방법 | 문헌 비교표, synthetic toy protocol, reproducibility evidence checklist |
| 분석/실험 | outputs 기준 clean accuracy 1.000000, ASR 1.000000, ASR after defense 0.000000 등 |
| 보안적 함의 | integrity, robustness, safety, accountability, governance |
| 한계 | toy 실험의 외적 타당성, P02 지정 문헌 동일 여부, PDF 저작권 상태 |

## 3. 반영 가능한 실험 근거

| 근거 파일 | 반영 내용 |
|---|---|
| `04_experiment/outputs/run_log.md` | clean accuracy 1.000000, ASR 1.000000, ASR after defense 0.000000 |
| `04_experiment/outputs/metrics_summary.csv` | 제출 표에 사용할 정량 지표 |
| `04_experiment/outputs/results.json` | config, centroid, 예측 샘플, 방어 플래그 세부 기록 |

이 실험은 실제 SSL/foundation model 성능 주장이 아니라, 기말논문에서 평가 지표와 재현성 기록 형식을 설명하는 안전한 사례로만 활용한다.

## 4. KCI/SCI 전환 메모

| 형식 | 전환 방향 | 확인 필요 |
|---|---|---|
| KCI | 국문 제목, 국문/영문초록, 키워드, 연구문제, 연구방법, 보안적 함의 중심 | 국내 참고문헌 3편 이상 |
| SCI | structured abstract, related work 축, threat model, methodology, experimental setup, threats to validity 중심 | 실제 SSL encoder 확장 실험 여부 |

## 5. 최종 제출 전 확인

- P02가 강의계획서 지정 일반 SSL survey인지 대체 문헌인지 확인한다.
- P03 Article 번호와 P04 제목/저자 표기를 원문 기준으로 확인한다.
- PDF 원문은 public GitHub 저장소에서 제거 또는 추적 해제할지 결정한다.
