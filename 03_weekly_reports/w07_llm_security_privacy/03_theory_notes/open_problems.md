# 한계와 오픈문제

## 1. 문헌 검증 한계

P01과 P05는 로컬 PDF 기준 DOI를 확인했다. P02, P03, P04는 arXiv/PDF 기준으로 제목·저자·식별자를 확인했지만, 프롬프트에 적힌 출판정보와 로컬 PDF 표기가 일부 달라 공식 출판사 페이지에서 권호와 DOI를 재검증해야 한다.

## 2. 방법론 한계

LLM 학습/정렬/평가와 보안·프라이버시는 하나의 지표로 요약하기 어렵다. ASR만 낮추면 정상 사용자의 over-refusal을 놓칠 수 있고, utility만 보면 privacy leakage와 insecure code generation 위험을 놓칠 수 있다.

## 3. 재현성 한계

W07에서는 seed 42, config, synthetic prompt category, 실행 로그를 보존했다. 다만 이 실험은 실제 LLM/API를 호출하지 않은 toy guard simulator이므로 실제 모델 성능으로 일반화할 수 없다.

## 4. 기말 논문으로 남길 질문

1. 실제 LLM/RAG 시스템에서는 어떤 prompt set과 정책 라벨을 사용할 것인가?
2. Utility, ASR, leakage, refusal quality, code risk의 가중치를 어떻게 정할 것인가?
3. Benchmark contamination과 prompt leakage를 같은 평가표에서 어떻게 구분할 것인가?
4. 사람 평가자 검토와 자동 평가 지표를 어떤 순서로 결합할 것인가?
