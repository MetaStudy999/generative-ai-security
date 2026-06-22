# W07 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | AI 원리 기여 | 보안 위협 연결 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|---|
| P01 | LLM은 어떤 task와 benchmark로 평가해야 하는가 | LLM evaluation taxonomy, benchmark survey | LLM benchmark와 평가 방법론 문헌 | LLM 평가 프레임워크와 benchmark discipline | benchmark contamination, evaluation leakage, capability-risk mismatch | task score, benchmark coverage, human evaluation, risk evaluation | 강의계획서의 ACM CSUR 표기와 실제 ACM TIST 출판정보 차이 확인 필요 | LLM/RAG 보안 평가의 evaluation axis |
| P02 | LLM 보안·프라이버시 공격과 방어는 어떻게 분류되는가 | security/privacy challenge survey | arXiv 및 ACM CSUR 기준 문헌조사 | LLM 학습·추론·배포 단계의 위험 분류 | jailbreak, prompt injection, PII leakage, training data extraction | attack category, defense category, risk level | ACM CSUR 2025 DOI는 확인, 강의계획서의 Ankur Das 표기는 확인 필요 | 위협모형과 방어 가정 |
| P03 | LLM은 보안에 어떻게 기여하고, 어떤 공격·취약성을 만드는가 | good/bad/ugly taxonomy 또는 AI Open 논문 확인 필요 | LLM security/privacy 문헌 분류 | LLM 보안 활용·공격 활용·취약성의 양면성 | offensive use, inherent vulnerability, prompt/context risk | taxonomy, attack surface, defense opportunity | 강의계획서 지정 AI Open 논문과 동일 여부 확인 필요 | 공격-방어-평가 연결표 |
| P04 | Multimodal LLM의 구조와 평가·hallucination 문제는 어떻게 정리되는가 | MLLM architecture/training/evaluation survey | MLLM 연구 흐름과 benchmark 정리 | image-text alignment, instruction tuning, MLLM evaluation | multimodal prompt injection, hallucination, visual context leakage | MLLM benchmark, hallucination metric, multimodal robustness | NSR DOI는 확인, 강의계획서의 Yongtao Yin 표기는 확인 필요 | multimodal LLM 확장 위험 |
| P05 | LLM은 software security workflow에 어떻게 쓰이는가 | software security meets LLM survey | fuzzing, unit test, program repair, bug detection, bug triage 분석 | code LLM과 software security task 연결 | insecure code generation, flawed repair, bug analysis failure | vulnerability rate, repair quality, triage quality | 실제 code benchmark 실험은 별도 필요, Shujun Li 표기 확인 필요 | code LLM 보안 평가 항목 |

## 종합 비교

1. P01은 LLM evaluation framework 문헌이다. W07에서는 benchmark score를 utility의 일부로만 보고, contamination과 leakage를 별도 위험으로 분리한다.
2. P02/P03은 LLM security/privacy taxonomy 문헌이다. P02는 공격·방어 분류가 강하고, P03은 보안 활용과 공격 활용의 양면성을 강조한다.
3. P04는 multimodal LLM 확장 문헌이다. 텍스트 prompt만이 아니라 image/document/GUI context가 보안 평가 대상이 된다.
4. P05는 software security와 code LLM 접점 문헌이다. code vulnerability rate와 over-refusal을 함께 기록해야 함을 뒷받침한다.
5. W07의 핵심 연결부는 LLM 보안 평가를 utility, ASR, leakage, refusal quality, over-refusal, code vulnerability rate, reproducibility evidence로 나누는 것이다.
6. P02/P03/P04/P05는 강의계획서 지정 정보와 로컬 PDF/공식 DOI 기준 정보의 차이를 검증표에 명확히 남긴다.

## 논문별 차별성

- P01: 공격을 직접 다루기보다 평가 체계의 신뢰성과 benchmark discipline을 제공한다.
- P02: LLM 보안·프라이버시 위협과 방어를 가장 직접적으로 분류한다.
- P03: LLM을 보안 도구, 공격 도구, 취약한 시스템으로 동시에 보는 관점을 제공한다.
- P04: multimodal context가 들어갈 때 prompt/context 위험이 확장되는 이유를 설명한다.
- P05: code LLM이 software security workflow를 보조하면서도 취약 코드 생성 위험을 만든다는 점을 분리한다.
