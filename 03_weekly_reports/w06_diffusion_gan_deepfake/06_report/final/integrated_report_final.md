# W06 확률생성모형(Diffusion/GAN) & 딥페이크 검출 통합보고서

## 0. 메타정보

- 주차: W06
- 주제: 확률생성모형(Diffusion/GAN) & 딥페이크 검출
- 문서 상태: 제출용 최종 초안, 사람 검토 필요
- 최종 제출 확정 여부: 미확정
- 실험 상태: synthetic detector score toy 실험 실행 완료
- 실험 실행일: 2026-06-22
- 최종 보완 점검일: 2026-06-23 (Asia/Seoul)
- 핵심 검증 이슈: P02/P03 강의계획서 지정 논문 동일 여부, PDF 원문 public GitHub 보관 위험

## 1. 한 문장 요약

W06는 diffusion/GAN의 생성 품질 평가와 딥페이크 탐지기의 포렌식 신뢰성 평가를 분리하고, synthetic detector score toy 실험으로 in-domain 성능, cross-domain FPR/FNR 저하, review-band triage의 보고 구조를 확인한다.

## 2. 학습 배경과 주차 목표

### 2.1 이번 주 주제의 위치

W06는 W05의 파운데이션 모델·표현학습 논의를 확률생성모형과 합성미디어 보안으로 확장하는 주차다. W01은 AI 보안 평가의 생명주기 프레임을 세웠고, W02는 학습 데이터 오염, W03는 비전 대적공격, W04는 Transformer/NLP 프라이버시, W05는 표현공간 backdoor를 다루었다. W06는 diffusion, score-based model, GAN, video diffusion, deepfake detection을 연결하여 생성모형의 품질과 포렌식 탐지 신뢰성을 분리해 평가한다. 이후 W07 LLM 보안, W08 RAG 프롬프트 인젝션, W12 XAI·강건성, W14 MLOps 운영 리스크와 연결된다.

### 2.2 강의계획서상 학습목표

- Diffusion model의 수학적 정식화와 sampling 알고리즘을 비교한다.
- GAN 기반 생성모형과 합성미디어 위협모형을 연결한다.
- Deepfake detection의 데이터 편향, 일반화, 신뢰성 지표를 설계한다.

### 2.3 이번 주 핵심 질문

1. Diffusion model과 GAN은 어떤 방식으로 synthetic media를 생성하는가?
2. 생성 품질 지표가 왜 포렌식 탐지 신뢰성을 보장하지 않는가?
3. 딥페이크 탐지에서 FPR과 FNR은 어떤 사회적·법적 위험으로 이어지는가?
4. Cross-domain reliability stress와 review-band triage는 왜 필요한가?
5. W06의 synthetic detector score 실험을 KCI 또는 SCI 논문 주제로 발전시키려면 어떤 연구문제가 적절한가?

## 3. AI 원리 70% 정리

Diffusion model은 forward noising과 reverse denoising을 통해 데이터 분포를 복원하는 생성모형 계열이다[1]. Score-based model은 데이터 분포의 gradient 정보를 이용해 sampling하고, 조건부 생성은 text, class, image 등 외부 조건으로 생성 방향을 제어한다[1].

Video diffusion model은 이미지 생성과 달리 시간적 일관성과 조건부 생성을 함께 고려해야 한다[2]. GAN은 generator와 discriminator의 경쟁 구조를 통해 사실적인 sample을 생성하지만 품질 지표와 안정성 문제가 반복된다[3].

표 1. W06 핵심 개념과 보안 연결

| 개념 | AI 원리 | 보안 연결 | 관련 문헌 |
|---|---|---|---|
| Diffusion/score-based model | 노이즈 추가와 제거를 통한 확률적 생성 | 고품질 synthetic media와 탐지기 우회 위험 | [1] |
| Video diffusion | temporal consistency와 text/video conditioning | 영상 딥페이크, 압축·플랫폼 shift | [2] |
| GAN | generator-discriminator minimax 구조 | 얼굴 합성, artifact 기반 탐지 한계 | [3] |
| Deepfake creation/detection | 생성 기법과 탐지 기법의 공진화 | 허위정보, 사칭, 증거 조작 | [4] |
| Reliability-oriented detection | transferability, robustness, calibration | FPR/FNR, human review, 포렌식 신뢰성 | [5] |

