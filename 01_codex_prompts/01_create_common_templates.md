# 01_create_common_templates.md
# 01_공통템플릿_생성.md

## Codex 작업 지시서: 공통 보고서 템플릿 생성

## 1. 작업 목표

`02_report_templates/` 폴더에 AI보안 주차별 보고서 작성을 위한 공통 템플릿을 생성하라.

보고서 본문은 한글로 작성해도 되지만, 파일명과 폴더명은 영문, 숫자, 언더바를 우선 사용한다.

---

## 2. 생성할 파일

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
├── presentation_slide_navigation_snippet.html
├── speaker_notes_template.md
├── qna_template.md
├── one_page_handout_template.md
├── submission_report_template.md
├── ai_worklog_template.md
├── final_paper_bridge_template.md
└── submission_checklist_template.md
```

---

## 3. `02_report_templates/README.md`

```markdown
# 02_report_templates

이 폴더는 AI 보안 주차별 보고서 작성을 위한 공통 템플릿을 보관한다.

## 템플릿 종류

- 주차별 통합보고서
- 논문요약
- 논문비교표
- 이론정리
- 실습보고서
- 발표용 보고서
- 발표용 슬라이드
- 발표자 대본
- 발표 예상 Q&A
- 1페이지 발표 요약
- 제출용 보고서
- AI 활용기록
- 기말논문 연결표
- 제출 전 체크리스트

## 작성 원칙

- 파일명은 영문, 숫자, 언더바를 사용한다.
- Markdown 본문은 한글로 작성한다.
- 논문 제목, DOI, 저자명은 임의 생성하지 않는다.
- 확인하지 못한 정보는 `확인 필요`로 표시한다.
- 본문 인용과 참고문헌 목록은 서로 대응시킨다.
- 미검증 문헌은 핵심 근거로 사용하지 않는다.
- 수식 또는 알고리즘은 논문 기여, 공격·방어 원리, 평가 지표를 이해하는 데 필요한 경우에만 포함한다.
- 수식을 포함할 때는 원문 또는 검증 가능한 표준 수식 기준으로 기호 정의, 직관적 설명, 보안 해석, 평가 지표 연결, 한계를 함께 적는다.
- 원문 확인이 부족한 수식은 `확인 필요`로 표시하고 임의로 작성하지 않는다.
- 수식 작성은 Markdown + LaTeX math를 기본으로 하며, HTML은 KaTeX/MathJax, 문서 변환은 Pandoc, 검산은 필요 시 `sympy`를 사용한다.
- 발표 기본 패키지는 `presentation_report.md`, `presentation_report.html`, `presentation_slides.md`, `presentation_slides.html`, `speaker_notes.md`, `qna.md`, `one_page_handout.md`로 구성한다.
- `presentation_slides.html`에는 `presentation_slide_navigation_snippet.html` 또는 `presentation_slides_template.md`의 공통 이동 버튼 스니펫을 반영한다.
- 슬라이드 이동은 이전/다음 화살표, 현재/전체 카운터, 방향키/PageUp/PageDown/Space/Home/End 키보드 이동을 모두 지원해야 한다.
- 실험 결과는 실제 실행 로그가 있을 때만 확정한다.
- 실행 완료 시 `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md`를 보존하고 관련 보고서와 제출 체크리스트를 함께 갱신한다.
- 실험 실행 명령어, 실행일, seed, Python/package 버전, 주요 config 상태를 기록한다.
- 실제 개인정보, 운영 서비스, 무단 API 질의, 실행 가능한 공격 절차는 실습 범위에서 제외한다.
- AI 도구를 사용한 경우 사용 도구, 사용 목적, 주요 프롬프트, 반영 위치, 사람 검토와 검증 방식을 기록한다.
- AI 산출물은 초안으로만 사용하며 최종 내용, 인용, 실험결과, 연구윤리 책임은 작성자에게 있다.
- 기말논문 연결자료에는 주차별 보고서 최소 2개 이상을 어떻게 반영할 수 있는지 추적 가능하게 기록한다.
```

---

## 4. `weekly_integrated_report_template.md`

```markdown
# 주차별 통합보고서 템플릿

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 |  |
| 주제 |  |
| 작성자 |  |
| 작성일 |  |
| 사용 AI 도구 |  |
| 실습 환경 | Ubuntu 24.04 / Docker |

---

## 1. 한 문장 요약

> 이번 주의 핵심은 _______ 이다.

