# 기말 모의투고 논문 초안

## 제목

국문 제목: AI 보안 연구의 재현 가능한 생명주기 기반 평가 프레임워크: LLM·RAG·프라이버시 위협 중심

영문 제목: A Reproducible Lifecycle-Based Evaluation Framework for AI Security: Focusing on LLM, RAG, and Privacy Threats

---

## 국문초록

본 연구는 LLM/RAG 기반 AI 시스템에서 발생할 수 있는 프롬프트 인젝션, 평가오염, 프라이버시 누수, 재현성 실패를 생명주기 관점에서 정리한다. 기존 문헌은 개별 위협과 방어를 폭넓게 분류하지만, 연구 보고서 작성 단계에서 성능·보안성·프라이버시·재현성·AI 활용 고지를 함께 점검하는 절차는 분산되어 있다. 이에 본 연구는 W07, W08, W11, W14, W15 주차 보고서를 바탕으로 위협모형, 평가항목, 참고문헌 검증표, AI 활용 고지서로 구성된 재현 가능한 평가 프레임워크를 제안한다.

---

## 영문초록

This study proposes a reproducible lifecycle-based evaluation framework for AI security, focusing on LLM and RAG systems. It organizes prompt injection, benchmark contamination, privacy leakage, and reproducibility failures across the AI lifecycle. Existing surveys provide useful taxonomies of attacks and defenses, but the connection between threat classification, evaluation metrics, reproducibility records, reference verification, and AI disclosure is often left fragmented. Based on weekly reports on LLM security, RAG prompt injection, privacy attacks, MLOps supply-chain risks, and research reproducibility, this study derives a threat model, evaluation criteria, a reference verification table, and an AI disclosure checklist. The framework emphasizes utility, attack impact, privacy leakage, robustness, cost, auditability, and reproducibility as joint evaluation dimensions. The proposed approach is intended for safe literature-based analysis and toy evaluation settings, excluding real service compromise, personal data use, and unverified experimental claims. By connecting technical security evaluation with research ethics controls, the study aims to support small-scale AI security papers that are transparent, auditable, and suitable for domestic mock-journal submission.

---

## 키워드

국문 키워드: AI 보안, LLM, RAG, 프롬프트 인젝션, 재현성, 연구윤리

영문 키워드: AI Security, LLM, RAG, Prompt Injection, Reproducibility, Research Ethics


---

## 1. 서론

### 1.1 연구 배경

LLM과 RAG 기반 시스템은 학습데이터, 프롬프트, 검색 문서, 평가셋, 배포 파이프라인이 연결된 복합 시스템이다. 이 구조에서는 단일 모델 성능만으로 보안성을 판단하기 어렵다.

### 1.2 문제 제기

프롬프트 인젝션, benchmark contamination, privacy leakage, 재현성 실패는 서로 다른 단계에서 발생하지만 최종적으로 모델 신뢰성과 연구 결과의 무결성을 함께 훼손한다.

### 1.3 연구 목적

본 연구는 AI 보안 위협을 생명주기 관점에서 정리하고, 성능·공격 영향·프라이버시·재현성·AI 활용 고지를 함께 확인하는 평가 프레임워크를 제안한다.

### 1.4 논문 구성

2장은 관련연구, 3장은 연구문제, 4장은 연구방법과 위협모형, 5장은 분석 및 실험 설계, 6장은 보안적 함의, 7장은 결론을 제시한다.


---

## 2. 관련연구

### 2.1 국내 연구

국내 연구는 최종 제출 전 KCI, DBpia, RISS에서 AI 보안, 개인정보보호, 연구윤리 관련 문헌을 검증해 보완한다. 현재 단계에서는 허위 인용 방지를 위해 구체 제목을 확정하지 않는다.

### 2.2 해외 연구

해외 연구는 LLM 평가, LLM 보안·프라이버시, 프롬프트 인젝션, 멤버십 추론, MLOps 재현성 문헌을 중심으로 정리한다.

### 2.3 선행연구 비교

> 표 1. 관련연구 비교표 삽입