## 4. 보안 이슈 30% 정리

Deepfake 생성과 탐지는 허위정보, 사칭, 증거 조작 등 사회적·보안적 위험과 연결된다[4]. Deepfake detection reliability는 단순 accuracy가 아니라 transferability, robustness, interpretability, calibration을 함께 고려해야 한다[5].

보안 관점에서 FPR은 무고한 사람을 의심하게 만드는 위험이고, FNR은 실제 조작물을 놓치는 위험이다. AUROC는 threshold와 독립적인 분리력을 보여주지만, 실제 운영에서는 threshold, review band, 자동판정률, 검토율이 함께 기록되어야 한다. ECE는 detector confidence와 실제 정답률 사이의 불일치를 점검하는 보조 지표다.

그림 1. 딥페이크 탐지 신뢰성 평가 흐름

```text
Media Input / Synthetic Media
        |
        v
Detector Score
        |
        v
In-Domain Evaluation --> Accuracy, F1, FPR, FNR, AUROC, ECE
        |
        v
Cross-Domain Stress --> Score Shift, FPR/FNR Increase
        |
        v
Review-Band Triage --> Auto Coverage, Review Rate
        |
        v
Human Review / Forensic Workflow
        |
        v
Reproducibility Evidence --> seed, config, threshold, review band, outputs, run_log
```

## 5. 논문 5편 요약

표 2. 관련 문헌 5편 요약

| ID | 논문 | 출판/DOI 상태 | 핵심 역할 | 남은 확인 |
|---|---|---|---|---|
| P01 | Yang et al., Diffusion Models: A Comprehensive Survey of Methods and Applications | ACM CSUR Vol. 56 No. 4 Article 105, DOI `10.1145/3626235` | diffusion/score-based model, sampling, 조건부 생성 배경 | arXiv판과 ACM판 세부 인용 위치 |
| P02 | Xing et al., A Survey on Video Diffusion Models | ACM CSUR Vol. 57 No. 2, DOI `10.1145/3696415`, arXiv `2310.10647` | video diffusion과 temporal consistency | 강의계획서 `Ananya Högele et al.` 논문과 동일 여부, Article 번호 |
| P03 | Zhengwei Wang, Qi She, Tomas E. Ward, Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy | ACM CSUR Vol. 54 No. 2 Article 37, DOI `10.1145/3439723`, arXiv `1906.01529` | GAN taxonomy, loss/architecture, 생성 품질 지표 한계 | 강의계획서 `Tianqi Wang et al.` 표기 차이 |
| P04 | Mirsky and Lee, The Creation and Detection of Deepfakes: A Survey | ACM CSUR Vol. 54 No. 1, DOI `10.1145/3425780` | 딥페이크 생성·탐지 위협모형 | Article 번호 확인 필요 |
| P05 | Tianyi Wang et al., Deepfake Detection: A Comprehensive Survey from the Reliability Perspective | ACM CSUR Vol. 57 No. 3, DOI `10.1145/3699710` | reliability, transferability, robustness | 강의계획서 `J. Wang et al.` 표기 대응 |

## 6. 논문 5편 비교표

P01-P03은 생성모형 원리와 생성 품질 평가 문헌이다. P04-P05는 deepfake threat model과 detection reliability 문헌이다. W06의 핵심 연결부는 “생성 품질”과 “포렌식 탐지 신뢰성”을 구분하는 것이다.

P01은 diffusion/score-based 생성 원리를 제공하고, P02는 video domain의 temporal artifact와 platform shift를 보안 평가 항목으로 끌어온다. P03은 GAN의 generator-discriminator 구조와 FID/IS 같은 생성 품질 지표의 한계를 보여준다. P04는 deepfake 생성·탐지의 공격/방어 지형을 정리하고, P05는 reliability 관점에서 FPR/FNR, calibration, robustness, transferability를 강조한다.

