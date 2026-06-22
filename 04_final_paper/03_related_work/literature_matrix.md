# 관련연구 비교표

| 번호 | 구분 | 논문 제목 | 저자 | 연도 | 연구문제 | 방법론 | 한계 | 본 연구와의 차별점 | DOI/URL 검증 |
|---:|---|---|---|---:|---|---|---|---|---|
| 1 | 국내 | AI 보안 평가·개인정보보호 관련 국내 문헌 최종 선별 예정 | 확인 필요 | 0 | 국내 규제와 AI 보안 평가 맥락 | KCI/DBpia/RISS 검색 예정 | 허위 인용 방지를 위해 확정 전 | 국내 맥락 보완 | 확인 필요 |
| 2 | 국내 | RAG/LLM 보안 또는 정보보호 정책 관련 국내 문헌 최종 선별 예정 | 확인 필요 | 0 | 국내 적용 가능성 | KCI/DBpia/RISS 검색 예정 | DOI/URL 검증 전 | 국내 정책·운영 관점 보완 | 확인 필요 |
| 3 | 국내 | AI 연구윤리·재현성 관련 국내 문헌 최종 선별 예정 | 확인 필요 | 0 | 연구윤리 검증 | KCI/DBpia/RISS 검색 예정 | 세부 서지 미확정 | 연구윤리 장 보완 | 확인 필요 |
| 4 | 해외 | A Survey on Evaluation of Large Language Models | J. Chang et al. | 2024 | LLM 평가 체계 | Survey | 평가 재현성과 오염 위험 별도 정교화 필요 | benchmark contamination을 평가축으로 반영 | 확인 필요 |
| 5 | 해외 | Security and Privacy Challenges of Large Language Models: A Survey | Ankur Das et al. | 2025 | LLM 보안·프라이버시 위협 | Survey | 실제 실험 프로토콜은 별도 설계 필요 | 위협모형 기반 분류에 활용 | 확인 필요 |
| 6 | 해외 | Prompt Injection Attacks on Large Language Models: A Survey of Attack Methods, Root Causes, and Defense Strategies | Tianlei Geng et al. | 2026 | 프롬프트 인젝션 원인과 방어 | Survey | 안전한 모의평가로 제한 필요 | RAG/agent 공격면 분석에 활용 | 확인 필요 |
| 7 | 해외 | Membership inference attacks on machine learning: a survey | Hongsheng Hu et al. | 2022 | 멤버십 추론 위협 | Survey | 실제 개인정보 사용 불가 | privacy leakage 평가축에 활용 | 확인 필요 |
| 8 | 해외 | A Multivocal Literature Review of MLOps Practices | Bayram Eken et al. | 2025 | MLOps 실무와 연구공백 | Multivocal review | 보안 체크리스트와 추가 연결 필요 | 재현성·artifact 관리 기준에 활용 | 확인 필요 |

## 종합 분석

### 1. 국내 연구의 경향

국내 연구는 최종 제출 전 KCI, DBpia, RISS, Google Scholar에서 AI 보안 평가, 개인정보보호, 연구윤리, LLM/RAG 보안 관련 문헌을 확인해 확정한다. 현재 단계에서는 허위 인용 방지를 위해 국내 문헌을 후보 슬롯으로만 둔다.

### 2. 해외 연구의 경향

해외 연구는 LLM 평가, LLM 보안·프라이버시, 프롬프트 인젝션, 멤버십 추론, MLOps 재현성 문헌을 중심으로 축적되어 있다. 각 문헌은 위협 분류에는 강하지만 제출 가능한 재현성·연구윤리 체크리스트까지 통합하지는 않는다.

### 3. 기존 연구의 한계

기존 연구는 공격 유형, 방어 방법, 평가 지표를 각각 잘 정리하지만, prompt injection, benchmark contamination, privacy leakage, reproducibility를 하나의 생명주기 평가표로 묶는 데 한계가 있다.

### 4. 본 연구의 차별점

본 연구는 LLM/RAG 기반 AI 시스템에서 보안 위협과 연구 재현성 문제를 함께 다루며, 참고문헌 검증표와 AI 활용 고지서를 포함한 제출 가능한 평가·통제 프레임워크를 제안한다.
