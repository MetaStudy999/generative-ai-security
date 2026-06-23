# P01 Summary

## A Survey on Evaluation of Large Language Models — Yupeng Chang et al., ACM Transactions on Intelligent Systems and Technology, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W07 LLM 보안·프라이버시 |
| 논문명 | A Survey on Evaluation of Large Language Models |
| 저자 | Yupeng Chang et al. |
| 공식 출판 정보 | ACM Transactions on Intelligent Systems and Technology, Vol. 15, No. 3, Article 39, pp. 1–45, 2024 |
| DOI | https://doi.org/10.1145/3641289 |
| 강의계획서 표기와 차이 | 강의계획서에는 `J. Chang et al.` 및 ACM Computing Surveys로 표기되어 있으나, repo의 공식 확인 정보는 ACM TIST 15(3), Article 39임 |
| 로컬/공식 확인 상태 | 제목과 DOI 기준 로컬 논문 확인. 최종 참고문헌은 공식 DOI 메타데이터 기준 사용 |
| 핵심 근거 사용 가능 여부 | 가능. 단, W07 보안 전문 문헌은 P02/P03이 담당하고, P01은 평가체계 배경 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 대규모 언어모델 평가를 **능력 평가, 정렬 평가, 안전성 평가, 강건성 평가, 프라이버시 평가, 환각 평가, 인간 평가, 벤치마크 설계**로 분해하여, LLM을 단일 점수로 평가하지 않고 다중 지표와 재현 가능한 평가 절차로 검증해야 한다는 기준을 제공하는 핵심 survey 문헌이다.

---

## 2. 핵심 연구문제

> LLM을 실제 시스템에 적용하려면 어떤 능력과 위험을 각각 측정해야 하며, benchmark 점수와 실제 안전성·신뢰성 사이의 간극을 어떻게 줄일 수 있는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | LLM 평가는 knowledge, reasoning, language generation, instruction following, tool use 등을 어떻게 구분해야 하는가? |
| RQ2 | Benchmark score가 높더라도 hallucination, privacy leakage, jailbreak, bias, toxicity가 남는 이유는 무엇인가? |
| RQ3 | LLM 평가에서 automatic metric, human evaluation, LLM-as-a-judge는 각각 어떤 장단점과 편향을 갖는가? |
| RQ4 | 평가 데이터 오염, hidden test leakage, benchmark overfitting을 어떻게 통제해야 하는가? |
| RQ5 | W07의 LLM 보안·프라이버시 평가를 W08 RAG, W14 MLOps, W15 재현성 평가로 어떻게 확장할 수 있는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W07 연결 |
|---|---|---|
| LLM 평가 범위 정리 | LLM의 능력과 위험을 여러 평가 축으로 분리 | LLM 보안 평가표의 상위 구조 제공 |
| Benchmark taxonomy | 다양한 benchmark와 task 유형을 분류 | 평가 데이터 오염·과적합 위험 분석 |
| Human evaluation 논의 | 자동 지표만으로 판단하기 어려운 영역 제시 | 안전성·책임성·사용자 신뢰 평가 연결 |
| Safety/robustness 평가 연결 | 일반 성능과 위험 조건 성능을 분리 | jailbreak, prompt injection, hallucination 평가로 확장 |
| 재현성 문제 제기 | 모델 버전, prompt, decoding, judge 기준 기록 필요 | W14/W15의 evidence chain으로 연결 |

---

## 4. 핵심 이론 및 수식

> 작성 원칙: GitHub, MS Word, PDF 변환 호환성을 위해 수식은 Markdown 표 밖의 LaTeX block math로 작성한다. 아래 수식은 논문의 특정 원문 수식을 직접 전사한 것이 아니라, 논문이 정리한 평가 문제를 W07 보고서에서 계량화하기 위한 표준화된 표현이다.

### 4.1 다중 평가 점수

LLM 평가는 하나의 점수가 아니라 여러 지표의 가중 결합으로 표현할 수 있다.

$$
Score_{LLM}=\sum_{k=1}^{K}w_k\cdot Metric_k
$$

| 기호 | 의미 |
|---|---|
| $Metric_k$ | 정확도, 추론 성능, 안전성, 강건성, 환각률, 프라이버시 위험 등 개별 평가 지표 |
| $w_k$ | 평가 목적별 가중치 |
| $K$ | 평가 지표 수 |

### 보안적 의미

