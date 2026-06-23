# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Deep Reinforcement Learning for Autonomous Driving: A Survey |
| 저자 | B. Ravi Kiran; Ibrahim Sobh; Victor Talpaert; Patrick Mannion; Ahmad A. Al Sallab; Senthil Yogamani; Patrick Perez |
| 학술지/학회 | IEEE Transactions on Intelligent Transportation Systems, Vol. 23, No. 6, pp. 4909-4926 |
| 연도 | 2022 |
| DOI/URL | https://doi.org/10.1109/TITS.2021.3054625 |
| PDF 파일명 | 02_Kiran_et_al_2022_DRL_Autonomous_Driving_Survey.pdf |
| 검증 상태 | 부분 검증: 공식 DOI 메타데이터 확인 완료. DOI 등록/early access는 2021, 최종 출판판은 2022; 로컬 PDF는 arXiv v2 |

## 2. 한 문장 요약

> 이 논문은 자율주행에서 DRL 정책을 실제 시스템에 적용할 때의 시뮬레이터, 안전 검증, sim-to-real gap 문제를 정리하며, 사이버 방어 자동화에서도 운영 환경과 학습 환경의 차이를 평가해야 함을 시사한다.

## 3. 연구문제

자율주행은 perception, planning, control이 순차적으로 연결되는 안전중요 시스템이다. 이 문헌은 DRL이 decision and planning, controller learning, trajectory optimization에 어떻게 쓰이며, 실제 배포에서 어떤 검증 문제가 발생하는지를 묻는다.

## 4. 핵심 개념

| 개념 | 설명 | W09 연결 |
|---|---|---|
| Simulator | 위험한 실제 환경 대신 학습과 평가를 수행하는 공간이다. | toy cyber-defense 사용 근거 |
| Safe RL | 보상을 최대화해도 안전 제약을 어기지 않도록 하는 접근이다. | safety violation rate |
| Validation | 학습 정책이 실제 운용 조건에서 작동하는지 확인한다. | perturbed alert 평가 |
| Sim-to-real gap | 시뮬레이션에서 좋은 정책이 실제 환경에서 실패하는 차이다. | synthetic 실험 일반화 한계 |

## 5. 방법론

자율주행 파이프라인의 구성 요소와 DRL 알고리즘 적용 영역을 survey 방식으로 정리한다. imitation learning, inverse RL, model-based/model-free RL, safe exploration, validation challenge를 함께 논의한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Safety-constrained Reward |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$J(\pi)=\mathbb{E}_\pi\left[\sum_t\gamma^t(r_t-\lambda c_t)\right]$$ |
| 기호·입력·출력 | \(r_t\): task reward, \(c_t\): safety cost, \(\lambda\): 안전 비용 가중치 |
| 직관적 의미 | Safety-constrained Reward는 DRL 사이버보안 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | DRL 사이버보안 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | return, safety violation, false action rate |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 참고만 |

## 6. 주요 결과

DRL은 복잡한 순차 의사결정에 유용하지만, 안전중요 시스템에서는 simulator 품질, validation, safe exploration, credit assignment가 핵심 병목이다. 이는 사이버 방어 에이전트에서도 실제 네트워크가 아니라 synthetic 환경에서 먼저 평가해야 하는 이유가 된다.

## 7. 보안 관점 분석

자율주행의 안전성 논의는 자동화된 사이버 대응의 안전성으로 번역할 수 있다. 잘못된 자동 격리, 잘못된 패치, 과잉 대응은 보안 시스템에서도 availability와 safety 문제를 만든다.

## 8. 한계와 오픈문제

도메인이 자율주행이므로 IDS/IPS, IAM, cyber-defense의 구체적 공격면은 직접 다루지 않는다. W09에서는 이 논문을 안전한 자동화 정책과 검증 필요성의 비유적 근거로 제한해 사용한다. 로컬 PDF는 arXiv v2이므로 최종 제출 참고문헌에는 IEEE TITS 출판판 정보를 우선한다.

## 9. 기말 논문에 반영할 부분

기말 논문에서 toy simulation의 한계, 실제 운영 환경 전이 문제, 안전 제약 기반 평가 지표를 설명하는 근거로 반영한다.
