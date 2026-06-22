# W07 LLM 학습·정렬·평가 & LLM 보안·프라이버시 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W07 |
| 주제 | LLM 학습·정렬·평가 & LLM 보안·프라이버시 |
| AI 원리 | LLM 학습, 추론, 정렬, 평가 프레임워크 |
| 보안 이슈 | 데이터 추출, 프롬프트 기반 공격, 프라이버시 누출, 소프트웨어 보안 접점 |
| 문서 상태 | 최종본 |
| 실험 상태 | synthetic toy 실험 실행 완료 |
| 실행 근거 | `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json` |

## 1. 한 문장 요약

W07는 LLM을 단순 생성 모델이 아니라 학습 데이터, prompt, context, output, 평가셋, 코드 산출물이 연결된 보안 평가 대상 시스템으로 보고, utility, ASR, privacy leakage, refusal quality, code vulnerability risk를 함께 기록하는 평가 프로토콜로 정리한다.

## 2. AI 원리 70% 정리

LLM의 기본 원리는 대규모 말뭉치 기반 pretraining, instruction tuning, alignment, RLHF 또는 preference optimization, tokenization, context window, decoding, benchmark evaluation으로 구성된다. 이 원리를 알아야 보안 이슈도 정확히 위치시킬 수 있다. 예를 들어 training data memorization은 pretraining corpus와 연결되고, prompt injection은 inference-time context 구성과 연결되며, benchmark contamination은 평가 데이터 관리와 연결된다.

| 개념 | W07 해석 | 보안 평가 연결 |
|---|---|---|
| Pretraining | 대규모 데이터에서 언어 패턴을 학습 | 학습데이터 추출, memorization |
| Instruction tuning | 지시 따르기 능력 강화 | unsafe instruction 대응 품질 |
| Alignment/RLHF | 선호와 안전 정책에 맞게 조정 | refusal quality, over-refusal |
| Context window | 입력·검색문서·system prompt가 함께 들어가는 공간 | prompt injection, prompt leakage |
| Benchmark evaluation | 모델 능력을 과제별로 측정 | contamination, evaluation leakage |
| Multimodal LLM | 이미지·텍스트 등 복수 modality를 LLM 추론에 연결 | multimodal prompt injection, hallucination |
| Code LLM | 코드 생성·분석·수정에 LLM 활용 | vulnerable code generation, bug triage 품질 |

### 2.1 핵심 수식 또는 알고리즘 쉬운 설명

아래 수식은 원문 수식의 직접 인용이 아니라, 각 논문의 핵심 개념을 보고서에서 설명하기 위한 대표 수식과 지표다. 최종 제출본에서 원문 수식으로 인용할 경우 논문 원문 쪽/절 번호를 추가 확인한다.

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보안 평가 연결 |
|---|---|---|---|
| P01 | $Score=\frac{1}{K}\sum_k s_k$ | LLM 평가는 여러 능력·위험 항목을 나누어 평균 또는 가중합으로 본다. | LLM evaluation taxonomy |
| P02 | $Risk=N_{unsafe}/N_{prompts}$ | 안전하지 않은 답변 비율을 따로 세어야 성능과 위험을 분리할 수 있다. | LLM security/privacy risk |
| P03 | $TotalRisk=\sum_i w_i r_i$ | LLM 보안은 jailbreak, privacy, misuse 같은 여러 위험을 가중합으로 관리할 수 있다. | Good/Bad/Ugly taxonomy |
| P04 | $z=f_{align}(z_{text},z_{image})$ | multimodal LLM은 이미지와 텍스트 표현을 맞추므로 한쪽 입력의 오염이 다른 쪽 판단에 영향을 줄 수 있다. | multimodal attack surface |
| P05 | $VulnRate=N_{vulnerable}/N_{code}$ | 코드 보안 LLM 평가는 생성 코드 중 취약한 산출물 비율을 별도 측정한다. | software security meets LLMs |

## 3. 보안 이슈 30% 정리

