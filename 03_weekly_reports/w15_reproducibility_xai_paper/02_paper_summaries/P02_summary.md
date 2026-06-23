# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges |
| 저자 | Rob Ashmore, Radu Calinescu, Colin Paterson |
| 학술지/학회 | ACM Computing Surveys 54(5), Article 111 |
| 연도 | 2021 |
| DOI/URL | `https://doi.org/10.1145/3453444` |
| PDF 파일명 | `02_Ashmore_Calinescu_Paterson_2021_Assuring_ML_Lifecycle.pdf` |
| 검증 상태 | White Rose accepted version 표지와 DOI/Crossref metadata에서 확인. 로컬 PDF는 최종 출판본이 아니라 accepted version |

## 2. 한 문장 요약

> 이 논문은 ML 생명주기의 data management, model learning, model verification, model deployment 단계별 보증 요구와 방법을 정리하며, AI 보안 연구에서 재현성 기록을 안전성 증거로 다루는 근거를 제공한다.

## 3. 연구문제

안전중요 ML 시스템에서 모델이 의도한 사용 환경에 충분히 안전하다는 증거를 어떻게 만들고 유지할 것인가가 핵심 질문이다. 기말논문에서는 이 질문을 LLM/RAG 연구의 데이터, 프롬프트, 평가셋, 로그, 제출물 단계로 옮겨 재현성 체크리스트를 구성한다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| ML lifecycle | 데이터 관리부터 배포까지 이어지는 반복 과정 | 생명주기 기반 위협모형 |
| Assurance evidence | 안전 주장을 뒷받침하는 검증 가능한 증거 | config, seed, logs, outputs 보존 |
| Verification and validation | 요구사항 충족과 실제 사용 적합성 확인 | toy evaluation 설계 |
| Deployment assurance | 운영 환경 통합 후 감시와 갱신 관리 | MLOps 공급망 보안 연결 |

## 5. 방법론

기존 ML 보증 방법을 생명주기 단계별 desiderata, 방법, 한계, open challenge로 정리한다. 본 보고서에서는 이 구조를 W15의 연구평가와 기말논문 제출 전 점검표로 전환했다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Assurance Evidence Coverage |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$Coverage=\frac{N_{verified\ evidence}}{N_{required\ evidence}}$$ |
| 기호·입력·출력 | \(N_{verified\ evidence}\): 검증 완료 증거 수, \(N_{required\ evidence}\): 요구 증거 수 |
| 직관적 의미 | Assurance Evidence Coverage는 Reproducibility·XAI 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Reproducibility·XAI 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | coverage, reproducibility score, audit finding count |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

ML 보증은 모델 학습 후 성능만 확인하는 절차가 아니라 데이터 준비, 학습, 검증, 배포의 각 단계에서 근거를 축적하는 과정이다. 재현성은 부가 문서가 아니라 안전 주장과 책임성의 일부가 된다.

## 7. 보안 관점 분석

데이터 출처 불명, seed/config 누락, 검증 로그 부재, 배포 후 모니터링 실패는 보안 연구에서도 재현성 실패와 연구 무결성 훼손으로 이어진다. 따라서 실험 결과를 주장할 때는 산출물과 로그를 함께 남겨야 한다.

## 8. 한계와 오픈문제

논문은 ML 전반의 assurance survey이므로 생성형 AI 특유의 prompt injection, RAG 문서 오염, benchmark leakage는 별도 보완이 필요하다.

## 9. 기말 논문에 반영할 부분

기말논문의 연구방법과 부록에서 `config -> seed -> outputs -> run_log -> reference verification -> AI disclosure`로 이어지는 evidence chain을 설계하는 근거로 사용한다.
