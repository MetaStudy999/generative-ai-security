# 예상 질문과 답변

| 질문 | 답변 | 근거 파일 |
|---|---|---|
| 왜 실제 FL framework를 사용하지 않았나? | 이번 주차의 목적은 공격 재현이 아니라 평가 구조와 로그 재현성을 안전하게 확인하는 것이다. synthetic toy 환경만 사용했다. | `04_experiment/experiment_report.md` |
| ASR이 높은데 accuracy가 유지되는 이유는? | backdoor는 전체 clean test set이 아니라 특정 trigger 조건에서만 목표 오동작을 유도한다. 그래서 clean accuracy와 ASR을 함께 봐야 한다. | `04_experiment/outputs/run_log.md` |
| Coordinate median이면 방어가 끝난 것인가? | 아니다. 20% 조건에서 ASR을 0.496835에서 0.237342로 낮췄지만 완전히 제거하지 못했다. | `03_theory_notes/evaluation_protocol.md` |
| Privacy Leakage Proxy는 실제 공격 성공률인가? | 아니다. update norm과 다양성 기반 대용 지표이며 실제 gradient inversion이나 membership inference를 수행하지 않았다. | `03_theory_notes/open_problems.md` |
| P03/P05 DOI는 확인되었나? | 확인했다. P03은 DOI 10.1016/j.inffus.2022.09.011, P05는 DOI 10.1016/j.engappai.2023.107166을 참고문헌에 반영했다. 발표에서는 최종 제출 전 DOI landing page를 사람이 다시 확인한다고 말한다. | `01_papers/doi_check.md` |
| PDF 원문을 GitHub에 올려도 되는가? | 현재 PDF 5개가 git 추적 중이므로 public 저장소에서는 저작권 위험이 있다. 공개 전 DOI/URL과 요약만 남길지 결정해야 한다. | `01_papers/download_source.md` |

<!-- formula-visual-qna:start -->
## 수식·그래프·그림 보강 Q&A

### Q. 그래프 수치는 어디에서 온 것인가?

A. `04_experiment/outputs/metrics_summary.csv`의 기존 수치만 사용했다. CSV에 없는 값, 실행하지 않은 실험, 외부 논문 실험 수치는 추가하지 않았다.

### Q. 이 수식은 해당 논문의 원문 수식인가?

A. 발표 보강용 수식은 표준 정의식 또는 검증 가능한 평가식이다. 논문별 원문 절·쪽·그림 번호가 필요한 경우 최종 제출 전 사람 검토로 확인한다.

### Q. 다이어그램은 실험 결과인가?

A. 아니다. `FL aggregation structure` 다이어그램은 AI-assisted conceptual diagram이며 threat model과 pipeline 설명을 위한 보조 그림이다.

### Q. 보안적으로 가장 조심해야 할 해석은 무엇인가?

A. privacy_leakage_proxy는 실제 gradient inversion 성공률이 아니며 proxy로만 해석한다. 또한 모든 실습은 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 범위로만 해석한다.
<!-- formula-visual-qna:end -->
