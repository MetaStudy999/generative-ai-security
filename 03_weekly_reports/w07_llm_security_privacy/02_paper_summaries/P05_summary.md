# P05 Summary

## When Software Security Meets Large Language Models: A Survey — Xiaogang Zhu et al., IEEE/CAA Journal of Automatica Sinica, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W07 LLM 보안·프라이버시 |
| 논문명 | When Software Security Meets Large Language Models: A Survey |
| 저자 | Xiaogang Zhu et al. |
| 출판 정보 | IEEE/CAA Journal of Automatica Sinica, 12(2), pp. 317–334, 2025 |
| DOI | https://doi.org/10.1109/JAS.2024.124971 |
| 검증 상태 | W07 `paper_list.md` 기준 공식 DOI 확인. 강의계획서 `Shujun Li` 표기 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 LLM과 소프트웨어 보안의 접점을 **vulnerability detection, secure code generation, program repair, malware analysis, fuzzing, exploit reasoning, code privacy, misuse risk** 관점에서 정리하고, W07에서 LLM 보안 활용과 LLM 기반 위험을 동시에 평가하게 하는 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | LLM은 소프트웨어 보안 분석과 취약점 탐지에 어떻게 활용될 수 있는가? |
| RQ2 | LLM이 생성한 코드에는 어떤 보안 취약점과 책임 문제가 남는가? |
| RQ3 | 코드·로그·취약점 정보가 LLM에 입력될 때 어떤 프라이버시·IP 위험이 발생하는가? |
| RQ4 | 기말논문에서 LLM 보안 활용을 어떤 안전 범위와 감사 기준으로 제한해야 하는가? |

---

## 3. 핵심 수식·지표

$$
SecureCodeScore = Utility_{code} - \lambda VulnRate - \mu LeakageRisk
$$

| 기호 | 의미 |
|---|---|
| $Utility_{code}$ | 기능 정합성, 테스트 통과율 |
| $VulnRate$ | 생성 코드의 취약 패턴 비율 |
| $LeakageRisk$ | 코드·비밀값·내부정보 노출 위험 |

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | 소스코드, 비밀키, 취약점 리포트, 빌드 로그, 보안 정책 |
| 공격자 목표 | 취약 코드 생성 유도, 보안정책 우회, 비밀정보 추출, 악성 자동화 |
| 공격자 능력 | prompt 조작, insecure requirement 삽입, 반복 질의, 코드 컨텍스트 제공 |
| 대표 지표 | pass@k, vulnerability rate, secret leakage, secure fix rate, false positive/negative |
| 제외 범위 | 악성코드 작성, 실제 취약점 악용, 무단 시스템 공격 |

---

## 5. 기말논문 연결

P05는 LLM을 보안 도구로 쓸 때의 실효성과 위험을 동시에 보여준다. 기말논문에서는 생성형 AI 보안 평가 프레임에 “코드·도구·자동화 출력의 보안성 검증” 항목을 추가하는 근거로 사용한다.

---

## 6. 최종 판단

P05는 W07의 소프트웨어 보안 응용 문헌이다. LLM 보안 평가는 prompt/output뿐 아니라 코드 생성, 취약점 분석, 도구 호출, 비밀정보 보호까지 포함해야 한다.
