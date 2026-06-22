# 99_write_final_paper.md

## Codex 작업 지시서: 기말 모의투고 논문 작성

## 1. 작업 대상

```text
04_final_paper/
```

## 2. 작업 목표

주차별 보고서 중 최소 2개 이상을 반영하여 국내 학회지 형식의 AI 보안 모의투고 논문 초안을 작성한다.

기말 논문은 단순 요약 보고서가 아니다.
한 학기 동안 읽고 분석한 논문, 주차별 보고서, 실습 기록, AI 활용 기록을 바탕으로 하나의 작은 AI 보안 연구문제를 정의하고, 국내 학회지 투고 형식에 맞춘 논문 원고로 구성한다.

---

## 3. 반드시 반영할 자료

다음 자료를 우선 확인하고 기말 논문에 반영하라.

```text
03_weekly_reports/*/08_final_paper_bridge/final_paper_bridge.md
03_weekly_reports/*/08_final_paper_bridge/topic_candidates.md
03_weekly_reports/*/08_final_paper_bridge/contribution_candidates.md
03_weekly_reports/*/08_final_paper_bridge/weekly_reflection_table.md
03_weekly_reports/*/02_paper_summaries/paper_matrix.md
03_weekly_reports/*/03_theory_notes/threat_model.md
03_weekly_reports/*/03_theory_notes/evaluation_protocol.md
03_weekly_reports/*/05_ai_worklog/ai_disclosure_draft.md
```

특히 다음 주차는 기말 논문 주제로 발전 가능성이 높으므로 우선 검토하라.

```text
w07_llm_security_privacy
w08_rag_prompt_injection
w11_differential_privacy_mi
w13_model_stealing_watermarking
w14_mlops_supply_chain
w15_reproducibility_xai_paper
```

---

## 4. 기말 논문 폴더 구조 확인

다음 구조가 없으면 생성하라.

```text
04_final_paper/
├── 00_journal_format
├── 01_planning
├── 02_weekly_reflection
├── 03_related_work
├── 04_methodology_experiment
├── 05_draft
├── 06_appendices
└── 07_final_submission
```

각 폴더에는 다음 파일이 있어야 한다.

```text
04_final_paper/
├── 00_journal_format/
│   ├── journal_format_source.md
│   ├── submission_rule.md
│   └── template_note.md
│
├── 01_planning/
│   ├── final_topic.md
│   ├── research_question.md
│   ├── contribution.md
│   └── paper_outline.md
│
├── 02_weekly_reflection/
│   ├── weekly_reflection_table.md
│   ├── selected_weeks.md
│   └── week_to_paper_mapping.md
│
├── 03_related_work/
│   ├── literature_matrix.md
│   ├── domestic_papers.md
│   ├── international_papers.md
│   └── research_gap.md
│
├── 04_methodology_experiment/
│   ├── methodology.md
│   ├── experiment_design.md
│   ├── threat_model.md
│   └── evaluation_protocol.md
│
├── 05_draft/
│   ├── paper_draft.md
│   ├── 00_title_abstract_keywords.md
│   ├── 01_introduction.md
│   ├── 02_related_work.md
│   ├── 03_research_question.md
│   ├── 04_methodology.md
│   ├── 05_analysis_experiment.md
│   ├── 06_security_implications.md
│   └── 07_conclusion.md
│
├── 06_appendices/
│   ├── ai_disclosure.md
│   ├── reference_verification.md
│   ├── journal_format_source_table.md
│   └── plagiarism_self_check.md
│
└── 07_final_submission/
    └── submit_checklist.md
```

---

## 5. 최종 논문 주제 선정

`04_final_paper/01_planning/final_topic.md`를 작성하라.

다음 형식으로 주제 후보를 비교하라.

