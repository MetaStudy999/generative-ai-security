# P04 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Membership Inference Attacks on Machine Learning: A Survey |
| 저자 | Hongsheng Hu, Zoran Salcic, Lichao Sun, Gillian Dobbie, Philip S. Yu, Xuyun Zhang |
| 학술지/학회 | ACM Computing Surveys 54(11s), pp. 1-37; print 2022-01-31, online 2022-09-09 |
| 연도 | 2022 |
| DOI/URL | DOI `10.1145/3523273`; arXiv `2103.07853` |
| PDF 파일명 | `04_Hu_et_al_2022_Membership_Inference_Attacks_Survey.pdf` |
| 검증 상태 | Crossref/ACM 등록 DOI 확인. 로컬 PDF는 arXiv/ACM preprint 판 |

## 2. 한 문장 요약

> 이 논문은 membership inference attack의 목표, 접근 지식, 대상 모델, 방어전략을 체계화하고 MI를 confidentiality/privacy violation 관점에서 설명한다.

## 3. 연구문제

공격자가 모델 출력, confidence, loss, gradient, 보조 데이터 등을 이용할 때 특정 레코드가 학습에 포함되었는지 얼마나 추론할 수 있는가를 묻는다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Membership inference | 특정 sample이 학습 데이터였는지 추론하는 privacy attack | W11 보안 핵심 |
| Black-box access | 모델 출력이나 confidence만 관찰하는 조건 | 안전한 toy 평가 |
| Overfitting gap | train/test confidence 차이가 leakage proxy가 될 수 있음 | 실험 지표 |
| Defense taxonomy | regularization, output restriction, DP 등 방어 범주 | 보안적 함의 |

## 5. 방법론

MI 공격과 방어를 모델 유형, 공격자 지식, 관측 정보, 방어 전략에 따라 분류한다. W11에서는 공격 절차를 악용 가능하게 재현하지 않고, synthetic confidence score 기반 위험 지표로만 축약한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Membership Inference Advantage |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$Adv_{MI}=TPR-FPR$$ |
| 기호·입력·출력 | TPR: member를 member로 맞힌 비율, FPR: non-member를 member로 잘못 판정한 비율 |
| 직관적 의미 | Membership Inference Advantage는 Differential Privacy·Membership Inference 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Differential Privacy·Membership Inference 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | attack accuracy, advantage, leakage score, utility |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

MI 위험은 모델의 과적합, confidence 노출, 데이터 분포, 공격자 보조 지식에 영향을 받는다. 따라서 accuracy만 보고 privacy risk를 판단하면 부족하다.

## 7. 보안 관점 분석

P04는 W11 threat model의 중심 문헌이다. 보호 자산은 단순 데이터 원문이 아니라 “학습 포함 여부”라는 메타정보이며, 이는 의료·위치·민감 도메인에서 privacy breach가 될 수 있다.

## 8. 한계와 오픈문제

Survey 문헌이므로 최신 LLM/FL 특화 MI와 실제 구현별 privacy accounting은 추가 문헌이 필요하다. 본 보고서의 toy 실험은 P04의 개념을 설명하는 모의 평가일 뿐 실제 공격 성능이 아니다. PDF metadata의 placeholder DOI는 DOI로 확정하지 않고, Crossref/ACM 등록 DOI `10.1145/3523273`만 사용한다.

## 9. 기말 논문에 반영할 부분

기말 논문 위협모형에서 `보호 자산: membership information`, `공격자 관측: output confidence/loss proxy`, `지표: MI attack accuracy`를 정의하는 근거로 사용한다.
