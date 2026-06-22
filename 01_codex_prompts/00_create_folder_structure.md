# 00_create_folder_structure.md
# 00_전체폴더_생성.md

## Codex 작업 지시서: AI보안 주차별보고서 전체 폴더 구조 초기 생성

## 1. 작업 목표

현재 프로젝트의 최상위 폴더명은 다음과 같다.

```text
AISEC_WEEKLY_REPORTS
```

이 프로젝트는 AI 보안 대학원 세미나의 다음 산출물을 체계적으로 관리하기 위한 저장소다.

1. 수업자료 정리
2. Codex 지시문 관리
3. 보고서 템플릿 관리
4. Week 01~15 주차별 통합보고서 작성
5. 논문 PDF 및 참고문헌 관리
6. Docker 기반 실습 기록
7. AI 활용기록 관리
8. 기말 모의투고 논문 작성
9. 최종 제출본 관리
10. 백업 관리

전체 작업 흐름은 다음과 같다.

```text
수업자료 확인
→ Codex 지시문 작성
→ 보고서 템플릿 관리
→ 주차별 보고서 작성
→ 기말논문 조립
→ 참고문헌 검증
→ 최종 제출
→ 백업
```

---

## 2. 생성 규칙

다음 규칙을 반드시 지켜라.

1. 기존 폴더와 파일은 삭제하지 않는다.
2. 기존 파일을 덮어쓰기 전에 `.bak` 확장자로 백업한다.
3. Markdown 파일은 UTF-8로 저장한다.
4. 폴더명과 파일명은 영문, 숫자, 언더바를 우선 사용한다.
5. Markdown 본문은 한글로 작성해도 된다.
6. 논문 제목, DOI, 저자명, 학술지명은 임의로 생성하지 않는다.
7. 모르는 정보는 `확인 필요`로 둔다.
8. 실습 코드는 아직 완성하지 않아도 된다.
9. 우선 폴더와 템플릿 파일 구조를 정확히 만든다.
10. Week 폴더명은 숫자만 쓰지 말고 주차 제목을 포함한다.
11. 생성 완료 후 전체 폴더 트리를 출력한다.
12. 다음 작업 우선순위 5개를 제안한다.

---

## 3. 최상위 대분류 폴더 생성

아래 대분류 폴더를 생성하라.

```text
AISEC_WEEKLY_REPORTS/
├── 00_class_materials
├── 01_codex_prompts
├── 02_report_templates
├── 03_weekly_reports
├── 04_final_paper
├── 05_references
├── 06_submission
└── 99_backup
```

각 대분류 폴더의 역할은 다음과 같다.

| 폴더                    | 역할                                   |
| --------------------- | ------------------------------------ |
| `00_class_materials`  | 강의계획서, 기말과제 안내문, 수업 운영 기준, 주차별 논문 목록 |
| `01_codex_prompts`    | Codex에 복사해 넣을 지시문 MD 파일              |
| `02_report_templates` | 주차별 보고서, 논문요약, 실습보고서, AI활용기록 템플릿     |
| `03_weekly_reports`   | Week 01~15 주차별 실제 작업 폴더              |
| `04_final_paper`      | 주차별 보고서를 모아 국내 학회지 모의투고 논문 작성        |
| `05_references`       | 전체 참고문헌, DOI 검증, BibTeX, 국내·해외 논문 목록 |
| `06_submission`       | 실제 제출할 DOCX, PDF, 부속서류, 압축파일         |
| `99_backup`           | 이전 버전, 실패한 산출물, 임시파일, 백업자료           |

---

## 4. `00_class_materials` 생성

다음 구조를 생성하라.

```text
00_class_materials/
├── README.md
├── syllabus_summary.md
├── final_assignment_summary.md
├── grading_policy.md
└── weekly_paper_list.md
```

### 4.1 `00_class_materials/README.md`

다음 내용을 넣어라.

```markdown
# 00_class_materials

이 폴더는 AI 보안 세미나의 기준 문서를 보관하는 공간이다.

## 보관 대상

- 강의계획서
- 기말고사 보고서 과제 안내문
- 수업 운영 및 평가 기준
- 주차별 논문 패킷 목록
- 제출 기준 및 점검표

## 사용 원칙

주차별 보고서와 기말논문을 작성할 때 이 폴더의 기준 문서를 먼저 확인한다.
```

