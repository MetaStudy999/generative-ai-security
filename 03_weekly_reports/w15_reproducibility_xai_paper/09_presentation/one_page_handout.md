# W15 1페이지 요약

## 핵심 메시지

AI 보안 연구의 신뢰성은 단일 성능 수치가 아니라 평가 데이터, 재현성 증거, 설명 신뢰성, 참고문헌 검증, AI 활용 고지가 연결된 evidence chain에서 나온다.

## 논문 패킷 역할

| 논문 | 한 줄 역할 |
|---|---|
| P01 | LLM evaluation을 what/where/how로 정리하고 benchmark contamination을 평가 위험으로 연결 |
| P02 | ML lifecycle assurance를 통해 config, seed, logs, outputs의 필요성을 설명 |
| P03 | XAI 핵심 문헌이지만 로컬 PDF가 대체 문헌이라 검증 필요 사례 |
| P04 | XAI taxonomy와 Responsible AI, privacy/accountability/fairness 연결 |
| P05 | concept-based XAI와 explanation stability/disclosure risk 연결 |

## W15 감사 결과

| 항목 | 결과 |
|---|---:|
| W15 필수 산출물 | 47/47 |
| 기말논문 연결 파일 | 9/9 |
| 로컬 PDF | 5 |
| DOI 확인 | 4 |
| DOI 부분 확인 | 1 |
| DOI 미검증 | 0 |
| 가중 참고문헌 검증률 | 0.90 |
| AI 활용 고지 완성도 | 11/11 |

## 보안적 함의

- Benchmark contamination은 평가 무결성 문제다.
- Hidden test leakage는 기밀성과 무결성을 동시에 훼손한다.
- XAI 설명은 편향과 오류를 찾지만 민감 단서도 노출할 수 있다.
- 허위 DOI, 대체 PDF 은폐, AI 활용 미고지는 연구 책임성을 훼손한다.

## 기말논문 Contribution

본 연구는 LLM/RAG 기반 AI 시스템의 데이터·평가·프롬프트 생명주기에서 prompt injection, benchmark contamination, privacy leakage 위협을 분석하고, 재현성 중심의 보안 평가 체크리스트를 제안한다.

## 남은 확인 항목

P03 지정 논문 원문 PDF 확보, P05 권호/issue 확인, 국내 문헌 3편 이상 검증, public GitHub PDF 보관 정책 검토.

<!-- formula-visual-handout:start -->
## 수식·그래프·그림 보강 요약

| 항목 | 반영 내용 |
|---|---|
| 핵심 수식 | Reproducibility Completion Rate, Reference Verification와 Explanation Consistency Proxy |
| 그래프 | `assets/charts/w15_metrics_chart.png` (`metrics_summary.csv` 기반) |
| 다이어그램 | `assets/diagrams/w15_pipeline_diagram.svg` (reproducibility workflow) |
| 기호 정의 | 통합보고서와 발표 슬라이드의 수식 블록에 포함 |
| 주의사항 | 비율 변환 값은 local completeness proxy이며 학술적 품질 보증 점수가 아니다. |
<!-- formula-visual-handout:end -->
