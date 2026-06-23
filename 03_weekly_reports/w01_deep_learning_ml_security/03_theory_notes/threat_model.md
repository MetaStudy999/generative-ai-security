# W01 위협모형

## 0. 문서 목적

이 문서는 W01의 통합 위협모형을 정의한다. 대상은 단일 딥러닝 모델이 아니라 **데이터 수집 → 전처리 → 학습 → 검증 → 배포 → 추론 → 모니터링**으로 이어지는 ML 생명주기 전체다.

---

## 1. 대상 시스템

W01의 대상은 딥러닝 또는 일반 ML 모델을 포함한 보안 응용 시스템이다. 단일 모델만 보지 않고 데이터 수집, 전처리, 학습, 검증, 배포, 추론, 모니터링으로 이어지는 생명주기 전체를 분석 단위로 둔다.

```text
Data → Preprocessing → Training → Verification → Deployment → Inference → Monitoring
```

---

## 2. 보호 자산

| 자산 | 설명 | 대표 위협 | 관련 논문 |
|---|---|---|---|
| 학습 데이터 | 원본 데이터, 라벨, 전처리 결과 | poisoning, privacy leakage, label noise | P01, P02, P05 |
| 모델 파라미터 | 학습된 가중치와 구조 정보 | model extraction, inversion, backdoor | P01, P05 |
| 입력 데이터 | 추론 시 들어오는 샘플, 로그, 패킷, 이미지 | adversarial example, evasion | P03, P04 |
| 출력 정보 | 클래스, confidence, embedding, 설명 결과 | membership inference, confidence leakage | P05 |
| 평가셋 | 성능 검증에 쓰이는 데이터와 라벨 | benchmark contamination, metric gaming | P02, P03 |
| 운영 로그 | 학습·배포·추론 기록 | 사고 추적 실패, 재현성 훼손 | P02 |
| 배포 파이프라인 | 모델 registry, config, Docker, CI/CD, 모니터링 | misconfiguration, supply-chain risk | P02, W14 |

---

## 3. 공격자 가정

| 구분 | 공격자 지식 | 공격자 능력 | 공격자 목표 | 예시 |
|---|---|---|---|---|
| White-box | 모델 구조, 파라미터, 학습 절차를 안다. | gradient 계산, 내부 상태 분석 | 최적 교란, 정보추출 | 연구실 평가, 내부자 위협 |
| Gray-box | 일부 구조나 출력, 데이터 분포를 안다. | 반복 질의, 대체 모델 구성 | 모델 동작 추론, 우회 | API 관찰 기반 공격 |
| Black-box | 입력과 출력만 관찰한다. | 질의 반복, 출력 비교 | evasion, membership inference | 외부 서비스 사용자 |
| Data contributor | 학습 데이터 일부를 제공한다. | 라벨 조작, backdoor 삽입 | 학습 데이터 오염 | 공급망·데이터 수집 단계 |
| Evaluator/Operator | 평가 또는 운영 파이프라인에 접근한다. | 지표 왜곡, 로그 누락 | 성능 과장, 사고 은폐 | 내부 운영 리스크 |

---

## 4. 방어자 가정

| 방어자 능력 | 설명 | 한계 |
|---|---|---|
| 데이터 출처 기록 | 데이터 수집 경로와 라벨링 과정을 기록한다. | 출처가 있어도 오염이 없다는 보장은 아님 |
| 모델·config 보존 | 모델 버전, seed, hyperparameter, 환경을 기록한다. | 기록만으로 안전성을 보장하지 않음 |
| 평가 지표 분리 | clean, robust, privacy, reproducibility 지표를 분리한다. | 지표 간 trade-off 발생 |
| Human review | 수치, 인용, 보안 해석을 사람이 재검토한다. | 평가자 편향과 누락 가능성 |
| 모니터링·로그 | 배포 후 입력/출력/성능 변화를 기록한다. | 로그 자체가 민감정보가 될 수 있음 |
| 접근제어·rate limit | 모델 API와 출력 노출을 제한한다. | black-box 질의를 완전히 차단하기 어렵다 |

---

## 5. 생명주기별 위협

