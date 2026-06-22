# W15 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | 보안 위협 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 | LLM을 무엇/어디서/어떻게 평가할 것인가 | LLM 평가 survey와 benchmark taxonomy | 문헌 기반, 다양한 benchmark 정리 | benchmark contamination, hidden test leakage | task score, human evaluation, robustness/safety 평가 | 최신 benchmark 변화와 데이터 누수 별도 점검 필요 | LLM/RAG 평가축과 평가오염 위협 정의 |
| P02 | ML lifecycle에서 안전성 증거를 어떻게 만들 것인가 | lifecycle stage별 assurance desiderata 정리 | 문헌 기반, data/model/verification/deployment 단계 분석 | 재현성 실패, evidence gap, deployment risk | assurance evidence, V&V, lifecycle coverage | 생성형 AI 특화 위협은 직접 다루지 않음 | config, seed, log, output 기반 재현성 체계 |
| P03 | XAI의 핵심 개념과 기술을 어떻게 분류할 것인가 | 지정 논문은 확인 필요, 로컬 대체 PDF는 XAI survey | 로컬 대체 PDF: arXiv survey | explanation leakage, misleading explanation | fidelity, stability, user trust, human evaluation | 지정 논문과 로컬 PDF 불일치 | XAI 평가 기준과 대체 PDF 상태 명시 |
| P04 | XAI taxonomy와 Responsible AI를 어떻게 연결할 것인가 | XAI 개념·taxonomy·Responsible AI 논의 | 문헌 기반, 약 400개 XAI 기여 검토 | privacy, confidentiality, robustness, fairwashing | transparency, interpretability, post-hoc explanation quality | LLM/RAG 최신 설명 문제는 별도 보완 필요 | 책임성·보안적 함의 장의 이론 근거 |
| P05 | concept-level 설명은 feature-level 설명을 어떻게 보완하는가 | C-XAI taxonomy, concept/explanation 유형 분류 | 문헌 기반, concept metric과 human evaluation 정리 | concept leakage, explanation gaming, spurious concept | completeness, fidelity, concept error, human evaluation | 최종 DOI 확인 필요, annotation 비용 큼 | explanation stability와 disclosure risk 평가 |

## 종합 비교

### 1. 공통적으로 다루는 문제

다섯 편은 모두 "성능 수치만으로 AI 시스템을 신뢰할 수 없다"는 문제의식을 공유한다. P01은 평가 대상과 benchmark, P02는 생명주기 증거, P03-P05는 설명가능성과 책임성을 다룬다.

### 2. 논문 간 차이점

P01은 LLM 평가의 범위와 benchmark를, P02는 ML 보증의 evidence chain을, P04는 XAI와 Responsible AI의 넓은 taxonomy를 제공한다. P05는 concept라는 더 높은 수준의 설명 단위에 집중한다. P03은 현재 로컬 PDF가 대체 문헌이므로 최종 인용 전 별도 검증이 필요하다.

### 3. 아직 해결되지 않은 문제

- benchmark contamination과 hidden test leakage를 실제 제출 문서에서 어떻게 검증할지 명확한 표준이 부족하다.
- XAI 설명이 충실한 설명인지, 사용자를 설득하는 그럴듯한 설명인지 구분하기 어렵다.
- 설명 공개가 모델·데이터·업무 규칙 누수로 이어질 수 있다.
- 연구자의 AI 도구 사용, DOI 검증, 실험 로그 보존을 기술 평가와 함께 묶는 제출 절차가 아직 약하다.

### 4. 기말 논문 주제로 발전 가능한 연결부

기말논문은 `LLM/RAG 보안 위협 -> 평가오염과 프라이버시 누수 -> 재현성 evidence -> XAI 설명 안정성 -> 참고문헌·AI 고지 체크리스트`로 연결한다. 최종 contribution은 새로운 공격 절차가 아니라, 안전한 문헌분석과 toy evaluation에서 쓸 수 있는 재현성 중심 평가·통제 프레임워크다.
