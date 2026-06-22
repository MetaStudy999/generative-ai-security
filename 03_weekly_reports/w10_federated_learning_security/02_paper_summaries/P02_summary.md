# P02 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A survey on security and privacy of federated learning |
| 저자 | Viraaji Mothukuri, Reza M. Parizi, Seyedamin Pouriyeh, Yan Huang, Ali Dehghantanha, Gautam Srivastava |
| 공식 출판 정보 | Future Generation Computer Systems, 115, pp. 619-640, 2021 |
| DOI/URL | https://doi.org/10.1016/j.future.2020.10.007 |
| PDF 파일명 | 02_Mothukuri_et_al_2021_FL_Security_Privacy_Survey.pdf |
| 검증 상태 | DOI 메타데이터 기준 제목, 저자, 학술지, volume, page 확인 |

## 2. 한 문장 요약

이 논문은 FL의 security/privacy 위험을 체계적으로 검토하며, poisoning, backdoor, communication bottleneck, inference attack을 FL 채택 전 평가해야 할 핵심 위험으로 정리한다[2].

## 3. 연구문제

FL이 raw data를 중앙 서버로 보내지 않아도 왜 보안·프라이버시 위험에서 자유롭지 않은가를 다룬다. W10에서는 security threat와 privacy threat를 분리해 threat model과 평가 지표를 설계하는 근거가 된다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Security threat | poisoning, backdoor, communication bottleneck 등 무결성과 가용성을 해치는 위험 | 보안 이슈 30% |
| Privacy threat | inference 기반 공격과 업데이트 노출 위험 | leakage proxy 설계 |
| Edge/on-device learning | 데이터가 클라이언트에 남는 FL 운영 구조 | 보호 자산 정의 |
| Mass adoption barrier | 신뢰 부족과 위험 문서화 미비 | 정책·책임성 논의 |

## 5. 방법론

이 문헌은 FL 보안·프라이버시 문헌을 survey 형식으로 묶고, 접근 방식, 구현 스타일, 위험요인을 설명한다. W10 보고서는 이를 confidentiality, integrity, privacy 항목으로 전환한다.

## 6. 보안 관점 분석

P02는 FL이 privacy-preserving 구조를 표방하더라도 local update, communication, aggregation 단계에서 공격면이 남는다는 점을 설명한다. W10 toy 실험은 그중 poisoning/backdoor 계열을 안전한 synthetic setting으로 축소해 다룬다.

## 7. 한계와 확인 필요

- 최신 FL backdoor, secure aggregation, DP, membership inference 논문은 후속 문헌으로 보완해야 한다.
- W10 실험은 P02의 위협 분류 전체를 재현하지 않고 poisoning/backdoor 평가 형식만 검증한다.

## 8. 기말 논문에 반영할 부분

P02는 FL security/privacy threat taxonomy의 기본 관련연구로 반영한다. 기말 논문에서는 raw data 비공유가 곧 완전한 privacy 보증이 아니라는 문제 제기에 사용한다.
