# 강의계획서 요약

## 1. 수업 개요

AI 보안 박사과정 논문지도 세미나는 최신 AI 보안 논문을 읽고 끝내는 수업이 아니라, 주차별 분석 결과를 학위논문 또는 국내외 학술지 논문으로 발전시키는 것을 목표로 한다.

| 항목 | 요약 |
|---|---|
| 수업 성격 | SCI/SCIE 논문 기반 박사과정 논문지도형 세미나 |
| 핵심 목표 | 연구문제 정의, 위협모형 구성, 평가방법 설계, 재현성 점검, 기여점 도출 |
| 지식 구성 | AI 원리·이론 약 70%, 보안 이슈 약 30% |
| 주교재 | 매주 제공되는 SCI/SCIE 논문 5편 |
| 최종 연결 | 주차별 보고서를 기말 모의투고 논문으로 재구성 |

## 2. 수업 운영 방식

| 항목 | 기준 |
|---|---|
| 수업 형태 | 온라인 실시간 세미나 |
| 운영 시간 | 매주 토요일, 총 100분 |
| 전반 50분 | 교수 강의와 핵심 이론 정리 |
| 후반 50분 | 학생 발표, 토론, 리뷰 |
| 참여 기준 | 카메라 ON, 기본 마이크 OFF, 발표·질의 시 마이크 ON |
| 평가 성격 | 발표 기반 peer scoring 중심 |

수업은 `Research Track`과 `AI Tool Track`을 병행한다. Research Track은 논문을 연구문제, 위협모형, 평가방법, 재현성, 한계/오픈문제로 해부하고, AI Tool Track은 AI 도구 활용 과정과 검증 방식을 Worklog로 남긴다.

## 3. Research Track

- 연구문제:
- 위협모형:
- 평가방법:
- 재현성:
- 한계/오픈문제:

각 주차 보고서와 발표자료에는 위 다섯 항목이 추적 가능하게 남아야 한다. 특히 기말논문으로 연결할 수 있는 항목은 `기말논문 연결표` 또는 `04_final_paper/02_weekly_reflection/`에 반영한다.

## 4. AI Tool Track

- 사용 도구:
- 사용 목적:
- Worklog:
- 검증 방식:

AI 도구는 번역, 개념 설명, 수식 해설, 코드 점검, 문장 교정, 목차 후보 작성에 활용할 수 있다. 다만 AI가 생성한 인용, DOI, 정량 실험값, 논문 해석은 원문·실행 로그·공식 출처로 검증한 뒤에만 최종 원고에 반영한다.

## 5. 주차별 구성

| 주차 | 핵심 영역 |
|---|---|
| Week 1-3 | 딥러닝 기초, 최적화, 컴퓨터비전 |
| Week 4-6 | Transformer, 자기지도학습, 생성모형 |
| Week 7-9 | LLM, RAG, 심층강화학습 |
| Week 10-12 | 연합학습, 차등프라이버시, 신경망 검증 |
| Week 13-15 | 모델 지식재산 보호, MLOps, 연구평가·재현성·XAI |

## 6. 기말고사 보고서와의 연결

기말고사 보고서는 국내 학회지 양식 기반 AI 보안 모의투고 논문이다. 주차별 보고서를 단순 취합하지 않고, 하나의 작은 연구문제, 관련연구 비교, 위협모형, 연구방법, 분석 또는 모의실험, 보안적 함의로 재구성한다.

| 항목 | 기준 |
|---|---|
| 원고 형식 | 선택한 국내 학회지 HWP 또는 DOCX 양식 |
| 분량 | A4 기준 6쪽 이상 12쪽 이하, 단 선택 학회지 기준 우선 |
| 참고문헌 | 국내 논문 3편 이상, 해외 논문 5편 이상 |
| 주차별 보고서 반영 | 최소 2개 이상 |
| 필수 부속 | PDF 변환본, 학회지 양식 출처표, AI 활용 고지서, 참고문헌 검증표, 주차별 보고서 반영표 |
| 연구윤리 | 허위 인용, 존재하지 않는 DOI, 실행하지 않은 실험 결과, AI 활용 은폐 금지 |

## 7. 수식·알고리즘 설명 반영 기준

수식은 모든 논문에 기계적으로 넣지 않는다. 다만 논문의 핵심 기여, 공격/방어 원리, 평가 지표, 프라이버시 보장, 최적화 절차를 이해하는 데 필요하면 반드시 설명한다.

| 분야 | 우선 설명할 수식·알고리즘 예시 |
|---|---|
| 딥러닝·최적화 | 손실함수, gradient descent, regularization, 일반화 지표 |
| 데이터 오염·백도어 | poisoning objective, attack success rate, clean accuracy, stealth 지표 |
| 컴퓨터비전·대적공격 | FGSM/PGD, perturbation norm, robust accuracy |
| Transformer·LLM·RAG | attention, retrieval score, ranking/generation pipeline, 평가오염 지표 |
| 생성모형 | GAN min-max objective, diffusion forward/reverse process, score matching |
| 심층강화학습 | MDP, Bellman equation, Q-learning, policy gradient, reward manipulation |
| 연합학습 | FedAvg, robust aggregation, client update, communication/privacy cost |
| 차등프라이버시·멤버십 추론 | epsilon-delta DP, privacy budget, DP-SGD clipping/noise, attack advantage |
| 신경망 검증·XAI | verification property, Lipschitz bound, saliency/attribution 안정성 |
| 모델 IP·MLOps | watermark detectability, false positive rate, drift metric, audit evidence |

수식을 반영할 때는 원문 수식 또는 검증 가능한 표준 수식만 사용하고, 기호 정의, 직관적 의미, 보안 관점 해석, 평가 지표와의 연결, 한계와 가정을 함께 적는다. 원문 확인이 부족하면 `확인 필요`로 표시하고 임의로 수식을 만들지 않는다.

수식 작성 도구는 `math_formula_toolchain.md`를 따른다. 기본 작성은 Markdown + LaTeX math, HTML 렌더링은 KaTeX/MathJax, 문서 변환은 Pandoc, 최종 PDF 품질 관리는 LaTeX/TeX Live, 수식 검산은 필요 시 `sympy`를 사용한다.
