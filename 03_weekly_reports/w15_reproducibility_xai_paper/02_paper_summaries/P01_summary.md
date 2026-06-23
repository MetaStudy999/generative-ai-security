# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A Survey on Evaluation of Large Language Models |
| 저자 | Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu, Linyi Yang, Kaijie Zhu, Hao Chen, Xiaoyuan Yi, Cunxiang Wang, Yidong Wang, Wei Ye, Yue Zhang, Yi Chang, Philip S. Yu, Qiang Yang, Xing Xie |
| 학술지/학회 | ACM Transactions on Intelligent Systems and Technology 15(3), Article 39 |
| 연도 | 2024 |
| DOI/URL | `https://doi.org/10.1145/3641289` |
| PDF 파일명 | `01_Chang_et_al_2024_Evaluation_of_LLMs_Survey.pdf` |
| 검증 상태 | 로컬 PDF 첫 페이지와 DOI/Crossref metadata에서 DOI, TIST 15(3), Article 39 확인. 원 프롬프트의 ACM Computing Surveys 표기와 차이 있음 |

## 2. 한 문장 요약

> 이 논문은 LLM을 무엇을 평가할지, 어디서 평가할지, 어떻게 평가할지의 세 축으로 정리하며, LLM 보안 연구에서 평가오염과 재현성 위험을 별도 평가 항목으로 다루어야 한다는 근거를 제공한다.

## 3. 연구문제

LLM의 능력과 위험을 task-level 평가만으로 판단하기 어렵기 때문에, 일반 NLP, 추론, 의료, 윤리, 교육, 과학, agent 응용 등 다양한 평가 영역을 체계화하는 것이 핵심 연구문제다. 기말논문 관점에서는 benchmark contamination, hidden test leakage, 평가 프로토콜 표기 차이가 성능 과대평가로 이어지는 지점을 확인하는 데 활용한다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| What to evaluate | 능력, 안전성, 도메인별 task 등 평가 대상 정의 | 평가 항목 설계 |
| Where to evaluate | benchmark, 데이터셋, 평가 환경 선택 | benchmark contamination 점검 |
| How to evaluate | 자동 지표, human evaluation, leaderboards, 실패 사례 분석 | 재현성 프로토콜 |
| Evaluation risk | 평가셋 노출, 벤치마크 과적합, 측정 기준 표기 차이 | 보안 위협모형 |

## 5. 방법론

대규모 문헌조사와 분류체계를 통해 LLM 평가 영역, benchmark, 평가 방법, 성공/실패 사례, 향후 과제를 정리한다. 본 보고서에서는 세부 benchmark 수치를 새로 인용하지 않고, 평가 프레임워크의 구조를 기말논문 평가축으로 전환한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Expected Calibration Error ECE |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$ECE=\sum_{m=1}^{M}\frac{\lvert B_m\rvert}{n}\lvert acc(B_m)-conf(B_m)\rvert$$ |
| 기호·입력·출력 | \(B_m\): confidence bin, \(acc(B_m)\): bin 정확도, \(conf(B_m)\): bin 평균 confidence |
| 직관적 의미 | Expected Calibration Error ECE는 Reproducibility·XAI 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Reproducibility·XAI 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | ECE, accuracy, refusal confidence, safety calibration |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

LLM 평가는 단일 accuracy나 leaderboard 순위가 아니라 평가 대상, 데이터 출처, 측정 방식, 사회적 위험을 함께 다루어야 한다. 특히 평가 데이터가 학습 또는 튜닝 과정에 노출되면 성능 수치가 실제 일반화 능력을 반영하지 못할 수 있다.

## 7. 보안 관점 분석

평가 데이터는 보안 자산이다. 공격자 또는 모델 개발자가 benchmark 정보를 사전에 알거나 반복 질의로 hidden test 특성을 추론하면 무결성 문제가 발생한다. 따라서 평가셋 출처, 중복 검사, 로그, 모델 버전, prompt/template 정보를 보존해야 한다.

## 8. 한계와 오픈문제

Survey 논문이므로 특정 보안 실험의 재현 코드를 제공하지 않는다. 최신 LLM 평가 benchmark는 빠르게 바뀌므로 최종 논문에서는 사용 시점, 모델 버전, 데이터 누수 점검 절차를 별도로 명시해야 한다.

## 9. 기말 논문에 반영할 부분

기말논문의 평가방법 장에서 clean performance, attack impact, leakage, reproducibility를 분리하고, benchmark contamination을 별도 위협으로 정의하는 근거로 활용한다.
