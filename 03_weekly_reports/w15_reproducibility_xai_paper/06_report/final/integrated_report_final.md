# W15 연구평가·재현성·설명가능성(XAI)·논문 구성 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W15 |
| 주제 | 연구평가·재현성·설명가능성(XAI)·논문 구성 |
| AI 원리 | Evaluation, reproducibility, XAI, paper structure |
| 보안 이슈 | Benchmark contamination, model leakage, policy/ethics risk |
| 문서 상태 | 최종본 |
| 실습 상태 | 로컬 재현성·제출 준비 감사 실행 완료 |

## 1. 한 문장 요약

W15는 LLM 평가, ML lifecycle assurance, XAI, concept-based explanation을 바탕으로 AI 보안 연구의 성능 주장, 설명 신뢰성, 참고문헌 검증, AI 활용 고지, 재현성 산출물을 하나의 evidence chain으로 묶는다.

## 2. AI 원리 70% 정리

LLM 평가는 무엇을 평가할지, 어디서 평가할지, 어떻게 평가할지를 분리해야 한다. 재현성은 같은 config, seed, 데이터, 코드, 로그로 결과를 다시 검토할 수 있는 성질이다. XAI는 모델 판단 근거를 사람이 이해할 수 있게 하지만, 설명 자체도 fidelity, stability, completeness, leakage risk를 평가해야 한다.

| 개념 | 핵심 의미 | 관련 논문 |
|---|---|---|
| Evaluation | 모델 능력과 위험을 기준에 따라 측정 | P01 |
| Benchmark Contamination | 평가 데이터가 학습·튜닝에 노출되어 성능이 과대평가됨 | P01 |
| Reproducibility | 동일 조건에서 결과와 결론을 재검토 가능 | P01, P02 |
| ML Lifecycle Assurance | data/model/verification/deployment 단계별 증거 축적 | P02 |
| XAI | 모델 판단 근거를 사람이 이해 가능하게 설명 | P03, P04, P05 |
| Concept-based XAI | 사람이 이해 가능한 concept를 설명 단위로 사용 | P05 |
| Contribution/Limitation | 연구의 기여와 해석 범위를 명확히 쓰는 논문 구성 요소 | 전체 |

## 3. 보안 이슈 30% 정리

| 이슈 | 보안 의미 | 방어 또는 점검 |
|---|---|---|
| Benchmark contamination | 평가 무결성 훼손 | 출처·중복·노출 여부 점검 |
| Hidden test leakage | 평가셋 기밀성과 무결성 훼손 | 접근 통제와 질의 로그 |
| Reproducibility failure | 결과 검증 불가 | Dockerfile, config, seed, outputs 보존 |
| Model/explanation leakage | 모델 내부 단서 또는 민감 feature 노출 | 설명 공개 범위 제한 |
| Fabricated citation | 연구윤리와 책임성 훼손 | DOI/URL/로컬 PDF 검증 |
| Missing AI disclosure | AI 활용 책임 추적 실패 | AI 활용 고지와 human review |

## 4. 논문 5편 요약

| ID | 논문 | 역할 | 검증 상태 |
|---|---|---|---|
| P01 | A Survey on Evaluation of Large Language Models | LLM 평가 taxonomy와 benchmark contamination 근거 | DOI 확인 |
| P02 | Assuring the Machine Learning Lifecycle | lifecycle assurance와 evidence chain 근거 | DOI 확인 |
| P03 | Explainable AI: Core Ideas, Techniques, and Solutions | XAI 핵심 문헌, 현재 로컬 PDF는 대체 문헌 | 미검증 |
| P04 | Explainable Artificial Intelligence (XAI): Concepts, Taxonomies... | XAI taxonomy와 Responsible AI 근거 | DOI 확인 |
| P05 | Concept-based Explainable Artificial Intelligence: A Survey | concept-based XAI와 설명 평가 지표 근거 | 부분 확인 |

## 5. 논문 5편 비교

P01은 평가 데이터와 benchmark의 신뢰성을, P02는 재현성 증거를, P04/P05는 설명가능성과 책임성을 다룬다. P03은 지정 논문과 로컬 PDF가 일치하지 않는 검증 실패 사례로 남겨 최종 인용 전 원문 확보가 필요하다.

## 6. Research Track

### 6.1 연구문제

RQ1. LLM/RAG 기반 AI 시스템의 생명주기에서 prompt injection, benchmark contamination, privacy leakage는 각각 어느 단계에서 발생하는가?

RQ2. AI 보안 연구에서 clean performance, attack impact, privacy leakage, reproducibility를 함께 평가하려면 어떤 공통 평가 항목이 필요한가?

RQ3. 허위 인용, 실험결과 조작, AI 활용 은폐를 줄이기 위한 참고문헌·실험·AI 고지 체크리스트는 어떻게 구성되어야 하는가?

### 6.2 위협모형

