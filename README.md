# AI 보안 연구 프로젝트

이 저장소는 AI 보안 세미나의 주차별 논문요약, 실험 설계, 통합보고서, 기말논문 자료를 관리한다.

## 연구 관리 Dashboard

| 구분 | 상태 | 근거 파일 |
|---|---|---|
| 최종 주제 | 확인 필요 | 04_final_paper/01_planning/final_topic.md |
| 연구질문 | 확인 필요 | 04_final_paper/01_planning/research_question.md |
| 논문 초안 | 확인 필요 | 04_final_paper/05_draft/paper_draft.md |
| 국내 문헌 3편 | 확인 필요 | 04_final_paper/06_appendices/reference_verification.md |
| 해외 문헌 5편 | 확인 필요 | 04_final_paper/06_appendices/reference_verification.md |
| 학회지 양식 출처 | 확인 필요 | 04_final_paper/00_journal_format/journal_format_source.md |
| AI 활용 고지 | 확인 필요 | 04_final_paper/06_appendices/ai_disclosure.md |
| 실험/분석 로그 | 확인 필요 | 04_final_paper/04_methodology_experiment/outputs/run_log.md |
| 최종 제출 패키지 | 확인 필요 | 06_submission/final_paper_submission/ |

## 연구 관리 원칙

이 저장소는 단순 보고서 보관소가 아니라, 연구질문-문헌-방법론-분석-결론-제출물까지 추적 가능한 연구 관리 저장소로 운영한다.

- 연구질문과 결론은 반드시 대응되어야 한다.
- 본문 인용과 참고문헌 목록은 반드시 상호 대응되어야 한다.
- 실행하지 않은 실험 결과는 작성하지 않는다.
- 확인하지 못한 DOI/URL은 `확인 필요`로 표시한다.
- AI 도구 사용 내역은 최종 제출 전 반드시 고지한다.

## 주요 폴더

- `00_class_materials/`: 강의자료와 과제 안내
- `01_codex_prompts/`: 주차별 작업 프롬프트
- `02_report_templates/`: 보고서와 검수 템플릿
- `03_weekly_reports/`: Week 01-15 주차별 논문, 실험, 보고서
- `04_final_paper/`: 기말논문 계획, 초안, 부록, 제출자료
- `05_references/`: 국내외 참고문헌과 검증표
- `06_submission/`: 제출 산출물 정리
- `99_backup/`: 이전 산출물과 실패 산출물 보관

## 공통 GPU 연구환경

루트에는 `uv + Docker + NVIDIA GPU + CUDA 13.2 + Python 3.11` 기반 공통 실행환경을 추가했다. GPU가 필요한 실험은 루트의 `Dockerfile`, `docker-compose.yml`, `pyproject.toml`, `uv.lock`, `scripts/verify_gpu.py`를 사용한다.

자세한 빌드, 실행, 검증 방법과 CUDA 13.2/PyTorch 주의사항은 `README_GPU.md`를 참고한다.

## 주차별 실험환경

각 주차의 `04_experiment/` 폴더에는 기존의 경량 Docker/uv 설정이 유지되어 있다. GPU가 필요 없는 실험은 주차별 환경을 그대로 사용하고, GPU 검증이나 CUDA가 필요한 실험은 루트 공통 GPU 환경을 사용한다.

## 주차별 실험 결과 원칙

주차별 실험은 공개 데이터 또는 synthetic/toy 환경에서만 수행한다. 실제 개인정보, 운영 서비스, 무단 API 질의, 악용 가능한 공격 절차는 제외한다.

정량값은 실제 실행 로그가 있을 때만 확정한다. 실행 전에는 `실행 전` 또는 `확인 필요`로 표시하고, 실행 후에는 각 주차 `04_experiment/outputs/`에 `metrics_summary.csv`, `results.json`, `run_log.md`를 저장한다. 그림이나 예시 입력이 필요한 주차는 같은 폴더에 이미지 또는 텍스트 예시를 추가한다.

실험을 실행한 주차는 `04_experiment/experiment_report.md`, `06_report/final/integrated_report_final.md`, `07_week_submission/submit_checklist.md`, `05_ai_worklog/ai_worklog.md`를 함께 갱신한다. 실행하지 않은 주차의 결과값은 임의로 채우지 않는다.

실험 재현성을 위해 실행 명령어, 실행일, seed, Python/package 버전, 주요 config 상태를 기록한다. `config.yaml`의 `design_only` 또는 `executed` 상태는 실제 `outputs/` 산출물 존재 여부와 일치해야 한다.

## 참고문헌 검증 원칙

논문 제목, 저자, 연도, 학술지명, 권호, 페이지, DOI/URL은 임의 생성하지 않는다. 확인하지 못한 항목은 `확인 필요`로 표시하고, 미검증 문헌은 핵심 근거로 사용하지 않는다.

본문에서 인용한 문헌은 참고문헌 목록에 있어야 하며, 참고문헌 목록의 문헌은 본문에서 최소 1회 이상 인용되어야 한다. 기말논문 제출 전에는 국내 문헌 3편 이상, 해외 문헌 5편 이상을 실제 검색과 원문 또는 공식 landing page로 검증한다.

