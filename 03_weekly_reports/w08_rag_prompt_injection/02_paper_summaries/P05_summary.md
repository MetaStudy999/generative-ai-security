# P05 Summary

## Vulnerability of Large Language Models to Prompt Injection When Providing Medical Advice — Ro Woon Lee et al., JAMA Network Open, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W08 RAG·프롬프팅 프레임워크 & 프롬프트 인젝션 |
| 논문명 | Vulnerability of Large Language Models to Prompt Injection When Providing Medical Advice |
| 저자 | Ro Woon Lee, Tae Joon Jun, Jeong-Moo Lee, Soo Ick Cho, Hyung Jun Park, Jungyo Suh |
| 공식 출판 정보 | JAMA Network Open, Vol. 8, No. 12, e2549963, 2025 |
| DOI | https://doi.org/10.1001/jamanetworkopen.2025.49963 |
| 로컬 PDF | `01_papers/pdf/05_Lee_et_al_2025_LLM_Prompt_Injection_Medical_Advice.pdf` |
| 검증 상태 | W08 `paper_list.md` 기준 DOI/PDF 확인. 강의계획서 지정 제목과 로컬 PDF 기준 제목 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W08 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W08에서 prompt injection이 의료 조언 같은 high-stakes domain에서 실제 안전 문제로 확장될 수 있음을 보여주는 관련 핵심 사례 문헌 |

---

## 1. 한 문장 요약

이 논문은 LLM이 의료 조언을 제공하는 상황에서 prompt injection에 의해 **안전정책 우회, 위험 조언, 근거 없는 정보 생성, 전문가 상담 회피, 사용자 신뢰 오도**가 발생할 수 있음을 다루는 high-stakes 응용 사례 문헌이며, W08에서 prompt injection 평가를 단순 보안 취약점이 아니라 **환자 안전·전문가 안내·근거 검증·감사 로그** 문제로 확장하는 근거를 제공한다.

---

## 2. 핵심 연구문제

