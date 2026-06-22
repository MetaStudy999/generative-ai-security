# P05 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A survey of backdoor attacks and defences: From deep neural networks to large language models |
| 저자 | Ling-Xin Jin et al. |
| 학술지/학회 | Journal of Electronic Science and Technology |
| 연도 | 2025 |
| DOI/URL | DOI: `10.1016/j.jnlest.2025.100326` |
| PDF 파일명 | `05_Jin_et_al_2025_Backdoor_Attacks_and_Defences_Survey.pdf` |
| 검증 상태 | 로컬 PDF XMP 메타데이터에서 DOI 확인 |

## 2. 한 문장 요약

> 이 논문은 DNN부터 LLM까지 backdoor 공격과 탐지·제거·방어 기술을 정리하며, clean accuracy와 ASR이 동시에 필요한 이유를 보여준다.

## 3. 연구문제

Backdoor 공격은 정상 입력에서는 모델이 정상적으로 동작하지만, 특정 trigger가 포함된 입력에서는 공격자가 원하는 행동을 하도록 만드는 조건부 무결성 공격이다. 이 논문은 DNN 대상 backdoor, 탐지 방법, 제거 방법, LLM backdoor까지 확장된 공격·방어 연구 흐름을 정리한다.

## 4. 핵심 개념

| 개념 | 설명 | W02 연결 |
|---|---|---|
| Backdoor trigger | 공격 행동을 활성화하는 특정 패턴 또는 조건 | digits toy trigger 설계 |
| Attack Success Rate | trigger 입력에서 목표 오분류가 발생한 비율 | 핵심 보안 지표 |
| Clean accuracy | 정상 입력에서의 분류 성능 | 은닉성 평가와 함께 사용 |
| Detection | backdoor 여부를 찾는 절차 | 탐지율, 오탐, 관측 가능성 |
| Removal/mitigation | pruning, retraining, preprocessing 등 | 방어 평가 후보 |

## 5. 방법론

논문은 backdoor 공격 기술, 탐지 기술, 제거 방법, LLM 환경의 backdoor 위협을 survey 방식으로 분류한다. 본 보고서에서는 P05를 ASR, clean accuracy 유지율, stealthiness, trigger coverage의 개념 근거로 사용한다.

## 6. 주요 결과

Backdoor 방어는 데이터, 모델 구조, 출력 분포, 재학습, pruning 등 여러 위치에서 가능하지만 어느 하나가 보편적 해결책은 아니다. 특히 LLM 환경에서는 fine-tuning 데이터, instruction data, parameter-efficient tuning, inference-time trigger 등 공격 표면이 넓어진다.

## 7. 보안 관점 분석

P05는 W02의 “clean accuracy와 ASR의 차이”를 설명하는 핵심 문헌이다. 정상 테스트셋 성능이 높아도 trigger 조건에서 목표 오분류가 높으면 보안적으로 실패한 모델일 수 있다. 따라서 실험 보고서와 발표자료는 두 지표를 반드시 분리해서 보여준다.

## 8. 한계와 오픈문제

Backdoor 연구는 모델, 데이터, trigger, fine-tuning 방식에 따라 결과가 크게 달라진다. LLM backdoor는 최신성이 빠르게 변하고 방어 평가 기준도 아직 안정화되지 않았으므로, 기말 논문에서는 “재현 가능한 최소 평가 프로토콜”로 범위를 제한하는 것이 안전하다.

## 9. 기말 논문에 반영할 부분

P05는 기말 논문의 보안적 함의와 평가방법 장에 반영한다. 특히 clean accuracy, ASR, stealthiness, detection rate를 동시에 기록하는 backdoor 평가표의 근거로 사용한다.
