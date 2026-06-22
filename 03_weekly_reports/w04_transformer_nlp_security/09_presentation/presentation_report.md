# W04 발표용 보고서

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W04 |
| 주제 | Transformer 변형 & NLP 대적공격·프라이버시 |
| 발표 시간 | 8-10분 |
| 권장 슬라이드 수 | 10-12장 |
| 핵심 메시지 | 프롬프트 기반 NLP 보안 평가는 clean score, attack success rate, privacy leakage, utility를 분리해야 한다. |
| 발표 근거 | `06_report/final/integrated_report_final.md`, `04_experiment/outputs/run_log.md` |

## 2. 한 문장 요약

W04는 Transformer와 X-former의 효율화 원리를 정리하고, NLP 단어 치환 공격과 프롬프트 프라이버시 위험을 synthetic toy 실험으로 분리 평가한다.

## 3. 발표 흐름

| 순서 | 슬라이드 주제 | 핵심 내용 | 시간 |
|---:|---|---|---:|
| 1 | 표지 | W04 주제와 핵심 질문 | 0:30 |
| 2 | 왜 중요한가 | 긴 프롬프트와 ICL은 성능뿐 아니라 민감정보 보호가 필요 | 1:00 |
| 3 | AI 원리 | self-attention, Q/K/V, multi-head attention | 1:30 |
| 4 | Efficient Transformer | sparse, low-rank, kernelized attention | 1:30 |
| 5 | 보안 이슈 | 단어 치환, 프롬프트 프라이버시, ICL leakage | 1:30 |
| 6 | 논문 5편의 역할 | 원리 문헌과 보안 문헌 연결 | 1:00 |
| 7 | 위협모형 | 보호 자산, 공격자 능력, 제외 범위 | 1:00 |
| 8 | Toy 실험 | synthetic privacy-risk prompts | 1:00 |
| 9 | 결과 | Clean 1.000000, ASR 0.750000, leakage 0.000000 | 1:00 |
| 10 | 기말 연결 | 프롬프트 민감정보 보호 평가체계 | 0:45 |
| 11 | 결론/Q&A | 지표 분리와 재현성 근거 | 0:15 |

## 4. 논문 5편의 발표 역할

| ID | 논문 | 발표에서 맡는 역할 | DOI/URL 상태 |
|---|---|---|---|
| P01 | Efficient Transformers: A Survey | X-former와 efficient attention 분류 | arXiv DOI 확인 |
| P02 | A Practical Survey on Faster and Lighter Transformers | faster/lighter transformer의 practical trade-off | ACM DOI 확인 |
| P03 | A survey of transformers | Transformer 변형 taxonomy | AI Open DOI 확인 |
| P04 | A Survey of Adversarial Defences and Robustness in NLP | NLP 대적공격 방어 taxonomy | arXiv DOI 확인 |
| P05 | Privacy Preserving Prompt Engineering: A Survey | prompt privacy와 ICL 보호 방법 | arXiv DOI 확인 |

## 5. AI 원리 설명

- Self-attention은 모든 토큰 쌍의 관계를 계산하므로 긴 입력에서 계산·메모리 비용이 커진다.
- Q/K/V는 어떤 정보를 찾고, 무엇과 비교하고, 어떤 값을 전달할지를 분리한다.
- Efficient Transformer 계열은 sparse attention, low-rank approximation, kernelized attention 등으로 비용을 낮춘다.
- 이 원리는 긴 프롬프트와 ICL 예시가 많은 LLM 시스템에서 보안 평가 비용과도 연결된다.

## 6. 보안 이슈 설명

| 항목 | 발표 내용 |
|---|---|
| 보호 자산 | 입력 문장, 프롬프트, synthetic 민감값, 모델 응답, 로그 |
| 공격자 능력 | 단어 치환, 민감정보 삽입, 프롬프트 조작 |
| 공격 경로 | 사용자 입력, ICL 예시, 로그 저장 경로 |
| 방어자 가정 | 입력 마스킹, 정책 지시, 실행 로그 보존 가능 |
| 평가 지표 | clean score, ASR, privacy leakage, utility score |

## 7. 실습/실험 결과

정량값은 `04_experiment/outputs/run_log.md` 기준이다.

| 조건 | Clean Score | Attack Success Rate | Privacy Leakage | Utility Score | 발표 해석 |
|---|---:|---:|---:|---:|---|
| Clean baseline | 1.000000 | 해당 없음 | 해당 없음 | 1.000000 | 정상 입력 기준 |
| Word substitution | 0.625000 | 0.750000 | 해당 없음 | 1.000000 | 키워드 우회 취약성 |
| Prompt masking | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 | 원시 민감값 제거 |
| Privacy-preserving prompt | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 | 마스킹과 정책 결합 |

## 8. 기말논문 연결

| 기말논문 장 | 발표에서 연결할 내용 |
|---|---|
| 서론 | 프롬프트 기반 AI 시스템의 개인정보 위험 |
| 관련연구 | Efficient Transformer, NLP adversarial defense, prompt privacy |
| 연구문제 | 민감정보 보호와 유용성의 동시 평가 |
| 연구방법 | 위협모형, 체크리스트, synthetic 사례 분석 |
| 분석/실험 | 단어 치환 ASR과 마스킹 leakage 비교 |
| 보안적 함의 | 기밀성, 프라이버시, 책임성 관점 |

## 9. 결론 메시지

1. Transformer 효율화는 긴 입력 처리의 전제 조건이지만, 보안성 자체를 보장하지 않는다.
2. NLP 보안 평가는 clean score와 공격 조건 지표를 분리해야 한다.
3. 프롬프트 프라이버시는 leakage와 utility를 함께 봐야 한다.
4. 수치는 실행 로그와 config, CSV/JSON 근거가 있을 때만 주장한다.

## 10. 예상 질문과 답변

| 질문 | 답변 요지 | 근거 파일 |
|---|---|---|
| 왜 실제 LLM을 쓰지 않았나? | 목표는 안전한 toy 환경에서 평가 지표 구조를 검증하는 것이다. 실제 API나 개인정보를 쓰지 않는다. | `04_experiment/experiment_report.md` |
| ASR 0.750000은 무엇을 뜻하나? | clean에서 privacy-risk로 탐지된 4개 위험 입력 중 3개가 단어 치환 후 benign으로 오분류된 비율이다. | `04_experiment/outputs/run_log.md` |
| 마스킹 leakage 0.000000은 실제 보호를 증명하나? | 아니다. synthetic 원시 민감값 패턴이 제거됐다는 toy 결과이며 실제 프롬프트 보안은 별도 검증이 필요하다. | `04_experiment/outputs/results.json` |
| DOI는 모두 확정인가? | P02/P03은 출판 DOI를 확인했고 P01/P04/P05는 arXiv DOI/URL을 확인했다. | `01_papers/doi_check.md` |

## 11. 발표 전 점검

| 확인 | 점검 항목 |
|---|---|
| □ | 발표 수치가 `outputs/run_log.md`와 일치한다. |
| □ | synthetic toy 결과를 실제 LLM 성능으로 일반화하지 않는다. |
| □ | 출판 DOI와 arXiv DOI를 구분해 말한다. |
| □ | 예상 질문 3개 이상을 준비한다. |
