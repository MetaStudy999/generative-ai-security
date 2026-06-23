# P05 Summary

## When Software Security Meets Large Language Models: A Survey — Xiaogang Zhu et al., IEEE/CAA Journal of Automatica Sinica, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W07 LLM 보안·프라이버시 |
| 논문명 | When Software Security Meets Large Language Models: A Survey |
| 저자 | Xiaogang Zhu et al. |
| 공식 출판 정보 | IEEE/CAA Journal of Automatica Sinica, Vol. 12, No. 2, pp. 317–334, 2025 |
| DOI | https://doi.org/10.1109/JAS.2024.124971 |
| 강의계획서 표기와 차이 | 강의계획서에는 `Shujun Li et al.`로 표기되어 있으나, repo의 공식 확인 정보는 `Xiaogang Zhu et al.`임 |
| 핵심 근거 사용 가능 여부 | 가능. LLM과 소프트웨어 보안의 접점을 설명하는 W07 응용 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 LLM과 소프트웨어 보안의 접점을 **취약점 탐지, 안전한 코드 생성, 프로그램 복구, 보안 테스트, 악성코드 분석, fuzzing, exploit reasoning, 코드 프라이버시, 악용 위험** 관점에서 정리하여, LLM을 보안 자동화 도구로 활용할 때도 출력 검증·비밀정보 보호·도구 권한 통제가 필수임을 보여주는 survey 문헌이다.

---

## 2. 핵심 연구문제

> LLM은 소프트웨어 보안을 어떻게 보조할 수 있으며, 동시에 어떤 취약 코드 생성·비밀정보 누출·악용 자동화 위험을 만드는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | LLM은 취약점 탐지, 코드 리뷰, 프로그램 복구, 테스트 생성에 어떤 방식으로 사용될 수 있는가? |
| RQ2 | LLM이 생성한 코드에는 어떤 보안 취약점, dependency 위험, 검증 누락 문제가 남을 수 있는가? |
| RQ3 | 소스코드, 비밀키, 내부 로그, 취약점 리포트를 LLM에 입력할 때 어떤 프라이버시·IP 위험이 발생하는가? |
| RQ4 | LLM 기반 보안 도구의 출력은 어떤 테스트, 정적분석, human review, audit log로 검증해야 하는가? |
| RQ5 | 기말논문에서 LLM 보안 활용을 안전한 범위로 제한하려면 어떤 제외 범위와 윤리적 한계가 필요한가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W07 연결 |
|---|---|---|
| LLM for software security 정리 | 취약점 탐지, 코드 생성, 패치, 테스트 등 응용 영역 정리 | LLM의 긍정적 보안 활용 |
| 보안 코드 생성 위험 | 생성 코드가 취약하거나 부정확할 수 있음을 강조 | secure code score 설계 |
| 코드 프라이버시 문제 | 내부 코드·비밀값·로그 입력 위험 제기 | privacy leakage 평가 |
| 악용 가능성 논의 | LLM이 공격 자동화에 악용될 가능성 인식 | dual-use 제한 문구 필요 |
| 운영 검증 필요 | 자동 출력은 테스트·검토·감사와 함께 써야 함 | W14 MLOps/CI-CD 연결 |

---

## 4. 핵심 이론 및 수식

> 아래 수식은 논문의 응용 영역을 W07 보고서의 평가 체계로 정리하기 위한 표준화된 표현이다. 악성 절차를 제공하지 않고, 방어적 평가와 안전한 사용 범위에 한정한다.

### 4.1 안전한 코드 생성 점수

LLM 기반 코드 생성은 기능 통과율만으로 평가하면 부족하다. 취약 패턴과 정보누출 위험을 함께 반영한다.

$$
SecureCodeScore = Utility_{code} - \lambda VulnRate - \mu LeakageRisk
$$

| 기호 | 의미 |
|---|---|
| $Utility_{code}$ | 기능 정합성, 테스트 통과율, 요구사항 충족도 |
| $VulnRate$ | 생성 코드 또는 패치에서 발견된 취약 패턴 비율 |
| $LeakageRisk$ | 코드, 비밀값, 내부정보 노출 위험 |
| $\lambda,\mu$ | 위험 항목 가중치 |

### 보안적 의미

테스트를 통과한 코드도 안전하지 않을 수 있다. 보안 요구사항, 정적분석, secret scanning, dependency 검증, human review가 필요하다.

---

### 4.2 취약점 탐지 성능

LLM 기반 취약점 탐지는 탐지율과 오탐률을 함께 봐야 한다.

$$
Precision=\frac{TP}{TP+FP}, \qquad Recall=\frac{TP}{TP+FN}
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

### 4.3 비밀정보 누출률

코드·로그·설정파일에서 비밀정보가 LLM 입력 또는 출력에 노출되는 비율을 측정한다.

$$
SecretLeakageRate=\frac{N_{secret\ exposed}}{N_{code\ prompts}}
$$

| 기호 | 의미 |
|---|---|
| $N_{secret\ exposed}$ | secret, token, key, credential 등이 노출된 사례 수 |
| $N_{code\ prompts}$ | 코드·로그 관련 평가 입력 수 |

### 보안적 의미

보안 분석을 위해 LLM에 코드를 넣는 순간 내부 IP, 비밀키, 취약점 정보가 외부로 전달될 수 있다. W14 MLOps에서는 입력 전 secret scanning과 승인 절차가 필요하다.

---

## 5. LLM-소프트웨어 보안 응용 축

