# W01 한계와 오픈문제

## 0. 문서 목적

이 문서는 W01의 한계와 오픈문제를 연구논문형으로 정리한다. 단순히 “부족한 점”을 나열하지 않고, **한계 → 왜 중요한가 → W01 대응 → 후속 주차 연결 → 기말논문 반영** 구조로 정리한다.

---

## 1. 한계 요약표

| 번호 | 한계 | 왜 중요한가 | W01 대응 | 후속 연결 |
|---|---|---|---|---|
| L1 | 이론과 실무 사이의 격차 | 딥러닝 원리만으로 실제 보안 운영 환경의 실패를 설명하기 어렵다. | lifecycle threat model 작성 | W14 MLOps |
| L2 | 평가 지표의 불완전성 | accuracy 하나로 보안성·프라이버시·강건성을 설명할 수 없다. | clean/robust/privacy/reproducibility 지표 분리 | W03, W11, W12 |
| L3 | 재현성 부족 | survey 기반 논문은 code, seed, config가 부족한 경우가 많다. | config, run_log, metrics 파일 연결 | W15 evidence chain |
| L4 | 안전한 실험 범위 제한 | adversarial/privacy 공격은 악용 가능성이 있다. | toy/public/synthetic evaluation으로 제한 | 전 주차 공통 |
| L5 | 공개 데이터셋과 실제망 차이 | IDS 공개 데이터셋 성능이 실제 운영망 성능을 보장하지 않는다. | domain gap 한계 명시 | W09, W14 |
| L6 | 프라이버시-유틸리티 trade-off | 프라이버시 방어는 모델 성능 저하를 만들 수 있다. | MI advantage와 utility 구분 | W11 DP/MIA |
| L7 | P04 문헌 동일성 주의 | 현재 P04는 관련 arXiv 문헌 기준이므로 강의계획서 지정 논문과 차이가 있을 수 있다. | paper_list와 matrix에 주의 메모 유지 | 최종 제출 전 확인 |

---

## 2. 주요 한계 상세

### 2.1 이론과 실무 사이의 격차

딥러닝의 표현학습 원리는 넓은 영역에서 성능을 설명하지만, 실제 보안 시스템에서는 데이터 수집 과정, 라벨 품질, 운영 환경, 공격자 적응 능력이 성능을 크게 흔든다.

| 항목 | 설명 |
|---|---|
| 문제 | 문헌의 분류체계를 그대로 실제 보안성으로 해석하면 안 된다. |
| W01 대응 | toy evaluation과 문헌 기반 analysis를 분리한다. |
| 기말논문 반영 | 실험 결과는 “제한된 synthetic/toy 조건”으로 표현한다. |

---

### 2.2 평가 지표의 불완전성

Accuracy는 보안 연구에서 충분하지 않다. 침입탐지에서는 오탐과 미탐 비용이 다르고, 대적 ML에서는 clean accuracy와 robust accuracy가 충돌하며, 프라이버시 보호에서는 utility와 leakage risk 사이의 trade-off가 생긴다.

| 지표 | 설명 | 한계 |
|---|---|---|
| Accuracy | 전체 정답률 | class imbalance와 오탐/미탐 비용을 숨긴다. |
| Precision | 탐지한 공격 중 실제 공격 비율 | 미탐 위험을 단독으로 설명하지 못한다. |
| Recall | 실제 공격 중 탐지한 비율 | 오탐 비용을 단독으로 설명하지 못한다. |
| Robust Accuracy | 공격 조건 정확도 | 공격 설정에 크게 의존한다. |
| ASR | 공격 성공률 | 공격자 능력과 threat model을 함께 명시해야 한다. |
| MI Advantage | membership inference 위험 | 실제 데이터·출력 접근 가정에 따라 달라진다. |

---

### 2.3 재현성 문제

Survey 논문은 폭넓은 분류체계를 제공하지만, 구체적인 코드·데이터·seed·실행환경이 없는 경우가 많다. 기말논문에서는 Docker, config, DOI 검증표, 실행 로그를 함께 남겨 재현성 증거를 보완해야 한다.

| 필요한 증거 | 이유 |
|---|---|
| DOI/URL | 참고문헌 허위 인용 방지 |
| config | 실험 조건 재현 |
| seed | random split/학습 재현 |
| raw output | 결과 해석 검증 |
| run_log | 실행 여부와 시간 기록 |
| AI disclosure | AI 활용 범위와 책임 분리 |

---