W07의 보안 이슈는 공격 절차 자체보다 보호 자산과 평가 항목을 중심으로 읽어야 한다. LLM 시스템의 주요 보호 자산은 학습데이터, 시스템 프롬프트, 사용자 입력, retrieval context, 모델 응답, 코드 산출물, 로그, 평가셋이다.

| 관점 | 관련 위협 | 평가 연결 |
|---|---|---|
| Confidentiality | training data extraction, prompt leakage | privacy leakage rate, secret exposure flag |
| Integrity | prompt injection, jailbreak, context manipulation | ASR, refusal quality |
| Availability | denial of wallet, abuse traffic | scope note, 운영 실험 제외 |
| Privacy | sensitive information disclosure, memorization | synthetic privacy-risk prompts |
| Safety | harmful generation, insecure code | code vulnerability rate |
| Accountability | benchmark contamination, audit failure | seed/config/output log 보존 |

## 4. 논문 5편 요약

| ID | 문헌 | 역할 | DOI/URL 상태 |
|---|---|---|---|
| P01 | Chang et al., *A Survey on Evaluation of Large Language Models* | LLM 평가 범주, benchmark, evaluation discipline 정리 | DOI `10.1145/3641289` PDF 기준 확인 |
| P02 | Das, Amini, Wu, *Security and Privacy Challenges of Large Language Models* | LLM 보안·프라이버시 공격과 방어 분류 | arXiv `2402.00888`, 출판사 DOI 재검증 필요 |
| P03 | Yao et al., *A Survey on Large Language Model Security and Privacy: The Good, the Bad, and the Ugly* | LLM의 보안 활용, 공격 활용, 취약성 분류 | arXiv `2312.02003`, 출판정보 재검증 필요 |
| P04 | Yin et al., *A Survey on Multimodal Large Language Models* | MLLM 구조, instruction tuning, hallucination, multimodal evaluation | arXiv `2306.13549`, 공식 권호/DOI 재검증 필요 |
| P05 | Zhu et al., *When Software Security Meets Large Language Models* | fuzzing, unit test, program repair, bug detection, bug triage와 LLM 연결 | DOI `10.1109/JAS.2024.124971` PDF 기준 확인 |

## 5. 논문 5편 비교

P01은 평가 방법론, P02와 P03은 LLM 보안·프라이버시 분류, P04는 multimodal 확장, P05는 소프트웨어 보안 접점을 담당한다. 다섯 편을 합치면 LLM 보안 평가가 단일 공격 성공률만으로 끝나지 않고 utility, refusal, leakage, code risk, 재현성을 함께 기록해야 한다는 결론으로 이어진다.

## 6. Research Track

### 6.1 연구문제

RQ1. LLM 평가 벤치마크의 오염과 leakage는 모델 성능 해석과 보안성 평가에 어떤 영향을 미치는가?

RQ2. LLM 시스템에서 데이터 추출, prompt injection, code generation 취약성은 어떤 공통 공격면을 갖는가?

RQ3. Utility, ASR, privacy leakage, refusal quality, code vulnerability, reproducibility를 함께 측정하는 최소 평가 프로토콜은 어떻게 설계할 수 있는가?

### 6.2 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | LLM 기반 질의응답, 코드 생성, 멀티모달 LLM |
| 보호 자산 | 학습데이터, 시스템 프롬프트, 사용자 입력, context, 모델 응답, 코드 산출물, 로그, 평가셋 |
| 공격자 | 외부 사용자, 악성 prompt 작성자, 반복 질의자, 내부 로그 접근자 |
| 공격자 지식 | black-box 또는 gray-box 중심 |
| 공격 경로 | 사용자 입력, retrieval context, API, 로그, 코드 생성 결과 |
| 성공 조건 | 민감정보 노출, 정책 우회, 취약 코드 생성, 평가 오염 |
| 방어자 가정 | 입력 필터링, 출력 검증, 로그 감사, 평가 데이터 관리 가능 |
| 제외 범위 | 실제 개인정보 추출, 실제 서비스 공격, 무단 우회, exploit instruction |

### 6.3 평가방법

