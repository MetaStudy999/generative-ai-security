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

## 결과 기록 원칙

실험 전 상태는 `실행 전`으로 표시한다. 실험 완료 상태는 실행 로그가 있는 값만 사용하며, 주차별 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 최종 보고서의 수치가 일치해야 한다.
