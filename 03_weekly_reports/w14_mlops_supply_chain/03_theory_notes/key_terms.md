# 핵심 용어

| 용어 | 작업 정의 | 검증 메모 |
|---|---|---|
| MLOps | ML 모델을 개발, 배포, 모니터링, 재학습까지 반복 관리하는 운영 practice | P01/P02 기준 원문 세부 대조 |
| DevOps | 소프트웨어 개발과 운영을 자동화·모니터링·CI/CD로 연결하는 방식 | MLOps와 차이 설명에 사용 |
| ML lifecycle | 데이터 준비부터 운영 감시와 재학습까지 이어지는 반복 생명주기 | W14 위협모형의 단계 |
| Data pipeline | 데이터 수집, 전처리, feature 생성, 품질 검증 흐름 | dataset hash와 provenance로 평가 |
| Model pipeline | 학습 코드, config, seed, model artifact, registry를 관리하는 흐름 | model hash와 re-run consistency로 평가 |
| Model registry | 모델 artifact와 metadata를 버전별로 보관하는 저장소 | 본 실험은 local artifact inventory로 대체 |
| Drift detection | 입력/출력/성능 분포가 기준과 달라졌는지 측정하는 절차 | toy 실험 drift score 0.307626, 공격 성공률 아님 |
| AIOps | 운영 telemetry에 AI/ML을 적용해 이상탐지, 장애예측, RCA, 대응을 보조하는 영역 | P03 로컬 대체문헌 기준 보조 |
| Edge AI | 데이터 발생 지점 가까이에서 AI 추론 또는 학습을 수행하는 구조 | P04 배포 공격면 설명 |
| DL for SE | 소프트웨어공학 task에 딥러닝을 적용하는 연구 영역 | P05 개발 pipeline 공격면 설명 |
| ML supply chain risk | 데이터, 코드, 의존성, 모델, 배포 설정이 이어지는 공급망의 보안 위험 | W14 핵심 보안 이슈 |
| Data poisoning | 학습 데이터나 label을 조작해 모델 산출물을 왜곡하는 위협 | 실제 공격 절차는 제외 |
| Artifact tampering | 저장 또는 배포된 모델 파일을 무단 변경하는 위협 | model hash match로 점검 |
| AI BOM / ML artifact inventory | 데이터, 모델, config, 로그 등 AI 산출물 목록과 출처·해시 기록 | outputs/artifact_inventory.json |
| Audit coverage | 필수 감사 필드 중 기록된 항목의 비율 | toy 실험 1.000000, 실제 감사 완전성 아님 |
| Assurance case | 시스템이 안전하고 재현 가능하다고 주장할 때 필요한 근거 묶음 | 기말 논문 방법론 후보 |