```markdown
# 최종 논문 주제 선정

## 1. 주제 후보 비교

| 번호 | 제목 후보 | 반영 주차 | 대상 시스템 | 보안 위협 | 연구방법 | 예상 기여 | 선택 여부 |
|---:|---|---|---|---|---|---|---|
| 1 | RAG 기반 생성형 AI 시스템에서 간접 프롬프트 인젝션 대응 방안 연구 | W08 | RAG 시스템 | 간접 프롬프트 인젝션 | 문헌분석/모의실험/체크리스트 | 방어 평가체계 |  |
| 2 | LLM 보안·프라이버시 평가를 위한 다중지표 프레임워크 연구 | W07 | LLM 시스템 | 데이터 추출·프롬프트 공격 | 평가체계 설계 | 다중지표 평가 |  |
| 3 | AI 공급망 보안을 위한 MLOps 보안통제 프레임워크 연구 | W14 | MLOps 파이프라인 | 공급망 공격 | 체크리스트/프레임워크 | 운영 보안통제 |  |

## 2. 최종 선택 주제

-

## 3. 선택 이유

-

## 4. 선택하지 않은 주제와 제외 이유

-
```

---

## 6. 연구문제 작성

`04_final_paper/01_planning/research_question.md`를 작성하라.

```markdown
# 연구문제

## 1. 연구 배경

-

## 2. 최종 연구문제

> RQ1. 

> RQ2. 

> RQ3. 

## 3. 연구범위

| 항목 | 포함 | 제외 |
|---|---|---|
| 대상 시스템 |  |  |
| 보안 위협 |  |  |
| 데이터 |  |  |
| 실험 |  |  |
| 방어 방법 |  |  |

## 4. 연구질문 검토

| 기준 | 점검 내용 | 확인 |
|---|---|---|
| 명확성 | 검토 가능한 질문인가 | □ |
| 범위 | 한 학기 과제로 가능한 작은 범위인가 | □ |
| 보안성 | AI 보안 주제와 직접 연결되는가 | □ |
| 방법론 | 문헌분석, 사례분석, 모의실험, 체크리스트 중 하나로 수행 가능한가 | □ |
| 기여 | 기존 연구와 구별되는 기여가 있는가 | □ |
```

---

## 7. Contribution 작성

`04_final_paper/01_planning/contribution.md`를 작성하라.

```markdown
# Contribution 정리

## 1. Contribution 후보

### 후보 1

본 연구는 _______ 환경에서 _______ 위협을 분석하고, _______을 제안한다.

### 후보 2

본 연구는 기존 _______ 연구의 한계를 보완하기 위해 _______ 평가 기준을 제시한다.

### 후보 3

본 연구는 _______ 공격에 대한 _______ 기반 점검표를 설계하고, _______ 관점에서 보안적 함의를 도출한다.

## 2. 최종 Contribution

본 연구의 기여는 다음과 같다.

1. 
2. 
3. 

## 3. Contribution 1~2문장 압축

> 본 연구는 _______ 환경에서 발생하는 _______ 위협을 분석하고, _______ 기반의 평가·통제 프레임워크를 제안한다. 이를 통해 기존 연구가 충분히 다루지 못한 _______ 문제를 보완한다.
```

---

## 8. 주차별 보고서 반영표 작성

`04_final_paper/02_weekly_reflection/weekly_reflection_table.md`를 작성하라.

주차별 보고서는 최소 2개 이상 반영해야 한다.

```markdown
# 주차별 보고서 반영표

| 번호 | 기존 보고서 제목 | 반영한 논문 장 | 반영 내용 | 반영 방식 |
|---:|---|---|---|---|
| 1 | W__ _______ | 1장 서론 |  | 문제의식 / 배경 |
| 2 | W__ _______ | 2장 관련연구 |  | 선행연구 비교 |
| 3 | W__ _______ | 4장 연구방법 |  | 위협모형 / 평가방법 |
| 4 | W__ _______ | 5장 분석 또는 실험 |  | 실습 결과 / 모의실험 |
| 5 | W__ _______ | 6장 보안적 함의 |  | CIA / Privacy / Safety 분석 |

## 반영 주차 선정 이유

-
```

---

