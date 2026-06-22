# W11_differential_privacy_mi.md

## Codex 작업 지시서: Week 11 보고서 작성

## 1. 작업 대상

```text
03_weekly_reports/w11_differential_privacy_mi/
```

## 2. 주차 정보

| 항목    | 내용                                                               |
| ----- | ---------------------------------------------------------------- |
| 주차    | W11                                                              |
| 주제    | 차등프라이버시(DP) & 멤버십 추론 공격·방어                                       |
| AI 원리 | Differential Privacy, privacy budget, DP-SGD, privacy accounting |
| 보안 이슈 | Membership inference, privacy leakage, utility trade-off         |
| 논문 패킷 | 5편                                                               |

---

## 3. 논문 패킷

1. Alberto Blanco-Justicia et al., "A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning", ACM Computing Surveys, 2022.
2. Jonathan Demelius et al., "Differential Privacy in Centralized Deep Learning: A Survey", ACM Computing Surveys, 2025.
3. Zizheng Pan et al., "Differential Privacy in Deep Learning: A Literature Survey", Neurocomputing, 2024.
4. Hongsheng Hu et al., "Membership inference attacks on machine learning: a survey", ACM Computing Surveys, 2022.
5. Hongsheng Hu et al., "Defenses to Membership Inference Attacks: A Survey", ACM Computing Surveys, 2023.

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
03_weekly_reports/w11_differential_privacy_mi/
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
# W11 논문 5편 비교표

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

1. 차등프라이버시의 기본 정의
2. Privacy budget, epsilon, delta
3. Local DP와 central DP의 차이
4. DP-SGD의 기본 구조
5. Gradient clipping과 noise injection
6. Privacy accounting
7. Utility-privacy trade-off
8. Deep learning에서 DP 적용의 어려움
9. FL, LLM 환경에서 DP 적용 한계
10. DP 오용과 잘못된 해석 사례

표 형식:

```markdown
# AI 원리 70% 정리

## 1. 핵심 이론

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 |
|---|---|---|---|
| Differential Privacy |  |  | P01, P02, P03 |
| Privacy Budget |  |  | P01, P02 |
| Epsilon |  |  | P01, P03 |
| Delta |  |  | P02, P03 |
| DP-SGD |  |  | P02, P03 |
| Privacy Accounting |  |  | P02 |
| Utility-Privacy Trade-off |  |  | P01, P03 |

## 3. 수식 또는 알고리즘

## 4. 초보자용 설명

## 5. 보안 연구와의 연결
```

---

## 9. 보안 이슈 30% 작성 지시

`03_theory_notes/security_issue_30.md`에는 다음 내용을 중심으로 정리하라.

1. Membership inference attack
2. Training data leakage
3. Model memorization
4. Overfitting과 privacy leakage의 관계
5. Shadow model 기반 MI 공격 개념
6. Confidence score 기반 MI 공격 개념
7. DP 기반 방어
8. Regularization, calibration, output restriction 방어
9. DP 적용 시 accuracy 저하
10. LLM/FL 환경에서 MI 방어 한계

표 형식:

```markdown
# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | Membership inference / training data leakage |  |
| Integrity | Privacy mechanism misuse |  |
| Availability | Utility degradation from excessive noise |  |
| Privacy | Individual record exposure |  |
| Safety | Incorrect privacy guarantee interpretation |  |
| Accountability | Unverified DP claim / missing privacy accounting |  |
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

RQ1. DP-SGD의 privacy budget 변화는 모델 정확도와 membership inference 방어 효과에 어떤 trade-off를 만드는가?

RQ2. Membership inference 공격은 모델의 overfitting, confidence score, 학습 데이터 특성에 따라 어떻게 달라지는가?

RQ3. AI 보안 연구에서 DP를 주장할 때 privacy accounting, utility, attack evaluation을 어떻게 함께 보고해야 하는가?
```

### 10.2 위협모형 표

```markdown
# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | 개인정보가 포함될 수 있는 ML/DL 학습 시스템 |
| 보호 자산 | 학습 데이터 포함 여부, 개인 레코드, 모델 출력, confidence score |
| 공격자 | 외부 질의자 / 모델 사용자 / API 접근자 / 내부 평가자 |
| 공격자의 지식 | White-box / Gray-box / Black-box |
| 공격자의 능력 | 모델 질의, confidence score 관찰, shadow model 학습, 출력 비교 |
| 공격 경로 | 모델 API, 예측 확률, 학습 결과, 평가 로그 |
| 공격 성공 조건 | 특정 데이터가 학습에 사용되었는지 추론 |
| 방어자 가정 | DP-SGD 적용, output restriction, calibration, privacy accounting 가능 |
| 제외 범위 | 실제 개인정보 데이터 사용, 실제 개인 대상 추론, 불법적 데이터 수집 |
```