### 4.2 `00_class_materials/syllabus_summary.md`

```markdown
# 강의계획서 요약

## 1. 수업 개요

확인 필요

## 2. 수업 운영 방식

확인 필요

## 3. Research Track

- 연구문제:
- 위협모형:
- 평가방법:
- 재현성:
- 한계/오픈문제:

## 4. AI Tool Track

- 사용 도구:
- 사용 목적:
- Worklog:
- 검증 방식:

## 5. 주차별 구성

확인 필요
```

### 4.3 `00_class_materials/final_assignment_summary.md`

```markdown
# 기말과제 요약

## 1. 과제명

AI 보안 국내 학술지 모의투고 논문 작성

## 2. 핵심 목표

한 학기 동안 읽고 분석한 논문과 주차별 보고서를 바탕으로 작은 AI 보안 연구문제를 정의하고, 국내 학회지 형식에 맞춘 모의투고 논문 원고를 작성한다.

## 3. 주요 제출물

- 최종 논문 원고
- PDF 변환본
- 학회지 양식 출처표
- AI 활용 고지서
- 참고문헌 검증표
- 주차별 보고서 반영표

## 4. 작성 기준

확인 필요
```

### 4.4 `00_class_materials/grading_policy.md`

```markdown
# 수업운영 및 평가 기준

## 1. 수업 운영

확인 필요

## 2. 발표 기준

확인 필요

## 3. 보고서 기준

확인 필요

## 4. 감점 기준

확인 필요

## 5. 제출 전 점검

확인 필요
```

### 4.5 `00_class_materials/weekly_paper_list.md`

```markdown
# 주차별 논문 목록

| 주차 | 주제 | 논문 수 | 비고 |
|---|---|---:|---|
| W01 | 딥러닝 패러다임 & ML 보안 분류학 | 5 | 확인 필요 |
| W02 | 대규모 최적화 & 데이터 오염 위협 | 5 | 확인 필요 |
| W03 | 컴퓨터비전 표현학습 & 비전 대적공격 | 5 | 확인 필요 |
| W04 | Transformer 변형 & NLP 대적공격·프라이버시 | 5 | 확인 필요 |
| W05 | 자기지도학습·파운데이션 모델 & Poisoning/Backdoor | 5 | 확인 필요 |
| W06 | 확률생성모형(Diffusion/GAN) & 딥페이크 검출 | 5 | 확인 필요 |
| W07 | LLM 학습·정렬·평가 & LLM 보안·프라이버시 | 5 | 확인 필요 |
| W08 | RAG·프롬프팅 프레임워크 & 프롬프트 인젝션 | 5 | 확인 필요 |
| W09 | 심층강화학습(DRL) & 사이버보안 적용·보상조작 | 5 | 확인 필요 |
| W10 | 연합학습(FL) & FL 위협·방어·정책 | 5 | 확인 필요 |
| W11 | 차등프라이버시(DP) & 멤버십 추론 공격·방어 | 5 | 확인 필요 |
| W12 | 신경망 검증·정형방법 & 대적방어·XAI·강건성 트레이드오프 | 5 | 확인 필요 |
| W13 | 모델 지식재산(IP)·모델 도난·모델 추출 위협 | 5 | 확인 필요 |
| W14 | MLOps/DevOps·데이터/모델 파이프라인·공급망 보안 | 5 | 확인 필요 |
| W15 | 연구평가·재현성·설명가능성(XAI)·논문 구성 | 5 | 확인 필요 |
```

---

## 5. `01_codex_prompts` 생성

다음 구조를 생성하라.

```text
01_codex_prompts/
├── 00_create_folder_structure.md
├── 01_create_common_templates.md
├── 02_create_final_paper_structure.md
├── W01_deep_learning_ml_security.md
├── W02_optimization_data_poisoning.md
├── W03_computer_vision_adversarial.md
├── W04_transformer_nlp_security.md
├── W05_ssl_backdoor.md
├── W06_diffusion_gan_deepfake.md
├── W07_llm_security_privacy.md
├── W08_rag_prompt_injection.md
├── W09_drl_cybersecurity.md
├── W10_federated_learning_security.md
├── W11_differential_privacy_mi.md
├── W12_nn_verification_xai.md
├── W13_model_stealing_watermarking.md
├── W14_mlops_supply_chain.md
├── W15_reproducibility_xai_paper.md
└── 99_write_final_paper.md
```

