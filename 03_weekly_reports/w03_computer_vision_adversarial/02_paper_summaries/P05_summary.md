# P05 요약: A Survey of Robustness and Safety of 2D and 3D Deep Learning Models against Adversarial Attacks

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A Survey of Robustness and Safety of 2D and 3D Deep Learning Models against Adversarial Attacks |
| 저자 | Yanjie Li, Bin Xie, Songtao Guo, Yuanyuan Yang, Bin Xiao |
| 학술지 | *ACM Computing Surveys* |
| 권호/쪽 | 56(6), 1-37 |
| 연도 | 2024 |
| DOI/URL | https://doi.org/10.1145/3636551 |
| PDF 파일명 | `05_Li_et_al_2024_Robustness_Safety_2D_3D_Adversarial_Attacks.pdf` |
| 검증 상태 | Crossref/ACM URL 및 로컬 PDF 제목 일치 확인 |

## 2. 한 문장 요약

2D 이미지와 3D 비전 모델의 adversarial attack, physical attack, defense, robustness/safety 평가를 위협모형 관점에서 체계화한 W03의 핵심 보안 survey 문헌이다.

## 3. 연구문제

2D/3D deep learning 모델은 어떤 adversarial attack과 physical-world attack에 취약하며, 이를 평가·방어·안전성 관점에서 어떻게 분류할 수 있는지를 다룬다.

## 4. 핵심 방법

| 요소 | 내용 | W03 연결 |
|---|---|---|
| Threat model | 공격자 지식, 능력, 목표, 공격면을 분류한다. | W03 위협모형 핵심 근거 |
| 2D adversarial attacks | 이미지 교란, semantic-preserving perturbation 등을 정리한다. | 이미지 입력 보안 |
| 3D adversarial attacks | point cloud, LiDAR, 3D perception 취약성을 다룬다. | 물리/3D 안전성 |
| Physical safety | 실제 환경 안전 위반 가능성을 논의한다. | 안전성 평가 |

## 5. AI 원리 기여

P05는 AI 원리 자체보다는 보안 평가 관점에 무게가 있다. 그러나 2D/3D 데이터 구조와 모델 입력 형태가 다르면 공격면과 강건성 평가도 달라진다는 점을 보여주므로, 표현학습 구조와 보안성의 연결을 설명하는 데 필요하다.

## 6. 보안 위협 연결

P05는 W03의 보안 이슈 30%를 직접 뒷받침한다. white-box, black-box, transfer, physical, 3D attack 등은 모두 공격자 지식과 능력을 분리해 기록해야 하며, 평가 지표는 clean accuracy, robust accuracy, ASR, robust drop, confusion matrix, safety impact로 분리해야 한다.

## 7. 평가 지표와 한계

robust accuracy, ASR, defense success, safety impact 등은 W03 평가 프로토콜의 핵심 지표다. 다만 본 주차 실험은 synthetic 8x8 막대 이미지와 nearest-centroid 모델을 사용한 toy protocol이므로, P05가 다루는 실제 2D/3D 모델 공격 성능을 재현했다고 해석하면 안 된다.

## 8. 출판연도 및 파일명 메모

강의계획서에는 2023년 또는 축약 저자 `Z. Li et al.`로 적혀 있으나 Crossref 기준 최종 출판 정보는 2024년, 저자는 Yanjie Li et al.이다. 로컬 PDF 파일명에 `2024`가 포함된 것은 최종 출판연도와 일치한다.

## 9. 기말 논문 활용

W03 기말논문 연결에서 가장 직접적인 보안 근거로 사용한다. 특히 threat model, clean/robust metric separation, physical/3D safety scope, 재현성 증거 보존 항목을 설계할 때 핵심 참고문헌으로 반영한다.
