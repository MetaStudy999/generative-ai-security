# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights and Future Frontiers |
| 저자 | M. Arbaoui et al. |
| 학술지/학회 | ACM Computing Surveys |
| 연도 | 2024 |
| DOI/URL | 확인 필요 |
| PDF 파일명 | 01_Arbaoui_et_al_2024_FL_Aggregation_Taxonomy.pdf |
| 검증 상태 | 로컬 PDF 파일명 확인, DOI/URL과 원문 세부 내용은 최종 대조 필요 |

## 2. 한 문장 요약

> 이 논문은 Federated Learning, aggregation, personalization, robustness의 신뢰성 및 보증 문제 문제를 문헌조사와 분류체계 정리 방법으로 다루며, 원리와 보안 보증 사이의 연결을 기말 연구에 반영할 수 있게 해준다.

## 3. 연구문제

이 논문에서 기말 연구와 연결되는 질문은 연합학습(FL) 및 FL 위협/방어/정책 영역에서 어떤 개념, 공격면, 평가 기준을 우선적으로 정리해야 하는가이다. 특히 연합학습의 기본 구조, Client, server, aggregation의 역할, FedAvg의 기본 원리와 Gradient leakage, Membership inference in FL, Poisoning attack가 서로 만나는 지점을 확인하는 데 초점을 둔다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| 연합학습의 기본 구조 | 주차 AI 원리의 출발점이며 모델 또는 시스템을 이해하는 기본 단위이다. | 배경 이론 |
| Client, server, aggregation의 역할 | 성능, 일반화, 효율 또는 신뢰성을 설명하는 보조 축이다. | 분석 기준 |
| Gradient leakage | 보안 위협을 식별하기 위한 대표 공격면이다. | 위협모형 |
| Membership inference in FL | 방어와 평가 프로토콜을 설계할 때 비교해야 하는 요소이다. | 평가방법 |

## 5. 방법론

이 문헌은 문헌조사와 분류체계 정리을 통해 기존 연구를 묶어 읽을 수 있게 한다. 본 보고서에서는 논문 제목, 프롬프트의 논문 패킷 정보, 로컬 PDF 존재 여부를 기준으로 요약했으며, 세부 실험값이나 DOI는 최종 원문 대조 단계에서 확인한다.

## 6. 주요 결과

핵심 개념, 공격면, 평가 기준, 향후 연구과제를 체계화한다. 수치 결과를 새로 만들지 않기 위해 본 요약에서는 정량값을 적지 않았고, 원문에서 직접 확인되는 항목만 최종 보고서에 반영하도록 남겨 둔다.

## 7. 보안 관점 분석

이 논문은 Gradient leakage, poisoning, backdoor, privacy attack을 이해하기 위한 배경 문헌으로 활용된다. 공격자의 능력, 방어자의 관측 가능성, 평가 데이터의 한계, 재현성 조건을 함께 정리해야 실제 보안 연구로 이어질 수 있다.

## 8. 한계와 오픈문제

원문 정밀 독해 전에는 세부 실험 설정, 데이터셋, DOI, 인용 관계를 확정할 수 없다. 또한 survey 성격의 문헌은 실제 재현 실험보다는 분류체계와 연구 공백 파악에 더 적합하므로, 기말 논문에서는 별도 평가 프로토콜로 보완해야 한다.

## 9. 기말 논문에 반영할 부분

P01는 연합학습(FL) 및 FL 위협/방어/정책 연구에서 개념 정의, 위협 분류, 평가 지표 후보를 정리하는 근거로 반영한다. 특히 원리와 보안 보증 사이의 연결을 관련연구와 연구방법 장에 연결한다.
