# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Deepfake Detection: A Comprehensive Survey from the Reliability Perspective |
| 저자 | Tianyi Wang, Xin Liao, Kam Pui Chow, Xiaodong Lin, Yinglong Wang |
| 학술지/학회 | ACM Computing Surveys |
| 연도 | 2024 |
| DOI/URL | https://doi.org/10.1145/3699710, https://arxiv.org/abs/2211.10881 |
| PDF 파일명 | 05_Wang_et_al_2024_Deepfake_Detection_Reliability_Survey.pdf |
| 검증 상태 | DOI/URL 확인 |

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

## 6. 주요 결과

Deepfake detection의 주요 과제는 transferability, interpretability, robustness로 요약된다. 특히 실제 포렌식에서는 단일 confidence score보다 불확실 구간의 human review, false positive/false negative trade-off가 중요하다.

## 7. 보안 관점 분석

P05는 W06 실험 설계와 가장 직접적으로 연결된다. cross-domain reliability stress에서 accuracy가 0.816667로 낮아지고 FNR이 0.200000으로 증가한 결과는, 탐지기 신뢰성을 domain shift 관점에서 분리 기록해야 함을 보여주는 toy 근거다.

## 8. 한계와 오픈문제

본 보고서의 실험은 실제 deepfake benchmark가 아닌 synthetic score 분포다. 따라서 P05의 reliability 개념을 설명하는 데만 사용하며, 실제 법적·포렌식 증거능력을 주장하지 않는다.

## 9. 기말 논문에 반영할 부분

기말 논문에서는 P05의 reliability 관점을 평가 프레임워크 핵심으로 삼고, FPR/FNR, AUROC, ECE, review rate, auto coverage를 함께 기록하는 절차를 제시한다.