대상 시스템은 AI 모델 평가 시스템, XAI 분석 시스템, AI 보안 논문 작성 프로세스다. 보호 자산은 benchmark, hidden test, model version, prompt/template, explanation output, reference list, AI worklog이다. 공격 성공 조건은 성능 과대평가, 검증 불가능한 결과 제출, 설명 결과의 민감정보 또는 모델 우회 단서 노출이다.

### 6.3 평가방법

| 평가 항목 | 지표 | 근거 |
|---|---|---|
| Evaluation Reliability | benchmark 오염·대체 PDF 여부 | `01_papers/doi_check.md` |
| Reproducibility | evidence coverage | `04_experiment/outputs/` |
| Reference Validity | weighted verification rate | `01_papers/doi_check.md` |
| AI Disclosure Quality | disclosure completeness | `05_ai_worklog/ai_disclosure_draft.md` |
| Limitation Clarity | 확인 필요 항목 명시 | `03_theory_notes/open_problems.md` |

### 6.4 재현성

W15는 `configs/config.yaml`, `src/run_experiment.py`, `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`를 보존한다. 로컬 실행에서는 `python3`로 검증했으며, 컨테이너 실행 예시는 `python src/run_experiment.py --config configs/config.yaml`이다.

### 6.5 한계와 오픈문제

P03 지정 논문 원문, P05 최종 DOI, 국내 문헌 3편 이상, 기말논문 표/그림 실제 삽입은 최종 제출 전 보완해야 한다. W15 감사는 모델 성능 실험이 아니므로 benchmark 성능을 주장하지 않는다.

## 7. 실습 요약

W15 실습은 로컬 재현성·제출 준비 감사로 실행했다.

| 점검 항목 | 결과 | 상태 |
|---|---:|---|
| W15 필수 산출물 | 47/47 | complete |
| 기말논문 연결 파일 | 9/9 | complete |
| 로컬 PDF | 5 | complete |
| DOI 확인 | 3 | partial |
| DOI 부분 확인 | 1 | partial |
| DOI 미검증 | 1 | attention |
| 가중 참고문헌 검증률 | 0.70 | partial |
| AI 활용 고지 완성도 | 9/9 | complete |

개인정보 사용, 실제 공격 수행, benchmark 성능 주장은 모두 없음으로 기록했다.

## 8. AI 활용 기록 요약

Codex를 사용해 공통 지침 확인, PDF/DOI 상태 대조, 보고서 구조 보완, 로컬 감사 스크립트 작성, 제출본과 발표자료 작성을 수행했다. AI 산출물은 사람 검토와 원문 대조를 거쳐 반영하며, 최종 책임은 작성자에게 있다.

## 9. 토론 질문

1. benchmark contamination을 소규모 연구에서 어느 수준까지 검증해야 하는가?
2. XAI 설명은 신뢰성 증거인가, 모델·데이터 누수 위험인가?
3. AI 활용 고지와 참고문헌 검증을 평가 루브릭에 정량 항목으로 넣을 수 있는가?

## 10. 기말 논문 연결

최종 주제는 "AI 보안 연구의 재현 가능한 생명주기 기반 평가 프레임워크: LLM·RAG·프라이버시 위협 중심"이다. W15는 연구방법, 평가방법, 보안적 함의, 부록의 참고문헌 검증과 AI 활용 고지에 연결된다.

## 11. 참고문헌 검증표

| 항목 | 수량 | 상태 |
|---|---:|---|
| DOI 확인 | 3 | P01, P02, P04 |
| 부분 확인 | 1 | P05 arXiv 확인, 최종 DOI 필요 |
| 미검증 | 1 | P03 지정 논문 원문 필요 |
| 가중 검증률 | 0.70 | 확인 1점, 부분 확인 0.5점 |

## 12. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 완료 |
| 비교표 | 완료 |
| AI 원리 70% | 완료 |
| 보안 이슈 30% | 완료 |
| Research Track | 완료 |
| 로컬 감사 outputs | 완료 |
| 제출용 Markdown/HTML | 완료 |
| 발표 패키지 | 완료 |
| DOI 임의 생성 방지 | 완료, 미검증 항목 표시 |
| AI 사용 은폐 방지 | 완료, AI 활용 고지서 작성 |

## 13. 기말 논문 최종 Contribution 후보

### 후보 1

본 연구는 LLM/RAG 기반 AI 시스템의 데이터·평가·프롬프트 생명주기에서 prompt injection, benchmark contamination, privacy leakage 위협을 분석하고, 재현성 중심의 보안 평가 체크리스트를 제안한다.

### 후보 2

본 연구는 기존 AI 보안 survey가 위협 분류와 실험 재현성의 연결을 충분히 제공하지 못하는 한계를 보완하기 위해 clean performance, attack impact, leakage, reproducibility, human review를 포함한 통합 평가 기준을 제시한다.
