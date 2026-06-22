# W07 발표용 보고서

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W07 |
| 주제 | LLM 학습·정렬·평가 & LLM 보안·프라이버시 |
| 발표 시간 | 8-10분 |
| 권장 슬라이드 수 | 10-13장 |
| 핵심 메시지 | LLM 보안 평가는 utility, ASR, privacy leakage, refusal quality, code vulnerability risk, 재현성을 함께 기록해야 한다. |
| 발표 근거 | `06_report/final/integrated_report_final.md`, `04_experiment/outputs/run_log.md` |

## 2. 한 문장 요약

W07는 LLM의 학습·정렬·평가 원리를 보안 평가 항목으로 바꾸고, synthetic toy 실험으로 정상 유용성, 공격 차단, 프라이버시 누출, 코드 보안 위험을 같은 표에서 비교한다.

## 3. 발표 흐름

| 순서 | 슬라이드 주제 | 핵심 내용 | 시간 |
|---:|---|---|---:|
| 1 | 표지 | W07 주제와 핵심 질문 | 0:30 |
| 2 | 왜 중요한가 | LLM은 prompt/context/output/evaluation이 엮인 시스템 | 1:00 |
| 3 | AI 원리 | pretraining, instruction tuning, alignment, context window | 1:10 |
| 4 | 평가 원리 | benchmark, contamination, reproducibility | 0:50 |
| 5 | 보안 이슈 | data extraction, prompt injection, leakage, code risk | 1:10 |
| 6 | 논문 5편 | evaluation, security/privacy, MLLM, software security 연결 | 1:00 |
| 7 | 위협모형 | 보호 자산과 공격 경로 | 0:55 |
| 8 | 평가 프로토콜 | utility, ASR, leakage, refusal, code vulnerability | 1:00 |
| 9 | Toy 실험 | synthetic prompt category와 toy guard score | 1:00 |
| 10 | 결과 | clean utility 0.866746, prompt ASR 0.150000 | 1:00 |
| 11 | 해석 | over-refusal과 code risk를 함께 봐야 함 | 0:50 |
| 12 | 기말 연결 | LLM/RAG 보안·프라이버시·재현성 평가 프레임워크 | 0:40 |
| 13 | 결론/Q&A | 수치는 로그가 있을 때만 주장 | 0:20 |

## 4. 논문 5편의 발표 역할

| ID | 논문 | 발표에서 맡는 역할 | DOI/URL 상태 |
|---|---|---|---|
| P01 | A Survey on Evaluation of Large Language Models | LLM 평가 범주와 benchmark 문제 | DOI 확인 |
| P02 | Security and Privacy Challenges of Large Language Models | 보안·프라이버시 공격과 방어 분류 | arXiv/PDF 확인, DOI 재검증 |
| P03 | A Survey on Large Language Model Security and Privacy | good/bad/ugly 관점의 보안 활용·공격·취약성 | arXiv/PDF 확인, 출판정보 재검증 |
| P04 | A Survey on Multimodal Large Language Models | MLLM 구조와 hallucination/evaluation | arXiv/PDF 확인, 공식 권호 재검증 |
| P05 | When Software Security Meets Large Language Models | fuzzing, repair, bug detection, bug triage | DOI 확인 |

## 5. AI 원리 설명

- Pretraining은 모델이 대규모 데이터에서 언어 패턴을 학습하는 단계다.
- Instruction tuning과 alignment는 사용자의 지시와 안전 정책에 맞게 응답을 조정한다.
- Context window는 system prompt, 사용자 입력, retrieval 문서가 함께 들어가는 보안 경계다.
- Evaluation benchmark는 능력 측정 도구이지만 contamination과 leakage가 생기면 보안 문제가 된다.

## 6. 보안 이슈 설명

| 항목 | 발표 내용 |
|---|---|
| 보호 자산 | 학습데이터, system prompt, user prompt, context, output, code, logs, benchmark |
| 실패 조건 | 민감정보 노출, 정책 우회, 취약 코드 생성, 평가셋 오염 |
| 평가 지표 | utility, ASR, privacy leakage, refusal quality, code vulnerability, reproducibility |
| 제외 범위 | 실제 LLM/API 호출, 실제 개인정보, 무단 서비스 질의, exploit instruction |

## 7. 실습/실험 결과

정량값은 `04_experiment/outputs/run_log.md` 기준이다.

| 조건 | Utility | Answer rate | ASR | Privacy Leakage | Refusal Quality | Code vuln. rate |
|---|---:|---:|---:|---:|---:|---:|
| Clean prompts | 0.866746 | 1.000000 | 0.000000 | 0.000000 | 해당 없음 | 0.000000 |
| Prompt attack simulation | 0.400908 | 0.150000 | 0.150000 | 0.000000 | 0.850000 | 0.000000 |
| Privacy-risk prompts | 0.392926 | 0.100000 | 0.100000 | 0.025000 | 0.900000 | 0.000000 |
| Code security prompts | 0.678267 | 0.650000 | 0.000000 | 0.000000 | 해당 없음 | 0.200000 |

## 8. 기말논문 연결

| 기말논문 장 | 발표에서 연결할 내용 |
|---|---|
| 서론 | LLM/RAG 시스템의 보안·프라이버시·재현성 평가 필요성 |
| 관련연구 | LLM evaluation, security/privacy, MLLM, software security survey |
| 연구문제 | 다중지표 LLM 보안 평가 프로토콜 |
| 연구방법 | synthetic prompt category, 위협모형, 로그 기반 재현성 |
| 분석/실험 | utility, ASR, leakage, refusal, code risk |
| 보안적 함의 | prompt/context boundary와 accountability |

## 9. 결론 메시지

1. LLM 보안 평가는 정상 유용성과 위험 차단을 함께 봐야 한다.
2. ASR만 낮추면 over-refusal을 놓칠 수 있고, utility만 보면 leakage와 code risk를 놓칠 수 있다.
3. 수치는 seed, config, CSV/JSON/run log가 있을 때만 주장한다.
4. W07은 기말논문의 LLM/RAG 보안 평가 프레임워크로 직접 연결된다.

## 10. 예상 질문과 답변

| 질문 | 답변 요지 | 근거 파일 |
|---|---|---|
| 왜 실제 LLM을 호출하지 않았나? | 주차 목적은 공격 재현이 아니라 평가표와 로그 구조를 안전하게 검증하는 것이다. | `04_experiment/experiment_report.md` |
| ASR 0.150000은 실제 공격 성공률인가? | 아니다. synthetic toy guard simulator에서 나온 평가 형식 검증용 값이다. | `04_experiment/outputs/run_log.md` |
| Code vulnerability rate 0.200000은 무엇인가? | code security 조건에서 toy vulnerability risk flag가 켜진 비율이다. | `04_experiment/src/run_experiment.py` |
| DOI는 모두 확정인가? | P01/P05는 PDF 기준 DOI 확인, P02/P03/P04는 arXiv/PDF 기준 확인과 출판정보 재검증이 필요하다. | `01_papers/doi_check.md` |
