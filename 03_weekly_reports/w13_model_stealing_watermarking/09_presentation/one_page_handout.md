# W13 1페이지 요약

## 핵심 메시지

모델 추출 위험은 victim/substitute 출력 일치율인 fidelity로 보고, 워터마크 기반 소유권 검증은 detection rate와 false positive rate를 함께 봐야 한다.

## 핵심 개념

| 개념 | 의미 |
|---|---|
| Model IP | 파라미터, 구조, 학습 데이터, 출력 행동, 생성물 출처에 담긴 지식재산 |
| Model extraction | query-response 쌍으로 원 모델 행동을 근사하는 대체 모델 학습 |
| Watermarking | 모델 또는 생성물에 소유권 검증 신호를 삽입하는 기술 |
| Extraction fidelity | victim과 substitute의 출력 일치율 |
| False positive | 무관 모델이 워터마크 signature와 우연히 일치하는 경우 |

## 실험 결과

| 조건 | Query Budget | Fidelity | Detection | FPR |
|---|---:|---:|---:|---:|
| Substitute query 100 | 100 | 0.864000 | 0.700000 | 0.600000 |
| Substitute query 500 | 500 | 0.920000 | 1.000000 | 0.600000 |
| Substitute query 1000 | 1000 | 0.902000 | 1.000000 | 0.600000 |

Baseline victim utility accuracy는 0.868000이다. 실험은 synthetic toy 환경에서만 수행했으며 실제 API, 실제 LLM, 개인정보, 무단 질의는 포함하지 않는다.

## 토론 포인트

1. Detection이 높고 FPR도 높을 때 소유권 검증 기준은 어떻게 잡아야 하는가?
2. Query budget을 보고할 때 공격 재현성과 악용 방지 사이의 균형은 어디에 둘 것인가?
3. P02/P05처럼 대체 PDF가 있을 때 최종 참고문헌 검증표에는 무엇을 남겨야 하는가?

## 기말논문 연결

“모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크”로 발전시킬 수 있다. 핵심 지표는 fidelity, query cost, detection, false positive, utility, reproducibility다.
