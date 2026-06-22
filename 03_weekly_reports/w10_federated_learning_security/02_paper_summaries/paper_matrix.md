# W10 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | AI 원리 기여 | 보안 위협 연결 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|---|
| P01 | FL aggregation, personalization, robustness를 어떻게 분류할 것인가 | aggregation taxonomy, bibliometric analysis, systematic review | aggregation 방법 비교와 실험적 통찰 | FedAvg, aggregation, personalization, heterogeneity 이해 | robust aggregation과 malicious update 방어 | aggregation type, IID/Non-IID, heterogeneity, communication | 강의계획서/프롬프트의 CSUR 표기와 공식 DOI/TIST 표기 차이 있음 | FedAvg와 coordinate median 비교 축 |
| P02 | FL 채택을 막는 security/privacy 위험은 무엇인가 | FL security/privacy survey | FL 구현 스타일과 threat factor 정리 | FL 구조의 보안·프라이버시 공격면 이해 | poisoning, backdoor, inference attack, privacy leakage | threat category, risk factor, defense type | 최신 FL backdoor/DP/MI 방어 논문 보완 필요 | CIA/privacy 위협분류 |
| P03 | FL attack과 defense taxonomy를 어떻게 짝지을 것인가 | 공격/방어 taxonomy, experimental study, challenges | FL threat 실험 연구 포함, arXiv와 출판본 확인 | attack-defense mapping과 evaluation design | adversarial attack, privacy attack, model integrity | attack category, defense category, evaluation setting | DOI 확인 완료이나 최종 제출 전 DOI landing page 육안 확인 권장 | malicious client rate와 방어 지표 설계 |
| P04 | FL privacy attack, defense, application, policy를 어떻게 연결할 것인가 | privacy attack/defense/application/policy landscape survey | 산업 적용과 정책 환경 검토 | FL privacy governance와 정책 함의 | gradient leakage, membership inference, privacy attack | privacy risk, defense coverage, policy implication | 실제 privacy attack 재현은 본 주차 범위 밖. Article 번호 추가 확인 필요 | privacy leakage proxy와 정책 함의 |
| P05 | FL backdoor attack과 defense를 어떻게 평가할 것인가 | backdoor attack/defense survey | backdoor 전략과 방어 과제 정리, arXiv와 출판본 확인 | backdoor threat의 FL 특수성 | backdoor, malicious client, poisoned update, stealthiness | ASR, clean accuracy, stealthiness, defense success | DOI 확인 완료이나 실제 공격 payload 재현은 제외 | ASR와 clean accuracy 동시 평가 |

## 종합 비교

### 1. 논문별 차별성

- P01은 FL aggregation taxonomy와 AI 원리 문헌이다. W10에서 FedAvg, coordinate median, non-IID, communication cost를 같은 평가표에 올리는 근거를 제공한다.
- P02/P03은 FL security/privacy와 attack-defense taxonomy 문헌이다. P02는 FL 채택 위험의 큰 분류를 제공하고, P03은 공격과 방어를 평가 프로토콜로 연결한다.
- P04는 FL privacy attack과 policy landscape 문헌이다. 기술적 privacy attack뿐 아니라 application domain, regulation, accountability를 함께 다룬다.
- P05는 FL backdoor 공격·방어 특화 문헌이다. clean accuracy가 유지되어도 ASR이 증가할 수 있다는 평가상의 함정을 설명한다.

### 2. Secure aggregation과 robust aggregation 구분

- Secure aggregation은 서버가 개별 client update를 보지 못하게 하여 confidentiality를 강화하는 보호 기법이다.
- Robust aggregation은 악성 또는 이상 update의 영향을 줄여 global model integrity를 강화하는 집계 기법이다.
- 두 기법은 보완적일 수 있지만 운영상 trade-off가 있다. 예를 들어 secure aggregation이 강해질수록 서버가 개별 update 이상치를 직접 검사하기 어려워질 수 있다.

### 3. Privacy Leakage Proxy 해석 제한

W10의 Privacy Leakage Proxy는 실제 gradient inversion 또는 membership inference 성공률이 아니라 update norm과 client update 다양성에 기반한 대용 지표다. 따라서 이 값은 실제 개인 데이터 복원 가능성이나 실제 서비스 privacy breach로 해석하지 않는다.

### 4. W10 toy 실험의 위치

W10 toy 실험은 실제 FL framework, 실제 secure aggregation, differential privacy, gradient inversion, membership inference를 구현하지 않은 synthetic logistic regression 실험이다. 목적은 공격을 재현하는 것이 아니라 FL 보안 평가표가 clean utility, ASR, privacy exposure proxy, aggregation type, communication bytes, reproducibility evidence를 분리해 기록해야 함을 검증하는 것이다.

### 5. 기말 논문 주제로 발전 가능한 연결부

W10는 "FL 보안 평가는 clean accuracy만으로 충분하지 않다"는 기말 논문 논지를 뒷받침한다. outputs 기준 20% poisoned FedAvg는 clean accuracy 0.950000을 유지하면서 ASR 0.496835를 보였고, coordinate median은 같은 20% 조건에서 ASR을 0.237342로 낮췄다. 이 결과는 실제 FL 제품 성능 보증이 아니라 안전한 synthetic toy protocol의 평가 형식 검증 결과다.
