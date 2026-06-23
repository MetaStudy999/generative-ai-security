# P02 Summary

## Challenges in Deploying Machine Learning: A Survey of Case Studies — Andrei Paleyes, Raoul-Gabriel Urma, Neil D. Lawrence, ACM Computing Surveys, 2022/2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W14 MLOps & AI Supply Chain |
| 논문명 | Challenges in Deploying Machine Learning: A Survey of Case Studies |
| DOI | https://doi.org/10.1145/3533378 |
| 검증 상태 | W14 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 arXiv판이지만 제목·저자·DOI 주제 대응 |

---

## 1. 한 문장 요약

이 논문은 ML 배포의 실제 어려움을 **data dependency, model drift, infrastructure, monitoring, human process, organizational gap** 관점에서 정리하며, W14의 운영 보안·재현성·incident 대응의 핵심 사례 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | ML 모델은 연구환경에서 운영환경으로 이동할 때 어떤 실패 조건을 갖는가? |
| RQ2 | Drift, feedback loop, data quality는 보안성과 신뢰성에 어떤 영향을 주는가? |
| RQ3 | 배포 후 모니터링과 rollback은 어떤 증거를 남겨야 하는가? |

---

## 3. 핵심 지표

$$
DeploymentRisk = DriftRisk + DataQualityRisk + InfraRisk + MonitoringGap
$$

$$
MTTR = t_{restore}-t_{incident}
$$

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | production data, model endpoint, feature pipeline, monitoring dashboard |
| 공격자/위험 | drift, schema break, data contamination, misconfiguration, feedback loop |
| 지표 | drift score, data quality error, incident count, MTTR, rollback success |
| 재현성 | deployment version, data schema, feature version, alert log 기록 |

---

## 5. 기말논문 연결

P02는 실험실 AI 보안 평가를 운영환경 배포 문제로 확장하는 근거다. 기말논문에서 RAG/LLM 보안 프레임워크도 배포·모니터링·rollback 체계를 포함해야 한다.

---

## 6. 최종 판단

P02는 W14의 실전 배포 핵심 문헌이다. 좋은 모델보다 운영 중 모니터링 가능한 모델이 중요하다.
