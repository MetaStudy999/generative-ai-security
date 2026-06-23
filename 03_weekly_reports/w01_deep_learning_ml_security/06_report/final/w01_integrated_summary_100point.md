# W01 100점형 통합 Summary

## 딥러닝 패러다임 & ML 보안 분류학

## 0. 문서 목적

이 문서는 W01 개별 논문 summary 5개를 기말논문 작성용 연구 노트로 통합한 100점형 요약본이다. 기존 `integrated_report_final.md`는 제출용 통합보고서이고, 본 문서는 개별 PDF summary 보강 결과를 반영한 **논문 작성용 압축본**으로 사용한다.

| 항목 | 내용 |
|---|---|
| 주차 | W01 |
| 주제 | 딥러닝 패러다임 & ML 보안 분류학 |
| 주요 문헌 | P01–P05 |
| 핵심 프레임 | AI 원리 + 생명주기 보증 + 침입탐지 지표 + 대적 강건성 + 프라이버시 누출 |
| 수식 작성 방식 | GitHub / Word / PDF 변환 호환을 위해 LaTeX block math 사용 |
| 주의사항 | P04는 강의계획서 지정 IEEE CS&T 논문과 동일 여부 확인 필요. 현재 repo에서는 arXiv 관련 논문으로 관리 |

---

## 1. 한 문장 통합 요약

W01은 딥러닝을 단순한 모델 구조가 아니라 **데이터, 학습, 검증, 배포, 모니터링이 연결된 ML 생명주기 시스템**으로 해석하고, AI 보안 평가는 clean performance, robust performance, privacy leakage, reproducibility evidence를 분리해 측정해야 함을 정리하는 기준 주차다.

---

## 2. W01 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | 딥러닝의 표현학습과 역전파 원리는 AI 보안 취약성 분석의 어떤 이론적 기반을 제공하는가? |
| RQ2 | ML 생명주기 각 단계에서 보안성 주장을 뒷받침하기 위한 최소 보증 증거는 무엇인가? |
| RQ3 | 침입탐지 모델의 성능을 accuracy 하나로 평가하면 왜 위험한가? |
| RQ4 | 대적 공격 조건에서 clean accuracy와 robust accuracy를 왜 분리해야 하는가? |
| RQ5 | 프라이버시 공격은 모델이 정상 동작하더라도 어떤 방식으로 학습 데이터 정보를 누출시키는가? |
| RQ6 | W01의 평가축을 RAG 문서 오염, LLM 보안, MLOps 감사 프레임워크로 어떻게 확장할 수 있는가? |

---

## 3. 문헌 5편 통합 매트릭스

| ID | 논문 | 핵심 역할 | 주요 수식/지표 | 기말논문 반영 위치 |
|---|---|---|---|---|
| P01 | LeCun et al., *Deep learning* | 딥러닝 원리, 표현학습, 역전파 | 경험위험최소화, 역전파, 표현학습 | 1장 배경, 2장 관련연구, 4장 평가 지표 |
| P02 | Ashmore et al., *Assuring the Machine Learning Lifecycle* | 생명주기 보증과 evidence framework | assurance function, lifecycle risk, evidence coverage | 3장 위협모형, 4장 연구방법, 6장 보안적 함의 |
| P03 | Buczak & Guven, *ML Methods for Cyber Security Intrusion Detection* | 보안 탐지 평가와 오탐·미탐 문제 | confusion matrix, precision, recall, F1, FAR | 4장 평가방법, 5장 분석/실험 |
| P04 | Wang et al., *Adversarial Attacks and Defenses in ML-Powered Networks* | 대적 공격·방어 평가와 강건성 | adversarial objective, robust accuracy, ASR | 3장 위협모형, 4장 연구방법, 5장 비교분석 |
| P05 | Rigaki & Garcia, *Privacy Attacks in Machine Learning* | 프라이버시 공격과 정보 누출 평가 | MI advantage, generalization gap, DP, privacy-utility trade-off | 3장 위협모형, 4장 평가방법, 6장 보안적 함의 |

