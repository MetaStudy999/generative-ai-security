# W06 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | AI 원리 기여 | 보안 위협 연결 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|---|
| P01 | Diffusion model의 방법군과 응용은 어떻게 분류되는가 | forward/reverse process, score-based model, sampling, conditional generation survey | 이미지·음성·텍스트 등 생성 응용 문헌 | diffusion/score-based 생성 원리 | 고품질 synthetic media 생성 가능성, 탐지기 우회 위험 | sampling cost, generation quality, likelihood, FID 등 원문 확인 | detector reliability 직접 실험은 아님 | diffusion 원리와 조건부 생성 배경 |
| P02 | Video diffusion model은 시간 일관성과 조건부 생성을 어떻게 다루는가 | video generation/editing/prediction taxonomy | video generation 문헌 조사 | temporal consistency와 video diffusion 구조 | 영상 딥페이크, temporal artifact, compression/platform shift | temporal consistency, video quality, FVD 등 원문 확인 | ACM DOI는 확인됐지만 강의계획서 지정 논문과 동일 여부 확인 필요 | cross-domain video deepfake 위험 |
| P03 | GAN은 computer vision에서 어떤 구조와 loss로 발전했는가 | GAN architecture, loss, taxonomy survey | image synthesis/computer vision 문헌 조사 | generator-discriminator 경쟁 구조 | GAN 기반 얼굴 합성·조작, 생성 품질 지표 한계 | FID, IS, diversity, stability 등 원문 확인 | 강의계획서 저자명과 현재 저자명 차이 확인 필요 | GAN 원리와 생성 품질-탐지 신뢰성 분리 |
| P04 | Deepfake 생성과 탐지는 어떻게 발전했는가 | creation/detection survey | face/video manipulation 문헌 | deepfake 생성·탐지 방법 연결 | 허위정보, 사칭, 명예훼손, 증거 조작 | FPR, FNR, detector accuracy, robustness | 최신 diffusion/video generation까지는 제한적 | deepfake threat model 핵심 근거 |
| P05 | Deepfake detection reliability는 어떤 요소로 평가해야 하는가 | reliability, transferability, interpretability, robustness survey | deepfake detector 문헌 | detector 평가 신뢰성 관점 | domain shift, compression, unknown generator, calibration failure | AUROC, ECE, FPR/FNR, cross-domain performance | 실제 법적 포렌식 증거능력은 별도 검토 필요 | W06 실험과 KCI/SCI 주제의 직접 근거 |

## 종합 비교

P01-P03은 생성모형 원리와 생성 품질 평가 문헌이다. P01은 diffusion과 score-based model의 확률적 생성 원리, P02는 video diffusion의 temporal consistency, P03은 GAN의 generator-discriminator 경쟁 구조와 생성 품질 지표를 다룬다.

P04-P05는 deepfake threat model과 detection reliability 문헌이다. P04는 생성과 탐지의 공격·방어 지형을 연결하고, P05는 transferability, robustness, interpretability, calibration 관점에서 실제 탐지 신뢰성을 재정리한다.

W06의 핵심 연결부는 “생성 품질”과 “포렌식 탐지 신뢰성”을 구분하는 것이다. 고품질 sample 생성, FID/IS, video quality 지표가 높다고 해서 detector의 FPR, FNR, calibration, cross-domain robustness가 자동으로 보장되지는 않는다.

딥페이크 탐지 평가는 accuracy 하나가 아니라 FPR, FNR, AUROC, ECE, review rate, auto coverage를 함께 봐야 한다. 특히 FPR은 무고한 사람을 의심하게 만드는 위험이고, FNR은 실제 조작물을 놓치는 위험이므로 사회적·법적 피해가 서로 다르다.

W06 toy 실험은 실제 deepfake detector 평가가 아니라 reliability metric reporting 구조를 설명하는 synthetic score 실험이다. 실험 수치는 실제 딥페이크 데이터셋, 실제 탐지 모델, 법적 포렌식 증거능력, 운영 서비스의 보안 성능으로 일반화하지 않는다.

P02/P03은 ACM DOI가 확인되었지만 강의계획서의 P02 저자·제목 표기와 P03 저자명 표기가 현재 로컬 PDF/출판사 메타데이터와 다르므로 최종 제출 전까지 `부분 검증` 상태를 유지한다.
