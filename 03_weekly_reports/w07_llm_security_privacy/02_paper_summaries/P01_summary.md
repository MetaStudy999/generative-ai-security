# 논문 요약: P01

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문명 | A Survey on Evaluation of Large Language Models |
| 저자 | Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu, Linyi Yang, Kaijie Zhu, Hao Chen, Xiaoyuan Yi, Cunxiang Wang, Yidong Wang, Wei Ye, Yue Zhang, Yi Chang, Philip S. Yu, Qiang Yang, Xing Xie |
| 출판정보 | ACM Transactions on Intelligent Systems and Technology, 15(3), Article 39, pp. 1-45, 2024 |
| DOI/URL | `https://doi.org/10.1145/3641289` |
| 검증 상태 | DOI, 권호, Article 번호, 쪽수 확인. 강의계획서의 ACM Computing Surveys 표기는 실제 출판지와 다름 |

## 2. 한 문장 요약

LLM 평가는 task score만이 아니라 task coverage, benchmark 구성, human evaluation, contamination risk, social risk를 함께 다루는 평가 discipline으로 이해해야 한다[1].

## 3. 연구문제

이 논문은 LLM을 무엇으로 평가할 것인가, 어디에서 평가할 것인가, 어떤 방식으로 평가할 것인가를 체계적으로 분류한다. W07에서는 이 관점을 LLM/RAG 보안 평가의 기본 축으로 사용한다.

## 4. 핵심 개념

- Evaluation task: 일반 NLP, reasoning, code, medical, ethics, education, agent task 등.
- Benchmark discipline: benchmark coverage, hidden test leakage, data contamination, prompt sensitivity.
- Evaluation method: automatic metric, human evaluation, model-as-judge, risk-oriented evaluation.

## 5. 보안 관점 분석

P01은 직접적인 공격 논문은 아니지만, 보안 평가의 기준선을 제공한다. benchmark contamination, evaluation leakage, capability-risk mismatch가 발생하면 모델의 실제 안전성 판단이 왜곡될 수 있다. 따라서 W07 실험은 utility와 answer rate만 보지 않고 ASR, privacy leakage, refusal quality, over-refusal, code vulnerability rate를 함께 기록한다.

## 6. 기말 논문 활용

LLM/RAG 보안 평가 프레임워크에서 “평가축을 먼저 정의한 뒤 지표를 기록한다”는 기본 논리의 근거로 활용한다.
