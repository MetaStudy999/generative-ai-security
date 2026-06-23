# P03 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 지정 논문 제목 | Differential Privacy in Deep Learning: A Literature Survey |
| 지정 논문 저자 | 강의자료: Zizheng Pan et al.; Crossref 공식 메타데이터: Ke Pan, Yew-Soon Ong, Maoguo Gong, Hui Li, A.K. Qin, Yuan Gao |
| 지정 논문 학술지 | Neurocomputing 589, Article 127663, 2024-07 |
| 지정 논문 DOI | `10.1016/j.neucom.2024.127663` |
| 로컬 PDF 제목 | Differentially Private Federated Learning: A Systematic Review |
| 로컬 PDF 저자 | Jie Fu, Yuan Hong, Xinpeng Ling, Leixia Wang, Xun Ran, Zhiyu Sun, Wendy Hui Wang, Zhili Chen, Yang Cao |
| PDF 파일명 | `03_SUBSTITUTE_Fu_et_al_2024_Differentially_Private_FL_Review.pdf` |
| 검증 상태 | DOI는 Neurocomputing 지정 논문과 연결됨. 단 강의자료 저자명 표기와 공식 메타데이터가 달라 최종 확인 필요. 로컬 PDF는 지정 논문과 불일치 |

## 2. 한 문장 요약

> 지정 논문은 deep learning 전반의 DP 적용을 다루는 문헌으로 쓰고, 현재 로컬 대체 PDF는 FL에서 DP model, 보호 대상, privacy level을 구분하는 보완 문헌으로 사용한다.

## 3. 연구문제

딥러닝 또는 연합학습에서 DP가 어느 지점의 정보를 보호하는지, central DP/local DP/shuffle model의 차이가 threat model과 평가 지표에 어떤 차이를 만드는지를 묻는다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Central DP | 신뢰 가능한 중앙 주체가 noise/accounting을 관리하는 가정 | 중앙 학습 위협모형 |
| Local DP | 데이터 제공자 쪽에서 randomization을 수행하는 가정 | 사용자 단말 보호 |
| Shuffle model | local randomization과 중앙 분석 사이의 중간 모델 | 시스템 설계 대안 |
| FL privacy object | sample, client, update 등 보호 대상의 층위 구분 | W10/W11 연결 |

## 5. 방법론

지정 논문은 deep learning DP survey로 다루고, 로컬 대체 PDF는 DP-FL systematic review로 별도 표시한다. 본 보고서에서는 대체 PDF의 내용을 FL 확장 한계와 privacy object 분류에만 제한적으로 사용한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Gaussian Mechanism |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$M(x)=f(x)+\mathcal{N}(0,\sigma^2\Delta_2(f)^2I)$$ |
| 기호·입력·출력 | \(f\): 질의 또는 통계 함수, \(\Delta_2(f)\): L2 sensitivity, \(\sigma\): noise scale |
| 직관적 의미 | Gaussian Mechanism는 Differential Privacy·Membership Inference 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Differential Privacy·Membership Inference 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | epsilon/delta, noise multiplier, utility drop, MI risk |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

DP는 적용 위치와 공격자 가정에 따라 의미가 달라진다. 같은 epsilon이라도 중앙 학습, local collection, federated update 보호에서 해석과 유틸리티 손실이 달라질 수 있다.

## 7. 보안 관점 분석

P03은 W11을 W10 연합학습 보안과 연결한다. membership inference risk는 학습 완료 후 model output뿐 아니라 FL training update에서도 고려될 수 있으므로 보호 자산을 명확히 적어야 한다.

## 8. 한계와 오픈문제

주의: W11의 P03은 지정 논문과 로컬 PDF가 불일치한다. 현재 로컬 PDF는 Fu et al.의 DP-FL systematic review이므로, 최종 제출 전 Pan et al.의 지정 논문 원문 PDF 또는 공식 출판 페이지를 확보해야 한다. 또한 DOI `10.1016/j.neucom.2024.127663`의 공식 메타데이터는 `Ke Pan et al.`로 확인되어, 강의자료의 `Zizheng Pan et al.` 표기는 최종 확인 필요 상태로 둔다.

## 9. 기말 논문에 반영할 부분

DP 평가표에 `보호 대상`, `적용 위치`, `공격자 관측 가능성`, `accounting 단위`를 추가하는 근거로 사용한다.
