# W05 1페이지 발표 요약

## 주제

자기지도학습·파운데이션 모델 & Poisoning/Backdoor

## 핵심 주장

표현학습 기반 모델의 보안 평가는 clean 성능 하나로 끝나지 않는다. Trigger 조건의 ASR, representation shift, defense check, 재현성 근거를 분리해서 기록해야 한다.

## 발표 흐름

| 구분 | 핵심 내용 |
|---|---|
| AI 원리 | 자기지도학습은 데이터 자체에서 supervision signal을 만들고, pretraining 표현을 downstream task에 전이한다. |
| 보안 이슈 | Poisoning은 학습 데이터를 오염시키고, backdoor는 trigger 조건에서 target behavior를 유도한다. |
| 문헌 역할 | P01-P03은 SSL/foundation 원리, P04-P05는 poisoning/backdoor 공격·방어 taxonomy를 담당한다. |
| 평가 관점 | clean accuracy, poisoned clean accuracy, ASR, mean shift, detection rate, clean FPR을 분리한다. |
| 기말 연결 | 표현학습 기반 AI 시스템의 poisoning/backdoor 평가 프레임워크로 발전시킨다. |

## Toy 실험 요약

| 항목 | 내용 |
|---|---|
| 데이터 | synthetic 2D representation clusters |
| 분류기 | nearest-centroid representation classifier |
| 공격 | source embedding에 trigger vector를 더해 target centroid 쪽으로 이동 |
| 방어 점검 | paired-view distance threshold |
| 산출물 | `metrics_summary.csv`, `results.json`, `run_log.md` |

## 주요 결과

정량값은 `04_experiment/outputs/run_log.md` 기준이다.

| 조건 | Clean | Poisoned Clean | ASR | ASR after defense | Shift |
|---|---:|---:|---:|---:|---:|
| Clean baseline | 1.000000 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 |
| Backdoor scenario | 해당 없음 | 1.000000 | 1.000000 | 해당 없음 | 2.418677 |
| Defense check | 해당 없음 | 해당 없음 | 해당 없음 | 0.000000 | 0.090597 |

## 해석

- Triggered source embedding은 toy 조건에서 target centroid로 모두 분류됐다.
- Consistency threshold는 trigger shift를 모두 플래그했고 clean FPR은 0.000000이었다.
- 이 결과는 toy 설정의 관찰값이며 실제 SSL/foundation model 보안 성능으로 일반화하지 않는다.

## DOI/URL 상태

| ID | 상태 |
|---|---|
| P01 | TPAMI DOI `10.1109/TPAMI.2024.3415112` 확인, 강의계획서 저자 표기 확인 필요 |
| P02 | DOI 확인, 현재 PDF는 recommendation survey이므로 지정 일반 SSL survey 동일 여부 확인 필요 |
| P03 | DOI 확인, arXiv URL 확인, 제목 차이와 Article 번호 확인 필요 |
| P04 | DOI 확인, 강의계획서 제목/저자 표기 차이 확인 필요 |
| P05 | DOI 확인, 강의계획서 저자 표기 확인 필요 |

## 관련 산출물

| 파일 | 용도 |
|---|---|
| `presentation_report.md` | 발표용 보고서 |
| `presentation_slides.md` | 슬라이드 원본 |
| `presentation_slides.html` | 브라우저 발표용 슬라이드 |
| `speaker_notes.md` | 슬라이드별 발표자 대본 |
| `qna.md` | 예상 질문과 답변 |
| `04_experiment/outputs/run_log.md` | 실험 수치 근거 |
