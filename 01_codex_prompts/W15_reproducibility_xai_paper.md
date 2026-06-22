# W15_reproducibility_xai_paper.md

## Codex 작업 지시서: Week 15 보고서 작성

## 1. 작업 대상

```text
03_weekly_reports/w15_reproducibility_xai_paper/
```

## 2. 주차 정보

| 항목    | 내용                                                         |
| ----- | ---------------------------------------------------------- |
| 주차    | W15                                                        |
| 주제    | 연구평가·재현성·설명가능성(XAI)·논문 구성                                  |
| AI 원리 | Evaluation, reproducibility, XAI, paper structure          |
| 보안 이슈 | Benchmark contamination, model leakage, policy/ethics risk |
| 논문 패킷 | 5편                                                         |

---

## 3. 논문 패킷

1. J. Chang et al., "A Survey on Evaluation of Large Language Models", ACM Computing Surveys, 2024.
2. R. Ashmore et al., "Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges", ACM Computing Surveys, 2021.
3. Vivek Dwivedi et al., "Explainable AI: Core Ideas, Techniques, and Solutions", ACM Computing Surveys, 2023.
4. A. B. Arrieta et al., "Explainable Artificial Intelligence (XAI): Concepts, Taxonomies, Opportunities and Challenges toward Responsible AI", Information Fusion, 2020.
5. K. D. et al., "Concept-based Explainable Artificial Intelligence: A Survey", ACM Computing Surveys, 2025.

---

## 4. 작성 목표

다음 산출물을 작성하라.

1. 논문 5편 요약
2. 논문 5편 비교표
3. AI 원리 70% 정리
4. 보안 이슈 30% 정리
5. Research Track 작성

   * 연구문제
   * 위협모형
   * 평가방법
   * 재현성
   * 한계와 오픈문제
6. Docker 기반 실습 보고서 초안
7. AI 활용기록
8. 기말논문 연결표
9. 주차별 통합보고서 최종본
10. 기말논문 최종 주제 후보 압축
11. 최종 Contribution 문장 1~2개 도출

---

## 5. 작성할 파일

아래 파일을 작성하거나 보완하라.

```text
03_weekly_reports/w15_reproducibility_xai_paper/
├── 00_management/
│   ├── week_info.md
│   ├── todo_checklist.md
│   ├── grading_rubric.md
│   └── progress_log.md
│
├── 01_papers/
│   ├── paper_list.md
│   ├── doi_check.md
│   └── download_source.md
│
├── 02_paper_summaries/
│   ├── P01_summary.md
│   ├── P02_summary.md
│   ├── P03_summary.md
│   ├── P04_summary.md
│   ├── P05_summary.md
│   └── paper_matrix.md
│
├── 03_theory_notes/
│   ├── ai_principle_70.md
│   ├── security_issue_30.md
│   ├── key_terms.md
│   ├── threat_model.md
│   ├── evaluation_protocol.md
│   └── open_problems.md
│
├── 04_experiment/
│   ├── experiment_report.md
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── pyproject.toml
│   └── configs/config.yaml
│
├── 05_ai_worklog/
│   ├── ai_worklog.md
│   ├── prompts.md
│   ├── ai_outputs.md
│   ├── human_review.md
│   └── ai_disclosure_draft.md
│
├── 06_report/
│   ├── draft/integrated_report_draft.md
│   ├── final/integrated_report_final.md
│   └── review/self_review.md
│
├── 07_week_submission/
│   ├── README.md
│   ├── submit_checklist.md
│   ├── wXX_submission_report.md
│   └── wXX_submission_report.html
│
├── 08_final_paper_bridge/
│   ├── final_paper_bridge.md
│   ├── topic_candidates.md
│   ├── contribution_candidates.md
│   └── weekly_reflection_table.md
│
└── 09_presentation/
    ├── presentation_report.md
    ├── presentation_report.html
    ├── presentation_slides.md
    ├── presentation_slides.html
    ├── speaker_notes.md
    ├── qna.md
    └── one_page_handout.md
```

---

## 6. 논문별 작성 지시

각 논문 요약 파일에는 다음 항목을 반드시 포함하라.

