# W03 컴퓨터비전 표현학습 & 비전 대적공격 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W03 |
| 주제 | 컴퓨터비전 표현학습 & 비전 대적공격 |
| AI 원리 | CNN, ViT, 멀티모달 정합, 표현학습 |
| 보안 이슈 | White-box/Black-box 비전 대적공격, 2D/3D 강건성, 안전성 평가 |
| 문서 상태 | 제출본 |

## 1. 한 문장 요약

W03는 컴퓨터비전 표현학습 및 비전 대적공격을 중심으로 AI 원리와 보안 위협을 함께 정리하고, 기말 논문의 위협모형·평가방법·재현성 설계로 연결한다.

## 2. AI 원리 70% 정리

CNN, ViT, 멀티모달 정합, 표현학습을 이해하기 위해 CNN의 기본 구조, 합성곱, 풀링, 특징맵, 계층적 표현, 컴퓨터비전 표현학습의 발전, Vision Transformer의 등장 배경, CNN과 ViT의 inductive bias 차이, 멀티모달 학습과 이미지-텍스트 정합을 핵심 개념으로 정리했다. 이 원리들은 모델 또는 시스템이 어떤 입력과 학습 구조를 갖고 어떤 기준으로 평가되는지 설명한다.

### 2.1 핵심 수식 또는 알고리즘 쉬운 설명

아래 수식은 원문 수식의 직접 인용이 아니라, 각 논문의 핵심 개념을 보고서에서 설명하기 위한 대표 수식과 지표다. 최종 제출본에서 원문 수식으로 인용할 경우 논문 원문 쪽/절 번호를 추가 확인한다.

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보안 평가 연결 |
|---|---|---|---|
| P01 | $y_{i,j,k}=\sigma(\sum_{u,v,c}W_{u,v,c,k}x_{i+u,j+v,c}+b_k)$ | CNN은 작은 필터를 이미지 위로 움직이며 지역 패턴을 찾는다. | 이미지 특징 추출 원리 |
| P02 | $CE=-\sum_c y_c\log p_c$ | 분류 모델은 정답 클래스 확률이 낮을수록 큰 벌점을 받는다. | vision classifier 평가 |
| P03 | $Attn(Q,K,V)=softmax(QK^T/\sqrt d)V$ | multimodal transformer는 서로 관련 있는 시각·텍스트 단서를 더 크게 본다. | multimodal robustness |
| P04 | $z_0=[x_{class};x_1E;\dots;x_NE]+E_{pos}$ | Vision Transformer는 이미지를 패치 토큰으로 바꾼 뒤 Transformer에 넣는다. | vision transformer 구조 |
| P05 | $RA=\frac{1}{n}\sum_i 1[f(x_i+\delta_i)=y_i]$ | robust accuracy는 공격 변형이 들어간 뒤에도 정답을 맞힌 비율이다. | 2D/3D adversarial 안전성 |

## 3. 보안 이슈 30% 정리

White-box/Black-box 비전 대적공격, 2D/3D 강건성, 안전성 평가를 중심으로 비전 기반 대적공격, White-box attack, Black-box attack, Transfer attack, FGSM, PGD 등 기본 공격 개념, 2D 이미지 모델과 3D 비전 모델의 취약성 차이를 정리했다. 보안 분석은 공격 절차 자체보다 보호 자산, 공격자 능력, 방어자 가정, 평가 지표를 명확히 하는 방향으로 작성했다.

## 4. 논문 5편 요약

| ID | 논문 | 저자 | 연도 | 검증 상태 |
|---|---|---|---|---|
| P01 | Gradient-Based Learning Applied to Document Recognition | Yann LeCun et al. | 1998 | 원문 세부 대조 필요 |
| P02 | Deep Learning for Computer Vision: A Brief Review | Apostolos Voulodimos et al. | 2018 | 원문 세부 대조 필요 |
| P03 | Multimodal Learning With Transformers: A Survey | Y. Xu et al. | 2023 | 원문 세부 대조 필요 |
| P04 | Transformers in Vision: A Survey | Salman Khan et al. | 2022 | 원문 세부 대조 필요 |
| P05 | A Survey of Robustness and Safety of 2D and 3D Deep Learning Models Against Adversarial Attacks | Z. Li et al. | 2023 | 원문 세부 대조 필요 |

## 5. 논문 5편 비교

