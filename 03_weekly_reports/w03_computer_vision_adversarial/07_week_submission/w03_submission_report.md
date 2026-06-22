# W03 제출용 보고서

## 표지

| 항목 | 내용 |
|---|---|
| 주차 | W03 |
| 보고서 제목 | 컴퓨터비전 표현학습 & 비전 대적공격 |
| 과목 범위 | AI 보안 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 통합본 |
| 관련 산출물 위치 | `03_weekly_reports/w03_computer_vision_adversarial/` |

## 초록

본 보고서는 컴퓨터비전 표현학습과 비전 대적공격을 연결하여, 이미지 모델의 정상 성능과 공격 조건 성능을 분리해 평가해야 함을 정리한다. AI 원리 측면에서는 CNN의 합성곱, 풀링, 특징맵, 계층적 표현과 Vision Transformer의 patch-token 기반 attention 구조를 다룬다. 보안 측면에서는 white-box/black-box attack, transfer attack, 2D/3D 비전 강건성, robust accuracy, attack success rate를 평가축으로 제시한다. 다섯 편의 문헌은 원리 문헌과 보안 문헌으로 나누어 활용했으며, synthetic 8x8 bar image 기반 toy experiment를 통해 clean baseline, 중심점 방향 L-infinity perturbation, feature squeezing check 조건을 재현 가능하게 기록했다. 결론적으로 W03는 기말논문의 “AI 보안 평가에서 clean performance, attack impact, reproducibility evidence를 분리하는 프레임워크”로 연결된다.

**키워드:** 컴퓨터비전, CNN, Vision Transformer, adversarial example, robust accuracy, ASR, 재현성

## 1. 서론

컴퓨터비전 모델은 이미지 분류, 인식, 검색, 멀티모달 정합 등 다양한 시스템의 핵심 구성요소다. 그러나 정상 테스트셋에서 높은 정확도를 보인 모델도 작은 입력 교란이나 분포 변화 앞에서 취약할 수 있다. W03의 핵심 질문은 “비전 모델의 성능을 평가할 때 clean accuracy와 robust accuracy, ASR, 재현성 근거를 어떻게 분리해 기록할 것인가”이다.

## 2. AI 원리

CNN은 지역 receptive field와 convolution 연산을 통해 이미지의 edge, texture, shape 같은 계층적 특징을 학습한다. Pooling과 feature map은 공간 정보를 압축하고, 깊은 계층은 더 추상적인 표현을 만든다. Vision Transformer는 이미지를 patch token으로 나누고 attention을 적용하여 장거리 의존성을 모델링한다. 따라서 CNN과 ViT는 같은 이미지 분류 문제를 다루더라도 inductive bias와 취약성의 양상이 다를 수 있다.

멀티모달 표현학습은 이미지와 텍스트를 같은 표현공간에 정렬한다. 이는 검색과 생성형 AI 응용에서 유용하지만, 입력 이미지 조작, 텍스트-이미지 정합 실패, 평가셋 오염 같은 보안 문제와 연결될 수 있다.

## 3. 보안 이슈

비전 대적공격은 모델 입력에 작은 교란을 추가하여 예측을 바꾸는 공격이다. White-box attack은 모델 구조나 gradient 정보에 접근할 수 있는 경우를 가정하고, black-box attack은 제한된 질의나 transferability를 이용한다. 이때 정상 조건의 accuracy만 보면 공격 조건에서의 실패를 설명할 수 없다. 따라서 clean accuracy, robust accuracy, ASR, robust drop, confusion matrix를 함께 기록해야 한다.

본 보고서는 실제 서비스 침해, 실제 개인정보 이미지, 무단 API 질의, 악용 가능한 공격 절차를 제외한다. 실험은 synthetic toy data와 단순 모델을 사용해 평가 지표 구조를 설명하는 데 한정한다.

## 4. 문헌 요약

| ID | 문헌 | 활용 |
|---|---|---|
| P01 | Gradient-Based Learning Applied to Document Recognition | CNN과 gradient 기반 학습의 출발점 |
| P02 | Deep Learning for Computer Vision: A Brief Review | 컴퓨터비전 딥러닝 발전 배경 |
| P03 | Multimodal Learning With Transformers: A Survey | transformer와 멀티모달 표현학습 배경 |
| P04 | Transformers in Vision: A Survey | ViT 구조와 CNN 대비 특징 설명 |
| P05 | A Survey of Robustness and Safety of 2D and 3D Deep Learning Models Against Adversarial Attacks | 비전 대적공격과 안전성 평가 연결 |

DOI/URL은 `01_papers/doi_check.md` 기준으로 아직 미검증 상태다. 제출 전 원문과 출판사 페이지를 대조해야 한다.

## 5. Research Track

