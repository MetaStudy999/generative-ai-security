# W11 차등프라이버시(DP) & 멤버십 추론 공격·방어 통합보고서 초안

최종 제출용 내용은 `06_report/final/integrated_report_final.md`에 정리했다. 본 초안은 같은 구조를 유지하며, 핵심 결론은 다음과 같다.

| 항목 | 내용 |
|---|---|
| 핵심 메시지 | DP 보장은 선언이 아니라 accounting, utility, MI risk, leakage, 재현성 로그로 검증해야 한다. |
| 실험 상태 | 실행 완료 |
| 결과 근거 | `04_experiment/outputs/run_log.md` |
| 주요 한계 | `epsilon_proxy`는 정식 DP 보장이 아니며 P03/P05 로컬 PDF는 관련 보조 문헌이다. |

## 실험 결과 요약

| 조건 | Accuracy | MI Attack Accuracy | Epsilon Proxy | Utility Drop | Privacy Leakage Score |
|---|---:|---:|---:|---:|---:|
| Non-DP baseline | 0.956250 | 0.515625 | 해당 없음 | 0.000000 | 0.014833 |
| DP-like noise low | 0.956250 | 0.515625 | 8.000000 | 0.000000 | 0.014494 |
| DP-like noise medium | 0.962500 | 0.512500 | 3.000000 | 0.000000 | 0.011769 |
| DP-like noise high | 0.950000 | 0.521875 | 1.000000 | 0.006250 | 0.016482 |

## 제출 전 남은 확인

- P01/P02/P04의 ACM DOI 공식 확인
- P03/P05 지정 논문 원문 PDF 확보
- 정식 DP-SGD/accountant 실험으로 확장할지 여부 결정
