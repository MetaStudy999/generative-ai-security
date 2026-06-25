# P05 Summary

## A Survey on Deep Learning for Software Engineering — Yanming Yang, Xin Xia, David Lo, John Grundy, ACM Computing Surveys, 2022

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W14 MLOps & AI Supply Chain |
| 논문명 | A Survey on Deep Learning for Software Engineering |
| 저자 | Yanming Yang, Xin Xia, David Lo, John Grundy |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 54, Issue 10s, pp. 1–73, online 2022-09-13, print 2022-01-31 |
| DOI | https://doi.org/10.1145/3505243 |
| 로컬 PDF | `01_papers/pdf/05_Yang_Xia_Lo_Grundy_2022_Deep_Learning_Software_Engineering.pdf` |
| 검증 상태 | W14 `paper_list.md` 기준 공식 DOI 확인. 수업자료의 `Xiang Chen et al., Deep Learning for Software Engineering: A Survey` 표기와 DOI/로컬 PDF 기준 `Yanming Yang, Xin Xia, David Lo, John Grundy` 서지 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P05 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W14 `paper_list.md`의 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W14에서 AI 기반 software engineering, code analysis, testing, defect prediction, program repair, dependency/build pipeline, CI/CD 보안, software supply chain governance를 설명하는 관련 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 deep learning이 software engineering 전 생명주기에 적용되는 방식을 **code representation, code search, code summarization, defect prediction, vulnerability detection, clone detection, program repair, test generation, requirements engineering, software maintenance, developer support, build/CI pipeline, software artifact quality** 관점에서 정리하며, W14에서 MLOps 보안을 **모델 공급망뿐 아니라 코드·dependency·build artifact·test result·CI/CD evidence까지 포함하는 software supply chain security**로 확장하는 관련 핵심 문헌이다.

---

## 2. 핵심 연구문제

> AI 보안 운영에서 모델만 안전하다고 충분하지 않다. 모델을 만드는 코드, 데이터 전처리 스크립트, dependency, test, build artifact, CI/CD 설정, 자동 생성 코드, 코드 분석 도구까지 신뢰할 수 있어야 한다. Deep learning for software engineering은 개발 생산성을 높일 수 있지만, 동시에 insecure code generation, vulnerable patch, test bypass, dependency confusion, build provenance gap 같은 공급망 위험을 만든다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Deep learning은 software engineering 생명주기의 어느 단계, 즉 code analysis, testing, maintenance, repair, requirements, documentation에 적용되는가? |
| RQ2 | AI 기반 code assistant, program repair, defect prediction, vulnerability detection 도구는 어떤 품질·보안 검증을 필요로 하는가? |
| RQ3 | 자동 생성 코드와 자동 수정 patch를 CI/CD pipeline에 반영할 때 test coverage, vulnerability scan, code review, build provenance를 어떻게 남겨야 하는가? |
| RQ4 | Software artifact와 model artifact를 함께 관리하려면 commit hash, dependency lock, build log, tool/model version, approval log가 어떻게 연결되어야 하는가? |
| RQ5 | LLM/RAG 기반 개발 자동화가 MLOps supply chain에 들어올 때 hallucinated dependency, insecure API usage, vulnerable patch risk를 어떻게 통제해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W14 연결 |
|---|---|---|
| DL4SE 영역 정리 | deep learning의 software engineering 적용 분야를 체계적으로 survey | W14 software supply chain 확장 |
| Code representation 강조 | token, AST, graph, sequence, embedding 기반 code modeling을 설명 | AI code assistant 이해 |
| 품질·보안 과제 연결 | defect prediction, vulnerability detection, program repair, testing을 software quality와 연결 | secure CI/CD 평가 |
| 자동화 위험 제시 | 자동 분석·자동 수정을 운영 pipeline에 넣을 때 검증과 책임성이 필요 | approval/evidence chain |
| MLOps와 SE 연결 | 모델 개발 코드와 software artifact를 함께 관리해야 함을 보여줌 | W14/W15 reproducibility 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | Deep learning은 code, bug, test, requirements, maintenance 등 software engineering 문제에 널리 적용된다. | AI가 코드를 읽고, 버그를 찾고, 테스트를 만들고, 수정을 도울 수 있다. |
| 2. Background | 소스코드 표현, sequence model, graph model, neural language model, software artifact 개념을 설명한다. | 코드를 텍스트처럼도 보고 구조화된 그래프처럼도 본다. |
| 3. Code Analysis | code classification, clone detection, code search, code summarization, API recommendation 등을 정리한다. | 비슷한 코드 찾기, 코드 설명 만들기, API 추천 같은 작업이다. |
| 4. Defect/Vulnerability Prediction | bug-prone module과 security vulnerability를 예측하는 DL 기반 접근을 다룬다. | AI가 취약하거나 버그가 있을 가능성이 높은 코드를 찾는다. |
| 5. Program Repair and Maintenance | 자동 patch generation, bug fixing, maintenance support, refactoring 지원을 설명한다. | AI가 코드를 고치거나 유지보수를 도울 수 있다. |
| 6. Testing | test generation, test prioritization, test oracle, coverage prediction을 다룬다. | 어떤 테스트를 만들고 먼저 돌릴지 AI가 도와준다. |
| 7. Requirements and Documentation | 요구사항 분석, traceability, documentation, natural language artifact 처리에 DL을 적용한다. | 요구사항 문서와 코드 사이의 연결을 찾는다. |
| 8. Challenges | 데이터셋 품질, 일반화, explainability, reproducibility, benchmark bias, 실제 개발환경 적용성이 과제로 남는다. | 논문 성능이 높아도 실제 프로젝트에 바로 적용하기 어렵다. |
| 9. Future Directions | trustworthy DL4SE, human-in-the-loop, secure development, tool integration, benchmark standardization이 필요하다. | 개발자를 돕는 AI 도구도 검증·감사·책임성이 필요하다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 DL4SE와 software supply chain security 평가를 W14 보고서에서 설명하기 위한 표준화된 표현이다. 실제 논문의 고유 정량식이라기보다 기말논문 운영 평가표 설계를 위한 지표다.

