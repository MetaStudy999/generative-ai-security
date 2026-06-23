# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

W15의 보안 이슈는 평가 결과의 무결성, 설명 결과의 정보노출, 연구 산출물의 책임성이다. 공격 절차를 상세히 수행하는 것이 아니라, 어떤 자산이 어떤 조건에서 훼손되는지와 이를 막기 위한 제출 전 점검 항목을 정리한다.

| 이슈 | 설명 | 방어 또는 점검 |
|---|---|---|
| Benchmark contamination | 평가 데이터가 학습 또는 프롬프트 설계에 섞여 성능이 과대평가됨 | 데이터 출처, 중복 검사, model/version 기록 |
| Hidden test leakage | hidden test의 정답·패턴·분포가 간접 노출됨 | 평가셋 접근 통제, 질의 로그, 공개/비공개 데이터 분리 |
| Evaluation reproducibility failure | 같은 조건에서 결과를 다시 확인할 수 없음 | config, seed, Dockerfile, outputs 보존 |
| Model leakage | 평가나 설명 과정에서 모델 내부 정보가 과도하게 노출됨 | 공개 설명 범위 제한, 민감 feature 점검 |
| XAI attack surface | 설명을 이용해 모델 회피·조작 단서를 얻음 | explanation disclosure policy, human review |
| Explanation misuse | 충실하지 않은 설명을 근거로 과신 또는 잘못된 결론을 냄 | fidelity, stability, limitation 명시 |
| Policy and ethics risk | AI 사용 은폐, 허위 DOI, 허위 인용, 결과 과장 | AI 활용 고지, 참고문헌 검증표, 자기점검표 |

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | Hidden test leakage / model leakage | 평가셋, 모델 내부 단서, 설명 결과가 외부에 노출될 수 있다. |
| Integrity | Benchmark contamination / fabricated citation | 오염된 benchmark나 허위 인용은 연구 결과의 무결성을 훼손한다. |
| Availability | Irreproducible evaluation | 로그와 환경이 없으면 결과를 재검토할 수 없어 연구 산출물의 사용성이 낮아진다. |
| Privacy | Sensitive information in explanation | XAI가 민감 feature나 학습 사례를 드러낼 수 있다. |
| Safety | Misleading explanation / unsafe model trust | 그럴듯하지만 틀린 설명은 안전중요 의사결정에서 과신을 유발한다. |
| Accountability | Missing AI disclosure / unverifiable reference | AI 활용과 참고문헌 검증이 빠지면 책임 추적이 어렵다. |

## 3. 공격-방어-평가 분류

| 구분 | 내용 |
|---|---|
| 보호 자산 | benchmark, hidden test, model version, prompt/template, explanation output, reference list, AI worklog |
| 공격자 능력 | 데이터 오염, 평가셋 노출, 반복 질의, 설명 결과 악용, 참고문헌 조작, AI 산출물 무검증 사용 |
| 방어 방법 | 출처 검증, DOI 확인, 실행 로그 저장, 관련 논문 PDF 표시, AI 활용 고지, human approval gate |
| 평가 지표 | reference verification rate, reproducibility evidence coverage, AI disclosure completeness, explanation stability, leakage risk |

## 4. 기말 논문 연결

기말논문에서는 공격 절차를 재현하지 않고도 보안적 함의를 제시할 수 있도록, 평가오염·프라이버시 누수·설명 오용·연구윤리 실패를 하나의 생명주기 체크리스트로 묶는다. 이 체크리스트는 본문 평가방법과 부록 제출 점검표에 동시에 반영한다.
