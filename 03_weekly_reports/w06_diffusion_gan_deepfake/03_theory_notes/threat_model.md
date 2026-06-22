# 위협모형

| 항목 | 내용 |
|---|---|
| 대상 시스템 | synthetic media detector, deepfake forensic review workflow |
| 보호 자산 | media evidence, detector score, threshold, model decision, review log, affected individuals |
| 공격자/실패 조건 | unknown generator, compression, re-encoding, platform shift, low-quality input, adversarial post-processing |
| 공격자의 지식 | white-box, gray-box, black-box 조건을 구분하되 W06 실험은 공격 실행을 포함하지 않음 |
| 공격자의 능력 | detector score 분포를 흔드는 도메인 이동, 압축, 후처리, 미지 생성기 조건 |
| 공격/실패 성공 조건 | false positive accusation, false negative missed detection, overconfident unreliable decision |
| 방어/점검 | review-band triage, calibration check, cross-domain stress test, reproducibility evidence |
| 로그와 책임성 | seed, config, threshold, review band, outputs, run log 보존 |
| 제외 범위 | 실제 딥페이크 생성, 실제 개인정보 사용, 무단 API 질의, 실제 운영 서비스 테스트, 악성코드 실행 |

## 연구문제 후보

RQ1. 딥페이크 탐지기의 in-domain 성능과 cross-domain 성능은 어떤 지표에서 차이를 보이는가?

RQ2. FPR, FNR, AUROC, ECE는 딥페이크 탐지 신뢰성을 각각 어떻게 설명하는가?

RQ3. Review-band triage는 자동판정률, 검토율, 자동판정 영역의 오류율을 어떻게 변화시키는가?

RQ4. 생성 품질 평가와 포렌식 탐지 신뢰성 평가는 어떤 기준으로 분리해야 하는가?
