# P03 Summary

## Prompting Frameworks for Large Language Models: A Survey — Xiaoxia Liu et al., ACM Computing Surveys, 2026

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W08 RAG·프롬프팅 프레임워크 & 프롬프트 인젝션 |
| 논문명 | Prompting Frameworks for Large Language Models: A Survey |
| 저자 | Xiaoxia Liu, Jingyi Wang, Xiaohan Yuan, Jun Sun, Guoliang Dong, Peng Di, Wenhai Wang, Dongxia Wang |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 58, No. 10, Article 255, 38 pages, 2026 |
| DOI | https://doi.org/10.1145/3789253 |
| 로컬 PDF | `01_papers/pdf/03_Liu_et_al_2026_Prompting_Frameworks_for_LLMs.pdf` |
| 검증 상태 | W08 `paper_list.md` 기준 DOI/PDF 확인. 강의계획서의 `X. Liu et al.` 표기는 Xiaoxia Liu et al.을 가리키는 것으로 해석 가능하나, 최종 제출 전 수업자료와 대조 필요 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W08 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W08에서 prompting framework, prompt 구성요소, RAG prompt, tool prompt, prompt injection 신뢰 경계 분석의 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 LLM prompting framework를 **prompt template, zero-shot/few-shot prompting, in-context learning, chain-of-thought, decomposition, self-refinement, retrieval-augmented prompting, tool prompting, agent prompting, prompt optimization, evaluation** 관점에서 체계화하며, W08에서 prompt가 단순 입력문이 아니라 **LLM 행동·정책·검색 context·도구 호출을 제어하는 핵심 인터페이스이자 보안 공격면**임을 설명하는 핵심 survey 문헌이다.

---

## 2. 핵심 연구문제

