# 한계와 오픈문제

## 1. 한계

| 구분 | 내용 | 보완 방향 |
|---|---|---|
| 문헌 검증 | P03 DOI metadata는 확인했지만 지정 논문 원문과 로컬 PDF가 일치하지 않는다. | Dwivedi et al. 원문 PDF 확보 후 저자명·권호·Article 번호 재확인 |
| 출판 정보 | P05는 최종 DOI `10.1145/3774643`을 확인했지만 권호/issue는 ACM 페이지에서 재확인해야 한다. | ACM/출판사 페이지 최종 확인 |
| 실험 범위 | W15 실행은 제출 준비 감사이며 모델 성능 실험이 아니다. | 필요 시 공개/synthetic toy evaluation 별도 설계 |
| XAI 평가 | 설명 안정성과 충실도를 실제 모델 출력으로 측정하지 않았다. | 향후 XAI output 샘플과 perturbation test 추가 |
| 국내 문헌 | 기말논문 국내 문헌 후보가 아직 확정되지 않았다. | KCI/DBpia/RISS 검색 후 검증표 갱신 |

## 2. 오픈문제

1. LLM benchmark contamination을 소규모 수업 과제 수준에서 어떻게 안전하고 검증 가능하게 점검할 것인가?
2. XAI 설명의 fidelity와 privacy leakage를 동시에 낮추는 공개 범위 정책은 어떻게 설계할 것인가?
3. AI 보안 논문에서 실험 재현성, 참고문헌 검증, AI 활용 고지를 평가 루브릭으로 어떻게 계량화할 것인가?
4. RAG 문서 오염, prompt injection, privacy leakage, benchmark leakage를 하나의 생명주기 표에 넣을 때 과도한 단순화를 어떻게 피할 것인가?
5. 대체 PDF나 미검증 DOI가 있는 상태에서 기말논문 초안을 작성할 때 어디까지 본문에 반영할 수 있는가?

## 3. 기말논문 후속 작업

- P03 원문 확보와 요약 재작성
- P05 권호/issue와 최종 formatted PDF 확인
- 국내 문헌 3편 이상 검증
- 최종 논문 표 1개와 그림 1개 실제 삽입
- W15 감사 결과와 W14 실험 결과의 수치 일치 여부 최종 확인
