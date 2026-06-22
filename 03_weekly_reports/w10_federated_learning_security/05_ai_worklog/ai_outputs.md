# AI 출력물 요약

| 산출물 | 내용 | 검토 상태 |
|---|---|---|
| 논문 메타데이터 보정 | P01-P05 DOI/URL 대조. P03/P05 출판 DOI 반영, P01 수업자료 표기 차이와 P04 Article 번호는 사람 검토 항목으로 표시 | 완료 |
| 이론노트 | FL 구조, FedAvg, robust aggregation, privacy-utility trade-off 정리 | 완료 |
| 보안노트 | gradient leakage, poisoning, backdoor, malicious client, policy landscape 정리 | 완료 |
| 실험 코드 | synthetic FL logistic regression toy experiment 작성 | 완료 |
| 실행 결과 | Clean FL, poisoned FL 10/20%, robust aggregation 20% 결과 생성 | 완료 |
| 통합보고서 | 실행 로그 기반 16장 최종 초안 작성 | 완료 |
| 제출/발표자료 | Markdown/HTML 제출본과 발표 패키지 수치 대조 | 완료 |

## 주요 수치

| 조건 | Global Accuracy | ASR |
|---|---:|---:|
| Clean FL | 0.960000 | 0.136076 |
| Poisoned FL 20% | 0.950000 | 0.496835 |
| Robust aggregation 20% | 0.955000 | 0.237342 |
