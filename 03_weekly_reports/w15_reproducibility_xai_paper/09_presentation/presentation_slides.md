# W15 연구평가·재현성·XAI·논문 구성

AI 보안 연구의 신뢰성은 성능 수치보다 evidence chain에서 나온다.

---

## 오늘의 질문

- 평가 데이터는 오염되지 않았는가?
- 같은 조건에서 결과를 다시 확인할 수 있는가?
- XAI 설명은 믿을 만한가, 아니면 새 공격면인가?
- 참고문헌과 AI 활용 고지는 검증 가능한가?

---

## 논문 패킷 역할

| 논문 | 역할 |
|---|---|
| P01 | LLM evaluation과 benchmark contamination |
| P02 | ML lifecycle assurance와 재현성 증거 |
| P03 | XAI 핵심 문헌, 대체 PDF 검증 이슈 |
| P04 | XAI taxonomy와 Responsible AI |
| P05 | concept-based XAI와 설명 안정성 |

---

## AI 원리 70%

- Evaluation: 무엇을, 어디서, 어떻게 평가할지 정한다.
- Reproducibility: config, seed, log, outputs가 결론의 근거가 된다.
- XAI: 설명도 fidelity, stability, leakage risk를 평가해야 한다.
- Paper structure: contribution과 limitation이 연구 신뢰성을 만든다.

---

## 보안 이슈 30%

| 자산 | 위협 |
|---|---|
| Benchmark | contamination, hidden test leakage |
| Model/explanation | model leakage, explanation gaming |
| Paper | fabricated citation, unverifiable DOI |
| AI worklog | missing disclosure, 책임 추적 실패 |

---

## 로컬 감사 결과

| 항목 | 결과 |
|---|---:|
| W15 필수 산출물 | 47/47 |
| 기말논문 연결 파일 | 9/9 |
| 로컬 PDF | 5 |
| 가중 참고문헌 검증률 | 0.70 |
| AI 활용 고지 완성도 | 9/9 |

---

## 확인 필요 항목

- P03: 지정 논문 원문과 로컬 PDF 불일치
- P05: arXiv는 확인, 최종 DOI 필요
- 기말논문: 국내 문헌 3편 이상 검증 필요
- 최종본: 표와 그림 실제 삽입 필요

---

## 기말논문 연결

최종 주제: AI 보안 연구의 재현 가능한 생명주기 기반 평가 프레임워크

대상 위협:

- prompt injection
- benchmark contamination
- privacy leakage
- reproducibility failure

---

## 최종 Contribution

본 연구는 LLM/RAG 기반 AI 시스템의 데이터·평가·프롬프트 생명주기에서 prompt injection, benchmark contamination, privacy leakage 위협을 분석하고, 재현성 중심의 보안 평가 체크리스트를 제안한다.

---

## 결론

W15의 결론은 간단하다.

평가와 설명은 결과가 아니라 증거다. 증거는 DOI, config, seed, log, output, AI disclosure와 함께 남을 때 신뢰할 수 있다.
