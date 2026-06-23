# P02 Summary

## Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges — Rob Ashmore, Radu Calinescu, Colin Paterson, ACM Computing Surveys, 2021

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W01 딥러닝 패러다임 & ML 보안 분류학 |
| 논문명 | Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges |
| 저자 | Rob Ashmore, Radu Calinescu, Colin Paterson |
| 학술지 | ACM Computing Surveys |
| 권호/쪽 | Vol. 54, No. 5, Article 111 |
| 연도 | 2021 |
| DOI | https://doi.org/10.1145/3453444 |
| 공개 원고 | https://arxiv.org/abs/1905.04223 |
| 논문 유형 | Survey / Assurance Framework Review |
| 로컬 PDF | `01_papers/pdf/02_Ashmore_Calinescu_Paterson_2021_Assuring_ML_Lifecycle.pdf` |
| 강의계획서 지정 논문과 일치 여부 | 일치 |
| 핵심 근거 사용 가능 여부 | 가능 |
| 검증 메모 | DOI, arXiv 공개 원고, 로컬 PDF 목록 기준으로 확인. 최종 제출 시 ACM 공식 서지정보와 참고문헌 형식을 재확인한다. |

---

## 1. 한 문장 요약

이 논문은 ML 컴포넌트의 신뢰성을 단일 모델 정확도 문제가 아니라 **데이터 관리, 모델 학습, 모델 검증, 모델 배포로 이어지는 전체 생명주기에서 충분한 보증 증거를 생성·추적·검토하는 문제**로 재정의한 핵심 survey 논문이다.

---

## 2. 연구문제

이 논문의 핵심 연구문제는 다음과 같이 정리할 수 있다.

> 안전 중요 시스템에 ML 컴포넌트를 통합하려면, ML 생명주기의 각 단계에서 어떤 보증 요건과 증거가 필요하며, 기존 방법들은 그 요건을 어느 정도 충족하는가?

### 세부 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | ML 생명주기는 어떤 단계와 산출물로 구성되는가? |
| RQ2 | 각 생명주기 단계에서 요구되는 assurance desiderata는 무엇인가? |
| RQ3 | 데이터 관리, 모델 학습, 모델 검증, 모델 배포 단계에서 신뢰성 증거를 생성하는 방법은 무엇인가? |
| RQ4 | 기존 assurance 방법으로 충분히 해결되지 않은 open challenge는 무엇인가? |
| RQ5 | AI 보안 관점에서 poisoning, evasion, privacy leakage, drift, model extraction 위험은 생명주기 어디에 배치되는가? |

---

## 3. 핵심 이론 및 수식

> 작성 원칙: 이 논문은 수식 중심 논문이 아니라 생명주기 보증 프레임워크 논문이다. 따라서 원문 수식을 억지로 만들지 않고, ML 보증을 기말논문 실험·감사 프레임워크에 연결하기 위한 표준화 가능한 지표와 절차식을 보조적으로 정리한다. GitHub, MS Word, PDF 변환 호환성을 위해 수식은 표 안에 넣지 않고 별도 블록 수식으로 작성한다.

### 3.1 ML 생명주기 보증 함수

ML 보증은 단일 정확도 지표가 아니라 생명주기 단계별 증거 집합을 종합하는 과정으로 볼 수 있다.

$$
A_{ML} = g(E_D, E_L, E_V, E_{Dep})
$$

| 기호 | 의미 |
|---|---|
| $A_{ML}$ | ML 컴포넌트의 assurance 수준 또는 보증 판단 |
| $g(\cdot)$ | 단계별 증거를 종합하는 평가 함수 |
| $E_D$ | Data Management 단계의 증거 |
| $E_L$ | Model Learning 단계의 증거 |
| $E_V$ | Model Verification 단계의 증거 |
| $E_{Dep}$ | Model Deployment 단계의 증거 |

### 보안적 의미

이 식은 ML 보증이 모델 정확도 하나로 결정되지 않음을 보여준다. 데이터 출처, 라벨 품질, 학습 설정, 검증 데이터 독립성, 배포 후 모니터링, 변경 이력 중 하나라도 부족하면 전체 assurance case가 약해진다.

| 생명주기 증거 | 보안 관점에서 필요한 기록 |
|---|---|
| $E_D$ | 데이터 출처, 라벨링 기준, 개인정보 처리, 오염 가능성, 데이터 버전 |
| $E_L$ | 모델 구조, 학습 코드, hyperparameter, seed, 학습 로그 |
| $E_V$ | 테스트셋 독립성, robust accuracy, FPR/FNR, stress test, formal property |
| $E_{Dep}$ | 배포 버전, 접근권한, drift 모니터링, 로그, 사고대응, rollback 기록 |