---

## 4. AI 원리 70% 통합 정리

### 4.1 딥러닝 학습 목적

딥러닝은 학습 데이터에서 평균 손실을 최소화하는 방향으로 모델 파라미터를 조정한다.

$$
\min_{\theta} \hat{R}(\theta)
= \frac{1}{n}\sum_{i=1}^{n} \ell(f_{\theta}(x_i), y_i)
$$

| 기호 | 의미 |
|---|---|
| $\theta$ | 모델 파라미터 |
| $x_i, y_i$ | 입력 데이터와 정답 레이블 |
| $f_{\theta}$ | 학습된 모델 |
| $\ell(\cdot)$ | 손실함수 |
| $\hat{R}(\theta)$ | 경험위험 |

**보안 해석:** 정상 데이터 평균 손실이 낮아도 공격 조건에서 안전하다는 뜻은 아니다. 공격자는 평균 분포가 아니라 모델이 취약한 특정 입력 영역, 특정 트리거, 특정 confidence 패턴을 노린다.

---

### 4.2 역전파와 공격면

모델은 손실함수의 gradient를 이용해 파라미터를 갱신한다.

$$
\theta_{t+1} = \theta_t - \eta \nabla_{\theta} \hat{R}(\theta_t)
$$

대적 공격은 같은 gradient 정보를 입력 조작에 활용할 수 있다.

$$
x^{adv} = x + \epsilon \cdot \operatorname{sign}\left(\nabla_x \ell(f_{\theta}(x), y)\right)
$$

| 항목 | AI 원리 | 보안 의미 |
|---|---|---|
| Gradient | 손실을 줄이는 방향 계산 | 공격자는 손실을 키우는 방향으로 입력 조작 가능 |
| Representation | 입력을 은닉 표현으로 변환 | 교란·트리거가 내부 표현을 왜곡 가능 |
| Generalization | 새 데이터에서 성능 유지 | 분포 이동·과적합·프라이버시 누출과 연결 |
| Confidence | 모델 출력 확률 또는 점수 | membership inference와 model extraction의 단서 가능 |

---

### 4.3 표현학습

딥러닝은 원시 입력을 여러 층의 비선형 변환으로 추상화한다.

$$
h^{(l)} = \sigma\left(W^{(l)}h^{(l-1)} + b^{(l)}\right)
$$

**보안 해석:** 표현학습은 고성능의 기반이지만, 내부 표현이 데이터 오염, 대적 교란, 백도어 트리거, 분포 이동에 민감할 경우 보안 실패로 이어진다.

---

## 5. 보안 이슈 30% 통합 정리

| 보안 축 | 관련 논문 | 핵심 문제 | 주요 지표/증거 |
|---|---|---|---|
| 생명주기 보증 | P02 | 데이터·학습·검증·배포 증거 누락 | evidence coverage, reproducibility score |
| 침입탐지 | P03 | 오탐·미탐·불균형 데이터 | precision, recall, F1, FAR, detection rate |
| 대적 강건성 | P04 | 정상 정확도와 공격 조건 정확도 불일치 | robust accuracy, ASR, robust drop |
| 프라이버시 | P05 | 정상 동작 중 학습 데이터 정보 누출 | MI advantage, AUC, privacy budget |
| 운영 감사 | P02–P05 | 로그·버전·설정 누락으로 사후 검증 불가 | seed, config, logs, DOI, data lineage |

---

## 6. W01 통합 위협모형

### 6.1 보호 자산

| 보호 자산 | 설명 |
|---|---|
| 학습 데이터 | 개인정보, 보안 로그, 이미지, 텍스트, 라벨 정보 |
| 모델 파라미터 | 학습된 가중치, 구조, checkpoint |
| 입력 데이터 | 운영 환경의 사용자 입력, 네트워크 트래픽, 센서값 |
| 출력 정보 | label, confidence, probability vector, embedding |
| 평가셋 | benchmark, validation data, hidden test data |
| 운영 로그 | API 호출, 모델 버전, 배포 이력, incident log |

