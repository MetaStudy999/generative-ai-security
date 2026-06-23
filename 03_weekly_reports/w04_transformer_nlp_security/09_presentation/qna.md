# W04 발표 예상 질문과 답변

## 기준

| 항목 | 내용 |
|---|---|
| 주제 | Transformer 변형 & NLP 대적공격·프라이버시 |
| 발표 파일 | `presentation_report.md`, `presentation_slides.md` |
| 실험 근거 | `04_experiment/outputs/run_log.md` |
| 주의 | synthetic toy 결과를 실제 LLM 보안 성능으로 일반화하지 않음 |

## Q1. 왜 실제 LLM이나 Transformer 모델을 쓰지 않았나요?

이번 주차의 목적은 최고 성능 모델을 만드는 것이 아니라, clean score, ASR, privacy leakage, utility score를 분리해 기록하는 평가 구조를 안전하게 확인하는 것입니다. 실제 개인정보, 운영 서비스, 무단 API 질의 없이 synthetic prompt만 사용했습니다.

근거 파일: `04_experiment/experiment_report.md`, `04_experiment/outputs/run_log.md`

## Q2. Word substitution의 ASR 0.750000은 정확히 무엇인가요?

Clean 조건에서 privacy-risk로 올바르게 탐지된 위험 입력 4개 중 3개가 단어 치환 후 benign으로 오분류됐다는 뜻입니다. 즉 키워드 기반 탐지기가 표면형 변화에 취약할 수 있음을 보여주는 toy 결과입니다.

근거 파일: `04_experiment/outputs/run_log.md`

## Q3. Prompt masking의 privacy leakage 0.000000은 실제 보안을 증명하나요?

증명하지 않습니다. 이 값은 synthetic 원시 민감값 패턴이 정규식 마스킹 후 남아 있지 않다는 관찰값입니다. 실제 LLM 시스템에서는 문맥 추론, 로그 처리, 외부 도구 호출, 우회 표현까지 별도로 검증해야 합니다.

근거 파일: `04_experiment/outputs/results.json`

## Q4. 왜 utility score를 함께 보나요?

민감정보를 모두 제거해도 작업 의도가 사라지면 실무적으로 쓸 수 없습니다. 따라서 privacy leakage를 낮추는 동시에 task intent가 유지되는지 확인해야 합니다.

근거 파일: `03_theory_notes/evaluation_protocol.md`, `04_experiment/experiment_report.md`

## Q5. P01, P04, P05는 DOI가 확정인가요?

P01, P04, P05 모두 ACM 출판 DOI를 확인했습니다. P01은 `10.1145/3530811`, P04는 `10.1145/3593042`, P05는 `10.1145/3729219`입니다. 다만 ACM Article 번호와 P04 강의자료의 `N. Goyal` 표기는 사람 검토가 필요합니다.

근거 파일: `01_papers/doi_check.md`

## Q6. W04 결과는 기말논문에 어떻게 반영되나요?

기말논문의 관련연구, 위협모형, 평가방법, 분석/실험 장에 반영됩니다. 특히 프롬프트 기반 AI 시스템에서 민감정보 보호와 유용성을 함께 평가하는 체크리스트와 지표표로 발전시킬 수 있습니다.

근거 파일: `08_final_paper_bridge/final_paper_bridge.md`, `07_week_submission/w04_submission_report.md`

## Q7. 다음 실험으로 확장한다면 무엇이 필요한가요?

실제 공개 NLP 데이터셋, 사전학습 Transformer 또는 LLM 평가 환경, 의미 유사도 측정, 복수 seed, 다양한 우회 표현, 로그 마스킹 정책을 추가해야 합니다. 확장 후에도 CSV/JSON/run_log와 한계 기록을 함께 남겨야 합니다.

근거 파일: `04_experiment/configs/config.yaml`, `04_experiment/src/run_experiment.py`

## Q8. 발표에서 피해야 할 표현은 무엇인가요?

“마스킹으로 실제 LLM 프라이버시가 검증됐다” 또는 “Transformer가 단어 치환 공격에 75% 취약하다” 같은 표현은 피해야 합니다. 정확한 표현은 “synthetic toy 조건에서 평가 지표 분리 구조를 확인했다”입니다.

근거 파일: `09_presentation/speaker_notes.md`

<!-- formula-visual-qna:start -->
## 수식·그래프·그림 보강 Q&A

### Q. 그래프 수치는 어디에서 온 것인가?

A. `04_experiment/outputs/metrics_summary.csv`의 기존 수치만 사용했다. CSV에 없는 값, 실행하지 않은 실험, 외부 논문 실험 수치는 추가하지 않았다.

### Q. 이 수식은 해당 논문의 원문 수식인가?

A. 발표 보강용 수식은 표준 정의식 또는 검증 가능한 평가식이다. 논문별 원문 절·쪽·그림 번호가 필요한 경우 최종 제출 전 사람 검토로 확인한다.

### Q. 다이어그램은 실험 결과인가?

A. 아니다. `Transformer security evaluation flow` 다이어그램은 AI-assisted conceptual diagram이며 threat model과 pipeline 설명을 위한 보조 그림이다.

### Q. 보안적으로 가장 조심해야 할 해석은 무엇인가?

A. efficient attention 복잡도는 구조별로 달라 표준 비교식으로만 제시한다. 또한 모든 실습은 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 범위로만 해석한다.
<!-- formula-visual-qna:end -->
