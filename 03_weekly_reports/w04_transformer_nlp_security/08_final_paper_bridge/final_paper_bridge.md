# W04 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 프롬프트 기반 AI 시스템의 민감정보 보호 평가체계 | LLM 프롬프트 시스템 | prompt privacy, ICL leakage | 문헌분석 + synthetic prompt toy protocol | 높음 |
| 2 | NLP 단어 치환 공격에 대한 privacy-risk 탐지 평가 | 키워드 또는 경량 NLP 탐지기 | word substitution 우회 | clean/ASR 분리 평가 | 보통 |
| 3 | Efficient Transformer 환경의 보안 평가 비용과 재현성 연구 | 긴 입력 NLP/LLM 시스템 | 긴 프롬프트 평가 비용, 로그 누락 | 문헌 비교 + 재현성 프로토콜 | 보통 |

## 2. 추천 최종 주제

- 국문: 프롬프트 기반 AI 시스템의 민감정보 보호 평가체계 연구
- 영문: A Study on an Evaluation Framework for Sensitive Information Protection in Prompt-Based AI Systems

## 3. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | 프롬프트 기반 AI 시스템에서 성능, 민감정보 보호, 로그 책임성을 함께 평가해야 하는 이유 |
| 관련연구 | Efficient Transformer, faster/lighter Transformer, Transformer taxonomy, NLP adversarial robustness, prompt privacy |
| 연구문제 | 단어 치환 우회, 프롬프트 마스킹, utility 보존을 함께 묻는 평가 질문 |
| 위협모형 | prompt input, ICL examples, model output, logs, tool-call arguments, user intent |
| 연구방법 | 문헌 비교표, threat model, clean/ASR/leakage/utility/reproducibility 평가 프로토콜 |
| 분석/실험 | W04 synthetic toy 실험: Clean 1.000000, Word substitution ASR 0.750000, Prompt masking leakage 0.000000 |
| 보안적 함의 | Confidentiality, Integrity, Privacy, Utility, Accountability, Reproducibility |
| 결론 | 프롬프트 민감정보 보호를 위한 재현 가능한 AI 보안 평가체계 제안 |

## 4. KCI 전환 메모

KCI형 원고는 국문 제목, 국문초록, 연구문제, 표 중심 비교, 국내 참고문헌 보강이 필요하다. 현재 국내 참고문헌 3편 이상은 확인 필요 상태이다.

## 5. SCI 전환 메모

SCI형 원고는 structured abstract, limitations/threats to validity, reproducibility evidence, related work 축을 강화해야 한다. W04 수치는 실제 LLM 성능 주장이 아니라 toy protocol demonstration으로 제한해야 한다.

## 6. 검증 필요 항목

| 항목 | 상태 |
|---|---|
| P01/P02/P04/P05 ACM Article 번호 | 확인 필요 |
| P04 강의자료 `N. Goyal` 표기 | 확인 필요 |
| 국내 참고문헌 | 확인 필요 |
| 공개 GitHub PDF 원문 보관 | 삭제 또는 비공개 전환 검토 필요 |
