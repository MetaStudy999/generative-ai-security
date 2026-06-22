# 한계와 오픈문제

## 1. 문헌 검증 한계

논문 제목과 로컬 PDF 파일명은 정리했지만 DOI/URL과 원문 세부 수치는 최종 대조가 필요하다. `SUBSTITUTE` PDF가 있는 문헌은 프롬프트 지정 문헌과 실제 확보 문헌의 차이를 확인해야 한다.

## 2. 방법론 한계

신경망 검증, XAI 안정성, 대적 강건성, 공정성은 단일 지표로 환원하기 어렵다. Clean accuracy가 높아도 robust accuracy가 낮을 수 있고, 설명 안정성이 높아도 검증 가능한 안전성을 의미하지는 않는다.

## 3. 실험 한계

W12 실험은 synthetic toy logistic classifier 기반이다. Clean model 기준 clean accuracy 0.818750, robust accuracy 0.543750, certified rate 0.543750을 기록했지만, certified rate는 선형 모델 bound proxy다. 대규모 DNN formal verification, 실제 saliency map 공격, 안전중요 시스템 검증으로 일반화하지 않는다.

## 4. 재현성 한계

`seed`, `config`, `script`, `CSV/JSON/run_log`는 보존했지만, 로컬 환경과 Docker 환경에서 verification cost ms는 작은 차이가 날 수 있다. 기말논문에는 절대 실행시간보다 평가 항목과 로그 보존 절차를 중심으로 반영한다.

## 5. 기말 논문으로 남길 질문

1. 위험기반 부분검증은 어느 수준까지 formal verification의 대안으로 허용될 수 있는가?
2. XAI 설명 안정성과 robust accuracy가 충돌할 때 어떤 기준으로 모델을 선택해야 하는가?
3. Robustness 개선이 fairness gap을 키울 경우 보고서에는 어떤 trade-off 표를 포함해야 하는가?
