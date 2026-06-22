# W01 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 핵심 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | ML 생명주기 기반 AI 보안 평가 프레임워크 | 딥러닝/ML 시스템 전체 생명주기 | 데이터 오염, adversarial example, privacy leakage, 재현성 실패 | 문헌 매트릭스 + 평가 체크리스트 | 높음 |
| 2 | Clean 성능과 보안 강건성을 함께 보는 평가 프로토콜 | 분류/탐지 모델 | 대적 입력, 탐지 오류, 방어 검증 실패 | toy evaluation + 문헌 기반 지표 비교 | 높음 |
| 3 | ML 프라이버시 공격 위험의 생명주기 매핑 | 학습 데이터와 모델 출력 인터페이스 | membership inference, model inversion, property inference | threat model + leakage risk rubric | 보통 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 | W01 근거 |
|---|---|---|
| 서론 | 딥러닝 성능만으로 AI 시스템 보안성을 주장할 수 없다는 문제 제기 | P01-P05 종합 |
| 관련연구 | 딥러닝 원리, ML 생명주기 보증, 침입탐지, 대적 ML, 프라이버시 공격 정리 | 논문 요약 5편 |
| 연구문제 | 생명주기별 보호 자산과 평가 지표를 어떻게 정의할 것인가 | `threat_model.md` |
| 연구방법 | 문헌 매트릭스, 위협모형, 평가 프로토콜, 재현성 체크리스트 | `paper_matrix.md`, `evaluation_protocol.md` |
| 분석/실험 | 공개/synthetic 데이터 기반 safe toy evaluation 설계 | `experiment_report.md` |
| 보안적 함의 | CIA, Privacy, Safety, Accountability 관점으로 평가 결과 해석 | `security_issue_30.md` |
| 결론 | 재현 가능한 AI 보안 평가 절차와 한계 제시 | W01 성찰표 |

## 3. W01에서 기말 논문으로 가져갈 핵심 주장

1. AI 보안 평가는 모델 accuracy가 아니라 생명주기 evidence의 문제다.
2. Robustness와 privacy는 서로 다른 보안 축이므로 한 지표로 합치면 안 된다.
3. Survey 기반 주차라도 DOI, PDF, config, seed, 결과표 상태를 보존하면 재현성 기여를 만들 수 있다.
4. 악용 가능성이 있는 공격은 toy/public data와 방어 중심 평가로 제한해야 한다.
5. P04는 현재 arXiv 대체 논문 기준이므로 최종 논문에서는 강의계획서 지정 IEEE COMST 논문과 동일 여부를 먼저 확정해야 한다.

## 4. 후속 주차 연결 방식

W02 이후 논문은 W01의 생명주기 표에 계속 매핑한다. 예를 들어 data poisoning은 데이터/학습 단계, adversarial vision은 추론/검증 단계, federated learning은 학습/통신 단계, model stealing은 배포/API 단계에 배치한다.

## 5. KCI/SCI 전환 메모

| 구분 | 후보 |
|---|---|
| KCI 국문 제목 | ML 생명주기 기반 AI 보안 평가 프레임워크 연구 |
| KCI 영문 제목 | A Study on an AI Security Evaluation Framework Based on the ML Lifecycle |
| SCI 제목 | A Lifecycle-Based Evaluation Framework for AI Security: Integrating Clean Performance, Robustness, Privacy Leakage, and Reproducibility Evidence |
| 핵심 contribution | clean performance, robust performance, privacy leakage, reproducibility evidence를 분리한 생명주기 기반 평가 구조 |
| 확인 필요 | P04 최종 출판정보, 국내 참고문헌 3편 이상, 공개 저장소 PDF 보관 정책 |