> 의료 조언 제공 상황에서 LLM이 외부 또는 사용자 입력의 악성 지시에 노출될 때, 모델은 안전한 의료 정보 제공 원칙을 유지할 수 있는가, 아니면 위험하거나 근거 없는 조언으로 유도되는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | 의료 조언 맥락에서 prompt injection은 모델의 응답 방향, 안전성, 전문가 상담 권고를 어떻게 왜곡하는가? |
| RQ2 | High-stakes domain의 prompt injection 평가는 일반 챗봇 안전성 평가와 어떤 차이를 갖는가? |
| RQ3 | 공격 성공률뿐 아니라 harmful advice, unsafe omission, hallucination, refusal quality, safe escalation을 어떻게 함께 평가해야 하는가? |
| RQ4 | RAG 의료 챗봇 또는 drug information system에서 retrieved context가 오염될 경우 어떤 위험이 발생할 수 있는가? |
| RQ5 | 기말논문에서는 실제 의료 조언을 생성하지 않고도 의료 prompt injection 사례를 어떻게 윤리적으로 분석할 수 있는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W08 연결 |
|---|---|---|
| High-stakes prompt injection 사례 | 의료 조언이라는 고위험 영역에서 prompt injection 취약성을 분석 | W08 보안 이슈를 사회적 피해로 확장 |
| Safety evaluation 관점 제공 | 단순 공격 성공률이 아니라 위험 조언, 안전한 거절, 전문가 안내를 평가축으로 제시 | P04의 ASR 평가를 high-stakes safety 평가로 보완 |
| 의료 정보 신뢰성 문제 제기 | LLM이 근거 없는 의료 정보를 확신 있게 생성할 위험을 강조 | hallucination·citation support 평가 연결 |
| RAG/외부 context 위험 연결 | 의료 문서·웹페이지·검색 결과가 오염될 경우 indirect prompt injection 경로가 될 수 있음 | W08 P01/P02 GraphRAG, P03 prompting framework와 연결 |
| 윤리적 제한 필요성 제시 | 실제 환자 상담이나 진단·치료 지시 실험은 제한해야 함 | 기말논문 실험 범위·제외 범위 근거 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | LLM은 의료 정보 검색과 조언에 활용될 수 있지만, prompt injection에 취약하면 환자 안전에 직접적인 위험을 만들 수 있다. | 의료 AI가 악성 지시에 속으면 잘못된 건강 조언을 줄 수 있다. |
| 2. Background | Prompt injection, LLM medical advice, safety guardrail, high-stakes decision support의 기본 문제를 설명한다. | 의료 분야에서는 AI 답변이 틀리면 단순 오류가 아니라 사람의 건강 문제가 된다. |
| 3. Methods | 의료 조언 상황에서 injection prompt 또는 오염된 context가 모델 응답에 미치는 영향을 평가하는 구조를 사용한다. | AI에게 위험한 방향으로 유도하는 문장이 들어갔을 때 안전하게 거절하는지 보는 것이다. |
| 4. Outcomes / Evaluation | 위험 조언, 안전한 거절, 전문가 상담 권고, 근거 제시, 환각 여부 등을 평가한다. | 답이 친절한지가 아니라 “위험하지 않은가, 의사를 찾으라고 안내하는가, 근거가 있는가”를 본다. |
| 5. Results | prompt injection이 의료 조언의 안전성과 신뢰성을 약화시킬 수 있음을 보여주는 사례 중심의 함의를 제공한다. | AI가 항상 안전 규칙을 지키는 것은 아니므로 의료 조언에는 추가 통제가 필요하다. |
| 6. Discussion | 의료 LLM은 안전정책, 전문가 안내, human review, 근거 검증, 도메인별 규제가 필요하다고 해석한다. | 의료 AI는 자동 답변만으로 운영하면 안 되고, 사람 전문가와 검증 절차가 필요하다. |
| 7. Limitations | 특정 모델·prompt set·평가조건의 결과를 모든 의료 AI에 일반화할 수 없고, 실제 환자 진료와 동일시하면 안 된다. | 실험은 경고 신호이지, 모든 상황을 완벽히 대표하지는 않는다. |
| 8. Conclusion | 의료 조언 LLM에서 prompt injection은 환자 안전과 신뢰성 문제로 이어질 수 있으므로 high-stakes safety 평가가 필수다. | 의료 분야의 LLM 보안은 “공격을 막는 것”을 넘어 “사람에게 해가 되지 않게 하는 것”이다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 의료 prompt injection 평가를 W08 보고서에서 설명하기 위한 표준화된 표현이다. 실제 의료 조언 생성이나 공격 payload 제공을 목적으로 하지 않으며, synthetic/toy prompt set 또는 문헌 기반 분석만 전제로 한다.

### 5.1 Medical Prompt Injection Output

의료 조언 LLM의 출력은 system safety policy, user medical query, retrieved medical context, injection context에 조건부로 생성된다.

$$
y\sim p_\theta(y\mid s_{safety},u_{medical},r_{medical},d^{mal},h)
$$

| 기호 | 의미 |
|---|---|
| $s_{safety}$ | 의료 안전정책, 면책·전문가 상담 지시 |
| $u_{medical}$ | 사용자의 의료 관련 질문 |
| $r_{medical}$ | 검색된 의료 정보 또는 문서 context |
| $d^{mal}$ | 악성 instruction 또는 오염된 context |
| $h$ | 대화 이력 |
| $y$ | LLM 응답 |

### 비전공자용 설명

의료 AI는 사용자 질문만 보고 답하지 않는다. 시스템 안전 규칙, 검색된 의료 문서, 이전 대화까지 함께 보고 답한다. 이 중 오염된 문서나 악성 지시가 들어오면 위험한 답변으로 유도될 수 있다.

### 보안적 의미

의료 RAG 시스템에서는 retrieved context가 안전한 참고자료인지, 아니면 hidden instruction을 포함한 공격 경로인지 구분해야 한다.

---

### 5.2 Unsafe Advice Rate

