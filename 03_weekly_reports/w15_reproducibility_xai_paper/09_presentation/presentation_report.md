# W15 발표용 보고서

## 1. 발표 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W15 |
| 주제 | 연구평가·재현성·설명가능성(XAI)·논문 구성 |
| 발표 시간 | 8-10분 |
| 핵심 메시지 | AI 보안 연구의 신뢰성은 성능 수치보다 평가 데이터, 재현성 증거, 설명 신뢰성, 참고문헌·AI 고지의 추적성에서 나온다. |
| 실험 근거 | `04_experiment/outputs/run_log.md` |

## 2. 한 문장 요약과 발표 흐름

W15는 LLM 평가, ML lifecycle assurance, XAI, concept-based explanation을 묶어 기말논문의 재현성 중심 평가·통제 프레임워크로 압축한다.

발표 흐름은 `왜 평가 신뢰성이 문제인가 -> 논문 5편 역할 -> AI 원리 70% -> 보안 이슈 30% -> 로컬 감사 결과 -> 기말논문 contribution` 순서로 진행한다.

## 3. 논문 5편의 발표 역할

| ID | 발표 역할 |
|---|---|
| P01 | LLM 평가를 what/where/how로 나누고 benchmark contamination을 평가 위협으로 설명 |
| P02 | ML lifecycle assurance를 통해 config, seed, log, outputs를 evidence chain으로 설명 |
| P03 | XAI 핵심 개념 문헌이지만 현재 PDF가 대체 문헌이라는 검증 이슈를 보여주는 사례 |
| P04 | XAI taxonomy와 Responsible AI가 privacy, accountability, fairness와 연결되는 지점 |
| P05 | concept-based XAI가 feature-level 설명을 보완하면서도 concept leakage 위험을 갖는 지점 |

## 4. AI 원리 70%와 보안 이슈 30%

| 구분 | 발표 포인트 |
|---|---|
| AI 원리 70% | Evaluation, reproducibility, lifecycle assurance, XAI, concept-based explanation, 논문 contribution/limitation |
| 보안 이슈 30% | benchmark contamination, hidden test leakage, model leakage, explanation misuse, 허위 DOI·AI 사용 은폐 |

핵심 설명은 "평가와 설명은 증거이면서 동시에 보호해야 할 자산"이라는 점이다.

## 5. 실습/실험 실행 상태와 결과 근거

W15 실습은 모델 성능 실험이 아니라 로컬 산출물 감사다. 실행 결과는 다음과 같다.

| 점검 항목 | 결과 | 상태 |
|---|---:|---|
| W15 필수 산출물 | 47/47 | complete |
| 기말논문 연결 파일 | 9/9 | complete |
| 로컬 PDF | 5 | complete |
| DOI 확인 | 3 | partial |
| DOI 부분 확인 | 1 | partial |
| DOI 미검증 | 1 | attention |
| 가중 참고문헌 검증률 | 0.70 | partial |
| AI 활용 고지 완성도 | 9/9 | complete |

P03은 지정 논문 원문과 로컬 PDF가 일치하지 않고, P05는 최종 DOI가 필요하므로 발표에서도 `확인 필요`로 말한다.

## 6. 기말논문 연결 지점

W15는 기말논문의 연구방법, 평가방법, 보안적 함의, 부록에 직접 연결된다. 최종 주제는 "AI 보안 연구의 재현 가능한 생명주기 기반 평가 프레임워크: LLM·RAG·프라이버시 위협 중심"으로 압축한다.

## 7. 예상 질문과 답변

| 질문 | 답변 |
|---|---|
| W15 감사 결과가 모델 성능을 의미하는가? | 아니다. 산출물 존재, 참고문헌 검증 상태, AI 고지 완성도를 확인한 로컬 감사 결과다. |
| DOI 확인이 3개뿐이면 제출해도 되는가? | 제출본에는 확인 필요 상태를 명시할 수 있지만, 최종 기말논문 확정 참고문헌에는 공식 DOI/URL을 확인한 항목만 넣어야 한다. |
| XAI는 방어인가 공격면인가? | 둘 다다. 설명은 편향과 오류를 찾는 방어 도구지만, 민감 feature나 우회 단서를 노출할 수 있다. |
| benchmark contamination은 왜 보안 문제인가? | 평가셋이 유출되면 성능이 과대평가되어 연구 결과의 무결성이 깨지기 때문이다. |