### 2.4 기존 연구의 한계

개별 survey는 위협과 방어를 폭넓게 다루지만, 제출 가능한 연구 프로세스에서 참고문헌 검증, 실험 재현성, AI 활용 고지를 통합하는 절차는 충분히 구체화되어 있지 않다.

### 2.5 본 연구의 차별점

본 연구는 공격 절차를 상세히 제공하지 않고도 보안 평가가 가능하도록 위협모형, 평가 지표, 재현성 기록, 연구윤리 점검을 하나의 프레임워크로 묶는다.


---

## 3. 연구문제 또는 연구가설

### 3.1 연구문제

> RQ1. LLM/RAG 기반 AI 시스템의 생명주기에서 prompt injection, benchmark contamination, privacy leakage는 각각 어느 단계에서 발생하는가?

> RQ2. AI 보안 연구에서 clean performance, attack impact, privacy leakage, reproducibility를 함께 평가하려면 어떤 공통 평가 항목이 필요한가?

> RQ3. 허위 인용, 실험결과 조작, AI 활용 은폐를 줄이기 위한 참고문헌·실험·AI 고지 체크리스트는 어떻게 구성되어야 하는가?

### 3.2 연구범위

공개 문헌과 공개 또는 synthetic data 기반 toy evaluation을 대상으로 한다. 실제 개인정보, 실제 서비스 침해, 무단 API 공격은 제외한다.


---

## 4. 연구방법

### 4.1 연구대상

LLM/RAG 기반 AI 응용과 연구용 평가 파이프라인을 대상으로 한다.

### 4.2 위협모형

공격자는 악성 프롬프트, 오염 문서, 평가셋 누수, 민감정보 노출 유도를 통해 시스템 신뢰성을 저하시킨다.

### 4.3 분석 방법

W07, W08, W11, W14, W15 보고서의 문헌표와 이론노트를 바탕으로 위협-방어-평가 항목을 통합한다.

### 4.4 평가방법

Clean performance, attack impact, privacy leakage, utility, cost, reproducibility, human review를 공통 평가 항목으로 둔다.

### 4.5 수식 및 지표 정의

본 연구의 지표는 실제 서비스 공격 절차를 재현하기 위한 것이 아니라, 공개 데이터 또는 synthetic context 기반 toy evaluation에서 결과를 과장 없이 보고하기 위한 기준이다. 공격 성공률은 `ASR = N_success / N_trials`로 정의하며, 여기서 `N_success`는 사전에 정의한 안전 실패 조건에 도달한 사례 수, `N_trials`는 전체 모의 평가 사례 수를 의미한다. 프라이버시 누수 점수는 `Leakage = N_leak / N_sensitive_tests`로 두며, 실제 개인정보가 아닌 synthetic 민감정보 테스트에만 적용한다.

방어 절차의 효과는 `DPR = N_blocked_or_corrected / N_risky_cases`로 기록한다. 이는 위험 사례 중 human approval, context filtering, 출처 검증 등으로 차단되거나 수정된 비율이다. 방어 적용 후 기능 보존 정도는 `UR = Score_defense / Score_baseline`으로 해석하되, 동일 평가셋과 동일 rubric을 사용한 경우에만 비교한다. 제출 가능성과 연구윤리 측면에서는 `RC = N_checked_items / N_required_items`로 재현성 완성도를 기록하고, AI 활용 고지서·참고문헌 검증표·학회지 양식 출처표 같은 근거 파일의 확인 상태를 함께 점검한다.

수식은 Markdown + LaTeX math로 작성하고, 문서 변환은 Pandoc 또는 선택 학회지 양식에서 확인한다. 필요한 경우 `sympy`로 수식 변형과 계산값을 검산하고, 사용한 도구는 AI 활용 고지 또는 실험 로그에 기록한다.

> 그림 1. 제안 프레임워크 또는 실험 구조도 삽입


---

## 5. 분석 또는 실험

### 5.1 분석 설계

