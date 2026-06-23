# P04 Summary

## Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI — Alejandro Barredo Arrieta et al., Information Fusion, 2020

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W15 Reproducibility, XAI & Final Paper Bridge |
| 논문명 | Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI |
| DOI | https://doi.org/10.1016/j.inffus.2019.12.012 |
| 검증 상태 | W15 `doi_check.md` 기준 공식 DOI 확인. Information Fusion 58, pp. 82–115 |

---

## 1. 한 문장 요약

이 논문은 XAI와 Responsible AI를 **transparency, interpretability, post-hoc explanation, trust, accountability, human-centered evaluation** 관점에서 체계화하며, W15의 책임성·보안적 함의 장을 뒷받침한다.

---

## 2. 핵심 수식·지표

$$
ResponsibleAIScore=Transparency+Accountability+Robustness+Fairness-PrivacyRisk
$$

$$
ExplanationQuality=w_1Fidelity+w_2Stability+w_3Comprehensibility
$$

---

## 3. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | user trust, explanation, decision rationale, accountability evidence |
| 위험 | fairwashing, privacy leakage, misleading explanation, automation bias |
| 지표 | transparency, interpretability, fidelity, stability, user trust, accountability coverage |
| 재현성 | explanation method, human evaluation protocol, decision log, limitation statement 기록 |

---

## 4. 기말논문 연결

P04는 기말논문의 보안적 함의와 책임성 장에 직접 반영한다. XAI는 AI 보안 평가의 보조 시각화가 아니라 책임 있는 의사결정의 증거로 다뤄야 한다.
