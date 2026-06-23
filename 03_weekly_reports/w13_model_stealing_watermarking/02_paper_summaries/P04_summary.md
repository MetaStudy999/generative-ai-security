# P04 Summary

## ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack — Kaiyi Pang et al., IEEE TIFS, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W13 Model Stealing & Watermarking |
| 논문명 | ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack |
| 출판 정보 | IEEE Transactions on Information Forensics and Security, Vol. 20, pp. 1767–1782, 2025 |
| DOI | https://doi.org/10.1109/TIFS.2025.3530691 |
| 검증 상태 | W13 `paper_list.md` 기준 IEEE DOI와 arXiv판 일치 확인 |

---

## 1. 한 문장 요약

이 논문은 model extraction attack 이후에도 소유권을 검증할 수 있는 adaptive and robust watermarking 방식을 제안하며, W13에서 model stealing 방어를 실험적으로 평가하는 핵심 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | Model extraction 이후에도 watermark를 어떻게 유지·검증할 수 있는가? |
| RQ2 | Adaptive watermark는 공격자의 surrogate 학습을 어떻게 고려하는가? |
| RQ3 | Watermark robustness와 clean utility 사이의 trade-off는 어떻게 평가하는가? |

---

## 3. 핵심 수식

$$
WatermarkAcc=\frac{1}{|T_w|}\sum_{(x,y)\in T_w}\mathbf{1}[f(x)=y]
$$

$$
UtilityDrop=Acc_{clean}^{base}-Acc_{clean}^{wm}
$$

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | watermarked model, trigger set, ownership proof, API output |
| 공격자 목표 | model extraction 후 watermark 제거 또는 무력화 |
| 공격자 능력 | black-box query, surrogate training, fine-tuning, pruning |
| 지표 | watermark accuracy, clean accuracy, extraction fidelity, robustness after extraction |

---

## 5. 기말논문 연결

P04는 W13의 실험형 watermark defense 근거다. 기말논문에서는 RAG/LLM 모델 서비스의 API 추출 위험과 watermark 검증을 연결할 수 있다.

---

## 6. 최종 판단

P04는 W13의 방어 기술 핵심 문헌이다. 모델 추출 이후의 소유권 검증과 clean utility 유지 지표를 함께 제시한다.
