# 6. 보안적 함의

## 6.1 기밀성

프롬프트와 검색 문서에 포함된 민감정보가 모델 출력으로 노출될 수 있다.

## 6.2 무결성

RAG 문서 오염과 benchmark contamination은 모델 응답과 평가 결과의 무결성을 훼손한다.

## 6.3 가용성

과도한 보안 통제는 응답 지연과 비용 증가를 유발할 수 있으므로 utility와 cost를 함께 본다.

## 6.4 프라이버시

privacy leakage와 membership inference 위험은 실제 개인정보가 아닌 synthetic data로 안전하게 평가한다.

## 6.5 안전성

의료, 법률, 보안 조언처럼 안전중요 영역에서는 human approval gate가 필요하다.

## 6.6 책임성

참고문헌 검증, AI 활용 고지, 실험 로그 보존은 연구자의 최종 책임을 명확히 한다.