### 5.1 Secure Software Engineering Score

AI 기반 개발 자동화의 보안 품질을 test 통과율, 취약점 비율, 유지보수 위험으로 요약한다.

$$
SecureSEScore=TestPassRate-\lambda VulnerabilityRate-\mu MaintenanceRisk
$$

| 기호 | 의미 |
|---|---|
| $TestPassRate$ | 자동 생성/수정 코드의 테스트 통과율 |
| $VulnerabilityRate$ | 정적분석·동적분석에서 발견된 취약점 비율 |
| $MaintenanceRisk$ | 복잡도, 중복, 문서 부족, 장기 유지보수 위험 |

### 보안적 의미

테스트를 통과한 코드라도 취약점이 많거나 유지보수성이 낮으면 안전한 artifact로 보기 어렵다.

---

### 5.2 Vulnerability Rate

분석된 코드 중 취약한 artifact의 비율이다.

$$
VulnerabilityRate=\frac{N_{vulnerable\ artifacts}}{N_{analyzed\ artifacts}}
$$

### 보안적 의미

AI code assistant나 자동 patch 도구를 CI/CD에 넣을 때 vulnerability rate를 반드시 기록해야 한다.

---

### 5.3 Test Coverage

코드 중 테스트로 실행·검증된 부분의 비율이다.

$$
TestCoverage=\frac{Lines_{covered}}{Lines_{total}}
$$

### 보안적 의미

coverage가 낮으면 자동 생성 코드의 결함과 취약점이 운영 pipeline으로 들어갈 가능성이 커진다.

---

### 5.4 Build Provenance Completeness

build artifact가 어떤 코드·dependency·도구·환경에서 만들어졌는지 추적 가능한 정도다.

$$
BuildProv=\frac{|Artifacts_{linked}|}{|Artifacts_{required}|}
$$

| 필수 연결 | 설명 |
|---|---|
| commit hash | 소스코드 버전 |
| dependency lock | 라이브러리 버전 |
| build log | 빌드 과정과 결과 |
| test report | 테스트 결과 |
| tool/model version | AI coding tool 또는 분석 모델 버전 |
| approval log | 승인자와 승인 시점 |

### 보안적 의미

build provenance가 부족하면 악성 dependency, vulnerable patch, CI/CD 변조 여부를 추적하기 어렵다.

---

### 5.5 AI Patch Risk

AI가 생성한 patch의 실패·취약성·회귀 위험을 요약한다.

$$
PatchRisk=\alpha TestFailure+\beta VulnerabilityFinding+\gamma RegressionRisk+\delta ReviewFinding
$$

### 보안적 의미

자동 수정 patch는 테스트 통과만으로 승인하지 말고 보안 스캔과 code review 결과를 함께 봐야 한다.

---

### 5.6 Dependency Risk

