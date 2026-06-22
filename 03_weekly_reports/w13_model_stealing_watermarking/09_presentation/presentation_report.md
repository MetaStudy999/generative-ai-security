# W13 발표용 보고서

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W13 |
| 주제 | 모델 지식재산(IP)·모델 도난·모델 추출 위협 |
| 발표 시간 | 8-10분 |
| 핵심 메시지 | 모델 추출 위험은 fidelity로, 소유권 검증은 detection과 false positive를 함께 보고해야 한다. |
| 실험 근거 | `../04_experiment/outputs/run_log.md` |

## 2. 한 문장 요약과 발표 흐름

W13는 모델이 API 뒤에 숨어 있어도 query-response 정보만으로 행동이 모방될 수 있고, 워터마크 검출도 위양성과 함께 평가해야 함을 보여준다.

발표 흐름은 문제 제기, 문헌 역할, AI 원리, 보안 이슈, toy 실험 결과, 한계, 기말논문 연결 순서로 구성한다.

## 3. 논문 5편의 발표 역할

| ID | 역할 |
|---|---|
| P01 | model stealing/extraction taxonomy와 query budget 관점 |
| P02 | LLM watermarking과 생성물 추적 보조 배경, 대체 PDF 상태 |
| P03 | DNN watermarking의 fidelity-robustness-capacity trade-off |
| P04 | ModelShield와 extraction 이후 ownership check |
| P05 | GAN privacy/security 보조 배경, 대체 PDF 상태 |

## 4. AI 원리 70% 발표 설명

모델 IP는 파라미터만이 아니라 출력 행동과 생성물 출처까지 포함한다. 모델 추출은 입력과 출력의 쌍을 모아 substitute model을 학습하는 방식으로 이해할 수 있다. 그래서 API가 black-box여도 출력 정보량과 query budget이 충분하면 모델 행동을 상당히 근사할 수 있다.

## 5. 보안 이슈 30% 발표 설명

보안 이슈는 두 축이다. 첫째, 모델 추출은 confidentiality와 accountability를 흔든다. 둘째, 워터마크는 소유권 검증에 유용하지만 false positive와 utility degradation이 있으면 증거력이 약해진다.

## 6. 실습/실험 실행 상태와 결과 근거

| 조건 | Query Budget | Extraction Fidelity | Substitute Accuracy | Watermark Detection | False Positive Rate |
|---|---:|---:|---:|---:|---:|
| Substitute query 100 | 100 | 0.864000 | 0.812000 | 0.700000 | 0.600000 |
| Substitute query 500 | 500 | 0.920000 | 0.840000 | 1.000000 | 0.600000 |
| Substitute query 1000 | 1000 | 0.902000 | 0.822000 | 1.000000 | 0.600000 |

Baseline victim model의 utility accuracy는 0.868000이다. 본 결과는 synthetic toy 실험이며 실제 API나 실제 LLM에 대한 결과가 아니다.

## 7. 기말논문 연결 지점

기말논문에는 “모델 추출 이후 소유권 검증을 위한 다중지표 평가 프레임워크”로 연결한다. 핵심 기여는 extraction fidelity, query budget, watermark detection, false positive, utility accuracy, reproducibility를 같은 표에서 관리하는 것이다.

## 8. 예상 질문과 답변

| 질문 | 답변 |
|---|---|
| detection이 1.000000이면 워터마크 방어가 성공한 것 아닌가? | false positive가 0.600000으로 높아 단독 증거로는 약하다. detection과 FPR을 함께 봐야 한다. |
| query 1000이 query 500보다 fidelity가 낮은 이유는 무엇인가? | 본 실험은 1NN toy substitute라 query 분포와 이웃 선택에 따라 단조 증가가 보장되지 않는다. |
| 이 실험이 실제 API 공격을 의미하는가? | 아니다. synthetic local toy 실험이며 실제 API, 개인정보, 무단 질의는 제외했다. |
| P02/P05는 왜 대체 PDF인가? | 로컬 확보 PDF가 프롬프트 지정 문헌과 달라 대체 문헌으로 표시했다. 최종 제출 전 교체 또는 대체 사유 확정이 필요하다. |