---

## 2. AI 원리 70% 정리

### 2.1 핵심 이론

### 2.2 핵심 개념

| 개념 | 정의 | 쉬운 설명 | 관련 논문 |
|---|---|---|---|
|  |  |  |  |

### 2.3 수식 또는 알고리즘

수식 또는 알고리즘은 이번 주 논문을 이해하는 데 필요한 경우에만 작성한다. 원문 확인이 부족하면 `확인 필요`로 표시한다.

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 |  |
| 원문 출처 | 논문/쪽/절 확인 필요 |
| 작성 형식 | Markdown + LaTeX math |
| 렌더링/변환 도구 | Pandoc / KaTeX / MathJax / LaTeX 중 선택 |
| 검산 도구 | 사용 안 함 / sympy / numpy / scipy / 기타 |
| 수식 또는 절차 |  |
| 기호 설명 |  |
| 직관적 의미 |  |
| 보안 관점 해석 |  |
| 평가 지표와 연결 |  |
| 한계와 가정 |  |

### 2.4 보안 연구와의 연결

---

## 3. 보안 이슈 30% 정리

### 3.1 주요 보안 이슈

### 3.2 CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality |  |  |
| Integrity |  |  |
| Availability |  |  |
| Privacy |  |  |
| Safety |  |  |
| Accountability |  |  |

---

## 4. 논문 5편 요약

| 번호 | 논문 제목 | 핵심 기여 | 한계 | 내 연구 활용 |
|---:|---|---|---|---|
| P01 |  |  |  |  |
| P02 |  |  |  |  |
| P03 |  |  |  |  |
| P04 |  |  |  |  |
| P05 |  |  |  |  |

---

## 5. 논문 5편 비교

| 논문 | 연구문제 | 방법론 | 데이터/실험 | 보안 위협 | 평가 지표 | 한계 |
|---|---|---|---|---|---|---|
| P01 |  |  |  |  |  |  |
| P02 |  |  |  |  |  |  |
| P03 |  |  |  |  |  |  |
| P04 |  |  |  |  |  |  |
| P05 |  |  |  |  |  |  |

---

## 6. Research Track

### 6.1 연구문제

> 연구문제: _______

### 6.2 위협모형

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

### 6.3 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 |
|---|---|---|---|
| Clean Accuracy |  |  |  |
| Attack Success Rate |  |  |  |
| Robust Accuracy |  |  |  |
| Privacy Leakage |  |  |  |
| Utility |  |  |  |
| Cost |  |  |  |

### 6.4 재현성

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 |
| Docker |  |
| Python |  |
| 주요 라이브러리 |  |
| Dataset |  |
| Seed |  |
| Config 상태 | design_only / executed |
| 실행 명령어 |  |

### 6.5 한계와 오픈문제

| 번호 | 오픈문제 | 왜 어려운가 | 기말 논문 연결 가능성 |
|---:|---|---|---|
| 1 |  |  | 높음 / 보통 / 낮음 |
| 2 |  |  | 높음 / 보통 / 낮음 |
| 3 |  |  | 높음 / 보통 / 낮음 |

---

## 7. 실습 요약

### 7.1 실습 목표

### 7.2 실습 환경

### 7.3 실험 설계

### 7.4 실험 결과

실행 전이면 `실행 전`으로 표시한다. 실행 완료 시 `04_experiment/outputs/run_log.md` 기준으로 정량값을 기록하고, `metrics_summary.csv`와 `results.json` 보존 여부를 함께 적는다.

### 7.5 오류와 해결

---

## 8. AI 활용 기록 요약

| 도구 | 사용 목적 | 반영 위치 | 검증 방식 |
|---|---|---|---|
|  |  |  |  |

---

## 9. 토론 질문

1. 
2. 
3. 

---

## 10. 기말 논문 연결

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 |  |
| 관련연구 |  |
| 연구문제 |  |
| 연구방법 |  |
| 분석/실험 |  |
| 보안적 함의 |  |
| 결론 |  |

---

## 11. 참고문헌 검증표

| 번호 | 문헌 | DOI/URL | 검증 경로 | 상태 |
|---:|---|---|---|---|
| 1 |  |  |  | 확인 필요 |

---

## 12. 자기 점검

