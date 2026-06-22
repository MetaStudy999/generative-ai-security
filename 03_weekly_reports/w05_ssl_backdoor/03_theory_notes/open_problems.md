# 한계와 오픈문제

## 1. 문헌 검증 한계

논문 제목과 로컬 PDF 파일명은 정리했지만 DOI/URL과 원문 세부 수치는 최종 대조가 필요하다. `SUBSTITUTE` PDF가 있는 주차는 프롬프트 지정 문헌과 실제 확보 문헌의 차이를 확인해야 한다.

## 2. 방법론 한계

자기지도학습/파운데이션 모델 및 Poisoning/Backdoor는 자기지도학습의 정의, Contrastive learning, Masked modeling와 Self-supervised pretraining 단계의 공격면, 데이터 오염과 표현공간 왜곡, Poisoning attack가 동시에 얽힌다. 단일 지표만으로 성능과 보안성을 판단하면 연구 결론이 과도하게 단순화될 수 있다.

## 3. 재현성 한계

Docker, seed, config, 데이터 버전, 실행 로그가 모두 보존되어야 한다. W05에서는 synthetic toy 실험의 `outputs/run_log.md`, `metrics_summary.csv`, `results.json`을 보존했지만, 실제 SSL 모델·공개 데이터셋 기반 재현은 별도 과제로 남는다.

## 4. 기말 논문으로 남길 질문

1. 어떤 위협을 기말 논문의 중심 사례로 삼을 것인가?
2. 문헌분석과 toy 실험을 어떻게 연결할 것인가?
3. 보안성, 설명가능성, 재현성을 하나의 평가표로 통합할 수 있는가?
