# W03 발표용 보고서

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W03 |
| 주제 | 컴퓨터비전 표현학습 & 비전 대적공격 |
| 발표 시간 | 8-10분 |
| 권장 슬라이드 수 | 10-12장 |
| 핵심 메시지 | 비전 모델 보안 평가는 clean accuracy, robust accuracy, ASR, 재현성 근거를 분리해야 한다. |
| 발표 근거 | `06_report/final/integrated_report_final.md`, `04_experiment/outputs/run_log.md` |

## 2. 한 문장 요약

W03는 CNN/ViT 기반 컴퓨터비전 표현학습의 핵심 원리를 정리하고, 비전 대적공격 평가에서 정상 성능과 공격 조건 성능을 분리해 기록해야 함을 synthetic toy 실험으로 확인한다.

## 3. 발표 흐름

| 순서 | 슬라이드 주제 | 핵심 내용 | 시간 |
|---:|---|---|---:|
| 1 | 표지 | W03 주제와 핵심 질문 | 0:30 |
| 2 | 왜 중요한가 | 이미지 모델은 성능뿐 아니라 교란 입력 강건성이 중요 | 1:00 |
| 3 | AI 원리 | CNN, 특징맵, 계층적 표현, ViT의 inductive bias 차이 | 2:00 |
| 4 | 보안 이슈 | White-box/Black-box attack, transfer attack, 2D/3D 강건성 | 2:00 |
| 5 | 논문 비교 | 5편의 역할과 기말논문 연결 | 1:30 |
| 6 | Toy 실험 | synthetic 8x8 bar image 기반 clean/robust 비교 | 1:30 |
| 7 | 기말논문 연결 | 위협모형과 재현성 평가 프레임워크로 연결 | 1:00 |
| 8 | 결론/Q&A | clean 성능과 보안 성능을 분리해야 함 | 0:30 |

## 4. 논문 5편의 발표 역할

| ID | 논문 | 발표에서 맡는 역할 | 강조할 한계 |
|---|---|---|---|
| P01 | Gradient-Based Learning Applied to Document Recognition | CNN과 gradient 기반 학습의 출발점 | 고전 문헌이므로 최신 공격 평가와 직접 연결은 제한 |
| P02 | Deep Learning for Computer Vision: A Brief Review | 컴퓨터비전 딥러닝 발전 배경 | 보안 위협보다는 원리 설명 중심 |
| P03 | Multimodal Learning With Transformers: A Survey | transformer와 멀티모달 표현학습 배경 | 대적공격 정량 평가는 별도 문헌 필요 |
| P04 | Transformers in Vision: A Survey | ViT 구조와 CNN 대비 특징 설명 | survey 문헌이므로 실험 수치 일반화 주의 |
| P05 | Robustness and Safety of 2D and 3D Deep Learning Models Against Adversarial Attacks | 비전 대적공격과 안전성 평가 연결 | 실제 2D/3D 모델 실험은 본 주차 toy 실험 범위 밖 |

## 5. AI 원리 설명

- CNN은 지역 receptive field, convolution, pooling을 통해 계층적 시각 표현을 만든다.
- ViT는 이미지를 patch token으로 보고 attention을 적용하므로 CNN과 다른 inductive bias를 가진다.
- 멀티모달 학습은 이미지와 텍스트를 같은 표현공간에서 정렬하지만, 입력 조작과 평가셋 오염에 취약할 수 있다.

발표에서는 “좋은 표현학습이 곧 안전한 모델을 의미하지 않는다”는 점을 먼저 말한다.

## 6. 보안 이슈 설명

| 항목 | 발표 내용 |
|---|---|
| 보호 자산 | 학습 데이터, 모델 파라미터, 입력 이미지, 출력 라벨, 평가 로그 |
| 공격자 능력 | 입력 이미지 교란, 일부 데이터 조작, 모델 정보 접근 수준 차이 |
| 공격 경로 | White-box perturbation, Black-box transfer, 2D/3D 입력 조작 |
| 방어자 가정 | 공개 또는 synthetic 평가 데이터, seed/config/log 보존, 실제 서비스 공격 제외 |
| 평가 지표 | Clean accuracy, robust accuracy, ASR, robust drop, confusion matrix |

