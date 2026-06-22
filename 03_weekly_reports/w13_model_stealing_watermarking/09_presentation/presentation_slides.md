# W13 모델 지식재산·모델 도난·모델 추출 위협

모델 추출 위험은 fidelity로, 소유권 검증은 detection과 false positive로 본다.

---

## 오늘의 질문

- API 뒤에 있는 모델도 훔쳐질 수 있는가?
- query-response만으로 얼마나 비슷한 모델을 만들 수 있는가?
- 워터마크 검출률이 높으면 소유권 증거로 충분한가?

---

## 문헌 5편의 역할

| 문헌 | 역할 |
|---|---|
| P01 | model stealing taxonomy |
| P02 | LLM watermarking |
| P03 | DNN watermarking trade-off |
| P04 | ModelShield |
| P05 | GAN privacy/security |

---

## AI 원리 70%

- Model IP는 파라미터, 행동, 생성물 출처를 포함한다.
- Model extraction은 query-response로 substitute model을 학습한다.
- Fidelity는 victim과 substitute의 출력 일치율이다.
- Watermark/fingerprint는 소유권 검증 신호다.

---

## 보안 이슈 30%

- Confidentiality: 모델 행동 유출
- Integrity: 워터마크 제거·위조
- Availability: query abuse
- Accountability: false positive/false negative

---

## Toy 실험 설계

| 항목 | 설정 |
|---|---|
| 데이터 | synthetic binary classification |
| Victim | toy logistic classifier |
| Substitute | query-response 1NN classifier |
| Query budgets | 100, 500, 1000 |
| Watermark | 20개 trigger-set signature |

---

## 실험 결과

| 조건 | Fidelity | Accuracy | Detection | FPR |
|---|---:|---:|---:|---:|
| Query 100 | 0.864000 | 0.812000 | 0.700000 | 0.600000 |
| Query 500 | 0.920000 | 0.840000 | 1.000000 | 0.600000 |
| Query 1000 | 0.902000 | 0.822000 | 1.000000 | 0.600000 |

---

## 해석

- query-response만으로 victim behavior에 접근할 수 있다.
- detection이 높아도 false positive가 높으면 소유권 증거가 약하다.
- 본 결과는 실제 API가 아닌 synthetic toy 평가다.

---

## 기말논문 연결

- 모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크
- 지표: fidelity, query cost, detection, FPR, utility, reproducibility
- W14/W15와 연결해 운영 로그와 연구윤리까지 확장

---

## 결론

모델 IP 보호 평가는 공격 성공률 하나로 끝나지 않는다.  
fidelity, detection, false positive, utility, 재현성을 함께 보고해야 한다.
