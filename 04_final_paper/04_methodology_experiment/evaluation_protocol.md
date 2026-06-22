# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Utility | Task utility | 정상 조건의 기준 응답 또는 분류 성능 평가 | 공개 또는 synthetic data | 기본 유용성 |
| Attack Success Rate | ASR/Risk score | 안전한 prompt injection/RAG 오염 시나리오를 개념 평가 | 모의 문서와 프롬프트 | 악용 절차 제외 |
| Privacy Leakage | Leakage score | 민감정보 노출 가능성 점검 | synthetic data | 실제 개인정보 금지 |
| Robustness | Robust score | 방어 정책 적용 전후 비교 | 변형 입력 | human approval 포함 |
| Reproducibility | Seed/config/log completeness | Docker, config, seed, 결과표, 참고문헌 검증표 확인 | 실행 로그와 문서 | 제출 전 필수 |
| Cost | 실행 시간/검토 비용 | 평가 절차별 비용 기록 | 로그 | 운영 가능성 |
| Auditability | Checklist completion | 참고문헌, AI 활용 고지, 실험 결과 구분 여부 확인 | 부록 체크리스트 | 연구윤리 |

## 평가방법 설명

평가는 실제 공격 성공을 재현하는 방식이 아니라, 연구자가 보고서에서 어떤 조건을 확인하고 어떤 결과를 주장할 수 있는지 구분하는 방식으로 설계한다. Utility와 Robustness는 모델 기능 보존을, Attack Success Rate와 Privacy Leakage는 보안 위험을, Reproducibility와 Auditability는 연구윤리와 제출 가능성을 점검한다.

## 지표 정의식 초안

아래 정의식은 실제 서비스 공격을 수행하기 위한 절차가 아니라, 공개 데이터 또는 synthetic context 기반의 안전한 toy evaluation에서 결과를 보고할 때 사용할 수 있는 최소 지표 정의다.

| 지표 | 정의식 | 해석 | 사용 조건 |
|---|---|---|---|
| Attack Success Rate | `ASR = N_success / N_trials` | 안전한 모의 위협 입력 중 실패 조건에 도달한 비율 | 실패 조건을 사전에 명확히 정의한 경우 |
| Leakage Score | `Leakage = N_leak / N_sensitive_tests` | synthetic 민감정보 테스트 중 노출이 발생한 비율 | 실제 개인정보가 아닌 synthetic data만 사용 |
| Defense Pass Rate | `DPR = N_blocked_or_corrected / N_risky_cases` | 방어·검토 절차가 위험 사례를 차단하거나 수정한 비율 | human approval, filtering 등 방어 조건이 있는 경우 |
| Utility Retention | `UR = Score_defense / Score_baseline` | 방어 적용 후 기능 성능이 얼마나 유지되는지 | 동일 rubric 또는 동일 평가셋 기준 |
| Reproducibility Completeness | `RC = N_checked_items / N_required_items` | seed, config, log, 결과표, 참고문헌 검증 등 필수 항목 충족률 | 제출 전 감사 지표 |
| Auditability Score | `AS = N_verified_artifacts / N_required_artifacts` | 근거 파일과 부속서류가 얼마나 검증 가능한지 | AI 고지서, 참고문헌표, 양식 출처표 포함 |

각 지표를 본문에 사용할 때는 `N_success`, `N_trials`처럼 기호의 의미와 실패 조건을 함께 적는다. 실행 로그가 없으면 수치 대신 `실행 전` 또는 `확인 필요`로 표시한다.

W01-W15 각 논문에 연결되는 대표 수식과 쉬운 설명은 `formula_metric_supplement.md`에 정리한다. 해당 보충표는 원문 수식 직접 인용이 아니라 보고서 설명용 정의식이므로, 최종 투고본에서 원문 수식으로 쓰는 경우 논문 원문 쪽/절 번호를 확인한다.

## 수식 작성 및 검산 도구

| 용도 | 도구 |
|---|---|
| 기본 작성 | Markdown + LaTeX math |
| HTML 렌더링 | KaTeX 또는 MathJax |
| DOCX/PDF 변환 | Pandoc 또는 선택 학회지 양식 |
| 최종 PDF 품질 확인 | LaTeX / TeX Live |
| 수식 검산 | 필요 시 `sympy` |
| 지표 계산·표 정리 | `numpy`, `pandas`, 필요 시 `scipy` |

## 결과 기록 원칙

실험 전 상태는 `실행 전`으로 표시한다. 실험 완료 상태는 실행 로그가 있는 값만 사용하며, 주차별 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 최종 보고서의 수치가 일치해야 한다.