| 점검 항목 | 확인 |
|---|---|
| 논문 5편을 모두 정리했다. | □ |
| AI 원리 70%, 보안 이슈 30%를 반영했다. | □ |
| Research Track 5요소를 작성했다. | □ |
| 실행하지 않은 실험 수치를 결과처럼 작성하지 않았다. | □ |
| 실행 완료 시 `outputs/` 산출물과 보고서 수치가 일치한다. | □ |
| `config.yaml` 상태와 실제 산출물 상태가 일치한다. | □ |
| 미검증 문헌을 핵심 근거로 사용하지 않았다. | □ |
| 본문 인용과 참고문헌 목록이 대응한다. | □ |
| 실제 개인정보, 운영 서비스, 무단 API 질의, 실행 가능한 공격 절차를 제외했다. | □ |
| AI 활용기록을 작성했다. | □ |
| AI 산출물 반영 위치와 검증 방식을 기록했다. | □ |
| 참고문헌 검증표를 작성했다. | □ |
| 기말 논문 연결표를 작성했다. | □ |
```

---

## 5. `paper_summary_template.md`

```markdown
# 논문요약 템플릿

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 |  |
| 저자 |  |
| 학술지/학회 |  |
| 연도 |  |
| DOI/URL |  |
| PDF 파일명 |  |
| 검증 상태 | 확인 필요 |

---

## 2. 한 문장 요약

> 이 논문은 _______ 문제를 _______ 방법으로 다루며, _______ 기여를 제시한다.

---

## 3. 연구문제

- 이 논문이 해결하려는 문제:
- 기존 연구의 한계:
- 핵심 연구질문:

---

## 4. 핵심 개념

| 개념 | 설명 | 내 연구와의 관련성 |
|---|---|---|
|  |  |  |

---

## 5. 방법론

| 항목 | 내용 |
|---|---|
| 사용 방법 |  |
| 데이터셋 |  |
| 실험 조건 |  |
| 평가 지표 |  |

---

## 6. 주요 결과

| 결과 | 의미 | 한계 |
|---|---|---|
|  |  |  |

---

## 7. 보안 관점 분석

| 항목 | 내용 |
|---|---|
| 공격자 |  |
| 공격 대상 |  |
| 공격자의 능력 |  |
| 방어자 가정 |  |
| 공격 성공 조건 |  |
| 평가 지표 |  |

---

## 8. 한계와 오픈문제

1. 
2. 
3. 

---

## 9. 기말 논문에 반영할 부분

| 기말 논문 위치 | 반영 가능 내용 |
|---|---|
| 서론 |  |
| 관련연구 |  |
| 연구문제 |  |
| 연구방법 |  |
| 분석/실험 |  |
| 보안적 함의 |  |
| 결론 |  |
```

---

## 6. `paper_matrix_template.md`

```markdown
# 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | 보안 위협 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 |  |  |  |  |  |  |  |
| P02 |  |  |  |  |  |  |  |
| P03 |  |  |  |  |  |  |  |
| P04 |  |  |  |  |  |  |  |
| P05 |  |  |  |  |  |  |  |

---

## 종합 비교

### 1. 공통적으로 다루는 문제

-

### 2. 논문 간 차이점

-

### 3. 아직 해결되지 않은 문제

-

### 4. 기말 논문 주제로 발전 가능한 연결부

-
```

---

## 7. `theory_note_template.md`

```markdown
# 이론정리 템플릿

## 1. AI 원리 70%

### 1.1 핵심 이론

### 1.2 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 |
|---|---|---|---|
|  |  |  |  |

### 1.3 수식 또는 알고리즘

필요한 경우에만 작성한다. 수식이 핵심 기여나 평가 지표와 연결되지 않으면 개념 설명으로 대체한다.

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 |  |
| 원문 또는 표준 출처 |  |
| 작성 형식 | Markdown + LaTeX math |
| 렌더링/변환 도구 | Pandoc / KaTeX / MathJax / LaTeX 중 선택 |
| 검산 도구 | 사용 안 함 / sympy / numpy / scipy / 기타 |
| 기호 정의 |  |
| 직관적 설명 |  |
| 보안 위협/방어와의 연결 |  |
| 평가 지표와의 연결 |  |
| 적용 범위와 한계 |  |

### 1.4 초보자용 설명

### 1.5 보안 연구와의 연결

---

## 2. 보안 이슈 30%

### 2.1 주요 보안 이슈

### 2.2 CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality |  |  |
| Integrity |  |  |
| Availability |  |  |
| Privacy |  |  |
| Safety |  |  |
| Accountability |  |  |

