# W14_mlops_supply_chain.md

## Codex 작업 지시서: Week 14 보고서 작성

## 1. 작업 대상

```text
03_weekly_reports/w14_mlops_supply_chain/
```

## 2. 주차 정보

| 항목    | 내용                                                        |
| ----- | --------------------------------------------------------- |
| 주차    | W14                                                       |
| 주제    | MLOps/DevOps·데이터/모델 파이프라인·공급망 보안                          |
| AI 원리 | MLOps, DevOps, data/model pipeline, monitoring, drift     |
| 보안 이슈 | ML supply chain, deployment/update/logging attack surface |
| 논문 패킷 | 5편                                                        |

---

## 3. 논문 패킷

1. Bayram Eken et al., "A Multivocal Literature Review of MLOps Practices: Emerging Trends, Challenges, and Research Directions", ACM Computing Surveys, 2025.
2. Andrei Paleyes et al., "Challenges in Deploying Machine Learning: A Survey of Case Studies", ACM Computing Surveys, 2022.
3. Daniel Diaz-de-Arcaya et al., "A Systematic Survey on MLOps and AIOps: Taxonomy, Challenges, and Future Directions", ACM Computing Surveys, 2023.
4. J. Chen et al., "Deep Learning with Edge Computing: A Review", Proceedings of the IEEE, 2019.
5. Xiang Chen et al., "Deep Learning for Software Engineering: A Survey", ACM Computing Surveys, 2022.

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
03_weekly_reports/w14_mlops_supply_chain/
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
# W14 논문 5편 비교표

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

1. MLOps의 기본 개념
2. DevOps와 MLOps의 차이
3. ML lifecycle
4. 데이터 파이프라인
5. 모델 학습 파이프라인
6. 모델 배포와 서빙
7. 모니터링과 drift detection
8. AIOps의 개념
9. Edge AI와 edge deployment
10. 연구용 실험과 운영용 ML 시스템의 차이
11. Software engineering for deep learning

표 형식:

```markdown
# AI 원리 70% 정리

## 1. 핵심 이론

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 |
|---|---|---|---|
| MLOps |  |  | P01, P03 |
| DevOps |  |  | P01, P03 |
| ML Lifecycle |  |  | P01, P02 |
| Data Pipeline |  |  | P01, P02 |
| Model Pipeline |  |  | P01, P03 |
| Drift Monitoring |  |  | P01, P03 |
| AIOps |  |  | P03 |
| Edge AI |  |  | P04 |
| Deep Learning for Software Engineering |  |  | P05 |

## 3. 수식 또는 알고리즘

## 4. 초보자용 설명

## 5. 보안 연구와의 연결
```

---

## 9. 보안 이슈 30% 작성 지시

`03_theory_notes/security_issue_30.md`에는 다음 내용을 중심으로 정리하라.

1. ML supply chain risk
2. 데이터 파이프라인 오염
3. 모델 아티팩트 변조
4. 의존성 패키지 취약점
5. 모델 배포 취약점
6. 로그와 모니터링 데이터 노출
7. Drift detection 실패
8. 모델 업데이트 공격면
9. CI/CD pipeline 보안
10. Assurance case
11. 운영환경과 연구환경의 보안 격차

표 형식:

```markdown
# 보안 이슈 30% 정리

## 1. 주요 보안 이슈

## 2. CIA 관점 분석

| 관점 | 관련 위협 | 설명 |
|---|---|---|
| Confidentiality | Log leakage / model artifact exposure |  |
| Integrity | Data pipeline poisoning / model artifact tampering |  |
| Availability | Deployment failure / pipeline disruption |  |
| Privacy | Monitoring data leakage |  |
| Safety | Unsafe model update / drift undetected |  |
| Accountability | Missing audit trail / weak assurance case |  |
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

RQ1. MLOps 파이프라인의 데이터 수집, 학습, 배포, 모니터링 단계에서 발생하는 보안 위협은 어떻게 분류할 수 있는가?

RQ2. 연구용 ML 실험과 운영용 ML 시스템 사이의 보안·재현성·평가 격차는 어떤 방식으로 줄일 수 있는가?

RQ3. ML 공급망 보안을 위해 어떤 로그, 메타데이터, 검증 절차, assurance case가 필요한가?
```

### 10.2 위협모형 표

```markdown
# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | MLOps 기반 ML 서비스 파이프라인 |
| 보호 자산 | 학습 데이터, 모델 아티팩트, 코드 저장소, 배포 설정, 로그, 모니터링 데이터 |
| 공격자 | 내부자 / 외부 공격자 / 공급망 공격자 / 악성 패키지 제공자 |
| 공격자의 지식 | White-box / Gray-box / Black-box |
| 공격자의 능력 | 데이터 오염, 코드 변경, 의존성 조작, 모델 아티팩트 변조, 로그 삭제 |
| 공격 경로 | 데이터 파이프라인, Git 저장소, CI/CD, 모델 레지스트리, 배포 서버, 모니터링 시스템 |
| 공격 성공 조건 | 오염된 모델 배포, 성능 저하, 보안 로그 누락, drift 미탐지, 서비스 장애 |
| 방어자 가정 | 버전관리, 접근통제, 로그 감사, artifact signing, drift monitoring 가능 |
| 제외 범위 | 실제 운영 서비스 침해, 무단 시스템 접근, 실제 악성 패키지 배포 |
```

