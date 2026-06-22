# W07 제출용 보고서

## 표지

| 항목 | 내용 |
|---|---|
| 주차 | W07 |
| 보고서 제목 | LLM 학습·정렬·평가 & LLM 보안·프라이버시 |
| 과목 범위 | AI 보안 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 통합본 |
| 관련 산출물 위치 | `03_weekly_reports/w07_llm_security_privacy/` |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## 초록

본 보고서는 LLM의 pretraining, instruction tuning, alignment, evaluation benchmark를 AI 원리 관점에서 정리하고, training data extraction, prompt injection, prompt leakage, privacy leakage, insecure code generation을 보안 평가 관점에서 분석한다. 문헌 5편을 통해 LLM evaluation, LLM security/privacy, multimodal LLM, software security 접점을 비교했다. 실습에서는 실제 LLM/API를 호출하지 않고 synthetic prompt category와 toy guard score simulator를 사용해 utility, ASR, privacy leakage, refusal quality, code vulnerability rate를 기록했다. 결과적으로 clean prompts utility는 0.866746, prompt attack simulation ASR은 0.150000, privacy-risk leakage는 0.025000, code security prompts의 code vulnerability rate는 0.200000이었다.

**키워드:** LLM evaluation, alignment, prompt injection, privacy leakage, refusal quality, code security, reproducibility

## 1. AI 원리 70%

LLM은 대규모 pretraining으로 언어 패턴을 학습하고 instruction tuning과 alignment를 통해 지시 따르기와 안전 정책 적합성을 높인다. Context window는 system prompt, 사용자 입력, retrieval 문서, 대화 이력을 함께 담기 때문에 inference-time 보안 경계가 된다.

평가는 benchmark score만으로 충분하지 않다. Benchmark contamination, evaluation leakage, prompt sensitivity, hallucination, multimodal input 처리 문제를 함께 봐야 모델 능력과 위험을 분리할 수 있다.

## 2. 보안 이슈 30%

| 관점 | 관련 위협 | W07 평가 연결 |
|---|---|---|
| Confidentiality | training data extraction, prompt leakage | privacy leakage rate |
| Integrity | prompt injection, jailbreak | ASR, refusal quality |
| Privacy | sensitive information disclosure | synthetic privacy-risk prompts |
| Safety | harmful generation, insecure code | code vulnerability rate |
| Accountability | benchmark contamination, audit failure | seed/config/output log |

## 3. 문헌 요약

| ID | 문헌 | DOI/URL 상태 | 활용 |
|---|---|---|---|
| P01 | A Survey on Evaluation of Large Language Models | DOI `10.1145/3641289` | LLM 평가 범주와 benchmark 관리 |
| P02 | Security and Privacy Challenges of Large Language Models | arXiv `2402.00888`, DOI 재검증 필요 | LLM 보안·프라이버시 위협과 방어 |
| P03 | A Survey on Large Language Model Security and Privacy: The Good, the Bad, and the Ugly | arXiv `2312.02003`, 출판정보 재검증 필요 | 보안 활용·공격 활용·취약성 분류 |
| P04 | A Survey on Multimodal Large Language Models | arXiv `2306.13549`, 공식 권호/DOI 재검증 필요 | MLLM 구조와 hallucination/evaluation |
| P05 | When Software Security Meets Large Language Models | DOI `10.1109/JAS.2024.124971` | LLM과 software security 접점 |

## 4. Research Track

| 항목 | 내용 |
|---|---|
| 연구문제 | LLM 보안 평가에서 utility, ASR, leakage, refusal, code risk, reproducibility를 함께 측정하는 최소 프로토콜은 무엇인가 |
| 대상 시스템 | LLM 기반 질의응답, 코드 생성, 멀티모달 LLM |
| 보호 자산 | 학습데이터, 시스템 프롬프트, 사용자 입력, context, 모델 응답, 코드 산출물, 로그, 평가셋 |
| 위협 | 데이터 추출, prompt injection, prompt leakage, insecure code generation, benchmark contamination |
| 평가 지표 | utility, answer rate, ASR, privacy leakage, refusal quality, over-refusal, code vulnerability rate |
| 재현성 | seed 42, config, script, CSV/JSON/run log 보존 |
| 제외 범위 | 실제 개인정보 추출, 실제 LLM/API 질의, 무단 서비스 공격, exploit instruction |

## 5. 실습/실험 결과

실습 코드는 `04_experiment/src/run_experiment.py`에 작성했다. 실행 명령은 `python3 src/run_experiment.py --config configs/config.yaml`이며 결과는 `04_experiment/outputs/`에 저장했다.

| 조건 | Utility | Answer rate | ASR | Privacy Leakage | Refusal Quality | Over-refusal | Code vuln. rate | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Clean prompts | 0.866746 | 1.000000 | 0.000000 | 0.000000 | 해당 없음 | 0.000000 | 0.000000 | 정상 질의 지원성 확인 |
| Prompt attack simulation | 0.400908 | 0.150000 | 0.150000 | 0.000000 | 0.850000 | 0.000000 | 0.000000 | 추상 공격 카테고리 대부분 차단 |
| Privacy-risk prompts | 0.392926 | 0.100000 | 0.100000 | 0.025000 | 0.900000 | 0.000000 | 0.000000 | synthetic leakage 낮게 기록 |
| Code security prompts | 0.678267 | 0.650000 | 0.000000 | 0.000000 | 해당 없음 | 0.350000 | 0.200000 | 취약 코드 위험과 과차단을 함께 확인 |

이 결과는 synthetic toy 실험의 평가 형식 검증용 수치다. 실제 LLM 보안 성능, 실제 jailbreak 성공률, 실제 개인정보 누출 가능성, 실제 코드 보안 품질로 일반화하지 않는다.

## 6. 발표자료 위치

| 파일 | 용도 |
|---|---|
| `09_presentation/presentation_report.md` | 발표용 보고서 |
| `09_presentation/presentation_slides.md` | 슬라이드 원본 |
| `09_presentation/presentation_slides.html` | 브라우저 발표용 슬라이드 |
| `09_presentation/speaker_notes.md` | 발표자 대본 |
| `09_presentation/qna.md` | 예상 질문과 답변 |
| `09_presentation/one_page_handout.md` | 1페이지 배포자료 |

## 7. 기말논문 연결

추천 주제는 “LLM/RAG 기반 AI 시스템의 보안·프라이버시·재현성 평가 프레임워크”이다. W07의 기여 후보는 LLM 보안 평가 지표표, prompt/context 중심 위협모형, code security risk와 over-refusal의 동시 기록, seed/config/output 기반 재현성 구조이다.

## 8. AI 활용 고지

Codex를 사용해 로컬 파일 점검, 문헌 요약 구조화, PDF 기준 서지정보 보정, synthetic 실험 코드 작성과 실행, 제출용 보고서 및 발표자료 작성을 수행했다. 정량값은 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 사용했다. 상세 기록은 `05_ai_worklog/`에 있다.

## 9. 제출 전 점검표

| 점검 항목 | 상태 |
|---|---|
| 논문 요약 5편 | 완료 |
| 논문 비교표 | 완료 |
| AI 원리/보안 이슈 | 완료 |
| Research Track | 완료 |
| 실험 코드 | 완료 |
| 실험 결과 | 완료 |
| DOI/URL 검증표 | 부분 완료 |
| AI 활용 고지 | 완료 |
| 발표자료 | 완료 |
