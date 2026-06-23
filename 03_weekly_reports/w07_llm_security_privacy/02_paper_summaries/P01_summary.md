# P01 Summary

## A Survey on Evaluation of Large Language Models — Yupeng Chang et al., ACM TIST, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W07 LLM 보안·프라이버시 |
| 논문명 | A Survey on Evaluation of Large Language Models |
| 저자 | Yupeng Chang et al. |
| 출판 정보 | ACM Transactions on Intelligent Systems and Technology, 15(3), Article 39, pp. 1–45, 2024 |
| DOI | https://doi.org/10.1145/3641289 |
| 검증 상태 | W07 `paper_list.md` 기준 공식 DOI 확인. 강의계획서 `J. Chang` 및 ACM CSUR 표기 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 LLM 평가를 **knowledge, reasoning, instruction following, alignment, robustness, safety, hallucination, human evaluation, benchmark design** 관점에서 체계화하며, W07에서 LLM 보안 평가의 기본 계량 프레임을 제공한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | LLM은 어떤 능력과 위험 축으로 평가해야 하는가? |
| RQ2 | Benchmark score와 실제 안전성·신뢰성 사이에는 어떤 간극이 있는가? |
| RQ3 | Hallucination, robustness, privacy, toxicity, jailbreak 저항성은 어떤 별도 지표가 필요한가? |
| RQ4 | 기말논문에서 LLM/RAG 보안을 평가할 때 어떤 evidence를 남겨야 하는가? |

---

## 3. 핵심 수식·지표

### 3.1 다중 평가 점수

$$
Score_{LLM}=\sum_{k=1}^{K}w_k\cdot Metric_k
$$

| 기호 | 의미 |
|---|---|
| $Metric_k$ | 정확도, hallucination, safety, robustness 등 개별 지표 |
| $w_k$ | 평가 목적별 가중치 |

### 3.2 Hallucination Rate

$$
HallucinationRate=\frac{N_{unsupported}}{N_{answers}}
$$

### 보안 해석

LLM 평가에서 높은 일반 성능은 보안성을 보장하지 않는다. 안전성·프라이버시·robustness·출처 근거를 분리해야 한다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | 사용자 입력, 시스템 프롬프트, 검색 문서, 모델 출력, 평가 로그 |
| 공격자 목표 | 허위 응답 유도, 안전 정책 우회, 민감정보 추출, 근거 없는 답변 생성 |
| 대표 지표 | task score, factuality, hallucination rate, refusal quality, jailbreak ASR, citation support |
| 재현성 | prompt set, model version, temperature, seed, judge 기준, 평가 로그 기록 |

---

## 5. 기말논문 연결

| 장 | 반영 내용 |
|---|---|
| 2장 관련연구 | LLM 평가 taxonomy |
| 4장 연구방법 | utility/safety/privacy/robustness/reproducibility 다중지표 설계 |
| 5장 분석 | 평가표와 실패 사례 분리 |

**연결 3문장:** LLM 보안 평가는 benchmark score 하나로 판단할 수 없다. hallucination, jailbreak, privacy leakage, citation support, human review를 분리해야 한다. W08 RAG 평가에서는 이 지표를 검색 문서 근거성과 문서 오염 평가로 확장한다.

---

## 6. 최종 판단

P01은 W07의 평가체계 배경 문헌이다. 보안 전문 문헌은 P02/P03이 담당하지만, LLM 보안 실험의 지표 설계는 P01을 기준으로 구성한다.
