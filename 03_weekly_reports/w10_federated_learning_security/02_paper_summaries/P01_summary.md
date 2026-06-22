# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights, and Future Frontiers |
| 저자 | M. Arbaoui et al. |
| 학술지/학회 | ACM Transactions on Intelligent Systems and Technology, 로컬 PDF 기준 |
| 연도 | 2024 |
| DOI/URL | 10.1145/3678182 |
| PDF 파일명 | 01_Arbaoui_et_al_2024_FL_Aggregation_Taxonomy.pdf |
| 검증 상태 | 로컬 PDF 첫 페이지에서 제목과 DOI 확인, 프롬프트의 학술지명은 최종 대조 필요 |

## 2. 한 문장 요약

> 이 논문은 연합학습 aggregation, personalization, optimization, robustness를 다층 분류체계와 실험적 통찰로 정리하며, FL 보안 평가에서 어떤 집계 축을 비교해야 하는지 보여준다.

## 3. 연구문제

이 논문에서 기말 연구와 연결되는 질문은 FL aggregation을 어떤 수준에서 분류하고, heterogeneity, communication cost, privacy, robustness를 하나의 평가표로 어떻게 묶을 것인가이다. 특히 FedAvg 계열 집계와 personalized FL, robust aggregation을 비교하는 기준을 제공한다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| FL aggregation | 여러 클라이언트의 로컬 업데이트를 글로벌 모델로 결합하는 단계 | 실험 조건의 FedAvg/median 비교 |
| Personalization | 클라이언트별 데이터 분포 차이를 반영하는 FL 설계 | Non-IID 한계 설명 |
| Heterogeneity | 클라이언트 데이터, 계산자원, 네트워크 조건의 차이 | 재현성·운영 비용 기준 |
| Robust aggregation | 이상 업데이트의 영향을 줄이기 위한 집계 방식 | 방어 실험 조건 |

## 5. 방법론

이 문헌은 bibliometric analysis와 systematic scrutinizing을 결합한 survey로, aggregation 전략을 architecture, synchronization, federation motivation, robustness 관점에서 분류한다. 본 보고서에서는 세부 수치 대신 W10 toy 실험의 집계 조건 설계 근거로 사용한다.

## 6. 주요 결과

FL aggregation은 단순 평균이 아니라 데이터 이질성, 효율성, 보안성, personalization 요구에 따라 달라진다. 따라서 W10 실험은 FedAvg 기준과 coordinate median 방어 조건을 분리해 기록한다.

## 7. 보안 관점 분석

이 논문은 Gradient leakage, poisoning, backdoor, privacy attack을 이해하기 위한 배경 문헌으로 활용된다. 공격자의 능력, 방어자의 관측 가능성, 평가 데이터의 한계, 재현성 조건을 함께 정리해야 실제 보안 연구로 이어질 수 있다.

## 8. 한계와 오픈문제

원문 정밀 독해 전에는 세부 실험 설정, 데이터셋, DOI, 인용 관계를 확정할 수 없다. 또한 survey 성격의 문헌은 실제 재현 실험보다는 분류체계와 연구 공백 파악에 더 적합하므로, 기말 논문에서는 별도 평가 프로토콜로 보완해야 한다.

## 9. 기말 논문에 반영할 부분

P01는 기말 논문의 FL 원리 배경과 aggregation taxonomy 근거로 반영한다. 특히 robust aggregation을 단순 방어기법이 아니라 FL 설계축 중 하나로 해석하는 근거가 된다.
