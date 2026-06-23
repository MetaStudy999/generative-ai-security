# 예상 질문과 답변

## Q1. Accuracy가 0.925000이면 공급망 보안도 충분하다고 볼 수 있나요?

아닙니다. Accuracy는 정상 조건 기준 성능입니다. 공급망 보안은 데이터 provenance, model artifact 무결성, config/seed 재현성, 로그 감사 가능성, drift monitoring을 별도로 봐야 합니다.

## Q2. Drift score 0.307626은 공격이 발생했다는 뜻인가요?

아닙니다. Drift score는 입력 분포 변화의 크기를 보여주는 경보 지표입니다. 공격인지, 계절성인지, 사용자 집단 변화인지 판단하려면 incident analysis와 human review가 필요합니다.

## Q3. Audit coverage 1.000000은 실제 감사가 완전하다는 뜻인가요?

아닙니다. W14 toy audit record에서 필수 필드 10개가 채워졌다는 뜻입니다. 로그의 진실성, 위변조 방지, 접근통제, immutable storage는 별도 운영 통제로 검증해야 합니다.

## Q4. Inventory coverage 1.000000은 완전한 AI BOM인가요?

아닙니다. Dataset, model artifact, config, run log 같은 최소 항목의 name/type 충족률입니다. 실제 AI BOM으로 확장하려면 SBOM, license, vulnerability scan, model registry ACL, approval record가 필요합니다.

## Q5. 왜 P03/P04/P05는 확인 필요로 남겼나요?

수업자료의 대상 논문 DOI와 로컬 PDF 파일명이 다릅니다. 그래서 보고서에서는 DOI를 수업자료 기준으로 기록하되, 로컬 PDF는 대체문헌임을 명시했습니다. 최종 학술 논문에서는 공식 원문 PDF를 확보해야 합니다.

## Q6. Toy pipeline이 실제 MLOps 보안성을 증명하나요?

아닙니다. 이번 실습은 실제 운영 보안성 증명이 아니라 evidence 구조의 최소 구현입니다. 실제 환경에서는 registry, CI/CD, 접근통제, SBOM, vulnerability scan, production monitoring이 추가되어야 합니다.

## Q7. AI BOM 또는 ML artifact inventory에는 무엇을 넣어야 하나요?

최소한 dataset, model artifact, config, run log가 들어가야 합니다. 운영환경에서는 code commit, container image digest, dependency lockfile, model card, data card, approval record까지 확장하는 것이 좋습니다.

<!-- formula-visual-qna:start -->
## 수식·그래프·그림 보강 Q&A

### Q. 그래프 수치는 어디에서 온 것인가?

A. `04_experiment/outputs/metrics_summary.csv`의 기존 수치만 사용했다. CSV에 없는 값, 실행하지 않은 실험, 외부 논문 실험 수치는 추가하지 않았다.

### Q. 이 수식은 해당 논문의 원문 수식인가?

A. 발표 보강용 수식은 표준 정의식 또는 검증 가능한 평가식이다. 논문별 원문 절·쪽·그림 번호가 필요한 경우 최종 제출 전 사람 검토로 확인한다.

### Q. 다이어그램은 실험 결과인가?

A. 아니다. `MLOps supply-chain map` 다이어그램은 AI-assisted conceptual diagram이며 threat model과 pipeline 설명을 위한 보조 그림이다.

### Q. 보안적으로 가장 조심해야 할 해석은 무엇인가?

A. hash/pass 항목은 시각화에서 제외했으며 원본 CSV와 artifact inventory를 함께 확인해야 한다. 또한 모든 실습은 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 범위로만 해석한다.
<!-- formula-visual-qna:end -->