```markdown
# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 |  |
| 저자 |  |
| 학술지/학회 |  |
| 연도 |  |
| DOI/URL | 확인 필요 |
| PDF 파일명 |  |
| 검증 상태 | 확인 필요 |

## 2. 한 문장 요약

> 이 논문은 _______ 문제를 _______ 방법으로 다루며, _______ 기여를 제시한다.

## 3. 연구문제

## 4. 핵심 개념

## 5. 방법론

## 6. 주요 결과

## 7. 보안 관점 분석

## 8. 한계와 오픈문제

## 9. 기말 논문에 반영할 부분
```

---

## 7. 논문 비교표 작성 지시

`02_paper_summaries/paper_matrix.md`에는 다음 표를 작성하라.

```markdown
# W15 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | 보안 위협 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 |  |  |  |  |  |  |  |
| P02 |  |  |  |  |  |  |  |
| P03 |  |  |  |  |  |  |  |
| P04 |  |  |  |  |  |  |  |
| P05 |  |  |  |  |  |  |  |

## 종합 비교

### 1. 공통적으로 다루는 문제

### 2. 논문 간 차이점

### 3. 아직 해결되지 않은 문제

### 4. 기말 논문 주제로 발전 가능한 연결부
```

---

## 8. AI 원리 70% 작성 지시

`03_theory_notes/ai_principle_70.md`에는 다음 내용을 중심으로 정리하라.

1. AI 모델 평가의 기본 개념
2. LLM 평가 프레임워크
3. Benchmark contamination
4. Evaluation leakage
5. Reproducibility의 의미
6. ML lifecycle assurance
7. XAI의 핵심 개념
8. Feature-based explanation
9. Concept-based explanation
10. Responsible AI와 XAI의 관계
11. 논문 구성에서 contribution, limitation, revision strategy의 역할

표 형식:

```markdown
# AI 원리 70% 정리

## 1. 핵심 이론

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 |
|---|---|---|---|
| Evaluation |  |  | P01 |
| Benchmark Contamination |  |  | P01 |
| Reproducibility |  |  | P01, P02 |
| ML Lifecycle Assurance |  |  | P02 |
| XAI |  |  | P03, P04, P05 |
| Concept-based XAI |  |  | P05 |
| Contribution |  |  | 전체 |
| Limitation |  |  | 전체 |

## 3. 수식 또는 알고리즘

## 4. 초보자용 설명

## 5. 보안 연구와의 연결
```

---

## 9. 보안 이슈 30% 작성 지시

`03_theory_notes/security_issue_30.md`에는 다음 내용을 중심으로 정리하라.

1. Benchmark contamination
2. Hidden test leakage
3. Evaluation reproducibility failure
4. Model leakage
5. XAI 공격면
6. Explanation misuse
7. Policy and ethics risk
8. AI tool 사용 투명성
9. AI 활용 고지
10. 연구윤리와 참고문헌 검증
11. 최종 논문 작성 시 허위 DOI·허위 인용 방지

표 형식:

```markdown
# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | Hidden test leakage / model leakage |  |
| Integrity | Benchmark contamination / fabricated citation |  |
| Availability | Irreproducible evaluation |  |
| Privacy | Sensitive information in explanation |  |
| Safety | Misleading explanation / unsafe model trust |  |
| Accountability | Missing AI disclosure / unverifiable reference |  |
```

---

## 10. Research Track 작성 지시

다음 5개 파일을 반드시 작성하라.

```text
03_theory_notes/threat_model.md
03_theory_notes/evaluation_protocol.md
03_theory_notes/open_problems.md
06_report/final/integrated_report_final.md
08_final_paper_bridge/final_paper_bridge.md
```

### 10.1 연구문제 예시

다음과 같은 방식으로 연구문제를 도출하라.

```markdown
# 연구문제 후보

RQ1. LLM과 AI 보안 연구에서 benchmark contamination과 evaluation leakage는 평가 신뢰성에 어떤 영향을 미치는가?

RQ2. XAI 기반 설명은 보안 평가에서 신뢰성 증거로 사용할 수 있는가, 아니면 새로운 공격면으로 보아야 하는가?

RQ3. AI 보안 논문에서 재현성, 참고문헌 검증, AI 활용 고지를 포함한 연구윤리 체크리스트는 어떻게 구성해야 하는가?
```

