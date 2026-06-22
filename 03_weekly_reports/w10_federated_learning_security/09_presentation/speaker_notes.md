# 발표자 노트

| 슬라이드 | 시간 | 발화 요지 |
|---:|---:|---|
| 1 | 0:40 | 오늘의 핵심은 FL이 privacy-preserving처럼 보이지만 보안 평가가 별도로 필요하다는 점이다. |
| 2 | 1:00 | client, server, aggregation 구조를 설명하고 FedAvg가 가장 기본 기준임을 말한다. |
| 3 | 1:10 | 보호 자산을 local update, global model, aggregation result, training log로 나눈다. |
| 4 | 1:00 | 다섯 논문이 각각 원리, 보안 taxonomy, privacy/policy, backdoor 평가를 담당한다고 연결한다. |
| 5 | 1:10 | 실제 공격이 아니라 synthetic toy 실험임을 먼저 밝힌다. |
| 6 | 1:40 | 20% poisoned FedAvg의 ASR 0.496835와 robust aggregation ASR 0.237342를 비교한다. |
| 7 | 1:00 | clean accuracy만 보면 위험을 놓친다는 메시지를 강조한다. |
| 8 | 0:50 | 기말논문의 평가표와 연결한다. |
| 9 | 0:40 | FL 보안은 update, aggregation, ASR, 로그 재현성을 함께 봐야 한다고 마무리한다. |

## 발표 주의

- Privacy Leakage Proxy는 실제 gradient inversion 성공률이 아니라고 명확히 말한다.
- 모든 수치는 `04_experiment/outputs/run_log.md` 기준이라고 밝힌다.
- P03/P05 출판 DOI는 확인했지만, 최종 제출 전 DOI landing page를 사람이 다시 확인한다고 말한다.
- P01은 수업자료의 ACM Computing Surveys 표기와 공식 TIST DOI 메타데이터 차이가 있음을 짧게 언급한다.
