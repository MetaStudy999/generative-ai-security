# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Survey on federated learning threats: Concepts, taxonomy on attacks and defences, experimental study and challenges |
| 저자 | Nuria Rodríguez-Barroso et al. |
| 학술지/학회 | Information Fusion |
| 연도 | 2023 |
| DOI/URL | arXiv:2201.08135, 출판사 DOI 확인 필요 |
| PDF 파일명 | 03_Rodriguez_Barroso_et_al_2023_FL_Threats_Survey.pdf |
| 검증 상태 | 로컬 PDF 첫 페이지에서 arXiv preprint 확인, Information Fusion 출판 DOI는 최종 대조 필요 |

## 2. 한 문장 요약

> 이 논문은 FL adversarial threat와 defense taxonomy를 정리하고 실험 연구를 포함해, 공격 유형별 방어 선택 기준과 남은 과제를 제시한다.

## 3. 연구문제

이 논문에서 기말 연구와 연결되는 질문은 FL에서 adversarial attack과 defense를 어떤 taxonomy로 짝지을 것인가이다. W10 실험에서는 이 논문을 근거로 malicious client rate, defense type, clean utility, ASR을 분리해 기록한다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Attack taxonomy | FL privacy/integrity attack을 분류하는 체계 | threat model |
| Defense taxonomy | 공격 범주에 대응하는 방어법 분류 | evaluation protocol |
| Model integrity | 악성 업데이트가 글로벌 모델을 왜곡하는 위험 | poisoning 실험 |
| Data privacy | 분산 구조에서도 local data 단서가 노출될 수 있는 위험 | leakage proxy |

## 5. 방법론

이 문헌은 공격과 방어 taxonomy를 함께 제시하고, 공격 범주별 적절한 방어 선택을 논의한다. 본 보고서는 실제 공격 재현 대신 toy malicious update와 coordinate median 방어 비교로 축소한다.

## 6. 주요 결과

FL에서는 데이터가 보이지 않는다는 특징 때문에 서버가 로컬 업데이트의 무결성을 검증하기 어렵다. 이 한계가 W10 실험에서 malicious client rate를 독립변수로 둔 이유다.

## 7. 보안 관점 분석

이 논문은 Gradient leakage, poisoning, backdoor, privacy attack을 이해하기 위한 배경 문헌으로 활용된다. 공격자의 능력, 방어자의 관측 가능성, 평가 데이터의 한계, 재현성 조건을 함께 정리해야 실제 보안 연구로 이어질 수 있다.

## 8. 한계와 오픈문제

원문 정밀 독해 전에는 세부 실험 설정, 데이터셋, DOI, 인용 관계를 확정할 수 없다. 또한 survey 성격의 문헌은 실제 재현 실험보다는 분류체계와 연구 공백 파악에 더 적합하므로, 기말 논문에서는 별도 평가 프로토콜로 보완해야 한다.

## 9. 기말 논문에 반영할 부분

P03는 공격-방어 taxonomy와 평가 프로토콜의 중심 문헌으로 반영한다. 특히 clean utility와 attack impact를 동시에 기록해야 한다는 근거로 사용한다.