### 10.2 위협모형 표

```markdown
# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | AI 모델 평가 시스템 / XAI 분석 시스템 / AI 보안 논문 작성 프로세스 |
| 보호 자산 | 평가 데이터, 벤치마크, 실험 로그, 설명 결과, 참고문헌, 연구윤리 |
| 공격자 | 평가 데이터 오염자 / 모델 개발자 / 논문 작성자 / AI 도구 오용자 |
| 공격자의 지식 | White-box / Gray-box / Black-box |
| 공격자의 능력 | 평가 데이터 노출, 벤치마크 오염, 실험결과 과장, 참고문헌 조작, AI 산출물 무검증 사용 |
| 공격 경로 | 평가 데이터셋, 실험 환경, 설명가능성 도구, 참고문헌 목록, AI 활용기록 |
| 공격 성공 조건 | 성능이 과대평가되거나, 검증 불가능한 논문 결과가 제출됨 |
| 방어자 가정 | 참고문헌 검증, DOI 확인, 실험 로그 저장, AI 활용 고지, 재현성 점검 가능 |
| 제외 범위 | 실제 학술 부정행위 수행, 허위 결과 조작, 실제 심사 시스템 공격 |
```

### 10.3 평가방법 표

```markdown
# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Evaluation Reliability | Reliability score | 벤치마크 중복·오염 여부 확인 | Benchmark metadata | 평가 신뢰성 |
| Reproducibility | Re-run consistency | 동일 환경 반복 실행 | Config/logs/results | 재현성 |
| Reference Validity | Verification rate | DOI/URL/출판사 확인 | Reference list | 연구윤리 |
| AI Disclosure Quality | Disclosure completeness | AI 활용 고지 항목 충족률 | AI worklog | 투명성 |
| Explanation Reliability | Explanation stability | 입력 변화 전후 설명 비교 | XAI outputs | 설명 신뢰성 |
| Contribution Clarity | Contribution score | 기여문장 명확성 평가 | Paper draft | 논문 완성도 |
| Limitation Clarity | Limitation coverage | 한계와 후속연구 명시 여부 | Paper draft | 논문 신뢰성 |
```

---

## 11. 실습 방향

`04_experiment/experiment_report.md`에는 기말 논문 통합을 위한 재현성·검증 점검 실습을 설계하라.

실습 목표:

1. 전체 주차 보고서에서 기말 논문 후보 주제 선별
2. 주차별 보고서 최소 2개 이상 반영표 작성
3. 참고문헌 DOI/URL 검증표 작성
4. AI 활용 고지서 초안 작성
5. 실험이 있는 경우 config, seed, results, logs 확인
6. 최종 논문 contribution 문장 1~2개 확정
7. 결과는 실제 확인 전까지 빈칸으로 둔다.

실습 환경:

```text
OS: Ubuntu 24.04
Container: Docker
Python: 3.11 (python:3.11-slim)
Package manager: uv (Dockerfile 내부 포함, WSL 호스트 설치 금지)
Install: 컨테이너 내부 uv sync
Dataset: 해당 주제에 따라 확인 필요
Seed: 42
```

Dockerfile 원칙:

```text
FROM python:3.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv sync --no-dev
```

Docker 실행 예시:

```bash
docker build -t w15-aisec .
docker run --rm -it -v $(pwd):/workspace w15-aisec bash
python src/run_experiment.py --config configs/config.yaml
```

실험·점검 결과 표 형식:

```markdown
# 기말 논문 준비 점검 결과

| 점검 항목 | 상태 | 근거 파일 | 보완 필요 |
|---|---|---|---|
| 주차별 보고서 2개 이상 반영 |  |  |  |
| 참고문헌 DOI/URL 검증 |  |  |  |
| AI 활용 고지서 작성 |  |  |  |
| 실험 재현성 기록 |  |  |  |
| Contribution 문장 확정 |  |  |  |
| 표 1개 이상 준비 |  |  |  |
| 그림 1개 이상 준비 |  |  |  |
```

---

## 12. AI 활용기록 작성 지시

`05_ai_worklog/`에는 다음을 작성하라.

