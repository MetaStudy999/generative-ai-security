# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A Survey of Deep Neural Network Watermarking Techniques |
| 저자 | Yue Li, Hongxia Wang, Mauro Barni |
| 학술지/학회 | Neurocomputing |
| 연도 | 2021 |
| DOI/URL | 확인 필요 |
| PDF 파일명 | 03_Li_Wang_Barni_2021_DNN_Watermarking_Survey.pdf |
| 검증 상태 | 로컬 PDF 제목/초록 확인, DOI/URL 최종 확인 필요 |

## 2. 한 문장 요약

> 이 논문은 DNN 워터마킹을 multimedia watermarking의 fidelity, robustness, capacity trade-off와 비교하면서 static/dynamic watermarking, white-box/black-box 검출, backdoor 기반 워터마킹의 가능성과 한계를 정리한다.

## 3. 연구문제

고비용 학습과 독점 데이터로 만들어진 DNN 모델의 지식재산을 어떻게 보호할 수 있는가가 핵심 질문이다. 기존 멀티미디어 워터마킹 개념을 DNN 모델의 weight, activation, trigger behavior에 어떻게 이식할 수 있는지도 다룬다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Fidelity | 워터마크 삽입 후 모델 성능 유지 | utility_accuracy 해석 |
| Robustness | fine-tuning, pruning, extraction 이후 검출 유지 | watermark_detection 지표 |
| Capacity | 삽입 가능한 watermark payload 크기 | 실험 범위 밖, 이론 배경 |
| Static/Dynamic watermarking | weight 기반 또는 입력-출력 행동 기반 검출 | trigger-set toy 설계 |

## 5. 방법론

워터마킹 이론의 기본 요구사항을 DNN 보호 문제에 맞게 재해석하고, 기존 방법을 taxonomy로 정리한다. 본 보고서는 이 문헌을 W13 실습의 trigger-set ownership check를 설명하는 배경으로 사용한다.

## 6. 주요 결과

DNN 워터마킹은 모델 소유권 검증에 유용하지만, 성능 저하 없이 강건한 신호를 넣는 것이 어렵다. 특히 dynamic watermark는 black-box 검증이 가능하다는 장점이 있으나 backdoor와의 경계, 오탐, 워터마크 제거 공격을 함께 고려해야 한다.

## 7. 보안 관점 분석

워터마킹은 accountability를 강화하지만 integrity와 utility를 동시에 흔들 수 있다. W13 실험의 false positive proxy가 높게 나온 점은 검출률만으로 소유권 주장을 확정하기 어렵다는 이 문헌의 trade-off 논의와 연결된다.

## 8. 한계와 오픈문제

2021년 survey라 LLM 시대의 watermarking과 model extraction 방어는 추가 문헌이 필요하다. 또한 워터마크와 backdoor의 안전한 구분, 법적 증거력, false positive 기준 설정이 남는다.

## 9. 기말 논문에 반영할 부분

fidelity-robustness-capacity trade-off, static/dynamic watermarking 분류, 오탐/미탐 관리 필요성을 보안 평가 프로토콜에 반영한다.
