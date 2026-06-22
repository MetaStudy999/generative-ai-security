# W06 통합보고서 초안

최종본은 `../final/integrated_report_final.md`에 정리했다. 본 초안은 W06 산출물의 작성 흐름과 검토 포인트를 남긴다.

## 핵심 방향

W06는 diffusion/GAN 생성 원리를 정리하되, 보안 분석의 초점을 “딥페이크를 만드는 방법”이 아니라 “탐지 결과를 얼마나 신뢰할 수 있는가”로 둔다. 따라서 실험도 실제 딥페이크 생성 없이 synthetic detector score 분포를 사용했다.

## 실험 초안 요약

| 조건 | 핵심 관찰 |
|---|---|
| In-domain detector baseline | 기준 도메인에서는 accuracy/F1 1.000000 |
| Cross-domain reliability stress | accuracy 0.816667, FNR 0.200000으로 신뢰성 저하 |
| Review-band triage | review rate 0.358333, auto coverage 0.641667로 자동판정 위험 완화 |

## 남은 검토 포인트

- P02와 P03의 최종 ACM DOI는 추가 확인이 필요하다.
- Synthetic toy 결과를 실제 forensic detector 성능으로 일반화하지 않는다.
- 제출본과 발표자료의 수치는 `04_experiment/outputs/`와 일치해야 한다.
