# W03 평가방법

## 1. 평가 원칙

비전 모델 보안 평가는 정상 조건 성능과 공격 조건 성능을 분리해 기록해야 한다. clean accuracy 하나만으로는 입력 교란, transfer attack, physical attack, 3D perception failure 같은 보안 위험을 설명할 수 없다.

## 2. 핵심 지표

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | W03 상태 |
|---|---|---|---|---|
| Clean Performance | Accuracy, Macro F1 | 정상 입력에서 기준 모델 평가 | 공개 또는 synthetic 데이터 | 실행 완료 |
| Robust Performance | Robust accuracy | perturbation 입력에서 성능 평가 | 변형 입력 | 실행 완료 |
| Attack Impact | ASR, robust drop | clean에서 맞던 샘플이 공격 조건에서 실패하는지 확인 | clean/adversarial paired data | 실행 완료 |
| Error Direction | Confusion matrix | 오류 방향과 label flip 확인 | true/pred label | 실행 완료 |
| Defense/Check | defended accuracy, ASR | feature squeezing 등 점검 조건 평가 | 방어/점검 후 입력 | 실행 완료 |
| Reproducibility | seed, config, Docker, CSV/JSON/log, PGM | 산출물 존재와 수치 정합성 확인 | 실행 로그 | 실행 완료 |
| Human Review | DOI/URL, 저작권, 인용 대응 | 사람이 최종 대조 | DOI/출판사/로컬 파일 | 검토 필요 |

## 3. condition 이름 대응

| 코드 condition | 보고서 표시명 | 지표 해석 |
|---|---|---|
| `clean_baseline` | Clean baseline | clean accuracy와 macro F1 |
| `centroid_direction_linf` | Adversarial perturbation | robust accuracy, ASR, robust drop |
| `adversarial_with_feature_squeeze` | Feature squeezing check | 방어/점검 조건의 accuracy, ASR |

## 4. W03 outputs 기준 결과

| 조건 | Epsilon | N | Accuracy | Macro F1 | ASR | Robust Drop | Confusion Matrix |
|---|---:|---:|---:|---:|---:|---:|---|
| Clean baseline | 0.00 | 120 | 1.000000 | 1.000000 | N/A | 0.000000 | `[[60, 0], [0, 60]]` |
| Adversarial perturbation | 0.05 | 120 | 1.000000 | 1.000000 | 0.000000 | 0.000000 | `[[60, 0], [0, 60]]` |
| Adversarial perturbation | 0.15 | 120 | 1.000000 | 1.000000 | 0.000000 | 0.000000 | `[[60, 0], [0, 60]]` |
| Adversarial perturbation | 0.30 | 120 | 1.000000 | 1.000000 | 0.000000 | 0.000000 | `[[60, 0], [0, 60]]` |
| Adversarial perturbation | 0.45 | 120 | 0.000000 | 0.000000 | 1.000000 | 1.000000 | `[[0, 60], [60, 0]]` |
| Feature squeezing check | 0.30 | 120 | 1.000000 | 1.000000 | 0.000000 | 0.000000 | `[[60, 0], [0, 60]]` |

## 5. 해석과 한계

epsilon 0.45의 성능 급락은 synthetic two-class toy decision boundary 전환이다. 실제 CNN/ViT/3D perception robustness를 대표하지 않는다. W03 평가방법의 핵심은 공격 성능을 주장하는 것이 아니라 clean performance, attack impact, defense/check, reproducibility evidence를 분리해 기록하는 것이다.
