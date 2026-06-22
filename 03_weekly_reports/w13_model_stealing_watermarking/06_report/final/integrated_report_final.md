# W13 모델 지식재산(IP)·모델 도난·모델 추출 위협 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W13 |
| 주제 | 모델 지식재산(IP)·모델 도난·모델 추출 위협 |
| AI 원리 | Model IP, model stealing, model extraction |
| 보안 이슈 | Watermarking, fingerprinting, model extraction defense |
| 작성일 | 2026-06-22 |
| 문서 상태 | 최종본 |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## 1. 한 문장 요약

W13는 query-response 기반 모델 추출 위험과 워터마크 기반 소유권 검증을 함께 다루며, 실험 결과는 검출률뿐 아니라 false positive와 utility를 함께 보고해야 함을 보여준다.

## 2. AI 원리 70% 정리

모델 IP는 파라미터, 구조, 학습 데이터, 출력 행동, 생성물 출처에 축적된 기술적·경제적 가치다. 모델 도난은 이 가치를 무단으로 획득하거나 복제하는 넓은 공격군이고, 모델 추출은 공개 API 또는 black-box 출력에서 query-response 쌍을 모아 대체 모델을 학습하거나 원 모델 속성을 추정하는 절차다.

핵심 원리는 query budget, 출력 정보량, fidelity, substitute learning, watermark/fingerprint, utility-protection trade-off다. 워터마크는 모델 또는 생성물에 소유권 검증 신호를 남기지만, 모델 품질 저하와 오탐 문제가 함께 관리되어야 한다.

### 2.1 핵심 수식 또는 알고리즘 쉬운 설명

아래 수식은 원문 수식의 직접 인용이 아니라, 각 논문의 핵심 개념을 보고서에서 설명하기 위한 대표 수식과 지표다. 최종 제출본에서 원문 수식으로 인용할 경우 논문 원문 쪽/절 번호를 추가 확인한다.

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보안 평가 연결 |
|---|---|---|---|
| P01 | $Fidelity=\frac{1}{n}\sum_i 1[f_v(x_i)=f_s(x_i)]$ | 추출 모델이 원 모델과 얼마나 같은 답을 내는지로 도난 위험을 본다. | model extraction |
| P02 | $z=\frac{\lvert G\rvert-E[\lvert G\rvert]}{\sqrt{Var(\lvert G\rvert)}}$ | 워터마크 검출은 생성 토큰이 기대보다 많이 특정 집합에 들어가는지 통계적으로 본다. | LLM watermarking |
| P03 | $RobustDetect=N_{detected\ after\ attack}/N_{watermarked}$ | watermark는 pruning, fine-tuning, extraction 뒤에도 검출되어야 의미가 있다. | DNN watermarking |
| P04 | $TPR=N_{wm\ detected}/N_{wm}$, $FPR=N_{clean\ detected}/N_{clean}$ | 소유권 검증은 탐지율이 높아도 위양성이 높으면 강한 증거가 아니다. | ModelShield 평가 |
| P05 | $\min_G\max_D E[\log D(x)]+E[\log(1-D(G(z)))]$ | GAN 보안 문헌은 생성모형이 privacy와 misuse 위험을 함께 가진다는 배경을 준다. | secure/private generative models |

## 3. 보안 이슈 30% 정리

| 관점 | 관련 위협 | 평가 연결 |
|---|---|---|
| Confidentiality | 모델 행동·결정경계 유출 | extraction fidelity |
| Integrity | watermark removal/forgery | watermark detection |
| Availability | query abuse/API cost exhaustion | query budget |
| Privacy | 도난 모델을 통한 학습 데이터 추론 가능성 | 제외 범위와 안전 한계 |
| Safety | 도난 생성모형 오용 | 생성물 추적과 책임성 |
| Accountability | ownership verification failure | false positive/false negative |

## 4. 논문 5편 요약

| ID | 문헌 | 역할 | 검증 상태 |
|---|---|---|---|
| P01 | I Know What You Trained Last Summer | model stealing/extraction taxonomy와 방어 선택 기준 | PDF DOI 표기 확인, 공식 페이지 대조 필요 |
| P02 | Watermarking Techniques for Large Language Models: A Survey | LLM watermarking, traceability, semantic invariance | 대체 PDF, 프롬프트 지정 문헌과 불일치 |
| P03 | A Survey of Deep Neural Network Watermarking Techniques | fidelity-robustness-capacity, static/dynamic watermarking | DOI/URL 확인 필요 |
| P04 | ModelShield | extraction 이후 watermark ownership check | arXiv 표기 확인, 출판 정보 대조 필요 |
| P05 | Generative Adversarial Networks: A Survey Towards Private and Secure Applications | 생성모형 privacy/security 보조 배경 | 대체 PDF, 프롬프트 지정 문헌과 불일치 |

## 5. 논문 5편 비교

