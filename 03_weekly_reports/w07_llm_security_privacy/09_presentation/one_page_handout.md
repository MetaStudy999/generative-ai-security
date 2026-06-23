# W07 1페이지 배포자료

## 핵심 메시지

LLM 보안 평가는 ASR 하나로 끝나지 않는다. Utility, privacy leakage, refusal quality, over-refusal, code vulnerability rate, 재현성 로그를 함께 기록해야 한다.

## AI 원리 70%

| 원리 | 의미 | 보안 연결 |
|---|---|---|
| Pretraining | 대규모 데이터 기반 언어 패턴 학습 | memorization, data extraction |
| Instruction tuning | 지시 따르기 강화 | unsafe instruction 대응 |
| Alignment/RLHF | 선호와 안전 정책 반영 | refusal quality |
| Context window | prompt와 retrieval context 결합 | prompt injection/leakage |
| Benchmark evaluation | 모델 능력 측정 | contamination, leakage |

## 보안 이슈 30%

| 위협 | 보호 자산 | 대표 지표 |
|---|---|---|
| Data extraction | 학습데이터 | privacy leakage |
| Prompt injection | context/tool chain | ASR |
| Prompt leakage | system prompt | leakage flag |
| Insecure code | 코드 산출물 | vulnerability rate |
| Over-refusal | 정상 사용자 workflow | answer rate |

## W07 synthetic 실험 결과

| 조건 | Utility | Answer rate | ASR | Leakage | Refusal | Over-refusal | Code risk |
|---|---:|---:|---:|---:|---:|---:|---:|
| Clean | 0.866746 | 1.000000 | 0.000000 | 0.000000 | 해당 없음 | 0.000000 | 0.000000 |
| Prompt attack | 0.400908 | 0.150000 | 0.150000 | 0.000000 | 0.850000 | 0.000000 | 0.000000 |
| Privacy-risk | 0.392926 | 0.100000 | 0.100000 | 0.025000 | 0.900000 | 0.000000 | 0.000000 |
| Code security | 0.678267 | 0.650000 | 0.000000 | 0.000000 | 해당 없음 | 0.350000 | 0.200000 |

위 수치는 synthetic prompt category와 rule-based toy guard score simulator를 사용한 평가 형식 검증값이며 실제 LLM 보안 성능으로 일반화하지 않는다.

## 참고문헌 상태

- P01 DOI `10.1145/3641289` PDF 기준 확인
- P05 DOI `10.1109/JAS.2024.124971` PDF 기준 확인
- P02/P03/P04는 arXiv/PDF 기준 확인, 공식 출판정보 재검증 필요

## 기말논문 연결

W07은 “LLM/RAG 기반 AI 시스템의 보안·프라이버시·재현성 평가 프레임워크”의 관련연구, 위협모형, 평가방법, 재현성 장에 연결된다.

## 한계

실험은 실제 LLM/API 호출 없이 synthetic prompt category와 toy guard score로 수행했다. 따라서 수치는 실제 LLM 보안 성능이 아니라 평가표와 로그 구조 검증용이다.

<!-- formula-visual-handout:start -->
## 수식·그래프·그림 보강 요약

| 항목 | 반영 내용 |
|---|---|
| 핵심 수식 | Language Modeling Objective와 Perplexity, Privacy Leakage Proxy |
| 그래프 | `assets/charts/w07_metrics_chart.png` (`metrics_summary.csv` 기반) |
| 다이어그램 | `assets/diagrams/w07_pipeline_diagram.svg` (LLM privacy/safety evaluation flow) |
| 기호 정의 | 통합보고서와 발표 슬라이드의 수식 블록에 포함 |
| 주의사항 | privacy leakage는 toy/proxy metric이며 실제 개인정보 추출 실험으로 해석하지 않는다. |
<!-- formula-visual-handout:end -->