| 평가 항목 | 지표 | W07 실습 연결 |
|---|---|---|
| Utility | utility score, answer rate | clean prompts에서 정상 지원성 확인 |
| Attack success | ASR | prompt attack simulation의 unsafe answer 비율 |
| Privacy leakage | leakage rate | privacy-risk prompts의 synthetic leakage flag |
| Refusal quality | risky request refusal ratio | 공격·프라이버시 조건의 차단 품질 |
| Code security | code vulnerability rate | code security prompts의 취약 코드 위험 flag |
| Reproducibility | seed/config/log | `outputs/` CSV/JSON/run log 보존 |

### 6.4 재현성

실험은 seed 42, condition별 40개 synthetic sample, guard threshold 0.55로 실행했다. 산출물은 `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md`에 저장했다. 실제 LLM/API 호출이 없으므로 수치는 모델 성능이 아니라 평가표와 기록 구조 검증용이다.

### 6.5 한계와 오픈문제

1. Synthetic toy score는 실제 LLM의 jailbreak 저항성이나 privacy leakage 확률로 일반화할 수 없다.
2. P02, P03, P04는 로컬 PDF 기준 arXiv 정보와 프롬프트의 출판정보가 달라 공식 출판정보 재검증이 필요하다.
3. 실제 연구로 확장하려면 공개 benchmark, 정책 라벨, 복수 모델, 복수 seed, 사람 평가자 간 agreement가 필요하다.

## 7. 실습 요약

| 조건 | Utility | Answer rate | ASR | Privacy Leakage | Refusal Quality | Over-refusal | Code vuln. rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Clean prompts | 0.866746 | 1.000000 | 0.000000 | 0.000000 | 해당 없음 | 0.000000 | 0.000000 |
| Prompt attack simulation | 0.400908 | 0.150000 | 0.150000 | 0.000000 | 0.850000 | 0.000000 | 0.000000 |
| Privacy-risk prompts | 0.392926 | 0.100000 | 0.100000 | 0.025000 | 0.900000 | 0.000000 | 0.000000 |
| Code security prompts | 0.678267 | 0.650000 | 0.000000 | 0.000000 | 해당 없음 | 0.350000 | 0.200000 |

## 8. AI 활용 기록 요약

Codex를 사용해 로컬 파일 점검, W07 문서 구조화, synthetic 실험 코드 작성, 실행 결과 정리, 제출본과 발표자료 작성을 수행했다. 정량값은 실행 로그와 CSV/JSON에 있는 값만 사용했고, DOI/URL은 PDF에서 확인된 값과 arXiv 식별자만 기록했다.

## 9. 토론 질문

1. LLM 보안 평가는 ASR을 낮추는 것과 over-refusal을 낮추는 것 중 어떤 균형을 우선해야 하는가?
2. Benchmark contamination은 성능 평가 문제인가, 보안 문제인가, 연구윤리 문제인가?
3. Code LLM의 취약 코드 생성 위험은 refusal로 막는 것이 좋은가, secure rewrite로 유도하는 것이 좋은가?

## 10. 기말 논문 연결

W07는 기말논문의 “LLM/RAG 기반 AI 시스템의 보안·프라이버시·재현성 평가 프레임워크”에서 핵심 반영 주차다. 관련연구에는 LLM evaluation/security/privacy/software security survey를 반영하고, 연구방법에는 synthetic prompt 평가표, 위협모형, 재현성 로그 구조를 반영한다.

## 11. 참고문헌 검증표

참고문헌 검증 상태는 `01_papers/doi_check.md`에 관리한다. P01/P05는 PDF 기준 DOI를 확인했고, P02/P03/P04는 arXiv/PDF 기준 확인 상태로 남겨 공식 출판정보 확인을 후속 작업으로 둔다.

## 12. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 완료 |
| 비교표 | 완료 |
| AI 원리 70% | 완료 |
| 보안 이슈 30% | 완료 |
| Research Track | 완료 |
| synthetic 실험 코드 | 완료 |
| 실행 로그/CSV/JSON | 완료 |
| 제출용 보고서 | 완료 |
| 발표자료 | 완료 |
| AI 활용 고지 | 완료 |
| DOI 임의 생성 방지 | 완료 |