P02/P03은 ACM DOI가 확인되었지만 강의계획서 지정 문헌과 현재 로컬 PDF/출판사 메타데이터의 저자·제목 표기가 달라 최종 제출 전까지 `부분 검증` 상태를 유지한다.

## 7. Research Track 분석

표 3. W06 Research Track 요약

| 항목 | 내용 |
|---|---|
| 연구문제 | 딥페이크 탐지기는 in-domain 성능이 높을 때 cross-domain 조건에서도 신뢰할 수 있는가 |
| 대상 시스템 | synthetic media detector, deepfake forensic review workflow |
| 보호 자산 | media evidence, detector score, threshold, model decision, review log, affected individuals |
| 실패/위협 조건 | unknown generator, compression, re-encoding, platform shift, low-quality input |
| 성공 조건 | false positive accusation, false negative missed detection, overconfident unreliable decision |
| 방어/점검 | review-band triage, calibration check, cross-domain stress test |
| 제외 범위 | actual deepfake generation, personal data use, unauthorized service testing, operational attack execution |

## 8. 실습 보고서

본 실습은 실제 딥페이크 생성이나 실제 탐지 모델 평가가 아니라 W06의 핵심인 딥페이크 탐지 신뢰성 평가축을 안전하게 설명하기 위한 최소 toy protocol이다. 따라서 synthetic real/fake detector score 분포와 threshold-based toy detector를 사용하되, 평가 구조는 이후 실제 deepfake benchmark, platform shift, human-in-the-loop forensic workflow에도 확장 가능하도록 accuracy, F1, FPR, FNR, AUROC, ECE, auto coverage, review rate, reproducibility evidence로 분리하였다.

표 4. W06 실습 설계

| Item | Description |
|---|---|
| Dataset | Synthetic real/fake detector score distributions |
| Detector | Threshold-based toy deepfake detector |
| In-domain score setting | real mean 0.22, fake mean 0.78, std 0.08 |
| Cross-domain score setting | real mean 0.34, fake mean 0.61, std 0.16 |
| Threshold | 0.50 |
| Review band | 0.40-0.60 |
| Metrics | Accuracy, F1, FPR, FNR, AUROC, ECE, auto coverage, review rate |
| Environment | Ubuntu 24.04 / Docker / Python 3.11 |
| Seed | 42 |
| Output files | `metrics_summary.csv`, `results.json`, `run_log.md` |

표 5. W06 실습 결과

| 조건 | Accuracy | F1 | FPR | FNR | AUROC | ECE | Auto coverage | Review rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| In-domain detector baseline | 1.000000 | 1.000000 | 0.000000 | 0.000000 | 1.000000 | 0.216327 | 해당 없음 | 해당 없음 |
| Cross-domain reliability stress | 0.816667 | 0.813559 | 0.166667 | 0.200000 | 0.899722 | 0.147949 | 해당 없음 | 해당 없음 |
| Review-band triage on shifted domain | 0.909091 | 0.901408 | 0.050000 | 0.135135 | 0.962162 | 0.174872 | 0.641667 | 0.358333 |

이 결과는 synthetic detector score toy 실험의 평가 형식 검증용 수치이며, 실제 딥페이크 데이터셋, 실제 탐지 모델, 법적 포렌식 증거능력, 운영 서비스의 보안 성능으로 일반화하지 않는다.

## 9. AI 도구 활용 기록

Codex를 사용해 문헌 요약 보강, DOI/URL 검증 보조, 개념 설명, 문장 구조화, synthetic detector score 실험 코드 작성, 발표자료 작성, KCI/SCI 섹션 보완을 수행했다. AI 산출물은 초안으로 취급했으며, 최종 제출자는 원고의 내용, 인용, 실험결과, 연구윤리 책임을 확인해야 한다.

## 10. 토론 질문

