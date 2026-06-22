# 7. 결론

## 7.1 연구 요약

본 연구는 W01-W15 final 보고서를 생명주기 관점에서 재점검하고, 그중 LLM/RAG 기반 AI 시스템의 보안 위협을 핵심 사례로 삼아 재현성 중심 평가 프레임워크를 제안한다.

## 7.2 연구 기여

1. 본 연구는 LLM/RAG 기반 AI 시스템의 데이터·평가·프롬프트 생명주기에서 prompt injection, benchmark contamination, privacy leakage 위협을 분석하고, 재현성 중심의 보안 평가 체크리스트를 제안한다.
2. 본 연구는 기존 AI 보안 survey가 위협 분류와 실험 재현성의 연결을 충분히 제공하지 못하는 한계를 보완하기 위해 clean performance, attack impact, leakage, reproducibility, human review를 포함한 통합 평가 기준을 제시한다.
3. 본 연구는 W01-W15의 논문별 핵심 수식·알고리즘을 쉬운 설명으로 정리해, ASR, leakage, DP, robust accuracy, fidelity, reproducibility coverage 같은 지표를 같은 기준에서 해석할 수 있게 한다.

## 7.3 한계

본 초안은 문헌분석과 설계 중심이며, 실제 실험 결과는 실행 로그와 CSV/JSON 산출물 대조 후 최종 제출 전 보완해야 한다. DOI/URL 검증도 최종 제출 전 확정한다. 수식 보충표의 대표 수식은 원문 직접 인용이 아니므로, 최종 제출본에서 원문 수식으로 사용할 경우 논문 원문 쪽/절 번호를 추가 확인한다.

## 7.4 후속 연구

후속 연구에서는 실제 공개 데이터 기반 toy RAG 평가를 수행하고, 국내 문헌 검증과 원문 수식 대조를 완료한 뒤 프레임워크의 적용 가능성을 점검한다.