## 7. 실습/실험 결과

정량값은 `04_experiment/outputs/run_log.md` 기준이다. 이 실험은 실제 이미지 모델 공격 성능 주장이 아니라, 평가 지표 분리 방식을 보여주는 synthetic toy 예시다.

| 조건 | Epsilon | Accuracy | Macro F1 | ASR | 발표 해석 |
|---|---:|---:|---:|---:|---|
| Clean baseline | 0.00 | 1.000000 | 1.000000 | 해당 없음 | 기준 성능 |
| Adversarial perturbation | 0.30 | 1.000000 | 1.000000 | 0.000000 | 작은 교란에서는 toy 결정 경계 유지 |
| Adversarial perturbation | 0.45 | 0.000000 | 0.000000 | 1.000000 | 반대 클래스 중심으로 넘어가 모든 샘플 오분류 |
| Feature squeezing check | 0.30 | 1.000000 | 1.000000 | 0.000000 | 작은 교란 제거 확인 |

## 8. 기말논문 연결

| 기말논문 장 | 발표에서 연결할 내용 |
|---|---|
| 서론 | AI 시스템 성능 평가에 보안성과 재현성을 함께 넣어야 하는 이유 |
| 관련연구 | CNN/ViT 원리 문헌과 adversarial robustness 문헌 연결 |
| 연구문제 | clean 성능, 공격 영향, 재현성 근거를 함께 묻는 평가 질문 |
| 연구방법 | 위협모형, 평가 프로토콜, 실행 로그 기반 결과 검증 |
| 분석/실험 | synthetic toy 평가를 통한 지표 분리 예시 |
| 보안적 함의 | 성능 수치만 보고 안전성을 판단하면 안 된다는 점 |

## 9. 결론 메시지

1. 컴퓨터비전 모델은 정상 성능과 공격 조건 성능을 분리해 평가해야 한다.
2. Toy 실험이라도 seed, config, log, CSV/JSON 결과를 함께 보존해야 한다.
3. 실제 CNN/ViT 강건성 주장은 별도 공개 데이터와 모델 검증이 있을 때만 가능하다.

## 10. 예상 질문과 답변

| 질문 | 답변 요지 | 근거 파일 |
|---|---|---|
| 왜 실제 CNN/ViT 모델이 아니라 toy 실험인가? | 본 주차의 목표는 공격 성능 경쟁이 아니라 평가 지표와 재현성 기록 구조를 안전하게 설명하는 것이다. | `04_experiment/experiment_report.md` |
| Accuracy 1.0 또는 0.0이 너무 극단적인데 의미가 있는가? | synthetic 2-class toy 데이터라 경계 전환을 명확히 보여준다. 실제 모델 강건성으로 일반화하지 않는다. | `04_experiment/outputs/run_log.md` |
| Feature squeezing 결과를 방어 성능으로 주장할 수 있는가? | 아니다. 작은 toy 교란 제거 확인일 뿐이며 실서비스 방어 성능을 의미하지 않는다. | `04_experiment/experiment_report.md` |
| 기말논문에는 어떤 식으로 반영되는가? | 비전 자체보다 clean performance, attack impact, reproducibility를 분리하는 평가 프레임워크의 예시로 반영된다. | `08_final_paper_bridge/final_paper_bridge.md` |

## 11. 발표 전 점검

| 확인 | 점검 항목 |
|---|---|
| □ | 발표 수치가 `outputs/run_log.md`와 일치한다. |
| □ | 실제 CNN/ViT 성능으로 일반화하지 않는다는 한계를 말한다. |
| □ | DOI/URL 미검증 항목을 확정 표현으로 말하지 않는다. |
| □ | 예상 질문 3개 이상을 준비했다. |