1. 사용한 AI 도구
2. 사용 목적
3. 주요 프롬프트
4. AI 출력물 요약
5. 본인 수정 내용
6. 사실관계 검증 방법
7. 참고문헌 검증 방법
8. 기말 논문 AI 활용 고지서로 옮길 내용

AI 활용 고지서 초안에는 다음 표를 넣어라.

```markdown
# AI 활용 고지서 초안

| 항목 | 작성 내용 |
|---|---|
| 사용한 AI 도구명 |  |
| 사용 일자 |  |
| 사용 목적 | 논문 요약 / 개념 설명 / 문장 교정 / 코드 점검 / 기타 |
| 주요 프롬프트 |  |
| AI 산출물 반영 위치 |  |
| 본인 수정 내용 |  |
| 사실관계 검증 방법 |  |
| 참고문헌 검증 방법 |  |
| 최종 책임 확인 | 본인은 최종 원고의 내용, 인용, 실험결과, 연구윤리 책임이 본인에게 있음을 확인합니다. |
```

---

## 13. 기말논문 연결 지시

`08_final_paper_bridge/final_paper_bridge.md`에는 다음을 작성하라.

```markdown
# W15 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | AI 보안 연구의 재현성·참고문헌 검증·AI 활용 고지를 통합한 연구윤리 체크리스트 연구 | AI 보안 논문 작성 프로세스 | 허위 인용·재현성 실패 | 체크리스트/프레임워크 | 높음 |
| 2 | LLM 평가에서 benchmark contamination과 재현성 위험 분석 | LLM 평가 시스템 | 평가 오염 | 문헌분석/평가체계 | 높음 |
| 3 | XAI 기반 AI 보안 평가에서 설명 안정성과 공격면 분석 연구 | XAI 시스템 | Explanation manipulation | 문헌분석/모의평가 | 보통 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | AI 보안 연구에서 재현성과 연구윤리의 중요성 |
| 관련연구 | LLM evaluation, ML lifecycle assurance, XAI survey |
| 연구문제 | 평가오염, 재현성, XAI 신뢰성 문제 |
| 연구방법 | 체크리스트 설계, 문헌분석, 주차별 보고서 반영 |
| 분석/실험 | 참고문헌 검증률, AI 활용 고지 완성도, 재현성 점검표 |
| 보안적 함의 | 무결성, 책임성, 안전성 관점 |
| 결론 | AI 보안 논문 작성·검증 프레임워크 제안 |
```

---

## 14. 최종 통합보고서 작성 지시

`06_report/final/integrated_report_final.md`에는 다음 목차로 작성하라.

```markdown
# W15 연구평가·재현성·설명가능성(XAI)·논문 구성 통합보고서

## 0. 메타정보

## 1. 한 문장 요약

## 2. AI 원리 70% 정리

## 3. 보안 이슈 30% 정리

## 4. 논문 5편 요약

## 5. 논문 5편 비교

## 6. Research Track

### 6.1 연구문제

### 6.2 위협모형

### 6.3 평가방법

### 6.4 재현성

### 6.5 한계와 오픈문제

## 7. 실습 요약

## 8. AI 활용 기록 요약

## 9. 토론 질문

## 10. 기말 논문 연결

## 11. 참고문헌 검증표

## 12. 자기 점검

## 13. 기말 논문 최종 Contribution 후보

### 후보 1

본 연구는 _______ 환경에서 _______ 위협을 분석하고, _______을 제안한다.

### 후보 2

본 연구는 기존 _______ 연구의 한계를 보완하기 위해 _______ 평가 기준을 제시한다.
```

---

## 15. 기말 논문 통합 추가 지시

이번 W15 보고서는 단독 주차 보고서로 끝내지 말고, 반드시 `04_final_paper/`와 연결하라.

다음 파일을 함께 점검하거나 보완하라.

```text
04_final_paper/01_planning/final_topic.md
04_final_paper/01_planning/research_question.md
04_final_paper/01_planning/contribution.md
04_final_paper/02_weekly_reflection/weekly_reflection_table.md
04_final_paper/03_related_work/literature_matrix.md
04_final_paper/05_draft/paper_draft.md
04_final_paper/06_appendices/ai_disclosure.md
04_final_paper/06_appendices/reference_verification.md
04_final_paper/07_final_submission/submit_checklist.md
```