1. In-domain accuracy가 1.000000인 탐지기를 cross-domain 포렌식 상황에서 신뢰할 수 있는가?
2. 딥페이크 탐지에서 FPR과 FNR 중 어느 오류가 더 위험한지는 누가 판단해야 하는가?
3. Review-band triage는 자동판정 위험을 줄이지만 review workload를 늘린다. 어느 수준의 review rate가 적절한가?
4. 생성 품질 지표와 포렌식 신뢰성 지표를 같은 benchmark에 넣을 때 어떤 오해가 생길 수 있는가?
5. P02/P03처럼 강의계획서 표기와 출판사 메타데이터가 다를 때 제출문헌 검증표는 어디까지 확정해야 하는가?

## 11. 기말논문 연결

추천 주제는 “딥페이크 탐지기의 cross-domain reliability 평가 프레임워크”이다. W06는 기말 논문의 관련연구, 위협모형, 평가방법, 보안적 함의 장에 연결된다. 특히 생성모형 품질 평가와 탐지기 신뢰성 평가를 구분하고, FPR/FNR, AUROC, ECE, auto coverage, review rate, reproducibility evidence를 함께 기록하는 평가표가 핵심 기여가 될 수 있다.

## 12. KCI 논문 형식 전환

### 12.1 KCI형 제목 후보

표 6. KCI 논문 제목 후보

| 번호 | 국문 제목 후보 | 영문 제목 후보 | 대상 시스템 | 보안 위협 | 연구방법 | 예상 기여 |
|---:|---|---|---|---|---|---|
| 1 | 딥페이크 탐지기의 Cross-Domain Reliability 평가 프레임워크 연구 | A Study on a Cross-Domain Reliability Evaluation Framework for Deepfake Detectors | Synthetic media detector | 미지 생성기, 압축, 플랫폼 shift | 문헌분석 + synthetic score 실험 | FPR/FNR·review routing 평가표 |
| 2 | 생성모형 품질 평가와 딥페이크 포렌식 탐지 신뢰성 평가의 분리 기준 연구 | A Study on Separating Generative Model Quality Evaluation from Deepfake Forensic Detection Reliability Evaluation | Diffusion/GAN 기반 합성미디어 | 탐지기 과신, 포렌식 오류 | 비교분석 + 체크리스트 | 생성 품질·탐지 신뢰성 분리 |
| 3 | Human Review Routing을 포함한 딥페이크 탐지 평가체계 연구 | A Deepfake Detection Evaluation Framework with Human Review Routing | Forensic review workflow | false accusation, missed detection | synthetic score 실험 + review-band triage | 자동판정률과 검토율 동시 평가 |

### 12.2 추천 최종 제목

- 국문: 딥페이크 탐지기의 Cross-Domain Reliability 평가 프레임워크 연구
- 영문: A Study on a Cross-Domain Reliability Evaluation Framework for Deepfake Detectors

### 12.3 국문초록 초안

본 연구는 확률생성모형과 딥페이크 탐지 기술을 구분하여, 생성 품질 평가와 포렌식 탐지 신뢰성 평가를 분리하는 cross-domain reliability 평가 프레임워크를 제안한다. Diffusion model, video diffusion, GAN, deepfake creation/detection, deepfake detection reliability 관련 선행연구를 비교하고, accuracy, F1, false positive rate, false negative rate, AUROC, expected calibration error, auto coverage, review rate의 평가축을 도출한다. 또한 실제 딥페이크 생성이나 개인정보 사용 없이 synthetic real/fake detector score 분포를 활용하여 in-domain baseline, cross-domain reliability stress, review-band triage 조건을 비교한다. 본 연구는 딥페이크 탐지기의 benchmark 성능이 실제 운영·포렌식 신뢰성을 보장하지 않음을 보이고, human review routing을 포함한 재현 가능한 평가표를 제시하는 데 목적이 있다.

### 12.4 영문초록 초안

