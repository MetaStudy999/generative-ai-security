# P02 Summary

## Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges — Rob Ashmore, Radu Calinescu, Colin Paterson, ACM Computing Surveys, 2021/2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W15 Reproducibility, XAI & Final Paper Bridge |
| 논문명 | Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges |
| DOI | https://doi.org/10.1145/3453444 |
| 검증 상태 | W15 `doi_check.md` 기준 공식 DOI 확인. 로컬 PDF는 accepted version 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 ML lifecycle assurance를 **data management, model learning, model verification, model deployment, evidence chain** 관점에서 정리하며, W15의 재현성·감사 가능성·AI 활용 고지 체계의 중심 문헌이다.

---

## 2. 핵심 수식·지표

$$
Coverage_E=\frac{|R_{covered}|}{|R_{total}|}
$$

$$
AssuranceScore=w_1DataEvidence+w_2ModelEvidence+w_3VerificationEvidence+w_4DeploymentEvidence
$$

---

## 3. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | dataset, model artifact, verification evidence, deployment log |
| 위험 | evidence gap, reproducibility failure, deployment drift, unverifiable claim |
| 지표 | evidence coverage, reproducibility score, lifecycle risk, audit completeness |
| 재현성 | DOI, data version, code, seed, config, outputs, run_log, AI disclosure 기록 |

---

## 4. 기말논문 연결

P02는 W15의 evidence chain 핵심 문헌이다. 최종 기말논문에서 모든 주장에는 문헌 근거, 실험 로그, 설정값, AI 활용 고지가 따라야 한다는 기준을 제공한다.
