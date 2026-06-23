# P04 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 강의계획서 표기 | Y. Wang et al., "A Survey of Poisoning Attacks and Defenses on Machine Learning", ACM Computing Surveys, 2022 |
| 정식 제목 | Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems |
| 저자 | Zhibo Wang, Jingjing Ma, Xue Wang, Jiahui Hu, Zhan Qin, Kui Ren |
| 출판 정보 | ACM Computing Surveys, 55(7), Article 134, 1-36, 2022 |
| DOI/URL | `10.1145/3538707`; https://doi.org/10.1145/3538707 |
| 로컬 PDF | `04_Wang_et_al_2022_Threats_to_Training_Poisoning_Survey.pdf` |
| 검증 상태 | DOI/정식 제목 확인. 강의계획서 제목과 저자 표기 동일 여부 확인 필요 |

## 2. 제목/저자 차이 메모

현재 로컬 PDF와 Crossref 기준 제목은 `Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems`다. 강의계획서의 `A Survey of Poisoning Attacks and Defenses on Machine Learning` 및 `Y. Wang et al.` 표기는 정식 출판 메타데이터와 다르므로, 동일 논문 여부와 최종 출판 정보를 확인 필요 상태로 유지한다.

## 3. 한 문장 요약

이 논문은 machine learning training phase의 poisoning attack과 defense를 체계화하며, W05에서 data poisoning, clean-label poisoning, model poisoning, federated poisoning을 구분하는 핵심 보안 문헌이다[4].

## 4. 핵심 기여

| 구분 | 내용 |
|---|---|
| Training-time focus | 추론 시 adversarial example이 아니라 학습 단계 공격을 중심으로 다룬다 |
| Threat taxonomy | data poisoning, model poisoning, outsourcing/federated setting 등 공격면을 분류한다 |
| Defense taxonomy | sanitization, robust training, detection, reproducibility issue를 연결한다 |

## 5. 보안 관점

P04는 W05의 보안 축을 직접 담당한다. Self-supervised pretraining에서도 라벨이 없을 뿐 training pipeline은 여전히 데이터와 objective에 의존하므로, poisoned corpus나 조작된 augmentation은 representation과 downstream boundary를 왜곡할 수 있다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Poisoned Training Objective |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$\min_\theta\left[\sum_{(x,y)\in D}\ell(f_\theta(x),y)+\lambda\sum_{(\tilde{x},\tilde{y})\in D_p}\ell(f_\theta(\tilde{x}),\tilde{y})\right]$$ |
| 기호·입력·출력 | \(D\): 정상 데이터, \(D_p\): toy 오염 데이터, \(\lambda\): 오염 항 가중치 |
| 직관적 의미 | Poisoned Training Objective는 자기지도학습·Backdoor 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | 자기지도학습·Backdoor 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | poison rate, clean accuracy drop, target failure, ASR |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 한계와 확인 필요

- 강의계획서 제목/저자 표기와 로컬 PDF 정식 정보가 다르다.
- 실제 공격 절차를 단계별로 재현하지 않고, 위협모형과 평가 지표 수준에서만 인용한다.

## 7. 기말 논문 활용

학습 생명주기 기반 위협모형, clean accuracy와 attack impact 분리, poisoning 방어 평가표의 근거로 활용한다.
