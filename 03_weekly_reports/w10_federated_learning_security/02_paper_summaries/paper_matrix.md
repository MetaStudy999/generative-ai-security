# W10 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | 보안 위협 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 | FL aggregation, personalization, robustness를 어떻게 분류할 것인가 | 문헌조사, bibliometric analysis, aggregation taxonomy | aggregation 방법 비교와 실험적 통찰, 세부 수치는 원문 대조 필요 | robust aggregation, privacy/security 고려 | aggregation 분류, IID/Non-IID, heterogeneity | 프롬프트 학술지명과 로컬 PDF 학술지명 차이 | FedAvg와 robust aggregation 비교 축 |
| P02 | FL 채택을 막는 security/privacy 위험은 무엇인가 | 보안·프라이버시 survey | 구현 스타일과 threat factor 정리 | poisoning, backdoor, inference attack, bottleneck | threat category, risk factor | 최신 방어법은 후속 문헌 보완 필요 | CIA/privacy 위협분류 |
| P03 | FL attack과 defense taxonomy를 어떻게 짝지을 것인가 | 공격/방어 taxonomy와 실험 연구 정리 | FL threat 실험 연구 포함, 출판 DOI 최종 대조 필요 | adversarial attack, privacy attack, model integrity | attack category, defense category | 로컬 PDF는 arXiv preprint | malicious client rate와 방어 지표 설계 |
| P04 | FL privacy attack, defense, application, policy를 어떻게 연결할 것인가 | privacy attack/defense/application/policy survey | 산업 적용과 정책 환경 검토 | gradient leakage, privacy attack | privacy risk, defense coverage, policy implication | 실제 privacy attack 재현은 본 주차 범위 밖 | privacy leakage proxy와 정책 함의 |
| P05 | FL backdoor attack과 defense를 어떻게 평가할 것인가 | backdoor attack/defense survey | backdoor 전략과 방어 과제 정리, 출판 DOI 최종 대조 필요 | backdoor, malicious client, poisoned update | ASR, clean accuracy, stealthiness | 로컬 PDF는 arXiv preprint | ASR와 clean accuracy 동시 평가 |

## 종합 비교

### 1. 공통적으로 다루는 문제

다섯 편은 모두 FL이 raw data를 중앙 서버로 모으지 않는다는 장점만으로는 충분하지 않다고 본다. 공통 축은 client-server-aggregation 구조, non-IID/heterogeneity, malicious client, privacy leakage, poisoning/backdoor, 방어 평가의 trade-off다.

### 2. 논문 간 차이점

P01은 aggregation taxonomy와 FL 원리 쪽에 강하고, P02/P03은 security/privacy taxonomy, P04는 privacy attack과 policy, P05는 backdoor 특화 평가에 강하다. 따라서 W10 보고서는 FedAvg 성능표 하나가 아니라 utility, ASR, leakage proxy, aggregation type을 함께 기록한다.

### 3. 아직 해결되지 않은 문제

출판본 DOI가 아직 확정되지 않은 P03/P05는 최종 참고문헌에서 재확인해야 한다. 또한 synthetic toy 실험은 실제 FL 시스템, secure aggregation, differential privacy, 대규모 non-IID benchmark를 대체하지 못한다.

### 4. 기말 논문 주제로 발전 가능한 연결부

W10는 "FL 보안 평가는 clean accuracy만으로 충분하지 않다"는 기말 논문 논지를 뒷받침한다. 20% poisoned FedAvg는 clean accuracy 0.950000을 유지하면서 ASR 0.496835까지 상승했고, coordinate median은 같은 20% 조건에서 ASR을 0.237342로 낮췄다.