P01은 모델 도난 taxonomy, P03은 DNN watermarking 이론, P04는 extraction 이후 소유권 검증을 담당한다. P02와 P05는 로컬 PDF가 프롬프트 지정 문헌과 달라 보조 문헌으로만 사용했다. 공통 결론은 모델 IP 보호가 fidelity, detection, false positive, utility, robustness, 재현성을 함께 요구한다는 점이다.

## 6. Research Track

### 6.1 연구문제

RQ1. 공개 API 기반 모델 서비스에서 query-response 정보만으로 모델 도난 위험을 어떻게 정량화할 수 있는가?

RQ2. 모델 워터마킹은 모델 추출 공격 이후에도 소유권 검증을 얼마나 안정적으로 수행할 수 있는가?

RQ3. 워터마킹 방어는 모델 품질, 탐지율, 위양성, 강건성 사이에서 어떤 trade-off를 만드는가?

### 6.2 위협모형

대상 시스템은 공개 API 또는 제한된 인터페이스로 제공되는 ML/LLM/생성모형 서비스다. 보호 자산은 모델 파라미터, 모델 행동, 학습된 결정경계, 워터마크, fingerprint, 생성물 출처, API 로그다. 공격자는 반복 질의와 입력-출력 쌍 수집으로 substitute model을 만들 수 있으나, 본 보고서는 실제 상용 API 공격과 무단 대량 질의를 제외한다.

### 6.3 평가방법

| 평가 항목 | 지표 | W13 사용값 |
|---|---|---|
| Extraction Fidelity | victim/substitute 출력 일치율 | 0.864000, 0.920000, 0.902000 |
| Substitute Accuracy | true label 기준 대체 모델 정확도 | 0.812000, 0.840000, 0.822000 |
| Query Cost | query budget | 100, 500, 1000 |
| Watermark Detection | trigger signature 일치율 | 0.700000, 1.000000, 1.000000 |
| False Positive Rate | clean control trigger 일치율 | 0.600000 |
| Utility Accuracy | victim clean accuracy | 0.868000 |

### 6.4 재현성

실험은 seed 42, synthetic binary classification, `configs/config.yaml`, `src/run_experiment.py`로 실행했다. 결과는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`에 저장했다.

### 6.5 한계와 오픈문제

본 실험은 실제 API나 실제 LLM이 아닌 toy classifier 평가다. false positive proxy가 0.600000으로 높아 trigger-set ownership check만으로 강한 소유권 주장을 할 수 없다. P02/P05 대체 PDF와 DOI/URL 공식 검증도 남아 있다.

## 7. 실습 요약

| 조건 | Query Budget | Extraction Fidelity | Substitute Accuracy | Watermark Detection | False Positive Rate | Utility Accuracy |
|---|---:|---:|---:|---:|---:|---:|
| Baseline victim model | 0 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 |
| Substitute query 100 | 100 | 0.864000 | 0.812000 | 0.700000 | 0.600000 |  |
| Substitute query 500 | 500 | 0.920000 | 0.840000 | 1.000000 | 0.600000 |  |
| Substitute query 1000 | 1000 | 0.902000 | 0.822000 | 1.000000 | 0.600000 |  |
| Watermarked ownership check | 0 | 1.000000 | 0.868000 | 1.000000 | 0.600000 | 0.868000 |

## 8. AI 활용 기록 요약

Codex를 사용해 공통 지침 확인, 문헌 요약 보완, toy 실험 코드 작성·실행, 통합보고서·제출본·발표자료 작성을 수행했다. AI 활용 내역은 `05_ai_worklog/`에 기록했으며, 실험 수치는 outputs와 일치하는 값만 반영했다.

## 9. 토론 질문

1. watermark detection이 1.000000이어도 false positive가 높다면 소유권 검증 기준은 어떻게 정해야 하는가?
2. query budget과 fidelity를 보고할 때 공격 재현성과 악용 방지 사이의 균형은 어디에 둘 것인가?
3. 프롬프트 지정 문헌과 로컬 PDF가 다를 때 제출물에서 어떻게 투명하게 표시할 것인가?

## 10. 기말 논문 연결

W13는 기말 논문의 관련연구, 위협모형, 평가방법, 보안적 함의 장에 연결된다. 특히 “모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크” 주제로 발전시키기 좋다.

## 11. 참고문헌 검증표

참고문헌 검증 상태는 `01_papers/doi_check.md`에서 관리한다. P02/P05는 대체 PDF이며, 최종 인용 전 원문 교체 또는 대체 사유 명시가 필요하다.

## 12. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 완료 |
| 비교표 | 완료 |
| AI 원리 70% | 완료 |
| 보안 이슈 30% | 완료 |
| Research Track | 완료 |
| 실험 코드/결과 | 완료 |
| 제출용 보고서 | 완료 |
| 발표자료 | 완료 |
| DOI 임의 생성 방지 | 확인 필요 유지 |
| AI 활용 고지 | 완료 |
