# W09_drl_cybersecurity.md

## Codex 작업 지시서: Week 09 보고서 작성

## 1. 작업 대상

```text
03_weekly_reports/w09_drl_cybersecurity/
```

## 2. 주차 정보

| 항목    | 내용                                                 |
| ----- | -------------------------------------------------- |
| 주차    | W09                                                |
| 주제    | 심층강화학습(DRL) & 사이버보안 적용·보상조작                        |
| AI 원리 | DQN, Policy Gradient, Actor-Critic, DRL 검증         |
| 보안 이슈 | DRL for cyber defense, reward manipulation, 모델 취약성 |
| 논문 패킷 | 5편                                                 |

---

## 3. 논문 패킷

1. Kai Arulkumaran et al., "Deep Reinforcement Learning: A Brief Survey", IEEE Signal Processing Magazine, 2017.
2. B. R. Kiran et al., "Deep Reinforcement Learning for Autonomous Driving: A Survey", IEEE TITS, 2022.
3. Ngoc-Tinh Nguyen et al., "Deep Reinforcement Learning for Cyber Security", IEEE TNNLS, 2023.
4. Aditya Adawadkar et al., "Cyber-security and reinforcement learning — A brief survey", Engineering Applications of Artificial Intelligence, 2022.
5. H. Yan et al., "Deep Reinforcement Learning Verification: A Survey", ACM Computing Surveys, 2023.

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

---

## 5. 작성할 파일

아래 파일을 작성하거나 보완하라.

```text
03_weekly_reports/w09_drl_cybersecurity/
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
# W09 논문 5편 비교표

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

1. 강화학습의 기본 구조
2. Agent, Environment, State, Action, Reward
3. Markov Decision Process
4. Value function과 Q-function
5. DQN
6. Policy Gradient
7. Actor-Critic
8. Exploration과 Exploitation
9. DRL 검증과 안전성 문제
10. 사이버보안 환경에서 상태·행동·보상 설계의 어려움

표 형식:

```markdown
# AI 원리 70% 정리

## 1. 핵심 이론

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 |
|---|---|---|---|
| Reinforcement Learning |  |  | P01 |
| Agent |  |  | P01 |
| Environment |  |  | P01 |
| State |  |  | P01, P03 |
| Action |  |  | P01, P03 |
| Reward |  |  | P01, P03 |
| DQN |  |  | P01 |
| Policy Gradient |  |  | P01 |
| Actor-Critic |  |  | P01 |
| DRL Verification |  |  | P05 |

## 3. 수식 또는 알고리즘

## 4. 초보자용 설명

## 5. 보안 연구와의 연결
```

---

## 9. 보안 이슈 30% 작성 지시

`03_theory_notes/security_issue_30.md`에는 다음 내용을 중심으로 정리하라.

1. DRL for cyber defense
2. 침입탐지와 자동 대응
3. 보상 설계 오류
4. Reward manipulation
5. Reward hacking
6. 환경 모델링 오류
7. 공격자가 상태 관측을 조작하는 경우
8. 방어 에이전트의 오탐·미탐 문제
9. DRL 정책 검증의 어려움
10. 안전한 자동화 대응의 필요성

표 형식:

```markdown
# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | State observation leakage |  |
| Integrity | Reward manipulation / state poisoning |  |
| Availability | Wrong automated response |  |
| Privacy | Security log exposure |  |
| Safety | Unsafe autonomous defense action |  |
| Accountability | Unexplainable DRL policy decision |  |
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

RQ1. 사이버보안 환경에서 DRL 에이전트의 상태·행동·보상 설계는 방어 성능과 안전성에 어떤 영향을 미치는가?

RQ2. Reward manipulation은 DRL 기반 사이버 방어 에이전트의 정책을 어떻게 왜곡할 수 있는가?