dependency 관리 실패로 생기는 공급망 위험을 평가한다.

$$
DependencyRisk=OutdatedRate+VulnDependencyRate+UnknownLicenseRate+UnpinnedRate
$$

### 보안적 의미

LLM이 존재하지 않는 패키지명을 제안하거나 취약한 dependency를 추천하면 dependency confusion과 supply-chain risk가 발생할 수 있다.

---

### 5.7 CI/CD Gate Pass Score

CI/CD 통제 단계별 검증 통과 정도를 측정한다.

$$
GatePassScore=\frac{|Gates_{passed}|}{|Gates_{required}|}
$$

| Gate 예 | 설명 |
|---|---|
| unit/integration test | 기능 검증 |
| SAST/DAST/SCA | 취약점 및 dependency 검증 |
| code review | 사람 검토 |
| build provenance | artifact 출처 검증 |
| model/tool version log | AI 도구 버전 기록 |

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W14/P05에서의 의미 |
|---|---|---|
| DL4SE | software engineering 문제에 deep learning 적용 | 관련 문헌 핵심 |
| Code Representation | token, AST, graph, embedding | 코드 분석 모델 입력 |
| Defect Prediction | 버그 가능성 예측 | 품질·보안 위험 탐지 |
| Vulnerability Detection | 취약 코드 식별 | secure pipeline 필요 |
| Program Repair | 자동 patch 생성 | 검증·승인 위험 |
| Test Generation | 테스트 자동 생성 | coverage와 oracle 문제 |
| Code Summarization | 코드 설명 생성 | 유지보수 지원 |
| Human-in-the-loop | 개발자 검토와 승인 | 자동화 과신 방지 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | DL4SE / Software Supply Chain 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | code repository, build log, prompt, proprietary code가 AI 도구로 유출될 수 있음 | access log, prompt redaction |
| 무결성 | 자동 생성 코드, dependency, build artifact가 악성 또는 취약할 수 있음 | SAST/SCA finding, BuildProv |
| 가용성 | 잘못된 patch와 CI/CD 장애가 배포 지연·서비스 장애로 연결 | rollback time, build failure rate |
| 프라이버시 | issue, commit, code comment에 개인정보·비밀정보가 포함될 수 있음 | secret scan, PII scan |
| 안전성 | 취약한 자동 수정과 테스트 부족은 downstream system harm으로 이어짐 | vulnerability rate, coverage |
| 책임성 | AI 도구가 만든 코드와 사람이 승인한 코드의 경계를 기록해야 함 | tool version, approval log |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | source code, dependency, build artifact, test result, CI/CD pipeline, code review log, AI tool/model version, deployment package |
| 공격자/위험 목표 | insecure code generation, vulnerable patch injection, dependency confusion, test bypass, build artifact tampering, secret leakage |
| 공격자/위험 능력 | malicious dependency publish, prompt injection to coding tool, CI/CD config modification, vulnerable API recommendation, test manipulation, insider mistake |
| 위험 경로 | AI code suggestion 또는 자동 patch → test 부족/취약점 스캔 누락 → build artifact 생성 → CI/CD 배포 → production vulnerability 노출 |
| 방어자 능력 | code review, SAST/DAST/SCA, dependency pinning, SBOM, build provenance, signed artifact, approval gate, rollback |
| 제외 범위 | 악성 코드 작성, dependency confusion 실행 방법, CI/CD 침투 절차, 취약점 악용 코드, secret 탈취 방법 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W14/P05 활용 |
|---|---|---|---|
| 코드 품질 | TestPassRate, TestCoverage, complexity | 기본 품질 | software quality |
| 보안성 | VulnerabilityRate, SAST/DAST finding | 취약 코드 비율 | secure SE 핵심 |
| dependency | DependencyRisk, SBOM completeness | 공급망 위험 | SCA/SBOM 연결 |
| 자동 수정 | PatchRisk, regression rate | AI patch 위험 | program repair 평가 |
| build provenance | BuildProv, artifact hash coverage | 빌드 출처 추적 | W15 evidence chain |
| CI/CD 통제 | GatePassScore, approval completeness | 배포 전 검증 | governance |
| 운영 영향 | rollback time, incident count | 배포 후 영향 | MLOps 연결 |
| 서지 정확성 | official DOI match, author/title mismatch flag | 참고문헌 정확성 | reference audit |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI 기준 서지, 수업자료 표기 차이, 로컬 PDF 판본 상태 |
| Code version | commit hash, branch, PR number, diff |
| Dependency | lockfile, SBOM, vulnerable dependency scan result |
| AI tool/model | coding assistant/model version, prompt policy, generated code marker |
| Tests | unit/integration/security test report, coverage, failed tests |
| Security scan | SAST, DAST, SCA, secret scan, license scan 결과 |
| Build | build log, artifact hash, container image digest, provenance attestation |
| Review/approval | reviewer, approval timestamp, exception reason |
| Deployment | release tag, rollout strategy, rollback target |
| 한계 | DL4SE survey의 연구 성능을 실제 secure software engineering 보장으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. Deep learning이 software engineering 전 생명주기에 적용되는 방식을 폭넓게 정리한다.
2. 코드 분석, 결함 예측, 취약점 탐지, 프로그램 수리, 테스트 자동화의 연구 흐름을 제공한다.
3. AI 기반 개발 자동화가 software supply chain에 들어올 때 필요한 검증 기준을 설계할 근거가 된다.
4. W14의 MLOps supply chain 논의를 model artifact에서 code/dependency/build artifact까지 확장한다.
5. W15 최종보고서의 reproducibility table에 commit, dependency, build, test, scan, approval evidence를 포함해야 함을 뒷받침한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 수업자료 표기 차이 | 수업자료의 Xiang Chen 표기와 DOI/로컬 PDF 기준 Yang/Xia/Lo/Grundy 서지가 다르다. | DOI 기준으로 인용하고 차이 메모 유지 |
| 실제 개발환경 일반화 | 논문 benchmark 성능이 실제 repository와 조직 환경에 그대로 적용되지 않을 수 있다. | real CI/CD evidence 기준으로 보완 |
| 자동화 과신 | AI가 만든 patch가 테스트는 통과해도 취약할 수 있다. | SAST/SCA/code review 필수화 |
| dependency hallucination | LLM이 존재하지 않거나 취약한 라이브러리를 추천할 수 있다. | dependency allowlist와 lockfile 검증 |
| 책임소재 | AI 도구가 작성한 코드와 사람 승인 코드의 경계가 불명확할 수 있다. | generated-code marker와 approval log 기록 |
| 보안평가 부족 | DL4SE 연구가 기능 성능 중심으로 치우치면 보안성 평가가 부족하다. | vulnerability rate와 build provenance 추가 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안 운영은 모델뿐 아니라 code, dependency, build artifact, CI/CD pipeline까지 포함해야 한다는 문제의식 |
| 2장 관련연구 | P05를 DL4SE와 software supply chain 관련 문헌으로 정리하고 수업자료 표기 차이는 검증표에 기록 |
| 3장 위협모형 | source code, dependency, build artifact, test result, AI coding tool version, approval log 보호 자산 정의 |
| 4장 연구방법 | SecureSEScore, VulnerabilityRate, TestCoverage, BuildProv, PatchRisk, DependencyRisk, GatePassScore 지표 설계 |
| 5장 분석 | AI-assisted software supply chain control matrix와 CI/CD evidence chain table 제시 |
| 6장 보안적 함의 | LLM 기반 개발 자동화, dependency risk, AI patch 검증, build provenance, human approval 필요성 해석 |

---

## 14. 기말논문 연결 3문장

1. W14에서 기말논문에 반영할 개념: Deep learning for software engineering은 code analysis와 자동화된 개발 지원을 가능하게 하지만, AI가 생성·수정한 코드가 CI/CD에 들어갈 때 보안 검증과 provenance가 필수다.
2. W14에서 기말논문에 반영할 표·그림·실험: SecureSEScore, VulnerabilityRate, TestCoverage, BuildProv, PatchRisk, DependencyRisk, GatePassScore 수식표와 AI-assisted CI/CD security gate diagram을 반영한다.
3. W14가 W15 최종 논문과 연결되는 지점: W15 최종보고서에서는 model hash뿐 아니라 commit hash, dependency lock, build log, test report, vulnerability scan, AI tool version, approval log를 함께 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P05는 W14에서 MLOps supply chain을 software engineering supply chain으로 확장하는 관련 핵심 문헌이다. 모델이 안전하려면 모델을 만드는 코드, dependency, build artifact, CI/CD gate, test report, vulnerability scan까지 안전해야 한다. 따라서 기말논문에서는 P05를 **AI-assisted software engineering, secure CI/CD, dependency/build provenance, AI patch 검증, LLM 기반 개발 자동화 위험 통제의 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
