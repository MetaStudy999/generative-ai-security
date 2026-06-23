# P05 Summary

## A Survey of Robustness and Safety of 2D and 3D Deep Learning Models against Adversarial Attacks — Yanjie Li et al., ACM Computing Surveys, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W03 컴퓨터비전 표현학습 & 비전 대적공격 |
| 논문명 | A Survey of Robustness and Safety of 2D and 3D Deep Learning Models against Adversarial Attacks |
| 저자 | Yanjie Li, Bin Xie, Songtao Guo, Yuanyuan Yang, Bin Xiao |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 56, No. 6, pp. 1–37 |
| 연도 | 2024 |
| DOI | https://doi.org/10.1145/3636551 |
| 논문 유형 | Survey / 2D and 3D Adversarial Robustness and Safety Review |
| 로컬 PDF | `01_papers/pdf/05_Li_et_al_2024_Robustness_Safety_2D_3D_Adversarial_Attacks.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치. 강의계획서 축약 표기 `Z. Li et al.`은 Crossref/PDF 기준 `Yanjie Li et al.`로 확인 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W03 `paper_list.md` 기준 Crossref/ACM URL 및 로컬 PDF 제목 일치 확인. 최종 출판연도는 2024년 |

---

## 1. 한 문장 요약

이 논문은 2D 이미지와 3D 비전 모델에 대한 adversarial attack, physical-world attack, defense, robustness, safety 평가를 **공격자 지식, 공격 목표, 입력 modality, 교란 제약, 물리 환경, 평가 지표** 관점에서 체계화한 W03의 핵심 보안 survey 문헌이다.

---

## 2. 연구문제

> 2D/3D deep learning 모델은 어떤 adversarial attack과 physical-world attack에 취약하며, 이를 방어하고 안전성을 평가하기 위해 어떤 threat model과 지표가 필요한가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | 2D 이미지와 3D point cloud/LiDAR 모델의 공격면은 어떻게 다른가? |
| RQ2 | White-box, black-box, transfer, physical-world attack은 어떤 공격자 능력을 가정하는가? |
| RQ3 | Digital perturbation과 physical attack은 평가 제약과 위험이 어떻게 다른가? |
| RQ4 | Robust accuracy, ASR, robust drop, safety impact는 어떻게 분리해 측정해야 하는가? |
| RQ5 | Toy 실험 결과를 실제 2D/3D 안전성으로 과장하지 않으려면 어떤 한계 문장이 필요한가? |

---

## 3. 핵심 이론 및 수식

### 3.1 대적 교란 일반식

비전 대적공격은 정상 입력 $x$에 제한된 교란 $\delta$를 더해 모델 예측을 바꾸는 문제로 볼 수 있다.

$$
x^{adv}=x+\delta, \qquad \lVert\delta\rVert_p \leq \epsilon
$$

| 기호 | 의미 |
|---|---|
| $x$ | 정상 이미지 또는 3D 입력 |
| $x^{adv}$ | 대적 입력 |
| $\delta$ | 공격 교란 |
| $\epsilon$ | 허용 교란 크기 |
| $\lVert\cdot\rVert_p$ | $L_p$ norm 제약 |

### 보안적 의미

사람에게는 작게 보이는 교란도 모델 결정경계를 넘으면 오분류가 발생한다. 그러나 norm 기반 디지털 교란만으로 실제 물리 안전성을 충분히 설명할 수는 없다.

---

### 3.2 FGSM 개념식

Gradient 기반 교란은 입력에 대한 손실 gradient 방향을 이용한다.

$$
x^{adv}=x+\epsilon\cdot\operatorname{sign}\left(\nabla_x\ell(f_{\theta}(x),y)\right)
$$

| 기호 | 의미 |
|---|---|
| $\nabla_x\ell$ | 입력 $x$에 대한 손실함수 gradient |
| $f_{\theta}$ | 비전 모델 |
| $y$ | 정답 레이블 |

### 보안적 의미

Gradient 정보가 있는 white-box 조건에서는 입력을 어떤 방향으로 바꾸면 손실이 커지는지 계산할 수 있다. 따라서 threat model에는 공격자 지식 수준을 반드시 기록해야 한다.

---

### 3.3 Robust Accuracy와 Robust Drop

공격 조건 성능은 정상 성능과 분리해서 측정한다.

$$
RobustAcc=\frac{1}{n}\sum_{i=1}^{n}\mathbf{1}[f_{\theta}(x_i^{adv})=y_i]
$$

$$
RobustDrop=CleanAcc-RobustAcc
$$

| 기호 | 의미 |
|---|---|
| $RobustAcc$ | 공격 입력에서 정답을 유지한 비율 |
| $CleanAcc$ | 정상 입력 정확도 |
| $RobustDrop$ | 공격 조건에서의 성능 저하 |

### 보안적 의미

Clean accuracy가 높은 모델도 robust drop이 크면 보안적으로 취약하다. 특히 safety-critical vision에서는 robust drop이 곧 위험 상황 증가로 연결될 수 있다.

---

### 3.4 3D Point Cloud 교란

3D 입력은 point set $P$의 좌표 교란이나 point 추가/삭제로 공격될 수 있다.

$$
P^{adv}=\{p_i+\delta_i\}_{i=1}^{N}
$$

| 기호 | 의미 |
|---|---|
| $P$ | 원본 point cloud |
| $p_i$ | $i$번째 3D point |
| $\delta_i$ | point 좌표 교란 |
| $P^{adv}$ | 대적 point cloud |

### 보안적 의미

3D 비전 공격은 이미지 픽셀 교란과 다르다. LiDAR, depth sensor, point cloud 입력에서는 point 추가/삭제, 밀도 변화, 물리 객체 배치가 보안·안전 문제로 이어질 수 있다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| 2D Vision | 이미지 pixel grid와 CNN/ViT 기반 표현학습을 사용한다. |
| 3D Vision | point cloud, voxel, mesh, depth 등 공간 구조가 다른 입력을 사용한다. |
| Digital Attack | norm 제한 교란, gradient-based attack, transfer attack이 대표적이다. |
| Physical Attack | 조명, 각도, 인쇄 patch, 3D object, sensor condition이 포함된다. |
| Defense | adversarial training, preprocessing, detection, certified robustness 등이 있다. |
| Safety | 모델 오분류가 물리적 피해, 자율주행 실패, 로봇 오작동으로 이어질 수 있다. |

---

## 5. 보안 이슈 관점 분석

| 보안 항목 | 2D/3D Adversarial Robustness 관점 해석 |
|---|---|
| 무결성 | 입력 조작으로 모델 판단이 바뀐다. |
| 가용성 | 공격 조건에서 모델 신뢰성이 급락하면 서비스가 중단되거나 무력화된다. |
| 안전성 | 자율주행·드론·로봇·의료영상에서 오분류는 물리 피해로 연결될 수 있다. |
| 책임성 | 공격 조건, 교란 범위, 실패 사례, 방어 설정을 기록해야 한다. |
| 운영 리스크 | 디지털 벤치마크 강건성이 실제 물리 환경 안전성을 보장하지 않는다. |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 대상 | 2D 이미지, 3D point cloud, LiDAR, depth map, perception output, safety decision |
| 공격자 목표 | 오분류, 객체 미탐, 잘못된 localization, 안전 판단 실패 |
| 공격자 능력 | white-box gradient 접근, black-box query, transfer attack, physical patch/object 배치 |
| 공격 경로 | sensor/input → representation → classifier/detector → safety decision |
| 제외 범위 | 실제 자율주행·드론·로봇 시스템 공격, 무단 센서 조작, 물리 피해 유발 실험 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W03/P05에서의 활용 |
|---|---|---|
| Clean Accuracy | 정상 입력 정확도 | 기본 성능 |
| Robust Accuracy | 공격 입력 정확도 | 강건성 평가 |
| ASR | 공격 목표 달성 비율 | 공격 효과 평가 |
| Robust Drop | clean 대비 공격 조건 성능 저하 | 취약성 정량화 |
| mAP Drop | detection task 성능 저하 | 객체탐지 공격 평가 |
| Safety Impact | 오분류가 안전 판단에 미치는 영향 | 물리 시스템 위험 평가 |
| Transferability | 한 모델 공격이 다른 모델에도 통하는 정도 | black-box 위험 평가 |
| Physical Realizability | 공격이 물리 환경에서 가능한 정도 | 실제 안전성 평가 |

---

## 8. 재현성 점검

| 항목 | 점검 |
|---|---|
| 데이터셋 | MNIST/CIFAR-10/toy 8x8 image, ModelNet/point cloud subset 가능 |
| 모델 | CNN, ViT, nearest-centroid toy model, simple point model |
| 공격 조건 | epsilon, norm, patch size, query budget, physical assumption 기록 필요 |
| 방어 조건 | preprocessing, adversarial training, detection 등 설정 기록 필요 |
| 결과 파일 | clean accuracy, robust accuracy, ASR, robust drop, confusion matrix 저장 |
| 한계 | toy protocol은 실제 2D/3D 모델 공격 성능을 재현한 것이 아님 |
| 재현 가능성 판단 | toy digital perturbation은 가능. physical/3D safety 실험은 장비·환경 의존성이 큼 |

---

## 9. 논문의 고유 기여

1. 2D와 3D deep learning 모델의 대적공격과 방어를 함께 정리했다.
2. Digital attack과 physical-world attack을 구분하여 안전성 평가 필요성을 제시했다.
3. White-box, black-box, transfer, physical threat model을 체계적으로 연결한다.
4. W03에서 clean accuracy와 robust accuracy, ASR, safety impact를 분리해야 하는 핵심 근거를 제공한다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| Survey 기반 한계 | 특정 방어가 모든 조건에서 효과적임을 입증하지 않는다. | toy 실험은 평가 구조 예시로만 사용한다. |
| Physical 일반화 한계 | 디지털 교란 결과가 실제 물리 환경에서 그대로 재현되지 않는다. | physical realizability를 별도 한계로 명시한다. |
| 3D 재현 비용 | 3D sensor/point cloud 실험은 장비와 데이터가 필요하다. | 문헌 기반 비교와 toy 2D 실험으로 제한한다. |
| 방어 trade-off | robust 성능 향상이 clean 성능·비용·지연시간을 악화시킬 수 있다. | clean/robust/cost multi-metric table을 제시한다. |
| 최신 multimodal 확장 필요 | MLLM, RAG-vision, embodied AI는 추가 문헌이 필요하다. | P03 및 W07/W08/W14로 연결한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | 비전 AI의 대적 취약성과 물리 안전성 문제 제시 |
| 2장 관련연구 | 2D/3D adversarial attack, defense, safety taxonomy 정리 |
| 3장 위협모형 | white/black-box, digital/physical, 2D/3D 공격자 능력 정의 |
| 4장 연구방법 | robust accuracy, ASR, robust drop, safety impact 평가 설계 |
| 5장 실험/분석 | toy perturbation 결과와 문헌 기반 2D/3D 비교표 제시 |
| 6장 보안적 함의 | 무결성, 안전성, 책임성, 물리 시스템 위험 해석 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: 비전 AI 보안 평가는 정상 이미지 성능과 공격 조건 성능을 분리해야 하며, 2D/3D와 digital/physical 공격면을 구분해야 한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: FGSM 개념식, robust accuracy/ASR 수식, 2D/3D threat model 표, clean-robust 비교표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: 이미지·3D 입력도 LLM/RAG의 멀티모달 컨텍스트로 들어갈 수 있으므로 P05의 robust/safety 평가를 W07/W08의 멀티모달 보안으로 확장한다.

---

## 13. 최종 판단

이 논문은 W03의 핵심 보안 문헌이다. P01–P04가 비전 표현학습과 Transformer 구조를 제공한다면, P05는 이를 대적공격·물리안전·강건성 평가로 연결한다.

---

## 14. 변환 호환성 메모

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
