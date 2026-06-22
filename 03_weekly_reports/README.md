# 주차별 통합보고서 폴더 안내

이 폴더는 AI 보안 세미나의 Week 01부터 Week 15까지 주차별 보고서, 논문요약, 이론정리, 실습, AI 활용기록, 기말논문 연결자료를 관리하는 공간이다.

각 주차 `04_experiment/Dockerfile`은 `python:3.11-slim` 기반으로 작성한다. WSL 호스트에는 uv를 설치하지 않고, Dockerfile 내부에서 `COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/`로 uv를 포함한 뒤 컨테이너 내부 `uv sync`로 `pyproject.toml`의 주차별 Python 패키지를 설치한다.

GPU가 필요한 실험은 루트의 공통 GPU 환경을 사용한다. 루트 `Dockerfile`은 `nvidia/cuda:13.2.1-cudnn-devel-ubuntu24.04`, Python 3.11, uv, `/opt/venv`, PyTorch CUDA 13.2 wheel을 기준으로 하며, 실행과 검증 절차는 루트 `README_GPU.md`에 기록한다.

## 공통 실험 산출물 규칙

모든 주차의 실험 결과는 W02/W03와 같은 방식으로 관리한다.

| 상태 | 작성 원칙 | 필수 확인 |
|---|---|---|
| 설계만 완료 | `config.yaml`의 상태를 `design_only`로 두고 결과값은 `실행 전` 또는 `확인 필요`로 표시 | 실행하지 않은 수치가 없는지 확인 |
| 실행 완료 | `config.yaml`의 상태를 `executed`로 바꾸고 `outputs/`에 실행 산출물을 저장 | `run_log.md` 기준으로 보고서 수치 갱신 |

실행 완료 주차의 `04_experiment/outputs/`에는 최소한 다음 파일을 둔다.

- `metrics_summary.csv`: 조건별 주요 지표 표
- `results.json`: 설정, 메타데이터, 원시 결과 보존
- `run_log.md`: 사람이 읽을 수 있는 실행 로그와 결과표
- 필요 시 예시 이미지, confusion matrix, 입력/출력 샘플

실험 실행 후에는 같은 주차의 `04_experiment/experiment_report.md`, `03_theory_notes/evaluation_protocol.md`, `06_report/final/integrated_report_final.md`, `07_week_submission/submit_checklist.md`, `05_ai_worklog/ai_worklog.md`를 함께 갱신한다. 실행하지 않은 결과를 결과처럼 작성하지 않는다.

## 발표용 보고서 규칙

발표가 필요한 주차는 `09_presentation/`에 발표 산출물을 둔다.

| 파일 | 용도 |
|---|---|
| `presentation_report.md` | 발표 흐름, 핵심 주장, 논문 역할, 실험 근거, 예상 질문을 통합한 발표용 보고서 |
| `presentation_report.html` | 브라우저 열람/인쇄용 발표 보고서 |
| `presentation_slides.md` | 슬라이드 원본 |
| `presentation_slides.html` | 하단 이동 버튼과 키보드로 넘길 수 있는 브라우저 발표용 슬라이드 |
| `speaker_notes.md` | 슬라이드별 발표자 대본 |
| `qna.md` | 예상 질문과 답변 |
| `one_page_handout.md` | 청중 배포용 1페이지 요약 |

`speaker_notes.md`, `qna.md`, `one_page_handout.md`는 선택 파일이 아니라 기본 발표 보조 산출물이다. 발표가 필요 없는 주차라면 해당 주차 README 또는 제출 체크리스트에 생략 사유를 남긴다.

`presentation_slides.html`에는 공통으로 하단 중앙 슬라이드 이동 버튼(`이전`, `현재/전체`, `다음`)을 넣고, 방향키/PageUp/PageDown/Home/End 키보드 이동도 지원한다. 기존 W01/W02처럼 주차 번호가 붙은 슬라이드 파일명을 쓰는 경우에도, 발표용 보고서에는 어떤 파일이 최종 발표본인지 명시한다. 발표용 보고서와 발표 보조자료의 수치와 주장은 통합보고서 및 `04_experiment/outputs/` 산출물과 일치해야 한다.

## 제출용 보고서 규칙

각 주차의 최종 제출본은 `07_week_submission/`에 둔다.

| 파일 | 용도 |
|---|---|
| `wXX_submission_report.md` | 제출용 보고서 Markdown 원본 |
| `wXX_submission_report.html` | 브라우저 열람/인쇄용 제출 보고서 |
| `submit_checklist.md` | 제출 전 점검표 |

제출용 보고서는 통합보고서, 발표용 보고서, 실험 산출물의 내용을 하나의 제출 문서로 압축한 것이다. HTML은 Markdown 제출본과 같은 수치와 상태를 담아야 한다. DOI/URL 미검증 항목은 제출용 보고서에서도 `확인 필요`로 유지한다.

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
