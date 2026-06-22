# 한계와 오픈문제

## 1. 문헌 검증 한계

- P01-P05의 DOI/URL을 대조했다.
- P01은 수업자료의 `ACM Computing Surveys` 표기와 DOI 메타데이터의 `ACM Transactions on Intelligent Systems and Technology` 표기 차이를 최종 제출 전 사람이 확인해야 한다.
- P04는 DOI를 확인했지만 Article 번호는 추가 확인이 필요하다.
- survey 문헌의 세부 실험 설정과 수치는 원문 정밀 독해 후 필요한 부분만 반영한다.

## 2. 실험 한계

- W10 실험은 synthetic 2차원 binary classification과 toy logistic regression만 사용한다.
- 실제 FL framework, 실제 의료·금융·모바일 데이터, 실제 secure aggregation protocol은 사용하지 않았다.
- Backdoor trigger는 교육용 toy feature shift이며 실제 공격 payload가 아니다.
- Privacy Leakage Proxy는 update norm 기반 대용 지표이며 실제 데이터 복원 성공률이 아니다.

## 3. 연구 오픈문제

| 오픈문제 | 설명 | 후속 작업 |
|---|---|---|
| Utility-security trade-off | robust aggregation이 ASR을 낮추더라도 clean accuracy, convergence, communication cost와 충돌할 수 있다. | 복수 seed와 여러 aggregation rule 비교 |
| Secure aggregation과 검증 충돌 | update privacy를 높이면 악성 update 탐지가 어려워질 수 있다. | secure aggregation 조건의 audit 가능성 검토 |
| Non-IID robustness | client별 데이터 분포 차이가 공격과 방어 효과를 모두 바꾼다. | Dirichlet split 등 다양한 non-IID 설정 추가 |
| Privacy metric 정교화 | proxy 지표만으로 실제 leakage를 설명하기 어렵다. | DP, membership inference, gradient inversion 별도 실험 설계 |
| 정책·책임성 | FL 운영자는 client 동의, 로그, 사고 대응 책임을 함께 다뤄야 한다. | P04 기반 정책 체크리스트 작성 |

## 4. 기말 논문 연결

기말 논문에서는 W10을 핵심 실험 주차로 쓰기보다 W11, W14와 연결해 "분산/프라이버시 보존형 AI 시스템의 보안 평가표"를 구성하는 보조 근거로 활용한다.
