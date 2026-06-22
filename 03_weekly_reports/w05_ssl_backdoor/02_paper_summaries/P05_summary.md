# P05 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 정식 제목 | A survey of backdoor attacks and defences: From deep neural networks to large language models |
| 저자 | Ling-Xin Jin, Wei Jiang, Xiang-Yu Wen, Mei-Yu Lin, Jin-Yu Zhan, Xing-Zhi Zhou, Maregu Assefa Habtie, Naoufel Werghi |
| 출판 정보 | Journal of Electronic Science and Technology, 23(3), Article 100326, 2025 |
| DOI/URL | `10.1016/j.jnlest.2025.100326`; https://doi.org/10.1016/j.jnlest.2025.100326 |
| 로컬 PDF | `05_Jin_et_al_2025_Backdoor_Attacks_and_Defences_Survey.pdf` |
| 검증 상태 | DOI, 제목, 저자, 학술지 확인. 강의계획서의 `Z. Jin et al.` 표기는 확인 필요 |

## 2. 저자 표기 메모

출판사 기준 첫 저자는 Ling-Xin Jin이다. 강의계획서의 `Z. Jin et al.`은 본 논문 제목과는 대응되지만 첫 저자명과 다르므로 최종 제출 전 수업자료 원본 또는 교수자 지정 목록을 확인한다.

## 3. 한 문장 요약

이 논문은 DNN부터 LLM까지 backdoor attack, detection, removal, defense를 정리하며, W05에서 clean accuracy와 ASR을 분리해야 하는 근거를 제공한다[5].

## 4. 핵심 기여

| 구분 | 내용 |
|---|---|
| Backdoor 범위 | vision/NLP/DNN backdoor에서 LLM backdoor까지 발전 흐름을 정리한다 |
| 평가축 | clean accuracy, attack success rate, stealthiness, defense success를 구분한다 |
| W05 연결 | toy 실험의 ASR, ASR after defense, detection rate, clean FPR 분리 보고의 근거가 된다 |

## 5. 보안 관점

Backdoor는 정상 입력에서는 높은 clean performance를 유지하면서 trigger 조건에서 target behavior가 나타나는 위험이다. 따라서 clean accuracy만으로는 안전성을 판단할 수 없고, ASR, representation shift, detection rate, clean false positive rate를 함께 기록해야 한다.

## 6. 한계와 확인 필요

- 2025년 최신 survey이므로 LLM backdoor 문헌은 계속 갱신될 수 있다.
- 본 보고서는 공격 절차를 악용 가능한 단계로 상세화하지 않고, 평가 지표와 방어 검증 관점만 사용한다.

## 7. 기말 논문 활용

foundation model/LLM backdoor까지 확장 가능한 평가표와 한계 분석, AI 안전성 함의 장에 활용한다.