---

## 3. 핵심 용어

| 용어 | 영문 | 쉬운 설명 | 논문에서의 의미 |
|---|---|---|---|
|  |  |  |  |

---

## 4. 위협모형

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

---

## 5. 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Clean Accuracy |  |  |  |  |
| Attack Success Rate |  |  |  |  |
| Robust Accuracy |  |  |  |  |
| Privacy Leakage |  |  |  |  |
| Utility |  |  |  |  |
| Cost |  |  |  |  |
| Reproducibility |  |  |  |  |

---

## 6. 한계와 오픈문제

| 번호 | 오픈문제 | 왜 어려운가 | 필요한 연구 | 기말 논문 연결 가능성 |
|---:|---|---|---|---|
| 1 |  |  |  | 높음 / 보통 / 낮음 |
| 2 |  |  |  | 높음 / 보통 / 낮음 |
| 3 |  |  |  | 높음 / 보통 / 낮음 |
```

---

## 8. `experiment_report_template.md`

````markdown
# 실습보고서 템플릿

## 1. 실습 목표

-

---

## 2. 실습 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 24.04 |
| 실행 방식 | Docker |
| Python | 3.11 (`python:3.11-slim`) |
| 패키지 관리자 | uv (Dockerfile 내부 포함) |
| 의존성 설치 | 컨테이너 내부 `uv sync` |
| Dataset | 확인 필요 |
| Seed | 확인 필요 |
| 결과 상태 | 설계만 완료 / 실행 완료 |
| Config 상태 | design_only / executed |
| GPU | Optional |

---

## 3. 프로젝트 구조

```text
experiment/
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
````

Dockerfile은 WSL 호스트에 uv를 설치하지 않고, 다음 방식으로 이미지 안에 uv를 포함한다.

```dockerfile
FROM python:3.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv sync --no-dev
```

---

## 4. 실행 명령어

```bash
docker build -t aisec-experiment .
docker run --rm -it -v $(pwd):/workspace aisec-experiment bash
python src/run_experiment.py --config configs/config.yaml
```

---

## 5. 실험 설계

| 항목 | 내용 |
|---|---|
| Baseline |  |
| Attack/Threat Scenario |  |
| Defense/Check |  |
| Evaluation Metric |  |
| Dataset | 공개 데이터 / synthetic data / toy data |
| Seed |  |
| Safety Scope | 실제 개인정보, 운영 서비스, 무단 공격 절차 제외 |

---

## 6. 실험 결과

실행 전에는 결과값을 비워 두거나 `실행 전`으로 표시한다. 실행 후에는 `outputs/run_log.md` 기준으로 아래 표를 채우고, CSV/JSON 원본을 함께 보존한다.

| 조건 | 주요 지표 | 결과 | 근거 파일 |
|---|---|---|---|
| Clean baseline | Accuracy/F1/Task score | 실행 전 |  |
| Security scenario | ASR/Attack impact/Risk score | 실행 전 |  |
| Defense/check | Robust score/Leakage score | 실행 전 |  |
| Reproducibility | Seed/config/log 확인 | 실행 전 |  |

---

## 7. 오류와 해결

| 오류 | 원인 | 해결 |
| -- | -- | -- |
|    |    |    |

---

## 8. 논문과의 연결

*

---

## 9. 재현 가능성 점검

* [ ] Dockerfile 존재
* [ ] pyproject.toml 존재
* [ ] WSL 호스트에 uv 미설치
* [ ] Dockerfile 내부 uv 복사 명령 확인
* [ ] 컨테이너 내부 uv sync 실행
* [ ] config.yaml 존재
* [ ] config.yaml 상태와 실제 산출물 상태 일치
* [ ] seed 고정
* [ ] Python/package 버전 기록
* [ ] `outputs/results.json` 저장
* [ ] `outputs/metrics_summary.csv` 저장
* [ ] `outputs/run_log.md` 저장
* [ ] 실행 명령어 기록
* [ ] 실행 후 통합보고서, 제출 체크리스트, AI 활용기록 갱신
* [ ] 실행하지 않은 수치를 결과처럼 작성하지 않았음
* [ ] 실제 개인정보, 운영 서비스, 무단 API 질의, 실행 가능한 공격 절차 제외

````

---

## 9. `presentation_report_template.md`