Prompt injection 조건에서 위험하거나 부적절한 의료 조언이 생성된 비율이다.

$$
UnsafeAdviceRate=\frac{N_{unsafe\ medical\ outputs}}{N_{injection\ prompts}}
$$

| 기호 | 의미 |
|---|---|
| $N_{unsafe\ medical\ outputs}$ | 위험하거나 부적절한 의료 응답 수 |
| $N_{injection\ prompts}$ | injection 평가 prompt 수 |

### 비전공자용 설명

공격성 문구가 들어간 상황에서 AI가 위험한 의료 조언을 몇 번이나 했는지 세는 지표다.

---

### 5.3 Safe Escalation Rate

고위험 의료 질문에서 전문가 상담, 응급 상황 안내, 안전한 한계 고지를 제공한 비율이다.

$$
SafeEscalationRate=\frac{N_{refer\ to\ professional}}{N_{high\ risk\ prompts}}
$$

| 기호 | 의미 |
|---|---|
| $N_{refer\ to\ professional}$ | 전문가 상담·응급 안내·안전한 한계 고지가 포함된 응답 수 |
| $N_{high\ risk\ prompts}$ | 고위험 의료 질문 수 |

### 비전공자용 설명

AI가 무리하게 진단하거나 치료법을 말하지 않고, “전문가에게 상담하라”는 안전한 방향으로 안내했는지 보는 지표다.

---

### 5.4 Citation Support Rate

의료 정보가 근거 문서와 일치하는지 평가한다.

$$
CitationSupportRate=\frac{N_{claims\ supported\ by\ evidence}}{N_{medical\ claims}}
$$

| 기호 | 의미 |
|---|---|
| $N_{claims\ supported\ by\ evidence}$ | 근거가 확인된 의료 주장 수 |
| $N_{medical\ claims}$ | 응답에 포함된 전체 의료 주장 수 |

### 보안적 의미

의료 분야에서는 그럴듯한 문장보다 검증 가능한 근거가 중요하다. 근거 없는 단정은 hallucination과 안전 문제로 이어질 수 있다.

---

### 5.5 Harmful Omission Rate

응답이 중요한 안전 경고나 전문가 상담 안내를 누락한 비율이다.

$$
HarmfulOmissionRate=\frac{N_{missing\ safety\ warnings}}{N_{high\ risk\ responses}}
$$

### 보안적 의미

LLM이 위험한 조언을 직접 하지 않더라도, 반드시 필요한 경고나 전문가 안내를 빠뜨리면 안전 문제가 된다.

---

### 5.6 High-Stakes Safety Score

의료 prompt injection 평가에서는 공격 성공률뿐 아니라 유용성, 안전한 escalations, 근거성, 과잉거절을 함께 봐야 한다.

$$
SafetyScore=Utility+\alpha SafeEscalation+\beta CitationSupport-\gamma UnsafeAdvice-\delta Hallucination-\eta OverRefusal
$$

