# W04 Transformer 변형 & NLP 대적공격·프라이버시 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W04 |
| 주제 | Transformer 변형 & NLP 대적공격·프라이버시 |
| AI 원리 | Transformer, X-formers, 효율화, sparse attention |
| 보안 이슈 | NLP 대적공격, 프롬프트 프라이버시, ICL 위험 |
| 문서 상태 | 초안 |

## 1. 한 문장 요약

W04는 Transformer 변형 및 NLP 대적공격/프라이버시를 중심으로 AI 원리와 보안 위협을 함께 정리하고, 기말 논문의 위협모형·평가방법·재현성 설계로 연결한다.

## 2. AI 원리 70% 정리

Transformer, X-formers, 효율화, sparse attention를 이해하기 위해 Transformer 기본 구조, Self-attention과 multi-head attention, Query, Key, Value의 역할, Positional encoding, X-formers와 Efficient Transformer 계열, Sparse attention, low-rank approximation, kernelized attention를 핵심 개념으로 정리했다. 이 원리들은 모델 또는 시스템이 어떤 입력과 학습 구조를 갖고 어떤 기준으로 평가되는지 설명한다.

## 3. 보안 이슈 30% 정리

NLP 대적공격, 프롬프트 프라이버시, ICL 위험를 중심으로 NLP 대적공격, 단어 치환 공격, 문장 재구성 공격, 의미 보존 공격, Prompt privacy, In-context learning 환경의 민감정보 노출를 정리했다. 보안 분석은 공격 절차 자체보다 보호 자산, 공격자 능력, 방어자 가정, 평가 지표를 명확히 하는 방향으로 작성했다.

## 4. 논문 5편 요약

| ID | 논문 | 저자 | 연도 | 검증 상태 |
|---|---|---|---|---|
| P01 | Efficient Transformers: A Survey | Yi Tay et al. | 2022 | arXiv DOI/URL 확인 |
| P02 | A Practical Survey on Faster and Lighter Transformers | Quentin Fournier et al. | 2023 | ACM 출판 DOI 확인 |
| P03 | A survey of transformers | Tianyang Lin et al. | 2022 | AI Open 출판 DOI 확인 |
| P04 | A Survey of Adversarial Defences and Robustness in NLP | Shreya Goyal et al. | 2023 | arXiv DOI/URL 확인 |
| P05 | Privacy Preserving Prompt Engineering: A Survey | Kennedy Edemacu, Xintao Wu | 2024 | arXiv DOI/URL 확인 |

## 5. 논문 5편 비교

다섯 편은 AI 원리 문헌과 보안 문헌을 함께 포함한다. 기말 논문에서는 개별 문헌의 세부 수치보다 분류체계, 위협모형, 평가 프로토콜의 연결 관계를 우선 반영한다.

## 6. Research Track

### 6.1 연구문제

RQ1. Transformer 변형 및 NLP 대적공격/프라이버시의 생명주기에서 보안 보증을 위해 어떤 평가 항목이 필요한가?

RQ2. 단어 치환 기반 NLP 대적공격은 어떤 조건에서 privacy-risk 탐지기를 우회하는가?

RQ3. 성능, 보안성, 재현성을 함께 평가하려면 어떤 최소 프로토콜이 필요한가?

### 6.2 위협모형

대상 시스템은 Transformer 변형 및 NLP 대적공격/프라이버시 기반 AI/ML 시스템이며, 보호 자산은 데이터, 모델, 입력/컨텍스트, 출력, 로그, 평가셋이다. 공격자는 외부 공격자, 내부자, 데이터 제공자, API 남용자 등으로 나뉜다.

### 6.3 평가방법

Clean performance, attack impact, privacy leakage, utility, reproducibility, human review를 기본 평가 항목으로 둔다.

### 6.4 재현성

Docker, pyproject.toml/uv sync, config, seed, 로그, PDF/DOI 검증표를 함께 보존한다. W04 실행 결과는 `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md`에 저장했다.

### 6.5 한계와 오픈문제

P01, P04, P05의 출판사 DOI는 추가 확인 대상이다. 또한 synthetic toy 실험 결과는 실제 Transformer 또는 LLM 강건성 주장으로 일반화할 수 없다.

## 7. 실습 요약

실습은 synthetic privacy-risk prompts 기반으로 실행했다. 실제 개인정보, 실제 서비스 침해, 무단 질의, 악용 가능한 절차는 포함하지 않는다.

| 조건 | Clean Score | Attack Success Rate | Privacy Leakage | Utility Score |
|---|---:|---:|---:|---:|
| Clean baseline | 1.000000 | 해당 없음 | 해당 없음 | 1.000000 |
| Word substitution | 0.625000 | 0.750000 | 해당 없음 | 1.000000 |
| Prompt masking | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 |
| Privacy-preserving prompt | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 |

## 8. AI 활용 기록 요약

Codex를 사용해 문헌 요약 구조화, 실험 코드 작성, 실행 결과 정리, 제출용 문서와 발표자료 작성을 수행했다. AI 활용 내역은 `05_ai_worklog/`에 기록했다.

## 9. 토론 질문

1. Transformer 변형 및 NLP 대적공격/프라이버시에서 가장 중요한 보호 자산은 무엇인가?
2. 공격 성공률과 일반 성능을 함께 볼 때 어떤 지표가 가장 설득력 있는가?
3. 원문 검증과 재현성 기록을 어느 수준까지 제출물에 포함해야 하는가?

## 10. 기말 논문 연결

W04는 기말 논문의 관련연구, 위협모형, 평가방법, 보안적 함의 장에 연결된다.

## 11. 참고문헌 검증표

참고문헌은 `01_papers/doi_check.md`에서 DOI/URL 확인 상태를 관리한다. 출판 DOI와 arXiv DOI를 구분해 기록했다.

## 12. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 완료 |
| 비교표 | 완료 |
| AI 원리 70% | 완료 |
| 보안 이슈 30% | 완료 |
| Research Track | 완료 |
| 실험 결과 조작 방지 | outputs 로그 기준으로만 반영 |
| DOI 임의 생성 방지 | 출판 DOI와 arXiv DOI를 구분 |
| AI 사용 은폐 방지 | AI 활용 고지서 작성 |