```markdown
# 발표용 보고서 템플릿

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | WXX |
| 주제 |  |
| 발표 시간 | 8-10분 |
| 권장 슬라이드 수 | 10-14장 |
| 핵심 메시지 |  |

## 2. 한 문장 요약

## 3. 발표 흐름

| 순서 | 슬라이드 주제 | 핵심 내용 | 시간 |
|---:|---|---|---:|
| 1 | 표지 | 주제와 핵심 질문 | 0:30 |
| 2 | 배경 | 왜 중요한가 | 1:00 |
| 3 | AI 원리 | 모델/학습/평가 핵심 | 2:00 |
| 4 | 보안 이슈 | 위협모형과 공격면 | 2:00 |
| 5 | 논문 비교 | 5편의 역할과 차이 | 1:30 |
| 6 | 실습/실험 | 실행 상태와 결과 근거 | 1:30 |
| 7 | 기말논문 연결 | 연구문제와 contribution | 1:00 |
| 8 | 결론/Q&A | 핵심 takeaway | 0:30 |

## 4. 논문 5편의 발표 역할

| ID | 논문 | 발표에서 맡는 역할 | 강조할 한계 |
|---|---|---|---|
| P01 |  |  |  |
| P02 |  |  |  |
| P03 |  |  |  |
| P04 |  |  |  |
| P05 |  |  |  |

## 5. 실습/실험 결과

실행 전이면 `실행 전`으로 표시한다. 실행 완료 시 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 대조 가능한 값만 적는다.

| 조건 | 주요 지표 | 결과 | 발표 해석 |
|---|---|---|---|
| Clean baseline |  | 실행 전 |  |
| Security scenario |  | 실행 전 |  |
| Defense/check |  | 실행 전 |  |

## 6. 예상 질문과 답변

| 질문 | 답변 요지 | 근거 파일 |
|---|---|---|
|  |  |  |

## 7. 발표 보조자료 점검

| 파일 | 작성 원칙 |
|---|---|
| `speaker_notes.md` | 슬라이드별 발화 흐름과 시간 배분 작성 |
| `qna.md` | 예상 질문 6개 이상과 근거 파일 작성 |
| `one_page_handout.md` | 청중 배포용 1페이지 요약 작성 |
```

---

## 10. `presentation_slides_template.md`

```markdown
# 발표용 슬라이드 템플릿

슬라이드는 8-10분 발표 기준 10-14장으로 작성한다. 한 장에는 하나의 주장만 둔다. 슬라이드 작성 후 `speaker_notes.md`, `qna.md`, `one_page_handout.md`를 같은 `09_presentation/` 폴더에 함께 작성한다.

HTML 슬라이드(`presentation_slides.html`)에는 모든 주차 공통으로 슬라이드 이동 버튼을 넣는다. 기본 구현은 `presentation_slide_navigation_snippet.html` 또는 `presentation_slides_template.md` 하단의 HTML 공통 이동 버튼 스니펫을 사용한다. 이전/다음 화살표, 현재/전체 카운터, 방향키/PageUp/PageDown/Space/Home/End 이동을 지원해야 한다.

---

# WXX 주차 제목

## 발표 핵심

이번 주차의 핵심 메시지를 1-2문장으로 작성한다.

---

# 1. 왜 중요한가

---

# 2. 발표 로드맵

---

# 3. AI 원리 70%

---

# 4. 보안 이슈 30%

---

# 5. 논문 5편의 역할

---

# 6. 위협모형

---

# 7. 평가 프로토콜

---

# 8. 실습/실험

실행 전이면 `실행 전`으로 표시한다. 실행 완료 시 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 쓴다.

---

# 9. 결과와 해석

---

# 10. 한계

---

# 11. 기말논문 연결

---

# 12. 결론
```

---

## 10-1. `presentation_slide_navigation_snippet.html`

```html
<!--
  공통 슬라이드 이동 스니펫
  사용 위치: presentation_slides.html
  전제: 각 슬라이드는 <section> 요소로 작성한다.
-->
<nav class="slide-nav" aria-label="슬라이드 이동">
  <button id="prevSlide" type="button" title="이전 슬라이드" aria-label="이전 슬라이드">‹</button>
  <span id="slideCounter" class="slide-counter" aria-live="polite">1 / 1</span>
  <button id="nextSlide" type="button" title="다음 슬라이드" aria-label="다음 슬라이드">›</button>
</nav>
```