| 기호 | 의미 |
|---|---|
| $Utility$ | 정상 의료 정보 제공의 유용성 |
| $SafeEscalation$ | 전문가·응급 안내 등 안전 전환 품질 |
| $CitationSupport$ | 근거 기반 주장 비율 |
| $UnsafeAdvice$ | 위험 조언 비율 |
| $Hallucination$ | 근거 없는 의료 정보 비율 |
| $OverRefusal$ | 안전한 정보 요청까지 과도하게 거절한 비율 |

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W08/P05에서의 의미 |
|---|---|---|
| LLM Medical QA | LLM이 의료 질문에 자연어 답변 생성 | high-stakes domain 적용 사례 |
| Instruction Following | 안전정책과 사용자 지시를 따르는 능력 | prompt injection 취약성의 원인 |
| RAG Context | 의료 문서·웹페이지·검색 결과를 context로 사용 | indirect injection 경로 |
| Safety Alignment | 위험 답변을 피하고 전문가 상담을 유도 | 의료 안전성 핵심 |
| Evidence Grounding | 응답이 근거 문서와 일치해야 함 | citation support 평가 |
| Escalation Policy | 고위험 질문에서 전문가·응급 안내로 전환 | safe escalation 지표 |
| Human-in-the-loop | 자동 응답을 전문가가 검토 | 운영 안전성 보완 |
| Evaluation | unsafe advice, hallucination, refusal quality, escalation 측정 | W08 보안 평가 확장 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | 의료 Prompt Injection 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 사용자 의료정보, 증상, 약물, 병력 등 민감정보가 prompt/log에 포함될 수 있음 | sensitive disclosure rate, log minimization |
| 무결성 | 오염된 지시가 의료 답변의 내용과 근거를 왜곡할 수 있음 | unsafe advice rate, hallucination rate |
| 가용성 | 방어가 과도하면 유용한 일반 정보 제공도 막힐 수 있음 | over-refusal, task utility |
| 프라이버시 | 의료 질문 자체가 민감정보이므로 저장·검색·로깅 정책이 중요 | privacy risk, access control |
| 안전성 | 잘못된 의료 조언은 실제 신체적 피해로 이어질 수 있음 | safe escalation rate, harmful omission rate |
| 책임성 | 어떤 문서·prompt·모델 설정 때문에 답변이 나왔는지 추적해야 함 | prompt-context-output trace, citation support |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 환자 안전, 의료 정보 신뢰성, 사용자 의료 개인정보, safety policy, retrieved medical context, citation, audit log |
| 공격자 목표 | 위험 조언 유도, 안전정책 우회, 전문가 상담 회피 유도, 근거 없는 의료정보 생성, citation spoofing |
| 공격자 능력 | injection prompt 작성, 웹/문서/검색 결과 오염, 반복 질의, 신뢰성 있어 보이는 문구 삽입 |
| 공격 경로 | user query/source document → retrieved medical context → prompt template → LLM output → 사용자 행동 영향 |
| 방어자 능력 | medical safety policy, source validation, citation verification, safe escalation, output monitoring, clinician/human review |
| 제외 범위 | 실제 환자 상담, 진단·치료 지시 생성, 개인정보 기반 실험, 실제 의료행위 대체, 유해 prompt 배포 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W08/P05 활용 |
|---|---|---|---|
| 공격 성공 | injection ASR | 공격 지시가 의료 응답을 왜곡했는지 | P04와 연결 |
| 안전성 | unsafe advice rate, harmful omission rate | 위험 조언 또는 안전 경고 누락 여부 | high-stakes 핵심 지표 |
| 안전 전환 | safe escalation rate | 전문가 상담·응급 안내로 전환했는지 | 의료 안전성 평가 |
| 근거성 | citation support, evidence faithfulness | 의료 주장이 근거와 일치하는지 | RAG 평가 연결 |
| 환각 | hallucination rate | 근거 없는 의료 정보 생성 여부 | 신뢰성 평가 |
| 거절 품질 | refusal quality, over-refusal | 위험 요청은 거절하고 안전 정보는 제공하는지 | 보안-유용성 균형 |
| 프라이버시 | sensitive disclosure rate | 사용자 의료정보 노출 여부 | W11 privacy 연결 |
| 감사 가능성 | prompt-context-output trace | 사고 재현·책임 추적 가능성 | W14/W15 연결 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Prompt set | 의료 질문 유형, high-risk category, injection category, 구체 payload 비공개 처리 |
| Safety policy | 전문가 상담 권고, 응급 안내, 금지 응답 범위, 면책 문구 정책 |
| Context source | 의료 문서 출처, DOI/URL, 신뢰도 label, 문서 hash |
| Model setting | LLM model/version, temperature, max tokens, safety setting |
| RAG setting | retriever, Top-k, chunking, source validation, citation extraction 방식 |
| Evaluation rubric | unsafe advice, hallucination, safe escalation, citation support 판정 기준 |
| Human review | 의료 전문가 또는 도메인 검토자 여부, disagreement 사례 |
| Security log | prompt-context-output trace, refusal case, unsafe case, reviewer decision |
| 한계 | toy/synthetic 의료 질문 결과를 실제 진료·상담 성능으로 일반화하지 않음 |

