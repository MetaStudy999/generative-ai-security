# W04 제출용 보고서

## 표지

| 항목 | 내용 |
|---|---|
| 주차 | W04 |
| 보고서 제목 | Transformer 변형 & NLP 대적공격·프라이버시 |
| 과목 범위 | AI 보안 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 통합본 |
| 관련 산출물 위치 | `03_weekly_reports/w04_transformer_nlp_security/` |

## 초록

본 보고서는 Transformer 변형과 NLP 보안 위협을 함께 다룬다. AI 원리 측면에서는 self-attention, multi-head attention, positional encoding, sparse attention, low-rank approximation, kernelized attention 등 Efficient Transformer 계열의 계산 복잡도 완화 전략을 정리한다. 보안 측면에서는 단어 치환 기반 NLP 대적공격, 프롬프트 프라이버시, in-context learning 환경의 민감정보 노출, privacy-preserving prompt engineering을 분석한다. 다섯 편의 문헌을 비교하고, synthetic privacy-risk prompts 기반 toy experiment를 실행해 clean score, attack success rate, privacy leakage, utility score를 분리 기록했다. 결론적으로 W04는 기말논문의 “프롬프트 기반 AI 시스템의 민감정보 보호 평가체계”로 발전 가능하다.

**키워드:** Transformer, X-former, sparse attention, NLP adversarial attack, prompt privacy, ICL, privacy-preserving prompt engineering

## 1. AI 원리 70%

Transformer는 입력 토큰 사이의 관계를 self-attention으로 계산한다. Query, Key, Value는 각각 질의, 비교 기준, 전달 정보를 맡고, attention score는 입력 문맥에서 어떤 토큰을 더 볼지 결정한다. Multi-head attention은 서로 다른 관점의 관계를 병렬로 학습한다. Positional encoding은 순서 정보가 없는 attention 구조에 위치 정보를 더한다.

Efficient Transformer 계열은 길이가 긴 입력에서 self-attention의 계산·메모리 비용이 커지는 병목을 줄이려 한다. 대표 접근은 sparse attention, low-rank approximation, kernelized attention, memory/compression 기반 attention, parameter sharing, distillation 등이다. W04에서는 이 원리를 LLM 입력 프롬프트와 NLP 보안 평가의 기반 구조로 연결한다.

## 2. 보안 이슈 30%

NLP 대적공격은 의미를 크게 바꾸지 않으면서 모델 또는 탐지기의 판단을 흔드는 입력 변조를 포함한다. 단어 치환 공격은 키워드 기반 탐지기를 우회하기 쉽고, 문장 재구성 공격은 표면형을 바꿔도 의미가 유지될 수 있다. 프롬프트 프라이버시는 사용자가 입력한 민감정보가 모델 응답, 로그, ICL 예시, 외부 도구 호출 과정에서 노출될 위험을 다룬다.

| 관점 | 관련 위협 | W04 평가 연결 |
|---|---|---|
| Confidentiality | 프롬프트 민감정보 노출 | masking 후 privacy leakage |
| Integrity | 단어 치환 공격 | attack success rate |
| Availability | 입력 변조에 따른 성능 저하 | clean score와 공격 후 score 분리 |
| Privacy | ICL 예시의 개인정보 포함 | synthetic prompt만 사용 |
| Accountability | 로그와 근거 누락 | CSV/JSON/run_log 보존 |

## 3. 문헌 요약

| ID | 문헌 | DOI/URL 상태 | 활용 |
|---|---|---|---|
| P01 | Efficient Transformers: A Survey | arXiv DOI `10.48550/arXiv.2009.06732` | Efficient Transformer와 X-former 분류 |
| P02 | A Practical Survey on Faster and Lighter Transformers | ACM DOI `10.1145/3586074` | 계산·메모리 효율화 전략 |
| P03 | A survey of transformers | AI Open DOI `10.1016/j.aiopen.2022.10.001` | Transformer 변형 taxonomy |
| P04 | A Survey of Adversarial Defences and Robustness in NLP | arXiv DOI `10.48550/arXiv.2203.06414` | NLP 대적공격 방어 taxonomy |
| P05 | Privacy Preserving Prompt Engineering: A Survey | arXiv DOI `10.48550/arXiv.2404.06001` | prompt privacy와 ICL 보호 방법 |

## 4. Research Track

| 항목 | 내용 |
|---|---|
| 연구문제 | 프롬프트 기반 NLP 시스템에서 민감정보 보호, 공격 우회, 유용성을 함께 평가하는 최소 지표는 무엇인가 |
| 대상 시스템 | Transformer 기반 NLP 모델, LLM 프롬프트 시스템, 키워드 기반 프라이버시 탐지기 |
| 위협 | 단어 치환 우회, 프롬프트 민감정보 노출, 로그 잔존 위험 |
| 평가 지표 | clean score, attack success rate, privacy leakage, utility score, reproducibility |
| 재현성 | Dockerfile, pyproject.toml, config, seed 42, `outputs/` 로그 보존 |
| 제외 범위 | 실제 개인정보, 실제 서비스 공격, 무단 API 질의, 운영 시스템 침해 |

## 5. 실습/실험 결과

실습 코드는 `04_experiment/src/run_experiment.py`에 작성했다. 실행 명령은 `python src/run_experiment.py --config configs/config.yaml`이며, 결과는 `04_experiment/outputs/`에 저장했다.

| 조건 | Clean Score | Attack Success Rate | Privacy Leakage | Utility Score | 해석 |
|---|---:|---:|---:|---:|---|
| Clean baseline | 1.000000 | 해당 없음 | 해당 없음 | 1.000000 | 정상 입력에서 keyword detector가 synthetic 라벨을 모두 맞춤 |
| Word substitution | 0.625000 | 0.750000 | 해당 없음 | 1.000000 | 민감 키워드 우회로 일부 privacy-risk 입력이 benign으로 오분류 |
| Prompt masking | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 | 정규식 마스킹 후 synthetic 민감값 노출 없음 |
| Privacy-preserving prompt | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 | 마스킹과 정책 지시를 결합해 입력 의도만 유지 |

이 결과는 synthetic toy 실험의 평가 형식 검증용 수치다. 실제 Transformer, LLM, 상용 NLP 시스템의 강건성 또는 프라이버시 보호 성능으로 일반화하지 않는다.

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

추천 주제는 “프롬프트 기반 AI 시스템의 민감정보 보호 평가체계”이다. 기여 후보는 prompt privacy threat model, masking/policy control checklist, clean score와 privacy leakage의 동시 평가표, 실행 로그 기반 재현성 기준이다.

## 8. AI 활용 고지

Codex를 사용해 문헌 요약 구조화, DOI/URL 검증 보조, synthetic 실험 코드 작성과 실행, 제출용 보고서 및 발표자료 작성을 수행했다. DOI와 URL은 확인 근거 수준을 구분해 반영했고, 정량값은 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 사용했다. 상세 기록은 `05_ai_worklog/`에 있다.

## 9. 제출 전 점검표

| 점검 항목 | 상태 |
|---|---|
| 논문 요약 5편 | 완료 |
| 논문 비교표 | 완료 |
| AI 원리/보안 이슈 | 완료 |
| Research Track | 완료 |
| 실험 코드 | 완료 |
| 실험 결과 | 완료 |
| DOI/URL 검증표 | 완료 |
| AI 활용 고지 | 완료 |
| 발표자료 | 완료 |
