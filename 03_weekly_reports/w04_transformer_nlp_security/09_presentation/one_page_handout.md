# W04 1페이지 발표 요약

## 주제

Transformer 변형 & NLP 대적공격·프라이버시

## 핵심 주장

프롬프트 기반 NLP 보안 평가는 clean score 하나로 끝나지 않는다. 단어 치환 공격 영향, privacy leakage, utility, 재현성 근거를 분리해서 기록해야 한다.

## 발표 흐름

| 구분 | 핵심 내용 |
|---|---|
| AI 원리 | Transformer는 self-attention으로 토큰 관계를 계산하고, Efficient Transformer는 긴 입력 비용을 줄인다. |
| 보안 이슈 | 단어 치환 공격은 키워드 기반 탐지를 우회할 수 있고, prompt privacy는 입력·응답·로그 노출을 다룬다. |
| 문헌 역할 | P01-P03은 Transformer/X-former 원리, P04-P05는 NLP 공격 방어와 prompt privacy를 담당한다. |
| 평가 관점 | clean score, ASR, privacy leakage, utility score, reproducibility를 분리한다. |
| 기말 연결 | 프롬프트 기반 AI 시스템의 민감정보 보호 평가체계로 발전시킨다. |

## Toy 실험 요약

| 항목 | 내용 |
|---|---|
| 데이터 | synthetic privacy-risk prompts |
| 분류기 | keyword privacy-risk detector |
| 공격 | `password`, `ssn`, `token` 우회 표현 치환 |
| 방어 | regex masking + privacy-preserving prompt wrapper |
| 산출물 | `metrics_summary.csv`, `results.json`, `run_log.md` |

## 주요 결과

정량값은 `04_experiment/outputs/run_log.md` 기준이다.

| 조건 | Clean Score | ASR | Leakage | Utility |
|---|---:|---:|---:|---:|
| Clean baseline | 1.000000 | 해당 없음 | 해당 없음 | 1.000000 |
| Word substitution | 0.625000 | 0.750000 | 해당 없음 | 1.000000 |
| Prompt masking | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 |
| Privacy-preserving prompt | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 |

## 해석

- 단어 치환 후 privacy-risk 입력 4개 중 3개가 benign으로 오분류됐다.
- 마스킹 후 synthetic 원시 민감값 패턴은 남지 않았다.
- 이 결과는 toy 설정의 관찰값이며 실제 LLM 보안 성능으로 일반화하지 않는다.

## DOI/URL 상태

| ID | 상태 |
|---|---|
| P01 | arXiv DOI 확인 |
| P02 | ACM 출판 DOI 확인 |
| P03 | AI Open 출판 DOI 확인 |
| P04 | arXiv DOI 확인 |
| P05 | arXiv DOI 확인 |

## 관련 산출물

| 파일 | 용도 |
|---|---|
| `presentation_report.md` | 발표용 보고서 |
| `presentation_slides.md` | 슬라이드 원본 |
| `presentation_slides.html` | 브라우저 발표용 슬라이드 |
| `speaker_notes.md` | 슬라이드별 발표자 대본 |
| `qna.md` | 예상 질문과 답변 |
| `04_experiment/outputs/run_log.md` | 실험 수치 근거 |
