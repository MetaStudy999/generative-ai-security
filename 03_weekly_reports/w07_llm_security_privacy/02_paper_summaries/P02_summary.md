# 논문 요약: P02

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문명 | Security and Privacy Challenges of Large Language Models: A Survey |
| 저자 | Badhan Chandra Das, M. Hadi Amini, Yanzhao Wu |
| 출판정보 | ACM Computing Surveys, 57(6), pp. 1-39, 2025 |
| DOI/URL | `https://doi.org/10.1145/3712001`; arXiv `https://arxiv.org/abs/2402.00888` |
| 검증 상태 | ACM CSUR 2025 출판판 확인. 강의계획서의 `Ankur Das et al.` 표기는 공식 저자명과 표기가 달라 확인 필요 |

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

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | LLM Security Risk Score |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$Risk=\alpha ASR+\beta Leakage+\gamma VulnRate-\lambda Utility$$ |
| 기호·입력·출력 | ASR: 정책 실패율, Leakage: 민감정보 노출률, VulnRate: 취약 코드 비율, Utility: 정상 유용성 |
| 직관적 의미 | LLM Security Risk Score는 LLM 보안·프라이버시 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | LLM 보안·프라이버시 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | ASR, privacy leakage, code vulnerability rate, refusal quality |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 검증 메모

현재 P02는 arXiv:2402.00888 및 ACM CSUR DOI `10.1145/3712001` 기준으로 확인했다. 강의계획서의 `Ankur Das et al.` 표기는 공식 메타데이터의 `Badhan Chandra Das et al.`과 다르므로 최종 제출 전 확인 필요 상태를 유지한다.

## 7. 기말 논문 활용

LLM/RAG 시스템의 threat taxonomy, privacy leakage 평가축, defense category를 설계할 때 기본 분류표로 활용한다.
