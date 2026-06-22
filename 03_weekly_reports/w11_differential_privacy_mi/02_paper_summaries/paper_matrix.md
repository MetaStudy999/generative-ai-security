# W11 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | 보안 위협 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 | DP가 ML에서 오용될 때 어떤 privacy claim 문제가 생기는가 | 비판적 문헌검토 | 로컬 PDF 기준 구체 수치 재확인 필요 | 잘못된 DP 보장, 과도한 epsilon | privacy budget, utility/privacy/efficiency | ACM DOI 공식 확인 필요 | DP reporting checklist와 misuse 기준 |
| P02 | 중앙집중형 DP-DL의 최신 연구축은 무엇인가 | systematic survey | DP-DL 문헌 분류 | privacy leakage, auditing failure | accuracy, privacy auditing, utility trade-off | arXiv/ACM 최종본 대조 필요 | DP-DL 평가 프로토콜의 상위 분류 |
| P03 | DP deep learning/DP-FL에서 보호 대상과 적용 위치는 어떻게 달라지는가 | 지정 논문 + 로컬 대체 PDF 분리 | 로컬 대체 PDF는 FL survey | client/sample/update leakage | DP model, neighborhood level, accounting | 지정 논문 PDF 미확보 | W10-FL과 W11-DP 연결 |
| P04 | MI 공격은 어떤 조건에서 privacy breach가 되는가 | MI attack/defense taxonomy | survey 중심 | membership inference, confidence leakage | MI attack accuracy, train/test confidence gap | ACM DOI 공식 확인 필요 | W11 위협모형의 핵심 근거 |
| P05 | MI 방어는 어떤 trade-off를 만드는가 | defense taxonomy + FL 대체 관점 | 로컬 대체 PDF는 FL-MIA survey | output leakage, overfitting, FL update leakage | clean accuracy, MI risk, utility drop | 지정 논문 PDF 미확보 | 방어 평가표와 보안적 함의 |

## 종합 비교

### 1. 공통적으로 다루는 문제

다섯 편은 모두 “학습 데이터의 존재 여부 또는 민감 정보가 모델 산출물에서 새어 나올 수 있는가”라는 질문을 공유한다. DP 문헌은 이 위험을 수학적 보장과 privacy accounting으로 줄이려 하고, MI 문헌은 모델 출력·confidence·loss·update가 공격 신호가 되는 조건을 분류한다.

### 2. 논문 간 차이점

P01은 DP claim의 오용을 비판하고, P02는 중앙집중형 DP-DL의 최신 연구축을 분류한다. P03은 지정 논문과 로컬 대체 PDF가 달라서 deep learning DP와 federated DP를 분리해 다뤄야 한다. P04는 MI 공격 자체의 taxonomy를 제공하고, P05는 방어와 trade-off를 정리한다.

### 3. 아직 해결되지 않은 문제

DP 적용 여부만으로 privacy가 보장되었다고 말할 수 없다. 같은 noise라도 accounting 방식, 공격자 관측 가능성, 출력 제한 여부, 데이터 분포, overfitting 정도에 따라 MI 위험이 달라진다. 또한 P03/P05는 로컬 PDF 대체 상태라 원문 확보가 필요하다.

### 4. 기말 논문 주제로 발전 가능한 연결부

W11는 기말논문의 4장 평가방법과 6장 보안적 함의에 직접 연결된다. 기여 후보는 “AI 보안 연구에서 privacy claim을 검증하기 위한 최소 보고항목: accuracy, MI attack accuracy, privacy leakage score, epsilon/accounting, utility drop, seed/config/output log”로 정리할 수 있다.
