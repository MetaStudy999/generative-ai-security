# Dataset Card: Synthetic RAG Security Dataset 100

## 개요

- 파일: [rag_security_dataset_100.csv](/home/ubuntu/generative-ai-security/data/rag_security_dataset_100.csv)
- 목적: 기업용 RAG 기반 생성형 AI 챗봇의 문서 오염, 간접 프롬프트 인젝션, 민감정보 노출, 출처 충돌, 오래된 정책, 환각 유도 문서를 안전하게 모의 평가한다.
- 규모: 100개 문서
- 생성일: 2026-06-23
- 성격: 전량 synthetic 데이터

## 구성

| 문서 유형 | 개수 |
|---|---:|
| normal | 20 |
| indirect_prompt_injection | 20 |
| privacy_leakage | 20 |
| source_conflict | 15 |
| outdated_policy | 15 |
| hallucination_trigger | 10 |
| 합계 | 100 |

## 안전 원칙

- 실제 개인정보, 실제 고객명, 실제 사번, 실제 전화번호, 실제 이메일, 실제 계정 정보는 포함하지 않는다.
- API 키와 토큰은 모두 `SYNTH_*_PLACEHOLDER_NOT_REAL` 형식의 가짜 문자열이다.
- 프롬프트 인젝션 문서는 공격 절차 재현이 아니라 방어 평가용 위험 신호로만 작성했다.
- 기업명, 서비스명, 사람 이름은 모두 가상 또는 일반명으로 처리했다.

## 한계

- 실제 운영 RAG 시스템의 검색기, 임베딩 모델, LLM 응답을 직접 평가하지 않는다.
- 문서 텍스트는 rule-based baseline 비교에 적합하도록 구성되어 있어 실제 문서 분포보다 단순하다.
- 실험 결과는 이 synthetic 데이터셋과 명시된 규칙 기반 판정기의 성능이며, 실제 기업 시스템 보안 성능으로 일반화하면 안 된다.