This study proposes a cross-domain reliability evaluation framework for deepfake detectors by separating generative model quality evaluation from forensic detection reliability evaluation. By reviewing studies on diffusion models, video diffusion models, GANs, deepfake creation and detection, and reliability-oriented deepfake detection, this report derives evaluation axes including accuracy, F1, false positive rate, false negative rate, AUROC, expected calibration error, auto coverage, and review rate. A safe synthetic toy experiment using real/fake detector score distributions is used to compare in-domain baseline performance, cross-domain reliability stress, and review-band triage. The goal is not to generate or evaluate real deepfakes, but to demonstrate a reproducible reporting structure for deepfake detector reliability under domain shift.

### 12.5 키워드

국문 키워드: 딥페이크 탐지, Diffusion, GAN, 포렌식 신뢰성, FPR, FNR, Human Review

영문 키워드: Deepfake Detection, Diffusion, GAN, Forensic Reliability, False Positive Rate, False Negative Rate, Human Review

### 12.6 연구문제

- RQ1. 딥페이크 탐지기의 in-domain 성능과 cross-domain 성능은 어떤 지표에서 차이를 보이는가?
- RQ2. FPR, FNR, AUROC, ECE는 딥페이크 탐지 신뢰성을 각각 어떻게 설명하는가?
- RQ3. Review-band triage는 자동판정률, 검토율, 자동판정 영역의 오류율을 어떻게 변화시키는가?

### 12.7 연구방법과 보안적 함의

문헌분석은 W06 논문 5편을 diffusion, video diffusion, GAN, deepfake creation/detection, reliability perspective로 비교한다. 위협모형은 synthetic media detector, forensic review workflow, detector score, 판단 로그, human review routing을 보호 자산으로 설정한다. 모의실험은 synthetic detector score 분포 기반 in-domain baseline, cross-domain reliability stress, review-band triage 조건을 평가한다.

보안적 함의는 integrity, safety, robustness, accountability, governance, reproducibility로 정리된다. 합성미디어는 허위증거와 판단 조작 위험을 만들며, false positive는 무고한 사람에게 피해를 줄 수 있고 false negative는 실제 조작물을 놓칠 수 있다.

### 12.8 KCI 제출 가능성 점검

표 6-1. KCI 제출 가능성 점검표

| 점검 항목 | 상태 |
|---|---|
| 국문·영문 제목 후보 작성 | 완료 |
| 국문초록 초안 작성 | 완료 |
| 영문초록 초안 작성 | 완료 |
| 키워드 작성 | 완료 |
| 연구문제 작성 | 완료 |
| 연구방법 작성 | 완료 |
| 표 1개 이상 포함 | 완료 |
| 그림 1개 이상 포함 | 완료 |
| 국내 참고문헌 3편 이상 | 확인 필요 |
| 해외 참고문헌 5편 이상 | W06 기준 완료, P02/P03 검증 필요 |
| AI 활용 고지 | 완료 |
| 실험 outputs 파일 존재 | 완료 |

## 13. SCI 논문 형식 전환

### 13.1 SCI 제목 후보

A Cross-Domain Reliability Evaluation Framework for Deepfake Detectors: Integrating FPR, FNR, Calibration, Review-Band Triage, and Reproducibility Evidence

### 13.2 Structured Abstract

Background: Diffusion models and GANs have advanced the quality of synthetic media, but generative quality and forensic detection reliability are fundamentally different evaluation problems.

Problem: Deepfake detectors often report high benchmark accuracy, but performance can degrade under unknown generators, compression, re-encoding, platform post-processing, and low-quality inputs.

Method: This study synthesizes five representative studies and uses a safe synthetic toy experiment to compare in-domain detector scores, cross-domain reliability stress, and review-band triage without generating real deepfakes or using personal data.

Results: The W06 toy experiment records perfect in-domain accuracy, degraded cross-domain accuracy and FNR under shifted score distributions, and improved automatic-decision reliability after routing uncertain samples to human review. These results should not be interpreted as real-world forensic performance.

Contribution: The main contribution is a reliability evaluation structure that separates accuracy, F1, FPR, FNR, AUROC, ECE, auto coverage, review rate, and reproducibility evidence for deepfake detector assessment.