## 9. 관련연구 비교표 작성

`04_final_paper/03_related_work/literature_matrix.md`를 작성하라.

국내 논문 3편 이상, 해외 논문 5편 이상을 넣을 수 있도록 표를 구성하라.
실제 확인하지 못한 문헌은 `확인 필요`로 표시하고, 임의 DOI를 만들지 말라.

```markdown
# 관련연구 비교표

| 번호 | 구분 | 논문 제목 | 저자 | 연도 | 연구문제 | 방법론 | 한계 | 본 연구와의 차별점 | DOI/URL 검증 |
|---:|---|---|---|---:|---|---|---|---|---|
| 1 | 국내 |  |  |  |  |  |  |  | 확인 필요 |
| 2 | 국내 |  |  |  |  |  |  |  | 확인 필요 |
| 3 | 국내 |  |  |  |  |  |  |  | 확인 필요 |
| 4 | 해외 |  |  |  |  |  |  |  | 확인 필요 |
| 5 | 해외 |  |  |  |  |  |  |  | 확인 필요 |
| 6 | 해외 |  |  |  |  |  |  |  | 확인 필요 |
| 7 | 해외 |  |  |  |  |  |  |  | 확인 필요 |
| 8 | 해외 |  |  |  |  |  |  |  | 확인 필요 |

## 종합 분석

### 1. 국내 연구의 경향

-

### 2. 해외 연구의 경향

-

### 3. 기존 연구의 한계

-

### 4. 본 연구의 차별점

-
```

---

## 10. 연구방법 작성

`04_final_paper/04_methodology_experiment/methodology.md`를 작성하라.

```markdown
# 연구방법

## 1. 연구방법 개요

본 연구는 다음 방법 중 해당하는 방식을 사용한다.

- 문헌분석
- 사례분석
- 모의실험
- 체크리스트 설계
- 프레임워크 설계

## 2. 분석 대상

| 항목 | 내용 |
|---|---|
| 대상 시스템 |  |
| 보안 위협 |  |
| 분석 자료 |  |
| 실험 데이터 |  |
| 평가 지표 |  |

## 3. 연구 절차

1. 관련연구 수집
2. 선행연구 비교표 작성
3. 위협모형 정의
4. 평가방법 설계
5. 모의실험 또는 사례분석 수행
6. 보안적 함의 도출
7. 한계와 후속 연구 정리

## 4. 방법론의 한계

-
```

---

## 11. 위협모형 작성

`04_final_paper/04_methodology_experiment/threat_model.md`를 작성하라.

```markdown
# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 |  |
| 보호 자산 |  |
| 공격자 |  |
| 공격자의 지식 | White-box / Gray-box / Black-box |
| 공격자의 능력 |  |
| 공격 경로 |  |
| 공격 성공 조건 |  |
| 방어자 가정 |  |
| 제외 범위 |  |

## 위협모형 설명

-
```

---

## 12. 평가방법 작성

`04_final_paper/04_methodology_experiment/evaluation_protocol.md`를 작성하라.

```markdown
# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Utility |  |  |  |  |
| Attack Success Rate |  |  |  |  |
| Privacy Leakage |  |  |  |  |
| Robustness |  |  |  |  |
| Reproducibility |  |  |  |  |
| Cost |  |  |  |  |
| Auditability |  |  |  |  |

## 평가방법 설명

-
```

---

## 13. 논문 초안 작성

`04_final_paper/05_draft/paper_draft.md`를 작성하라.

