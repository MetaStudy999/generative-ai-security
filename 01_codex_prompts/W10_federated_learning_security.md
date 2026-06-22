# W10_federated_learning_security.md

## Codex 작업 지시서: Week 10 보고서 작성

## 1. 작업 대상

```text
03_weekly_reports/w10_federated_learning_security/
```

## 2. 주차 정보

| 항목    | 내용                                                           |
| ----- | ------------------------------------------------------------ |
| 주차    | W10                                                          |
| 주제    | 연합학습(FL) & FL 위협·방어·정책                                       |
| AI 원리 | Federated Learning, aggregation, personalization, robustness |
| 보안 이슈 | Gradient leakage, poisoning, backdoor, privacy attack        |
| 논문 패킷 | 5편                                                           |

---

## 3. 논문 패킷

1. M. Arbaoui et al., "Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights and Future Frontiers", ACM Computing Surveys, 2024.
2. Viraaji Mothukuri et al., "A survey on security and privacy of federated learning", Future Generation Computer Systems, 2021.
3. Nuria Rodríguez-Barroso et al., "Survey on federated learning threats: Concepts, taxonomy on attacks and defences, experimental study and challenges", Information Fusion, 2023.
4. J. Zhao et al., "A Survey of Federated Learning Privacy Attacks, Defenses, Applications, and Policy Landscape", ACM Computing Surveys, 2025.
5. T. D. Nguyen et al., "Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions", Engineering Applications of Artificial Intelligence, 2024.

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
03_weekly_reports/w10_federated_learning_security/
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
# W10 논문 5편 비교표

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

1. 연합학습의 기본 구조
2. Client, server, aggregation의 역할
3. FedAvg의 기본 원리
4. Aggregation technique taxonomy
5. Personalized federated learning
6. Non-IID data 문제
7. Communication cost와 computation cost
8. Robust aggregation
9. FL에서 privacy와 utility의 trade-off
10. 중앙집중 학습과 연합학습의 차이

표 형식:

```markdown
# AI 원리 70% 정리

## 1. 핵심 이론

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 |
|---|---|---|---|
| Federated Learning |  |  | P01, P02 |
| Client |  |  | P01 |
| Server |  |  | P01 |
| Aggregation |  |  | P01 |
| FedAvg |  |  | P01 |
| Personalized FL |  |  | P01 |
| Non-IID Data |  |  | P01, P03 |
| Robust Aggregation |  |  | P03, P05 |

## 3. 수식 또는 알고리즘

## 4. 초보자용 설명

## 5. 보안 연구와의 연결
```

---

## 9. 보안 이슈 30% 작성 지시

`03_theory_notes/security_issue_30.md`에는 다음 내용을 중심으로 정리하라.

1. Gradient leakage
2. Membership inference in FL
3. Poisoning attack
4. Model poisoning
5. Backdoor attack in FL
6. Malicious client
7. Byzantine client
8. Secure aggregation
9. Robust aggregation defense
10. FL privacy policy landscape

표 형식:

```markdown
# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | Gradient leakage / privacy attack |  |
| Integrity | Model poisoning / backdoor |  |
| Availability | Byzantine client / training disruption |  |
| Privacy | Membership inference / client data leakage |  |
| Safety | Compromised global model behavior |  |
| Accountability | Malicious client attribution failure |  |
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

RQ1. 연합학습 환경에서 malicious client 비율은 global model의 성능과 backdoor 공격 성공률에 어떤 영향을 미치는가?

RQ2. Secure aggregation과 robust aggregation은 gradient leakage, poisoning, backdoor 위험을 각각 어느 정도 완화할 수 있는가?

RQ3. FL 보안 평가에는 privacy leakage, robustness, utility, communication cost를 어떻게 결합해야 하는가?
```

### 10.2 위협모형 표

```markdown
# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | 연합학습 기반 분산 AI 학습 시스템 |
| 보호 자산 | 클라이언트 데이터, 로컬 모델 업데이트, 글로벌 모델, 집계 결과 |
| 공격자 | 악성 클라이언트 / 내부자 / 서버 관찰자 / 외부 질의자 |
| 공격자의 지식 | White-box / Gray-box / Black-box |
| 공격자의 능력 | 로컬 업데이트 조작, poisoned update 제출, backdoor trigger 삽입, gradient 관찰 |
| 공격 경로 | 클라이언트 업데이트, 서버 집계, 통신 채널, 글로벌 모델 배포 |
| 공격 성공 조건 | 글로벌 모델 성능 저하, backdoor 삽입, 클라이언트 데이터 추론 |
| 방어자 가정 | client sampling, update validation, secure aggregation, robust aggregation 가능 |
| 제외 범위 | 실제 개인정보 데이터 사용, 실제 분산 시스템 침해, 무단 클라이언트 접속 |
```