각 파일에는 아래 기본 문구를 넣어라.

```markdown
# Codex 지시문

## 목적

이 파일은 Codex에게 복사해 넣기 위한 작업 지시문이다.

## 작업 대상

확인 필요

## 생성할 산출물

확인 필요

## 주의사항

- 기존 파일은 삭제하지 않는다.
- 참고문헌은 임의 생성하지 않는다.
- DOI와 저자명은 확인 필요로 둔다.
- AI 활용 내역은 반드시 기록한다.
```

단, 현재 실행 중인 `00_create_folder_structure.md` 파일은 덮어쓰지 말라.

---

## 6. `02_report_templates` 생성

다음 구조를 생성하라.

```text
02_report_templates/
├── README.md
├── weekly_integrated_report_template.md
├── paper_summary_template.md
├── paper_matrix_template.md
├── theory_note_template.md
├── experiment_report_template.md
├── presentation_report_template.md
├── presentation_slides_template.md
├── speaker_notes_template.md
├── qna_template.md
├── one_page_handout_template.md
├── submission_report_template.md
├── ai_worklog_template.md
├── final_paper_bridge_template.md
└── submission_checklist_template.md
```

---

## 7. `03_weekly_reports` 생성

Week 폴더는 숫자만 쓰지 말고 주제명을 포함하여 생성하라.

```text
03_weekly_reports/
├── README.md
├── w01_deep_learning_ml_security
├── w02_optimization_data_poisoning
├── w03_computer_vision_adversarial
├── w04_transformer_nlp_security
├── w05_ssl_backdoor
├── w06_diffusion_gan_deepfake
├── w07_llm_security_privacy
├── w08_rag_prompt_injection
├── w09_drl_cybersecurity
├── w10_federated_learning_security
├── w11_differential_privacy_mi
├── w12_nn_verification_xai
├── w13_model_stealing_watermarking
├── w14_mlops_supply_chain
└── w15_reproducibility_xai_paper
```

### 7.1 `03_weekly_reports/README.md`

```markdown
# 주차별 통합보고서 폴더 안내

이 폴더는 AI 보안 세미나의 Week 01부터 Week 15까지 주차별 보고서, 논문요약, 이론정리, 실습, AI 활용기록, 기말논문 연결자료를 관리하는 공간이다.

| 주차 | 폴더명 | 주제 |
|---|---|---|
| W01 | w01_deep_learning_ml_security | 딥러닝 패러다임 & ML 보안 분류학 |
| W02 | w02_optimization_data_poisoning | 대규모 최적화 & 데이터 오염 위협 |
| W03 | w03_computer_vision_adversarial | 컴퓨터비전 표현학습 & 비전 대적공격 |
| W04 | w04_transformer_nlp_security | Transformer 변형 & NLP 대적공격·프라이버시 |
| W05 | w05_ssl_backdoor | 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| W06 | w06_diffusion_gan_deepfake | 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| W07 | w07_llm_security_privacy | LLM 학습·정렬·평가 & LLM 보안·프라이버시 |
| W08 | w08_rag_prompt_injection | RAG·프롬프팅 프레임워크 & 프롬프트 인젝션 |
| W09 | w09_drl_cybersecurity | 심층강화학습(DRL) & 사이버보안 적용·보상조작 |
| W10 | w10_federated_learning_security | 연합학습(FL) & FL 위협·방어·정책 |
| W11 | w11_differential_privacy_mi | 차등프라이버시(DP) & 멤버십 추론 공격·방어 |
| W12 | w12_nn_verification_xai | 신경망 검증·정형방법 & 대적방어·XAI·강건성 트레이드오프 |
| W13 | w13_model_stealing_watermarking | 모델 지식재산(IP)·모델 도난·모델 추출 위협 |
| W14 | w14_mlops_supply_chain | MLOps/DevOps·데이터/모델 파이프라인·공급망 보안 |
| W15 | w15_reproducibility_xai_paper | 연구평가·재현성·설명가능성(XAI)·논문 구성 |
```