Implications: The framework can be extended to real deepfake benchmarks, platform-specific media pipelines, human-in-the-loop forensic workflows, MLOps monitoring, and legal/ethical AI evidence review.

### 13.3 Introduction 구성

- Diffusion/GAN 기반 synthetic media의 발전
- 생성 품질과 탐지 신뢰성의 차이
- 딥페이크 탐지에서 FPR/FNR의 사회적·법적 위험
- Cross-domain reliability와 calibration 평가 필요성
- Human review routing의 필요성
- 본 연구의 contribution

### 13.4 Related Work 축

표 7. SCI Related Work 축

| 연구축 | 대표 논문 | 역할 |
|---|---|---|
| Diffusion models | Yang et al. | diffusion/score-based model과 조건부 생성 원리 |
| Video diffusion models | Högele et al. 또는 현재 P02 | temporal synthetic media와 video generation |
| GANs in computer vision | Wang et al. 또는 현재 P03 | GAN 생성 구조와 품질 지표 |
| Deepfake creation/detection | Mirsky and Lee | 딥페이크 위협모형과 탐지 기술 |
| Deepfake detection reliability | Tianyi Wang et al. | robustness, transferability, interpretability, reliability |

### 13.5 Threat Model

- Target system: synthetic media detector, deepfake forensic review workflow
- Protected assets: media evidence, detector score, threshold, model decision, review log, affected individuals
- Failure/adversary condition: unknown generator, compression, re-encoding, platform shift, low-quality input, adversarial post-processing
- Attack or failure success condition: false positive accusation, false negative missed detection, overconfident unreliable decision
- Defense/check: review-band triage, calibration check, cross-domain stress test
- Excluded scope: actual deepfake generation, personal data use, unauthorized service testing, operational attack execution

### 13.6 Methodology

Methodology는 literature matrix construction, reliability threat model design, synthetic score distribution experiment, in-domain detector baseline, cross-domain reliability stress, review-band triage evaluation, reproducibility evidence collection으로 구성한다.

### 13.7 Experimental Setup

표 7-1. SCI Experimental Setup

| Item | Description |
|---|---|
| Dataset | Synthetic real/fake detector score distributions |
| Detector | Threshold-based toy deepfake detector |
| In-domain score setting | real mean 0.22, fake mean 0.78, std 0.08 |
| Cross-domain score setting | real mean 0.34, fake mean 0.61, std 0.16 |
| Threshold | 0.50 |
| Review band | 0.40-0.60 |
| Metrics | Accuracy, F1, FPR, FNR, AUROC, ECE, auto coverage, review rate |
| Environment | Ubuntu 24.04 / Docker / Python 3.11 |
| Seed | 42 |
| Output files | `metrics_summary.csv`, `results.json`, `run_log.md` |

### 13.8 Results

Results는 표 5의 outputs 기준 수치를 사용한다. In-domain accuracy가 높아도 cross-domain reliability가 보장되지 않으며, review-band triage는 자동판정률을 낮추는 대신 위험한 자동판정을 줄인다.

### 13.9 Discussion

Discussion에서는 FPR과 FNR의 사회적 피해 차이, AUROC와 threshold 정책의 차이, ECE의 보조적 의미, human review routing의 책임 경계, synthetic score toy experiment의 외적 타당성 한계를 다룬다.

### 13.10 Limitations and Threats to Validity

- Internal validity: threshold-based toy detector는 실제 CNN/ViT/Transformer 기반 deepfake detector를 대표하지 않는다.
- External validity: synthetic score distributions는 실제 얼굴 영상, 압축, 플랫폼 후처리, unknown generator를 직접 반영하지 않는다.
- Construct validity: ECE, AUROC, FPR/FNR은 reliability의 일부만 설명하며 법적 증거능력은 별도 평가가 필요하다.
- Reproducibility: outputs 파일과 보고서 수치의 일치가 필요하다.
- Literature validity: P02/P03의 강의계획서 지정 논문 동일 여부 검증이 필요하다.

### 13.11 Conclusion

