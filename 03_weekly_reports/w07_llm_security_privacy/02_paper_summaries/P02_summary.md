# 논문 요약: P02

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문명 | Security and Privacy Challenges of Large Language Models: A Survey |
| 저자 | Badhan Chandra Das, M. Hadi Amini, Yanzhao Wu |
| 출판정보 | ACM Computing Surveys, 57(6), pp. 1-39, 2025 |
| DOI/URL | `https://doi.org/10.1145/3712001`; arXiv `https://arxiv.org/abs/2402.00888` |
| 검증 상태 | ACM CSUR 2025 출판판 확인. 강의계획서의 `Ankur Das et al.` 표기는 공식 저자명과 불일치하여 확인 필요 |

## 2. 한 문장 요약

LLM 보안·프라이버시 연구는 jailbreak, prompt injection, data poisoning, PII leakage, privacy attack, 방어 메커니즘을 학습·추론·응용 단계별로 분류한다[2].

## 3. 연구문제

LLM이 보편적 인터페이스가 되면서 어떤 보안·프라이버시 취약성이 발생하고, 이를 어떤 공격과 방어 범주로 체계화할 수 있는가를 다룬다.

## 4. 핵심 개념

- Security challenge: jailbreak, prompt injection, data poisoning, model misuse.
- Privacy challenge: PII leakage, memorization, membership inference, training data exposure.
- Defense mechanism: filtering, alignment, privacy-preserving learning, monitoring, governance.

## 5. 보안 관점 분석

P02는 W07 위협모형에서 protected assets와 attack category를 정리하는 핵심 근거다. 다만 공격 절차를 재현하지 않고, 보고서에서는 synthetic prompt category와 추상 지표로만 ASR, privacy leakage, refusal quality를 설명한다.

## 6. 검증 메모

현재 P02는 arXiv:2402.00888 및 ACM CSUR DOI `10.1145/3712001` 기준으로 확인했다. 강의계획서의 `Ankur Das et al.` 표기는 공식 메타데이터의 `Badhan Chandra Das et al.`과 다르므로 최종 제출 전 확인 필요 상태를 유지한다.

## 7. 기말 논문 활용

LLM/RAG 시스템의 threat taxonomy, privacy leakage 평가축, defense category를 설계할 때 기본 분류표로 활용한다.
