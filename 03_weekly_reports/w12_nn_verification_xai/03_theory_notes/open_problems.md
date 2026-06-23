# 한계와 오픈문제

## 1. 문헌 검증 한계

P01~P05는 강의계획서 지정 표기, 공식 DOI 메타데이터, 로컬 PDF 사이에 여러 표기 차이가 있다. P01은 제목과 DOI 후보는 맞지만 매체 정보가 강의 표기와 다르고, P02는 Sen/Shuai Zhou 및 로컬 Kui Ren PDF 차이가 남아 있다. P03은 공식 published title과 강의 표기 제목이 다르다. P04와 P05는 유사 DOI 후보가 있으나 지정 저자·제목·연도와 일치하지 않아 확정하지 않았다.

## 2. 방법론 한계

신경망 검증, XAI 안정성, 대적 강건성, 공정성은 단일 지표로 환원하기 어렵다. Clean accuracy가 높아도 robust accuracy가 낮을 수 있고, explanation stability가 높아도 formal safety guarantee를 의미하지 않는다.

## 3. 실험 한계

W12 실험은 synthetic binary classification 기반 toy logistic classifier를 사용한다. `certified_rate`는 선형 모델 bound proxy이며, 실제 DNN verifier, IBP, MILP, SMT, abstract interpretation 도구가 산출한 formal certificate가 아니다. `adversarial_features()`도 실제 PGD/FGSM이 아니라 선형 가중치 부호 기반 proxy다.

## 4. 재현성 한계

`seed`, `config`, `script`, `metrics_summary.csv`, `results.json`, `run_log.md`는 보존했다. 다만 `verification_cost_ms`는 실행 환경과 CPU 상태에 따라 약간 달라질 수 있으므로 기말논문에서는 절대 시간보다 평가 항목과 로그 보존 절차를 중심으로 해석한다.

## 5. 기말 논문으로 남길 질문

1. 위험기반 부분검증은 어느 수준까지 formal verification의 대안으로 허용될 수 있는가?
2. XAI 설명 안정성과 robust accuracy가 충돌할 때 어떤 기준으로 모델을 선택해야 하는가?
3. Robustness 개선이 fairness gap을 키울 경우 보고서에는 어떤 trade-off 표를 포함해야 하는가?
4. 공식 DOI와 로컬 PDF가 표기 차이가 있는 상태에서 연구윤리적으로 어떤 인용 정책을 적용해야 하는가?
