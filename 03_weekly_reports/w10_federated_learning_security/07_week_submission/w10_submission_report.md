# W10 제출용 보고서

## 1. 표지

| 항목 | 내용 |
|---|---|
| 주차 | W10 |
| 보고서 제목 | 연합학습(FL) & FL 위협·방어·정책 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 통합본 |
| 최종 보고서 | `06_report/final/integrated_report_final.md` |
| 실험 근거 | `04_experiment/outputs/run_log.md` |
| 발표자료 | `09_presentation/` |

## 2. 초록과 키워드

본 보고서는 연합학습의 client-server-aggregation 구조와 FedAvg, robust aggregation의 원리를 정리하고, FL에서 발생할 수 있는 gradient leakage, poisoning, backdoor, privacy attack을 위협모형과 평가방법으로 연결한다. Synthetic toy FL 실험에서는 malicious client 비율이 증가할수록 clean accuracy는 크게 무너지지 않아도 ASR이 상승할 수 있음을 확인했다. 20% poisoned FedAvg의 ASR은 0.496835였고, 같은 조건에서 coordinate median은 ASR을 0.237342로 낮췄다.

키워드: Federated Learning, FedAvg, Robust Aggregation, Poisoning, Backdoor, Privacy Leakage

## 3. AI 원리 70%와 보안 이슈 30%

| 구분 | 핵심 내용 |
|---|---|
| AI 원리 70% | FL 구조, client/server 역할, FedAvg, aggregation taxonomy, personalization, Non-IID data, communication cost, robust aggregation |
| 보안 이슈 30% | gradient leakage, membership inference, poisoning, model poisoning, backdoor, malicious/byzantine client, secure aggregation, privacy policy |

FL은 raw data를 중앙 서버로 보내지 않는 장점이 있지만, model update와 aggregation 단계가 새로운 공격면이 된다. 따라서 성능 평가와 보안 평가를 분리하지 않고 함께 기록해야 한다.

## 4. 논문 5편 요약과 검증 상태

| ID | 논문 | 핵심 역할 | DOI/URL 상태 |
|---|---|---|---|
| P01 | Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights, and Future Frontiers | aggregation taxonomy | DOI 확인 |
| P02 | A survey on security and privacy of federated learning | FL security/privacy survey | DOI 확인 |
| P03 | Survey on federated learning threats: Concepts, taxonomy on attacks and defences, experimental study and challenges | attack-defense taxonomy | arXiv 확인, 출판 DOI 확인 필요 |
| P04 | The Federation Strikes Back: A Survey of Federated Learning Privacy Attacks, Defenses, Applications, and Policy Landscape | privacy attack와 policy | DOI 확인 |
| P05 | Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions | backdoor와 ASR 평가 | arXiv 확인, 출판 DOI 확인 필요 |

## 5. Research Track

| 항목 | 내용 |
|---|---|
| 연구문제 | malicious client 비율과 aggregation rule이 clean utility와 ASR에 미치는 영향 |
| 대상 시스템 | FL 기반 분산 학습 시스템 |
| 보호 자산 | client data, local update, global model, aggregation result, run log |
| 공격자 | 악성 client, 내부자, 서버 관찰자 |
| 평가 지표 | Global Accuracy, Global F1, ASR, Privacy Leakage Proxy, Communication Bytes |
| 재현성 | seed 42, config, run log, CSV, JSON 보존 |
| 제외 범위 | 실제 개인정보, 실제 FL 서비스 침해, 무단 클라이언트 접속, 실제 공격 payload |

## 6. 실습/실험 실행 상태와 결과표

실험은 실행 완료 상태이며, 모든 수치는 `04_experiment/outputs/run_log.md`와 일치한다.

| 조건 | Malicious Client Rate | Aggregation | Global Accuracy | Global F1 | ASR | Privacy Leakage Proxy |
|---|---:|---|---:|---:|---:|---:|
| Clean FL | 0% | fedavg | 0.960000 | 0.958042 | 0.136076 | 0.442597 |
| Poisoned FL 10% | 10% | fedavg | 0.953333 | 0.951557 | 0.297468 | 0.428377 |
| Poisoned FL 20% | 20% | fedavg | 0.950000 | 0.948630 | 0.496835 | 0.486591 |
| Robust aggregation 20% | 20% | coordinate_median | 0.955000 | 0.953368 | 0.237342 | 0.439875 |

해석: 20% poisoned FedAvg는 clean accuracy 0.950000을 유지했지만 ASR 0.496835로 상승했다. Coordinate median은 같은 20% 조건에서 ASR을 0.237342로 낮췄다.

## 7. 발표용 보고서 위치

발표자료는 `09_presentation/`에 있다. 최종 발표본은 `presentation_slides.html`이며, 발표 보고서, speaker notes, Q&A, one-page handout을 함께 작성했다.

## 8. 기말논문 연결

W10는 기말논문에서 분산 AI 학습의 보안 평가 프레임워크를 설명하는 보조 근거로 활용할 수 있다. 특히 clean accuracy, ASR, privacy leakage, reproducibility를 함께 기록하는 평가표가 W11 DP/MI, W14 MLOps supply chain과 연결된다.

## 9. AI 활용 고지

Codex를 사용해 공통 지침 확인, 로컬 PDF 메타데이터 확인, synthetic toy 실험 코드 작성과 실행, 보고서·제출본·발표자료 작성을 수행했다. 확인된 DOI만 확정했고, P03/P05 출판 DOI는 확인 필요로 유지했다. 최종 내용, 인용, 실험결과, 연구윤리 책임은 작성자에게 있다.

## 10. 제출 전 점검

| 점검 항목 | 상태 |
|---|---|
| 실험 수치와 outputs 일치 | 완료 |
| 개인정보 사용 없음 | 완료 |
| 실제 서비스 공격 없음 | 완료 |
| DOI 임의 생성 없음 | 완료 |
| AI 활용 고지 포함 | 완료 |
| P03/P05 출판 DOI 확인 | 확인 필요 |