> Prompting framework는 LLM의 추론·검색·도구사용·응답 형식을 어떻게 제어하며, system/user/retrieved/tool prompt의 신뢰 경계가 무너질 때 prompt injection과 policy bypass가 어떻게 발생하는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | Prompting framework는 LLM 행동을 zero-shot, few-shot, CoT, decomposition, self-refinement, RAG, tool use 방식으로 어떻게 구조화하는가? |
| RQ2 | System prompt, user prompt, retrieved context, tool instruction, memory/history는 어떤 신뢰 경계를 가져야 하는가? |
| RQ3 | Chain-of-thought, tool prompting, RAG prompting, agent prompting은 어떤 새로운 공격면을 만드는가? |
| RQ4 | Prompt template과 prompt pipeline은 어떻게 버전관리·재현성·감사 대상으로 다뤄야 하는가? |
| RQ5 | Prompt injection은 prompting framework의 어떤 구조적 취약성, 즉 instruction hierarchy와 untrusted context 분리 실패로 해석할 수 있는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W08 연결 |
|---|---|---|
| Prompting framework taxonomy | LLM prompting 방법을 task formulation, reasoning, retrieval, tool use, optimization, evaluation 관점으로 정리 | W08 prompt 구조의 기본 분류체계 |
| Prompt 구성요소 정리 | system instruction, user input, context, example, retrieved evidence, tool instruction을 구분 | prompt injection 신뢰 경계 정의 |
| Reasoning prompt 정리 | CoT, decomposition, self-consistency, reflection, verification 등 reasoning prompting 정리 | 환각 완화와 사고과정 제어 분석 |
| RAG/tool/agent prompt 확장 | retrieval context, tool call, memory, agent planning을 prompt framework에 포함 | RAG와 agent 보안 공격면 연결 |
| 평가·한계·미래방향 제시 | utility, robustness, safety, reproducibility, prompt optimization의 한계 제시 | W08 보안 평가 지표와 W15 evidence chain 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | LLM은 prompt에 따라 행동이 크게 달라지며, prompting은 LLM 활용의 핵심 인터페이스다. 다양한 prompting framework를 체계화할 필요가 있다. | LLM은 같은 모델이어도 질문을 어떻게 쓰느냐에 따라 전혀 다르게 답한다. 이 논문은 “질문을 설계하는 방법들”을 정리한다. |
| 2. Background | LLM, instruction following, in-context learning, prompt template, decoding, evaluation 기본 개념을 설명한다. | prompt는 단순 문장이 아니라 모델에게 주는 작업 지시서다. |
| 3. Basic Prompting | zero-shot, few-shot, example-based prompting 등 기본 방식을 정리한다. | 예시를 주지 않고 시키거나, 몇 개 예시를 보여주고 따라 하게 하는 방식이다. |
| 4. Reasoning-Oriented Prompting | chain-of-thought, step-by-step reasoning, decomposition, self-consistency 등을 정리한다. | 어려운 문제를 한 번에 풀지 않고 중간 단계를 나눠 풀게 하는 방법이다. |
| 5. Retrieval-Augmented Prompting | 외부 문서, 검색 결과, knowledge base를 prompt context로 넣어 답변을 보강한다. | LLM에게 기억에만 의존하지 말고 자료를 찾아보고 답하게 하는 방식이다. |
| 6. Tool/Agent Prompting | calculator, search, code interpreter, API, database 등 외부 도구를 호출하도록 prompt를 구성한다. | LLM이 말만 하는 것이 아니라 도구를 골라 쓰도록 지시하는 방식이다. |
| 7. Prompt Optimization | 사람이 직접 prompt를 쓰는 것뿐 아니라 자동으로 prompt를 탐색·개선하는 방법을 다룬다. | 여러 질문 방식을 시험해 보고 가장 잘 작동하는 지시문을 찾는 과정이다. |
| 8. Evaluation | prompt 성능을 accuracy, consistency, robustness, safety, cost, human preference 등으로 평가한다. | 답이 맞는지만 보지 말고, 안전한지·일관적인지·비용이 적절한지도 봐야 한다. |
| 9. Applications | QA, summarization, code generation, reasoning, planning, domain-specific assistant 등 응용을 정리한다. | prompt 설계는 검색, 코딩, 요약, 상담, 업무 자동화에 모두 영향을 준다. |
| 10. Challenges and Future Directions | prompt sensitivity, prompt injection, reproducibility, privacy, evaluation standard, automation 한계를 논의한다. | prompt가 조금만 바뀌어도 결과가 달라지고, 악성 문서가 prompt처럼 작동할 수 있다. |
| 11. Conclusion | Prompting framework는 LLM 활용의 핵심 계층이며, 안전성·재현성·평가체계가 함께 필요하다. | LLM을 잘 쓰려면 질문을 잘 쓰는 수준을 넘어 prompt pipeline 전체를 관리해야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 prompting framework와 W08 보안 평가를 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Prompt-Conditioned Generation

LLM 출력은 system instruction, user prompt, context, retrieved evidence, tool instruction, 이전 출력에 조건부로 생성된다.

$$
y_t\sim p_\theta(y_t\mid s,u,c,r,\tau,y_{<t})
$$

| 기호 | 의미 |
|---|---|
| $s$ | system prompt 또는 상위 정책 지시 |
| $u$ | user prompt |
| $c$ | conversation history 또는 task context |
| $r$ | retrieved documents/context |
| $\tau$ | tool instruction 또는 tool output |
| $y_{<t}$ | 이전에 생성된 token |

### 비전공자용 설명

LLM은 사용자 질문만 보고 답하는 것이 아니다. 시스템 지시, 이전 대화, 검색된 문서, 도구 결과가 한꺼번에 섞인 조건에서 다음 단어를 고른다.

### 보안적 의미

신뢰할 수 없는 retrieved context나 tool output이 $r,\tau$에 들어가면 system prompt와 충돌하는 악성 지시가 포함될 수 있다. 이것이 indirect prompt injection의 구조적 원인이다.

---

### 5.2 Prompt Template

Prompt framework는 입력 변수를 template에 채워 LLM prompt를 구성한다.

$$
P=T(s,u,c,r,\tau;\phi)
$$