다섯 편은 AI 원리 문헌과 보안 문헌을 함께 포함한다. 기말 논문에서는 개별 문헌의 세부 수치보다 분류체계, 위협모형, 평가 프로토콜의 연결 관계를 우선 반영한다.

## 6. Research Track

### 6.1 연구문제

RQ1. 컴퓨터비전 표현학습 및 비전 대적공격의 생명주기에서 보안 보증을 위해 어떤 평가 항목이 필요한가?

RQ2. 비전 기반 대적공격, White-box attack는 어느 단계에서 발생하며 어떤 조건에서 성공하는가?

RQ3. 성능, 보안성, 재현성을 함께 평가하려면 어떤 최소 프로토콜이 필요한가?

### 6.2 위협모형

대상 시스템은 컴퓨터비전 표현학습 및 비전 대적공격 기반 AI/ML 시스템이며, 보호 자산은 데이터, 모델, 입력/컨텍스트, 출력, 로그, 평가셋이다. 공격자는 외부 공격자, 내부자, 데이터 제공자, API 남용자 등으로 나뉜다.

### 6.3 평가방법

Clean performance, attack impact, robust performance, privacy/leakage, reproducibility, human review를 기본 평가 항목으로 둔다.

### 6.4 재현성

Docker, pyproject.toml/uv sync, config, seed, 로그, PDF/DOI 검증표를 함께 보존한다. W03 synthetic toy 실험은 `04_experiment/src/run_experiment.py`로 실행했고 CSV, JSON, Markdown 로그, PGM 예시 이미지를 `04_experiment/outputs/`에 보존했다.

### 6.5 한계와 오픈문제

DOI/URL, 원문 세부 수치, 대체 PDF 여부는 최종 확인이 필요하다. 또한 synthetic toy 실험 결과를 실제 CNN/ViT 또는 2D/3D 비전 강건성 평가와 어떻게 연결할지 추가 검토가 필요하다.

## 7. 실습 요약

실습은 synthetic 8x8 bar image와 nearest-centroid 모델을 사용해 안전한 toy 조건에서 실행했다. 실제 개인정보, 실제 서비스 침해, 무단 질의, 악용 가능한 절차는 포함하지 않는다.

| 조건 | Epsilon | Accuracy | Macro F1 | ASR | 해석 |
|---|---:|---:|---:|---:|---|
| Clean baseline | 0.00 | 1.000000 | 1.000000 | 해당 없음 | 기준 성능 |
| Adversarial perturbation | 0.30 | 1.000000 | 1.000000 | 0.000000 | 작은 교란에서는 toy 결정 경계 유지 |
| Adversarial perturbation | 0.45 | 0.000000 | 0.000000 | 1.000000 | 반대 클래스 중심으로 전환 |
| Feature squeezing check | 0.30 | 1.000000 | 1.000000 | 0.000000 | 작은 교란 제거 확인 |

## 8. AI 활용 기록 요약

Codex를 사용해 구조화 작업과 문서 간 수치·상태 일치성 점검을 수행했다. AI 산출물은 사람 검토와 원문 대조 책임을 전제로 제출본에 반영했다.

## 9. 토론 질문

1. 컴퓨터비전 표현학습 및 비전 대적공격에서 가장 중요한 보호 자산은 무엇인가?
2. 공격 성공률과 일반 성능을 함께 볼 때 어떤 지표가 가장 설득력 있는가?
3. 원문 검증과 재현성 기록을 어느 수준까지 제출물에 포함해야 하는가?

## 10. 기말 논문 연결

W03는 기말 논문의 관련연구, 위협모형, 평가방법, 보안적 함의 장에 연결된다.

## 11. 참고문헌 검증표

참고문헌은 `01_papers/doi_check.md`에서 DOI/URL 확인 상태를 관리한다.

## 12. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 작성 |
| 비교표 | 작성 |
| AI 원리 70% | 작성 |
| 보안 이슈 30% | 작성 |
| Research Track | 작성 |
| 실험 결과 조작 방지 | 실행 로그 기준 수치만 기록 |
| 발표용 보고서 | 작성 |
| 발표용 슬라이드 | 작성 |
| 제출용 보고서 및 HTML | 작성 |
| DOI 임의 생성 방지 | 미검증 항목은 확인 필요로 유지 |
| AI 사용 은폐 방지 | AI 활용 고지서 작성 |
