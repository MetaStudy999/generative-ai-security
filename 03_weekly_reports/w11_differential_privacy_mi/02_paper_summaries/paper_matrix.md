# W11 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | AI 원리 기여 | 보안 위협 연결 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|---|
| P01 | DP가 ML에서 오용될 때 어떤 privacy claim 문제가 생기는가 | 비판적 문헌검토, DP misuse/reporting 분석 | ML privacy claim 사례 중심 | epsilon/delta 해석, DP claim reporting 책임 | 잘못된 DP 보장, 큰 epsilon, accountant 누락 | privacy budget, utility, efficiency, reporting completeness | DOI `10.1145/3547139` 확인, 로컬 PDF는 arXiv 판 | DP reporting checklist와 misuse 기준 |
| P02 | 중앙집중형 DP-DL의 최신 연구축은 무엇인가 | systematic survey, DP-DL taxonomy | centralized deep learning DP 문헌 분류 | DP-SGD, clipping, noise, accountant, utility-privacy trade-off | privacy leakage, auditing failure, incomplete accounting | accuracy, privacy auditing, utility trade-off | DOI `10.1145/3712000` 확인, 강의자료의 저자명/권호 표기 대조 필요 | DP-DL 평가 프로토콜의 상위 분류 |
| P03 | DP deep learning에서 보호 대상과 적용 위치는 어떻게 달라지는가 | 지정 논문과 로컬 대체 PDF 분리 필요 | 지정 논문은 Neurocomputing, 로컬 대체 PDF는 DP-FL systematic review | centralized/deep/FL DP 적용 위치 비교 | sample-level, client-level, update-level leakage | epsilon/accounting, utility, FL privacy metric | 지정 논문 PDF 미확보, 강의자료의 저자명 표기 확인 필요, 대체 PDF 상태 | W10-FL과 W11-DP 연결, 단 대체 PDF를 지정 논문처럼 인용 금지 |
| P04 | MI 공격은 어떤 조건에서 privacy breach가 되는가 | MI attack taxonomy survey | model output, confidence, loss 기반 공격 문헌 | MI attack의 threat model과 signal 분류 | membership inference, confidence leakage, overfitting | MI attack accuracy, TPR/FPR, confidence gap | DOI `10.1145/3523273` 확인, 로컬 PDF는 arXiv/ACM preprint 판 | W11 threat model 핵심 근거 |
| P05 | MI 방어는 어떤 utility-privacy trade-off를 만드는가 | MI defense taxonomy survey, 로컬 대체 PDF 분리 필요 | 지정 논문은 ACM CSUR, 로컬 대체 PDF는 FL-MIA survey | output restriction, regularization, DP, calibration 등 방어축 | output leakage, overfitting, FL update leakage | clean accuracy, MI risk, utility drop | DOI `10.1145/3620667` 확인, 지정 논문 PDF 미확보, 강의자료의 저자명 표기 확인 필요 | 방어 평가표와 보안적 함의, 단 대체 PDF를 지정 논문처럼 인용 금지 |

## 종합 비교

### 1. 공통적으로 다루는 문제

다섯 편은 모두 학습 데이터의 존재 여부 또는 민감 정보가 모델 산출물에서 새어 나올 수 있는지 다룬다. P01/P02/P03은 DP 원리, DP-SGD, privacy accounting, DP reporting 책임을 중심으로 privacy claim의 근거를 묻는다. P04/P05는 membership inference attack과 defense taxonomy를 통해 모델 출력, confidence, loss, overfitting이 privacy breach로 이어지는 조건을 정리한다.

### 2. 논문 간 차이점

P01은 DP claim 자체의 오용을 비판하는 기준점이다. P02는 중앙집중형 deep learning에서 DP-SGD, auditing, utility-privacy trade-off를 체계화한다. P03은 지정 논문과 로컬 대체 PDF가 달라서 deep learning DP와 federated DP를 분리해 다뤄야 한다. P04는 MI 공격 taxonomy를 제공하고, P05는 방어 taxonomy와 utility-privacy trade-off를 설명한다.

### 3. 아직 해결되지 않은 문제

DP 적용 여부만으로 privacy가 보장되었다고 말할 수 없다. 같은 noise라도 accounting 방식, 공격자 관측 가능성, 출력 제한 여부, 데이터 분포, overfitting 정도에 따라 MI 위험이 달라진다. `epsilon_proxy`는 formal accountant 산출값이 아니므로 실제 DP 보장으로 해석하면 안 된다.

### 4. W11 toy 실험과의 연결

W11 toy 실험은 실제 개인정보, 실제 DP-SGD library, formal accounting, 실제 MI 공격을 구현하지 않는다. synthetic binary classification 기반 toy logistic regression으로 Non-DP baseline, DP-like noise low/medium/high 조건을 비교하여 accuracy, train accuracy, MI attack accuracy proxy, privacy leakage score, utility drop, noise multiplier, reproducibility evidence를 기록하는 형식만 검증한다.

### 5. 기말 논문 주제로 발전 가능한 연결부

기여 후보는 “AI 보안 연구에서 privacy claim을 검증하기 위한 최소 보고항목: accuracy, train accuracy, MI attack accuracy, privacy leakage score, utility drop, epsilon/accounting, noise setting, seed/config/output log”로 정리할 수 있다. P03/P05는 원문 확보 전까지 대체 PDF로만 표시하고, 지정 논문처럼 확정 인용하지 않는다.