LLM이 특정 benchmark에서 높은 점수를 받아도 안전한 모델이라는 뜻은 아니다. 보안 평가에서는 일반 task utility, hallucination, privacy leakage, jailbreak resistance, prompt injection resistance를 분리해야 한다.

---

### 4.2 Hallucination Rate

모델 응답 중 근거가 없거나 제공된 source와 불일치하는 응답 비율을 다음처럼 표현할 수 있다.

$$
HallucinationRate=\frac{N_{unsupported}}{N_{answers}}
$$

| 기호 | 의미 |
|---|---|
| $N_{unsupported}$ | 근거가 없거나 출처와 불일치한 응답 수 |
| $N_{answers}$ | 전체 응답 수 |

### 보안적 의미

환각은 단순 품질 문제가 아니라 보안 문제다. RAG, 의료, 법률, 보안관제에서는 근거 없는 답변이 잘못된 의사결정, 허위 경보, 위험 조언, 책임소재 불명확성으로 이어질 수 있다.

---

### 4.3 Benchmark Contamination Risk

평가 데이터가 학습 데이터에 포함되었거나 모델이 benchmark 패턴을 사전에 접했을 가능성을 평가해야 한다.

$$
ContaminationRisk=\frac{|D_{train}\cap D_{test}|}{|D_{test}|}
$$

| 기호 | 의미 |
|---|---|
| $D_{train}$ | 학습 또는 사전학습 데이터셋 |
| $D_{test}$ | 평가 데이터셋 |
| $D_{train}\cap D_{test}$ | 학습 데이터와 평가 데이터의 중복 영역 |

### 보안적 의미

평가 데이터 오염이 있으면 실제 능력보다 높은 성능을 보고할 수 있다. 최종 보고서에서는 benchmark contamination을 직접 계산하지 못하더라도, 평가 데이터 출처와 한계 문장을 명시해야 한다.

---

### 4.4 안전성·유틸리티 균형 점수

보안 평가에서는 유틸리티와 위험 지표를 함께 봐야 한다.

$$
SafetyUtilityScore=Utility-\lambda_1 HallucinationRate-\lambda_2 UnsafeRate-\lambda_3 LeakageRate
$$

| 기호 | 의미 |
|---|---|
| $Utility$ | 정상 task 수행 성능 |
| $UnsafeRate$ | 유해·정책 위반 응답 비율 |
| $LeakageRate$ | 민감정보 노출 비율 |
| $\lambda_i$ | 위험 지표의 상대 가중치 |

### 보안적 의미

무조건 거절하는 모델은 안전해 보일 수 있지만 utility가 낮다. 반대로 utility만 높은 모델은 위험 응답을 낼 수 있다. 따라서 refusal quality와 over-refusal도 함께 기록해야 한다.

---

## 5. LLM 평가 축 정리

| 평가 축 | 설명 | 대표 지표 | W07 보안 연결 |
|---|---|---|---|
| Knowledge | 사실 지식과 domain knowledge | QA accuracy, factuality | hallucination, citation support |
| Reasoning | 수리·논리·다단계 추론 | reasoning accuracy, chain validity | reasoning hallucination |
| Instruction Following | 지시 준수 능력 | task success, format compliance | system/user instruction conflict |
| Alignment/Safety | 정책·안전 기준 준수 | refusal quality, unsafe rate | jailbreak, harmful response |
| Robustness | 입력 교란·우회 표현 대응 | robust accuracy, ASR | prompt injection, adversarial prompt |
| Privacy | 민감정보 보호 | leakage rate, memorization risk | prompt privacy, data extraction |
| Human Evaluation | 사람 기준 품질·신뢰성 | human preference, agreement | 책임성, high-stakes review |
| Reproducibility | 평가 재현 가능성 | prompt log, model version, seed | W14/W15 evidence chain |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 평가 데이터셋, hidden test set, user prompt, system prompt, retrieved context, model output, evaluation log |
| 공격자 목표 | benchmark gaming, 평가 점수 과장, hallucination 유도, safety policy 우회, 민감정보 추출 |
| 공격자 능력 | prompt 조작, benchmark pattern 학습, repeated query, indirect prompt injection, context stuffing |
| 방어자 능력 | prompt set versioning, benchmark provenance, contamination check, human review, judge rubric, output logging |
| 제외 범위 | 실제 서비스 대상 jailbreak 실험, 민감정보 포함 prompt 사용, 비공개 benchmark 유출 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W07/P01에서의 활용 |
|---|---|---|
| Task Score | 정상 task 수행 성능 | utility baseline |
| Hallucination Rate | 근거 없는 응답 비율 | factuality·RAG 평가 |
| Citation Support | 응답이 source로 뒷받침되는 정도 | W08 RAG 연결 |
| Unsafe Rate | 유해·정책 위반 응답 비율 | safety 평가 |
| Refusal Quality | 위험 요청을 적절히 거절하는 정도 | alignment 평가 |
| Over-refusal | 정상 요청까지 과도하게 거절하는 비율 | utility 손실 평가 |
| Leakage Rate | 민감정보 노출 비율 | privacy 평가 |
| Jailbreak ASR | 공격 prompt 성공률 | robustness 평가 |
| Human Agreement | 평가자 간 일치도 | human evaluation 신뢰성 |
| Reproducibility Score | prompt/model/config/output 보존 정도 | W15 evidence chain |

