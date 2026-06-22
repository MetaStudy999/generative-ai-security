# W03 기말논문 연결표

## 1. 이번 주차에서 얻은 연구 주제 후보

| 번호 | 주제 후보 | 대상 시스템 | 보안 위협 | 방법론 | 기여 가능성 |
|---:|---|---|---|---|---|
| 1 | 컴퓨터비전 모델의 대적공격 평가를 위한 다중지표 프레임워크 연구 | 이미지 분류 모델 | 비전 대적공격 | 문헌분석 + synthetic toy 실험 | 높음 |
| 2 | CNN과 Vision Transformer 기반 비전 모델의 보안 평가 항목 비교 연구 | CNN/ViT | 입력 교란, 강건성 저하 | 문헌 비교분석 | 높음 |
| 3 | AI 보안 평가에서 비전 대적공격의 Clean Accuracy와 Robust Accuracy 분리 기록 필요성 연구 | 비전 AI 시스템 | white-box/black-box attack | 평가 프로토콜 설계 | 높음 |

## 2. 추천 기말논문 연결 제목

- 국문: 컴퓨터비전 모델의 대적공격 평가를 위한 다중지표 프레임워크 연구
- 영문: A Multi-Metric Evaluation Framework for Adversarial Attacks on Computer Vision Models

## 3. 기말 논문에 반영할 내용

| 논문 장 | 반영 가능 내용 |
|---|---|
| 서론 | clean accuracy 중심 평가의 한계와 비전 AI 보안 평가 필요성 |
| 관련연구 | CNN, CV deep learning, multimodal Transformer, ViT, 2D/3D adversarial robustness 문헌 정리 |
| 연구문제 | clean performance와 attack-condition performance 분리 필요성 |
| 위협모형 | 이미지 입력, 표현, 모델, 출력, 평가셋, 로그를 보호 자산으로 설정 |
| 연구방법 | 문헌 비교표, 위협모형, 평가 프로토콜, safe toy experiment |
| 분석/실험 | synthetic 8x8 막대 이미지와 nearest-centroid model 기반 지표 분리 예시 |
| 보안적 함의 | Integrity, Safety, Availability, Accountability, Reproducibility |
| 한계 | toy setting은 실제 CNN/ViT/3D perception robustness를 대표하지 않음 |

## 4. KCI형 확장 방향

| 항목 | 내용 |
|---|---|
| 핵심 기여 | clean accuracy, robust accuracy, ASR, robust drop, confusion matrix, reproducibility evidence를 분리한 평가 체크리스트 |
| 필요한 보강 | 국내 KCI 참고문헌 3편 이상, 실제 공개 데이터셋 기반 추가 실험, 최종 연구윤리 고지 |
| 제출 전 주의 | public GitHub 저장소의 PDF 원문 삭제 또는 DOI/URL 대체 |

## 5. SCI형 확장 방향

| 항목 | 내용 |
|---|---|
| Structured abstract | Background, Problem, Method, Results, Contribution, Implications |
| Related work 축 | CNN, CV deep learning, multimodal Transformer, ViT, vision adversarial robustness |
| Methodology | literature matrix, threat model, metric separation, safe synthetic evaluation, reproducibility evidence |
| Threats to validity | internal, external, construct, reproducibility, literature validity |

## 6. W03 outputs 기반 연결 문장

W03 toy experiment shows that small centroid-direction perturbations do not change predictions in the synthetic setting, while epsilon 0.45 crosses the two-class toy decision boundary and produces a complete label flip. This result should not be interpreted as real-world CNN/ViT attack performance; its value is to demonstrate structured adversarial robustness reporting.
