# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Adversarial Attacks and Defenses in Machine Learning-Powered Networks: A Contemporary Survey |
| 저자 | Yulong Wang, Tong Sun, Shenghong Li, Xin Yuan, Wei Ni, Ekram Hossain, H. Vincent Poor |
| 학술지/학회 | arXiv preprint |
| 연도 | 2023 |
| DOI/URL | https://doi.org/10.48550/arXiv.2303.06302 |
| PDF 파일명 | 04_Wang_et_al_2023_Adversarial_Attacks_and_Defenses.pdf |
| 검증 상태 | arXiv 제목, 저자, 제출일, DOI 확인. 강의계획서 지정 IEEE COMST 논문과 동일 여부 확인 필요 |

주의: 본 W01 보고서의 P04는 강의계획서 지정 IEEE Communications Surveys & Tutorials 논문과 동일 여부를 최종 확인하지 못했거나, 대체 arXiv 논문으로 정리되었다. 최종 제출 전 강의계획서 지정 논문으로 교체하거나, 대체 논문 사용 사유를 교수자에게 설명해야 한다.

## 2. 한 문장 요약

> 이 논문은 ML 기반 네트워크와 딥러닝 분류 모델을 대상으로 한 대적 공격과 방어를 최신 공격 원리, 방어 전략, 평가 난점 중심으로 분류한다.

## 3. 연구문제

핵심 질문은 “ML-powered network에서 공격자는 어떤 방식으로 모델의 예측을 교란하고, 방어자는 어떤 기준으로 방어 효과를 검증해야 하는가”이다. W01에서는 대적 ML을 별도 기술이 아니라 ML 생명주기 중 추론·평가·배포 단계의 보안 위협으로 연결한다.

## 4. 핵심 개념

| 개념 | 설명 | 보안 연구 연결 |
|---|---|---|
| Adversarial example | 사람이 보기에는 작거나 무해한 변화가 모델 예측을 바꾸는 입력이다. | 추론 단계 무결성 위협 |
| White/black-box attack | 공격자가 모델 구조·파라미터·출력에 얼마나 접근 가능한지에 따른 구분이다. | threat model의 지식 수준 정의 |
| Robustness enhancement | adversarial training, regularization 등으로 모델 민감도를 낮추는 방어다. | clean accuracy와 robust accuracy의 trade-off 평가 |
| Gradient masking | 방어가 실제 강건성을 높이지 않고 gradient만 숨기는 현상이다. | 방어 검증에서 우회 공격과 transfer attack이 필요함을 시사 |

## 5. 방법론

최근 adversarial attack/defense 문헌을 공격 원리와 방어 메커니즘에 따라 분류하고, 각 방법의 강점과 한계를 비교한다. 본 보고서에서는 공격 재현 절차가 아니라 평가 항목과 방어 검증상의 주의점을 중심으로 정리했다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | 대적 교란 목적함수와 Robust Accuracy |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$\max_{\delta\in\mathcal{S}}\ell(f_\theta(x+\delta),y),\qquad RobustAcc=\frac{1}{n}\sum_i\mathbf{1}\{f_\theta(x_i+\delta_i)=y_i\}$$ |
| 기호·입력·출력 | \(\delta\): 허용된 교란, \(\mathcal{S}\): toy/synthetic 교란 집합, \(\ell\): 손실함수 |
| 직관적 의미 | 대적 교란 목적함수와 Robust Accuracy는 딥러닝·ML 보안 기본 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | 딥러닝·ML 보안 기본 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | ASR, robust accuracy, robust drop, clean accuracy |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

공격은 gradient 기반, score/decision 기반, search 기반, physical-world attack 등으로 확장되고 있다. 방어는 탐지, 입력 정제, robust training, regularization, 인증된 방어 등으로 나뉘지만, 많은 방어가 계산 비용, clean accuracy 감소, 공격 이전성, gradient masking 문제를 동시에 안고 있다.

## 7. 보안 관점 분석

P04는 W01의 보안 이슈 중 대적 머신러닝 축을 담당한다. 특히 모델이 “정상 데이터에서 높은 성능”을 보이는 것과 “공격자가 만든 입력에서 안전”한 것은 다른 주장임을 분명히 한다. 따라서 보안 보고서에는 clean accuracy, attack success rate, robust accuracy, 방어 후 성능 변화, 공격자 지식 수준을 함께 기록해야 한다.

## 8. 한계와 오픈문제

arXiv preprint 기준으로 정리했으므로 최종 출판 버전이 있다면 참고문헌 형식을 다시 확인해야 한다. 특히 강의계획서에는 IEEE Communications Surveys & Tutorials, 25(4), 2023, pp. 2245-2298 논문이 지정되어 있으므로, 현재 P04가 해당 논문과 동일한지 또는 대체 논문인지 최종 제출 전 확인해야 한다. 또한 survey 논문만으로 특정 방어의 실제 효과를 단정할 수 없으므로, 기말 논문에서는 제한된 toy 실험 또는 문헌 기반 비교 프로토콜을 별도로 둔다.

## 9. 기말 논문에 반영할 부분

기말 논문에서는 P04를 adversarial robustness 평가 장의 기준 문헌으로 사용한다. 특히 “방어 성능은 clean 성능, 공격 성공률, 공격자 지식, 계산 비용, 재현성 조건을 동시에 보고해야 한다”는 평가 원칙으로 반영한다.
