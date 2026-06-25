# P05 Summary

## When Software Security Meets Large Language Models: A Survey — Xiaogang Zhu, Wei Zhou, Qing-Long Han, Wanlun Ma, Sheng Wen, Yang Xiang, IEEE/CAA Journal of Automatica Sinica, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W07 LLM 보안·프라이버시 |
| 논문명 | When Software Security Meets Large Language Models: A Survey |
| 저자 | Xiaogang Zhu, Wei Zhou, Qing-Long Han, Wanlun Ma, Sheng Wen, Yang Xiang |
| 공식 출판 정보 | IEEE/CAA Journal of Automatica Sinica, Vol. 12, No. 2, pp. 317–334, 2025 |
| DOI | https://doi.org/10.1109/JAS.2024.124971 |
| 로컬 PDF | `01_papers/pdf/05_Zhu_et_al_2025_Software_Security_Meets_LLMs.pdf` |
| 검증 상태 | W07 `paper_list.md`와 `download_source.md` 기준 공식 DOI 확인. 강의계획서에는 `Shujun Li et al.`로 표기되어 있으나, repo의 공식 확인 정보는 `Xiaogang Zhu et al.`임 |
| PDF 확인 메모 | repo의 PDF 폴더에 P05 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W07 `paper_list.md`, `download_source.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고, 긴 영문 subscript 대신 짧은 변수명과 표 설명을 사용했다. |
| 핵심 근거 사용 가능 여부 | 가능. LLM과 소프트웨어 보안의 접점, secure code generation, vulnerability detection, program repair, security testing, secret leakage, tool governance, CI/CD evidence chain을 설명하는 W07 응용 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 LLM과 소프트웨어 보안의 접점을 **취약점 탐지, 안전한 코드 생성, 프로그램 복구, 보안 테스트, fuzzing 보조, 악성코드 분석, 보안 로그 분석, 소프트웨어 공급망, 코드 프라이버시, secret leakage, tool integration, human review, CI/CD 검증** 관점에서 정리하며, W07에서는 LLM을 보안 자동화 도구로 사용할 때도 **출력 검증·정적분석·테스트·비밀정보 보호·도구 권한 통제·감사 로그**가 필수임을 보여주는 survey 문헌이다.

---

## 2. 핵심 연구문제

> LLM은 소프트웨어 보안 업무를 보조할 수 있지만, 생성 코드가 취약하거나 내부 코드와 비밀정보가 외부 LLM에 노출될 수 있다. 따라서 LLM 기반 소프트웨어 보안은 “자동화 효율”이 아니라 “검증 가능한 보안 자동화”로 설계해야 한다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | LLM은 취약점 탐지, 코드 리뷰, 프로그램 복구, 테스트 생성, 보안 로그 분석에 어떤 방식으로 사용될 수 있는가? |
| RQ2 | LLM이 생성한 코드에는 어떤 취약 패턴, dependency risk, 불완전 패치, 검증 누락 문제가 남을 수 있는가? |
| RQ3 | 소스코드, 비밀키, 내부 로그, 취약점 리포트를 LLM에 입력할 때 어떤 privacy, IP, secret leakage 위험이 발생하는가? |
| RQ4 | LLM 기반 보안 도구의 출력은 어떤 테스트, 정적분석, secret scan, dependency scan, human review, audit log로 검증해야 하는가? |
| RQ5 | 기말논문에서 LLM 보안 활용을 안전한 범위로 제한하려면 어떤 제외 범위, 윤리적 한계, evidence chain이 필요한가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W07 연결 |
|---|---|---|
| LLM for software security 정리 | 취약점 탐지, 코드 생성, 패치, 테스트, 로그 분석 등 응용 영역 정리 | LLM의 긍정적 보안 활용 |
| 보안 코드 생성 위험 | 생성 코드가 기능적으로 맞아도 취약하거나 부정확할 수 있음을 강조 | secure code score 설계 |
| 취약점 탐지 평가 관점 | precision, recall, false positive, false negative를 함께 봐야 함 | 실험 지표 설계 |
| 코드 프라이버시 문제 | 내부 코드·비밀값·로그 입력 위험 제기 | secret leakage 평가 |
| 악용 가능성 논의 | LLM이 공격 자동화나 부적절한 보안 조언에 악용될 가능성 인식 | dual-use 제한 문구 필요 |
| 운영 검증 필요 | 자동 출력은 테스트·검토·감사와 함께 써야 함 | W14 MLOps/CI-CD 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | LLM은 소프트웨어 보안 작업을 자동화할 가능성이 있지만, 신뢰성과 안전성 검증이 필요하다. | AI가 코드를 도와도 그대로 믿으면 위험하다. |
| 2. Background | LLM, code model, software security, vulnerability, testing, repair의 기본 개념을 설명한다. | AI 코드 도구와 보안 업무의 접점을 이해한다. |
| 3. Vulnerability Detection | LLM을 이용해 취약 코드 후보를 찾고 설명하는 연구를 정리한다. | 코드에서 위험한 부분을 찾는 보조 도구다. |
| 4. Secure Code Generation | 보안 요구사항을 반영한 코드 생성과 취약 코드 생성 위험을 다룬다. | AI가 만든 코드도 보안 검사해야 한다. |
| 5. Program Repair | 취약점 패치와 자동 수정 가능성을 정리한다. | AI가 수정안을 제시해도 테스트와 리뷰가 필요하다. |
| 6. Testing and Fuzzing | 테스트 케이스 생성, 보안 테스트 보조, coverage 개선 가능성을 설명한다. | 테스트를 늘리는 데 도움될 수 있다. |
| 7. Malware and Threat Analysis | 악성코드 분석, 로그 요약, 위협 인텔리전스 보조 가능성을 논의한다. | 분석 보조는 가능하지만 악용 제한이 필요하다. |
| 8. Risks and Challenges | hallucination, insecure code, secret leakage, dependency risk, malicious use, evaluation 한계를 정리한다. | 자동화가 위험을 새로 만들 수 있다. |
| 9. Governance | human review, tool approval, audit log, CI/CD 검증, safe logging이 필요하다. | AI 결과를 검토하고 기록해야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 논문의 응용 영역을 W07 보고서의 평가 체계로 정리하기 위한 표준화된 표현이다. 악성 절차를 제공하지 않고, 방어적 평가와 안전한 사용 범위에 한정한다. GitHub 호환성을 위해 `\operatorname`은 사용하지 않는다.

### 5.1 안전한 코드 생성 점수

LLM 기반 코드 생성은 기능 통과율만으로 평가하면 부족하다. 취약 패턴, 정보누출, dependency 위험을 함께 반영한다.

$$
SecureCodeScore=TestPassRate-\lambda_1VulnRate-\lambda_2LeakageRate-\lambda_3DepRisk
$$

| 기호 | 의미 |
|---|---|
| $TestPassRate$ | 기능 테스트 통과율 |
| $VulnRate$ | 생성 코드 또는 패치에서 발견된 취약 패턴 비율 |
| $LeakageRate$ | 코드, secret, 내부정보 노출 위험 |
| $DepRisk$ | dependency 또는 supply-chain 위험 |
| $\lambda_i$ | 위험 항목 가중치 |

### 보안적 의미

테스트를 통과한 코드도 안전하지 않을 수 있다. 보안 요구사항, 정적분석, secret scanning, dependency 검증, human review가 필요하다.

---

### 5.2 취약점 탐지 성능

LLM 기반 취약점 탐지는 탐지율과 오탐률을 함께 봐야 한다.

$$
Precision=\frac{TP}{TP+FP}
$$

$$
Recall=\frac{TP}{TP+FN}
$$

$$
F1=\frac{2\cdot Precision\cdot Recall}{Precision+Recall}
$$

| 기호 | 의미 |
|---|---|
| $TP$ | 실제 취약 코드를 취약으로 탐지 |
| $FP$ | 정상 코드를 취약으로 오탐 |
| $FN$ | 취약 코드를 놓침 |

### 보안적 의미

오탐이 많으면 개발자가 경고를 무시하게 되고, 미탐이 많으면 취약 코드가 배포된다. 따라서 LLM의 설명 품질뿐 아니라 실제 탐지 지표가 필요하다.

---

### 5.3 Secret Leakage Rate

코드·로그·설정파일에서 secret이 LLM 입력 또는 출력에 노출되는 비율을 측정한다.

$$
SecretLeakage=\frac{N_{sl}}{N_{cp}}
$$

| 기호 | 의미 |
|---|---|
| $N_{cp}$ | 코드·로그 관련 privacy-risk 평가 입력 수 |
| $N_{sl}$ | secret, token, key, credential 등이 노출된 사례 수 |

### 보안적 의미

보안 분석을 위해 LLM에 코드를 넣는 순간 내부 IP, 비밀키, 취약점 정보가 외부로 전달될 수 있다. W14 MLOps에서는 입력 전 secret scanning과 승인 절차가 필요하다.

---

### 5.4 Secure Fix Rate

LLM이 제안한 패치가 취약점을 실제로 줄이고 테스트를 통과한 비율이다.

$$
SecureFixRate=\frac{N_{fixed}}{N_{vuln}}
$$

| 기호 | 의미 |
|---|---|
| $N_{vuln}$ | 취약점이 포함된 평가 사례 수 |
| $N_{fixed}$ | 취약점이 제거되고 기본 테스트를 통과한 사례 수 |

### 보안적 의미

패치가 그럴듯해 보여도 취약점이 남거나 기능 회귀를 만들 수 있다. 보안 패치는 테스트와 전문가 검토를 통과해야 한다.

---

### 5.5 Regression Rate

패치 이후 기존 기능이 깨진 비율이다.

$$
RegressionRate=\frac{N_{reg}}{N_{test}}
$$

| 기호 | 의미 |
|---|---|
| $N_{test}$ | 기존 기능 테스트 수 |
| $N_{reg}$ | 패치 후 실패한 기존 기능 테스트 수 |

### 보안적 의미

보안 패치가 기존 기능을 깨뜨리면 운영 배포가 어렵다. Secure fix는 취약점 제거와 기능 유지가 동시에 필요하다.

---

### 5.6 Tool Execution Risk

LLM이 SAST, DAST, package manager, CI/CD 등 외부 도구를 호출할 때의 위험을 평가한다.

$$
ToolRisk=PrivilegeRisk+ExecutionRisk+DataRisk-ApprovalCoverage
$$

### 보안적 의미

LLM이 자동으로 도구를 실행하면 권한 오남용, 잘못된 수정, 민감 로그 노출, 공급망 위험이 발생할 수 있다. 도구 호출에는 승인 게이트와 감사 로그가 필요하다.

---

### 5.7 Build Evidence Coverage

CI/CD와 보안 검증 재현에 필요한 산출물이 얼마나 남았는지 측정한다.

$$
BuildEvidenceCoverage=\frac{|Artifacts_{logged}|}{|Artifacts_{required}|}
$$

| 필수 artifact 예 | 설명 |
|---|---|
| commit | 코드 변경 commit hash |
| lockfile | dependency lock 또는 SBOM |
| test log | unit/security test 결과 |
| scan report | SAST, secret scan, dependency scan 결과 |
| review note | human review와 승인 기록 |

---

## 6. LLM-소프트웨어 보안 응용 축

| 응용 축 | 긍정적 활용 | 위험 | 대표 지표 |
|---|---|---|---|
| 취약점 탐지 | 코드 취약 패턴 설명·탐지 보조 | 오탐·미탐, hallucinated vulnerability | precision, recall, F1 |
| 안전한 코드 생성 | 보안 요구사항 반영 코드 생성 | 취약 코드 생성, dependency 위험 | VulnRate, TestPassRate |
| 프로그램 복구 | 취약 패치 초안 생성 | 불완전 패치, 기능 회귀 | SecureFixRate, RegressionRate |
| 테스트 생성 | fuzz/test case 보조 | coverage 과장, 실제 결함 미탐 | coverage, defect detection |
| 보안 로그 분석 | 로그 요약·원인 후보 제시 | 민감정보 노출, 잘못된 원인 추론 | SecretLeakage, human agreement |
| 도구 호출 | SAST/DAST/CI 도구 연동 | 권한 오남용, 무검증 자동 실행 | approval rate, audit log |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | LLM+software security 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 내부 코드, secret, 빌드 로그, 취약점 리포트가 LLM 입력·출력·로그에 노출 가능 | SecretLeakage, log leakage |
| 무결성 | LLM이 취약 코드, 불완전 패치, 잘못된 보안 조언을 생성할 수 있음 | VulnRate, SecureFixRate |
| 가용성 | 오탐·과차단·잘못된 자동 패치가 개발 파이프라인을 지연시킬 수 있음 | FPR, RegressionRate |
| 프라이버시/IP | 소스코드와 내부 설계가 외부 LLM에 전달될 수 있음 | data exposure check |
| 공급망 보안 | dependency 제안, package install, CI/CD 자동화가 공급망 위험을 만들 수 있음 | DepRisk, SBOM coverage |
| 책임성 | LLM 제안과 실제 commit, test, scan, review가 연결되어야 함 | BuildEvidenceCoverage |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 소스코드, 비밀키, API token, 취약점 리포트, 빌드 로그, CI/CD 설정, dependency lock, 보안 정책 |
| 공격자 목표 | 취약 코드 생성 유도, 보안정책 우회, 내부 코드·비밀정보 추출, 잘못된 패치 배포 유도, tool 권한 오용 |
| 공격자 능력 | prompt 조작, insecure requirement 삽입, 반복 질의, 코드 context 제공, tool 권한 오용 유도, dependency 조작 |
| 공격 경로 | code prompt → LLM suggestion → tool execution/commit → build/test/scan → deployment artifact |
| 방어자 능력 | secret scanning, static analysis, unit/security test, dependency scan, human code review, tool approval gate, audit logging |
| 제외 범위 | 악성코드 작성, 실제 취약점 악용, 무단 시스템 공격, 실제 비밀키 입력, 공격 자동화 절차 제공 |

---

## 9. 평가방법 및 지표

| 지표 | 의미 | W07/P05 활용 |
|---|---|---|
| TestPassRate | 기능 테스트 통과율 | code utility |
| VulnRate | 생성 코드의 취약 패턴 비율 | secure code 평가 |
| SecureFixRate | 보안 패치가 취약점을 실제로 줄인 비율 | repair 평가 |
| RegressionRate | 패치 후 기존 기능 실패율 | 안정성 평가 |
| SecretLeakage | 코드·로그 내 secret 노출률 | privacy 평가 |
| FPR | 정상 코드를 취약으로 오탐한 비율 | 개발자 피로도 |
| FNR | 취약 코드를 놓친 비율 | 보안 실패 위험 |
| HumanReviewAgreement | 보안 전문가 검토와 일치도 | 책임성 평가 |
| BuildEvidenceCoverage | commit, dependency, build log, scan report 보존 정도 | W14 supply chain 연결 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, IEEE/CAA Journal of Automatica Sinica 출판정보, 강의계획서 표기 차이, 로컬 PDF 상태 |
| Code input | synthetic/open-source snippet 사용 여부, 실제 내부 코드 제외 여부 |
| Model | LLM 모델명, 버전, temperature, prompt template |
| Security tools | SAST, secret scan, dependency scan, test framework 버전 |
| Evaluation | TestPassRate, VulnRate, SecureFixRate, RegressionRate, SecretLeakage, human review 결과 |
| CI/CD | commit hash, dependency lock, build log, artifact hash, scan report |
| Tool permission | LLM이 실행 가능한 tool 목록과 승인 여부 |
| Evidence | raw prompt/output, patch diff, scan report, test result, review note |
| Limitation | toy 코드 결과를 실제 제품 보안성으로 일반화하지 않음 |
| GitHub math | `\operatorname` 사용 금지, 긴 영문 subscript 대신 짧은 변수명과 표 설명 사용 |

---

## 11. 논문의 고유 기여

1. LLM과 소프트웨어 보안의 접점을 체계적으로 정리한다.
2. 보안 자동화의 장점과 위험을 동시에 평가해야 한다는 기준을 제공한다.
3. 코드·로그·취약점 리포트가 LLM 입력으로 들어갈 때의 privacy/IP/secret leakage 위험을 드러낸다.
4. W14의 software supply chain과 W15의 evidence chain으로 이어지는 운영 검증 기준을 제공한다.
5. 기말논문에서 LLM 보안 활용을 “자동화”가 아니라 “검증 가능한 보조 도구”로 제한하는 근거가 된다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 빠른 도구 변화 | LLM code/security 도구는 빠르게 변한다. | 모델/도구 버전 기록 |
| 실제 코드 사용 위험 | 내부 코드와 secret을 외부 LLM에 입력하면 위험하다. | synthetic/open-source toy code로 제한 |
| 자동화 과신 위험 | LLM 출력은 그럴듯하지만 틀릴 수 있다. | human review와 test를 필수화 |
| 악용 위험 | 공격 자동화나 악성코드 생성으로 오해될 수 있다. | 방어·검증 중심으로 제한 |
| benchmark 부족 | 코드 보안 평가는 언어·취약점 유형·도구별 차이가 크다. | 자체 평가 범위와 한계 명시 |
| 공급망 위험 | dependency 추천과 tool execution이 supply-chain risk를 만들 수 있다. | dependency scan, SBOM, approval gate 추가 |
| 강의계획서 표기 차이 | 강의계획서의 `Shujun Li et al.` 표기와 공식 저자 목록이 다르다. | DOI 기준 인용, 차이 메모 유지 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | LLM 보안 자동화는 코드 생성·탐지·패치·테스트를 돕지만 검증 없이는 위험하다는 문제의식 |
| 2장 관련연구 | LLM과 소프트웨어 보안 접점 survey로 P05 정리 |
| 3장 위협모형 | 소스코드, secret, build log, dependency, tool permission, CI/CD artifact 보호 자산 정의 |
| 4장 연구방법 | SecureCodeScore, Precision/Recall/F1, SecretLeakage, SecureFixRate, RegressionRate, ToolRisk, BuildEvidenceCoverage 지표 설계 |
| 5장 분석 | LLM software security application matrix와 evidence table 제시 |
| 6장 보안적 함의 | 검증 없는 자동화, secret leakage, dependency risk, human review, tool approval gate 필요성 해석 |
| 부록 | synthetic code snippet, prompt template, test log, scan report, patch diff, review note 수록 |

---

## 14. 기말논문 연결 3문장

1. W07에서 기말논문에 반영할 개념: LLM은 소프트웨어 보안 업무를 돕는 도구가 될 수 있지만, 생성 코드와 패치가 안전하다는 보장은 없으므로 정적분석·테스트·secret scan·human review가 필요하다.
2. W07에서 기말논문에 반영할 표·그림·실험: SecureCodeScore, Precision/Recall/F1, SecretLeakage, SecureFixRate, RegressionRate, ToolRisk, BuildEvidenceCoverage 수식표와 LLM software security application matrix를 반영한다.
3. W07이 W14/W15와 연결되는 지점: LLM이 만든 코드·패치·보안 설명은 commit, dependency lock, build log, scan report, review note와 함께 evidence chain으로 남겨야 한다.

---

## 15. 최종 판단

P05는 W07의 LLM+software security 응용 핵심 문헌이다. 이 논문은 LLM이 취약점 탐지, 코드 생성, 프로그램 복구, 보안 테스트를 돕는 가능성을 보여주지만, 동시에 취약 코드 생성, secret leakage, 불완전 패치, dependency risk, tool misuse 위험을 만든다는 점을 강조한다. 따라서 기말논문에서는 P05를 **secure code generation, vulnerability detection, secret leakage, software supply chain, CI/CD evidence, human review의 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `\operatorname{softmax}` | `\mathrm{softmax}` |
| `\operatorname{argmax}` | `\mathrm{argmax}` 또는 `\arg\max` |
| `N_{secret\ exposed}` | `N_{sl}`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| `N_{code\ prompts}` | `N_{cp}`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| 긴 영문 subscript | 짧은 변수명 사용 후 표에서 의미 설명 |

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
