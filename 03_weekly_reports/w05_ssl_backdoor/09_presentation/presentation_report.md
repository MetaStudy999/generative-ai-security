# W05 발표용 보고서

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W05 |
| 주제 | 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| 발표 시간 | 8-10분 |
| 권장 슬라이드 수 | 10-14장 |
| 핵심 메시지 | 표현학습 기반 모델의 보안 평가는 clean 성능과 trigger 조건의 ASR, representation shift, 재현성 근거를 분리해야 한다. |
| 발표 근거 | `06_report/final/integrated_report_final.md`, `04_experiment/outputs/run_log.md` |

## 2. 한 문장 요약

W05는 자기지도학습과 파운데이션 모델의 표현학습 원리를 정리하고, poisoning/backdoor가 표현공간을 어떻게 이동시켜 downstream 판단을 바꿀 수 있는지 synthetic toy 실험으로 분리 평가한다.

## 3. 발표 흐름

| 순서 | 슬라이드 주제 | 핵심 내용 | 시간 |
|---:|---|---|---:|
| 1 | 표지 | W05 주제와 핵심 질문 | 0:30 |
| 2 | 왜 중요한가 | foundation pretraining은 데이터와 표현공간 보안이 핵심 | 1:00 |
| 3 | AI 원리 | self-supervised learning과 representation learning | 1:20 |
| 4 | SSL 방법 | contrastive, masked, predictive learning | 1:20 |
| 5 | 보안 이슈 | poisoning, backdoor, trigger, representation shift | 1:20 |
| 6 | 논문 5편의 역할 | 원리 survey와 보안 survey 연결 | 1:00 |
| 7 | 위협모형 | pretraining data, embedding, downstream classifier | 1:00 |
| 8 | 평가 프로토콜 | clean, ASR, shift, detection, reproducibility | 1:00 |
| 9 | Toy 실험 | synthetic 2D representation clusters | 1:00 |
| 10 | 결과 | clean 1.000000, ASR 1.000000, defense 후 ASR 0.000000 | 1:00 |
| 11 | 해석과 한계 | toy 결과의 의미와 일반화 금지 | 0:50 |
| 12 | 기말 연결 | 표현학습 보안 평가 프레임워크 | 0:40 |
| 13 | 결론/Q&A | 지표 분리와 재현성 근거 | 0:20 |

## 4. 논문 5편의 발표 역할

| ID | 논문 | 발표에서 맡는 역할 | DOI/URL 상태 |
|---|---|---|---|
| P01 | A Survey on Self-supervised Learning: Algorithms, Applications, and Future Trends | SSL 알고리즘과 응용 taxonomy | arXiv DOI 확인, 출판 DOI 미확인 |
| P02 | A Comprehensive Survey on Self-Supervised Learning for Recommendation | SSL recommendation survey와 contrastive/generative/adversarial 분류 | DOI 확인 |
| P03 | Self-Supervised Learning for Videos: A Survey | video SSL과 temporal/cross-modal representation | DOI 확인, arXiv URL 확인 |
| P04 | Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems | poisoning 공격·방어 taxonomy | DOI 확인 |
| P05 | A survey of backdoor attacks and defences | DNN부터 LLM까지 backdoor 분류 | DOI 확인 |

## 5. AI 원리 설명

- 자기지도학습은 데이터 자체에서 supervision signal을 만들어 표현을 학습한다.
- Contrastive learning은 positive pair와 negative pair의 거리를 이용해 embedding space를 구성한다.
- Masked modeling은 입력 일부를 가리고 복원하며 문맥 표현을 학습한다.
- Foundation model은 대규모 pretraining 표현을 downstream task로 전이한다.

## 6. 보안 이슈 설명

| 항목 | 발표 내용 |
|---|---|
| 보호 자산 | pretraining data, augmentation pair, embedding, downstream classifier, config/log |
| 공격자 능력 | poisoned sample 삽입, trigger pattern 주입, target behavior 유도 |
| 공격 경로 | 데이터 수집, pretraining corpus, representation pipeline, downstream fine-tuning |
| 방어자 가정 | 데이터 검수, representation consistency check, seed/config/log 보존 가능 |
| 평가 지표 | clean accuracy, ASR, mean shift, detection rate, clean FPR |

## 7. 실습/실험 결과

정량값은 `04_experiment/outputs/run_log.md` 기준이다.

| 조건 | Clean Acc. | Poisoned Clean Acc. | ASR | ASR after defense | Mean Shift | Detection Rate | Clean FPR |
|---|---:|---:|---:|---:|---:|---:|---:|
| Clean representation baseline | 1.000000 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 |
| Poisoned/backdoor representation | 해당 없음 | 1.000000 | 1.000000 | 해당 없음 | 2.418677 | 해당 없음 | 해당 없음 |
| Consistency defense check | 해당 없음 | 해당 없음 | 해당 없음 | 0.000000 | 0.090597 | 1.000000 | 0.000000 |

## 8. 기말논문 연결

| 기말논문 장 | 발표에서 연결할 내용 |
|---|---|
| 서론 | foundation pretraining 보안 평가 필요성 |
| 관련연구 | SSL/foundation model survey와 poisoning/backdoor survey |
| 연구문제 | 표현공간 오염과 trigger 조건을 함께 평가하는 최소 지표 |
| 연구방법 | 위협모형, synthetic toy 평가, 재현성 체크리스트 |
| 분석/실험 | clean 성능, ASR, representation shift, defense check 분리 |
| 보안적 함의 | integrity, robustness, accountability, governance |

## 9. 결론 메시지

1. 자기지도학습의 핵심 산출물은 표현공간이며, 이 표현공간도 보안 자산이다.
2. Backdoor 평가는 clean 성능과 trigger 조건 ASR을 반드시 분리해야 한다.
3. Representation shift와 consistency check는 안전한 toy 환경에서 설명 가능한 평가축이다.
4. 수치는 실행 로그와 config, CSV/JSON 근거가 있을 때만 주장한다.

## 10. 예상 질문과 답변

| 질문 | 답변 요지 | 근거 파일 |
|---|---|---|
| 왜 실제 SSL 모델을 쓰지 않았나? | 목표는 공격 성능 경쟁이 아니라 안전한 toy 환경에서 평가 지표 구조를 검증하는 것이다. | `04_experiment/experiment_report.md` |
| ASR 1.000000은 무엇을 뜻하나? | toy source-class test embedding 전체가 trigger 후 target centroid로 분류됐다는 뜻이다. | `04_experiment/outputs/run_log.md` |
| Detection rate 1.000000은 실제 방어를 증명하나? | 아니다. synthetic paired-view 거리 threshold 조건에서 trigger shift를 모두 플래그했다는 의미다. | `04_experiment/outputs/results.json` |
| DOI는 모두 확정인가? | 확인 가능한 DOI/URL은 기록했지만 P01 출판 DOI는 미확인으로 남겼다. | `01_papers/doi_check.md` |

## 11. 발표 전 점검

| 확인 | 점검 항목 |
|---|---|
| □ | 발표 수치가 `outputs/run_log.md`와 일치한다. |
| □ | synthetic toy 결과를 실제 SSL/foundation model 성능으로 일반화하지 않는다. |
| □ | 제목 차이와 DOI 확인 수준을 구분해 말한다. |
| □ | 예상 질문 3개 이상을 준비한다. |