### 6.2 공격자 능력

| 공격자 유형 | 가능 행위 | 관련 평가축 |
|---|---|---|
| Data attacker | 학습 데이터·라벨 오염 | lifecycle risk, poisoning |
| Inference attacker | 입력을 조작해 오분류 유도 | robust accuracy, ASR |
| Privacy attacker | 출력 신호로 membership 또는 속성 추론 | MI advantage, AUC |
| Evaluation attacker | 평가셋 오염 또는 benchmark leakage 유도 | reproducibility, contamination check |
| Deployment attacker | API 반복 질의, model extraction, drift 악용 | query budget, audit log |

### 6.3 공격 경로

```text
데이터 수집/라벨링
→ 모델 학습
→ 검증/평가
→ 배포/API 제공
→ 운영 모니터링
→ 공격자가 데이터·입력·출력·로그 중 하나를 조작 또는 관찰
→ 성능 저하, 오탐/미탐, 대적 실패, 프라이버시 누출, 감사 실패 발생
```

---

## 7. 통합 평가 지표

| 평가축 | 대표 지표 | 해석 | 관련 논문 |
|---|---|---|---|
| Clean Performance | accuracy, precision, recall, F1 | 정상 조건에서 모델이 얼마나 잘 작동하는가 | P01, P03 |
| Detection Quality | detection rate, FAR, PR-AUC | 보안 이벤트에서 오탐과 미탐을 어떻게 균형화하는가 | P03 |
| Robust Performance | robust accuracy, ASR, robust drop | 공격 입력에서도 성능이 유지되는가 | P04 |
| Privacy Leakage | MI advantage, AUC, reconstruction error | 학습 데이터 또는 민감 속성이 새는가 | P05 |
| Lifecycle Assurance | evidence coverage, data lineage completeness | 보안 주장을 뒷받침할 증거가 있는가 | P02 |
| Operational Feasibility | latency, compute cost, alert burden | 실제 운영 가능한 방어인가 | P02–P04 |
| Reproducibility | seed, config, code, logs, DOI | 동일 결과와 주장을 검토할 수 있는가 | P02 |

---

## 8. 핵심 수식 묶음

### 8.1 보증 증거 커버리지

$$
Coverage_E = \frac{|R_{covered}|}{|R_{total}|}
$$

| 기호 | 의미 |
|---|---|
| $Coverage_E$ | 보증 증거 커버리지 |
| $R_{covered}$ | 증거가 있는 요구사항 또는 통제항목 |
| $R_{total}$ | 전체 요구사항 또는 통제항목 |

### 8.2 Precision, Recall, F1

$$
Precision = \frac{TP}{TP + FP}
$$

$$
Recall = \frac{TP}{TP + FN}
$$

$$
F1 = \frac{2 \cdot Precision \cdot Recall}{Precision + Recall}
$$

### 8.3 Robust Accuracy와 ASR

$$
RobustAcc = \frac{1}{n}\sum_{i=1}^{n} \mathbf{1}\left[f_{\theta}(x_i + \delta_i^{adv}) = y_i\right]
$$

$$
ASR = \frac{1}{n}\sum_{i=1}^{n} \mathbf{1}\left[f_{\theta}(x_i + \delta_i^{adv}) \neq y_i\right]
$$

### 8.4 Membership Inference Advantage

$$
Adv_{MI} = \Pr[A(z)=1 \mid z \in D_{train}]
- \Pr[A(z)=1 \mid z \notin D_{train}]
$$

### 8.5 차등프라이버시 기본식