## AI 활용 및 연구윤리 원칙

생성형 AI 도구를 사용한 경우 사용 도구, 사용 목적, 주요 프롬프트, 반영 위치, 사람 검토 및 사실관계 검증 방식을 기록한다. 주차별 작업은 `05_ai_worklog/`에 남기고, 기말논문은 `04_final_paper/06_appendices/ai_disclosure.md`에 최종 고지를 정리한다.

AI 산출물은 초안으로만 사용한다. 최종 원고의 내용, 인용, 해석, 실험 결과, 연구윤리 책임은 작성자에게 있으며, 허위 인용, 표절, 존재하지 않는 DOI, 실행하지 않은 실험 결과 작성은 금지한다.

## 발표용 보고서 원칙

발표가 필요한 주차는 `09_presentation/` 폴더에 발표용 보고서, 슬라이드, 발표 보조자료를 둔다. 기본 발표 패키지는 `presentation_report.md`, `presentation_report.html`, `presentation_slides.md`, `presentation_slides.html`, `speaker_notes.md`, `qna.md`, `one_page_handout.md`이다.

발표용 보고서는 새 결과를 주장하는 문서가 아니라, 주차별 통합보고서와 실험 산출물을 발표 흐름으로 압축한 문서다. 실험 수치는 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치해야 하며, 실행하지 않은 결과는 발표에서도 말하지 않는다.

`speaker_notes.md`는 슬라이드별 발화 흐름과 시간 배분, `qna.md`는 예상 질문과 근거 파일, `one_page_handout.md`는 청중 배포용 1페이지 요약을 담는다. 발표 보조자료도 통합보고서와 실험 로그의 수치·한계 표현을 그대로 따른다.

## 제출용 보고서 원칙

주차별 제출본은 `07_week_submission/`에 Markdown과 HTML을 함께 둔다. 기본 파일명은 `wXX_submission_report.md`와 `wXX_submission_report.html`이다.

제출용 보고서는 통합보고서, 발표용 보고서, 실험 산출물을 제출 형식으로 압축한 문서다. HTML은 Markdown 제출본과 같은 수치, DOI/URL 검증 상태, AI 활용 고지, 실험 한계를 유지해야 한다.

## 기말논문 연결 원칙

기말논문은 한 학기 주차별 보고서 중 최소 2개 이상을 반영하고, `04_final_paper/02_weekly_reflection/` 또는 관련 반영표에 연결 근거를 남긴다. 선택한 국내 학회지 양식, 국문/영문 제목과 초록, 키워드, 표 1개 이상, 그림 1개 이상, 참고문헌 검증표, AI 활용 고지서, 학회지 양식 출처표를 제출 패키지에 포함한다.

기말고사 보고서는 국내 학회지 양식 기반 모의투고 논문으로 작성한다. 주차별 보고서를 단순히 합치지 않고 하나의 작은 연구문제, 관련연구 비교, 위협모형, 연구방법, 분석 또는 모의실험, 보안적 함의, 결론으로 재구성한다. 세부 기준은 `00_class_materials/final_report_assignment_ai_security.md`와 `00_class_materials/final_assignment_summary.md`를 우선 확인한다.

## 수식 및 알고리즘 설명 원칙

각 분야별 논문에서 수식이나 알고리즘이 핵심 기여, 공격·방어 원리, 평가 지표, 프라이버시 보장, 최적화 절차를 이해하는 데 필요하면 본문에 설명을 포함한다. 모든 논문에 기계적으로 수식을 넣지는 않는다.

수식을 반영할 때는 원문 수식 또는 검증 가능한 표준 수식만 사용하고, 기호 정의, 직관적 의미, 보안 관점 해석, 평가 지표와의 연결, 한계와 가정을 함께 적는다. 원문 확인이 부족하면 `확인 필요`로 표시하고 임의로 수식을 만들지 않는다. AI 도구로 수식 설명을 받았으면 AI 활용 기록에 사용 목적, 반영 위치, 검증 방식을 남긴다.

수식 작성 기본 형식은 Markdown 안의 LaTeX math로 통일한다. HTML 렌더링은 KaTeX 또는 MathJax, 문서 변환은 Pandoc, PDF 품질이 중요한 경우 LaTeX/TeX Live를 사용한다. 수식 검산과 그림 작성에는 `sympy`, `numpy`, `scipy`, `matplotlib`, `pandas`, `jupyterlab`을 상황에 따라 사용한다. 상세 기준은 `00_class_materials/math_formula_toolchain.md`를 참고한다.

현재 루트 공통 환경에는 `numpy`, `pandas`, `matplotlib`이 이미 포함되어 있으므로 수식 작성을 위해 추가 라이브러리를 즉시 설치하지 않는다. 수식 검산이 실제로 필요할 때 `sympy`를 먼저 선택 추가하고, 통계·최적화가 필요할 때 `scipy`, 노트북 기반 검토가 필요할 때 `jupyterlab`을 추가한다. 의존성을 추가하면 `pyproject.toml`, `uv.lock`, 실행 로그 또는 AI 활용기록에 추가 사유를 남긴다.
