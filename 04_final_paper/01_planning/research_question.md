# 연구문제

## 1. 연구 배경

생성형 AI와 LLM 기반 응용은 학습데이터, 프롬프트, 검색 문서, 평가셋, 배포 파이프라인이 서로 연결된 생명주기형 시스템이다. 기존 보안 논의는 공격 유형을 잘 분류하지만, 실제 연구 보고서에서 성능·보안성·프라이버시·재현성을 함께 검증하는 절차는 상대적으로 분산되어 있다.

## 2. 최종 연구문제

> RQ1. LLM/RAG 기반 AI 시스템의 생명주기에서 prompt injection, benchmark contamination, privacy leakage는 각각 어느 단계에서 발생하는가?

> RQ2. AI 보안 연구에서 clean performance, attack impact, privacy leakage, reproducibility를 함께 평가하려면 어떤 공통 평가 항목이 필요한가?

> RQ3. 허위 인용, 실험결과 조작, AI 활용 은폐를 줄이기 위한 참고문헌·실험·AI 고지 체크리스트는 어떻게 구성되어야 하는가?

## 2.1 KCI 제출형 연구문제

> RQ1. LLM/RAG 기반 AI 시스템의 생명주기에서 prompt injection, benchmark contamination, privacy leakage는 어느 단계에서 발생하는가?

> RQ2. AI 보안 연구에서 clean performance, attack impact, leakage, reproducibility, human review를 함께 평가하기 위한 최소 항목은 무엇인가?

> RQ3. 참고문헌 검증표와 AI 활용 고지서는 AI 보안 연구의 재현성과 연구윤리를 어떻게 강화하는가?

## 3. 연구범위

| 항목 | 포함 | 제외 |
|---|---|---|
| 대상 시스템 | LLM, RAG, 평가 파이프라인, 연구용 toy ML 시스템 | 실제 상용 API 무단 공격 |
| 보안 위협 | 프롬프트 인젝션, 평가오염, 프라이버시 누수, 재현성 실패 | 실제 개인정보 추론, 실제 시스템 침해 |
| 데이터 | 공개 문헌, 공개 데이터 또는 synthetic data | 실제 민감정보 |
| 실험 | 설계 중심 toy evaluation, 체크리스트 검증 | 실행하지 않은 결과의 수치화 |
| 방어 방법 | 출처 검증, human approval gate, 재현성 기록, 참고문헌 검증 | 실제 운영 시스템 보안 우회 또는 공격 코드 |

## 4. 연구질문 검토

| 기준 | 점검 내용 | 확인 |
|---|---|---|
| 명확성 | 검토 가능한 질문인가 | ■ |
| 범위 | 한 학기 과제로 가능한 작은 범위인가 | ■ |
| 보안성 | AI 보안 주제와 직접 연결되는가 | ■ |
| 방법론 | 문헌분석, 사례분석, 모의실험, 체크리스트 중 하나로 수행 가능한가 | ■ |
| 기여 | 기존 연구와 구별되는 기여가 있는가 | ■ |
