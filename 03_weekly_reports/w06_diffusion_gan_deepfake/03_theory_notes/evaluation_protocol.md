# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| In-domain performance | Accuracy, F1, FPR, FNR, AUROC, ECE | 기준 score 분포에서 threshold detector 평가 | synthetic real/fake score | 기본 성능 |
| Cross-domain reliability | Accuracy, F1, FPR, FNR, AUROC, ECE | 압축·미지 도메인 score shift 조건에서 성능 비교 | synthetic shifted score | 일반화 |
| Calibration | ECE | confidence와 correctness 차이 계산 | detector score | 신뢰도 해석 |
| Human review routing | Auto coverage, review rate | 불확실 score band를 자동판정에서 제외 | review band 설정 | 포렌식 검토 |
| Reproducibility | Seed/config/log completeness | seed, config, Docker, 결과표 보존 여부 점검 | 실행 로그 | 제출 근거 |
| Human Review | 검토 완료 여부 | 원문, DOI, 수치, 인용을 사람이 재검토 | 체크리스트 | 최종 책임 |

## 실행 결과 위치

정량 수치는 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`에 기록했다. 보고서와 발표자료는 이 산출물의 값을 기준으로 작성한다.

## 한계 문장

이 결과는 synthetic detector score toy 실험의 평가 형식 검증용 수치이며, 실제 딥페이크 데이터셋, 실제 탐지 모델, 법적 포렌식 증거능력, 운영 서비스의 보안 성능으로 일반화하지 않는다.
