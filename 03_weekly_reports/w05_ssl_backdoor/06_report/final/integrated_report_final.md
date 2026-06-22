# W05 자기지도학습·파운데이션 모델 & Poisoning/Backdoor 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W05 |
| 주제 | 자기지도학습·파운데이션 모델 & Poisoning/Backdoor |
| AI 원리 | 자기지도학습, contrastive learning, masked modeling, representation learning |
| 보안 이슈 | 표현공간 오염, poisoning, backdoor, 데이터 거버넌스 |
| 문서 상태 | 최종본 |

## 1. 한 문장 요약

W05는 자기지도학습/파운데이션 모델 및 Poisoning/Backdoor를 중심으로 AI 원리와 보안 위협을 함께 정리하고, 기말 논문의 위협모형·평가방법·재현성 설계로 연결한다.

## 2. AI 원리 70% 정리

자기지도학습, contrastive learning, masked modeling, representation learning를 이해하기 위해 자기지도학습의 정의, Contrastive learning, Masked modeling, Predictive learning, Representation learning, Foundation model의 사전학습 구조를 핵심 개념으로 정리했다. 이 원리들은 모델 또는 시스템이 어떤 입력과 학습 구조를 갖고 어떤 기준으로 평가되는지 설명한다.

## 3. 보안 이슈 30% 정리

표현공간 오염, poisoning, backdoor, 데이터 거버넌스를 중심으로 Self-supervised pretraining 단계의 공격면, 데이터 오염과 표현공간 왜곡, Poisoning attack, Backdoor attack, Trigger injection, Feature distribution shift를 정리했다. 보안 분석은 공격 절차 자체보다 보호 자산, 공격자 능력, 방어자 가정, 평가 지표를 명확히 하는 방향으로 작성했다.

## 4. 논문 5편 요약

| ID | 논문 | 저자 | 연도 | 검증 상태 |
|---|---|---|---|---|
| P01 | A Survey on Self-supervised Learning: Algorithms, Applications, and Future Trends | Jie Gui et al. | 2024 | arXiv DOI/URL 확인, 출판 DOI 미확인 |
| P02 | A Comprehensive Survey on Self-Supervised Learning for Recommendation | Xubin Ren et al. | 2025 | DOI 확인 |
| P03 | Self-Supervised Learning for Videos: A Survey | Madeline C. Schiappa et al. | 2023 | DOI 확인 |
| P04 | Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems | Zhibo Wang et al. | 2022 | DOI 확인 |
| P05 | A survey of backdoor attacks and defences: From deep neural networks to large language models | Ling-Xin Jin et al. | 2025 | DOI 확인 |

## 5. 논문 5편 비교

다섯 편은 AI 원리 문헌과 보안 문헌을 함께 포함한다. 기말 논문에서는 개별 문헌의 세부 수치보다 분류체계, 위협모형, 평가 프로토콜의 연결 관계를 우선 반영한다.

## 6. Research Track

### 6.1 연구문제

RQ1. 자기지도학습/파운데이션 모델 및 Poisoning/Backdoor의 생명주기에서 보안 보증을 위해 어떤 평가 항목이 필요한가?

RQ2. Self-supervised pretraining 단계의 공격면, 데이터 오염과 표현공간 왜곡는 어느 단계에서 발생하며 어떤 조건에서 성공하는가?

RQ3. 성능, 보안성, 재현성을 함께 평가하려면 어떤 최소 프로토콜이 필요한가?

### 6.2 위협모형

대상 시스템은 자기지도학습/파운데이션 모델 및 Poisoning/Backdoor 기반 AI/ML 시스템이며, 보호 자산은 데이터, 모델, 입력/컨텍스트, 출력, 로그, 평가셋이다. 공격자는 외부 공격자, 내부자, 데이터 제공자, API 남용자 등으로 나뉜다.

### 6.3 평가방법

Clean performance, attack impact, robust performance, privacy/leakage, reproducibility, human review를 기본 평가 항목으로 둔다.

### 6.4 재현성

Docker, pyproject.toml/uv sync, config, seed, 로그, PDF/DOI 검증표를 함께 보존한다. W05 toy 실험은 `python3 src/run_experiment.py --config configs/config.yaml`로 실행했고, 결과는 `04_experiment/outputs/`에 저장했다.

### 6.5 한계와 오픈문제

P01의 출판 DOI와 일부 원문 세부 수치는 최종 확인이 필요하다. 또한 survey 문헌의 분류체계를 실제 SSL 모델 실험과 어떻게 연결할지는 추가 검토가 필요하다.

## 7. 실습 요약

실습은 synthetic 2D representation 기반으로 실행했다. 실제 개인정보, 실제 서비스 침해, 무단 질의, 악용 가능한 절차는 포함하지 않는다.

| 조건 | Clean Acc. | Poisoned Clean Acc. | ASR | ASR after defense | Mean Shift | Detection Rate | Clean FPR |
|---|---:|---:|---:|---:|---:|---:|---:|
| Clean representation baseline | 1.000000 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 |
| Poisoned/backdoor representation | 해당 없음 | 1.000000 | 1.000000 | 해당 없음 | 2.418677 | 해당 없음 | 해당 없음 |
| Consistency defense check | 해당 없음 | 해당 없음 | 해당 없음 | 0.000000 | 0.090597 | 1.000000 | 0.000000 |

이 결과는 표현공간 오염과 backdoor 평가 지표를 설명하기 위한 toy 값이며, 실제 SSL/파운데이션 모델 보안 성능으로 일반화하지 않는다.

## 8. AI 활용 기록 요약

Codex를 사용해 구조화 초안, synthetic 실험 코드, 제출용 보고서, 발표자료를 작성했다. AI 산출물은 사람 검토와 원문 대조를 거쳐 최종본에 반영한다.

## 9. 토론 질문

1. 자기지도학습/파운데이션 모델 및 Poisoning/Backdoor에서 가장 중요한 보호 자산은 무엇인가?
2. 공격 성공률과 일반 성능을 함께 볼 때 어떤 지표가 가장 설득력 있는가?
3. 원문 검증과 재현성 기록을 어느 수준까지 제출물에 포함해야 하는가?

## 10. 기말 논문 연결

W05는 기말 논문의 관련연구, 위협모형, 평가방법, 보안적 함의 장에 연결된다.

## 11. 참고문헌 검증표

참고문헌은 `01_papers/doi_check.md`에서 DOI/URL 확인 상태를 관리한다.

## 12. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 완료 |
| 비교표 | 완료 |
| AI 원리 70% | 완료 |
| 보안 이슈 30% | 완료 |
| Research Track | 완료 |
| 실험 결과 조작 방지 | 실행 로그 기준 수치만 반영 |
| DOI 임의 생성 방지 | 확인 근거 수준을 구분해 기록 |
| AI 사용 은폐 방지 | AI 활용 고지서 완료 |
| 제출용 보고서/HTML | 완료 |
| 발표자료 | 완료 |
