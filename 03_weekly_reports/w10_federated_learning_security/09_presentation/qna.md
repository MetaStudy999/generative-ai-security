# 예상 질문과 답변

| 질문 | 답변 | 근거 파일 |
|---|---|---|
| 왜 실제 FL framework를 사용하지 않았나? | 이번 주차의 목적은 공격 재현이 아니라 평가 구조와 로그 재현성을 안전하게 확인하는 것이다. synthetic toy 환경만 사용했다. | `04_experiment/experiment_report.md` |
| ASR이 높은데 accuracy가 유지되는 이유는? | backdoor는 전체 clean test set이 아니라 특정 trigger 조건에서만 목표 오동작을 유도한다. 그래서 clean accuracy와 ASR을 함께 봐야 한다. | `04_experiment/outputs/run_log.md` |
| Coordinate median이면 방어가 끝난 것인가? | 아니다. 20% 조건에서 ASR을 0.496835에서 0.237342로 낮췄지만 완전히 제거하지 못했다. | `03_theory_notes/evaluation_protocol.md` |
| Privacy Leakage Proxy는 실제 공격 성공률인가? | 아니다. update norm과 다양성 기반 대용 지표이며 실제 gradient inversion이나 membership inference를 수행하지 않았다. | `03_theory_notes/open_problems.md` |
| P03/P05 DOI는 왜 확인 필요인가? | 로컬 PDF가 arXiv/preprint 표기를 포함하므로 출판본 DOI와 페이지 정보는 최종 제출 전 다시 대조해야 한다. | `01_papers/doi_check.md` |
