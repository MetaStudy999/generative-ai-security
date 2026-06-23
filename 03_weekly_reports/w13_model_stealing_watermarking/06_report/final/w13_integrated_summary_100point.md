# W13 100점형 통합 Summary

## Model Stealing & Watermarking

## 0. 문서 목적

이 문서는 W13 개별 논문 summary 5개를 기말논문 작성용 연구 노트로 통합한 100점형 요약본이다. 모델 추출, 모델 IP, 워터마킹, fingerprinting, provenance를 하나의 보안 평가체계로 묶는다.

---

## 1. 한 문장 통합 요약

W13은 AI 모델을 **서비스 API이자 지식재산 자산**으로 보고, model stealing·extraction·watermarking·fingerprinting·ownership verification·generated artifact provenance를 fidelity, query budget, watermark robustness, FPR/FNR, utility drop으로 평가해야 함을 정리하는 주차다.

---

## 2. 문헌 5편 통합 매트릭스

| ID | 논문 | 핵심 역할 | 주요 지표 |
|---|---|---|---|
| P01 | Model stealing survey | 모델 추출 위협 핵심 | fidelity, query budget |
| P02 | LLM watermark/fingerprint | LLM 산출물·소유권 보호 | detection score, FPR/FNR |
| P03 | DNN watermarking survey | DNN ownership verification | watermark verification, robustness |
| P04 | ModelShield | 추출 공격 후 watermark 방어 | watermark accuracy, extraction fidelity |
| P05 | GAN attack/defense | 생성모형 provenance 연결 | generated risk, provenance coverage |

---

## 3. 핵심 수식 묶음

$$
Fidelity=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[f_{victim}(x_i)=f_{stolen}(x_i)]
$$

$$
Verify(f_w,K)=\mathbf{1}[Score(f_w,K)>\tau]
$$

$$
WatermarkAcc=\frac{1}{|T_w|}\sum_{(x,y)\in T_w}\mathbf{1}[f(x)=y]
$$

$$
FPR=\frac{FP}{FP+TN}, \qquad FNR=\frac{FN}{FN+TP}
$$

---

## 4. 통합 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | model weights, decision boundary, API output, trigger set, watermark key, generated output |
| 공격자 목표 | model extraction, watermark removal, false ownership claim, IP theft |
| 공격자 능력 | black-box query, surrogate training, fine-tuning, pruning, paraphrase, output rewriting |
| 방어자 능력 | watermarking, fingerprinting, rate limit, output restriction, monitoring, provenance log |
| 제외 범위 | 실제 API 무단 추출, 저작권 침해 목적 모델 복제 |

---

## 5. 통합 평가 지표

| 평가축 | 대표 지표 | 해석 |
|---|---|---|
| Extraction Risk | fidelity, stolen accuracy, query budget | 모델 도난 위험 |
| Ownership | watermark verification, fingerprint match | 소유권 증명 |
| Robustness | watermark survival after pruning/fine-tuning | 방어 내구성 |
| Utility | clean accuracy, utility drop | 정상 성능 손실 |
| Error Risk | FPR/FNR | 허위 소유권·검출 실패 위험 |
| Auditability | key, trigger hash, query log | 사후 검증 가능성 |

---

## 6. 기말논문 연결 3문장

1. W13에서 기말논문에 반영할 개념: 모델과 생성물은 보안 자산이며, API 질의·출력·워터마크·fingerprint·provenance를 통해 소유권과 무단 복제를 평가해야 한다.
2. 반영할 표·그림·실험: model stealing threat model, fidelity/query budget 수식, watermark verification, FPR/FNR, utility drop 비교표를 반영한다.
3. W14 연결: 모델 IP 보호는 MLOps 배포·API 로그·모델 버전·승인 기록과 결합되어야 하므로 운영 감사 체계로 확장한다.

---

## 7. 최종 판단

W13은 생성형 AI 서비스의 지식재산 보호와 책임성을 다루는 핵심 주차다. RAG/LLM 서비스에서는 모델 자체뿐 아니라 prompt template, retrieval index, generated content provenance도 보호 자산으로 본다.
