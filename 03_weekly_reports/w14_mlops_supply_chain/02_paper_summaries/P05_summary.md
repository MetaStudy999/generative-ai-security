# P05 Summary

## A Survey on Deep Learning for Software Engineering — Yanming Yang, Xin Xia, David Lo, John Grundy, ACM Computing Surveys, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W14 MLOps & AI Supply Chain |
| 논문명 | A Survey on Deep Learning for Software Engineering |
| DOI | https://doi.org/10.1145/3505243 |
| 검증 상태 | W14 `paper_list.md` 기준 공식 DOI 확인. 수업자료 Xiang Chen 표기와 DOI/로컬 PDF 기준 Yang/Xia/Lo/Grundy 서지 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 deep learning이 software engineering에 적용되는 영역을 **code analysis, defect prediction, program repair, testing, requirements, software maintenance** 관점에서 정리하며, W14에서 AI 기반 개발·운영 도구의 공급망 보안과 품질 검증을 연결한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | DL은 소프트웨어 개발 생명주기의 어느 단계에 적용되는가? |
| RQ2 | AI code assistant와 자동화 도구는 어떤 보안·품질 리스크를 만드는가? |
| RQ3 | 생성 코드와 분석 결과를 운영 pipeline에 넣을 때 어떤 검증이 필요한가? |

---

## 3. 핵심 지표

$$
SecureSEScore = TestPassRate - \lambda VulnerabilityRate - \mu MaintenanceRisk
$$

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | source code, dependency, build artifact, test result, CI/CD pipeline |
| 공격자/위험 | insecure code generation, dependency confusion, test bypass, vulnerable patch |
| 지표 | test pass rate, vulnerability rate, code review finding, build provenance |
| 재현성 | commit hash, dependency lock, build log, model/tool version 기록 |

---

## 5. 기말논문 연결

P05는 AI 보안 운영을 software supply chain과 연결한다. W14에서는 모델뿐 아니라 코드, dependency, build artifact, 배포 로그까지 감사 대상으로 본다.

---

## 6. 최종 판단

P05는 W14의 software engineering supply chain 관련 문헌이다. LLM 기반 개발 자동화와 MLOps 보안을 연결하는 근거로 사용한다.
