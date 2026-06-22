# W12_nn_verification_xai.md

## Codex 작업 지시서: Week 12 보고서 작성

## 1. 작업 대상

```text
03_weekly_reports/w12_nn_verification_xai/
```

## 2. 주차 정보

| 항목    | 내용                                                                         |
| ----- | -------------------------------------------------------------------------- |
| 주차    | W12                                                                        |
| 주제    | 신경망 검증·정형방법 & 대적방어·XAI·강건성 트레이드오프                                          |
| AI 원리 | Neural network verification, abstraction, formal methods, robustness proof |
| 보안 이슈 | 대적방어, XAI 공격면, robustness-accuracy-fairness trade-off                      |
| 논문 패킷 | 5편                                                                         |

---

## 3. 논문 패킷

1. Boudardara et al., "A Review of Abstraction Methods Toward Verifying Neural Networks", ACM Computing Surveys, 2024.
2. Sen Zhou et al., "Adversarial Attacks and Defenses in Deep Learning", ACM Computing Surveys, 2022.
3. G. Vadillo et al., "Adversarial machine learning attacks against explainable artificial intelligence: A review", WIREs Data Mining and Knowledge Discovery, 2025.
4. Inaki Pérez et al., "Adversarial Robustness of Neural Networks from Lipschitz Regularization: A Survey", ACM Computing Surveys, 2024.
5. Chih-Hsiang Cheng et al., "The Triangular Trade-off between Robustness, Accuracy, and Fairness", ACM Computing Surveys, 2024.

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
03_weekly_reports/w12_nn_verification_xai/
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
# W12 논문 5편 비교표

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

1. 신경망 검증의 기본 개념
2. 정형검증과 경험적 평가의 차이
3. Abstraction method
4. Reachability analysis
5. Lipschitz regularization
6. Robustness certificate
7. Verification scalability 문제
8. Robustness-accuracy-fairness trade-off
9. XAI의 기본 개념
10. XAI와 모델 신뢰성 평가의 관계

표 형식:

```markdown
# AI 원리 70% 정리

## 1. 핵심 이론

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 |
|---|---|---|---|
| Neural Network Verification |  |  | P01 |
| Abstraction |  |  | P01 |
| Formal Methods |  |  | P01 |
| Adversarial Robustness |  |  | P02, P04 |
| Lipschitz Regularization |  |  | P04 |
| XAI |  |  | P03 |
| Robustness-Accuracy-Fairness Trade-off |  |  | P05 |

## 3. 수식 또는 알고리즘

## 4. 초보자용 설명

## 5. 보안 연구와의 연결
```

---

## 9. 보안 이슈 30% 작성 지시

`03_theory_notes/security_issue_30.md`에는 다음 내용을 중심으로 정리하라.

1. 대적공격과 대적방어
2. Certified robustness
3. Empirical robustness와 formal robustness의 차이
4. XAI 공격
5. Explanation manipulation
6. Saliency map 조작
7. Robustness-accuracy trade-off
8. Robustness-fairness trade-off
9. 검증 가능성과 확장성 한계
10. Risk-based verification 필요성

표 형식:

```markdown
# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | Explanation leakage |  |
| Integrity | Adversarial attack / XAI manipulation |  |
| Availability | Verification scalability failure |  |
| Privacy | Explanation-based sensitive feature exposure |  |
| Safety | Unverified robust behavior |  |
| Accountability | Misleading explanation / unverifiable decision |  |
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

RQ1. 신경망 검증 기법은 대규모 딥러닝 모델에서 어떤 확장성 한계를 갖는가?

RQ2. XAI 기반 설명 결과는 대적공격 또는 입력 조작에 의해 얼마나 쉽게 왜곡될 수 있는가?

RQ3. Robustness, accuracy, fairness 간 trade-off를 보안 평가에서 어떻게 통합 지표로 보고해야 하는가?
```

### 10.2 위협모형 표

```markdown
# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | 딥러닝 분류 모델 / XAI 기반 설명 시스템 / 신경망 검증 파이프라인 |
| 보호 자산 | 모델 예측, 강건성 보증, 설명 결과, 공정성 지표, 안전 판단 |
| 공격자 | 입력 조작자 / 설명 조작자 / 평가 회피자 |
| 공격자의 지식 | White-box / Gray-box / Black-box |
| 공격자의 능력 | adversarial input 생성, explanation manipulation, 평가 데이터 조작 |
| 공격 경로 | 입력 데이터, 설명 모듈, 검증 설정, 평가 프로토콜 |
| 공격 성공 조건 | 예측 또는 설명이 왜곡되지만 방어자에게 탐지되지 않음 |
| 방어자 가정 | robust evaluation, XAI 검토, 검증 로그, 모델 재현 가능 |
| 제외 범위 | 실제 안전중요 시스템 공격, 실제 운영 모델 침해 |
```

