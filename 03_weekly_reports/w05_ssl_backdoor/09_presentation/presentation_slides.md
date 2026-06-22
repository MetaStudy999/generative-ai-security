# W05 자기지도학습·파운데이션 모델 & Poisoning/Backdoor

## 발표 핵심

표현학습 기반 모델의 보안 평가는 clean 성능 하나로 끝나지 않는다. Trigger 조건의 ASR, representation shift, defense check, 재현성 근거를 분리해야 한다.

---

# 1. 왜 W05가 중요한가

- Foundation model은 대규모 pretraining 표현을 여러 task에 전이한다.
- Pretraining 데이터와 augmentation pair가 오염되면 표현공간 자체가 흔들릴 수 있다.
- W05의 질문: “좋은 representation”은 backdoor 조건에서도 안전한가?

---

# 2. 발표 로드맵

1. 자기지도학습과 표현학습 원리
2. Contrastive/masked/predictive learning
3. Poisoning과 backdoor 위협
4. 논문 5편의 역할
5. Synthetic toy 실험과 결과
6. 기말논문 연결

---

# 3. AI 원리 70%: Self-Supervised Learning

- 사람이 붙인 라벨 없이 데이터 자체에서 supervision signal을 만든다.
- 학습 목표는 downstream task에 전이 가능한 representation이다.
- Foundation model은 대규모 pretraining 표현을 여러 task에 재사용한다.
- 핵심 보안 질문은 표현공간이 신뢰 가능한지 여부다.

---

# 4. AI 원리 70%: 주요 방법

| 방법 | 핵심 | 보안 연결 |
|---|---|---|
| Contrastive learning | positive pair를 가깝게, negative pair를 멀게 | pair 오염과 false positive |
| Masked modeling | 입력 일부를 가리고 복원 | corpus 오염과 memorization |
| Predictive learning | 미래/문맥을 예측 | temporal trigger와 drift |
| Transfer learning | pretraining 표현 전이 | downstream 취약성 전파 |

---

# 5. 보안 이슈 30%

| 위협 | 공격자 능력 | 대표 지표 |
|---|---|---|
| Poisoning | pretraining sample 삽입 | clean/poisoned 성능 차이 |
| Backdoor | trigger 조건 target behavior 유도 | ASR |
| Representation shift | embedding을 target 영역으로 이동 | mean shift |
| Governance gap | 출처·로그 불명확 | reproducibility |

---

# 6. 논문 5편의 역할

| ID | 중심 역할 | W05 활용 |
|---|---|---|
| P01 | SSL 알고리즘 survey | 원리 taxonomy |
| P02 | SSL for recommendation | 응용 도메인과 SSL objective |
| P03 | Video SSL survey | temporal/cross-modal representation |
| P04 | Poisoning survey | 공격·방어 taxonomy |
| P05 | Backdoor survey | DNN-LLM backdoor 연결 |

---

# 7. 위협모형

```text
Pretraining data -> SSL objective -> Embedding space -> Downstream classifier
       |                 |                 |                  |
 poisoned sample     poisoned pair      trigger shift      target class
```

- 보호 자산: 데이터, embedding, downstream label, config/log
- 공격 경로: corpus 오염, trigger 삽입, fine-tuning 전파
- 제외 범위: 실제 서비스 공격, 실제 개인정보, 악용 가능한 절차

---

# 8. 평가 프로토콜

| 평가 항목 | 지표 | 기록 방법 |
|---|---|---|
| Clean performance | clean accuracy | 정상 synthetic embedding |
| Backdoor impact | ASR | trigger 후 target 분류 |
| Representation change | mean shift | embedding 거리 |
| Defense check | detection rate, clean FPR | paired-view consistency |
| Reproducibility | seed, config, outputs | CSV/JSON/run log |

---

# 9. Synthetic toy 실험

- 데이터: synthetic 2D representation clusters
- 분류기: nearest-centroid representation classifier
- 공격: source embedding에 trigger vector를 더해 target centroid 쪽으로 이동
- 방어 점검: paired-view distance threshold
- 출력: `metrics_summary.csv`, `results.json`, `run_log.md`

안전 범위: 실제 개인정보와 실제 서비스 공격 없음.

---

# 10. 실험 결과

| 조건 | Clean | Poisoned Clean | ASR | ASR after defense | Shift |
|---|---:|---:|---:|---:|---:|
| Clean baseline | 1.000000 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 |
| Backdoor scenario | 해당 없음 | 1.000000 | 1.000000 | 해당 없음 | 2.418677 |
| Defense check | 해당 없음 | 해당 없음 | 해당 없음 | 0.000000 | 0.090597 |

정량값은 `04_experiment/outputs/run_log.md` 기준이다.

---

# 11. 결과 해석과 한계

- Triggered source embedding은 toy 조건에서 target centroid로 모두 분류됐다.
- Consistency threshold는 trigger shift를 모두 플래그했고 clean FPR은 0.000000이었다.
- 이는 toy 설정의 관찰값이며 실제 SSL/foundation model 보안 성능으로 일반화하지 않는다.
- 핵심은 수치 자체보다 지표 분리와 재현성 기록 방식이다.

---

# 12. 기말논문 연결

| 기말논문 장 | 연결 내용 |
|---|---|
| 관련연구 | SSL/foundation survey와 poisoning/backdoor survey 연결 |
| 위협모형 | pretraining data, embedding, downstream classifier |
| 평가방법 | clean, ASR, shift, detection, reproducibility |
| 분석/실험 | synthetic toy 평가를 통한 지표 구조 예시 |

Contribution 후보: 표현학습 기반 AI 시스템의 poisoning/backdoor 평가 프레임워크.

---

# 13. 결론

W05 결론:

- 표현공간은 AI 보안의 핵심 보호 자산이다.
- Backdoor 평가는 clean 성능과 trigger 조건을 분리해야 한다.
- Representation shift는 toy 환경에서 설명 가능한 보안 평가축이다.
- DOI/URL, seed, config, outputs가 있어야 제출 수치를 주장할 수 있다.