### 2.4 안전한 실험 범위

대적 공격과 프라이버시 공격은 교육적 가치가 있지만 악용 가능성도 있다. W01에서는 실제 서비스, 실제 개인정보, 무단 API 질의, 상세 공격 절차를 제외하고 toy/public data 기반의 안전한 평가 설계로 제한한다.

| 허용 | 제외 |
|---|---|
| synthetic data | 실제 개인정보 |
| 공개 toy dataset | 실제 서비스 공격 |
| 문헌 기반 비교 | 무단 API 대량 질의 |
| 안전한 perturbation 설명 | 상세 공격 절차 제공 |
| high-level threat model | 악성코드 실행 |

---

## 3. 오픈문제

| 번호 | 오픈문제 | 연구 가능성 | 후속 주차 연결 |
|---|---|---|---|
| OP1 | ML 생명주기 단계별 최소 보안 보증 증거를 어떻게 정의할 수 있는가? | 기말논문 핵심 프레임 가능 | W14, W15 |
| OP2 | Clean performance, robust performance, privacy leakage, reproducibility를 한 표에서 어떻게 비교할 수 있는가? | 다중지표 평가표 설계 가능 | W03, W11, W12 |
| OP3 | 공격-방어-평가 표준을 주차별 survey 논문에 일관되게 적용할 수 있는가? | 전체 주차 통합 matrix 가능 | W01~W15 |
| OP4 | 정량 실험이 부족한 survey 주차를 문헌 기반 evidence matrix로 어떻게 보완할 수 있는가? | 문헌분석형 KCI 주제 가능 | W15 |
| OP5 | 프라이버시 보호와 모델 유틸리티의 trade-off를 비전문 독자에게 어떻게 설명할 것인가? | 교육·정책적 가치 있음 | W11 |
| OP6 | P04처럼 지정 문헌과 로컬 PDF가 다른 경우 제출 신뢰성을 어떻게 확보할 것인가? | reference verification table 설계 가능 | W15 |

---

## 4. RQ/Hypothesis 후보

### 4.1 연구질문 후보

| 번호 | 연구질문 |
|---|---|
| RQ1 | ML 생명주기 기반 AI 보안 평가에서 최소한으로 남겨야 할 evidence chain은 무엇인가? |
| RQ2 | Survey 기반 AI 보안 과제를 clean performance, robust performance, privacy risk, reproducibility로 일관되게 비교할 수 있는가? |
| RQ3 | Synthetic toy evaluation과 문헌 기반 matrix를 결합하면 실제 공격 절차 없이도 교육용 AI 보안 평가 프레임워크를 만들 수 있는가? |
| RQ4 | DOI 검증, PDF 보관 정책, AI 활용 고지가 AI 보안 보고서의 신뢰성을 얼마나 높이는가? |

### 4.2 가설 후보

| 번호 | 가설 |
|---|---|
| H1 | Accuracy 단일 지표보다 clean/robust/privacy/reproducibility 다중지표가 AI 보안 보고서의 설명력을 높인다. |
| H2 | Evidence chain을 명시한 보고서는 문헌 기반 survey 과제에서도 재현성과 신뢰성을 개선한다. |
| H3 | Toy evaluation을 안전하게 제한해도 보안 위협모형과 평가 지표 교육에는 충분한 효과가 있다. |
| H4 | Reference verification table은 지정 문헌·로컬 PDF·공식 DOI 불일치로 인한 제출 리스크를 줄인다. |

---

## 5. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | accuracy 중심 AI 보안 평가의 한계 제기 |
| 2장 관련연구 | survey 문헌의 분류체계와 재현성 한계 정리 |
| 3장 연구문제 | RQ1~RQ4 중 1~2개 선택 |
| 4장 연구방법 | evidence chain, multi-metric evaluation, toy protocol 제시 |
| 5장 분석 | W01 toy 결과와 문헌 matrix의 한계 비교 |
| 6장 결론 | 실제 운영 보증으로 일반화하지 않는 한계와 후속 연구 제시 |

---

## 6. 최종 판단

W01의 오픈문제는 “딥러닝을 이해했는가”보다 “딥러닝 기반 보안 주장을 어떻게 검증 가능한 증거로 만들 것인가”에 집중해야 한다. 따라서 기말논문 주제는 다음 방향이 가장 적합하다.

```text
ML 생명주기 기반 AI 보안 평가 프레임워크:
성능·강건성·프라이버시·재현성 evidence chain을 중심으로
```