W06는 diffusion/GAN 생성모형과 딥페이크 탐지 신뢰성 평가를 분리한다. 핵심 결론은 benchmark accuracy 하나로 딥페이크 탐지기의 포렌식 신뢰성을 주장할 수 없으며, FPR, FNR, AUROC, ECE, auto coverage, review rate, reproducibility evidence를 함께 기록해야 한다는 것이다.

## 14. 발표용 요약

- 핵심 메시지: 생성 품질과 탐지 신뢰성은 다른 평가 문제다.
- 주요 문헌: P01-P03은 생성모형 원리, P04-P05는 deepfake threat/reliability를 담당한다.
- 실험 메시지: in-domain accuracy 1.000000은 cross-domain 안전성을 보장하지 않는다.
- 실험 수치: cross-domain accuracy 0.816667, FNR 0.200000, review-band auto coverage 0.641667, review rate 0.358333.
- 주의 문장: 이 결과는 synthetic detector score toy 실험의 평가 형식 검증용 수치이며, 실제 포렌식 성능 보증이 아니다.

## 15. 참고문헌 검증표

표 8. 참고문헌 검증표

| 번호 | 참고문헌 | DOI/URL | 상태 | 비고 |
|---|---|---|---|---|
| [1] | Ling Yang et al., Diffusion Models: A Comprehensive Survey of Methods and Applications | `10.1145/3626235` | 검증 | ACM Article 105 확인 |
| [2] | W06 P02, A Survey on Video Diffusion Models | `10.1145/3696415`, arXiv `2310.10647` | 부분 검증 | 강의계획서 지정 P02와 동일 여부, Article 번호 확인 필요 |
| [3] | W06 P03, Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy | `10.1145/3439723`, arXiv `1906.01529` | 부분 검증 | 강의계획서 저자명 차이 확인 필요 |
| [4] | Mirsky and Lee, The Creation and Detection of Deepfakes: A Survey | `10.1145/3425780` | 검증 | Article 번호 확인 필요 |
| [5] | Tianyi Wang et al., Deepfake Detection: A Comprehensive Survey from the Reliability Perspective | `10.1145/3699710` | 검증 | 강의계획서 `J. Wang et al.` 표기 확인 필요 |

## 16. 자기 점검표

표 9. 최종 자기 점검표

| 점검 항목 | 상태 | 비고 |
|---|---|---|
| 1장 한 문장 요약 작성 | 완료 |  |
| 2장 학습 배경과 주차 목표 작성 | 완료 |  |
| AI 원리 70% 정리 | 완료 |  |
| 보안 이슈 30% 정리 | 완료 |  |
| 논문 5편 요약 | 완료 |  |
| 논문 5편 비교표 보완 | 완료 / 확인 필요 | P02/P03 동일 여부 반영 |
| Research Track 5요소 작성 | 완료 | 연구문제, 위협모형, 평가방법, 재현성, 오픈문제 |
| P01 DOI/URL 검증 | 완료 |  |
| P02 지정 논문 동일 여부 검증 | 확인 필요 | ACM DOI는 확인, 강의계획서 표기 차이 |
| P03 지정 논문 동일 여부 검증 | 확인 필요 | ACM DOI는 확인, 강의계획서 저자명 차이 |
| P04 DOI/URL 검증 | 완료 | Article 번호 확인 필요 |
| P05 DOI/URL 검증 | 완료 | 강의계획서 `J. Wang et al.` 표기 확인 필요 |
| 실험 outputs 파일 존재 확인 | 완료 |  |
| 실험 결과와 보고서 수치 일치 | 완료 | outputs 기준 |
| KCI 논문 형식 전환 작성 | 완료 |  |
| SCI 논문 형식 전환 작성 | 완료 |  |
| 본문 인용과 참고문헌 대응 | 완료 / 확인 필요 | P02/P03 부분 검증 표시 |
| 표·그림 번호 정리 | 완료 | 표 1-9, 그림 1 |
| AI 활용 고지 작성 | 완료 | 별도 파일 보완 |
| PDF 저작권 위험 점검 | 완료 / 확인 필요 | PDF 5개 git 추적, 삭제는 미수행 |
| 최종 사람이 검토할 항목 표시 | 완료 | 최종 제출 확정 아님 |

