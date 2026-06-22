# W06 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | 보안 위협 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|
| P01 | Diffusion model 방법군과 적용 범위 정리 | diffusion taxonomy, sampling/likelihood/application 분류 | survey 중심 | 조건부 생성과 고품질 synthetic media 확산 | sampling cost, 생성 품질, 적용 범위 | 탐지 신뢰성 실험은 직접 수행하지 않음 | diffusion 원리와 조건부 생성 배경 |
| P02 | Video diffusion model의 생성·편집·이해 과제 정리 | video generation/editing taxonomy | survey 중심 | temporal synthetic media와 비디오 딥페이크 | temporal consistency, video quality, domain shift | ACM DOI 미확인, 실제 detector 검증 아님 | 비디오 도메인 이동과 압축 후처리 위험 |
| P03 | GAN의 computer vision taxonomy와 안정성 문제 정리 | architecture/loss variant survey | survey 중심 | GAN 기반 얼굴 합성·조작 | 품질, 다양성, 안정성, FID/IS 한계 | 최신 diffusion 기반 생성까지는 부족 | GAN 원리와 생성 품질 지표의 한계 |
| P04 | Deepfake 생성과 탐지 방법을 함께 정리 | creation/detection survey | survey 중심 | 허위정보, 사칭, 명예훼손, 증거 조작 | FPR/FNR, 일반화, 조작 유형별 탐지 | 최신 video diffusion까지는 제한적 | 딥페이크 위협모형과 피해 시나리오 |
| P05 | Deepfake detection reliability 정의 | transferability/interpretability/robustness taxonomy | survey와 case 중심 | 탐지기의 실제 적용 실패와 포렌식 신뢰성 | transferability, robustness, reliability | 실제 법적 증거능력은 별도 검토 필요 | W06 toy 실험의 직접 근거 |

## 종합 비교

### 1. 공통적으로 다루는 문제

다섯 편은 모두 생성 품질과 탐지 신뢰성이 같은 문제가 아니라는 점을 보여준다. P01-P03은 diffusion, video diffusion, GAN의 생성 원리를 설명하고, P04-P05는 deepfake creation/detection과 reliability 문제를 보안 평가로 연결한다.

### 2. 논문 간 차이점

P01-P03은 모델 구조, sampling, generation, quality metric을 다루는 반면 P04-P05는 피해 시나리오, 탐지 실패, reliability를 다룬다. 따라서 W06 보고서는 생성모형 원리와 forensic detector 평가를 구분하되, 기말 논문에서는 생명주기 기반 평가표로 통합한다.

### 3. 아직 해결되지 않은 문제

P02와 P03의 최종 ACM DOI는 확인하지 못했다. 또한 실제 딥페이크 benchmark 없이 survey taxonomy만으로 탐지 신뢰성을 주장할 수 없으므로, 본 주차에서는 synthetic detector score 실험으로 FPR/FNR, AUROC, ECE, review rate 기록 구조를 보완했다.

### 4. 기말 논문 주제로 발전 가능한 연결부

W06는 “생성모형 자체의 품질 평가”와 “합성미디어 탐지기의 신뢰성 평가”를 구분하는 기말 논문 장으로 발전시킬 수 있다. 특히 cross-domain reliability와 human review routing을 포함한 최소 평가표가 핵심 연결부다.
