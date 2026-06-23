# P01 Summary

## A Multivocal Review of MLOps Practices, Challenges and Open Issues — Beyza Eken et al., ACM Computing Surveys, 2025/2026

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W14 MLOps & AI Supply Chain |
| 논문명 | A Multivocal Review of MLOps Practices, Challenges and Open Issues |
| 저자 | Beyza Eken et al. |
| DOI | https://doi.org/10.1145/3747346 |
| 검증 상태 | W14 `paper_list.md` 기준 공식 DOI 확인. 수업자료의 Bayram Eken 및 긴 제목 표기 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 MLOps 실무를 **data management, model training, deployment, monitoring, governance, reproducibility, organizational challenge** 관점에서 정리하며, W14에서 AI 보안 운영체계의 기본 배경을 제공한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | MLOps는 모델 개발과 운영을 어떤 생명주기로 연결하는가? |
| RQ2 | 재현성·모니터링·거버넌스는 AI 보안과 어떻게 연결되는가? |
| RQ3 | 운영 중 drift, incident, rollback은 어떤 audit evidence를 요구하는가? |

---

## 3. 핵심 지표

$$
MLOpsRisk = DataRisk + ModelRisk + DeploymentRisk + MonitoringGap
$$

$$
Coverage_{audit}=\frac{|Controls_{logged}|}{|Controls_{required}|}
$$

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | dataset, pipeline, model artifact, registry, deployment config, monitoring log |
| 공격자 목표 | 데이터/모델 공급망 오염, 배포 설정 조작, 모니터링 우회 |
| 지표 | audit coverage, drift detection, rollback time, reproducibility score |
| 재현성 | data version, model version, environment, approval log 기록 |

---

## 5. 기말논문 연결

P01은 AI 보안 프레임워크를 운영 가능한 MLOps 통제로 변환하는 근거다. W01~W13의 공격·방어 지표를 운영 로그와 승인 절차로 묶는 데 사용한다.

---

## 6. 최종 판단

P01은 W14의 MLOps 기본 문헌이다. AI 보안은 실험 성능이 아니라 운영 증거와 감사 가능성까지 포함해야 한다.
