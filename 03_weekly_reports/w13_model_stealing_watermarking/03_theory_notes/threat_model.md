# W13 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | 공개 API 또는 제한된 인터페이스로 제공되는 ML/LLM/생성모형 서비스 |
| 보호 자산 | 모델 파라미터, 모델 행동, 학습된 결정경계, 워터마크, fingerprint, 생성물 출처, API 로그 |
| 공격자 | 외부 질의자, 경쟁 서비스 운영자, 모델 추출 시도자, 워터마크 제거·희석 시도자 |
| 공격자의 지식 | Black-box 또는 제한적 gray-box. W13 실습은 로컬 synthetic black-box query-response만 가정 |
| 공격자의 능력 | 반복 질의, 입력-출력 쌍 수집, substitute model 학습, watermark removal 또는 imitation |
| 공격 경로 | 공개 API, query-response 로그, 생성물, 배포 모델, imitation training data |
| 공격 성공 조건 | 높은 fidelity의 substitute model 생성, watermark inheritance 또는 forgery, ownership ambiguity 발생 |
| 방어/검증 | watermark detection, trigger-set verification, false positive controls, query rate monitoring, provenance logs |
| 제외 범위 | 실제 상용 API extraction, 무단 대량 질의, 실제 모델 탈취, 개인정보 사용, live model theft |

## 연구문제 후보

1. Query-response 정보만으로 모델 행동은 어느 정도 모방될 수 있는가?
2. Extraction fidelity와 substitute accuracy는 각각 무엇을 의미하는가?
3. Watermark detection이 높아도 false positive가 높으면 왜 소유권 증거가 약한가?
4. 모델 IP 보호에서 utility, detection, FPR, query cost는 어떤 trade-off를 만드는가?
5. W13의 synthetic toy 실험을 KCI 또는 SCI 논문 주제로 발전시키려면 어떤 연구문제가 적절한가?

## W13 실습 범위

본 실습은 실제 API가 아닌 synthetic binary classification 기반 안전 toy 실험이다. 공격자는 `src/run_experiment.py`가 만든 query-response pairs만 보고 1-nearest-neighbor substitute model을 구성한다. `query_response_1nn_classifier`는 실제 model extraction 공격 구현이 아니라 toy substitute model이며, `trigger_set`은 실제 watermarking scheme이 아니라 deterministic toy ownership signal이다.

이 결과는 synthetic binary classification 기반 toy 실험의 평가 형식 검증용 수치이며, 실제 상용 API, 실제 LLM, 실제 모델 탈취, 무단 대량 질의, 개인정보 기반 모델 추출 또는 소유권 분쟁 증거로 일반화하지 않는다.
