# W07 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | 보안 위협 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 | LLM은 무엇을, 어디서, 어떻게 평가해야 하는가 | 평가 task·benchmark·방법론 survey | LLM evaluation benchmark와 사례 정리 | benchmark contamination, evaluation reliability | task score, benchmark coverage, risk evaluation | 실제 보안 공격 실험보다 평가 분류 중심 | LLM/RAG 보안 평가의 evaluation axis |
| P02 | LLM 보안·프라이버시 공격과 방어는 어떻게 분류되는가 | security/privacy challenge survey | arXiv/PDF 기준 문헌조사 | jailbreak, data poisoning, PII leakage | attack/defense category, risk domain | 로컬 PDF의 DOI가 임시값이라 출판정보 재검증 필요 | 위협모형과 방어 가정 |
| P03 | LLM은 보안에 어떻게 기여하고, 어떤 공격·취약성을 만드는가 | good/bad/ugly taxonomy | 281편 문헌 분류 | offensive use, inherent vulnerability, prompt injection | taxonomy, attack surface, defense opportunity | arXiv/PDF 기준 확인, 출판정보 재검증 필요 | 공격-방어-평가 연결표 |
| P04 | MLLM 구조와 평가, hallucination 문제는 어떻게 정리되는가 | MLLM architecture/training/evaluation survey | MLLM 연구 흐름과 benchmark 정리 | multimodal hallucination, multimodal prompt risk | MLLM capability/evaluation categories | 공식 권호/DOI 재검증 필요 | multimodal LLM 확장 위험 |
| P05 | LLM은 software security workflow에 어떻게 쓰이는가 | software testing/analysis survey | fuzzing, unit test, repair, bug detection, triage 분석 | insecure code generation, bug analysis failure | vulnerability rate, repair quality, triage quality | 실제 code benchmark 실험은 별도 필요 | code LLM 보안 평가 항목 |

## 종합 비교

### 1. 공통적으로 다루는 문제

다섯 편은 모두 “LLM을 어떻게 믿을 것인가”라는 문제로 모인다. P01은 평가 신뢰성, P02/P03은 보안·프라이버시 위협, P04는 multimodal 확장, P05는 software security 접점을 제공한다.

### 2. 논문 간 차이점

P01은 모델 능력 평가의 체계를 제공하고, P02/P03은 공격·방어 분류를 제공한다. P04는 이미지 등 복수 modality가 추가될 때 context와 hallucination 문제가 확장됨을 보여주며, P05는 LLM output이 코드 산출물로 이어질 때 별도 보안 평가가 필요함을 보여준다.

### 3. 아직 해결되지 않은 문제

Benchmark contamination, prompt leakage, refusal quality, code vulnerability risk를 한 평가표에 넣는 표준 절차는 아직 분산되어 있다. 또한 문헌 survey의 분류체계를 실제 모델 평가 프로토콜로 바꾸려면 prompt set, 라벨링 기준, 복수 모델, 복수 seed가 필요하다.

### 4. 기말 논문 주제로 발전 가능한 연결부

W07는 “LLM/RAG 기반 AI 시스템의 보안·프라이버시·재현성 평가 프레임워크”의 핵심 주차로 활용할 수 있다. 특히 utility, ASR, privacy leakage, refusal quality, over-refusal, code vulnerability rate를 함께 기록하는 평가표가 기말논문의 방법론 초안이 된다.
