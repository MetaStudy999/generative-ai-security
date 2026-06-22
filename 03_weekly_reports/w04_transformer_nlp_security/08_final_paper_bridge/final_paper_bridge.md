# W04 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 프롬프트 기반 AI 시스템의 민감정보 보호 평가체계 | LLM 프롬프트 시스템 | 프롬프트 프라이버시, ICL leakage | 문헌분석/체크리스트/synthetic 사례 | 높음 |
| 2 | NLP 단어 치환 공격에 대한 privacy-risk 탐지 평가 | 키워드 또는 경량 NLP 탐지기 | 단어 치환 우회 | toy 실험/ASR 측정 | 보통 |
| 3 | Efficient Transformer 환경의 보안 평가 비용과 재현성 연구 | 긴 입력 NLP 시스템 | 긴 프롬프트 평가 비용, 로그 누락 | 문헌 비교/재현성 프로토콜 | 보통 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | 프롬프트 기반 AI 시스템에서 성능, 민감정보 보호, 로그 책임성을 함께 평가해야 하는 이유 |
| 관련연구 | Efficient Transformer, NLP adversarial defense, prompt privacy, privacy-preserving prompt engineering |
| 연구문제 | 단어 치환 우회, 프롬프트 마스킹, utility 보존을 함께 묻는 평가 질문 |
| 연구방법 | 문헌 비교표, 위협모형, clean/ASR/leakage/utility 평가 프로토콜 |
| 분석/실험 | W04 synthetic toy 실험: Clean 1.000000, Word substitution ASR 0.750000, Prompt masking leakage 0.000000 |
| 보안적 함의 | Confidentiality, Privacy, Accountability 관점에서 프롬프트 입력·응답·로그 통제 |
| 결론 | 프롬프트 민감정보 보호를 위한 재현 가능한 AI 보안 평가체계 제안 |