```markdown
# 기말 모의투고 논문 초안

## 제목

국문 제목:

영문 제목:

---

## 국문초록

연구 배경, 문제, 방법, 결과, 기여를 500자 내외로 작성한다.

---

## 영문초록

Write an English abstract of 150–250 words.

---

## 키워드

국문 키워드:  
영문 키워드:

---

## 1. 서론

### 1.1 연구 배경

### 1.2 문제 제기

### 1.3 연구 목적

### 1.4 논문 구성

---

## 2. 관련연구

### 2.1 국내 연구

### 2.2 해외 연구

### 2.3 선행연구 비교

> 표 1. 관련연구 비교표 삽입

### 2.4 기존 연구의 한계

### 2.5 본 연구의 차별점

---

## 3. 연구문제 또는 연구가설

### 3.1 연구문제

### 3.2 연구범위

---

## 4. 연구방법

### 4.1 연구대상

### 4.2 위협모형

### 4.3 분석 방법

### 4.4 평가방법

> 그림 1. 제안 프레임워크 또는 실험 구조도 삽입

---

## 5. 분석 또는 실험

### 5.1 분석 설계

### 5.2 실험 또는 사례분석 결과

### 5.3 결과 해석

---

## 6. 보안적 함의

### 6.1 기밀성

### 6.2 무결성

### 6.3 가용성

### 6.4 프라이버시

### 6.5 안전성

### 6.6 책임성

---

## 7. 결론

### 7.1 연구 요약

### 7.2 연구 기여

### 7.3 연구 한계

### 7.4 후속 연구

---

## 참고문헌

확인된 참고문헌만 작성한다.  
임의 DOI, 허위 논문, 존재하지 않는 저자명은 작성하지 않는다.

---

## AI 활용 고지

AI 도구 사용 내역은 `04_final_paper/06_appendices/ai_disclosure.md`에 별도 작성한다.
```

---

## 14. AI 활용 고지서 작성

`04_final_paper/06_appendices/ai_disclosure.md`를 작성하라.

```markdown
# AI 활용 고지서

| 항목 | 작성 내용 |
|---|---|
| 사용한 AI 도구명 |  |
| 사용 일자 |  |
| 사용 목적 | 번역 / 수식 설명 / 개념 설명 / 문장 교정 / 제목 후보 / 코드 점검 / 기타 |
| 주요 프롬프트 |  |
| AI 산출물 반영 위치 |  |
| 본인 수정 내용 |  |
| 사실관계 검증 방법 |  |
| 참고문헌 검증 방법 |  |
| 최종 책임 확인 | 본인은 최종 원고의 내용, 인용, 실험결과, 연구윤리 책임이 본인에게 있음을 확인합니다. |
```

---

## 15. 참고문헌 검증표 작성

`04_final_paper/06_appendices/reference_verification.md`를 작성하라.

```markdown
# 참고문헌 검증표

| 번호 | 구분 | 문헌명 | 검증 경로 | DOI/URL | 본문 인용 위치 | 확인 |
|---:|---|---|---|---|---|---|
| 1 | 국내 |  | KCI / DBpia / RISS / Google Scholar / 출판사 홈페이지 |  |  | □ |
| 2 | 국내 |  | KCI / DBpia / RISS / Google Scholar / 출판사 홈페이지 |  |  | □ |
| 3 | 국내 |  | KCI / DBpia / RISS / Google Scholar / 출판사 홈페이지 |  |  | □ |
| 4 | 해외 |  | IEEE / ACM / Springer / Elsevier / Google Scholar |  |  | □ |
| 5 | 해외 |  | IEEE / ACM / Springer / Elsevier / Google Scholar |  |  | □ |
| 6 | 해외 |  | IEEE / ACM / Springer / Elsevier / Google Scholar |  |  | □ |
| 7 | 해외 |  | IEEE / ACM / Springer / Elsevier / Google Scholar |  |  | □ |
| 8 | 해외 |  | IEEE / ACM / Springer / Elsevier / Google Scholar |  |  | □ |

## 검증 원칙

- 본문에서 인용한 문헌은 참고문헌 목록에 반드시 있어야 한다.
- 참고문헌 목록에 있는 문헌은 본문에서 최소 1회 이상 인용되어야 한다.
- 논문 제목, 저자명, 학술지명, 연도, 권호, 페이지, DOI 또는 URL을 확인해야 한다.
- 존재하지 않는 논문 또는 DOI는 작성하지 않는다.
```

---