실제 파일에는 CSS와 JavaScript까지 포함해 `02_report_templates/presentation_slide_navigation_snippet.html`과 같은 완성형 스니펫으로 작성한다.

---

## 11. `speaker_notes_template.md`

```markdown
# 발표자 대본 템플릿

## 발표 기준

| 항목 | 내용 |
|---|---|
| 주차 | WXX |
| 주제 |  |
| 권장 시간 | 8-10분 |
| 기준 슬라이드 | `presentation_slides.md`, `presentation_slides.html` |
| 수치 근거 | `04_experiment/outputs/run_log.md` 또는 `실행 전` |

## 사용 원칙

- 슬라이드 순서와 같은 순서로 작성한다.
- 각 슬라이드마다 예상 시간을 적는다.
- 실험 수치는 `04_experiment/outputs/` 산출물과 일치하는 값만 말한다.
- 확인하지 못한 DOI/URL, 논문 원문 세부 수치, 실행하지 않은 결과는 확정 표현으로 말하지 않는다.
```

---

## 12. `qna_template.md`

```markdown
# 발표 예상 질문과 답변 템플릿

## 기준

| 항목 | 내용 |
|---|---|
| 주차 | WXX |
| 주제 |  |
| 발표 파일 | `presentation_report.md`, `presentation_slides.md` |
| 실험 근거 | `04_experiment/outputs/run_log.md` 또는 `실행 전` |

## 작성 원칙

- 최소 6개 이상의 질문을 준비한다.
- 실험 일반화, 지표 정의, 논문 검증 상태, 기말논문 연결 질문을 반드시 포함한다.
- 답변마다 근거 파일을 적는다.
- 확인하지 못한 논문 세부 정보나 실행하지 않은 실험 결과는 확정하지 않는다.
```

---

## 13. `one_page_handout_template.md`

```markdown
# 1페이지 발표 요약 템플릿

## 주제

WXX 주차 제목을 적는다.

## 핵심 주장

이번 발표에서 청중이 기억해야 할 한 문장 결론을 적는다.

## 발표 흐름

| 구분 | 핵심 내용 |
|---|---|
| AI 원리 |  |
| 보안 이슈 |  |
| 문헌 역할 |  |
| 평가 관점 |  |
| 기말 연결 |  |

## 실습/실험 요약

실행 전이면 `실행 전`으로 표시한다. 실행 완료 시 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 적는다.
```

---

## 14. `submission_report_template.md`

```markdown
# 제출용 보고서 템플릿

## 표지

| 항목 | 내용 |
|---|---|
| 주차 | WXX |
| 보고서 제목 |  |
| 과목 범위 | AI 보안 |
| 작성일 |  |
| 문서 상태 | 제출용 통합본 |
| 관련 산출물 위치 |  |

## 초록

주차의 AI 원리, 보안 이슈, 문헌 5편, 실습/실험 결과 또는 실행 전 상태, 기말논문 연결을 1문단으로 요약한다.

## 1. 서론

## 2. AI 원리

## 3. 보안 이슈

## 4. 문헌 요약

## 5. Research Track

## 6. 실습 설계와 결과

실행 전이면 `실행 전`으로 표시한다. 실행 완료 시 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 기록한다.

## 7. 발표용 보고서

## 8. 기말논문 연결

## 9. AI 활용 고지

## 10. 참고문헌

DOI/URL은 검증 전까지 `확인 필요`로 표시한다.

## 11. 제출 전 점검표
```

---

## 15. `ai_worklog_template.md`

```markdown
# AI 활용기록 템플릿

## 1. AI 활용 기록

| 날짜 | 사용 도구 | 사용 목적 | 산출물 | 검증 방식 |
|---|---|---|---|---|
|  | ChatGPT / Codex / Claude / Gemini |  |  |  |

---

## 2. 주요 프롬프트

### Prompt 1

```text

````

### Prompt 2

```text
```

---

## 3. AI 출력물 기록

| 번호 | 사용 도구 | 출력 요약 | 반영 여부            | 반영 위치 |
| -: | ----- | ----- | ---------------- | ----- |
|  1 |       |       | 반영 / 미반영 / 일부 반영 |       |

---

## 4. 본인 검토 및 수정 기록

| AI 산출물 | 문제점 | 본인 수정 내용 | 검증 근거 |
| ------ | --- | -------- | ----- |
|        |     |          |       |

---

## 5. AI 활용 고지서 초안