| 기호 | 의미 |
|---|---|
| $P$ | 최종 prompt |
| $T$ | prompt template 함수 |
| $\phi$ | template parameter, formatting rule, instruction hierarchy |

### 비전공자용 설명

메일 양식에 이름·날짜·본문을 끼워 넣듯이, LLM에게 보낼 지시문도 일정한 틀에 여러 정보를 넣어 만든다.

### 보안적 의미

Template이 system/user/retrieved/tool 영역을 명확히 분리하지 않으면, 외부 문서에 들어 있는 문장이 상위 지시처럼 해석될 수 있다.

---

### 5.3 In-Context Learning

Few-shot prompting은 예시 집합을 prompt에 넣어 모델이 task pattern을 따라 하게 한다.

$$
y\sim p_\theta(y\mid x,\{(x_i,y_i)\}_{i=1}^{k})
$$

| 기호 | 의미 |
|---|---|
| $x$ | 현재 입력 |
| $(x_i,y_i)$ | prompt에 포함된 예시 |
| $k$ | 예시 개수 |

### 비전공자용 설명

모델에게 “이런 식으로 답해라”는 예시를 몇 개 보여주면, 모델이 그 형식을 따라 답한다.

### 보안적 의미

예시가 오염되면 모델은 잘못된 형식이나 정책 위반 패턴을 따라 할 수 있다. 따라서 few-shot example도 prompt supply chain의 일부다.

---

### 5.4 Retrieval-Augmented Prompting

검색된 문서 $r$을 prompt context에 넣어 LLM 답변을 생성한다.

$$
y\sim p_\theta(y\mid q,R(q))
$$

$$
R(q)=TopK_{d_i\in D}\;sim(E(q),E(d_i))
$$

| 기호 | 의미 |
|---|---|
| $q$ | 사용자 질문 |
| $R(q)$ | 검색된 문서 또는 context |
| $D$ | 문서 집합 |
| $E(\cdot)$ | embedding 함수 |

### 비전공자용 설명

질문과 비슷한 문서를 찾아서, 그 문서를 보고 답하게 하는 방식이다.

### 보안적 의미

검색된 문서 안에 “이전 지시를 무시하라” 같은 악성 instruction이 들어 있으면 LLM이 이를 따를 수 있다. W08의 prompt injection과 직접 연결된다.

---

### 5.5 Tool Prompting

LLM이 외부 도구를 호출할 때는 도구 선택과 인자 생성이 prompt로 제어된다.

$$
a_t\sim p_\theta(a_t\mid s,u,c,Tools,y_{<t})
$$

| 기호 | 의미 |
|---|---|
| $a_t$ | tool call 또는 action |
| $Tools$ | 사용 가능한 도구 목록과 설명 |

### 비전공자용 설명

LLM에게 계산기, 검색, DB, 코드 실행 도구를 줄 수 있다. 이때 LLM은 어떤 도구를 쓸지, 어떤 값을 넣을지 결정한다.

### 보안적 의미

Prompt injection이 tool call을 유도하면 잘못된 API 호출, 과도한 권한 사용, 데이터 유출이 발생할 수 있다. 따라서 tool permission과 human approval이 필요하다.

---

### 5.6 Prompt Robustness Score

Prompt framework의 안정성은 prompt 변형이나 공격 prompt에 대해 정책을 유지하는지로 평가할 수 있다.

$$
RobustPromptScore=Utility-\lambda_1 ASR-\lambda_2 PolicyViolation-\lambda_3 OverRefusal
$$

| 기호 | 의미 |
|---|---|
| $Utility$ | 정상 task 성능 |
| $ASR$ | prompt injection 또는 jailbreak 성공률 |
| $PolicyViolation$ | 정책 위반 출력 비율 |
| $OverRefusal$ | 안전한 요청까지 거절하는 비율 |

### 비전공자용 설명