---

### 3.2 생명주기 위험 점수

기말논문에서 ML 또는 RAG 보안 위험을 정량화하려면 단계별 위험을 가중합으로 표현할 수 있다.

$$
Risk_{LC} = \sum_{s \in S} w_s \cdot r_s
$$

| 기호 | 의미 |
|---|---|
| $Risk_{LC}$ | 전체 생명주기 위험 점수 |
| $S$ | 생명주기 단계 집합. 예: data, learning, verification, deployment |
| $w_s$ | 단계 $s$의 중요도 가중치 |
| $r_s$ | 단계 $s$에서 관측된 위험 수준 |

### 보안적 의미

공격자는 모델 자체만 공격하지 않는다. 데이터 수집 단계에서는 poisoning이나 privacy leakage가 발생할 수 있고, 검증 단계에서는 평가셋 오염이나 benchmark contamination이 발생할 수 있으며, 배포 단계에서는 evasion, drift, model extraction, logging failure가 발생할 수 있다. 따라서 생명주기별 위험 점수는 “어디서 사고가 발생했는가”를 설명하는 감사 프레임워크의 뼈대가 된다.

---

### 3.3 보증 증거 커버리지

보증 증거가 충분한지 확인하기 위해 요구사항 대비 증거 커버리지를 계산할 수 있다.

$$
Coverage_E = \frac{|R_{covered}|}{|R_{total}|}
$$

| 기호 | 의미 |
|---|---|
| $Coverage_E$ | 보증 증거 커버리지 |
| $R_{covered}$ | 증거가 존재하는 요구사항 또는 보안통제 항목 집합 |
| $R_{total}$ | 전체 요구사항 또는 보안통제 항목 집합 |

### 보안적 의미

정확도가 높더라도 데이터 출처, 모델 설정, 평가 로그, 배포 모니터링 증거가 누락되어 있으면 assurance case가 약하다. 따라서 기말논문에서는 실험 수치뿐 아니라 “어떤 증거가 존재하는가”를 표로 남겨야 한다.

---

## 4. AI 원리 관점 분석

| 항목 | 분석 |
|---|---|
| ML 생명주기 | 데이터 관리, 모델 학습, 모델 검증, 모델 배포의 네 단계로 ML 개발과 운영을 구조화한다. |
| 데이터 관리 | 데이터 수집, 전처리, 라벨링, 증강, 분석을 통해 학습·검증 데이터셋을 구성한다. |
| 모델 학습 | 알고리즘 선택, 손실함수, hyperparameter, validation 전략, transfer learning 등을 포함한다. |
| 모델 검증 | 일반화 성능, 테스트 기반 검증, formal verification, 요구사항 충족 여부를 점검한다. |
| 모델 배포 | 모델을 실제 시스템에 통합하고, 운영 중 모니터링·업데이트·유지보수를 수행한다. |
| 반복성 | 검증 실패나 운영 문제 발생 시 데이터 관리 또는 모델 학습 단계로 되돌아가는 반복 구조를 가진다. |
| 자율시스템 연결 | 배포된 ML 컴포넌트는 MAPE loop의 monitoring, analysis, planning, execution 과정에 통합될 수 있다. |

---

## 5. 보안 이슈 관점 분석

P02는 W01에서 가장 중요한 “보안 평가 프레임” 문헌이다. 이 논문은 보안 공격을 직접 다루는 논문은 아니지만, AI 보안 위협을 생명주기 단계별로 배치할 수 있는 구조를 제공한다.

| 생명주기 단계 | 대표 보안 위험 | 필요한 보증 증거 |
|---|---|---|
| Data Management | 데이터 오염, 라벨 조작, 개인정보 포함, 데이터 편향 | 데이터 출처표, 라벨링 기준, 데이터 버전, 개인정보 점검표 |
| Model Learning | 백도어 학습, 과적합, 부적절한 hyperparameter, 재현 불가능한 학습 | config, seed, 학습 로그, 코드 버전, 모델 카드 |
| Model Verification | 평가셋 오염, benchmark contamination, 공격 조건 미평가, 지표 왜곡 | 독립 테스트셋, robust test, FPR/FNR, ASR, 검증 보고서 |
| Model Deployment | drift, evasion, model extraction, 권한 오남용, 로그 누락 | 배포 버전, API 접근 로그, drift metric, 모니터링 대시보드, incident log |

