# W14 100점형 통합 Summary

## MLOps & AI Supply Chain

## 0. 문서 목적

이 문서는 W14 개별 논문 summary 5개를 기말논문 작성용 연구 노트로 통합한 100점형 요약본이다. MLOps, AIOps, ML deployment, edge AI, software engineering supply chain을 하나의 운영 보안 평가체계로 묶는다.

---

## 1. 한 문장 통합 요약

W14는 AI 보안을 **데이터·모델·코드·배포·모니터링·로그·승인·롤백**으로 이어지는 운영 생명주기 문제로 보고, 실험 성능보다 audit coverage, deployment risk, drift, incident response, build/model provenance가 중요함을 정리하는 주차다.

---

## 2. 문헌 5편 통합 매트릭스

| ID | 논문 | 핵심 역할 | 주요 지표 |
|---|---|---|---|
| P01 | MLOps Practices Review | MLOps 생명주기·거버넌스 | audit coverage, reproducibility |
| P02 | ML Deployment Challenges | 배포 실패·운영 문제 | drift, MTTR, rollback |
| P03 | MLOps/AIOps Survey | 관제·incident 자동화 | alert precision, recovery readiness |
| P04 | Edge DL Review | edge/cloud 배포 보안 | latency, update integrity |
| P05 | DL for SE Survey | software supply chain 연결 | vulnerability rate, build provenance |

---

## 3. 핵심 수식 묶음

$$
Coverage_{audit}=\frac{|Controls_{logged}|}{|Controls_{required}|}
$$

$$
DeploymentRisk = DriftRisk + DataQualityRisk + InfraRisk + MonitoringGap
$$

$$
MTTR = t_{restore}-t_{incident}
$$

$$
SecureSEScore = TestPassRate - \lambda VulnerabilityRate - \mu MaintenanceRisk
$$

---

## 4. 통합 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | dataset, feature pipeline, model artifact, registry, source code, dependency, deployment config, monitoring log |
| 공격자/위험 | data poisoning, dependency confusion, model tampering, misconfiguration, monitoring blind spot, log tampering |
| 방어자 능력 | data/version control, model registry, CI/CD gate, SBOM, approval, monitoring, rollback, incident response |
| 제외 범위 | 실제 운영 시스템 무단 변경, 공급망 공격 재현, 악성코드 실행 |

---

## 5. 통합 평가 지표

| 평가축 | 대표 지표 | 해석 |
|---|---|---|
| Governance | audit coverage, approval completeness | 통제 준수 |
| Deployment | drift score, data quality error, MTTR | 운영 안정성 |
| Monitoring | alert precision/recall, false alarm rate | 관제 품질 |
| Edge Security | update hash, device attestation, latency | edge 배포 안전성 |
| Software Supply Chain | dependency lock, build provenance, vulnerability rate | 코드/빌드 보안 |
| Reproducibility | commit, data version, model version, environment | 재현성과 책임성 |

---

## 6. 기말논문 연결 3문장

1. W14에서 기말논문에 반영할 개념: AI 보안은 모델 성능 평가로 끝나지 않고 데이터·모델·코드·배포·모니터링·감사 로그까지 포함하는 운영 통제 문제다.
2. 반영할 표·그림·실험: MLOps lifecycle, audit coverage, deployment risk, MTTR, build/model provenance 체크리스트를 반영한다.
3. W15 연결: 최종 종합평가에서는 W01~W13의 공격·방어 지표를 W14의 운영 감사 체계로 통합한다.

---

## 7. 최종 판단

W14는 전체 과정을 실제 서비스·연구 산출물·기말논문으로 묶는 핵심 주차다. RAG/LLM 보안 프레임워크는 반드시 MLOps 감사, 승인, 모니터링, 롤백 구조를 포함해야 한다.
