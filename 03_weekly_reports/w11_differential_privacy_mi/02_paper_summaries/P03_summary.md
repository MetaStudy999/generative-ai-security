# P03 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 지정 논문 제목 | Differential Privacy in Deep Learning: A Literature Survey |
| 지정 논문 저자 | Zizheng Pan et al. |
| 지정 논문 학술지 | Neurocomputing |
| 지정 논문 DOI | `10.1016/j.neucom.2024.127663` |
| 로컬 PDF 제목 | Differentially Private Federated Learning: A Systematic Review |
| 로컬 PDF 저자 | Jie Fu, Yuan Hong, Xinpeng Ling, Leixia Wang, Xun Ran, Zhiyu Sun, Wendy Hui Wang, Zhili Chen, Yang Cao |
| PDF 파일명 | `03_SUBSTITUTE_Fu_et_al_2024_Differentially_Private_FL_Review.pdf` |
| 검증 상태 | 지정 논문과 로컬 PDF 불일치. 제출본에서는 대체 문헌으로 명시 |

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

## 6. 주요 결과

DP는 적용 위치와 공격자 가정에 따라 의미가 달라진다. 같은 epsilon이라도 중앙 학습, local collection, federated update 보호에서 해석과 유틸리티 손실이 달라질 수 있다.

## 7. 보안 관점 분석

P03은 W11을 W10 연합학습 보안과 연결한다. membership inference risk는 학습 완료 후 model output뿐 아니라 FL training update에서도 고려될 수 있으므로 보호 자산을 명확히 적어야 한다.

## 8. 한계와 오픈문제

현재 로컬 PDF가 지정 논문과 다르다. 최종 제출이나 기말논문 인용에서는 Neurocomputing 지정 논문 원문을 확보하고, Fu et al. 대체 문헌은 FL 보완 참고문헌으로 분리해야 한다.

## 9. 기말 논문에 반영할 부분

DP 평가표에 `보호 대상`, `적용 위치`, `공격자 관측 가능성`, `accounting 단위`를 추가하는 근거로 사용한다.
