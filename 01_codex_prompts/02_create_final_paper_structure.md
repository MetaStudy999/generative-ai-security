# 02_create_final_paper_structure.md
# 02_기말논문_통합구조.md

## Codex 작업 지시서: 기말 모의투고 논문 통합 구조 생성

## 1. 작업 목표

`04_final_paper/` 폴더를 국내 학회지 모의투고 논문 작성에 맞게 구성하라.

기말 논문은 주차별 보고서를 단순히 모으는 것이 아니라, 하나의 작은 AI 보안 연구문제를 정의하고 학회지 논문 형식으로 재구성하는 것이 목표다.

파일명과 폴더명은 영문, 숫자, 언더바를 우선 사용한다. Markdown 본문은 한글로 작성한다.

---

## 2. 생성할 폴더

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

---

## 3. 생성할 파일

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

## 4. `04_final_paper/00_journal_format/journal_format_source.md`

```markdown
# 학회지 양식 출처

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

## 5. `04_final_paper/01_planning/final_topic.md`

```markdown
# 최종 논문 주제

## 1. 최종 제목 후보

| 번호 | 제목 후보 | 대상 시스템 | 보안 위협 | 방법론 | 예상 기여 |
|---:|---|---|---|---|---|
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |

## 2. 선택한 최종 주제

-

## 3. 선택 이유

-
```

---

## 6. `04_final_paper/01_planning/research_question.md`

```markdown
# 연구문제

## 1. 연구 배경

-

## 2. 연구문제

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
```

---

## 7. `04_final_paper/01_planning/contribution.md`

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

-
```

---

## 8. `04_final_paper/01_planning/paper_outline.md`

```markdown
# 논문 목차

## 제목

-

## 국문초록

-

## 영문초록

-

## 키워드

-

## 1. 서론

## 2. 관련연구

## 3. 연구문제 또는 연구가설

## 4. 연구방법

## 5. 분석 또는 실험

## 6. 보안적 함의

## 7. 결론

## 참고문헌

## AI 활용 고지
```

---

## 9. `04_final_paper/02_weekly_reflection/weekly_reflection_table.md`

```markdown
# 주차별 보고서 반영표

| 번호 | 기존 보고서 제목 | 기말 논문에 반영한 위치 | 반영 내용 |
|---:|---|---|---|
| 1 |  | 예: 2장 관련연구 |  |
| 2 |  | 예: 4장 연구방법 |  |
| 3 |  | 선택 |  |
```

---

## 10. `04_final_paper/03_related_work/literature_matrix.md`

```markdown
# 관련연구 비교표

| 번호 | 구분 | 논문 제목 | 저자 | 연도 | 연구문제 | 방법론 | 한계 | 본 연구와의 차별점 |
|---:|---|---|---|---:|---|---|---|---|
| 1 | 국내 |  |  |  |  |  |  |  |
| 2 | 국내 |  |  |  |  |  |  |  |
| 3 | 국내 |  |  |  |  |  |  |  |
| 4 | 해외 |  |  |  |  |  |  |  |
| 5 | 해외 |  |  |  |  |  |  |  |
| 6 | 해외 |  |  |  |  |  |  |  |
| 7 | 해외 |  |  |  |  |  |  |  |
| 8 | 해외 |  |  |  |  |  |  |  |
```

---

## 11. `04_final_paper/04_methodology_experiment/threat_model.md`

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
```

---

## 12. `04_final_paper/04_methodology_experiment/evaluation_protocol.md`

```markdown
# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Clean Accuracy |  |  |  |  |
| Attack Success Rate |  |  |  |  |
| Robust Accuracy |  |  |  |  |
| Privacy Leakage |  |  |  |  |
| Utility |  |  |  |  |
| Cost |  |  |  |  |
| Reproducibility |  |  |  |  |
```

---

## 13. `04_final_paper/05_draft/paper_draft.md`

```markdown
# 기말 모의투고 논문 초안

## 제목

## 국문초록

## 영문초록

## 키워드

## 1. 서론

### 1.1 연구 배경

### 1.2 문제 제기

### 1.3 연구 목적

### 1.4 논문 구성

## 2. 관련연구

### 2.1 국내 연구

### 2.2 해외 연구

### 2.3 선행연구의 한계

### 2.4 본 연구의 차별점

## 3. 연구문제 또는 연구가설

## 4. 연구방법

### 4.1 연구대상

### 4.2 위협모형

### 4.3 분석 방법

### 4.4 평가방법

## 5. 분석 또는 실험

### 5.1 분석 결과

### 5.2 표 삽입 위치

> 표 1. 관련연구 비교표

### 5.3 그림 삽입 위치

> 그림 1. 제안 프레임워크 또는 실험 구조도

## 6. 보안적 함의

### 6.1 기밀성

### 6.2 무결성

### 6.3 가용성

### 6.4 프라이버시

### 6.5 안전성

### 6.6 책임성

## 7. 결론

### 7.1 연구 요약

### 7.2 연구 기여

### 7.3 한계

### 7.4 후속 연구

## 참고문헌

## AI 활용 고지
```

---

## 14. `04_final_paper/06_appendices/ai_disclosure.md`

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

## 15. `04_final_paper/06_appendices/reference_verification.md`

```markdown
# 참고문헌 검증표

| 번호 | 구분 | 문헌명 | 검증 경로 | DOI/URL | 확인 |
|---:|---|---|---|---|---|
| 1 | 국내 |  | KCI / DBpia / RISS / Google Scholar / 출판사 홈페이지 |  | □ |
| 2 | 국내 |  | KCI / DBpia / RISS / Google Scholar / 출판사 홈페이지 |  | □ |
| 3 | 국내 |  | KCI / DBpia / RISS / Google Scholar / 출판사 홈페이지 |  | □ |
| 4 | 해외 |  | IEEE / ACM / Springer / Elsevier / Google Scholar |  | □ |
| 5 | 해외 |  | IEEE / ACM / Springer / Elsevier / Google Scholar |  | □ |
| 6 | 해외 |  | IEEE / ACM / Springer / Elsevier / Google Scholar |  | □ |
| 7 | 해외 |  | IEEE / ACM / Springer / Elsevier / Google Scholar |  | □ |
| 8 | 해외 |  | IEEE / ACM / Springer / Elsevier / Google Scholar |  | □ |
```

---

## 16. `04_final_paper/07_final_submission/submit_checklist.md`

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
| □ | PDF 변환 후 서식 깨짐을 확인했다. |
| □ | 파일명을 지정 형식에 맞추었다. |
```

---

## 17. 작업 규칙

1. 기존 파일은 삭제하지 않는다.
2. 기존 파일을 덮어쓰기 전 `.bak` 백업을 만든다.
3. Markdown 파일은 UTF-8로 저장한다.
4. 참고문헌은 임의 생성하지 않는다.
5. DOI, 저자명, 학술지명은 확인 필요로 둔다.
6. 주차별 보고서 최소 2개 이상을 반영할 수 있도록 구조를 만든다.
7. AI 활용 고지서를 별도 파일로 둔다.
8. 실험하지 않은 결과를 결과처럼 작성하지 않는다.
9. 실행한 실험 결과는 `outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 대조 가능한 값만 반영한다.

---

## 18. 완료 후 출력 형식

```markdown
# 기말논문 통합 구조 생성 완료 보고

## 1. 생성된 폴더

## 2. 생성된 파일

## 3. 백업한 파일

## 4. 확인 필요 항목

## 5. 다음 작업 우선순위
```
