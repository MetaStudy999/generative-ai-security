# 실험 보고서

## 1. 실험 목표

W15 실습은 모델을 학습하거나 공격을 실행하는 실험이 아니라, 기말논문 제출 직전의 재현성·참고문헌·AI 활용 고지·발표/제출 산출물 준비 상태를 감사하는 안전한 로컬 점검이다.

## 2. 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 기준 |
| Container | Docker 지원, 로컬 감사 스크립트는 Python 표준 라이브러리만 사용 |
| Python | 3.11 |
| Seed | 42 |
| 데이터 | 로컬 repository metadata |
| 결과 상태 | 실행 완료 |

## 3. 실행 절차

```bash
cd 03_weekly_reports/w15_reproducibility_xai_paper/04_experiment
python3 src/run_experiment.py --config configs/config.yaml
```

Docker 환경에서 실행할 경우:

```bash
docker build -t w15-reproducibility-xai-paper .
docker run --rm -v /home/ubuntu/generative-ai-security:/workspace -w /workspace/03_weekly_reports/w15_reproducibility_xai_paper/04_experiment w15-reproducibility-xai-paper python src/run_experiment.py --config configs/config.yaml
```

## 4. 기말 논문 준비 점검 결과

| 점검 항목 | 상태 | 근거 파일 | 보완 필요 |
|---|---|---|---|
| 주차별 보고서 2개 이상 반영 | 완료 | `04_final_paper/02_weekly_reflection/weekly_reflection_table.md` | 없음 |
| 참고문헌 DOI/URL 검증 | 부분 완료 | `01_papers/doi_check.md` | P03 원문 PDF와 저자명 표기, P05 권호/issue 최종 확인 |
| AI 활용 고지서 작성 | 완료 | `05_ai_worklog/ai_disclosure_draft.md` | 최종 제출 전 사용자 확인 |
| 실험 재현성 기록 | 완료 | `configs/config.yaml`, `outputs/run_log.md` | 모델 성능 실험 아님을 명시 |
| Contribution 문장 확정 | 완료 | `08_final_paper_bridge/contribution_candidates.md`, `04_final_paper/01_planning/contribution.md` | 최종 원고 반영 |
| 표 1개 이상 준비 | 완료 | `02_paper_summaries/paper_matrix.md`, `04_final_paper/03_related_work/literature_matrix.md` | 논문 본문 삽입 |
| 그림 1개 이상 준비 | 완료 | `04_final_paper/05_draft/paper_draft.md` | Mermaid 프레임워크 그림 작성, 최종 변환 확인 필요 |

## 5. 실행 산출물

| 파일 | 내용 |
|---|---|
| `outputs/metrics_summary.csv` | 감사 항목별 지표, 상태, 근거 파일 |
| `outputs/results.json` | 실행 메타데이터와 원시 감사 결과 |
| `outputs/run_log.md` | 사람이 읽을 수 있는 실행 로그 |

## 5-1. 기준 수치 대조표

출처: `outputs/metrics_summary.csv`. 본 표는 W15 제출 준비 감사의 기준 원천을 그대로 옮긴 것이며, 실제 모델 성능이나 운영 환경 보안 성능을 의미하지 않는다.

| category | metric | value | status |
|---|---|---:|---|
| artifact | w15_required_files | 47/47 | complete |
| artifact | final_paper_link_files | 9/9 | complete |
| paper | local_pdf_count | 5 | complete |
| reference | doi_confirmed | 4 | complete |
| reference | doi_partial | 1 | partial |
| reference | doi_unverified | 0 | complete |
| reference | weighted_reference_verification_rate | 0.90 | partial |
| ai_disclosure | ai_disclosure_completeness | 11/11 | complete |
| reproducibility | config_present | 1 | complete |
| reproducibility | seed_recorded | 42 | complete |

## 6. 결과 해석

W15 감사는 개인정보를 사용하지 않았고 실제 공격을 수행하지 않았다. 결과는 산출물 존재 여부와 검증 상태만 나타내며, LLM 또는 XAI 모델의 성능을 주장하지 않는다. 참고문헌 검증은 P01, P02, P04, P05는 확인, P03은 대체 PDF로 인한 부분 확인 상태다.

## 7. 한계

이 실습은 제출 준비 상태를 점검하는 감사이며, benchmark contamination이나 XAI stability를 실제 모델 출력으로 측정하지 않았다. 최종 기말논문에는 확인된 DOI와 실행 로그가 있는 값만 반영해야 한다.

이 결과는 로컬 산출물 존재 여부, DOI/URL 검증 상태, AI 활용 고지 완성도, 제출/발표 패키지 준비 상태를 확인하는 감사 결과이며, LLM 또는 XAI 모델의 성능, 실제 benchmark contamination 측정, 실제 보안 공격 실험으로 일반화하지 않는다.