| 항목 | 내용 |
|---|---|
| 연구문제 | 비전 모델의 clean 성능과 공격 조건 성능을 어떻게 분리해 기록할 것인가 |
| 대상 시스템 | 이미지 분류 또는 멀티모달 비전 모델 |
| 위협 | white-box/black-box adversarial perturbation, transfer attack |
| 평가 지표 | clean accuracy, robust accuracy, ASR, robust drop, confusion matrix |
| 재현성 | Docker, pyproject.toml/uv sync, config, seed, outputs 로그 |
| 제외 범위 | 실제 개인정보, 실제 서비스, 무단 API, 운영 시스템 공격 |

## 6. 실습 설계와 결과

실습 코드는 `04_experiment/src/run_experiment.py`에 작성했다. 로컬 Python 또는 Docker 환경에서 `python3 src/run_experiment.py --config configs/config.yaml`로 실행할 수 있고, 결과는 `04_experiment/outputs/`에 저장했다.

| 조건 | Epsilon | Defense | Accuracy | Macro F1 | ASR | Robust Drop |
|---|---:|---|---:|---:|---:|---:|
| Clean baseline | 0.00 | none | 1.000000 | 1.000000 | 해당 없음 | 0.000000 |
| Adversarial perturbation | 0.05 | none | 1.000000 | 1.000000 | 0.000000 | 0.000000 |
| Adversarial perturbation | 0.15 | none | 1.000000 | 1.000000 | 0.000000 | 0.000000 |
| Adversarial perturbation | 0.30 | none | 1.000000 | 1.000000 | 0.000000 | 0.000000 |
| Adversarial perturbation | 0.45 | none | 0.000000 | 0.000000 | 1.000000 | 1.000000 |
| Feature squeezing check | 0.30 | 2-level | 1.000000 | 1.000000 | 0.000000 | 0.000000 |

정량값은 `04_experiment/outputs/run_log.md` 기준이다. Epsilon 0.45에서 모든 샘플이 반대 클래스 중심으로 넘어가 accuracy가 0.000000, ASR이 1.000000이 되었다. 이는 synthetic 2-class toy 데이터의 결정 경계 전환을 보여주는 결과이며, 실제 CNN/ViT 모델의 강건성으로 일반화하지 않는다.

## 7. 발표용 보고서

발표용 보고서는 `09_presentation/presentation_report.md`와 `09_presentation/presentation_report.html`에 작성했다. 발표에서는 clean 성능과 공격 조건 성능을 분리해야 한다는 메시지를 중심으로, 문헌 5편의 역할과 toy 실험의 한계를 함께 설명한다.

## 8. 기말논문 연결

W03는 기말논문의 관련연구, 위협모형, 평가방법, 분석/실험 장에 연결된다. 특히 비전 모델 사례는 LLM/RAG 중심 기말논문에서도 “정상 성능과 보안 성능을 분리해 기록해야 한다”는 평가 원칙을 설명하는 보조 사례로 활용할 수 있다.

추천 contribution 문장은 다음과 같다.

> 본 연구는 AI 보안 평가에서 clean performance, attack impact, reproducibility evidence를 분리해 기록하는 제출 가능형 평가 프레임워크를 제시한다.

## 9. AI 활용 고지

Codex를 사용해 실험 코드 작성, synthetic toy 실험 실행, 보고서 구조화, 발표용 보고서 및 HTML 작성 보조를 수행했다. 정량값은 `04_experiment/outputs/run_log.md`와 CSV/JSON 산출물 기준으로 반영했다. 상세 기록은 `05_ai_worklog/`에 있다.

## 10. 참고문헌

1. Yann LeCun et al., “Gradient-Based Learning Applied to Document Recognition,” 1998. DOI/URL: 확인 필요.
2. Apostolos Voulodimos et al., “Deep Learning for Computer Vision: A Brief Review,” 2018. DOI/URL: 확인 필요.
3. Y. Xu et al., “Multimodal Learning With Transformers: A Survey,” 2023. DOI/URL: 확인 필요.
4. Salman Khan et al., “Transformers in Vision: A Survey,” 2022. DOI/URL: 확인 필요.
5. Z. Li et al., “A Survey of Robustness and Safety of 2D and 3D Deep Learning Models Against Adversarial Attacks,” 2023. DOI/URL: 확인 필요.

## 11. 제출 전 점검표

| 점검 항목 | 상태 |
|---|---|
| 논문 요약 5편 | 완료 |
| 논문 비교표 | 완료 |
| AI 원리/보안 이슈 | 완료 |
| Research Track | 완료 |
| 실험 코드 | 완료 |
| 실험 결과 | 완료 |
| 발표용 보고서 | 완료 |
| 제출용 보고서 HTML | 완료 |
| AI 활용 고지 | 완료 |
| DOI/URL 검증 | 확인 필요 |
