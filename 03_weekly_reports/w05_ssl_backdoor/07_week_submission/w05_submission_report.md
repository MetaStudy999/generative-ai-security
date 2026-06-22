# W05 제출용 보고서

## 표지

| 항목 | 내용 |
|---|---|
| 주차 | W05 |
| 보고서 제목 | 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| 과목 범위 | AI 보안 |
| 작성일 | 2026-06-22 |
| 문서 상태 | 제출용 통합본 |
| 관련 산출물 위치 | `03_weekly_reports/w05_ssl_backdoor/` |

## 초록

본 보고서는 자기지도학습과 파운데이션 모델의 표현학습 원리를 정리하고, pretraining 데이터 오염과 backdoor trigger가 표현공간과 downstream 판단에 미치는 위험을 분석한다. AI 원리 측면에서는 self-supervised learning, contrastive learning, masked modeling, representation learning, transfer learning을 다룬다. 보안 측면에서는 poisoning, backdoor, trigger injection, representation shift, 데이터 거버넌스를 위협모형과 평가 지표로 연결한다. synthetic 2D representation toy 실험을 실행해 clean accuracy, poisoned clean accuracy, attack success rate, representation shift, consistency defense 지표를 분리 기록했다. 결론적으로 W05는 기말논문의 “표현학습 기반 AI 시스템의 poisoning/backdoor 평가 프레임워크”로 발전 가능하다.

**키워드:** self-supervised learning, representation learning, foundation model, poisoning, backdoor, trigger, reproducibility

## 1. AI 원리 70%

자기지도학습은 사람이 붙인 라벨 없이 데이터 자체에서 supervision signal을 구성해 표현을 학습한다. Contrastive learning은 positive pair를 가깝게, negative pair를 멀게 배치해 표현공간의 구조를 만든다. Masked modeling은 입력 일부를 가리고 복원하도록 학습해 문맥 표현을 얻는다. 이러한 pretraining 표현은 downstream task로 전이되며, foundation model에서는 대규모 사전학습과 transfer learning의 기반이 된다.

W05에서 중요한 점은 표현공간 자체가 보안 자산이라는 것이다. 모델이 어떤 표현을 학습했는지, trigger나 poisoned sample이 표현을 어느 방향으로 이동시키는지, downstream classifier가 그 이동을 어떻게 해석하는지가 보안 평가의 핵심이 된다.

## 2. 보안 이슈 30%

Poisoning은 학습 데이터나 pretraining corpus에 악의적 샘플을 섞어 모델의 표현 또는 판단 경계를 왜곡하는 공격이다. Backdoor는 일반 입력에서는 정상 동작을 유지하면서 특정 trigger가 포함된 입력에서 공격자가 원하는 target behavior를 유도한다. 자기지도학습 환경에서는 라벨이 명시되지 않아도 augmentation pair, contrastive objective, masked token 복원, 데이터 수집 파이프라인이 공격면이 될 수 있다.

| 관점 | 관련 위협 | W05 평가 연결 |
|---|---|---|
| Integrity | poisoned pretraining data | poisoned clean accuracy와 ASR 분리 |
| Robustness | trigger-induced representation shift | mean representation shift |
| Safety | hidden target behavior | ASR after defense |
| Accountability | 데이터/seed/config 누락 | `outputs/` 로그 보존 |
| Governance | 출처 불명 corpus | DOI/URL 및 PDF 검증표 |

## 3. 문헌 요약

| ID | 문헌 | DOI/URL 상태 | 활용 |
|---|---|---|---|
| P01 | A Survey on Self-supervised Learning: Algorithms, Applications, and Future Trends | arXiv DOI `10.48550/arXiv.2301.05712` | SSL 알고리즘과 응용 taxonomy |
| P02 | A Comprehensive Survey on Self-Supervised Learning for Recommendation | DOI `10.1145/3746280` | 추천 시스템 SSL survey, contrastive/generative/adversarial SSL 분류 |
| P03 | Self-Supervised Learning for Videos: A Survey | DOI `10.1145/3577925`, arXiv URL 확인 | video SSL과 temporal/cross-modal representation |
| P04 | Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems | DOI `10.1145/3538707` | poisoning 공격·방어 taxonomy |
| P05 | A survey of backdoor attacks and defences: From deep neural networks to large language models | DOI `10.1016/j.jnlest.2025.100326` | DNN부터 LLM까지 backdoor 공격·방어 분류 |

