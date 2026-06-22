# W15 제출용 보고서

## 1. 표지

| 항목 | 내용 |
|---|---|
| 주차 | W15 |
| 보고서 제목 | 연구평가·재현성·설명가능성(XAI)·논문 구성 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 통합본 |
| 최종 보고서 | `06_report/final/integrated_report_final.md` |
| 실험 근거 | `04_experiment/outputs/run_log.md` |
| 발표자료 | `09_presentation/` |

## 2. 초록과 키워드

본 보고서는 LLM 평가, ML lifecycle assurance, XAI, concept-based explanation을 바탕으로 AI 보안 연구의 재현성·평가 신뢰성·연구윤리 점검 절차를 정리한다. W15 실습은 모델 성능 실험이 아니라 로컬 산출물 감사로 수행했으며, W15 필수 파일, 기말논문 연결 파일, DOI/URL 검증 상태, AI 활용 고지 완성도를 확인했다. P01, P02, P04는 DOI를 확인했고, P03은 지정 논문과 로컬 대체 PDF가 불일치하며, P05는 arXiv URL은 확인했으나 최종 DOI가 필요하다.

키워드: LLM Evaluation, Reproducibility, XAI, Benchmark Contamination, AI Disclosure, Reference Verification

## 3. AI 원리 70%와 보안 이슈 30%

| 구분 | 핵심 내용 |
|---|---|
| AI 원리 70% | LLM 평가 프레임워크, benchmark contamination, reproducibility, ML lifecycle assurance, XAI, concept-based explanation, contribution/limitation 작성 |
| 보안 이슈 30% | hidden test leakage, model leakage, explanation misuse, fabricated citation, AI 활용 은폐, 재현성 실패 |

AI 보안 연구에서 평가는 성능 수치뿐 아니라 데이터 출처, 평가셋 오염 여부, 설명 결과의 충실도, 실험 로그와 AI 활용 고지를 함께 확인해야 한다.

## 4. 논문 5편 요약과 DOI/URL 검증 상태

| ID | 논문 | 핵심 역할 | DOI/URL 상태 |
|---|---|---|---|
| P01 | A Survey on Evaluation of Large Language Models | LLM 평가 대상·benchmark·평가방법 분류 | 확인: `10.1145/3641289` |
| P02 | Assuring the Machine Learning Lifecycle | ML lifecycle assurance와 evidence chain | 확인: `10.1145/3453444` |
| P03 | Explainable AI: Core Ideas, Techniques, and Solutions | XAI 핵심 개념 문헌, 현재 PDF는 대체 문헌 | 미검증: 지정 논문 원문 필요 |
| P04 | Explainable Artificial Intelligence (XAI): Concepts, Taxonomies... | XAI taxonomy와 Responsible AI 연결 | 확인: `10.1016/j.inffus.2019.12.012` |
| P05 | Concept-based Explainable Artificial Intelligence: A Survey | concept-based XAI taxonomy와 평가 지표 | 부분 확인: arXiv `2312.12936`, 최종 DOI 필요 |

## 5. Research Track

| 항목 | 내용 |
|---|---|
| 연구문제 | LLM/RAG 기반 AI 시스템에서 prompt injection, benchmark contamination, privacy leakage를 생명주기 단계별로 분류하고, 재현성 중심 평가항목을 제안한다. |
| 대상 시스템 | AI 모델 평가 시스템, XAI 분석 시스템, AI 보안 논문 작성 프로세스 |
| 보호 자산 | benchmark, hidden test, model version, prompt/template, explanation output, reference list, AI worklog |
| 공격자 | 평가 데이터 오염자, 모델 개발자, 논문 작성자, AI 도구 오용자 |
| 평가 지표 | reference verification rate, reproducibility evidence coverage, AI disclosure completeness, explanation stability, limitation coverage |
| 재현성 | Dockerfile, pyproject.toml, config.yaml, seed 42, outputs/run_log.md, metrics_summary.csv, results.json 보존 |
| 제외 범위 | 실제 개인정보, 실제 서비스 침해, 무단 API 공격, 허위 실험결과 생성 |

## 6. 실습/실험 실행 상태와 결과표

실습은 로컬 감사로 실행 완료했다. 수치는 `04_experiment/outputs/run_log.md`와 일치해야 한다.

| 점검 항목 | 결과 | 상태 | 의미 |
|---|---:|---|---|
| W15 필수 산출물 | 47/47 | complete | 주차 산출물 패키지 완성 |
| 기말논문 연결 파일 | 9/9 | complete | W15와 `04_final_paper/` 연결 |
| 로컬 PDF | 5 | complete | 논문 패킷 파일 존재 |
| DOI 확인 | 3 | partial | P01, P02, P04 확인 |
| DOI 부분 확인 | 1 | partial | P05 arXiv 확인, 최종 DOI 필요 |
| DOI 미검증 | 1 | attention | P03 지정 논문 원문 필요 |
| 가중 참고문헌 검증률 | 0.70 | partial | 확인 1점, 부분 확인 0.5점 기준 |
| AI 활용 고지 완성도 | 9/9 | complete | 고지서 필수 항목 작성 |

## 7. 발표용 보고서 위치

발표자료는 `09_presentation/`에 정리했다. 최종 발표본은 `presentation_slides.html`이며, 발표 보고서, speaker notes, Q&A, one-page handout을 함께 포함한다.

## 8. 기말논문 연결

W15는 기말논문의 연구방법, 평가방법, 보안적 함의, 부록 체크리스트에 직접 연결된다. 최종 contribution은 다음 두 문장으로 압축한다.

1. 본 연구는 LLM/RAG 기반 AI 시스템의 데이터·평가·프롬프트 생명주기에서 prompt injection, benchmark contamination, privacy leakage 위협을 분석하고, 재현성 중심의 보안 평가 체크리스트를 제안한다.
2. 본 연구는 기존 AI 보안 survey가 위협 분류와 실험 재현성의 연결을 충분히 제공하지 못하는 한계를 보완하기 위해 clean performance, attack impact, leakage, reproducibility, human review를 포함한 통합 평가 기준을 제시한다.

## 9. AI 활용 고지

Codex를 사용해 공통 지침 확인, 로컬 PDF/DOI 상태 대조, W15 보고서 구조 보완, 로컬 감사 스크립트 작성, 제출본·발표자료 작성, 기말논문 연결 점검을 수행했다. AI 산출물은 초안이며 최종 원고의 내용, 인용, 실험결과, 연구윤리 책임은 작성자에게 있다.

## 10. 제출 전 점검표

| 점검 항목 | 상태 |
|---|---|
| 통합보고서 최종본 작성 | 완료 |
| 논문 5편 요약과 비교표 작성 | 완료 |
| AI 원리 70%와 보안 이슈 30% 작성 | 완료 |
| Research Track 작성 | 완료 |
| 로컬 감사 outputs 생성 | 완료 |
| 제출용 Markdown/HTML 작성 | 완료 |
| 발표 패키지 작성 | 완료 |
| AI 활용 고지 포함 | 완료 |
| P03 지정 논문 원문 확인 | 확인 필요 |
| P05 최종 DOI 확인 | 확인 필요 |
