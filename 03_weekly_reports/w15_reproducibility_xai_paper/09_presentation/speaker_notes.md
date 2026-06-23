# W15 발표자 노트

## 슬라이드 1. 제목

30초. W15는 새 공격 실험을 하는 주차가 아니라, 기말논문 직전 평가·재현성·XAI·연구윤리를 하나의 evidence chain으로 묶는 주차라고 소개한다.

## 슬라이드 2. 오늘의 질문

50초. 평가 데이터, 재현성, XAI 설명, 참고문헌·AI 고지의 네 질문을 던진다. 이 네 가지가 빠지면 성능 수치가 있어도 연구 신뢰성이 약하다는 점을 강조한다.

## 슬라이드 3. 논문 패킷 역할

1분. P01은 LLM 평가, P02는 lifecycle assurance, P04/P05는 XAI와 concept-based explanation을 맡는다. P03은 지정 논문과 로컬 PDF가 달라 검증 필요 사례로 설명한다.

## 슬라이드 4. AI 원리 70%

1분. Evaluation, reproducibility, XAI, paper structure를 보안보다 먼저 설명한다. 보안 이슈는 이 원리의 실패 조건으로 이어진다고 연결한다.

## 슬라이드 5. 보안 이슈 30%

1분. benchmark contamination은 무결성, hidden test leakage는 기밀성, explanation misuse는 안전성과 책임성 문제라고 설명한다.

## 슬라이드 6. 로컬 감사 결과

1분 20초. W15 실습은 모델 성능 실험이 아니라 로컬 산출물 감사라고 먼저 말한다. 47/47, 9/9, PDF 5개, 검증률 0.90, AI 고지 11/11를 `outputs/run_log.md` 기준으로 제시한다.

## 슬라이드 7. 확인 필요 항목

1분. 완성 상태와 별개로 P03 원문 PDF, P05 권호/issue, 국내 문헌, PDF 보관 정책은 남은 리스크라고 말한다. 숨기지 않는 것이 W15의 핵심이라고 정리한다.

## 슬라이드 8. 기말논문 연결

1분. W07/W08/W11/W14/W15를 묶어 LLM/RAG 보안 생명주기 평가 프레임워크로 연결한다고 설명한다.

## 슬라이드 9. 최종 Contribution

1분. contribution 문장을 읽고, 새 공격 절차가 아니라 재현 가능한 평가·통제 체크리스트가 기여라고 강조한다.

## 슬라이드 10. 결론

40초. 평가와 설명은 결과가 아니라 증거라는 메시지로 마무리한다. 질문을 받을 때는 P03 DOI 부분 확인과 대체 PDF 상태를 먼저 투명하게 인정한다.

<!-- formula-visual-speaker-notes:start -->
## 수식·그래프·그림 발표자 노트

- 핵심 수식: Reproducibility Completion Rate, Reference Verification와 Explanation Consistency Proxy. 수식은 표준 정의식이며, 원문 위치나 formal guarantee가 확인되지 않은 부분은 확인 필요로 말한다.
- 기호 정의표는 청중이 식을 해석할 수 있도록 먼저 읽고, 이후 보안 지표와 연결한다.
- 그래프 설명: 그래프는 numeric 또는 ratio로 변환 가능한 reproducibility evidence만 표시한다. `47/47`, `9/9`, `11/11` 같은 비율은 1.0으로 환산해 completeness proxy로만 그렸다. 원문 DOI 세부 검증과 citation 형식은 별도 사람 검토가 필요하다.
- 다이어그램 설명: `reproducibility workflow`는 threat model 또는 평가 pipeline을 한 장으로 보여주는 보조 그림이다.
- 한계 고지: 비율 변환 값은 local completeness proxy이며 학술적 품질 보증 점수가 아니다.
<!-- formula-visual-speaker-notes:end -->
