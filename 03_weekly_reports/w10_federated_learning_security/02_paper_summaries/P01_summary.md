# P01 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights, and Future Frontiers |
| 저자 | Meriem Arbaoui, Mohamed-el-Amine Brahmia, Abdellatif Rahmoun, Mourad Zghal |
| 공식 출판 정보 | ACM Transactions on Intelligent Systems and Technology, 15(6), pp. 1-69, 2024 |
| DOI/URL | https://doi.org/10.1145/3678182 |
| PDF 파일명 | 01_Arbaoui_et_al_2024_FL_Aggregation_Taxonomy.pdf |
| 검증 상태 | DOI 메타데이터와 로컬 AAM PDF에서 TIST 확인. 강의계획서/프롬프트의 ACM Computing Surveys 표기와 차이 있음 |

## 2. 한 문장 요약

이 논문은 연합학습 aggregation, personalization, optimization, robustness를 다층 분류체계와 실험적 통찰로 정리하며, FL 보안 평가에서 어떤 집계 축을 비교해야 하는지 보여준다[1].

## 3. 연구문제

FL aggregation을 어떤 수준에서 분류하고, heterogeneity, communication cost, privacy, robustness를 하나의 평가표로 어떻게 묶을 것인가를 다룬다. W10에서는 FedAvg와 coordinate median 비교 축, non-IID 조건, aggregation rule 기록 항목을 설계하는 근거로 사용한다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| FL aggregation | 여러 클라이언트의 로컬 업데이트를 글로벌 모델로 결합하는 단계 | FedAvg/coordinate median 비교 |
| Personalization | 클라이언트별 데이터 분포 차이를 반영하는 FL 설계 | non-IID 한계 설명 |
| Heterogeneity | 클라이언트 데이터, 계산자원, 네트워크 조건의 차이 | 재현성·운영 비용 기준 |
| Robust aggregation | 악성 또는 이상 update의 영향을 줄이는 집계 방식 | integrity 방어 조건 |

## 5. 방법론

이 문헌은 bibliometric analysis와 systematic review 성격의 문헌조사를 결합해 aggregation 전략을 architecture, synchronization, federation motivation, robustness 관점에서 분류한다. W10 보고서에서는 세부 원문 수치보다 aggregation taxonomy와 평가 축 설계 근거로 사용한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | FedAvg Aggregation |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$w_{t+1}=\sum_{k=1}^{K}\frac{n_k}{n}w_{t+1}^{(k)}$$ |
| 기호·입력·출력 | \(w_{t+1}^{(k)}\): client k의 local model, \(n_k\): client 데이터 수, \(n\): 전체 데이터 수 |
| 직관적 의미 | FedAvg Aggregation는 Federated Learning 보안 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Federated Learning 보안 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | global accuracy, client drift, poisoning ASR, aggregation robustness |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 보안 관점 분석

P01은 직접적인 공격 논문이라기보다 FL 원리와 aggregation taxonomy 문헌이다. Secure aggregation은 서버가 개별 update를 보지 못하게 하여 confidentiality를 강화하는 반면, robust aggregation은 악성 또는 이상 update의 영향을 줄여 integrity를 강화한다. W10 toy 실험은 후자인 robust aggregation의 간단한 예시로 coordinate median을 사용한다.

## 7. 한계와 확인 필요

- 수업자료/프롬프트의 `ACM Computing Surveys` 표기와 DOI 메타데이터의 `ACM Transactions on Intelligent Systems and Technology` 표기가 다르다.
- DOI 등록 메타데이터에서 별도 Article 번호는 확인되지 않았다.
- 최종 참고문헌은 공식 DOI 메타데이터 기준 TIST 표기를 우선 사용한다.

## 8. 기말 논문에 반영할 부분

P01은 기말 논문의 FL 원리 배경과 aggregation taxonomy 근거로 반영한다. 특히 robust aggregation을 단순 방어기법이 아니라 FL 설계축 중 하나로 해석하는 근거가 된다.