### 10.3 평가방법 표

```markdown
# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Clean Accuracy | Accuracy | 정상 테스트셋 평가 | Clean test data | 기본 성능 |
| Robust Accuracy | Robust Acc. | 공격 조건에서 정확도 측정 | Adversarial data | 강건성 |
| Certified Robustness | Certified radius / bound | 검증 도구 또는 이론적 bound 측정 | Model/specification | 증명 가능성 |
| Explanation Stability | Explanation similarity | 입력 변조 전후 설명 비교 | Explanation maps | XAI 안정성 |
| Fairness Impact | Group metric gap | 집단별 성능 차이 측정 | Group-labeled data | 공정성 |
| Verification Cost | Runtime / memory | 검증 실행 비용 측정 | Verification logs | 확장성 |
| Reproducibility | Seed/run log | 반복 실행 비교 | Config/logs | 재현성 |
```

---

## 11. 실습 방향

`04_experiment/experiment_report.md`에는 신경망 강건성·XAI 안정성 평가 중심의 안전한 모의 실습을 설계하라.

실습 목표:

1. 간단한 이미지 분류 모델 또는 scikit-learn 기반 분류 모델 준비
2. Clean accuracy와 robust accuracy 비교 설계
3. Saliency map 또는 feature importance 변화 분석 계획 작성
4. 공격 전후 설명 결과의 안정성 비교
5. Verification cost 또는 scalability 한계 정리
6. 결과는 실제 실행 전까지 빈칸으로 두고, 실행 후에는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`를 생성한 뒤 실험보고서, 통합보고서, 제출 체크리스트, AI 활용기록을 함께 갱신한다.

실습 환경:

```text
OS: Ubuntu 24.04
Container: Docker
Python: 3.11 (python:3.11-slim)
Package manager: uv (Dockerfile 내부 포함, WSL 호스트 설치 금지)
Install: 컨테이너 내부 uv sync
Dataset: scikit-learn digits 또는 공개 이미지 데이터
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
docker build -t w12-aisec .
docker run --rm -it -v $(pwd):/workspace w12-aisec bash
python src/run_experiment.py --config configs/config.yaml
```

실험 결과 표 형식:

```markdown
# 실험 결과

| 조건 | Clean Accuracy | Robust Accuracy | Explanation Stability | Verification Cost | 해석 |
|---|---:|---:|---:|---:|---|
| Clean model |  |  |  |  |  |
| Adversarial input |  |  |  |  |  |
| Robust defense |  |  |  |  |  |
| XAI stability check |  |  |  |  |  |
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
# W12 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 신경망 강건성 평가에서 robustness-accuracy-fairness trade-off 분석 | 딥러닝 모델 | 대적공격 | 문헌분석/평가체계 | 높음 |
| 2 | XAI 기반 설명 결과의 대적공격 취약성 평가 연구 | XAI 시스템 | Explanation manipulation | 모의실험/사례분석 | 높음 |
| 3 | 대규모 AI 모델의 위험기반 부분검증 프레임워크 연구 | AI 검증 시스템 | 검증 한계 / 안전성 위험 | 프레임워크 설계 | 높음 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | AI 모델 강건성과 설명가능성 검증의 필요성 |
| 관련연구 | 신경망 검증, 대적방어, XAI 공격, trade-off survey |
| 연구문제 | 강건성·정확도·공정성·설명안정성 통합 평가 |
| 연구방법 | 문헌분석, 모의실험, 체크리스트 설계 |
| 분석/실험 | robust accuracy, explanation stability, verification cost 비교 |
| 보안적 함의 | 무결성, 안전성, 책임성 관점 |
| 결론 | 위험기반 AI 검증·XAI 보안 평가체계 제안 |
```

---

## 14. 최종 통합보고서 작성 지시

`06_report/final/integrated_report_final.md`에는 다음 목차로 작성하라.

```markdown
# W12 신경망 검증·정형방법 & 대적방어·XAI·강건성 트레이드오프 통합보고서

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
10. 실제 안전중요 시스템 공격이나 운영 모델 침해 절차는 작성하지 않는다.
11. 검증·강건성·XAI 실습은 공개 데이터 또는 toy model 기반으로 제한한다.

---

## 16. 완료 후 출력 형식

작업 완료 후 다음 형식으로 보고하라.

```markdown
# W12 작성 완료 보고

## 1. 작성한 파일

## 2. 보완한 파일

## 3. 확인 필요 항목

## 4. 논문 원문 확인 필요 항목

## 5. 다음 작업 우선순위
```
