# W03 1페이지 발표 요약

## 주제

컴퓨터비전 표현학습 & 비전 대적공격

## 핵심 주장

비전 모델 보안 평가는 clean accuracy 하나로 끝나지 않는다. 정상 조건 성능, 공격 조건 성능, ASR, 재현성 근거를 분리해서 기록해야 한다.

## 발표 흐름

| 구분 | 핵심 내용 |
|---|---|
| AI 원리 | CNN은 지역 특징을 계층적으로 학습하고, ViT는 이미지를 patch token으로 처리한다. |
| 보안 이슈 | 작은 입력 교란, transfer attack, 2D/3D 조작이 모델 출력을 바꿀 수 있다. |
| 문헌 역할 | CNN/딥러닝 원리, 멀티모달/ViT 표현학습, adversarial robustness 문헌을 연결한다. |
| 평가 관점 | clean performance, attack impact, robust performance, reproducibility를 분리한다. |
| 기말 연결 | 재현성 중심 AI 보안 평가 프레임워크의 사례로 사용한다. |

## Toy 실험 요약

| 항목 | 내용 |
|---|---|
| 데이터 | synthetic 8x8 vertical/horizontal bar image |
| 모델 | nearest-centroid classifier |
| 공격 | 반대 클래스 중심점 방향 L-infinity perturbation |
| 방어 점검 | 2-level feature squeezing |
| 산출물 | `metrics_summary.csv`, `results.json`, `run_log.md`, PGM 예시 이미지 |

## 주요 결과

정량값은 `04_experiment/outputs/run_log.md` 기준이다.

| 조건 | Epsilon | Accuracy | Macro F1 | ASR |
|---|---:|---:|---:|---:|
| Clean baseline | 0.00 | 1.000000 | 1.000000 | 해당 없음 |
| Perturbation | 0.30 | 1.000000 | 1.000000 | 0.000000 |
| Perturbation | 0.45 | 0.000000 | 0.000000 | 1.000000 |
| Feature squeezing | 0.30 | 1.000000 | 1.000000 | 0.000000 |

## 해석

- Epsilon 0.45는 toy decision boundary 전환이며 실제 CNN/ViT 공격 성공이 아니다.
- 이 결과는 synthetic 2-class toy 설정의 관찰값이며 실제 CNN/ViT 강건성으로 일반화하지 않는다.
- 발표의 핵심은 수치 자체보다 평가 조건과 재현성 산출물을 분리하는 방식이다.

## 한계와 주의

- DOI/URL은 확인되었고, PDF 보관 정책과 원문 세부 수치는 최종 제출 전 사람 검토가 필요하다.
- 실제 개인정보, 운영 서비스 이미지, 무단 공격 절차는 사용하지 않는다.
- 실제 모델 확장을 주장하려면 별도 데이터셋, 모델, 공격 설정, 반복 실험이 필요하다.

## 관련 산출물

| 파일 | 용도 |
|---|---|
| `presentation_report.md` | 발표용 보고서 |
| `presentation_slides.md` | 슬라이드 원본 |
| `presentation_slides.html` | 브라우저 발표용 슬라이드 |
| `speaker_notes.md` | 슬라이드별 발표자 대본 |
| `qna.md` | 예상 질문과 답변 |
| `04_experiment/outputs/run_log.md` | 실험 수치 근거 |
