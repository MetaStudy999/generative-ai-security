# P03 Summary

## A Survey of Deep Neural Network Watermarking Techniques — Yue Li, Hongxia Wang, Mauro Barni, Neurocomputing, 2021

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W13 Model Stealing & Watermarking |
| 논문명 | A survey of Deep Neural Network watermarking techniques |
| 저자 | Yue Li, Hongxia Wang, Mauro Barni |
| 출판 정보 | Neurocomputing, Vol. 461, pp. 171–193, 2021 |
| DOI | https://doi.org/10.1016/j.neucom.2021.07.051 |
| 검증 상태 | W13 `paper_list.md` 기준 공식 DOI 확인. 강의계획서 저자명·제목 표기 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 DNN watermarking을 **white-box watermark, black-box trigger watermark, ownership verification, robustness, fidelity, capacity, security** 관점에서 정리하며, W13의 모델 소유권 보호 핵심 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | DNN watermark는 모델 내부 파라미터 또는 입력-출력 행동 중 어디에 삽입되는가? |
| RQ2 | Watermark 검증은 소유권 증명과 모델 추출 탐지에 어떻게 활용되는가? |
| RQ3 | Fine-tuning, pruning, distillation, model extraction 이후에도 watermark가 유지되는가? |

---

## 3. 핵심 수식

$$
Verify(f_w,K)=\mathbf{1}[Score(f_w,K)>\tau]
$$

$$
Robustness=\frac{N_{verified\ after\ attack}}{N_{verified\ before\ attack}}
$$

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | model ownership, weights, trigger set, watermark key |
| 공격자 목표 | watermark 제거, ownership 부인, model extraction 후 재배포 |
| 지표 | verification accuracy, FPR/FNR, robustness, fidelity loss, capacity |
| 재현성 | trigger set hash, key, threshold, attack condition, model version 기록 |

---

## 5. 기말논문 연결

P03은 모델 워터마킹의 기본 평가축을 제공한다. 기말논문에서는 모델·문서·생성물 provenance를 구분하고, ownership verification과 false claim risk를 함께 다룬다.

---

## 6. 최종 판단

P03은 W13의 DNN watermarking 핵심 문헌이다. 모델 IP 보호와 model stealing 방어 지표의 중심 근거로 사용한다.
