# W02 논문 목록

> 최종 판정 우선: 이 문서의 현재 상태는 `논문/관련 논문 최종 반영표`를 우선한다. 상단의 제목·저자·로컬 PDF 차이 메모는 오류 판정이 아니라 검증 이력이며, `관련 논문 / 확인`은 주차 주제에 맞는 공식 확인 논문으로 사용한다.
>
> 2026-06-24 기준: `02_paper_summaries/P01_summary.md` ~ `P05_summary.md`는 100점형 구조로 보완 완료했다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성했다.

## 강의계획서 패킷 대조 결과

| ID | 강의계획서 지정 | 로컬 W02 정리본 | 대조 결과 |
|---|---|---|---|
| P01 | Bottou et al., "Optimization Methods for Large-Scale Machine Learning" | 동일 | 확인 완료 |
| P02 | Menghani, "Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better" | 동일 | ACM CSUR 최종판 확인 완료. 강의계획서의 `Gulzar Menghani` 표기는 출판 정보 기준 `Gaurav Menghani`로 정리 |
| P03 | Zhipeng Tian et al., "A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning" | Zhiyi Tian et al. | 출판 정보 기준 저자명은 `Zhiyi Tian` |
| P04 | Antonio Cina et al., "Training Data Poisoning Attacks and Defenses: A Systematic Review" | "Wild Patterns Reloaded: A Survey of Machine Learning Security against Training Data Poisoning" | 동일 저자군/주제의 ACM CSUR 논문은 확인됐으나, 강의계획서 지정 제목과 완전 동일한 제목의 출판판은 확인하지 못함. 현재 P04는 관련 논문/판본 차이 추가 확인 메모 문헌으로 표시 |
| P05 | Z. Jin et al., "A survey of backdoor attacks and defences: From deep neural networks to large language models" | Ling-Xin Jin et al. | 출판 정보 기준 제1저자 `Ling-Xin Jin`; 강의계획서 `Z. Jin` 표기는 약식 표기로 추정 |

## 최종 제출용 문헌 목록

| ID | 논문 제목 | 저자 | 연도 | 출처 | DOI/URL | 로컬 PDF | 확인 상태 |
|---|---|---|---:|---|---|---|---|
| P01 | Optimization Methods for Large-Scale Machine Learning | Leon Bottou, Frank E. Curtis, Jorge Nocedal | 2018 | SIAM Review, 60(2), 223-311 | `https://doi.org/10.1137/16M1080173` | `01_Bottou_Curtis_Nocedal_2018_Optimization_Methods_Large_Scale_ML.pdf` | DOI/권호/쪽 확인 완료. 100점형 summary 보완 완료 |
| P02 | Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better | Gaurav Menghani | 2023 | ACM Computing Surveys, 55(12), 1-37 | `https://doi.org/10.1145/3578938`; arXiv `https://arxiv.org/abs/2106.08962` | `02_Menghani_2023_Efficient_Deep_Learning_Survey.pdf` | ACM 최종판 DOI 확인 완료. 100점형 summary 보완 완료. Article 번호는 ACM 원문 페이지에서 최종 추가 확인 메모 |
| P03 | A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning | Zhiyi Tian, Lei Cui, Jie Liang, Shui Yu | 2022/2023 | ACM Computing Surveys, 55(8), 1-35 | `https://doi.org/10.1145/3551636` | `03_Tian_Cui_Liang_Yu_2023_Comprehensive_Poisoning_Survey.pdf` | DOI/저자명 확인 완료. 100점형 summary 보완 완료. 온라인/출판월 표기는 양식별 추가 확인 메모 |
| P04 | Wild Patterns Reloaded: A Survey of Machine Learning Security against Training Data Poisoning | Antonio Emanuele Cina, Kathrin Grosse, Ambra Demontis, Sebastiano Vascon, Werner Zellinger, Bernhard A. Moser, Alina Oprea, Battista Biggio, Marcello Pelillo, Fabio Roli | 2023 | ACM Computing Surveys, 55(13s), 1-39 | `https://doi.org/10.1145/3585385`; arXiv `https://arxiv.org/abs/2205.01992` | `04_Cina_et_al_2023_Wild_Patterns_Reloaded_Poisoning_Survey.pdf` | ACM DOI 확인 완료. 100점형 summary 보완 완료. 단, 강의계획서의 "Training Data Poisoning Attacks and Defenses: A Systematic Review"와 제목 표기 차이가 있어 관련 논문/판본 차이 추가 확인 메모 |
| P05 | A survey of backdoor attacks and defences: From deep neural networks to large language models | Ling-Xin Jin et al. | 2025 | Journal of Electronic Science and Technology, 23(3), Article 100326 | `https://doi.org/10.1016/j.jnlest.2025.100326` | `05_Jin_et_al_2025_Backdoor_Attacks_and_Defences_Survey.pdf` | DOI/저자명/학술지 확인 완료. 100점형 summary 보완 완료 |