좋은 prompt system은 일을 잘하면서도, 공격 지시에 속지 않고, 정상 요청을 과도하게 거절하지 않아야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W08/P03에서의 의미 |
|---|---|---|
| Prompting | LLM의 task, format, reasoning, policy를 지시문으로 제어 | LLM 행동 제어 인터페이스 |
| Zero-shot/Few-shot | 예시 없이 또는 예시와 함께 task 수행 | 기본 prompt 설계 |
| In-context Learning | prompt 안의 예시와 맥락으로 task pattern 학습 | prompt가 임시 학습 데이터처럼 작동 |
| Chain-of-Thought | 중간 추론 단계를 유도 | reasoning 성능 향상과 누출 위험 병존 |
| Decomposition | 복잡한 task를 작은 단계로 분할 | agent/RAG pipeline 설계 기반 |
| RAG Prompting | 검색 context를 prompt에 포함 | hallucination 완화와 injection 위험 병존 |
| Tool Prompting | 외부 도구 사용을 prompt로 제어 | 권한·API·데이터 유출 위험 |
| Prompt Optimization | prompt를 자동 탐색·개선 | 성능 향상과 평가 재현성 문제 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Prompting Framework 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | prompt, retrieved context, tool output에 민감정보가 포함될 수 있음 | sensitive disclosure rate, leakage rate |
| 무결성 | 악성 prompt가 system instruction, retrieved context, tool instruction을 오염 | prompt injection ASR, policy violation rate |
| 가용성 | prompt가 길어지고 tool/RAG pipeline이 복잡해지면 latency와 failure 증가 | latency, token cost, tool failure rate |
| 프라이버시 | user prompt와 conversation history가 개인정보를 포함할 수 있음 | prompt privacy risk, log minimization rate |
| 책임성 | 어떤 prompt template과 context로 답했는지 추적해야 함 | prompt provenance, template version, audit completeness |
| 안전성 | CoT/tool/agent prompt가 위험한 action을 유도할 수 있음 | safe completion rate, human approval rate |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | system prompt, prompt template, user prompt, retrieved context, few-shot example, chain-of-thought, tool instruction, memory, output policy, prompt log |
| 공격자 목표 | system instruction override, prompt injection, jailbreak, retrieved-context injection, tool misuse, data exfiltration, policy bypass |
| 공격자 능력 | user prompt 조작, 악성 문서 업로드, few-shot example 오염, tool output 조작, prompt-like instruction 삽입 |
| 공격 경로 | user input/source document → prompt template → retrieved/tool context → LLM decoding → output/tool call |
| 방어자 능력 | instruction hierarchy, context isolation, prompt sanitization, tool permission, template versioning, output policy check, human approval |
| 제외 범위 | 실제 서비스 공격, 실제 개인정보 유출, 무단 API 호출, 공격 payload 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W08/P03 활용 |
|---|---|---|---|
| Task utility | accuracy, exact match, BLEU/ROUGE, human preference | 정상 task 수행 능력 | 기본 prompt 성능 |
| Prompt robustness | prompt sensitivity, variance across prompt variants | prompt 표현 변화에 대한 안정성 | 재현성 평가 |
| Injection safety | ASR, policy compliance, instruction conflict rate | 악성 지시 방어 능력 | W08 P04 연결 |
| RAG faithfulness | citation support, evidence faithfulness | 검색 근거에 충실한지 | W08 P01/P02 연결 |
| Tool safety | unauthorized tool call rate, tool error rate | 도구 호출 안전성 | agent security 연결 |
| Privacy | sensitive disclosure rate, context leakage rate | 민감정보 노출 여부 | W11 privacy 연결 |
| Cost | token length, latency, tool call count | 운영 비용 | W14 MLOps 연결 |
| Auditability | prompt template version, prompt-context-output trace | 사후 검증 가능성 | W15 evidence chain |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Prompt template | system/user/context/tool 영역 분리, template version, 작성일 |
| Prompt variables | user input, retrieved context, few-shot examples, tool descriptions |
| Model setting | LLM model/version, temperature, top-p, max tokens, decoding setting |
| RAG setting | retriever, Top-k, chunking, reranker, context formatting |
| Tool setting | tool list, permission, API scope, human approval rule |
| Evaluation | utility, ASR, policy compliance, over-refusal, latency, cost |
| Security log | prompt-context-output-tool trace, failed/successful injection case, reviewer decision |
| 한계 | toy prompt set 결과를 실제 서비스 보안 보증으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. Prompting framework를 단순 prompt engineering 팁이 아니라 LLM 시스템 설계 계층으로 정리한다.
2. Zero-shot/few-shot, CoT, RAG prompting, tool prompting, prompt optimization을 하나의 taxonomy로 연결한다.
3. Prompt가 LLM의 task, reasoning, external knowledge, tool use, output format을 통제하는 핵심 인터페이스임을 설명한다.
4. W08 prompt injection을 구조적으로 해석하기 위한 system/user/retrieved/tool 신뢰 경계의 근거를 제공한다.
5. 기말논문에서 prompt pipeline 감사표와 prompt-template versioning 지표를 설계하는 근거 문헌으로 사용 가능하다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 직접 prompt injection survey는 아님 | prompting framework survey이며 공격·방어 전문 논문은 아니다. | W08 P04/P05와 결합 |
| Prompt 재현성 문제 | 같은 prompt라도 모델 버전·decoding 설정·context에 따라 결과가 달라진다. | template version, model setting, output trace 기록 |
| Prompt sensitivity | 작은 표현 차이로 성능과 안전성이 달라질 수 있다. | prompt variant evaluation 포함 |
| RAG context 신뢰 문제 | 검색 문서가 신뢰할 수 없으면 prompt 전체가 오염된다. | context isolation, source trust, citation support 평가 |
| Tool/agent 위험 | prompt가 tool call을 제어하면서 권한 문제를 만든다. | least privilege, human approval, tool audit 적용 |
| CoT/내부추론 노출 | reasoning prompt가 민감 정보나 정책 우회 단서를 노출할 수 있다. | reasoning visibility 정책과 redaction 규칙 포함 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | LLM 보안에서 prompt는 단순 입력이 아니라 시스템 행동을 제어하는 보안 인터페이스라는 문제의식 |
| 2장 관련연구 | prompting framework, CoT, RAG prompting, tool prompting, prompt optimization survey 정리 |
| 3장 위협모형 | system/user/retrieved/tool/memory prompt의 신뢰 경계 정의 |
| 4장 연구방법 | ASR, policy compliance, over-refusal, prompt sensitivity, template versioning 지표 설계 |
| 5장 분석 | prompt pipeline과 prompt injection attack surface mapping 표/그림 제시 |
| 6장 보안적 함의 | context isolation, tool permission, human approval, prompt audit log 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W08에서 기말논문에 반영할 개념: prompting framework는 LLM의 출력, reasoning, retrieval, tool use를 제어하는 시스템 계층이므로, prompt injection은 단순 입력 공격이 아니라 신뢰 경계 붕괴 문제로 정의해야 한다.
2. W08에서 기말논문에 반영할 표·그림·실험: system/user/retrieved/tool prompt 분리표, prompt injection ASR·policy compliance·over-refusal 평가표, prompt-template versioning checklist를 반영한다.
3. W08이 LLM 보안 감사 프레임워크와 연결되는 지점: prompt template, retrieved context, tool instruction, output log를 W14/W15 evidence chain으로 관리해야 RAG/agent 보안 평가가 재현 가능해진다.

---

## 15. 최종 판단

P03은 W08에서 prompt injection을 구조적으로 해석하기 위한 핵심 문헌이다. P01/P02가 GraphRAG와 graph context를 제공한다면, P03은 그 context가 LLM prompt로 들어가 LLM 행동을 어떻게 제어하는지 설명한다. 따라서 W08 기말논문 연결에서는 P03을 **prompt pipeline, 신뢰 경계, prompt-template versioning, RAG/tool prompt 보안 평가의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P03_summary.md -o P03_summary.docx
pandoc P03_summary.md -o P03_summary.pdf --pdf-engine=xelatex
```