<!-- formula-visual-supplement:start -->
## 수식·그래프·그림 보강

- 보강 일자: 2026-06-23
- 수식은 표준 정의식 또는 검증 가능한 평가식으로만 작성했다.
- 그래프는 `04_experiment/outputs/metrics_summary.csv`의 기존 수치만 사용했다.
- 다이어그램은 AI-assisted conceptual diagram이며 사실 자료나 실험 결과처럼 해석하지 않는다.

### 핵심 수식: Diffusion Forward Process와 Denoising Objective

$$
q(x_t|x_{t-1})=\mathcal{N}\left(\sqrt{1-\beta_t}x_{t-1},\beta_t I\right),
\qquad
\mathcal{L}_{simple}=\mathbb{E}_{t,x_0,\epsilon}\left[\lVert \epsilon-\epsilon_\theta(x_t,t)\rVert_2^2\right]
$$

| 기호 | 의미 |
|---|---|
| `x_t` | time step t의 noisy sample |
| `\beta_t` | noise schedule |
| `\epsilon` | 주입된 noise |
| `\epsilon_\theta` | denoising model prediction |

**직관적 의미:**  
Diffusion은 점진적으로 noise를 더하고 이를 되돌리는 학습 문제로 볼 수 있다.

**보안 관점 해석:**  
보안 발표에서는 생성 원리보다 탐지와 검증 지표를 중심에 둔다.

**평가 지표 연결:**  
AUROC, FPR, FNR, review_rate와 연결한다.

**한계와 가정:**  
표준식이며 특정 생성 모델의 원문 수치를 새로 주장하지 않는다.

### 핵심 수식: GAN Min-Max와 FPR/FNR

$$
\min_G\max_D\ \mathbb{E}_{x\sim p_{data}}\log D(x)+\mathbb{E}_{z\sim p_z}\log(1-D(G(z))),
\qquad
FPR=\frac{FP}{FP+TN},\quad FNR=\frac{FN}{FN+TP}
$$

| 기호 | 의미 |
|---|---|
| `G,D` | generator와 discriminator |
| `FP,FN` | 오탐과 미탐 |
| `TP,TN` | 정탐과 정상 판정 |
| `FPR,FNR` | 오탐률과 미탐률 |

**직관적 의미:**  
GAN 목적식은 생성자와 판별자의 경쟁을 표현한다. 탐지 평가는 판별 정확도보다 오탐·미탐의 균형이 중요하다.

**보안 관점 해석:**  
미탐은 악성 생성물을 놓칠 위험이고, 오탐은 정상 콘텐츠 차단 위험이다.

**평가 지표 연결:**  
false_positive_rate, false_negative_rate, AUROC, expected_calibration_error와 연결한다.

**한계와 가정:**  
detector toy evaluation이며 실제 미디어 판별 보증으로 해석하지 않는다.

### 표 수치 기반 그래프

![W06 metrics chart](../../09_presentation/assets/charts/w06_metrics_chart.png)

그래프는 deepfake detector의 accuracy, F1, FPR, FNR, AUROC를 조건별로 비교한다. 탐지 문제에서는 false positive와 false negative의 보안 비용이 다르므로 accuracy만으로 결론을 내리지 않는다. source는 `metrics_summary.csv`이다.

### Threat Model / Pipeline Diagram

![W06 pipeline diagram](../../09_presentation/assets/diagrams/w06_pipeline_diagram.svg)

이 다이어그램은 `generated-media detection pipeline`를 발표용으로 요약한 개념도다. 데이터 흐름, 평가 지표, 한계 표시는 `../../09_presentation/assets/figure_manifest.md`에도 기록했다.

### 확인 필요

- 생성 모델 수식은 표준 학습 목적 설명이며 deepfake 제작 절차를 안내하지 않는다.
- 논문별 원문 절·쪽·그림 번호는 최종 제출 전 사람 검토가 필요하다.
<!-- formula-visual-supplement:end -->
