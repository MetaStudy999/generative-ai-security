# W13 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | 보안 위협 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 | 모델 도난/추출 공격과 방어를 어떻게 체계화할 것인가 | model stealing taxonomy, attack/defense guideline | 문헌조사, 원문 세부 표 대조 필요 | model stealing, model extraction | fidelity, query cost, attack goal, defense coverage | 최신 LLM 방어는 추가 문헌 필요 | 위협모형과 query budget 지표 |
| P02 | LLM 생성물과 모델 IP를 watermarking으로 어떻게 추적할 것인가 | LLM watermarking survey, modality/function 분류 | 문헌조사, 대체 PDF | watermark removal, paraphrasing, semantic shift | detection, robustness, quality, system cost | 프롬프트 지정 P02와 로컬 PDF 불일치 | LLM watermarking 보조 배경 |
| P03 | DNN watermarking의 요구조건과 taxonomy는 무엇인가 | fidelity-robustness-capacity trade-off, static/dynamic 분류 | 문헌조사 | watermark removal, forgery, false positive | fidelity, robustness, capacity, detection reliability | LLM extraction 방어는 추가 문헌 필요 | 워터마크 평가 지표 정의 |
| P04 | 모델 추출 이후에도 LLM 소유권 신호를 검출할 수 있는가 | ModelShield, self-watermarking, robust detection | PDF 기준 LLM/QA 벤치마크 실험, 수치 원문 대조 필요 | imitation/model extraction | watermark detection, robustness, quality degradation | 법적 증거력과 adaptive removal 기준 필요 | toy trigger-set 실험의 직접 배경 |
| P05 | 생성모형을 privacy/security 관점에서 어떻게 분류할 것인가 | GAN privacy/security survey | 문헌조사, 대체 PDF | 생성모형 오용, 데이터 누출 | 적용 영역별 위험/효용 | 프롬프트 지정 P05와 로컬 PDF 불일치 | 생성모형 보호 자산 보조 배경 |

## 종합 비교

### 1. 공통적으로 다루는 문제

다섯 문헌은 모델이 단순한 파일이 아니라 학습 데이터, 파라미터, 출력 행동, 생성물, 운영 로그가 결합된 지식재산이라는 점을 공유한다. 공격자는 query-response 쌍을 모아 모델 행동을 모방하거나, 워터마크를 제거·희석하거나, 생성물을 오용할 수 있다.

### 2. 논문 간 차이점

P01은 모델 도난 공격과 방어 taxonomy, P03은 DNN 워터마킹 이론, P04는 LLM extraction 이후 소유권 검출이라는 실전형 방어를 담당한다. P02와 P05는 로컬 확보본이 프롬프트 지정 문헌과 달라 LLM watermarking과 GAN privacy/security의 보조 문헌으로만 사용한다.

### 3. 아직 해결되지 않은 문제

워터마크 검출률이 높아도 false positive가 높으면 소유권 주장의 신뢰도가 약하다. 또한 watermarking은 모델 품질, 의미 보존, robustness, 운영 비용 사이의 trade-off를 만든다. 프롬프트 지정 문헌과 로컬 PDF 불일치도 최종 제출 전 해결해야 한다.

### 4. 기말 논문 주제로 발전 가능한 연결부

W13는 “query budget, extraction fidelity, watermark detection, false positive, utility loss를 함께 보고하는 모델 IP 보호 평가표”로 발전시키기 좋다. 실제 공격 절차는 배제하고 synthetic toy 실험과 문헌 기반 threat model로 제한한다.
