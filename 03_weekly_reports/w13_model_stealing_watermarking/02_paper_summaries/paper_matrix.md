# W13 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | AI 원리 기여 | 보안 위협 연결 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|---|
| P01 | 모델 도난·모델 추출 공격과 방어를 어떻게 체계화할 것인가 | model stealing taxonomy, attack goal, defense selection guideline | 문헌조사, ACM CSUR DOI 확인 완료 | query-response learning, substitute model, fidelity 개념 | model extraction, query abuse, behavior leakage | extraction fidelity, query cost, attack goal, defense coverage | 최신 LLM/생성모형 방어는 추가 문헌 필요 | 위협모형과 query budget 지표 |
| P02 | Deep learning model watermarking/fingerprinting 또는 LLM watermarking을 어떻게 분류할 것인가 | watermarking/fingerprinting survey, detection/robustness taxonomy | 현재 로컬 PDF는 LLM watermarking 관련 보조 문헌 | watermark signal, fingerprint, traceability | watermark removal, paraphrasing, semantic shift, false positive | detection rate, robustness, quality, FPR, system cost | 지정 P02와 로컬 PDF 표기 차이 | LLM watermarking 보조 배경, 지정 논문처럼 인용 금지 |
| P03 | DNN watermarking의 요구조건과 taxonomy는 무엇인가 | fidelity-robustness-capacity trade-off, static/dynamic watermarking 분류 | Neurocomputing 461, 171-193, DOI 확인 완료 | model watermark/fingerprint 기본 요구조건 | watermark removal, forgery, ownership ambiguity | fidelity, robustness, capacity, detection reliability, FPR | 강의계획서 저자명·제목 차이 확인 필요 | 워터마크 평가 지표 정의 |
| P04 | 모델 추출 이후에도 소유권 신호를 안정적으로 검출할 수 있는가 | ModelShield, adaptive watermark, robust ownership check | IEEE TIFS 20, 1767-1782, DOI 확인 완료 | extraction 이후 watermark inheritance와 detection | imitation/model extraction, watermark removal | watermark detection, robustness, utility degradation, FPR | 법적 증거력·adaptive removal 기준 별도 필요 | toy trigger-set 실험의 직접 배경 |
| P05 | GAN 또는 생성모형의 attack/defense와 privacy/security를 어떻게 분류할 것인가 | GAN security/privacy survey 또는 attack/defense survey | 현재 로컬 PDF는 GAN private/security application 관련 보조 문헌 | generative model misuse, model/data leakage, provenance | 생성모형 오용, 데이터 누출, 생성물 출처 모호성 | application risk, privacy/security metric | 지정 P05와 로컬 PDF 표기 차이 | 생성모형 보호 자산 보조 배경, 지정 논문처럼 인용 금지 |

## 종합 비교

P01은 model stealing/extraction taxonomy 문헌이다. P02는 현재 LLM watermarking 관련 보조 문헌이며, 지정 논문과 분리해야 한다. P03은 DNN watermarking 요구조건과 trade-off 문헌이다. P04는 extraction 이후 ownership check를 다루는 직접 관련 문헌이다. P05는 현재 GAN privacy/security 관련 보조 문헌이며, 지정 논문과 분리해야 한다.

W13의 핵심 연결부는 query budget, extraction fidelity, substitute accuracy, watermark detection, false positive rate, utility accuracy를 함께 보고하는 것이다. watermark detection이 높아도 false positive가 높으면 소유권 검증 신뢰도가 낮다. W13 toy 실험은 실제 API 공격이나 상용 모델 탈취가 아니라 synthetic query-response evaluation이다.

## False Positive 기반 차별성

| 검증 항목 | 단독 해석 위험 | 보완 지표 |
|---|---|---|
| Watermark Detection | 높으면 소유권 증거처럼 보일 수 있음 | FPR, FNR, p-value, 대조군 |
| False Positive Rate | 높으면 무관 모델도 소유 모델처럼 판단될 수 있음 | unrelated model control, random trigger control |
| Extraction Fidelity | 높으면 추출 위험을 보여주지만 ownership 증거는 아님 | query budget, utility, trigger inheritance |
| Utility Accuracy | 워터마크 삽입이 모델 성능을 해치지 않는지 확인 | clean accuracy, task score |
| Query Budget | 공격 비용과 위험 노출 범위 | rate limit, monitoring, logging |
