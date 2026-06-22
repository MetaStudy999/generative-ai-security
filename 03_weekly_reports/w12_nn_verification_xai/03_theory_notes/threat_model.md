# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | deep learning classifier, XAI explanation module, neural network verification pipeline |
| 보호 자산 | model prediction, robustness certificate, explanation output, fairness metric, verification log |
| 공격자 지식 | white-box, gray-box, black-box를 구분하되 W12 실험은 실제 공격 수행이 아니라 toy proxy만 사용 |
| 공격자 능력 | input perturbation, explanation manipulation, evaluation setting manipulation |
| 공격 경로 | 입력 데이터, 설명 모듈, 검증 설정, 평가 로그, 보고서 해석 |
| 공격 성공 조건 | 예측 변화, 설명 변화, robustness 과장, fairness gap 증가, 검증 누락 |
| 방어/점검 | robust training proxy, XAI stability check, bound-based certified-rate proxy, fairness-gap reporting, reproducibility evidence |
| 제외 범위 | actual safety-critical system attack, production model compromise, personal data evaluation, operational adversarial testing, unauthorized probing |

## 연구문제 후보

RQ1. AI 보안 평가에서 clean accuracy, robust accuracy, certified rate, explanation stability를 함께 보고해야 하는 이유는 무엇인가?

RQ2. Robust defense 조건은 clean accuracy, robust accuracy, certified rate, fairness gap에 어떤 trade-off를 만드는가?

RQ3. XAI stability check는 모델의 accountability 평가에 어떤 추가 정보를 제공하는가?

## 해석 주의

W12 실험의 adversarial input은 실제 공격 절차가 아니다. `certified_rate`도 toy 선형 모델의 bound proxy이며 formal DNN verification으로 해석하지 않는다.