---

## 8. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| 모델 | 모델명, 버전, API/로컬 여부, checkpoint |
| 프롬프트 | system prompt, user prompt, retrieved context, prompt template |
| Decoding | temperature, top-p, max tokens, seed 가능 여부 |
| 평가 데이터 | benchmark 이름, 버전, 생성 방식, contamination 한계 |
| Judge | 사람 평가자, rubric, LLM judge 모델, 평가 기준 |
| 결과 | raw output, score, error case, hallucination case |
| 보안 평가 | jailbreak ASR, leakage rate, refusal/over-refusal, citation support |
| 한계 | toy prompt 결과를 실제 서비스 안전성으로 일반화하지 않음 |

---

## 9. 논문의 고유 기여

1. LLM 평가를 다양한 task와 위험 축으로 체계화했다.
2. LLM benchmark를 단순 성능 순위가 아니라 평가 설계 문제로 다루게 한다.
3. 안전성·강건성·프라이버시·환각을 일반 성능과 분리해야 한다는 근거를 제공한다.
4. W07~W08의 LLM/RAG 보안 평가표와 W15 재현성 checklist의 기준 문헌이 된다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 빠른 benchmark 변화 | LLM 평가 benchmark는 빠르게 변한다. | 평가일, benchmark version, 모델 version을 명시한다. |
| 평가 데이터 오염 | 학습 데이터와 평가 데이터 중복 가능성이 있다. | contamination risk를 한계로 명시한다. |
| Human evaluation 비용 | 사람 평가가 필요하지만 비용과 편향이 있다. | rubric과 평가자 기준을 기록한다. |
| LLM-as-judge 편향 | LLM judge도 오류와 편향을 가질 수 있다. | judge 모델과 한계를 기록한다. |
| 보안 전문성 제한 | P01은 보안 전문 survey는 아니다. | P02/P03의 LLM security/privacy 문헌과 결합한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | LLM/RAG 보안 평가는 단일 benchmark score로 부족하다는 문제의식 |
| 2장 관련연구 | LLM evaluation taxonomy 정리 |
| 3장 위협모형 | 평가 데이터 오염, hallucination, jailbreak, privacy leakage 정의 |
| 4장 연구방법 | utility/safety/privacy/robustness/reproducibility 다중지표 설계 |
| 5장 실험/분석 | raw output과 실패 사례, 환각 사례, refusal 사례 분리 보고 |
| 6장 보안적 함의 | high-stakes domain에서 human review와 evidence 필요성 설명 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: LLM 보안 평가는 benchmark score가 아니라 utility, safety, privacy, robustness, factuality, reproducibility를 분리해 측정하는 다중지표 문제다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: LLM 평가 taxonomy 표, hallucination rate, contamination risk, refusal/over-refusal, citation support 평가표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG 답변은 검색 문서와 생성 응답을 함께 평가해야 하므로 P01의 평가 taxonomy를 W08의 source faithfulness와 W14/W15의 evidence chain으로 확장한다.

---

## 13. 최종 판단

P01은 W07의 평가체계 배경 문헌이다. 직접적인 보안 공격·방어 taxonomy는 P02/P03이 담당하지만, LLM 보안 실험의 지표 설계와 재현성 기록은 P01을 기준으로 구성하는 것이 적절하다.

---

## 14. 변환 호환성 메모

```bash
pandoc P01_summary.md -o P01_summary.docx
pandoc P01_summary.md -o P01_summary.pdf --pdf-engine=xelatex
```