| 항목           | 작성 내용                                             |
| ------------ | ------------------------------------------------- |
| 사용한 AI 도구명   |                                                   |
| 사용 일자        |                                                   |
| 사용 목적        | 번역 / 수식 설명 / 개념 설명 / 문장 교정 / 제목 후보 / 코드 점검 / 기타   |
| 주요 프롬프트      |                                                   |
| AI 산출물 반영 위치 |                                                   |
| 본인 수정 내용     |                                                   |
| 사실관계 검증 방법   |                                                   |
| 참고문헌 검증 방법   |                                                   |
| 최종 책임 확인     | 본인은 최종 원고의 내용, 인용, 실험결과, 연구윤리 책임이 본인에게 있음을 확인합니다. |

````

---

## 16. `final_paper_bridge_template.md`

```markdown
# 기말논문 연결표 템플릿

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 |  |  |  |  | 높음 / 보통 / 낮음 |
| 2 |  |  |  |  | 높음 / 보통 / 낮음 |
| 3 |  |  |  |  | 높음 / 보통 / 낮음 |

---

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 |  |
| 관련연구 |  |
| 연구문제 |  |
| 연구방법 |  |
| 분석/실험 |  |
| 보안적 함의 |  |
| 결론 |  |

---

## 3. Contribution 후보

### 후보 1

본 연구는 _______ 환경에서 _______ 위협을 분석하고, _______을 제안한다.

### 후보 2

본 연구는 기존 _______ 연구의 한계를 보완하기 위해 _______ 평가 기준을 제시한다.

### 후보 3

본 연구는 _______ 공격에 대한 _______ 기반 점검표를 설계하고, _______ 관점에서 보안적 함의를 도출한다.

---

## 4. 주차별 보고서 반영표 초안

| 번호 | 기존 보고서 제목 | 기말 논문에 반영한 위치 | 반영 내용 |
|---:|---|---|---|
| 1 |  | 예: 2장 관련연구 |  |
| 2 |  | 예: 4장 연구방법 |  |
| 3 |  | 선택 |  |
````

---

## 17. `submission_checklist_template.md`

```markdown
# 제출 전 체크리스트

| 확인 | 점검 항목 |
|---|---|
| □ | 최종 보고서 파일명을 확인했다. |
| □ | PDF 변환을 완료했다. |
| □ | 표와 그림이 깨지지 않았는지 확인했다. |
| □ | 참고문헌과 본문 인용이 일치하는지 확인했다. |
| □ | 미검증 문헌을 핵심 근거로 사용하지 않았다. |
| □ | 논문 제목, 저자, 연도, 학술지명, DOI/URL을 임의 생성하지 않았다. |
| □ | 핵심 수식 또는 알고리즘이 필요한 경우 기호, 직관, 보안 해석, 평가 지표 연결을 설명했다. |
| □ | 확인하지 못한 수식 또는 알고리즘을 임의로 작성하지 않았다. |
| □ | AI 활용 기록을 포함했다. |
| □ | AI 활용 기록에 사용 도구, 목적, 주요 프롬프트, 반영 위치, 검증 방식을 포함했다. |
| □ | 실습 결과를 과장 없이 작성했다. |
| □ | 실행하지 않은 실험 결과를 결과처럼 작성하지 않았다. |
| □ | 실행 완료 주차는 `outputs/run_log.md`, `metrics_summary.csv`, `results.json`을 포함했다. |
| □ | 실험 실행 명령어, 실행일, seed, Python/package 버전, config 상태를 기록했다. |
| □ | `config.yaml`의 `design_only` 또는 `executed` 상태와 실제 산출물 상태가 일치한다. |
| □ | 실험 보고서, 통합보고서, 제출 체크리스트, AI 활용기록의 결과 상태가 서로 일치한다. |
| □ | 실제 개인정보, 운영 서비스, 무단 API 질의, 실행 가능한 공격 절차를 포함하지 않았다. |
| □ | 발표용 보고서, 슬라이드, 발표 보조자료를 `09_presentation/`에 포함했다. |
| □ | 발표자 대본, 예상 Q&A, 1페이지 요약을 작성했다. |
| □ | 제출본 폴더에는 최종본만 넣었다. |
| □ | DOI/URL 검증표를 확인했다. |
| □ | AI 활용 고지서를 작성했다. |
| □ | 기말 논문 연결표에 주차별 보고서 최소 2개 이상 반영 근거를 남겼다. |
```
