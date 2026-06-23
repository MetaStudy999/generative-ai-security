# W07 100점형 통합 Summary

## LLM 보안·프라이버시

## 0. 문서 목적

이 문서는 W07 개별 논문 summary 5개를 기말논문 작성용 연구 노트로 통합한 100점형 요약본이다. LLM 평가, 보안·프라이버시, 멀티모달 LLM, 소프트웨어 보안 응용을 하나의 위협모형과 평가체계로 묶는다.

---

## 1. 한 문장 통합 요약

W07은 LLM을 **평가 대상, 보안 도구, 공격 대상, 프라이버시 위험, 멀티모달 시스템, 소프트웨어 보안 자동화 도구**로 동시에 바라보고, utility, safety, privacy, robustness, tool risk, auditability를 분리해 평가해야 함을 정리하는 주차다.

---

## 2. 문헌 5편 통합 매트릭스

| ID | 논문 | 핵심 역할 | 주요 지표 |
|---|---|---|---|
| P01 | LLM Evaluation Survey | LLM 평가 taxonomy | hallucination, factuality, safety, benchmark score |
| P02 | LLM Security & Privacy Challenges | 직접 보안 위협모형 | ASR, leakage rate, refusal quality |
| P03 | LLM Security & Privacy: Good/Bad/Ugly | dual-use와 관련 보조 taxonomy | misuse risk, defense coverage |
| P04 | Multimodal LLM Survey | 시각·텍스트 결합 공격면 | visual jailbreak ASR, grounding accuracy |
| P05 | Software Security Meets LLM | 코드·보안 자동화 응용 | vulnerability rate, secure fix rate, secret leakage |

---

## 3. 핵심 수식 묶음

$$
HallucinationRate=\frac{N_{unsupported}}{N_{answers}}
$$

$$
ASR=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[f_\theta(p_i^{attack})\in Y_{unsafe}]
$$

$$
LeakageRate=\frac{N_{sensitive\ output}}{N_{privacy\ risk\ prompts}}
$$

$$
SecureCodeScore = Utility_{code} - \lambda VulnRate - \mu LeakageRisk
$$

---

## 4. 통합 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | system prompt, user prompt, training data, output, tool credential, code, log, visual input |
| 공격자 목표 | jailbreak, prompt injection, 민감정보 추출, 허위 응답, 취약 코드 생성 유도 |
| 공격자 능력 | adversarial prompt, context stuffing, repeated query, visual prompt injection, insecure code requirement |
| 방어자 능력 | guardrail, red teaming, prompt filtering, privacy wrapper, audit log, human review |
| 제외 범위 | 실제 서비스 공격, 개인정보 포함 실험, 악성코드 작성, 무단 API 공격 |

---

## 5. 통합 평가 지표

| 평가축 | 대표 지표 | 해석 |
|---|---|---|
| Utility | task score, pass@k, VQA accuracy | 정상 기능 성능 |
| Safety | refusal quality, harmful response rate | 정책 준수 |
| Robustness | jailbreak ASR, prompt injection ASR | 공격 저항성 |
| Privacy | leakage rate, secret leakage | 민감정보 보호 |
| Factuality | hallucination rate, citation support | 근거 기반 응답 |
| Multimodal | grounding accuracy, visual jailbreak ASR | 이미지-텍스트 보안 |
| Auditability | prompt-output-tool log completeness | 사후 검증 가능성 |

---

## 6. 재현성 체크리스트

| 항목 | 필수 기록 |
|---|---|
| 모델 | 모델명, 버전, temperature, decoding 설정 |
| 프롬프트 | clean, attack, privacy-risk, visual prompt set 분리 |
| 도구 | tool schema, 권한, 호출 로그 |
| 평가 | ASR, leakage, refusal, over-refusal, utility, hallucination |
| 한계 | toy prompt 결과를 실제 LLM 안전성 보증으로 일반화 금지 |

---

## 7. 기말논문 연결 3문장

1. W07에서 기말논문에 반영할 개념: LLM 보안 평가는 입력·출력만이 아니라 system prompt, 도구 호출, 로그, 멀티모달 입력, 코드 생성까지 포함해야 한다.
2. 반영할 표·그림·실험: LLM threat model, ASR/leakage/hallucination 수식, multimodal/tool/code security 평가표를 반영한다.
3. W08/W14 연결: RAG와 MLOps에서는 검색 문서·도구 권한·감사 로그가 결합되므로 W07의 LLM 보안 지표를 운영 보안 프레임으로 확장한다.

---

## 8. 최종 판단

W07은 후속 W08 RAG/Prompt Injection, W14 MLOps, W15 종합평가의 핵심 기반이다. P01은 평가체계, P02/P03은 보안·프라이버시, P04는 멀티모달 확장, P05는 소프트웨어 보안 응용을 담당한다.