### 10.3 평가방법 표

```markdown
# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Global Utility | Accuracy / F1 | 글로벌 모델 성능 평가 | Clean test data | 기본 성능 |
| Poisoning Impact | Accuracy drop | 악성 클라이언트 비율별 성능 비교 | Poisoned updates | 무결성 |
| Backdoor Success | ASR | trigger 조건부 오분류율 측정 | Triggered test data | backdoor 효과 |
| Privacy Leakage | Leakage score | gradient leakage 또는 MI 위험 평가 | Simulated client updates | 프라이버시 |
| Robustness | Robust accuracy | robust aggregation 적용 전후 비교 | Clean/poisoned updates | 방어 효과 |
| Communication Cost | Rounds / bytes | 통신 라운드와 전송량 측정 | Training logs | 운영 비용 |
| Reproducibility | Seed/run log | 반복 실행 비교 | Config/logs | 재현성 |
```

---

## 11. 실습 방향

`04_experiment/experiment_report.md`에는 연합학습 보안 모의 실습을 설계하라.

실습 목표:

1. 간단한 FL 구조도 작성
2. Client-server-aggregation 흐름 정리
3. malicious client 비율에 따른 위험 설계
4. poisoning 또는 backdoor update 개념 설명
5. secure aggregation과 robust aggregation 차이 비교
6. 실제 개인정보 데이터는 사용하지 않는다.
7. 결과는 실제 실행 전까지 빈칸으로 두고, 실행 후에는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`를 생성한 뒤 실험보고서, 통합보고서, 제출 체크리스트, AI 활용기록을 함께 갱신한다.

실습 환경:

```text
OS: Ubuntu 24.04
Container: Docker
Python: 3.11 (python:3.11-slim)
Package manager: uv (Dockerfile 내부 포함, WSL 호스트 설치 금지)
Install: 컨테이너 내부 uv sync
Dataset: scikit-learn digits 또는 synthetic data
FL Framework: 직접 구현 / Flower / 확인 필요
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
docker build -t w10-aisec .
docker run --rm -it -v $(pwd):/workspace w10-aisec bash
python src/run_experiment.py --config configs/config.yaml
```

실험 결과 표 형식:

```markdown
# 실험 결과

| 조건 | Malicious Client Rate | Global Accuracy | ASR | Privacy Leakage | 해석 |
|---|---:|---:|---:|---:|---|
| Clean FL | 0% |  |  |  |  |
| Poisoned FL | 10% |  |  |  |  |
| Poisoned FL | 20% |  |  |  |  |
| Robust aggregation | 20% |  |  |  |  |
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
# W10 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 연합학습 환경에서 malicious client 비율에 따른 poisoning 위험 분석 | FL 시스템 | Model poisoning | 모의실험/평가체계 | 높음 |
| 2 | 연합학습 보안 평가를 위한 privacy-robustness-utility 통합 지표 연구 | FL 시스템 | Gradient leakage / Backdoor | 프레임워크 설계 | 높음 |
| 3 | 연합학습 환경의 backdoor 공격과 robust aggregation 방어 비교 연구 | FL 모델 | Backdoor | 문헌분석/모의실험 | 높음 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | 분산 AI 학습과 데이터 프라이버시 요구 증가 |
| 관련연구 | FL taxonomy, FL security/privacy, poisoning/backdoor survey |
| 연구문제 | malicious client와 FL 보안 평가 |
| 연구방법 | synthetic FL 실험 또는 문헌기반 평가체계 |
| 분석/실험 | malicious client rate, global accuracy, ASR 비교 |
| 보안적 함의 | 기밀성, 무결성, 프라이버시, 책임성 관점 |
| 결론 | FL 보안 평가 프레임워크 제안 |
```

---

## 14. 최종 통합보고서 작성 지시

`06_report/final/integrated_report_final.md`에는 다음 목차로 작성하라.

```markdown
# W10 연합학습(FL) & FL 위협·방어·정책 통합보고서

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
11. 실제 분산 시스템 침해, 무단 클라이언트 접속, 실제 FL 서비스 공격 절차는 작성하지 않는다.
12. 실습은 synthetic data 또는 공개 데이터 기반 모의 환경으로 제한한다.

---

## 16. 완료 후 출력 형식

작업 완료 후 다음 형식으로 보고하라.

```markdown
# W10 작성 완료 보고

## 1. 작성한 파일

## 2. 보완한 파일

## 3. 확인 필요 항목

## 4. 논문 원문 확인 필요 항목

## 5. 다음 작업 우선순위
```