## 16. 학회지 양식 출처표 작성

`04_final_paper/06_appendices/journal_format_source_table.md`를 작성하라.

```markdown
# 학회지 양식 출처표

| 항목 | 작성 내용 |
|---|---|
| 선택 학회명 |  |
| 선택 논문지명 |  |
| 논문 양식 다운로드 URL |  |
| 투고규정 URL |  |
| 연구윤리규정 URL |  |
| 확인일 |  |
| 선택 이유 |  |
```

---

## 17. 표절·연구윤리 자기점검

`04_final_paper/06_appendices/plagiarism_self_check.md`를 작성하라.

```markdown
# 표절 및 연구윤리 자기점검표

| 확인 | 점검 항목 |
|---|---|
| □ | 허위 논문을 인용하지 않았다. |
| □ | 허위 DOI를 작성하지 않았다. |
| □ | 본문 인용과 참고문헌 목록이 일치한다. |
| □ | 실험하지 않은 결과를 실험 결과처럼 작성하지 않았다. |
| □ | AI가 생성한 내용을 검증 없이 제출하지 않았다. |
| □ | AI 활용 고지서를 작성했다. |
| □ | 표와 그림의 출처를 명확히 표시했다. |
| □ | PDF 변환 후 서식 깨짐을 확인했다. |
```

---

## 18. 최종 제출 체크리스트 작성

`04_final_paper/07_final_submission/submit_checklist.md`를 작성하라.

```markdown
# 기말논문 최종 제출 체크리스트

| 확인 | 점검 항목 |
|---|---|
| □ | 선택한 국내 학회지 양식을 사용했다. |
| □ | 투고규정과 참고문헌 형식을 확인했다. |
| □ | 국문 제목과 영문 제목을 작성했다. |
| □ | 국문초록과 영문초록을 작성했다. |
| □ | 키워드를 작성했다. |
| □ | 서론, 관련연구, 연구문제, 연구방법, 분석, 보안적 함의, 결론을 모두 포함했다. |
| □ | 표 1개 이상, 그림 1개 이상을 포함했다. |
| □ | 국내 논문 3편 이상, 해외 논문 5편 이상을 실제로 검증했다. |
| □ | 주차별 보고서 2개 이상을 논문에 반영했다. |
| □ | AI 활용 고지서를 작성했다. |
| □ | 참고문헌 검증표를 작성했다. |
| □ | 학회지 양식 출처표를 작성했다. |
| □ | PDF 변환 후 서식 깨짐을 확인했다. |
| □ | 파일명을 지정 형식에 맞추었다. |
```

---

## 19. 작성 규칙

1. 기존 파일은 삭제하지 않는다.
2. 기존 파일을 덮어쓰기 전 `.bak` 백업을 만든다.
3. Markdown 파일은 UTF-8로 저장한다.
4. 참고문헌은 임의 생성하지 않는다.
5. DOI, 저자명, 학술지명은 확인 필요로 둔다.
6. 주차별 보고서 최소 2개 이상을 반영한다.
7. AI 활용 고지서를 별도 파일로 둔다.
8. 실험하지 않은 결과를 결과처럼 작성하지 않는다.
9. 실행한 실험 결과는 `outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 대조 가능한 값만 반영한다.
10. 표 1개 이상, 그림 1개 이상 들어갈 위치를 표시한다.
11. 국문 제목과 영문 제목을 모두 작성한다.
12. 국문초록과 영문초록을 모두 작성한다.
13. 최종 DOCX/PDF 변환은 별도 단계로 남겨둔다.

---

## 20. 완료 후 출력 형식

작업 완료 후 다음 형식으로 보고하라.

```markdown
# 기말논문 작성 완료 보고

## 1. 작성한 파일

## 2. 보완한 파일

## 3. 반영한 주차별 보고서

## 4. 최종 논문 주제

## 5. 최종 연구문제

## 6. 최종 Contribution

## 7. 확인 필요 항목

## 8. 다음 작업 우선순위
```
