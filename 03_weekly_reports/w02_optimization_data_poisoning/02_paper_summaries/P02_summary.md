# P02 Summary

## Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better — Gaurav Menghani, ACM Computing Surveys, 2023

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W02 대규모 최적화 & 데이터 오염 위협 |
| 논문명 | Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better |
| 저자 | Gaurav Menghani |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 55, No. 12, pp. 1–37 |
| 연도 | 2023 |
| DOI | https://doi.org/10.1145/3578938 |
| 공개 원고 | https://arxiv.org/abs/2106.08962 |
| 논문 유형 | Survey / Efficient Deep Learning Review |
| 로컬 PDF | `01_papers/pdf/02_Menghani_2023_Efficient_Deep_Learning_Survey.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치. 단, 강의계획서의 `Gulzar Menghani` 표기는 출판 정보 기준 `Gaurav Menghani`로 정리 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | W02 `paper_list.md` 기준 ACM 최종판 DOI 확인 완료. Article 번호와 최종 출판 세부정보는 제출 전 ACM 페이지에서 재확인 필요 |

---

## 1. 한 문장 요약

이 논문은 딥러닝 모델을 더 작고 빠르고 효율적으로 만들기 위한 **압축, 경량 아키텍처, 효율적 학습, 추론 최적화, 시스템·하드웨어 수준 기법**을 폭넓게 정리하고, 성능만이 아니라 latency, memory, energy, model size, deployment constraint를 함께 평가해야 함을 제시하는 survey 논문이다.

---

## 2. 연구문제

이 논문의 핵심 연구문제는 다음과 같이 정리할 수 있다.

> 딥러닝 모델의 정확도를 유지하거나 개선하면서도 모델 크기, 연산량, 지연시간, 에너지 비용, 배포 제약을 줄이기 위해 어떤 효율화 기법을 선택해야 하는가?

### 세부 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | 딥러닝 모델 효율성은 accuracy 외에 어떤 footprint metric으로 평가해야 하는가? |
| RQ2 | pruning, quantization, distillation, efficient architecture는 각각 어떤 원리로 모델 비용을 줄이는가? |
| RQ3 | 학습 효율화와 추론 효율화는 어떤 지표와 trade-off로 비교할 수 있는가? |
| RQ4 | edge, mobile, cloud, embedded 환경의 배포 제약은 모델 선택과 보안 검증에 어떤 영향을 주는가? |
| RQ5 | 모델 경량화는 poisoning/backdoor 방어, 탐지 민감도, 재학습 비용, 감사 가능성에 어떤 영향을 줄 수 있는가? |

---

## 3. 핵심 이론 및 수식

> 작성 원칙: GitHub, MS Word, PDF 변환 호환성을 위해 수식은 표 안에 넣지 않고 별도 블록 수식으로 작성한다. 변수 설명은 Markdown 표로 분리한다.

### 3.1 다목적 효율성 점수

효율적 딥러닝 모델은 정확도만으로 선택할 수 없다. 품질과 비용을 함께 고려하는 다목적 점수로 표현할 수 있다.

$$
Score = Utility - \lambda_1 Latency - \lambda_2 Size - \lambda_3 Energy - \lambda_4 Memory
$$

| 기호 | 의미 |
|---|---|
| $Score$ | 모델 선택을 위한 종합 효율성 점수 |
| $Utility$ | accuracy, F1, robust accuracy 등 작업 성능 |
| $Latency$ | 추론 지연시간 |
| $Size$ | 모델 크기 또는 파라미터 수 |
| $Energy$ | 에너지 사용량 |
| $Memory$ | 추론 또는 학습 시 메모리 사용량 |
| $\lambda_1,\lambda_2,\lambda_3,\lambda_4$ | 각 비용 항목의 중요도 가중치 |

### 보안적 의미

보안 모델은 성능만 높아서는 부족하다. poisoning 탐지기, backdoor scanner, robust classifier가 너무 느리거나 무거우면 실제 배포 파이프라인에서 제외될 수 있다. 따라서 W02 보안 평가는 clean accuracy, ASR뿐 아니라 latency, retraining cost, audit cost도 함께 기록해야 한다.

---

### 3.2 압축률

모델 압축의 효과는 원본 모델 대비 압축 모델의 크기 비율로 표현할 수 있다.

$$
Compression\ Ratio = \frac{Size_{original}}{Size_{compressed}}
$$

| 기호 | 의미 |
|---|---|
| $Size_{original}$ | 압축 전 모델 크기 |
| $Size_{compressed}$ | 압축 후 모델 크기 |

### 보안적 의미

압축률이 높다고 항상 좋은 것은 아니다. pruning이나 quantization이 모델의 정상 성능, robust accuracy, backdoor trigger 반응, 탐지 민감도를 바꿀 수 있기 때문이다. 따라서 압축 모델은 clean 성능과 보안 지표를 동시에 재평가해야 한다.

---

### 3.3 유틸리티 손실

경량화 후 성능 변화를 다음과 같이 측정할 수 있다.

$$
\Delta Utility = Utility_{compressed} - Utility_{original}
$$

| 기호 | 의미 |
|---|---|
| $Utility_{original}$ | 원본 모델의 성능 |
| $Utility_{compressed}$ | 압축 또는 경량화 모델의 성능 |
| $\Delta Utility$ | 경량화 후 성능 변화 |

### 보안적 의미

$\Delta Utility$가 작더라도 보안 조건에서 $ASR$이 증가하거나 탐지율이 낮아질 수 있다. 따라서 경량화 모델 평가는 정상 작업 utility와 security utility를 분리해야 한다.

---

### 3.4 보안-효율 Trade-off

보안성까지 포함하면 효율적 딥러닝 평가는 다음과 같이 확장할 수 있다.

$$
SecurityEfficiency = \alpha CleanAcc + \beta RobustAcc - \gamma ASR - \lambda Cost
$$

| 기호 | 의미 |
|---|---|
| $SecurityEfficiency$ | 보안성과 효율성을 함께 고려한 평가 점수 |
| $CleanAcc$ | 정상 입력 정확도 |
| $RobustAcc$ | 공격 또는 교란 조건 정확도 |
| $ASR$ | 공격 성공률 |
| $Cost$ | latency, memory, energy, retraining cost, audit cost의 종합 비용 |
| $\alpha,\beta,\gamma,\lambda$ | 평가 목적에 따른 가중치 |

### 보안적 의미

효율화는 방어 비용을 줄일 수 있지만, 방어 성능을 희생할 수도 있다. W02에서는 모델 경량화를 독립 목표로 보지 않고, poisoning/backdoor 방어의 운영 가능성과 보안 성능을 함께 보는 다중지표 평가로 연결한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| 모델 압축 | pruning, quantization, low-rank factorization 등으로 모델 크기와 연산량을 줄인다. |
| 지식 증류 | 큰 teacher model의 출력을 작은 student model에 전달해 성능 손실을 줄인다. |
| 효율적 아키텍처 | MobileNet, EfficientNet 계열처럼 연산 효율을 고려한 구조를 설계한다. |
| 학습 효율화 | mixed precision, distributed training, early stopping, efficient optimizer로 학습 비용을 줄인다. |
| 추론 최적화 | batching, caching, operator fusion, hardware acceleration으로 latency를 줄인다. |
| 배포 제약 | edge, mobile, embedded, cloud 환경마다 메모리·전력·지연시간 요구가 다르다. |
| 평가 문제 | 모델 효율성은 단일 지표가 아니라 quality-footprint trade-off로 평가해야 한다. |

---

## 5. 보안 이슈 관점 분석

이 논문은 직접적인 poisoning 공격 문헌은 아니지만, W02의 방어·탐지·재학습이 실제 배포 가능한지 평가하는 기준을 제공한다.

| 보안 항목 | 효율적 딥러닝 관점 해석 |
|---|---|
| 데이터 오염 탐지 | 오염 탐지기는 대규모 데이터에서 반복 실행 가능해야 하므로 latency와 compute cost가 중요하다. |
| 백도어 탐지 | trigger scanning이나 activation analysis는 비용이 높을 수 있어 경량화 전략이 필요하다. |
| Robust Training | adversarial/robust training은 비용이 크므로 효율적 학습 방법과 결합이 필요하다. |
| 모델 압축 | pruning·quantization이 backdoor 잔존 여부와 robust accuracy에 영향을 줄 수 있다. |
| Edge Deployment | 경량 모델은 edge 배포에 유리하지만, 보안 모니터링과 감사 로그가 제한될 수 있다. |
| 재학습 비용 | poisoning 발견 후 재학습이나 fine-tuning 비용을 평가해야 한다. |

---

## 6. 위협모형

### 6.1 보호 대상

| 보호 대상 | 설명 |
|---|---|
| 압축 전 모델 | 원본 모델의 성능, 파라미터, 내부 표현 |
| 압축 후 모델 | pruning, quantization, distillation 적용 후 모델 |
| 보안 탐지기 | poisoning detector, backdoor scanner, anomaly detector |
| 배포 환경 | edge device, mobile device, cloud inference server |
| 평가 로그 | latency, memory, energy, accuracy, ASR, retraining cost 기록 |

### 6.2 공격자 능력

| 공격자 유형 | 가능 행위 |
|---|---|
| Poisoning attacker | 학습 데이터 일부를 오염시켜 압축 후에도 잔존하는 취약성을 만든다. |
| Backdoor attacker | 압축 또는 pruning 후에도 살아남는 trigger 반응을 유도한다. |
| Resource-exhaustion attacker | 고비용 방어를 유도해 보안 검증이나 탐지를 비활성화시킨다. |
| Deployment attacker | edge 환경의 제한된 로그·연산 자원을 악용한다. |
| Supply-chain attacker | 압축 모델, quantized checkpoint, distillation dataset을 조작한다. |

### 6.3 공격 경로

```text
원본 모델 학습
→ 압축/경량화 적용
→ clean accuracy만 확인하고 배포
→ backdoor/poisoning 조건 또는 edge 제약에서 보안 평가 누락
→ ASR 증가, 탐지 지연, 로그 부족, 재학습 비용 증가 발생
```

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W02/P02에서의 활용 |
|---|---|---|
| Clean Accuracy | 정상 조건 성능 | 원본/압축 모델 기본 비교 |
| Robust Accuracy | 교란 또는 공격 조건 성능 | 경량화 후 강건성 확인 |
| ASR | backdoor 또는 poisoning 공격 성공률 | 압축 후 공격 잔존 여부 평가 |
| Model Size | 모델 저장 크기 | 배포 가능성 평가 |
| Parameter Count | 파라미터 수 | 압축 효과 확인 |
| FLOPs | 추론 연산량 | 계산 비용 평가 |
| Latency | 평균 또는 p95 추론 지연시간 | 실시간 보안 적용 가능성 평가 |
| Memory | 추론·학습 메모리 사용량 | edge 배포 가능성 평가 |
| Energy | 전력 또는 에너지 비용 | 모바일/IoT 환경 평가 |
| Retraining Cost | 방어 적용 후 재학습 비용 | poisoning 대응 운영성 평가 |
| Audit Cost | 보안 검증에 필요한 시간·자원 | MLOps 감사 프레임 연결 |

---

## 8. 재현성 점검

이 논문은 survey 논문이므로 특정 단일 실험을 재현하기보다는, 효율성 평가 지표를 W02 poisoning/backdoor 실험에 붙이는 방식으로 재현하는 것이 적절하다.

| 항목 | 점검 |
|---|---|
| 데이터셋 | MNIST, CIFAR-10, UCI digits, synthetic classification 등 공개 데이터셋 사용 가능 |
| 모델 | 원본 baseline과 압축/경량화 모델을 함께 관리 |
| 압축 설정 | pruning ratio, quantization bit-width, distillation temperature 등 기록 필요 |
| 효율 지표 | size, parameter count, FLOPs, latency, memory 기록 필요 |
| 보안 지표 | clean accuracy, robust accuracy, ASR, detection rate 함께 기록 필요 |
| 환경 | CPU/GPU, batch size, runtime setting, library version 기록 필요 |
| 결과 파일 | metric CSV/JSON, latency log, model size log 저장 필요 |
| 재현 가능성 판단 | 소규모 모델 경량화 실험은 가능. 대규모 모델·하드웨어 최적화 재현은 환경 의존성이 큼 |

### W02 실습 연결

W02에서는 다음 최소 실험으로 P02의 평가 관점을 연결할 수 있다.

1. clean baseline 모델을 학습한다.
2. poisoned 또는 backdoor 조건 모델을 학습한다.
3. 모델 크기, 추론 시간, clean accuracy, ASR을 함께 기록한다.
4. 간단한 pruning 또는 quantization을 적용한 경우 동일 지표를 재측정한다.
5. “성능이 유지되더라도 ASR이 증가하는지”를 별도 표로 확인한다.
6. 실험 결과를 accuracy-only가 아닌 multi-metric table로 저장한다.

---

## 9. 논문의 고유 기여

1. Efficient deep learning을 모델 구조, 학습, 추론, 시스템, 하드웨어까지 포함하는 다층 문제로 정리했다.
2. 모델 효율성을 accuracy가 아니라 latency, size, memory, energy 등 footprint metric과 함께 평가해야 함을 강조했다.
3. pruning, quantization, distillation, efficient architecture 등 대표 기법의 장단점을 통합적으로 비교할 수 있는 틀을 제공한다.
4. W02에서는 poisoning/backdoor 방어가 실제 배포 가능한지 판단하는 운영 비용 평가 기준으로 활용된다.
5. 기말논문에서 accuracy, ASR, latency, model size, audit cost를 함께 보고하는 다중지표 평가표의 근거가 된다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 보안 공격 직접성 부족 | 이 논문은 효율적 딥러닝 survey이므로 poisoning/backdoor 보안 실험은 직접 다루지 않는다. | P03–P05의 poisoning/backdoor 문헌과 결합한다. |
| 보안 지표 부족 | 효율성 지표는 풍부하지만 ASR, stealthiness, detection rate는 별도 설계가 필요하다. | 보안-효율 multi-metric table을 작성한다. |
| 압축 후 보안성 미확정 | 압축이 항상 보안성을 높이거나 낮춘다고 단정할 수 없다. | 원본/압축 모델의 clean accuracy와 ASR을 함께 비교한다. |
| 하드웨어 의존성 | latency, energy, memory는 환경에 따라 크게 달라진다. | 실험 환경과 batch size를 명시한다. |
| LLM/RAG 확장 필요 | 효율적 LLM, quantized LLM, RAG serving 비용은 별도 최신 문헌이 필요하다. | W07, W08, W14와 연결한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 방어는 정확도뿐 아니라 비용·속도·배포 가능성까지 고려해야 한다는 문제의식 제시 |
| 2장 관련연구 | Efficient DL, model compression, quality-footprint trade-off 정리 |
| 3장 위협모형 | resource constraint, edge deployment, compressed model supply-chain risk 정의 |
| 4장 연구방법 | accuracy, ASR, latency, model size, audit cost를 포함한 다중지표 평가 설계 |
| 5장 실험/분석 | 원본/경량 모델 또는 baseline/defense 모델의 성능·비용 비교표 제시 |
| 6장 보안적 함의 | 방어 성능과 운영 비용의 trade-off 해석 |
| 7장 결론 | 실사용 가능한 AI 보안은 보안성과 효율성을 함께 만족해야 함을 제시 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: 효율적 딥러닝은 모델 성능을 accuracy 하나로 보지 않고 latency, size, memory, energy, deployment constraint까지 포함해 평가해야 한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: quality-footprint trade-off 표, 원본/압축 모델 비교표, clean accuracy-ASR-latency-size 다중지표 평가표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG/LLM 방어에서도 문서 필터링, 검색 검증, LLM judge, human approval gate는 비용과 지연시간을 만들기 때문에 P02의 효율성 지표를 W08/W14 운영 평가로 확장한다.

---

## 13. 최종 판단

이 논문은 W02에서 공격 taxonomy 자체보다 “방어와 검증이 실제로 배포 가능한가”를 판단하는 효율성 평가 문헌으로 사용한다. 기말논문에서는 P02를 통해 poisoning/backdoor 방어 평가에 accuracy와 ASR뿐 아니라 model size, latency, retraining cost, audit cost를 포함하는 다중지표 평가체계를 구성하는 것이 적절하다.

---

## 14. 변환 호환성 메모

- GitHub Markdown, MS Word, PDF 변환 호환성을 위해 수식은 LaTeX 블록 수식으로 작성했다.
- 긴 수식은 Markdown 표 안에 넣지 않고 별도 문단으로 분리했다.
- 표에는 변수 설명과 해석만 배치했다.
- DOCX/PDF 변환 시에는 Pandoc 기준으로 다음 명령을 권장한다.

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
