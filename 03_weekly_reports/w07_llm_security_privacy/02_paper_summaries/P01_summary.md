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

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Benchmark Contamination Rate |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$ContamRate=\frac{N_{overlap}}{N_{benchmark}}$$ |
| 기호·입력·출력 | \(N_{overlap}\): 학습/평가 중복 의심 항목 수, \(N_{benchmark}\): benchmark 항목 수 |
| 직관적 의미 | Benchmark Contamination Rate는 LLM 보안·프라이버시 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | LLM 보안·프라이버시 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | benchmark coverage, contamination rate, utility, ASR |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 기말 논문 활용

LLM/RAG 보안 평가 프레임워크에서 “평가축을 먼저 정의한 뒤 지표를 기록한다”는 기본 논리의 근거로 활용한다.