| 응용 축 | 긍정적 활용 | 위험 | 대표 지표 |
|---|---|---|---|
| 취약점 탐지 | 코드 취약 패턴 설명·탐지 보조 | 오탐·미탐, hallucinated vulnerability | precision, recall, F1 |
| 안전한 코드 생성 | 보안 요구사항 반영 코드 생성 | 취약 코드 생성, dependency 위험 | VulnRate, test pass rate |
| 프로그램 복구 | 취약 패치 초안 생성 | 불완전 패치, 기능 회귀 | secure fix rate, regression test |
| 테스트 생성 | fuzz/test case 보조 | coverage 과장, 실제 결함 미탐 | coverage, defect detection |
| 보안 로그 분석 | 로그 요약·원인 후보 제시 | 민감정보 노출, 잘못된 원인 추론 | leakage rate, human agreement |
| 도구 호출 | SAST/DAST/CI 도구 연동 | 권한 오남용, 무검증 자동 실행 | tool approval rate, audit log |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 소스코드, 비밀키, API token, 취약점 리포트, 빌드 로그, CI/CD 설정, 보안 정책 |
| 공격자 목표 | 취약 코드 생성 유도, 보안정책 우회, 내부 코드·비밀정보 추출, 잘못된 패치 배포 유도 |
| 공격자 능력 | prompt 조작, insecure requirement 삽입, 반복 질의, 코드 컨텍스트 제공, tool 권한 오용 유도 |
| 방어자 능력 | secret scanning, static analysis, unit/security test, dependency scan, human code review, tool approval gate |
| 제외 범위 | 악성코드 작성, 실제 취약점 악용, 무단 시스템 공격, 실제 비밀키 입력 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W07/P05 활용 |
|---|---|---|
| Test Pass Rate | 기능 테스트 통과율 | code utility |
| Vulnerability Rate | 생성 코드의 취약 패턴 비율 | secure code 평가 |
| Secure Fix Rate | 보안 패치가 취약점을 실제로 줄인 비율 | repair 평가 |
| Regression Rate | 패치 후 기존 기능 실패율 | 안정성 평가 |
| Secret Leakage Rate | 코드·로그 내 민감정보 노출률 | privacy 평가 |
| False Positive Rate | 정상 코드를 취약으로 오탐한 비율 | 개발자 피로도 |
| False Negative Rate | 취약 코드를 놓친 비율 | 보안 실패 위험 |
| Human Review Agreement | 보안 전문가 검토와 일치도 | 책임성 평가 |
| Build Provenance | commit, dependency, build log 보존 정도 | W14 supply chain 연결 |

---

## 8. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| 코드 입력 | synthetic/open-source snippet 사용 여부, 실제 내부 코드 제외 여부 |
| 모델 | LLM 모델명, 버전, temperature, prompt template |
| 보안 도구 | SAST/secret scan/test framework 버전 |
| 평가 | test pass, vulnerability pattern, leakage 여부, human review 결과 |
| CI/CD | commit hash, dependency lock, build log, artifact hash |
| 도구 권한 | LLM이 실행 가능한 tool 목록과 승인 여부 |
| 한계 | toy 코드 결과를 실제 제품 보안성으로 일반화하지 않음 |

---

## 9. 논문의 고유 기여

1. LLM과 소프트웨어 보안의 접점을 체계적으로 정리한다.
2. 보안 자동화의 장점과 위험을 동시에 평가해야 한다는 기준을 제공한다.
3. 코드·로그·취약점 리포트가 LLM 입력으로 들어갈 때의 privacy/IP 위험을 드러낸다.
4. W14의 software supply chain과 W15의 evidence chain으로 이어지는 운영 검증 기준을 제공한다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 빠른 도구 변화 | LLM code/security 도구는 빠르게 변한다. | 모델/도구 버전 기록 |
| 실제 코드 사용 위험 | 내부 코드와 secret을 외부 LLM에 입력하면 위험하다. | synthetic/open-source toy code로 제한 |
| 자동화 과신 위험 | LLM 출력은 그럴듯하지만 틀릴 수 있다. | human review와 test를 필수화 |
| 악용 가능성 | 공격 자동화로 오용될 수 있다. | 방어적 분석과 안전한 범위로 제한 |
| 평가 기준 복잡성 | 기능 통과와 보안성은 다르다. | test pass와 vulnerability rate를 분리 |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | LLM 보안 활용은 생산성 향상과 보안 위험을 동시에 만든다는 문제의식 |
| 2장 관련연구 | LLM for software security taxonomy 정리 |
| 3장 위협모형 | code, secret, dependency, build log, tool call 보호 자산 정의 |
| 4장 연구방법 | secure code score, vulnerability rate, secret leakage rate 평가 설계 |
| 5장 분석 | toy code/security-assist 평가와 한계 제시 |
| 6장 보안적 함의 | human review, CI/CD gate, tool approval, audit log 필요성 논의 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: LLM을 소프트웨어 보안에 활용할 때는 기능 정확도뿐 아니라 취약 코드 생성, secret leakage, dependency risk, human review를 함께 평가해야 한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: SecureCodeScore, precision/recall/F1, SecretLeakageRate, CI/CD audit checklist를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: 보안 로그와 코드 문서가 RAG context로 들어올 수 있으므로 W08의 문서 오염 평가와 W14의 build/model provenance를 함께 적용해야 한다.

---

## 13. 최종 판단

P05는 W07의 소프트웨어 보안 응용 문헌이다. LLM 보안 평가는 prompt와 output만 볼 것이 아니라, 코드 생성, 취약점 분석, 도구 호출, dependency, secret, CI/CD 로그까지 포함해야 한다.

---

## 14. 변환 호환성 메모

```bash
pandoc P05_summary.md -o P05_summary.docx
pandoc P05_summary.md -o P05_summary.pdf --pdf-engine=xelatex
```
