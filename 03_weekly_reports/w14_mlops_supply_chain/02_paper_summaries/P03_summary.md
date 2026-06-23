# P03 Summary

## A Joint Study of the Challenges, Opportunities, and Roadmap of MLOps and AIOps: A Systematic Survey — Josu Diaz-de-Arcaya et al., ACM Computing Surveys, 2023/2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W14 MLOps & AI Supply Chain |
| 논문명 | A Joint Study of the Challenges, Opportunities, and Roadmap of MLOps and AIOps: A Systematic Survey |
| DOI | https://doi.org/10.1145/3625289 |
| 검증 상태 | W14 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 Cheng et al. AIOps 관련 보조 문헌으로 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 MLOps와 AIOps를 **model lifecycle, operational telemetry, incident management, automation, monitoring, roadmap** 관점에서 함께 정리하며, W14에서 AI 보안 운영과 관제 자동화의 연결을 제공한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | MLOps와 AIOps는 어떤 운영 데이터를 공유하는가? |
| RQ2 | AI 시스템 장애·보안사고를 탐지하기 위해 어떤 telemetry와 alert가 필요한가? |
| RQ3 | 자동화된 운영 대응은 어떤 approval과 rollback 절차가 필요한가? |

---

## 3. 핵심 지표

$$
OpsScore = DetectionCoverage + AlertQuality + RecoveryReadiness - AutomationRisk
$$

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | telemetry, incident log, alert pipeline, model registry, deployment event |
| 공격자/위험 | log tampering, alert fatigue, automation error, monitoring blind spot |
| 지표 | alert precision/recall, incident MTTR, false alarm rate, audit completeness |
| 재현성 | incident timeline, model version, alert rule, operator action 기록 |

---

## 5. 기말논문 연결

P03은 AI 보안을 운영 관제와 incident response로 확장하는 문헌이다. W09 DRL 자동 대응과 W14 MLOps 감사체계를 연결한다.

---

## 6. 최종 판단

P03은 W14의 MLOps/AIOps bridge 문헌이다. 로컬 PDF 차이 메모를 유지하고 공식 DOI 기준으로 사용한다.
