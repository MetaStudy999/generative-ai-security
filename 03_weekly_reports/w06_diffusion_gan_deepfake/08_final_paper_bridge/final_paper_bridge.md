# W06 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 딥페이크 탐지기의 cross-domain reliability 평가 프레임워크 | Synthetic media detector | 압축·미지 생성기·platform shift에 따른 FPR/FNR 증가 | 문헌분석 + synthetic score 실험 | 높음 |
| 2 | 생성모형 품질 평가와 포렌식 탐지 신뢰성 평가의 분리 기준 | Diffusion/GAN 기반 합성미디어 | 생성 품질 지표가 보안 신뢰성을 보장하지 않는 문제 | 비교분석 | 높음 |
| 3 | Human review routing을 포함한 딥페이크 탐지 제출 체크리스트 | Forensic review workflow | 자동판정 과신, false accusation, missed detection | toy 실험 + 체크리스트 | 보통 |

## 2. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | 확률생성모형(Diffusion/GAN) 및 딥페이크 검출의 보안 평가 필요성 |
| 관련연구 | Diffusion, Score-based model, GAN, 조건부 생성 및 딥페이크, 합성미디어, 포렌식, 신뢰성 평가 문헌 정리 |
| 연구문제 | 생명주기 기반 위협모형과 평가방법 필요성 |
| 연구방법 | 문헌 비교표, 위협모형, 평가 프로토콜 |
| 분석/실험 | synthetic detector score 실험: cross-domain accuracy 0.816667, FNR 0.200000, review rate 0.358333 |
| 보안적 함의 | false positive/false negative, human review, accountability 관점 |
| 결론 | 재현 가능한 AI 보안 평가체계 제안 |