---

## 제출용 보고서 작성 지시

`07_week_submission/wXX_submission_report.md`와 `07_week_submission/wXX_submission_report.html`을 작성하라. `wXX`는 해당 주차 번호로 바꾼다. 제출용 보고서는 통합보고서, 실험보고서, 발표용 보고서, AI 활용기록을 하나의 제출 문서로 압축한 산출물이다.

필수 내용:

1. 표지: 주차, 제목, 작성일, 문서 상태, 관련 산출물 위치
2. 초록과 키워드
3. AI 원리 70%와 보안 이슈 30% 요약
4. 논문 5편 요약과 DOI/URL 검증 상태
5. Research Track: 연구문제, 대상 시스템, 위협, 평가 지표, 재현성, 제외 범위
6. 실습/실험 실행 상태와 결과표
7. 발표용 보고서 위치
8. 기말논문 연결
9. AI 활용 고지
10. 제출 전 점검표

HTML은 Markdown 제출본과 같은 수치, DOI/URL 상태, AI 활용 고지, 한계 표현을 유지해야 한다. 실험 수치는 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 사용한다.

---

## 발표용 보고서 작성 지시

`09_presentation/presentation_report.md`에는 발표용 보고서를 작성하고, `presentation_report.html`도 함께 생성하라. 발표용 보고서는 통합보고서와 실험 산출물을 8-10분 발표 흐름으로 압축한 문서이며, 새 정량 결과를 임의로 주장하지 않는다.

필수 내용:

1. 발표 메타정보: 주차, 주제, 발표 시간, 핵심 메시지
2. 한 문장 요약과 발표 흐름
3. 논문 5편의 발표 역할
4. AI 원리 70%와 보안 이슈 30%의 발표용 설명
5. 실습/실험 실행 상태와 결과 근거
6. 기말논문 연결 지점
7. 예상 질문과 답변 3개 이상

기본 슬라이드 산출물:

- `presentation_slides.md`: 슬라이드 원본
- `presentation_slides.html`: 키보드로 넘길 수 있는 브라우저 발표용 슬라이드

기본 발표 보조 산출물:

- `speaker_notes.md`: 슬라이드별 발표자 대본
- `qna.md`: 예상 질문과 답변
- `one_page_handout.md`: 청중 배포용 1페이지 요약

실험 수치는 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 사용한다. 실행 전 주차는 발표에서도 `실행 전` 또는 `확인 필요`로 표시한다.

---

## 16. 작성 규칙

1. 논문 내용을 임의로 지어내지 않는다.
2. PDF 원문을 확인하지 못한 부분은 `원문 확인 필요`로 표시한다.
3. DOI는 임의 생성하지 않고 `확인 필요`로 둔다.
4. 실험 결과는 실제 실행 전까지 빈칸으로 두고, 실행 후에는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`를 생성한 뒤 실험보고서, 통합보고서, 제출 체크리스트, AI 활용기록을 함께 갱신한다.
5. 기말 논문 주제 후보를 최소 3개 제안한다.
6. AI 활용 내역은 `05_ai_worklog/`에 반드시 기록한다.
7. Markdown 파일은 UTF-8로 저장한다.
8. 파일명과 폴더명은 영문, 숫자, 언더바를 사용한다.
9. 보고서 본문은 한글로 작성한다.
10. 허위 DOI, 허위 참고문헌, 실험결과 조작, AI 사용 은폐를 방지하는 점검표를 포함한다.
11. W15는 기말 논문 작성 직전 점검 주차로 처리한다.
12. 최종 Contribution 문장을 반드시 1~2개로 압축한다.

---

## 17. 완료 후 출력 형식

작업 완료 후 다음 형식으로 보고하라.

```markdown
# W15 작성 완료 보고

## 1. 작성한 파일

## 2. 보완한 파일

## 3. 확인 필요 항목

## 4. 논문 원문 확인 필요 항목

## 5. 기말 논문으로 연결한 파일

## 6. 최종 Contribution 후보

## 7. 다음 작업 우선순위
```