---

## 6. 위협모형

### 6.1 보호 대상

| 보호 대상 | 설명 |
|---|---|
| 데이터셋 | 학습 데이터, 검증 데이터, 운영 데이터 |
| 학습 파이프라인 | 전처리 코드, 학습 코드, hyperparameter, seed |
| 모델 산출물 | 모델 가중치, 모델 구조, checkpoint, model card |
| 검증 증거 | 테스트 결과, robust evaluation, formal property, 성능 로그 |
| 배포 환경 | API, 권한, 로그, 모니터링, 업데이트 절차 |
| assurance case | 시스템이 요구사항을 만족한다는 주장과 증거의 연결 구조 |

### 6.2 공격자 능력

| 공격자 유형 | 가능 행위 |
|---|---|
| Data attacker | 데이터 수집·라벨링·전처리 과정에 오염을 삽입한다. |
| Training attacker | 학습 코드, hyperparameter, seed, dependency를 조작한다. |
| Evaluation attacker | 테스트셋 오염, benchmark leakage, 지표 선택 편향을 유도한다. |
| Deployment attacker | API를 반복 질의하거나 운영 입력을 조작하여 evasion 또는 model extraction을 시도한다. |
| Insider or process attacker | 로그 삭제, 승인 절차 우회, 모델 버전 변경 등 운영 통제를 약화시킨다. |

### 6.3 공격 경로

```text
데이터 관리 단계의 취약점
→ 학습 데이터 또는 라벨 품질 저하
→ 모델 학습 단계에서 취약한 파라미터 형성
→ 검증 단계에서 위험 조건 미탐지
→ 배포 단계에서 drift/evasion/extraction 발생
→ assurance case 붕괴 및 운영 사고 발생
```

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W01/P02에서의 활용 |
|---|---|---|
| Evidence Coverage | 요구사항 대비 증거가 존재하는 비율 | assurance case의 완성도 평가 |
| Reproducibility Score | 동일 설정으로 결과를 재현할 수 있는 정도 | seed, config, data version, code version 점검 |
| Data Lineage Completeness | 데이터 출처와 변환 이력이 기록된 정도 | poisoning, privacy leakage 추적 |
| Verification Adequacy | 테스트·robustness·formal property 검증의 충분성 | 평가셋 편향과 공격 조건 누락 방지 |
| Drift Metric | 운영 데이터와 학습 데이터 분포 차이 | 배포 후 성능 저하 및 공격 가능성 탐지 |
| Incident Traceability | 사고 발생 시 원인 추적 가능성 | 로그, 승인 이력, 배포 버전 연결 |
| Risk Score | 단계별 위험을 종합한 점수 | 기말논문 보안 감사표 설계에 활용 |

---

## 8. 재현성 점검

이 논문은 survey 성격이므로 특정 실험 결과를 그대로 재현하는 논문은 아니다. 대신 논문이 제시한 ML 생명주기와 assurance desiderata를 실습 프로젝트의 체크리스트로 재현할 수 있다.

| 항목 | 점검 |
|---|---|
| 데이터셋 | UCI digits, MNIST, 보안 로그 데이터셋 등 공개 데이터로 대체 가능 |
| 코드 | 실습 코드와 config를 Git으로 버전 관리해야 함 |
| 학습 환경 | Python 버전, package version, OS, hardware 기록 필요 |
| seed/config | seed, train/test split, hyperparameter, model version 기록 필요 |
| 결과 파일 | metric JSON, CSV, confusion matrix, plot, log 저장 필요 |
| 배포 증거 | 실제 배포가 없다면 pseudo-deployment checklist로 대체 가능 |
| 재현 가능성 판단 | 이론 프레임워크 재현 가능성은 높음. 원문 survey의 모든 문헌 검토 재현은 범위가 큼. |

### W01 실습 연결

W01에서는 P02의 assurance 관점을 다음과 같이 최소 실습으로 구현할 수 있다.

1. 공개 데이터셋을 로딩하고 데이터 출처를 기록한다.
2. train/validation/test split과 seed를 고정한다.
3. 모델 학습 config를 YAML로 저장한다.
4. clean accuracy와 robustness 관련 metric을 JSON으로 저장한다.
5. 실험 로그, 결과표, 그림을 자동 생성한다.
6. 데이터·모델·검증·배포 단계별 evidence checklist를 작성한다.

---

## 9. 논문의 고유 기여

