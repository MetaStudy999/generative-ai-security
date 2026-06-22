# W06 확률생성모형(Diffusion/GAN) & 딥페이크 검출 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W06 |
| 주제 | 확률생성모형(Diffusion/GAN) & 딥페이크 검출 |
| AI 원리 | Diffusion, score-based model, GAN, 조건부 생성 |
| 보안 이슈 | 딥페이크, 합성미디어, 포렌식, 탐지 신뢰성 |
| 문서 상태 | 최종본 |
| 실험 상태 | synthetic toy 실험 실행 완료 |

## 1. 한 문장 요약

W06는 diffusion/GAN의 생성 원리와 딥페이크 탐지의 신뢰성 문제를 연결하고, synthetic detector score 실험으로 in-domain 성능과 cross-domain FPR/FNR 차이를 분리 기록한다.

## 2. AI 원리 70%

Diffusion model은 forward process에서 데이터에 노이즈를 점진적으로 추가하고, reverse process에서 denoising을 통해 데이터 분포를 복원한다. Score-based model은 데이터 분포의 gradient 정보를 이용해 sampling을 수행하며, 조건부 생성은 text, class, image 등 외부 조건으로 생성 방향을 제어한다.

GAN은 generator와 discriminator의 경쟁 구조를 통해 사실적인 sample을 생성한다. 그러나 training instability, mode collapse, 생성 품질 지표의 한계가 반복적으로 나타난다. W06에서 중요한 점은 생성 품질이 곧 포렌식 신뢰성을 의미하지 않는다는 것이다.

## 3. 보안 이슈 30%

딥페이크와 합성미디어는 허위정보, 사칭, 명예훼손, 협박, 증거 조작 위험을 만든다. 탐지기는 benchmark에서 높은 accuracy를 보일 수 있지만, 새로운 생성기, 압축, 재인코딩, 플랫폼 후처리, 낮은 품질 영상에서는 score 분포가 변할 수 있다.

따라서 보안 평가는 accuracy 하나가 아니라 FPR, FNR, AUROC, calibration, human review routing, cross-domain generalization을 함께 기록해야 한다.

## 4. 논문 5편 요약

| ID | 논문 | 핵심 역할 | 검증 상태 |
|---|---|---|---|
| P01 | Diffusion Models: A Comprehensive Survey of Methods and Applications | diffusion 원리, sampling, 조건부 생성 배경 | DOI 확인 |
| P02 | A Survey on Video Diffusion Models | video diffusion과 temporal consistency 문제 | arXiv DOI 확인, ACM DOI 미확인 |
| P03 | Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy | GAN 구조, loss/architecture taxonomy, 안정성 문제 | arXiv DOI 확인, ACM DOI 미확인 |
| P04 | The Creation and Detection of Deepfakes: A Survey | 딥페이크 생성·탐지 위협모형 | DOI 확인 |
| P05 | Deepfake Detection: A Comprehensive Survey from the Reliability Perspective | transferability, interpretability, robustness 중심 신뢰성 관점 | DOI 확인 |

## 5. Research Track

| 항목 | 내용 |
|---|---|
| 연구문제 | 딥페이크 탐지기는 in-domain 성능이 높을 때 cross-domain 환경에서도 신뢰할 수 있는가 |
| 대상 시스템 | synthetic media detector, forensic review workflow |
| 보호 자산 | 영상/이미지 증거, 판단 로그, 모델 score, 검토 기록, 피의심자·피해자 권익 |
| 공격/실패 조건 | 새로운 생성기, 압축, 재인코딩, platform shift, low-quality input |
| 평가 지표 | accuracy, F1, FPR, FNR, AUROC, ECE, auto coverage, review rate |
| 제외 범위 | 실제 딥페이크 생성, 개인정보 사용, 무단 API/서비스 테스트 |

## 6. 실습 결과

실습은 `04_experiment/src/run_experiment.py`로 수행했다. Synthetic real/fake detector score를 만들고 threshold 0.50과 review band 0.40-0.60을 적용했다.

| 조건 | Accuracy | F1 | FPR | FNR | AUROC | ECE | Auto coverage | Review rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| In-domain detector baseline | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 1.000000 | 0.216327 | 해당 없음 | 해당 없음 |
| Cross-domain reliability stress | 0.816667 | 0.813559 | 0.166667 | 0.200000 | 0.899722 | 0.147949 | 해당 없음 | 해당 없음 |
| Review-band triage on shifted domain | 0.909091 | 0.901408 | 0.050000 | 0.135135 | 0.962162 | 0.174872 | 0.641667 | 0.358333 |

해석은 명확하다. 기준 도메인에서 완전한 분리가 가능해도, 압축·미지 도메인을 가정하면 FPR과 FNR이 동시에 생긴다. 불확실 구간을 human review로 보내면 자동판정 범위는 줄지만 자동판정 영역의 오류율을 낮출 수 있다.

## 7. 기말논문 연결

W06는 기말 논문의 관련연구, 위협모형, 평가방법, 보안적 함의 장에 연결된다. 특히 “생성모형 품질 평가”와 “탐지기 신뢰성 평가”를 구분하고, cross-domain reliability와 review routing을 포함한 평가표를 제안하는 근거가 된다.

## 8. AI 활용 기록

Codex를 사용해 문헌 요약 구조화, DOI/URL 검증 보조, synthetic toy 실험 코드 작성, 실행 로그 생성, 제출·발표자료 작성을 수행했다. 정량값은 `04_experiment/outputs/` 산출물과 일치하는 값만 사용했다.

## 9. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 완료 |
| 비교표 | 완료 |
| AI 원리 70% | 완료 |
| 보안 이슈 30% | 완료 |
| Research Track | 완료 |
| 실험 코드와 실행 로그 | 완료 |
| 제출 보고서 | 완료 |
| 발표자료 | 완료 |
| DOI/URL 검증표 | 부분 완료 |