## 4. Research Track

| 항목 | 내용 |
|---|---|
| 연구문제 | 자기지도/파운데이션 모델의 표현공간에서 poisoning과 backdoor를 평가하려면 어떤 최소 지표가 필요한가 |
| 대상 시스템 | SSL pretraining 표현, downstream classifier, foundation model 데이터 파이프라인 |
| 위협 | poisoned pretraining sample, trigger injection, representation shift, target misclassification |
| 평가 지표 | clean accuracy, poisoned clean accuracy, ASR, ASR after defense, mean shift, detection rate, clean FPR |
| 재현성 | seed 42, config, script, CSV/JSON/run log 보존 |
| 제외 범위 | 실제 서비스 공격, 실제 개인정보, 악용 가능한 backdoor 제작 절차 |

## 5. 실습/실험 결과

실습 코드는 `04_experiment/src/run_experiment.py`에 작성했다. 실행 명령은 `python3 src/run_experiment.py --config configs/config.yaml`이며, 결과는 `04_experiment/outputs/`에 저장했다.

| 조건 | Clean Acc. | Poisoned Clean Acc. | ASR | ASR after defense | Mean Shift | Detection Rate | Clean FPR | 해석 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Clean representation baseline | 1.000000 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 | clean synthetic embedding 분류 기준 |
| Poisoned/backdoor representation | 해당 없음 | 1.000000 | 1.000000 | 해당 없음 | 2.418677 | 해당 없음 | 해당 없음 | trigger가 source embedding을 target centroid 쪽으로 이동 |
| Consistency defense check | 해당 없음 | 해당 없음 | 해당 없음 | 0.000000 | 0.090597 | 1.000000 | 0.000000 | paired-view 거리 기준으로 trigger shift를 플래그 |

이 결과는 synthetic toy 실험의 평가 형식 검증용 수치다. 실제 SSL 모델, foundation model, 상용 시스템의 보안 성능으로 일반화하지 않는다.

## 6. 발표자료 위치

| 파일 | 용도 |
|---|---|
| `09_presentation/presentation_report.md` | 발표용 보고서 |
| `09_presentation/presentation_slides.md` | 슬라이드 원본 |
| `09_presentation/presentation_slides.html` | 브라우저 발표용 슬라이드 |
| `09_presentation/speaker_notes.md` | 발표자 대본 |
| `09_presentation/qna.md` | 예상 질문과 답변 |
| `09_presentation/one_page_handout.md` | 1페이지 배포자료 |

## 7. 기말논문 연결

추천 주제는 “표현학습 기반 AI 시스템의 poisoning/backdoor 평가 프레임워크”이다. 기여 후보는 SSL/foundation pretraining 위협모형, representation shift 기반 toy 평가표, clean performance와 ASR의 분리 기록, seed/config/output 기반 재현성 체크리스트다.

## 8. AI 활용 고지

Codex를 사용해 문헌 요약 구조화, DOI/URL 검증 보조, synthetic 실험 코드 작성과 실행, 제출용 보고서 및 발표자료 작성을 수행했다. 정량값은 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 사용했다. 상세 기록은 `05_ai_worklog/`에 있다.

## 9. 제출 전 점검표

| 점검 항목 | 상태 |
|---|---|
| 논문 요약 5편 | 완료 |
| 논문 비교표 | 완료 |
| AI 원리/보안 이슈 | 완료 |
| Research Track | 완료 |
| 실험 코드 | 완료 |
| 실험 결과 | 완료 |
| DOI/URL 검증표 | 부분 완료 |
| AI 활용 고지 | 완료 |
| 발표자료 | 완료 |
