# Generative AI Security Research Project

## 연구 제목

기업용 생성형 AI 챗봇의 RAG 문서 오염 위험 탐지를 위한 재현성 중심 보안 감사 프레임워크 연구

## 대상 학회지

- 한국산학기술학회논문지
- Journal of the Korea Academia-Industrial cooperation Society
- KCI 등재 국내 학술지 투고형 모의논문

## 연구 목적

기업용 RAG 기반 생성형 AI 챗봇에서 발생할 수 있는 문서 오염, 간접 프롬프트 인젝션, 민감정보 노출 위험을 사전에 탐지하기 위한 보안 감사 프레임워크를 제안하고, synthetic 데이터셋과 baseline 비교 실험을 통해 재현 가능한 평가 절차를 제시한다.

## 핵심 산출물

| 산출물 | 경로 |
|---|---|
| 논문 초안 | [04_final_paper/05_draft/JKAIS_paper_draft.md](/home/ubuntu/generative-ai-security/04_final_paper/05_draft/JKAIS_paper_draft.md) |
| 논문 DOCX 초안 | [04_final_paper/05_draft/JKAIS_paper_draft.docx](/home/ubuntu/generative-ai-security/04_final_paper/05_draft/JKAIS_paper_draft.docx) |
| 논문 PDF 초안 | [04_final_paper/05_draft/JKAIS_paper_draft.pdf](/home/ubuntu/generative-ai-security/04_final_paper/05_draft/JKAIS_paper_draft.pdf) |
| 논문 메타데이터 | [04_final_paper/01_planning/paper_metadata.yaml](/home/ubuntu/generative-ai-security/04_final_paper/01_planning/paper_metadata.yaml) |
| 제목 후보 | [04_final_paper/01_planning/title_candidates.md](/home/ubuntu/generative-ai-security/04_final_paper/01_planning/title_candidates.md) |
| 학회 양식 출처표 | [04_final_paper/00_journal_format/journal_format_source.md](/home/ubuntu/generative-ai-security/04_final_paper/00_journal_format/journal_format_source.md) |
| 공식 학회 양식 | [04_final_paper/00_journal_format/journal_template/](/home/ubuntu/generative-ai-security/04_final_paper/00_journal_format/journal_template) |
| AI 활용 고지서 | [04_final_paper/06_appendices/ai_disclosure.md](/home/ubuntu/generative-ai-security/04_final_paper/06_appendices/ai_disclosure.md) |
| 참고문헌 검증표 | [04_final_paper/06_appendices/reference_verification.md](/home/ubuntu/generative-ai-security/04_final_paper/06_appendices/reference_verification.md) |
| 주차별 보고서 반영표 | [04_final_paper/02_weekly_reflection/weekly_report_mapping.md](/home/ubuntu/generative-ai-security/04_final_paper/02_weekly_reflection/weekly_report_mapping.md) |
| 데이터셋 | [04_final_paper/04_methodology_experiment/data/rag_security_dataset_100.csv](/home/ubuntu/generative-ai-security/04_final_paper/04_methodology_experiment/data/rag_security_dataset_100.csv) |
| 실험 코드 | [04_final_paper/04_methodology_experiment/scripts/](/home/ubuntu/generative-ai-security/04_final_paper/04_methodology_experiment/scripts) |
| 실험 결과 | [04_final_paper/04_methodology_experiment/outputs/](/home/ubuntu/generative-ai-security/04_final_paper/04_methodology_experiment/outputs) |
| 제출 전 체크리스트 | [04_final_paper/07_final_submission/submission_checklist.md](/home/ubuntu/generative-ai-security/04_final_paper/07_final_submission/submission_checklist.md) |
| 최종 제출 복사본 | [06_submission/2026-06-13_JKAIS_mock_submission/](/home/ubuntu/generative-ai-security/06_submission/2026-06-13_JKAIS_mock_submission) |

## 폴더 구조 원칙

이 저장소는 번호형 루트 구조를 표준으로 사용한다.

- 기말논문 작업 원본은 `04_final_paper/`에 둔다.
- 실제 제출 복사본은 `06_submission/2026-06-13_JKAIS_mock_submission/`에 둔다.
- 루트에는 `paper/`, `data/`, `experiments/`, `outputs/`, `references/`, `submission/`, `ethics/`, `reports/` 같은 비번호형 작업 폴더를 만들지 않는다.

## 현재 실험 결과

| method | Precision | Recall | F1-score | FPR | Dangerous Prevention | Leakage Rate | Human Review |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline_no_filter | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1.000000 | 0.000000 |
| baseline_keyword | 1.000000 | 0.500000 | 0.666667 | 0.000000 | 0.500000 | 0.000000 | 0.000000 |
| baseline_regex | 1.000000 | 0.250000 | 0.400000 | 0.000000 | 0.250000 | 0.000000 | 0.000000 |
| rag_docguard | 1.000000 | 1.000000 | 1.000000 | 0.000000 | 0.500000 | 0.000000 | 0.400000 |

이 수치는 synthetic 데이터셋과 규칙 기반 판정기의 재현성 검증 결과이며, 실제 기업 RAG 시스템이나 실제 LLM 보안 성능으로 일반화하지 않는다.

## 실행 방법

```bash
python3 04_final_paper/04_methodology_experiment/scripts/run_baseline_no_filter.py
python3 04_final_paper/04_methodology_experiment/scripts/run_baseline_keyword.py
python3 04_final_paper/04_methodology_experiment/scripts/run_baseline_regex.py
python3 04_final_paper/04_methodology_experiment/scripts/run_proposed_framework.py
python3 04_final_paper/04_methodology_experiment/scripts/evaluate_metrics.py
```

Markdown 원고에서 DOCX/PDF 초안을 다시 생성하려면 다음을 실행한다.

```bash
04_final_paper/05_draft/build_docx.sh
```

이 변환은 프로젝트 `.venv`에 설치한 `python-docx`와 `reportlab`를 사용한다. 생성 파일은 [04_final_paper/05_draft/JKAIS_paper_draft.docx](/home/ubuntu/generative-ai-security/04_final_paper/05_draft/JKAIS_paper_draft.docx)와 [04_final_paper/05_draft/JKAIS_paper_draft.pdf](/home/ubuntu/generative-ai-security/04_final_paper/05_draft/JKAIS_paper_draft.pdf)이다.

JKAIS 공식 HWP 양식은 [04_final_paper/00_journal_format/journal_template/](/home/ubuntu/generative-ai-security/04_final_paper/00_journal_format/journal_template)에 다운로드되어 있다. 최종 제출본은 공식 HWP 양식에 맞춰 수동 편집하고 PDF 변환 후 서식 깨짐을 확인해야 한다.

## 연구윤리 원칙

- 허위 참고문헌 금지
- 허위 DOI 금지
- 실험결과 조작 금지
- 실제 개인정보 사용 금지
- 실제 API 키 또는 실제 토큰 사용 금지
- AI 활용 내역 공개
- 참고문헌 검증표 작성
- PDF 변환 후 서식 확인

## 기존 자료

이 저장소의 기존 주차별 보고서와 강의자료는 보존한다. 기말논문은 특히 다음 주차 자료를 반영한다.

- Week 7: LLM 보안·프라이버시
- Week 8: RAG·프롬프트 인젝션
- Week 14: MLOps·공급망·운영 로그
- Week 15: 연구평가·재현성·논문 구성