| 단계 | 주요 위협 | 공격자 목표 | 방어·점검 | 대표 지표 |
|---|---|---|---|---|
| 데이터 수집 | 오염 데이터, 편향, 개인정보 포함 | 데이터 기반 성능 왜곡, leakage 유발 | 출처 기록, 라벨 검수, 개인정보 제거 | data provenance, label error |
| 전처리 | feature leakage, 잘못된 정규화, split leakage | 평가 성능 과장, 정보누출 | 파이프라인 버전 관리, split audit | split integrity |
| 모델 학습 | poisoning, backdoor, overfitting | 모델 동작 왜곡, membership leakage | seed/config 보존, validation split 점검 | train-test gap |
| 모델 검증 | 평가셋 오염, 단일 지표 의존 | 성능 과장, 보안성 과장 | clean/robust/privacy/reproducibility 지표 분리 | robust acc, MI advantage |
| 배포 | 환경 차이, model extraction | API 기반 모델 복제, 운영 실패 | 접근 제어, rate limit, 출력 최소화 | query rate, output exposure |
| 추론 | evasion, adversarial example | 탐지 회피, 오분류 유도 | 입력 검증, 모니터링, robust evaluation | ASR, detection rate |
| 모니터링 | drift 미탐, 로그 누락 | 사고 추적 방해, 책임 회피 | drift detection, 감사 로그, rollback | drift score, audit completeness |

---

## 6. 제외 범위

다음 항목은 W01 분석 범위에서 제외한다.

- 실제 서비스 침해
- 실제 개인정보 사용
- 무단 API 대량 질의
- 실제 악성코드 실행
- 공격 절차의 세부 재현
- 비공개 데이터셋·비공개 benchmark 무단 사용

실험은 공개 데이터 또는 synthetic data 기반의 안전한 toy evaluation으로 제한한다.

---

## 7. 평가 증거 요구사항

| 증거 | 목적 | W01 상태 | 기말논문 연결 |
|---|---|---|---|
| DOI/URL 검증표 | 참고문헌과 본문 인용 대응 확인 | 작성 완료, P04 확인 필요 | reference verification table |
| Seed/config | 실험 재현 조건 확인 | 작성 완료 | reproducibility appendix |
| 실행 로그 | 정량값의 근거 보존 | outputs 파일 존재 확인 | experiment evidence |
| AI 활용 고지 | 초안 작성 과정과 책임 범위 표시 | 작성 완료 | AI disclosure section |
| PDF 보관 상태 | 공개 저장소 저작권 위험 점검 | PDF 원문 Git 추적 중, 조치 필요 | submission risk note |
| Human review | 원문, 수치, 해석 재검토 | 필요 | final paper checklist |

---

## 8. 위협-지표 매핑

| 위협 | 평가 지표 | 해석 |
|---|---|---|
| IDS 오탐 | FPR, precision | 운영자 피로와 alert 신뢰성 평가 |
| IDS 미탐 | recall, FNR | 공격 누락 위험 평가 |
| 대적 교란 | ASR, robust accuracy | 무결성 공격 저항성 평가 |
| 과적합 | generalization gap | privacy leakage와 일반화 위험 신호 |
| membership inference | MI advantage | 학습 데이터 포함 여부 노출 위험 |
| 생명주기 증거 누락 | evidence coverage | 연구 주장과 운영 보증의 신뢰성 |
| 로그 누락 | audit completeness | 사고 조사와 책임 추적 가능성 |

---

## 9. 연구문제 후보

| 번호 | 연구문제 후보 | W01 기반 근거 |
|---|---|---|
| RQ1 | ML 생명주기 각 단계에서 보안 보증을 위해 최소한으로 남겨야 할 증거는 무엇인가? | P02, evidence chain |
| RQ2 | Clean performance, robust performance, privacy leakage, reproducibility를 함께 볼 때 어떤 지표 조합이 가장 설득력 있는가? | P01~P05 통합 지표 |
| RQ3 | Survey 기반 분류체계를 실제 toy 실험 또는 문헌 매트릭스로 연결할 때 어떤 한계가 생기는가? | W01 실험·문헌 matrix |
| RQ4 | IDS·adversarial·privacy 평가 지표를 하나의 생명주기 프레임으로 통합할 수 있는가? | P03~P05 |

---

## 10. 최종 판단

W01 위협모형은 전체 과목의 기준 위협모형이다. 이후 주차의 poisoning, adversarial, LLM security, RAG injection, FL, DP, MLOps 주제는 모두 W01의 보호 자산과 생명주기 단계 위에 배치할 수 있다.