## 100점형 summary 반영 상태

| ID | 보완 상태 | 추가된 핵심 요소 |
|---|---|---|
| P01 | 완료 | 기대위험, 경험위험, 오염 데이터 경험위험, SGD, mini-batch gradient, regularization, 최적화 기반 poisoning 해석 |
| P02 | 완료 | utility-cost score, compression ratio, security-efficiency score, latency/size/memory/energy, 보안-효율 trade-off |
| P03 | 완료 | poisoned ERM, poison rate, bilevel poisoning objective, clean accuracy-ASR 분리, poisoning taxonomy, defense metric |
| P04 | 완료 / 검증 필요 | training data poisoning threat model, targeted poisoning objective, stealthiness, defense FPR, provenance checklist |
| P05 | 완료 | backdoor trigger 함수, backdoor 학습 목적, ASR, utility drop, stealth risk, DNN-to-LLM hidden behavior 평가 |

## 작성 기준

- DOI는 Crossref/DOI content negotiation, 출판사 DOI URL, arXiv URL 중 확인 가능한 근거가 있는 경우에만 기록한다.
- P02의 최종 ACM판은 2023년 ACM Computing Surveys 판본을 우선 인용하고, arXiv는 보조 URL로 병기한다.
- P04는 현재 로컬 PDF와 DOI 기준으로는 "Wild Patterns Reloaded"가 ACM Computing Surveys 최종판이다. 강의계획서 지정 제목과 완전히 동일한 출판물은 확인하지 못했으므로 최종 제출 전 사람이 한 번 더 대조한다.
- 로컬 PDF 원문은 Git 추적 중이므로 public GitHub 공개 시 저작권 위험이 있다. 공개 저장소에는 원칙적으로 DOI/URL, 서지정보, 요약만 남긴다.

<!-- AUTO-RELATED-PAPER-REFLECTION:start -->
## 논문/관련 논문 최종 반영표

아래 표는 공식 DOI/arXiv 재검색 결과를 주차 보고서에 반영하기 위한 최종 판정이다. 기존 대조 기록은 보존하고, 보고서 본문과 참고문헌에서는 이 표의 `구분`과 `검증 상태`를 우선 사용한다.

| ID | 구분 | 논문 제목 | 논문 | 저자 | 연도 | 학술지/학회 | 학술지/출처 | DOI/URL | 검증 상태 | 보고서 반영 |
|---|---|---|---|---|---:|---|---|---|---|---|
| P01 | 논문 / 확인 | Optimization Methods for Large-Scale Machine Learning | Optimization Methods for Large-Scale Machine Learning | Leon Bottou, Frank E. Curtis, Jorge Nocedal | 2018 | SIAM Review | SIAM Review | `https://doi.org/10.1137/16M1080173` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P02 | 논문 / 확인 | Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better | Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better | Gaurav Menghani | 2023 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3578938` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P03 | 논문 / 확인 | A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning | A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning | Zhiyi Tian, Lei Cui, Jie Liang, Shui Yu | 2023 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3551636` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P04 | 관련 논문 / 확인 | Wild Patterns Reloaded: A Survey of Machine Learning Security against Training Data Poisoning | Wild Patterns Reloaded: A Survey of Machine Learning Security against Training Data Poisoning | Antonio Emanuele Cina et al. | 2023 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3585385` | 공식 DOI 확인. 강의계획서 지정 제목과 동일성 확인 필요 | 주차 주제 보강용 관련 논문으로 인용. 최종 제출 전 지정 논문 교체 여부 결정 |
| P05 | 논문 / 확인 | A survey of backdoor attacks and defences: From deep neural networks to large language models | A survey of backdoor attacks and defences: From deep neural networks to large language models | Ling-Xin Jin et al. | 2025 | Journal of Electronic Science and Technology | Journal of Electronic Science and Technology | `https://doi.org/10.1016/j.jnlest.2025.100326` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
<!-- AUTO-RELATED-PAPER-REFLECTION:end -->
