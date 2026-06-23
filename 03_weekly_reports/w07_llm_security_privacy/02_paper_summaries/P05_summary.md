# 논문 요약: P05

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문명 | When Software Security Meets Large Language Models: A Survey |
| 저자 | Xiaogang Zhu, Wei Zhou, Qing-Long Han, Wanlun Ma, Sheng Wen, Yang Xiang |
| 출판정보 | IEEE/CAA Journal of Automatica Sinica, 12(2), pp. 317-334, 2025 |
| DOI/URL | `https://doi.org/10.1109/JAS.2024.124971`; IEEE Xplore `https://ieeexplore.ieee.org/document/10846956/` |
| 검증 상태 | DOI, 권호, 호수, 쪽수, 출판연도 확인. 강의계획서의 `Shujun Li et al.` 표기는 공식 저자 목록과 불일치하여 확인 필요 |

## 2. 한 문장 요약

Code LLM은 fuzzing, unit test, program repair, bug detection, bug triage를 지원하지만 insecure code generation과 flawed repair 위험도 함께 평가해야 한다[5].

## 3. 연구문제

LLM을 software security workflow에 어떻게 통합할 수 있으며, 각 단계에서 어떤 자동화 가능성과 보안 위험이 생기는가를 다룬다.

## 4. 핵심 개념

- Software testing: fuzzing, unit test generation, bug reproduction.
- Software analysis: bug detection, bug triage, program repair.
- Code LLM risk: insecure code generation, vulnerable patch, false sense of security, prompt-dependent repair.

## 5. 보안 관점 분석

P05는 W07 실험의 code security prompts 조건과 직접 연결된다. code vulnerability rate만 낮추는 것이 아니라 정상 보안 코딩 지원을 과도하게 거절하는 over-refusal도 함께 기록해야 한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | Code Vulnerability Rate |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$VulnRate=\frac{N_{unsafe\ code}}{N_{code\ outputs}}$$ |
| 기호·입력·출력 | \(N_{unsafe\ code}\): 취약 패턴 코드 출력 수, \(N_{code\ outputs}\): 코드 생성 평가 수 |
| 직관적 의미 | Code Vulnerability Rate는 LLM 보안·프라이버시 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | LLM 보안·프라이버시 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | pass rate, vulnerability rate, refusal quality, fix success rate |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 검증 메모

공식 DOI 기준 저자 목록은 Xiaogang Zhu, Wei Zhou, Qing-Long Han, Wanlun Ma, Sheng Wen, Yang Xiang이다. 강의계획서의 Shujun Li 표기는 현재 확인 자료와 대응되지 않으므로 확인 필요로 유지한다.

## 7. 기말 논문 활용

Code LLM 보안 평가에서 취약 코드 생성률, 수정 품질, bug triage 품질, refusal/over-refusal을 함께 보는 평가표 설계에 활용한다.
