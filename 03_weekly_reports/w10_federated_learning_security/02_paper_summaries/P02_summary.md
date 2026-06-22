# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A survey on security and privacy of federated learning |
| 저자 | Viraaji Mothukuri et al. |
| 학술지/학회 | Future Generation Computer Systems |
| 연도 | 2021 |
| DOI/URL | 10.1016/j.future.2020.10.007 |
| PDF 파일명 | 02_Mothukuri_et_al_2021_FL_Security_Privacy_Survey.pdf |
| 검증 상태 | 로컬 PDF 첫 페이지에서 제목, 학술지, DOI 확인 |

## 2. 한 문장 요약

> 이 논문은 FL의 security/privacy 위험을 체계적으로 검토하며, poisoning·backdoor·communication bottleneck·inference attack을 FL 채택 전 평가해야 할 핵심 위험으로 정리한다.

## 3. 연구문제

이 논문에서 기말 연구와 연결되는 질문은 FL이 raw data를 중앙 서버로 보내지 않아도 왜 보안·프라이버시 위험에서 자유롭지 않은가이다. 특히 security threat와 privacy threat를 분리해 threat model과 평가 지표를 설계하는 근거가 된다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Security threat | poisoning, backdoor, communication bottleneck 등 무결성과 가용성을 해치는 위험 | 보안 이슈 30% |
| Privacy threat | inference 기반 공격과 업데이트 노출 위험 | leakage proxy 설계 |
| Edge/on-device learning | 데이터가 클라이언트에 남는 FL 운영 구조 | 보호 자산 정의 |
| Mass adoption barrier | 신뢰 부족과 위험 문서화 미비 | 정책·책임성 논의 |

## 5. 방법론

이 문헌은 FL 보안·프라이버시 문헌을 survey 형식으로 묶고, 접근 방식, 구현 스타일, 위험요인을 설명한다. 본 보고서는 이를 W10 위협모형의 confidentiality, integrity, privacy 항목으로 전환한다.

## 6. 주요 결과

로컬 PDF 초록 기준, 보안 위협으로 communication bottleneck, poisoning, backdoor가 두드러지고 privacy 위협으로 inference-based attack이 중요하다고 정리한다. W10 실험은 이 중 poisoning/backdoor 계열을 toy 조건으로만 축소해 다룬다.

## 7. 보안 관점 분석

이 논문은 Gradient leakage, poisoning, backdoor, privacy attack을 이해하기 위한 배경 문헌으로 활용된다. 공격자의 능력, 방어자의 관측 가능성, 평가 데이터의 한계, 재현성 조건을 함께 정리해야 실제 보안 연구로 이어질 수 있다.

## 8. 한계와 오픈문제

원문 정밀 독해 전에는 세부 실험 설정, 데이터셋, DOI, 인용 관계를 확정할 수 없다. 또한 survey 성격의 문헌은 실제 재현 실험보다는 분류체계와 연구 공백 파악에 더 적합하므로, 기말 논문에서는 별도 평가 프로토콜로 보완해야 한다.

## 9. 기말 논문에 반영할 부분

P02는 FL security/privacy threat taxonomy의 기본 관련연구로 반영한다. 기말 논문에서는 raw data 비공유가 곧 완전한 privacy 보증이 아니라는 문제 제기에 사용한다.
