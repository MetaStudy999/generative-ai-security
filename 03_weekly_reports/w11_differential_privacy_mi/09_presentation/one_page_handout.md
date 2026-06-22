# W11 1페이지 요약

## 핵심 메시지

DP 보장은 “noise를 넣었다”는 선언이 아니라 accounting, utility, MI risk, leakage, 재현성 로그가 함께 있을 때 해석 가능하다.

## AI 원리

| 개념 | 요점 |
|---|---|
| Differential Privacy | 한 레코드 포함 여부가 출력 분포에 크게 드러나지 않도록 제한 |
| DP-SGD | gradient clipping, noise injection, privacy accounting의 결합 |
| Privacy budget | epsilon/delta와 utility 사이의 trade-off |

## 보안 이슈

| 이슈 | 평가 지표 |
|---|---|
| Membership inference | MI Attack Accuracy |
| Privacy leakage | Privacy Leakage Score |
| Utility cost | Accuracy, Utility Drop |
| Accountability | DOI/PDF 검증, seed/config/output log |

## 실험 결과

| 조건 | Accuracy | MI Attack Accuracy | Epsilon Proxy | Leakage |
|---|---:|---:|---:|---:|
| Non-DP baseline | 0.956250 | 0.515625 | 해당 없음 | 0.014833 |
| DP-like noise low | 0.956250 | 0.515625 | 8.000000 | 0.014494 |
| DP-like noise medium | 0.962500 | 0.512500 | 3.000000 | 0.011769 |
| DP-like noise high | 0.950000 | 0.521875 | 1.000000 | 0.016482 |

## 주의

- `epsilon_proxy`는 정식 DP accountant 값이 아니다.
- `noise_multiplier`는 toy gradient noise scale이며 formal DP-SGD accountant 값이 아니다.
- 결과는 synthetic toy 평가이며 실제 개인정보 보호 수준으로 일반화하지 않는다.
- P03/P05는 로컬 PDF가 대체 문헌이므로 최종 인용 전 원문 PDF 확보가 필요하다.

## 기말논문 연결

W11은 기말논문의 관련연구, 위협모형, 평가방법, 보안적 함의에 연결된다. 핵심 기여 후보는 privacy claim 다중지표 평가 프레임워크다.
