# 핵심 용어

| 용어 | 작업 정의 | 검증 메모 |
|---|---|---|
| Model IP | 모델 파라미터, 구조, 학습 데이터, 출력 행동, 생성물 출처에 포함된 지식재산 가치 | P01/P03 원문 대조 |
| Model stealing | 허가 없이 모델 지식 또는 행동을 획득·복제하는 공격군 | P01 taxonomy 확인 |
| Model extraction | query-response 관찰로 대체 모델을 학습하거나 원 모델 속성을 추정하는 절차 | W13 toy 실험과 직접 연결 |
| Query-response pair | 입력과 victim model 출력으로 구성된 substitute training record | 실제 API가 아닌 synthetic pair만 사용 |
| Substitute model | 원 모델 출력으로 학습된 대체 모델 | 본 실험은 1-nearest-neighbor toy classifier |
| Extraction fidelity | 원 모델과 대체 모델의 출력 일치율 | `outputs/metrics_summary.csv` 기준 |
| Watermarking | 모델 또는 생성물에 소유권 검증 신호를 삽입하는 기술 | P02/P03/P04 |
| Fingerprinting | 모델 고유 행동 패턴으로 출처를 식별하는 기술 | P02/P03 |
| Trigger set | 소유권 검증을 위해 준비한 입력 집합 | 본 실험은 synthetic trigger 20개 |
| Watermark detection | trigger set에서 예상 signature와 출력이 일치하는 비율 | false positive와 함께 해석 |
| False positive | 무관 모델이 소유권 signature와 우연히 일치하는 경우 | 본 실험 proxy 0.600000 |
| Utility accuracy | 워터마크 또는 방어가 일반 성능에 미치는 영향 | victim clean utility 0.868000 |
| Adaptive watermark | 출력·공격 조건에 따라 삽입/검출을 조정하는 워터마크 | P04 ModelShield |
| Robust watermark | fine-tuning, extraction, editing 이후에도 검출되는 워터마크 | 강건성 평가 필요 |
| 대체 PDF | 프롬프트 지정 문헌과 로컬 확보 PDF가 다른 상태 | P02/P05 최종 검증 필요 |
