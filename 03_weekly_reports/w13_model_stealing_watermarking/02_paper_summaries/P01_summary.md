# P01 Summary

## I Know What You Trained Last Summer: A Survey on Stealing Machine Learning Models and Defences — Daria/Daryna Oliynyk et al., ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W13 Model Stealing & Watermarking |
| 논문명 | I Know What You Trained Last Summer: A Survey on Stealing Machine Learning Models and Defences |
| 출판 정보 | ACM Computing Surveys, Vol. 55, Issue 14s, pp. 1–41 |
| DOI | https://doi.org/10.1145/3595292 |
| 검증 상태 | W13 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 VOR가 아닌 accepted/arXiv 계열 메타데이터 포함 |

---

## 1. 한 문장 요약

이 논문은 model stealing을 **black-box query, surrogate model, model extraction, functionality stealing, fidelity, query budget, defense, watermark** 관점에서 정리하며, W13의 핵심 모델 IP 보호 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | 공격자는 모델 API 질의만으로 어느 정도 모델 기능을 복제할 수 있는가? |
| RQ2 | 모델 추출 공격의 성공은 fidelity, accuracy, query budget으로 어떻게 평가되는가? |
| RQ3 | 방어자는 rate limit, output restriction, watermark, monitoring으로 어떻게 대응하는가? |

---

## 3. 핵심 수식

$$
Fidelity=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[f_{victim}(x_i)=f_{stolen}(x_i)]
$$

$$
ExtractionCost=N_{queries}\cdot Cost_{query}
$$

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | 모델 파라미터, decision boundary, API output, training investment |
| 공격자 목표 | 기능 복제, 대체 모델 학습, IP 침해, 방어 회피 |
| 공격자 능력 | black-box query, confidence/logit 관찰, synthetic input 생성 |
| 지표 | fidelity, stolen accuracy, query budget, detection rate, watermark verification |

---

## 5. 기말논문 연결

P01은 모델 IP와 API 보안의 기본 문헌이다. 기말논문에서는 LLM/RAG 서비스의 모델·프롬프트·문서 인덱스가 추출 대상이 될 수 있음을 설명하는 근거로 사용한다.

---

## 6. 최종 판단

P01은 W13의 중심 문헌이다. 모델 공개 API의 유용성과 IP 보호·남용 방지를 함께 평가해야 한다.
