# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Deepfake Detection: A Comprehensive Survey from the Reliability Perspective |
| 저자 | Tianyi Wang, Xin Liao, Kam Pui Chow, Xiaodong Lin, Yinglong Wang |
| 학술지/학회 | ACM Computing Surveys |
| 출판 정보 | Vol. 57, No. 3, pages 1-35, online 2024-11-11, print issue 2025-03-31 |
| 연도 | 2024 online / 2025 print issue |
| DOI/URL | https://doi.org/10.1145/3699710, https://arxiv.org/abs/2211.10881 |
| PDF 파일명 | 05_Wang_et_al_2024_Deepfake_Detection_Reliability_Survey.pdf |
| 검증 상태 | DOI/URL 확인, 강의계획서 `J. Wang et al.` 표기 대응 확인 필요 |

## 2. 한 문장 요약

> 이 논문은 deepfake detection을 reliability 관점에서 재정리하며, transferability, interpretability, robustness가 실제 포렌식 활용의 핵심 조건임을 제시한다.

## 3. 연구문제

딥페이크 탐지기는 benchmark 성능이 높아도 unseen dataset, 압축, post-processing, 실제 사건 맥락에서 신뢰성을 잃을 수 있다. 이 논문은 탐지 모델의 reliability를 어떻게 정의하고, 임의의 의심 사례에 대해 어떤 근거로 판단할 수 있는지 묻는다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Transferability | 학습 데이터 밖 생성기·데이터셋으로 일반화 | cross-domain generalization |
| Interpretability | 탐지 판단의 근거 설명 가능성 | 포렌식 신뢰성 |
| Robustness | 압축·노이즈·후처리에 대한 안정성 | 보안 평가 조건 |
| Reliability metric | 탐지 결과를 실제 사용 맥락에서 신뢰할 수 있는지 평가 | W06 toy 실험 |
| Case study | 실제 사건 맥락에서 탐지기 사용 가능성 검토 | 보안적 함의 |

## 5. 방법론

기존 deepfake detection 연구를 reliability 중심으로 재분류한다. 본 W06 실험은 이 관점을 축소해, synthetic score distribution에서 in-domain과 cross-domain 성능 차이, review-band triage 효과를 수치로 기록했다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Reliability 관점 Balanced Error |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$BalancedError=\frac{FPR+FNR}{2}$$ |
| 기호·입력·출력 | FPR: 정상 콘텐츠 오탐률, FNR: deepfake 미탐률 |
| 직관적 의미 | Reliability 관점 Balanced Error는 Diffusion/GAN·Deepfake 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Diffusion/GAN·Deepfake 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | FPR, FNR, balanced error, compression robustness |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

Deepfake detection의 주요 과제는 transferability, interpretability, robustness로 요약된다. 특히 실제 포렌식에서는 단일 confidence score보다 불확실 구간의 human review, false positive/false negative trade-off가 중요하다.

## 7. 보안 관점 분석

P05는 W06 실험 설계와 가장 직접적으로 연결된다. cross-domain reliability stress에서 accuracy가 0.816667로 낮아지고 FNR이 0.200000으로 증가한 결과는, 탐지기 신뢰성을 domain shift 관점에서 분리 기록해야 함을 보여주는 toy 근거다.

## 8. 한계와 오픈문제

본 보고서의 실험은 실제 deepfake benchmark가 아닌 synthetic score 분포다. 따라서 P05의 reliability 개념을 설명하는 데만 사용하며, 실제 법적·포렌식 증거능력을 주장하지 않는다.

출판사 기준 첫 저자는 `Tianyi Wang`으로 확인된다. 강의계획서의 `J. Wang et al.` 표기는 현재 확인된 출판사 메타데이터와 다르므로 최종 제출 전 강의계획서 표기와 매칭 여부를 확인한다.

## 9. 기말 논문에 반영할 부분

기말 논문에서는 P05의 reliability 관점을 평가 프레임워크 핵심으로 삼고, FPR/FNR, AUROC, ECE, review rate, auto coverage를 함께 기록하는 절차를 제시한다.
