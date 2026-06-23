# P01 Summary

## A Survey on Evaluation of Large Language Models — Yupeng Chang et al., ACM TIST, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W15 Reproducibility, XAI & Final Paper Bridge |
| 논문명 | A Survey on Evaluation of Large Language Models |
| DOI | https://doi.org/10.1145/3641289 |
| 검증 상태 | W15 `doi_check.md` 기준 공식 DOI 확인. ACM TIST 15(3), Article 39. 원 프롬프트의 ACM CSUR 표기와 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 LLM 평가를 **benchmark taxonomy, task ability, human evaluation, robustness, safety, hallucination, contamination** 관점에서 정리하며, W15의 최종 평가체계와 benchmark contamination 관리의 핵심 문헌이다.

---

## 2. 핵심 수식·지표

$$
EvalScore=\sum_{k=1}^{K}w_k Metric_k
$$

$$
ContaminationRisk=\frac{|D_{train}\cap D_{test}|}{|D_{test}|}
$$

---

## 3. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | benchmark, hidden test set, prompt set, evaluation log |
| 위험 | benchmark contamination, evaluation gaming, cherry-picking, hidden leakage |
| 지표 | task score, hallucination rate, safety score, contamination check, human review agreement |
| 재현성 | model version, prompt, decoding config, judge rubric, raw output log 기록 |

---

## 4. 기말논문 연결

P01은 기말논문의 평가방법 장에서 LLM/RAG 평가축을 설계하는 근거다. 단일 점수가 아니라 성능·안전·프라이버시·근거성·재현성을 분리한다.
