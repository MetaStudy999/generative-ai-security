# W10 연합학습(FL) & FL 위협·방어·정책 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W10 |
| 주제 | 연합학습(FL) & FL 위협·방어·정책 |
| AI 원리 | Federated Learning, FedAvg, aggregation, personalization, robustness |
| 보안 이슈 | Gradient leakage, poisoning, backdoor, privacy attack |
| 문서 상태 | 최종본 |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## 1. 한 문장 요약

W10는 FL이 raw data를 중앙 서버로 모으지 않는다는 장점에도 불구하고, model update와 aggregation 단계에서 privacy·integrity 위험이 남으며 clean accuracy와 ASR을 함께 봐야 함을 보여준다.

## 2. AI 원리 70% 정리

FL은 client가 local data로 update를 계산하고 server가 aggregation으로 global model을 갱신하는 구조다. FedAvg는 가장 기본적인 평균 집계이며, robust aggregation은 이상 update의 영향을 줄이기 위해 median, trimmed mean 같은 규칙을 사용할 수 있다. Non-IID data, personalization, communication cost는 FL 성능과 운영 가능성을 동시에 좌우한다.

## 3. 보안 이슈 30% 정리

FL의 주요 위험은 gradient leakage, membership inference, poisoning, model poisoning, backdoor, malicious/byzantine client다. Secure aggregation은 confidentiality에는 도움이 될 수 있지만 악성 update 검증을 어렵게 만들 수 있고, robust aggregation은 integrity 방어에 유용하지만 privacy 보장을 직접 제공하지는 않는다.

## 4. 논문 5편 요약

| ID | 논문 | 역할 | 검증 상태 |
|---|---|---|---|
| P01 | Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights, and Future Frontiers | aggregation taxonomy와 robust aggregation 배경 | DOI 확인 |
| P02 | A survey on security and privacy of federated learning | FL security/privacy threat taxonomy | DOI 확인 |
| P03 | Survey on federated learning threats: Concepts, taxonomy on attacks and defences, experimental study and challenges | 공격-방어 taxonomy와 평가 기준 | arXiv 확인, 출판 DOI 확인 필요 |
| P04 | The Federation Strikes Back: A Survey of Federated Learning Privacy Attacks, Defenses, Applications, and Policy Landscape | privacy attack, defense, policy landscape | DOI 확인 |
| P05 | Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions | backdoor threat와 ASR 평가 근거 | arXiv 확인, 출판 DOI 확인 필요 |

## 5. 논문 5편 비교

P01은 AI 원리와 aggregation 설계축, P02/P03은 security/privacy taxonomy, P04는 privacy와 정책, P05는 backdoor 평가에 강하다. 다섯 편을 합치면 FL 보안 평가는 utility, ASR, privacy leakage, aggregation type, reproducibility를 함께 기록해야 한다는 결론으로 이어진다.

## 6. Research Track

### 6.1 연구문제

RQ1. 연합학습 환경에서 malicious client 비율은 global model의 clean 성능과 backdoor ASR에 어떤 영향을 미치는가?

RQ2. Robust aggregation은 poisoned update의 영향을 줄일 수 있는가, 그리고 clean utility와 어떤 trade-off를 갖는가?

RQ3. FL 보안 평가에는 privacy leakage, robustness, utility, communication cost를 어떻게 결합해야 하는가?

### 6.2 위협모형

대상 시스템은 FL 기반 분산 학습 시스템이다. 보호 자산은 client data, local update, global model, aggregation result, training log다. 공격자는 악성 client로 참여해 poisoned update를 제출하거나, update 관찰을 통해 privacy 단서를 추론할 수 있다. 본 주차 실험은 실제 시스템 침해나 실제 개인정보 사용을 제외한다.

### 6.3 평가방법

| 평가 항목 | 지표 | 근거 |
|---|---|---|
| Global utility | Global Accuracy, Global F1 | clean synthetic test set |
| Backdoor success | ASR | triggered synthetic test set |
| Privacy exposure | Privacy Leakage Proxy | update norm과 다양성 기반 대용 지표 |
| Robustness | 20% poisoned FedAvg와 coordinate median 비교 | `metrics_summary.csv` |
| Reproducibility | seed, config, run log, JSON | `outputs/` |

### 6.4 재현성

실험은 seed 42, 10 clients, client별 80 samples, test samples 600, 25 rounds, local epochs 3으로 실행했다. 산출물은 `run_log.md`, `metrics_summary.csv`, `results.json`에 보존했다.

### 6.5 한계와 오픈문제

본 실험은 synthetic toy logistic regression이며 실제 FL framework, secure aggregation, differential privacy, gradient inversion을 구현하지 않았다. P03, P05의 출판본 DOI는 최종 참고문헌 작성 시 추가 확인해야 한다.

## 7. 실습 요약

| 조건 | Malicious Client Rate | Aggregation | Global Accuracy | Global F1 | ASR | Privacy Leakage Proxy |
|---|---:|---|---:|---:|---:|---:|
| Clean FL | 0% | fedavg | 0.960000 | 0.958042 | 0.136076 | 0.442597 |
| Poisoned FL 10% | 10% | fedavg | 0.953333 | 0.951557 | 0.297468 | 0.428377 |
| Poisoned FL 20% | 20% | fedavg | 0.950000 | 0.948630 | 0.496835 | 0.486591 |
| Robust aggregation 20% | 20% | coordinate_median | 0.955000 | 0.953368 | 0.237342 | 0.439875 |

Clean FL 대비 20% poisoned FedAvg는 accuracy가 0.010000p 낮아지는 수준이지만 ASR은 0.136076에서 0.496835로 크게 상승했다. 같은 20% 조건에서 coordinate median은 ASR을 0.237342로 낮췄다.

## 8. AI 활용 기록 요약

Codex를 사용해 공통 지침 확인, W10 프롬프트 확인, 로컬 PDF 첫 페이지 메타데이터 대조, synthetic toy 실험 코드 작성·실행, 결과 로그 기반 보고서·제출본·발표자료 작성을 수행했다. DOI와 출판 정보는 확인된 항목만 확정하고 나머지는 확인 필요로 남겼다.

## 9. 토론 질문

1. FL에서 secure aggregation과 robust aggregation은 서로 보완적인가, 충돌하는가?
2. Clean accuracy가 유지되는 backdoor 위험을 운영 환경에서 어떻게 발견할 수 있는가?
3. Privacy leakage proxy를 실제 membership inference 또는 gradient inversion 평가로 확장하려면 어떤 통제가 필요한가?

## 10. 기말 논문 연결

W10는 기말 논문의 관련연구, 위협모형, 평가방법, 보안적 함의 장에 연결된다. 특히 "AI 보안 평가는 일반 성능, 공격 성공률, 프라이버시 노출, 재현성 로그를 동시에 요구한다"는 주장에 활용할 수 있다.

## 11. 참고문헌 검증표

참고문헌 검증 상태는 `01_papers/doi_check.md`에 기록했다. P01, P02, P04는 DOI를 확인했고, P03과 P05는 arXiv/preprint 확인 상태로 두었다.

## 12. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 완료 |
| 비교표 | 완료 |
| AI 원리 70% | 완료 |
| 보안 이슈 30% | 완료 |
| Research Track | 완료 |
| 실험 실행 | 완료 |
| 실행 로그/CSV/JSON | 완료 |
| 제출용 보고서 | 완료 |
| 발표자료 | 완료 |
| AI 활용 고지 | 완료 |
| DOI 임의 생성 방지 | 확인 필요 항목 유지 |