### 10.3 평가방법 표

```markdown
# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Model Utility | Accuracy / F1 | 정상 테스트셋 평가 | Clean train/test data | 기본 성능 |
| Privacy Budget | epsilon / delta | privacy accounting으로 계산 | Training config | DP 보장 |
| Membership Inference Risk | MI attack accuracy | member/non-member 구분 성능 | Shadow/evaluation data | 프라이버시 위험 |
| Privacy Leakage | Leakage score | confidence gap 또는 MI 성공률 측정 | Model outputs | 정보노출 |
| Utility Drop | Accuracy drop | DP 적용 전후 성능 비교 | Baseline/DP model | 효용 손실 |
| Stability | Variance across seeds | 반복 실행 결과 비교 | Multiple runs | 안정성 |
| Reproducibility | Seed/run log | 반복 실행 비교 | Config/logs | 재현성 |
```

---

## 11. 실습 방향

`04_experiment/experiment_report.md`에는 DP와 MI 공격 평가 중심의 안전한 모의 실습을 설계하라.

실습 목표:

1. 공개 데이터 또는 synthetic data 기반 baseline 모델 학습
2. Overfitting 정도에 따른 MI 위험 개념 설명
3. DP-like noise 또는 regularization 적용 전후 비교 설계
4. Privacy budget과 accuracy trade-off 표 작성
5. 실제 개인정보 데이터는 사용하지 않는다.
6. 결과는 실제 실행 전까지 빈칸으로 두고, 실행 후에는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`를 생성한 뒤 실험보고서, 통합보고서, 제출 체크리스트, AI 활용기록을 함께 갱신한다.

실습 환경:

```text
OS: Ubuntu 24.04
Container: Docker
Python: 3.11 (python:3.11-slim)
Package manager: uv (Dockerfile 내부 포함, WSL 호스트 설치 금지)
Install: 컨테이너 내부 uv sync
Dataset: scikit-learn digits 또는 synthetic data
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
docker build -t w11-aisec .
docker run --rm -it -v $(pwd):/workspace w11-aisec bash
python src/run_experiment.py --config configs/config.yaml
```

실험 결과 표 형식:

```markdown
# 실험 결과

| 조건 | Accuracy | MI Attack Accuracy | Epsilon | Utility Drop | 해석 |
|---|---:|---:|---:|---:|---|
| Non-DP baseline |  |  |  |  |  |
| DP-like noise low |  |  |  |  |  |
| DP-like noise medium |  |  |  |  |  |
| DP-like noise high |  |  |  |  |  |
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
# W11 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 차등프라이버시 기반 AI 학습에서 privacy budget과 정확도 간 상충관계 분석 | ML 학습 시스템 | Privacy leakage | 모의실험/평가체계 | 높음 |
| 2 | 멤버십 추론 공격 관점에서 AI 모델 프라이버시 위험 분석 | ML/DL 모델 | Membership inference | 문헌분석/모의실험 | 높음 |
| 3 | DP-SGD 적용 모델의 utility-privacy trade-off 평가 프레임워크 연구 | DP 학습 모델 | 프라이버시 누출 | 프레임워크 설계 | 높음 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | AI 모델 학습에서 개인정보 보호와 성능 간 상충관계 |
| 관련연구 | DP misuse, centralized DP deep learning, MI attack/defense survey |
| 연구문제 | privacy budget, utility, MI risk의 관계 |
| 연구방법 | synthetic data 기반 DP-like noise 실험 또는 문헌기반 평가체계 |
| 분석/실험 | Accuracy, MI attack accuracy, epsilon, utility drop 비교 |
| 보안적 함의 | 기밀성, 프라이버시, 책임성 관점 |
| 결론 | DP 기반 AI 보안 평가체계 제안 |
```

---

## 14. 최종 통합보고서 작성 지시

`06_report/final/integrated_report_final.md`에는 다음 목차로 작성하라.

```markdown
# W11 차등프라이버시(DP) & 멤버십 추론 공격·방어 통합보고서

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
10. 실제 개인정보 데이터는 사용하지 않는다.
11. 실제 개인의 학습 포함 여부를 추론하는 공격 절차는 작성하지 않는다.
12. MI 공격은 synthetic data 또는 공개 데이터 기반의 안전한 평가 개념으로만 다룬다.

---

## 16. 완료 후 출력 형식

작업 완료 후 다음 형식으로 보고하라.

```markdown
# W11 작성 완료 보고

## 1. 작성한 파일

## 2. 보완한 파일

## 3. 확인 필요 항목

## 4. 논문 원문 확인 필요 항목

## 5. 다음 작업 우선순위
```
