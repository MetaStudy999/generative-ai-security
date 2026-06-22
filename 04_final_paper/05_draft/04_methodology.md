# 4. 연구방법

## 4.1 연구대상

LLM/RAG 기반 AI 응용과 연구용 평가 파이프라인을 중심 대상으로 한다. 단, 분석 배경은 W01-W15 final 보고서 전체로 확장해 딥러닝, 최적화, 생성모형, 강화학습, 연합학습, 프라이버시, 검증, MLOps까지의 생명주기 위협을 함께 본다.

## 4.2 위협모형

공격자는 악성 프롬프트, 오염 문서, 평가셋 누수, 민감정보 노출 유도를 통해 시스템 신뢰성을 저하시킨다.

## 4.3 분석 방법

W01-W15 final 보고서의 문헌표, 이론노트, 실험 로그, 참고문헌 검증표를 먼저 대조한다. 이후 기말 논문 주제와 직접 연결되는 W07, W08, W11, W14, W15를 핵심 축으로 삼아 위협-방어-평가 항목을 통합한다. 주차별 핵심 수식과 알고리즘은 `04_final_paper/04_methodology_experiment/formula_metric_supplement.md`의 보충표를 사용해 기호, 쉬운 의미, 보안 평가 연결을 함께 설명한다.

## 4.4 평가방법

Clean performance, attack impact, privacy leakage, utility, cost, reproducibility, human review를 공통 평가 항목으로 둔다.

수식은 실제 공격 절차를 상세화하기 위한 목적이 아니라 보고 지표의 의미를 명확히 하기 위한 목적이다. 따라서 ASR, leakage, robust accuracy, DP 정의, FedAvg, watermark fidelity 같은 지표는 synthetic 또는 문헌 기반 평가에서만 사용하며, 실행 로그가 없는 값은 정량 결과로 주장하지 않는다.