---

## 8. 각 주차 폴더 내부 구조 생성

각 주차 폴더 안에는 동일하게 다음 구조를 생성하라.

```text
00_management/
├── README.md
├── week_info.md
├── todo_checklist.md
├── grading_rubric.md
└── progress_log.md

01_papers/
├── pdf/
├── bibtex/
├── paper_list.md
├── doi_check.md
└── download_source.md

02_paper_summaries/
├── P01_summary.md
├── P02_summary.md
├── P03_summary.md
├── P04_summary.md
├── P05_summary.md
└── paper_matrix.md

03_theory_notes/
├── ai_principle_70.md
├── security_issue_30.md
├── key_terms.md
├── threat_model.md
├── evaluation_protocol.md
└── open_problems.md

04_experiment/
├── README.md
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── configs/
│   └── config.yaml
├── src/
├── outputs/
│   ├── metrics_summary.csv
│   ├── results.json
│   └── run_log.md
└── experiment_report.md

05_ai_worklog/
├── ai_worklog.md
├── prompts.md
├── ai_outputs.md
├── human_review.md
└── ai_disclosure_draft.md

06_report/
├── draft/
├── final/
└── review/

07_week_submission/
├── README.md
├── submit_checklist.md
├── wXX_submission_report.md
└── wXX_submission_report.html

08_final_paper_bridge/
├── final_paper_bridge.md
├── topic_candidates.md
├── contribution_candidates.md
└── weekly_reflection_table.md

09_presentation/
├── presentation_report.md
├── presentation_report.html
├── presentation_slides.md
├── presentation_slides.html
├── speaker_notes.md
├── qna.md
└── one_page_handout.md
```

`04_experiment/Dockerfile`은 `python:3.11-slim` 기반으로 작성하고, WSL 호스트에 uv를 설치하지 않는다. uv는 `COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/`로 이미지 내부에 포함하며, 주차별 Python 패키지는 컨테이너 내부에서 `uv sync`로 설치한다.

---

## 9. `04_final_paper` 생성

다음 구조를 생성하라.

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

각 폴더 안에 다음 파일을 생성하라.

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

`04_final_paper/05_draft/paper_draft.md`에는 다음 구조를 넣어라.

```markdown
# 기말 모의투고 논문 초안

## 제목

## 국문초록

## 영문초록

## 키워드

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

## 10. `05_references` 생성

다음 구조를 생성하라.

```text
05_references/
├── 00_master_paper_list.md
├── 01_domestic_papers
├── 02_international_papers
├── 03_bibtex
├── 04_doi_url_verification
└── 05_reference_verification_table
```

`05_references/00_master_paper_list.md`에는 다음 내용을 넣어라.

```markdown
# 전체 논문 목록

| 번호 | 구분 | 주차 | 논문 제목 | 저자 | 연도 | 학술지/학회 | DOI/URL | 검증 상태 |
|---:|---|---|---|---|---:|---|---|---|
| 1 | 해외 | W01 |  |  |  |  |  | 확인 필요 |
```

각 하위 폴더에는 `README.md`를 생성하고 용도를 2~3줄로 설명하라.

---

## 11. `06_submission` 생성

다음 구조를 생성하라.

```text
06_submission/
├── final_paper_docx
├── final_paper_pdf
├── ai_disclosure
├── reference_verification
├── journal_format_source
├── weekly_reflection_table
└── final_zip
```

각 하위 폴더에는 `README.md`를 생성하라.

---

## 12. `99_backup` 생성

다음 구조를 생성하라.

```text
99_backup/
├── old_versions
├── failed_outputs
├── temp
└── archive
```

각 하위 폴더에는 `README.md`를 생성하라.

---

## 13. 완료 후 출력 형식

작업 완료 후 다음 형식으로 보고하라.

```markdown
# 생성 완료 보고

## 1. 생성된 주요 폴더

## 2. 생성된 주요 파일

## 3. 기존 파일 백업 여부

## 4. 누락 또는 확인 필요 항목

## 5. 다음 작업 우선순위 5개
```
