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

## 6. 검증 메모

공식 DOI 기준 저자 목록은 Xiaogang Zhu, Wei Zhou, Qing-Long Han, Wanlun Ma, Sheng Wen, Yang Xiang이다. 강의계획서의 Shujun Li 표기는 현재 확인 자료와 대응되지 않으므로 확인 필요로 유지한다.

## 7. 기말 논문 활용

Code LLM 보안 평가에서 취약 코드 생성률, 수정 품질, bug triage 품질, refusal/over-refusal을 함께 보는 평가표 설계에 활용한다.
