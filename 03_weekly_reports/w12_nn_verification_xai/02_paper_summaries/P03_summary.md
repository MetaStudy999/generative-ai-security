# P03 논문 요약

## 1. 서지와 검증 상태

| 항목 | 내용 |
|---|---|
| 강의 지정 제목 | Adversarial machine learning attacks against explainable artificial intelligence: A review |
| 강의 지정 저자 | G. Vadillo et al. |
| 공식 DOI 후보 | `10.1002/widm.1567` |
| 공식 URL | https://doi.org/10.1002/widm.1567 |
| 공식 메타데이터 | Jon Vadillo, Roberto Santana, Jose A. Lozano, "Adversarial Attacks in Explainable Machine Learning: A Survey of Threats Against Models and Humans", WIREs Data Mining and Knowledge Discovery, Vol. 15, Issue 1, Article e1567 |
| 강의 표기와 차이 | 공식 published title이 강의 표기 제목과 다름 |
| 로컬 PDF | `03_SUBSTITUTE_Baniecki_Biecek_2023_Adversarial_XAI_Survey.pdf` |
| 로컬 PDF 상태 | Baniecki/Biecek adversarial XAI survey. 지정 논문 원문 아님 |

주의: W12의 P03은 지정 논문과 로컬 PDF가 불일치한다. 현재 로컬 PDF는 Baniecki/Biecek 2023 adversarial XAI 관련 대체 문헌이므로, 최종 제출 전 G. Vadillo et al. 지정 논문 원문 PDF 또는 공식 출판 페이지를 확보해야 한다.

## 2. 핵심 연구문제

P03은 XAI 설명이 대적 조작의 대상이 될 수 있음을 다룬다[3]. 예측 결과가 유지되는 것처럼 보여도 saliency, feature attribution, counterfactual explanation이 크게 바뀌면 human review와 accountability가 약해진다.

## 3. W12에서의 역할

| 관점 | 요약 |
|---|---|
| AI 원리 | feature attribution, saliency, explanation stability, explanation similarity |
| 보안 연결 | misleading explanation, fairwashing, accountability failure |
| 평가 지표 | explanation stability, attribution similarity, explanation robustness |
| 한계 | 로컬 PDF가 지정 Vadillo 논문이 아니라 대체 문헌임 |
| 내 논문 활용 | XAI stability를 별도 보안 평가축으로 넣는 근거 |

## 4. 실습 연결

W12 실험은 feature attribution의 cosine similarity로 `explanation_stability`를 계산한다. 이 값은 실제 모든 XAI 공격 방어를 의미하지 않는다. 설명 조작 가능성을 안전하게 보여주는 toy 지표다.

## 5. 최종 제출 전 확인 항목

- WIREs 공식 페이지에서 최종 제목, 권호, Article e1567, DOI를 대조한다.
- Baniecki/Biecek PDF는 SUBSTITUTE로 표시한다.
- 본문에서 P03을 인용할 때 공식 제목 차이를 각주 또는 검증표에 남긴다.
