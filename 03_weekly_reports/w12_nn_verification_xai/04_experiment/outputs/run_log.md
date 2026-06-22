# W12 실험 실행 로그

| 항목 | 내용 |
|---|---|
| 실행일 | 2026-06-22 |
| Seed | 42 |
| 데이터 | synthetic_binary_classification |
| 개인정보 사용 | False |
| 모델 | toy_logistic_classifier |
| epsilon | 0.35 |
| 보안 범위 | synthetic toy robustness/XAI evaluation and formal-bound proxy |
| 제외 범위 | actual safety-critical system attack, production model probing, personal data use |

## 결과 요약

| 조건 | Clean Accuracy | Robust Accuracy | Explanation Stability | Certified Rate | Fairness Gap | Verification Cost ms |
|---|---:|---:|---:|---:|---:|---:|
| Clean model | 0.818750 | 0.543750 | 0.927782 | 0.543750 | 0.039141 | 0.223524 |
| Adversarial input | 0.818750 | 0.543750 | 0.862321 | 0.340625 | 0.039141 | 0.190324 |
| Robust defense | 0.815625 | 0.543750 | 0.927152 | 0.543750 | 0.044823 | 0.191790 |
| XAI stability check | 0.815625 | 0.696875 | 0.976252 | 0.696875 | 0.044823 | 0.193048 |

## 해석 주의

- 이 결과는 synthetic toy classification에서 얻은 교육용 수치다.
- certified rate는 synthetic binary classification 기반 toy logistic classifier의 L-infinity bound proxy이며, 대규모 DNN의 완전한 formal verification 결과가 아니다.
- 실제 안전중요 시스템 공격, 운영 모델 침해, 개인정보 기반 평가는 수행하지 않았다.