1. ML 보증을 단일 검증 문제가 아니라 데이터 관리부터 배포까지 이어지는 생명주기 문제로 정리했다.
2. Data Management, Model Learning, Model Verification, Model Deployment의 네 단계 구조를 제시했다.
3. 각 단계에서 필요한 assurance desiderata를 정의하고 관련 방법과 한계를 survey 형태로 정리했다.
4. 안전 중요 시스템에서 ML 컴포넌트를 신뢰하려면 성능 수치뿐 아니라 체계적인 보증 증거가 필요함을 강조했다.
5. 기말논문에서 사용할 수 있는 “성능 평가 + 위협모형 + 재현성 증거 + 운영 로그”의 통합 구조를 제공한다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 공격별 세부 수식 부족 | 이 논문은 assurance survey이므로 poisoning, evasion, privacy attack의 세부 수식은 직접 제공하지 않는다. | P04 대적 공격, P05 프라이버시 공격 summary와 결합한다. |
| 보안 위협 분류 직접성 부족 | 안전성과 assurance 중심이며 AI 보안 공격 taxonomy는 별도 보완이 필요하다. | lifecycle 단계별 security threat mapping 표를 추가한다. |
| 운영 데이터 접근 한계 | 실제 배포 환경에서는 로그, drift, incident data가 조직 내부에 있어 공개 재현이 어렵다. | synthetic log 또는 toy MLOps pipeline으로 감사 절차를 재현한다. |
| LLM/RAG 미반영 | 논문 작성 시점상 RAG, LLM agent, prompt injection은 직접 다루지 않는다. | W07, W08, W14, W15의 LLM/RAG/MLOps 문헌으로 확장한다. |
| assurance case 자동화 한계 | 증거를 수집해도 주장-증거 연결이 수작업에 의존할 수 있다. | evidence checklist와 자동 보고서 생성 스크립트를 기말논문 부록으로 제시한다. |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 평가는 모델 정확도만으로 충분하지 않으며 생명주기 보증이 필요하다는 문제의식 제시 |
| 2장 관련연구 | ML lifecycle assurance의 네 단계와 assurance desiderata 정리 |
| 3장 위협모형 | 데이터, 학습, 검증, 배포 단계별 공격자 능력과 공격 경로 정의 |
| 4장 연구방법 | evidence checklist, reproducibility score, lifecycle risk score 설계 |
| 5장 실험/분석 | 실험 결과와 함께 seed, config, data version, metric log를 보증 증거로 제시 |
| 6장 보안적 함의 | CIA, privacy, safety, accountability 관점에서 생명주기 통제 필요성 해석 |
| 7장 결론 | AI 보안 연구는 알고리즘 방어뿐 아니라 보증 증거 기반 운영 프레임워크로 확장되어야 함을 제시 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: ML 보안성은 모델 단독 성능이 아니라 데이터 관리, 모델 학습, 모델 검증, 모델 배포 전 단계의 증거 축적으로 평가해야 한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: ML 생명주기 4단계 도식, 단계별 위협-증거 매핑표, evidence coverage 계산표, reproducibility checklist를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: RAG/LLM 시스템에서도 문서 수집, 임베딩 생성, 검색 평가, 배포 모니터링, 감사로그가 생명주기 증거로 관리되어야 하므로 P02의 assurance 구조를 W08과 W14의 운영형 보안 프레임워크로 확장한다.

---

## 13. 최종 판단

이 논문은 W01의 핵심 보안 프레임 문헌으로 사용한다. P01이 딥러닝의 이론적 기반을 제공한다면, P02는 AI 보안 연구를 “생명주기 보증” 관점으로 확장하는 구조를 제공한다. 기말논문에서는 P02를 중심 프레임으로 삼고, P03의 침입탐지 평가, P04의 대적 공격, P05의 프라이버시 공격을 각 생명주기 단계에 배치하는 방식이 적절하다.

---

## 14. 변환 호환성 메모

- GitHub Markdown, MS Word, PDF 변환 호환성을 위해 수식은 LaTeX 블록 수식으로 작성했다.
- 긴 수식은 Markdown 표 안에 넣지 않고 별도 문단으로 분리했다.
- 표에는 변수 설명과 해석만 배치했다.
- DOCX/PDF 변환 시에는 Pandoc 기준으로 다음 명령을 권장한다.

```bash
pandoc P02_summary.md -o P02_summary.docx
pandoc P02_summary.md -o P02_summary.pdf --pdf-engine=xelatex
```