분석은 LLM/RAG 시스템의 생명주기를 데이터, 프롬프트, 검색 문서, 평가셋, 로그, 제출물 단계로 나누고 각 단계의 보호 자산과 실패 조건을 정리하는 방식으로 수행한다.

### 5.2 실험 또는 사례분석 결과

모델 성능 정량 실험은 아직 수행하지 않았으므로 accuracy, F1, attack success rate는 작성하지 않는다. 다만 W15에서는 기말논문 제출 준비를 위한 로컬 재현성·참고문헌·AI 활용 고지 감사를 실행했으며, W15 필수 산출물 47/47, 기말논문 연결 파일 9/9, 로컬 PDF 5개, 가중 참고문헌 검증률 0.70, AI 활용 고지 완성도 9/9를 `04_experiment/outputs/run_log.md`에 기록했다. 이 값은 모델 성능이 아니라 제출 준비 상태를 나타내는 감사 지표다.

사례분석 결과는 LLM/RAG 보안 평가에서 입력·검색 문서·평가셋·로그가 모두 보호 자산이 된다는 점을 보여준다. 특히 RAG 문서 오염은 prompt injection과 결합되고, benchmark contamination은 평가 재현성을 훼손한다.

### 5.3 결과 해석

본 연구는 정량 결과를 새로 주장하기보다, 안전한 평가 설계와 연구윤리 체크리스트를 제시한다.


---

## 6. 보안적 함의

### 6.1 기밀성

프롬프트와 검색 문서에 포함된 민감정보가 모델 출력으로 노출될 수 있다.

### 6.2 무결성

RAG 문서 오염과 benchmark contamination은 모델 응답과 평가 결과의 무결성을 훼손한다.

### 6.3 가용성

과도한 보안 통제는 응답 지연과 비용 증가를 유발할 수 있으므로 utility와 cost를 함께 본다.

### 6.4 프라이버시

privacy leakage와 membership inference 위험은 실제 개인정보가 아닌 synthetic data로 안전하게 평가한다.

### 6.5 안전성

의료, 법률, 보안 조언처럼 안전중요 영역에서는 human approval gate가 필요하다.

### 6.6 책임성

참고문헌 검증, AI 활용 고지, 실험 로그 보존은 연구자의 최종 책임을 명확히 한다.


---

## 7. 결론

### 7.1 연구 요약

본 연구는 LLM/RAG 기반 AI 시스템의 보안 위협을 생명주기 관점에서 정리하고, 재현성 중심 평가 프레임워크를 제안한다.

### 7.2 연구 기여

1. 본 연구는 LLM/RAG 기반 AI 시스템의 데이터·평가·프롬프트 생명주기에서 prompt injection, benchmark contamination, privacy leakage 위협을 분석하고, 재현성 중심의 보안 평가 체크리스트를 제안한다.
2. 본 연구는 기존 AI 보안 survey가 위협 분류와 실험 재현성의 연결을 충분히 제공하지 못하는 한계를 보완하기 위해 clean performance, attack impact, leakage, reproducibility, human review를 포함한 통합 평가 기준을 제시한다.

### 7.3 연구 한계

본 초안은 문헌분석과 설계 중심이며, 모델 성능 실험 결과는 실행 로그와 CSV/JSON 산출물 대조 후 최종 제출 전 보완해야 한다. DOI/URL 검증도 최종 제출 전 확정한다. 현재 W15 기준 P01, P02, P04는 DOI 확인, P05는 부분 확인, P03은 지정 논문 원문 미확보 상태다.

### 7.4 후속 연구

후속 연구에서는 실제 공개 데이터 기반 toy RAG 평가를 수행하고, 국내 문헌 검증을 완료한 뒤 프레임워크의 적용 가능성을 점검한다.


---

## 참고문헌

확인된 참고문헌만 작성한다. 임의 DOI, 허위 논문, 존재하지 않는 저자명은 작성하지 않는다. 참고문헌은 `04_final_paper/06_appendices/reference_verification.md`에서 검증 상태를 관리한다.

---

## AI 활용 고지

AI 활용 내역은 `04_final_paper/06_appendices/ai_disclosure.md`에 기록한다.
