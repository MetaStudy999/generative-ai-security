# W15 예상 Q&A

| 질문 | 답변 | 근거 파일 |
|---|---|---|
| W15 감사 결과가 모델 성능을 의미하나요? | 아닙니다. W15 감사는 로컬 파일, DOI/URL 상태, AI 고지, 제출/발표 패키지 준비 여부를 확인한 것입니다. 모델 accuracy나 F1을 주장하지 않습니다. | `04_experiment/outputs/run_log.md` |
| 왜 P03은 부분 확인으로 남겼나요? | DOI metadata는 `10.1145/3561048`로 확인했지만, 로컬 PDF는 Mersha et al.의 arXiv 대체 survey입니다. 최종 인용 전 지정 논문 원문 PDF를 확보해야 합니다. | `01_papers/doi_check.md`, `02_paper_summaries/P03_summary.md` |
| P05는 왜 추가 확인이 남아 있나요? | arXiv:2312.12936과 최종 DOI `10.1145/3774643`은 확인했지만, ACM 권호/issue와 최종 formatted PDF는 제출 전 사람이 재확인해야 합니다. | `01_papers/doi_check.md` |
| benchmark contamination은 왜 보안 이슈인가요? | 평가셋이 학습·튜닝·프롬프트 설계에 노출되면 성능이 실제 일반화 능력을 반영하지 못하므로 연구 결과의 무결성이 깨집니다. | `03_theory_notes/security_issue_30.md` |
| XAI는 방어 도구인가요? | 설명은 오류와 편향을 찾는 방어 도구가 될 수 있지만, 민감 feature나 모델 우회 단서를 노출할 수 있어 공격면이기도 합니다. | `03_theory_notes/threat_model.md` |
| 기말논문의 최종 contribution은 무엇인가요? | LLM/RAG 기반 AI 시스템의 prompt injection, benchmark contamination, privacy leakage를 생명주기 관점에서 분석하고, 재현성 중심 보안 평가 체크리스트를 제안하는 것입니다. | `08_final_paper_bridge/contribution_candidates.md` |
| 실제 개인정보나 상용 API 공격을 다루나요? | 다루지 않습니다. 공개 문헌, 로컬 산출물, 공개 또는 synthetic toy evaluation 범위로 제한합니다. | `04_experiment/configs/config.yaml` |
| 최종 제출 전에 남은 일은 무엇인가요? | P03 원문 PDF 확보, P05 권호/issue 확인, 국내 문헌 3편 이상 검증, PDF 저작권/보관 정책 검토입니다. | `03_theory_notes/open_problems.md` |
