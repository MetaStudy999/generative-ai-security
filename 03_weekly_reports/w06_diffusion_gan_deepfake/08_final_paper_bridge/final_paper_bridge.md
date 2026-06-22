# W06 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 딥페이크 탐지기의 cross-domain reliability 평가 프레임워크 | Synthetic media detector | 압축·미지 생성기·platform shift에 따른 FPR/FNR 증가 | 문헌분석 + synthetic score 실험 | 높음 |
| 2 | 생성모형 품질 평가와 포렌식 탐지 신뢰성 평가의 분리 기준 | Diffusion/GAN 기반 합성미디어 | 생성 품질 지표가 보안 신뢰성을 보장하지 않는 문제 | 비교분석 + 체크리스트 | 높음 |
| 3 | Human review routing을 포함한 딥페이크 탐지 평가체계 | Forensic review workflow | 자동판정 과신, false accusation, missed detection | toy 실험 + review-band triage | 보통 |

## 2. 추천 기말논문 제목

- 국문: 딥페이크 탐지기의 Cross-Domain Reliability 평가 프레임워크 연구
- 영문: A Study on a Cross-Domain Reliability Evaluation Framework for Deepfake Detectors
- SCI형 제목: A Cross-Domain Reliability Evaluation Framework for Deepfake Detectors: Integrating FPR, FNR, Calibration, Review-Band Triage, and Reproducibility Evidence

## 3. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | Diffusion/GAN 기반 synthetic media 발전과 포렌식 탐지 신뢰성 평가 필요성 |
| 관련연구 | P01-P03 생성모형 원리, P04-P05 딥페이크 위협모형과 reliability 관점 |
| 연구문제 | in-domain/cross-domain 성능 차이, FPR/FNR, ECE, review routing |
| 연구방법 | 문헌 비교표, 위협모형, synthetic score toy protocol, 재현성 증거 |
| 분석/실험 | cross-domain accuracy 0.816667, FNR 0.200000, review rate 0.358333 |
| 보안적 함의 | false positive/false negative, human review, accountability, governance |
| 한계 | 실제 deepfake dataset과 실제 detector가 아닌 synthetic score toy 실험 |
| 결론 | 재현 가능한 딥페이크 탐지 신뢰성 평가체계 제안 |

## 4. 최종 제출 전 확인

- P02가 강의계획서 지정 `Ananya Högele et al., "Video Diffusion Models: A Survey"`와 동일한지 확인한다.
- P03의 강의계획서 `Tianqi Wang et al.` 표기와 출판사 메타데이터 `Zhengwei Wang et al.` 차이를 확인한다.
- PDF 원문을 public GitHub에 보관할지 삭제할지 사람이 결정한다.