### 10.3 평가방법 표

```markdown
# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Pipeline Integrity | Integrity check rate | 데이터·모델·코드 해시 검증 | Pipeline metadata | 무결성 |
| Deployment Reliability | Deployment success/failure rate | 배포 성공률 및 롤백 기록 분석 | Deployment logs | 운영 안정성 |
| Drift Detection | Drift score | 입력/출력 분포 변화 측정 | Monitoring data | 모델 감시 |
| Incident Response | MTTR | 장애 또는 보안 이벤트 복구 시간 측정 | Incident logs | 대응력 |
| Reproducibility | Re-run consistency | 동일 config 재실행 결과 비교 | Config, seed, artifact | 재현성 |
| Auditability | Audit coverage | 로그·메타데이터 추적 가능성 평가 | Logs/metadata | 책임성 |
| Supply Chain Risk | Dependency risk score | 패키지·모델 artifact 검증 | SBOM/AI BOM | 공급망 |
```

---

## 11. 실습 방향

`04_experiment/experiment_report.md`에는 MLOps 보안 파이프라인 점검 실습을 설계하라.

실습 목표:

1. 간단한 ML 프로젝트 파이프라인 구조 작성
2. 데이터 버전, 모델 버전, config, seed, 결과 로그 관리 설계
3. Docker 기반 재현 실행 구조 설계
4. 모델 아티팩트 해시 검증 설계
5. Drift monitoring 체크리스트 작성
6. AI BOM 또는 ML artifact inventory 초안 작성
7. 결과는 실제 실행 전까지 빈칸으로 두고, 실행 후에는 `outputs/metrics_summary.csv`, `outputs/results.json`, `outputs/run_log.md`를 생성한 뒤 실험보고서, 통합보고서, 제출 체크리스트, AI 활용기록을 함께 갱신한다.

실습 환경:

```text
OS: Ubuntu 24.04
Container: Docker
Python: 3.11 (python:3.11-slim)
Package manager: uv (Dockerfile 내부 포함, WSL 호스트 설치 금지)
Install: 컨테이너 내부 uv sync
Dataset: scikit-learn digits 또는 synthetic data
Model Registry: local folder 또는 확인 필요
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
docker build -t w14-aisec .
docker run --rm -it -v $(pwd):/workspace w14-aisec bash
python src/run_experiment.py --config configs/config.yaml
```

실험 결과 표 형식:

```markdown
# 실험 결과

| 점검 항목 | 측정 지표 | 결과 | 보안 의미 |
|---|---|---|---|
| 데이터 버전관리 | Dataset hash |  | 데이터 무결성 |
| 모델 아티팩트 검증 | Model hash |  | 모델 변조 탐지 |
| 재현 실행 | Re-run consistency |  | 재현성 |
| Drift monitoring | Drift score |  | 운영 감시 |
| 로그 감사 | Audit coverage |  | 책임성 |
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
# W14 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | AI 공급망 보안을 위한 MLOps 보안통제 프레임워크 연구 | MLOps pipeline | Supply chain attack | 프레임워크 설계 | 높음 |
| 2 | ML 모델 배포 파이프라인의 데이터·모델 아티팩트 무결성 검증 연구 | ML deployment | Artifact tampering | 체크리스트/모의실험 | 높음 |
| 3 | 운영형 AI 시스템의 drift monitoring과 보안 사고대응 평가 기준 연구 | 운영 AI 시스템 | Drift / monitoring failure | 평가체계 설계 | 보통 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | 연구용 ML과 운영용 ML 시스템의 보안 격차 |
| 관련연구 | MLOps practices, ML deployment, AIOps, edge AI, software engineering |
| 연구문제 | ML 공급망과 운영 파이프라인 보안 |
| 연구방법 | 문헌분석, 보안통제 매핑, 체크리스트 설계 |
| 분석/실험 | artifact hash, drift score, audit coverage 평가 |
| 보안적 함의 | 기밀성, 무결성, 가용성, 책임성 관점 |
| 결론 | MLOps 보안통제 및 assurance case 프레임워크 제안 |
```

---

## 14. 최종 통합보고서 작성 지시

`06_report/final/integrated_report_final.md`에는 다음 목차로 작성하라.

```markdown
# W14 MLOps/DevOps·데이터/모델 파이프라인·공급망 보안 통합보고서

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
10. 실제 운영 서비스 침해, 무단 시스템 접근, 실제 악성 패키지 배포 절차는 작성하지 않는다.
11. 실습은 local toy MLOps pipeline 또는 synthetic data 기반 점검으로 제한한다.

---

## 16. 완료 후 출력 형식

작업 완료 후 다음 형식으로 보고하라.

```markdown
# W14 작성 완료 보고

## 1. 작성한 파일

## 2. 보완한 파일

## 3. 확인 필요 항목

## 4. 논문 원문 확인 필요 항목

## 5. 다음 작업 우선순위
```
