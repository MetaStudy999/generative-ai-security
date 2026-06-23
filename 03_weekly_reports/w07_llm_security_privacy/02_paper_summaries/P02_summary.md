# P02 Summary

## Security and Privacy Challenges of Large Language Models: A Survey — Badhan Chandra Das, M. Hadi Amini, Yanzhao Wu, ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W07 LLM 보안·프라이버시 |
| 논문명 | Security and Privacy Challenges of Large Language Models: A Survey |
| 저자 | Badhan Chandra Das, M. Hadi Amini, Yanzhao Wu |
| 출판 정보 | ACM Computing Surveys, 57(6), pp. 1–39, 2025 |
| DOI | https://doi.org/10.1145/3712001 |
| 보조 URL | https://arxiv.org/abs/2402.00888 |
| 검증 상태 | W07 `paper_list.md` 기준 공식 DOI 확인. 강의계획서의 `Ankur Das` 표기 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 LLM의 보안·프라이버시 문제를 **prompt injection, jailbreaking, data leakage, memorization, model extraction, poisoning, backdoor, misuse, defense, governance** 관점에서 정리하는 W07의 핵심 보안 survey 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | LLM 보안 위협은 입력, 학습, 추론, 출력, 배포 단계에서 어떻게 발생하는가? |
| RQ2 | Prompt injection과 jailbreak는 시스템 지시와 안전정책을 어떻게 우회하는가? |
| RQ3 | Memorization과 privacy leakage는 어떤 데이터 보호 문제를 만드는가? |
| RQ4 | 방어자는 policy, filtering, monitoring, red teaming, audit log를 어떻게 설계해야 하는가? |

---

## 3. 핵심 수식·지표

### 3.1 Jailbreak/공격 성공률

$$
ASR=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[f_\theta(p_i^{attack})\in Y_{unsafe}]
$$

### 3.2 Leakage Rate

$$
LeakageRate=\frac{N_{sensitive\ output}}{N_{privacy\ risk\ prompts}}
$$

### 보안 해석

LLM 보안은 단일 취약점이 아니라 입력-모델-도구-출력-로그 전반의 시스템 리스크다. 공격 성공률, leakage, over-refusal, utility를 함께 보고해야 한다.

---

## 4. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | system prompt, user data, training data, model weights, tool credentials, output log |
| 공격자 목표 | 정책 우회, 민감정보 추출, 악성 응답 유도, 도구 오남용 |
| 공격자 능력 | adversarial prompt, repeated query, indirect prompt injection, context stuffing |
| 제외 범위 | 실제 서비스 공격, 개인정보 포함 실험, 악성코드 실행 |

---

## 5. 평가방법 및 재현성

| 지표 | 의미 |
|---|---|
| ASR | jailbreak/prompt injection 성공률 |
| Leakage Rate | 민감정보 노출률 |
| Refusal Quality | 위험 요청 거절 품질 |
| Over-refusal | 정상 요청 과차단률 |
| Utility | 정상 작업 성능 |
| Auditability | prompt-output-tool log 보존 |

---

## 6. 기말논문 연결

P02는 기말논문의 LLM 보안 위협모형 중심 문헌으로 사용한다. W08 RAG 보안에서는 indirect prompt injection과 retrieved context poisoning으로 확장하고, W14에서는 운영 감사와 정책 준수 로그로 확장한다.

---

## 7. 최종 판단

P02는 W07의 직접 보안 핵심 문헌이다. P01의 평가체계와 결합해 LLM 보안 평가표를 구성한다.