$$
\Pr[M(D) \in S] \leq e^{\epsilon} \Pr[M(D') \in S] + \delta
$$

---

## 9. 재현성 체크리스트

| 항목 | 필수 기록 | W01 적용 |
|---|---|---|
| 문헌 | DOI, URL, 로컬 PDF명, 검증 상태 | P01–P05 summary에 반영 |
| 데이터 | 출처, 버전, split, 라벨 기준 | synthetic/toy data 기준 |
| 코드 | 실행 스크립트, commit, dependency | repo 관리 |
| 설정 | seed, hyperparameter, model version | seed 42 등 기록 |
| 결과 | metric CSV/JSON, 그림, 로그 | outputs 파일 기준 |
| 한계 | toy/synthetic 일반화 제한 | 실제 운영 성능으로 해석 금지 |
| AI 활용 | 사용 도구, 목적, 검증 방식 | AI 활용 고지 필요 |

---

## 10. 기말논문 반영 구조

| 기말논문 장 | W01 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 평가는 정확도 중심 접근을 넘어 생명주기 기반으로 확장되어야 함 |
| 2장 관련연구 | 딥러닝 원리, ML 생명주기 보증, IDS, 대적 공격, 프라이버시 공격 문헌 정리 |
| 3장 위협모형 | 데이터·모델·입력·출력·로그를 보호 자산으로 정의하고 공격자 능력 분리 |
| 4장 연구방법 | clean, detection, robust, privacy, lifecycle, reproducibility 지표 설계 |
| 5장 실험/분석 | toy/synthetic 실험은 평가 절차 예시로 사용하고 실제 보안성 입증으로 과장하지 않음 |
| 6장 보안적 함의 | CIA, privacy, safety, accountability 관점으로 해석 |
| 7장 결론 | W02 이후 poisoning, RAG, LLM, MLOps 보안으로 확장 가능한 기준 프레임 제시 |

---

## 11. W01 기말논문 연결 3문장

1. W01에서 기말논문에 반영할 개념: 딥러닝 기반 AI 시스템의 보안성은 모델 정확도만으로 판단할 수 없고, ML 생명주기 전 단계의 증거와 공격 조건별 성능을 함께 평가해야 한다.
2. W01에서 기말논문에 반영할 표·그림·실험: ML 생명주기 위협모형 그림, 문헌 5편 비교표, confusion matrix, robust accuracy/ASR 계산식, MI advantage 수식, evidence checklist를 반영한다.
3. W01이 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG와 LLM 시스템에서도 문서 수집, 임베딩, 검색, 프롬프트 구성, 응답 생성, 로그 감사가 생명주기로 관리되어야 하며, W01의 clean/robust/privacy/reproducibility 평가축을 W07/W08/W14로 확장한다.

---

## 12. 최종 판단

W01의 5개 문헌은 다음 역할로 정리한다.

| 문헌 | 최종 판단 |
|---|---|
| P01 | AI 원리의 핵심 배경 문헌. 표현학습과 역전파 설명에 사용 |
| P02 | W01 전체의 중심 프레임. 생명주기 보증과 evidence 구조의 핵심 문헌 |
| P03 | 보안 탐지 평가 지표 문헌. accuracy 한계와 오탐·미탐 문제 설명에 사용 |
| P04 | 대적 강건성 관련 문헌. 단, 강의계획서 지정 논문과 동일 여부 확인 필요 |
| P05 | 프라이버시 공격 문헌. accuracy/robustness와 별개인 leakage risk 축 설명에 사용 |

W01은 후속 주차 전체를 묶는 기준 주차다. 이후 W02 데이터 오염, W08 RAG 프롬프트 인젝션, W14 MLOps 보안은 모두 W01의 생명주기 보증, 위협모형, 평가지표, 재현성 기준 위에서 해석하는 것이 적절하다.

---

## 13. 변환 호환성 메모

- 모든 핵심 수식은 Markdown 표 밖에 LaTeX block math로 작성했다.
- 변수 설명은 표로 분리했다.
- GitHub Markdown, MS Word, PDF 변환을 모두 고려했다.
- DOCX/PDF 변환 시 다음 명령을 권장한다.

```bash
pandoc w01_integrated_summary_100point.md -o w01_integrated_summary_100point.docx
pandoc w01_integrated_summary_100point.md -o w01_integrated_summary_100point.pdf --pdf-engine=xelatex
```
