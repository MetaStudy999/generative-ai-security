# W07 Q&A

## Q1. 이 수식이 실제 실험 지표와 어떻게 연결되는가?

A. 핵심 수식은 utility, attack_success_rate, privacy_leakage_rate, code_vulnerability_rate 같은 지표를 해석하는 표준 정식화다. 실제 값은 `04_experiment/outputs/metrics_summary.csv`에서만 가져오며, 수식 자체가 운영 보증을 뜻하지는 않는다.

## Q2. 이 그래프의 수치는 실제 실행 결과인가, 설계 예시인가?

A. 그래프는 `metrics_summary.csv`가 존재하고 numeric 컬럼을 확인한 경우에만 생성했다. CSV에 없는 값은 만들지 않았으며, 산출물이 없을 때는 `design_only / 실행 전 / 확인 필요`로 표시한다.

## Q3. clean accuracy와 보안 지표가 다른 이유는 무엇인가?

A. clean accuracy는 정상 조건의 예측 성능이고, 보안 지표는 공격 조건, 교란 조건, 프라이버시 누출, 재현성 증거처럼 다른 실패 모드를 본다. 둘은 같은 숫자로 합치면 안 된다.

## Q4. 이 주차 내용을 기말논문에 어떻게 반영할 수 있는가?

A. `LLM privacy/safety evaluation flow`를 위협모형 그림으로 쓰고, utility, attack_success_rate, privacy_leakage_rate, code_vulnerability_rate를 평가방법 표에 연결할 수 있다. 단, toy/synthetic 범위와 확인 필요 항목은 한계 절에 남겨야 한다.

## Q5. 현재 한계는 무엇이고 추가 실험은 무엇인가?

A. privacy leakage는 toy/proxy metric이며 실제 개인정보 추출 실험으로 해석하지 않는다. 추가 실험은 run_log.md와 results.json까지 일치하는 조건에서만 확정 수치로 반영한다.

## Q6. 논문 5편 중 핵심 근거는 무엇인가?

A. P01은 핵심 이론, P02는 위협 분류, P03은 평가 지표, P04는 공격·방어 사례, P05는 재현성·정책 근거로 사용한다. 세부 서지와 DOI/URL은 최종 제출 전 원문으로 확인한다.

## Q7. 실제 운영 시스템에 바로 적용할 수 없는 이유는 무엇인가?

A. 발표의 실습과 그림은 public, synthetic, toy, local evaluation 범위다. 운영 적용에는 실제 데이터 거버넌스, 정책 승인, 위협모형 검토, 독립 검증, 법적 검토가 추가로 필요하다.