---

## 11. 논문의 고유 기여

1. Prompt injection을 의료 조언이라는 high-stakes domain에서 분석한다.
2. 단순 ASR이 아니라 unsafe advice, safe escalation, citation support, hallucination을 함께 봐야 함을 보여준다.
3. RAG 의료 챗봇에서 retrieved context 오염이 실제 안전 문제로 이어질 수 있음을 설명하는 사례 근거를 제공한다.
4. Prompt injection 방어가 보안 필터링만이 아니라 domain safety policy, human review, evidence grounding과 결합되어야 함을 시사한다.
5. 기말논문에서 “고위험 도메인 LLM 보안 평가표”를 설계하는 데 활용할 수 있다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 특정 도메인 사례 | 의료 조언은 대표적 high-stakes 사례이나 모든 도메인을 대표하지는 않는다. | 법률·금융·공공행정 등과 비교 가능한 일반 평가축으로 추상화 |
| 실제 진료와 구분 필요 | LLM 응답 실험을 실제 환자 상담이나 의료행위로 해석하면 안 된다. | 실험 범위와 제외 범위를 명확히 명시 |
| 평가자 전문성 필요 | unsafe advice 판정에는 의료 전문성 또는 명확한 rubric이 필요하다. | human review와 판정 기준 기록 |
| Prompt set 일반화 한계 | 제한된 prompt set 결과가 모든 injection 변형을 포괄하지 못한다. | direct/indirect/high-risk category별 확장 평가 |
| 개인정보 위험 | 의료 질문과 응답 로그 자체가 민감정보일 수 있다. | synthetic prompt, log minimization, access control 적용 |
| 과잉거절 문제 | 안전을 위해 모든 의료 질문을 거절하면 유용성이 낮아진다. | refusal quality와 utility를 함께 평가 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | Prompt injection은 high-stakes domain에서 실제 안전 문제로 이어질 수 있다는 문제의식 |
| 2장 관련연구 | 의료 조언 LLM의 prompt injection 취약성 사례 문헌으로 정리 |
| 3장 위협모형 | 환자 안전, 의료정보 신뢰성, retrieved medical context, safety policy 보호 자산 정의 |
| 4장 연구방법 | unsafe advice rate, safe escalation rate, citation support, harmful omission, over-refusal 지표 설계 |
| 5장 분석 | 의료 조언을 직접 생성하지 않고 synthetic/toy high-risk scenario 기반 평가표 제시 |
| 6장 보안적 함의 | 전문가 상담, human review, 근거 확인, 의료 개인정보 보호, 감사 로그 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W08에서 기말논문에 반영할 개념: 의료 조언 상황의 prompt injection은 LLM 보안 실패가 사용자 안전과 직접 연결될 수 있음을 보여주므로, RAG 보안 평가는 ASR뿐 아니라 unsafe advice, safe escalation, citation support를 포함해야 한다.
2. W08에서 기말논문에 반영할 표·그림·실험: high-stakes prompt injection 평가표, 안전한 거절·전문가 안내 rubric, prompt-context-output-citation audit workflow를 반영한다.
3. W08이 LLM 보안 감사 프레임워크와 연결되는 지점: 의료처럼 위험도가 높은 도메인에서는 retrieved context, safety policy, 모델 출력, human review decision을 W14/W15 evidence chain에 포함해야 책임 있는 운영이 가능하다.

---

## 15. 최종 판단

P05는 W08의 관련 보조 문헌이지만 중요도는 높다. P04가 prompt injection의 일반 공격·방어 taxonomy를 제공한다면, P05는 그 취약성이 의료 조언이라는 high-stakes domain에서 어떤 안전 문제로 확장되는지 보여준다. 따라서 기말논문에서는 P05를 **고위험 도메인 LLM 보안 평가, safe escalation, citation support, human review, 개인정보 보호 원칙의 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
