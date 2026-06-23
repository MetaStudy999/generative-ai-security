# 평가방법

| 평가 항목 | 지표 | 측정 방법 | 필요한 데이터 | 비고 |
|---|---|---|---|---|
| Evaluation Reliability | Reliability score | 벤치마크 중복·오염·대체 PDF 여부 확인 | Benchmark metadata, paper list | 평가 신뢰성 |
| Reproducibility | Evidence coverage | Dockerfile, config, seed, outputs, run_log 존재 확인 | Config/logs/results | 재현성 |
| Reference Validity | Verification rate | DOI/URL/출판사/로컬 PDF 일치 여부 점검 | Reference list, doi_check.md | 연구윤리 |
| AI Disclosure Quality | Disclosure completeness | AI 활용 고지 항목 충족률 확인 | AI worklog, disclosure draft | 투명성 |
| Explanation Reliability | Explanation stability | 입력 변화 전후 설명 변화, fidelity, completeness 비교 | XAI outputs | 설명 신뢰성 |
| Contribution Clarity | Contribution score | 기여문장 1-2개로 압축 가능 여부 검토 | Paper draft, contribution.md | 논문 완성도 |
| Limitation Clarity | Limitation coverage | 대체 PDF, 미검증 DOI, 실행 전 결과, 제외 범위 명시 여부 | Paper draft, self review | 연구 신뢰성 |

## 실행 전제

실험 수치는 실제 실행 로그가 있을 때만 확정한다. W15의 실행 단위는 모델 성능 벤치마크가 아니라 제출 준비 감사이며, 결과는 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`이 생성된 뒤 해당 값만 사용한다.

## 보고서 반영 규칙

- 제출본과 발표본의 수치는 outputs와 일치해야 한다.
- DOI가 확인되지 않은 항목은 `확인 필요` 또는 `부분 확인`으로 유지한다.
- 대체 PDF는 최종 참고문헌처럼 표현하지 않는다.
- AI 활용 고지와 human review를 누락하지 않는다.
- P03처럼 DOI metadata가 확인되어도 로컬 PDF가 지정 논문과 다르면 `부분 확인`으로 남기고, 본문 인용번호에는 원문 확인 필요를 함께 쓴다.
- P05처럼 arXiv와 최종 DOI가 연결된 경우에도 권호/issue와 최종 formatted PDF는 제출 전 사람이 재확인한다.