RQ3. DRL 기반 사이버 방어 시스템의 검증에는 탐지율, 오탐률, 보상 안정성, 안전성 지표를 어떻게 결합해야 하는가?
```

### 10.2 위협모형 표

```markdown
# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | DRL 기반 사이버 방어 에이전트 / 자동 대응 시스템 |
| 보호 자산 | 상태 관측값, 보상함수, 정책, 보안 로그, 대응 액션 |
| 공격자 | 외부 공격자 / 내부자 / 환경 조작자 |
| 공격자의 지식 | White-box / Gray-box / Black-box |
| 공격자의 능력 | 상태 관측 조작, 보상 신호 왜곡, 환경 이벤트 조작, 로그 오염 |
| 공격 경로 | 보안 로그, 상태 입력, 보상 계산, 정책 업데이트, 자동 대응 액션 |
| 공격 성공 조건 | 방어 에이전트가 잘못된 정책을 학습하거나 부적절한 대응 수행 |
| 방어자 가정 | 로그 검증, 정책 평가, 시뮬레이션 환경, human override 가능 |
| 제외 범위 | 실제 네트워크 공격 자동화, 실제 시스템 침해, 무단 스캔 |
```

### 10.3 평가방법 표

```markdown
# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Detection Performance | Precision / Recall / F1 | 탐지 결과 평가 | Security event data | 방어 성능 |
| False Positive Rate | FPR | 정상 이벤트 오탐 비율 | Normal events | 운영 위험 |
| False Negative Rate | FNR | 공격 이벤트 미탐 비율 | Attack events | 보안 위험 |
| Reward Stability | Reward variance | 에피소드별 보상 변동 측정 | Training logs | 학습 안정성 |
| Policy Robustness | Robust return | 조작 환경에서 성능 측정 | Perturbed environment | 강건성 |
| Safety Violation Rate | Violation rate | 위험 액션 발생 비율 측정 | Action logs | 안전성 |
| Reproducibility | Seed/run log | 반복 실행 비교 | Config/logs | 재현성 |
```

---

## 11. 실습 방향

`04_experiment/experiment_report.md`에는 DRL 사이버보안 모의 실습을 설계하라.

실습 목표:

1. 간단한 grid-world 또는 toy cyber-defense 환경 정의
2. 상태, 행동, 보상 표 작성
3. 정상 보상과 조작된 보상 비교
4. Reward manipulation이 정책에 미치는 영향 설명
5. 실제 공격 자동화가 아니라 안전한 시뮬레이션으로 제한
6. 결과는 실제 실행 전까지 빈칸으로 두고, 실행 후에는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`를 생성한 뒤 실험보고서, 통합보고서, 제출 체크리스트, AI 활용기록을 함께 갱신한다.

실습 환경:

```text
OS: Ubuntu 24.04
Container: Docker
Python: 3.11 (python:3.11-slim)
Package manager: uv (Dockerfile 내부 포함, WSL 호스트 설치 금지)
Install: 컨테이너 내부 uv sync
Environment: toy grid-world 또는 synthetic cyber-defense environment
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
docker build -t w09-aisec .
docker run --rm -it -v $(pwd):/workspace w09-aisec bash
python src/run_experiment.py --config configs/config.yaml
```

실험 결과 표 형식:

```markdown
# 실험 결과

| 조건 | Average Reward | Detection F1 | Safety Violation Rate | 해석 |
|---|---:|---:|---:|---|
| Normal reward |  |  |  |  |
| Manipulated reward |  |  |  |  |
| Robust reward design |  |  |  |  |
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
# W09 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | DRL 기반 사이버 방어 시스템의 보상조작 위협모형 연구 | DRL cyber defense | Reward manipulation | 위협모형/평가체계 | 높음 |
| 2 | 사이버보안 DRL 에이전트의 상태·행동·보상 설계 기준 연구 | DRL agent | 상태 조작·보상 왜곡 | 프레임워크 설계 | 높음 |
| 3 | 자동화된 AI 보안 대응 시스템의 안전성 평가 체크리스트 연구 | Autonomous defense | Unsafe action | 체크리스트/사례분석 | 보통 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | AI 기반 자동 방어 시스템의 필요성과 위험 |
| 관련연구 | DRL survey, cyber security RL survey, DRL verification |
| 연구문제 | reward manipulation과 safe cyber-defense policy |
| 연구방법 | toy environment 기반 위협모형 및 평가설계 |
| 분석/실험 | reward stability, safety violation, detection score 비교 |
| 보안적 함의 | 무결성, 가용성, 안전성, 책임성 관점 |
| 결론 | 안전한 DRL 보안 에이전트 평가체계 제안 |
```

---

## 14. 최종 통합보고서 작성 지시

`06_report/final/integrated_report_final.md`에는 다음 목차로 작성하라.

```markdown
# W09 심층강화학습(DRL) & 사이버보안 적용·보상조작 통합보고서

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

## 15. 작성 규칙

1. 논문 내용을 임의로 지어내지 않는다.
2. PDF 원문을 확인하지 못한 부분은 `원문 확인 필요`로 표시한다.
3. DOI는 임의 생성하지 않고 `확인 필요`로 둔다.
4. 실험 결과는 실제 실행 전까지 빈칸으로 두고, 실행 후에는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`를 생성한 뒤 실험보고서, 통합보고서, 제출 체크리스트, AI 활용기록을 함께 갱신한다.
5. 기말 논문 주제 후보를 최소 3개 제안한다.
6. AI 활용 내역은 `05_ai_worklog/`에 반드시 기록한다.
7. Markdown 파일은 UTF-8로 저장한다.
8. 파일명과 폴더명은 영문, 숫자, 언더바를 사용한다.
9. 보고서 본문은 한글로 작성한다.
10. 실제 공격 자동화 코드, 실제 네트워크 공격, 무단 스캔 절차는 작성하지 않는다.
11. DRL 실습은 안전한 toy environment 또는 synthetic cyber-defense environment로 제한한다.

---

## 16. 완료 후 출력 형식

작업 완료 후 다음 형식으로 보고하라.

```markdown
# W09 작성 완료 보고

## 1. 작성한 파일

## 2. 보완한 파일

## 3. 확인 필요 항목

## 4. 논문 원문 확인 필요 항목

## 5. 다음 작업 우선순위
```
