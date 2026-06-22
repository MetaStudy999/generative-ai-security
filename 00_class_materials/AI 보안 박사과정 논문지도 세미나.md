# AI 보안 박사과정 논문지도 세미나 강의계획서

> 원본: `AI 보안 박사과정 논문지도 세미나.pdf`  
> 형식: Markdown 정리본  
> 목적: 수업 운영, 주차별 학습, 논문 패킷, 발표·평가 기준, 실습 설계를 한 파일에서 확인할 수 있도록 재구성

---

## 1. 수업 개요

| 항목 | 내용 |
|---|---|
| 과목/세미나명 | AI 보안 박사과정 논문지도 세미나 |
| 수업 목표 | AI 보안 전공 박사과정생의 논문 기획–작성–투고–리비전 전 과정을 주간 SCI/SCIE 논문 기반 세미나 형태로 지도 |
| 지식 구성 | AI 기본 원리·이론 약 70% + 기술 의존 보안 이슈 약 30% |
| AI 원리·이론 | 모델, 학습, 일반화, 추론, 평가 프레임워크의 과학적 이해 |
| 보안 이슈 | 위협모형, 공격면, 방어, 검증, 운영 리스크 |
| 교수 프로필 표기 | 강장묵 교수 복수 박사 (공학:정보보호 2005, 정치학:정치법학 2009) |

본 수업은 최신 이론과 SCI/SCIE 논문을 바탕으로 다음 내용을 체계화한다.

- AI 학습이론, 모델링, 일반화, 최적화, 표현학습
- 대적(Adversarial) 위협
- 데이터 오염 및 모델 오염
- 프라이버시 공격
- 모델 도난
- 에이전트 및 프롬프트 취약성
- MLOps 공급망 리스크

---

## 2. 수업 형태 및 운영 방식

| 구분 | 내용 |
|---|---|
| 수업 형태 | 온라인 실시간 세미나(Zoom) |
| 운영 시간 | 매주 토요일 오후, 총 100분 |
| 전반 50분 | 교수 강의 및 핵심 정리 |
| 후반 50분 | 학생 발표, 토론, 리뷰 |
| 주교재 | 매주 제공되는 SCI/SCIE 해외저널 논문 5편 |

### 2.1 Zoom 참여 규정

| 규정 | 내용 |
|---|---|
| 카메라 ON | 모든 수강생은 수업 중 카메라를 항상 켠다. |
| 마이크 OFF | 기본은 마이크 OFF이며, 발표·질의 시에만 ON으로 전환한다. |
| 통신 환경 | 안정적인 인터넷 환경을 확보한다. |

---

## 3. 학습활동 2-트랙 운영

### 3.1 논문 트랙: Research Track

매주 5편의 논문을 기반으로 다음 항목을 구조화한다.

| 분석 항목 | 영문 표현 | 핵심 질문 |
|---|---|---|
| 연구문제 | Problem formulation | 이 논문은 어떤 문제를 해결하려 하는가? |
| 위협모형 | Threat model | 공격자, 자산, 공격면, 방어자는 어떻게 정의되는가? |
| 평가방법 | Evaluation protocol | 데이터셋, 지표, 비교대상, 실험조건은 타당한가? |
| 재현성 | Reproducibility | 코드, 데이터, 환경, seed, 하이퍼파라미터가 충분히 공개되는가? |
| 한계/오픈문제 | Open problems | 논문의 한계와 후속 연구 기회는 무엇인가? |

### 3.2 AI 도구 트랙: Tool Track

모든 수강생은 유료 버전 AI 도구를 최소 1개 이상 구독·사용한다. 범주는 제한하지 않는다.

예시 범주:

- 텍스트 LLM
- 멀티모달 생성 도구
- 에이전트형 개발도구/IDE
- 비디오 생성 도구
- 데이터 분석 자동화 도구
- 논문 작성 보조 도구
- 실험 자동화 도구

학생은 자신의 사용 경험(Worklog) 또는 AI를 활용해 획득한 지식·성과를 발표하여 집단 지식에 기여한다.

예시 발표 주제:

- KCI/SCIE 논문 초안 작성 과정
- 연구주제 도출 과정
- 실험 자동화 과정
- 동영상 제작 과정
- 에이전트 파이프라인 구축 과정

### 3.3 문의 및 연락

| 항목 | 내용 |
|---|---|
| 보고서/과제 제출 이메일 | 별도 공지 |
| 수업 운영·평가 관련 문의 | 수업 종료 후 이메일 접수 |
| 연락처 | mooknc@naver.co / honukang@gmail.com |

---

## 4. 평가 및 성적 처리 기준

### 4.1 평가 방식

평가는 발표 기반(peer scoring 중심)으로 운영한다.

| 구분 | 내용 |
|---|---|
| 발표 점수 산정 | 실제 수업에 참여한 학생에 한하여 발표 종료 후 각 수강생이 발표 점수를 과대(반장)에게 제출 |
| 점수 취합 | 과대가 제출 점수를 종합·정규화·요약통계 처리 후 담당교수에게 익명 전달 |
| 익명성 | 개별 채점자의 식별정보는 전달하지 않음 |
| 성적 부여 | 발표 점수 분포에 따라 A+ ~ F 부여 |
| 일반 운영 기준 | 일반적으로 C+ ~ B 범위를 중심으로 처리하되, 학습활동·발표수준·특이사정 등을 반영 가능 |
| 특이사정 | 장기질병, 불가항력적 시간충돌 등은 조정 가능 |

### 4.2 불이익 및 가산점

| 구분 | 내용 |
|---|---|
| 발표 미수행 | 발표를 하지 않거나 하지 못하는 경우 불이익 발생 가능: 하위등급 처리, 추가구제기회 제한 등 |
| 수업운영 지원 | 과대 등 수업운영을 자진 지원하는 경우 가산점 일부 부여 가능 |
| 지원 예시 | 채점 취합, 자료공유 지원, 세미나 진행 보조 |

### 4.3 이의 제기 정책

- 운영상의 문의·이의는 수업 종료 후 이메일로 접수한다.
- 성적 처리 완료 및 확정 이후에는 해당 기준에 대한 이의를 받지 않는다.
- 발표 리스트는 발표자, 주제, 도구를 포함하여 확정·공유한다.

---

## 5. 주차별 강의 구성 개요

각 주차는 다음 비율로 설계된다.

| 구성 | 비율 | 내용 |
|---|---:|---|
| AI 원리 | 70% | 모델, 학습, 일반화, 추론, 평가 프레임워크의 과학적 이해 |
| 보안 이슈 | 30% | 위협모형, 공격면, 방어, 검증, 운영 리스크 |

### 5.1 주차 블록

| 주차 | 핵심 영역 |
|---|---|
| Week 1–3 | 딥러닝 기초, 최적화, 컴퓨터비전 |
| Week 4–6 | Transformer, 자기지도학습, 생성모형 |
| Week 7–9 | LLM, RAG, 심층강화학습 |
| Week 10–12 | 연합학습, 차등프라이버시, 신경망 검증 |
| Week 13–15 | 모델 지식재산 보호, MLOps, 연구평가·재현성·XAI |

---

# 6. 주차별 세부 강의계획 및 SCI/SCIE 논문 패킷

## Week 1. 딥러닝 패러다임 & ML 보안 분류학

| 구분 | 내용 |
|---|---|
| AI 원리 | 딥러닝 패러다임, 학습–일반화–표현의 기초 정식화 |
| 보안 이슈 | ML 시스템 생명주기 관점의 보증(assurance)·위협모형, 대적 ML·프라이버시 공격의 분류학 |
| 학습목표 1 | DL 핵심 구성요소를 공통 언어로 정리 |
| 학습목표 2 | ML lifecycle assurance desiderata 정의 |
| 학습목표 3 | 대적·프라이버시 공격 분류학을 연구지도 템플릿으로 고정 |

### 논문 패킷

1. Yann LeCun et al., “Deep learning”, *Nature*, 521(7553), 2015, pp. 436–444. DOI
2. Rob Ashmore et al., “Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges”, *ACM Computing Surveys*, 54(5), 2021, Article 111. DOI
3. Anna L. Buczak et al., “A Survey of Data Mining and Machine Learning Methods for Cyber Security Intrusion Detection”, *IEEE Communications Surveys & Tutorials*, 18(2), 2016, pp. 1153–1176. DOI
4. Y. Wang et al., “Adversarial Attacks and Defenses in Machine Learning: A Survey”, *IEEE Communications Surveys & Tutorials*, 25(4), 2023, pp. 2245–2298. DOI
5. Maria Rigaki et al., “A Survey of Privacy Attacks in Machine Learning”, *ACM Computing Surveys*, 56(4), 2023, Article 101. DOI

---

## Week 2. 대규모 최적화 & 데이터 오염 위협

| 구분 | 내용 |
|---|---|
| AI 원리 | 대규모 최적화(First/Second-order), 효율적 학습(압축·경량화)과 일반화 |
| 보안 이슈 | 데이터 오염(poisoning)·훈련데이터 조작의 위협모형·평가규약 |
| 학습목표 1 | 최적화–일반화의 병목 정량화 |
| 학습목표 2 | 효율화 기법의 정확도–비용 트레이드오프 분석 |
| 학습목표 3 | poisoning/backdoor의 공격자 비용모형과 방어평가 설계 |

### 논문 패킷

1. Léon Bottou et al., “Optimization Methods for Large-Scale Machine Learning”, *SIAM Review*, 60(2), 2018, pp. 223–311. DOI
2. Gulzar Menghani, “Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better”, *ACM Computing Surveys*, 55(12), 2023, Article 257. DOI
3. Zhipeng Tian et al., “A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning”, *ACM Computing Surveys*, 55(8), 2022, Article 167. DOI
4. Antonio Cinà et al., “Training Data Poisoning Attacks and Defenses: A Systematic Review”, *ACM Computing Surveys*, 56(2), 2023, Article 34. DOI
5. Z. Jin et al., “A survey of backdoor attacks and defences: From deep neural networks to large language models”, *Journal of Electronic Science and Technology*, 23(1), 2025, Article 100326. DOI

---

## Week 3. 컴퓨터비전 표현학습 & 비전 대적공격

| 구분 | 내용 |
|---|---|
| AI 원리 | 컴퓨터비전 표현학습(CNN→ViT), 멀티모달 정합(공간·언어 임베딩) |
| 보안 이슈 | 비전 기반 대적공격(white-box/black-box), 2D/3D 안전성·강건성(robustness) 평가 |
| 학습목표 1 | 비전 학습의 귀납편향(inductive bias) 해부 |
| 학습목표 2 | 멀티모달 Transformer의 구조·학습규약 정리 |
| 학습목표 3 | 비전 대적평가 벤치마크/지표를 논문 레벨로 재구성 |

### 논문 패킷

1. Yann LeCun et al., “Gradient-Based Learning Applied to Document Recognition”, *Proceedings of the IEEE*, 86(11), 1998, pp. 2278–2324. DOI
2. Apostolos Voulodimos et al., “Deep Learning for Computer Vision: A Brief Review”, *Computational Intelligence and Neuroscience*, 2018, Article 7068349. DOI
3. Y. Xu et al., “Multimodal Learning With Transformers: A Survey”, *IEEE TPAMI*, 45(10), 2023, pp. 12113–12132. DOI
4. Salman Khan et al., “Transformers in Vision: A Survey”, *ACM Computing Surveys*, 54(10s), 2022, Article 200. DOI
5. Z. Li et al., “A Survey of Robustness and Safety of 2D and 3D Deep Learning Models Against Adversarial Attacks”, *ACM Computing Surveys*, 56(5), 2023, Article 117. DOI

---

## Week 4. Transformer 변형 & NLP 대적공격·프라이버시

| 구분 | 내용 |
|---|---|
| AI 원리 | Transformer 변형(X-formers)과 효율화: 근사주의, 저랭크, 커널화, 스파스 어텐션 |
| 보안 이슈 | NLP 대적공격/방어, 프롬프트·ICL(in-context learning) 환경의 프라이버시 위험 |
| 학습목표 1 | 어텐션 복잡도 병목의 수학적 해소기법 비교 |
| 학습목표 2 | NLP 강건성의 공격면–방어면 매핑 |
| 학습목표 3 | 프롬프트 입력, 특히 민감정보 보호기법의 평가항목 정의 |

### 논문 패킷

1. Yi Tay et al., “Efficient Transformers: A Survey”, *ACM Computing Surveys*, 55(6), 2022, Article 109. DOI
2. Quentin Fournier et al., “A Practical Survey on Faster and Lighter Transformers”, *ACM Computing Surveys*, 55(14s), 2023, Article 304. DOI
3. Tianyang Lin et al., “A survey of transformers”, *AI Open*, 3(1), 2022, pp. 111–132. DOI
4. N. Goyal et al., “A Survey on Adversarial Defenses and Robustness in NLP”, *ACM Computing Surveys*, 56(3), 2023, Article 62. DOI
5. Kennedy Edemacu et al., “Privacy Preserving Prompt Engineering: A Survey”, *ACM Computing Surveys*, 57(10), 2025, Article 255. DOI

---

## Week 5. 자기지도학습·파운데이션 모델 & Poisoning/Backdoor

| 구분 | 내용 |
|---|---|
| AI 원리 | 자기지도학습(Self-Supervised Learning)·표현학습·파운데이션 모델의 사전학습 규약 |
| 보안 이슈 | 표현학습 단계에서의 poisoning/backdoor 삽입, 벤치마크 데이터 거버넌스와 탐지 |
| 학습목표 1 | SSL 표준 문제정의: contrastive/masked/predictive 정리 |
| 학습목표 2 | 비디오 SSL의 사전학습–전이학습 평가 |
| 학습목표 3 | poisoning/backdoor가 representation space에 미치는 영향 측정 |

### 논문 패킷

1. Yan Gui et al., “Self-Supervised Learning: Algorithms, Applications, and Future Trends”, *IEEE TPAMI*, 46(11), 2024, pp. 9052–9071. DOI
2. H. Ren et al., “A Comprehensive Survey on Self-Supervised Learning”, *ACM Computing Surveys*, 58(1), 2025, Article 22. DOI
3. Madeline Schiappa et al., “Self-Supervised Learning of Video Representations: A Survey”, *ACM Computing Surveys*, 55(13s), 2023, Article 278. DOI
4. Y. Wang et al., “A Survey of Poisoning Attacks and Defenses on Machine Learning”, *ACM Computing Surveys*, 55(3), 2022, Article 50. DOI
5. Z. Jin et al., “A survey of backdoor attacks and defences: From deep neural networks to large language models”, *Journal of Electronic Science and Technology*, 23(1), 2025, Article 100326. DOI

---

## Week 6. 확률생성모형(Diffusion/GAN) & 딥페이크 검출

| 구분 | 내용 |
|---|---|
| AI 원리 | 확률생성모형(Score-based/Diffusion, GAN)과 샘플링·조건부 생성 |
| 보안 이슈 | 합성미디어(딥페이크) 공격면, 검출·신뢰성(reliability)·포렌식 관점의 평가 |
| 학습목표 1 | diffusion의 수학적 정식화와 샘플링 알고리즘 비교 |
| 학습목표 2 | GAN 기반 생성과 위협모형 연결 |
| 학습목표 3 | deepfake 검출의 데이터편향·일반화·신뢰성 지표 설계 |

### 논문 패킷

1. Ling Yang et al., “Diffusion Models: A Comprehensive Survey of Methods and Applications”, *ACM Computing Surveys*, 56(3), 2023, Article 65. DOI
2. Ananya Högele et al., “Video Diffusion Models: A Survey”, *ACM Computing Surveys*, 56(9), 2024, Article 209. DOI
3. Tianqi Wang et al., “Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy”, *ACM Computing Surveys*, 54(2), 2021, Article 38. DOI
4. Yisroel Mirsky et al., “The Creation and Detection of Deepfakes: A Survey”, *ACM Computing Surveys*, 54(1), 2021, Article 7. DOI
5. J. Wang et al., “Deepfake Detection: A Comprehensive Survey from the Reliability Perspective”, *ACM Computing Surveys*, 57(2), 2024, Article 43. DOI

---

## Week 7. LLM 학습·정렬·평가 & LLM 보안·프라이버시

| 구분 | 내용 |
|---|---|
| AI 원리 | 대규모 언어모델(LLM) 학습·추론·정렬(alignment)·평가(evaluation) 프레임워크 |
| 보안 이슈 | LLM 보안·프라이버시: 데이터 추출, 프롬프트 기반 공격, 소프트웨어 보안 접점 |
| 학습목표 1 | LLM 평가 프로토콜: 벤치마크, 오염, 재현성 체계화 |
| 학습목표 2 | LLM 보안·프라이버시 위협면 지도화 |
| 학습목표 3 | 소프트웨어 보안–LLM 인터페이스에서의 공격표면 정의 |

### 논문 패킷

1. J. Chang et al., “A Survey on Evaluation of Large Language Models”, *ACM Computing Surveys*, 56(12), 2024, Article 253. DOI
2. Ankur Das et al., “Security and Privacy Challenges of Large Language Models: A Survey”, *ACM Computing Surveys*, 57(9), 2025, Article 203. DOI
3. Mingzhe Yao et al., “A survey on large language model security and privacy: problems, methods, and opportunities”, *AI Open*, 2024(4), 2024. DOI
4. Yongtao Yin et al., “A survey on multimodal large language models”, *National Science Review*, 11(12), 2024, Article nwae403. DOI
5. Shujun Li et al., “When Software Security Meets Large Language Models: A Survey”, *IEEE/CAA Journal of Automatica Sinica*, 12(1), 2025. DOI

---

## Week 8. RAG·프롬프팅 프레임워크 & 프롬프트 인젝션

| 구분 | 내용 |
|---|---|
| AI 원리 | Retrieval-Augmented Generation(RAG), 그래프 기반 RAG, 프롬프팅 프레임워크 |
| 보안 이슈 | 프롬프트 인젝션(prompt injection), 간접 인젝션, 의료/안전영역의 취약성, 에이전트형 파이프라인 공격면 |
| 학습목표 1 | RAG의 추론경로: 검색–재순위–생성 구조 해부 |
| 학습목표 2 | 프롬프팅 구성요소와 공격면 일치화 |
| 학습목표 3 | prompt injection의 근본원인(root cause)과 방어정책 설계 |

### 논문 패킷

1. Shiyu Chen et al., “Graph Retrieval-Augmented Generation: A Survey”, *ACM Computing Surveys*, 2025(in press). DOI
2. Jianxiang Li et al., “Graph-Based Approaches and Functionalities in Retrieval-Augmented Generation: A Survey”, *ACM Computing Surveys*, 2026(in press). DOI
3. X. Liu et al., “Prompting Frameworks for Large Language Models”, *ACM Computing Surveys*, 2026(in press). DOI
4. Tianlei Geng et al., “Prompt Injection Attacks on Large Language Models: A Survey of Attack Methods, Root Causes, and Defense Strategies”, *Computers, Materials & Continua*, 82(2), 2026, pp. 3785–3826. DOI
5. P. Lee et al., “Generative Artificial Intelligence and Prompt Injection Vulnerability in Drug Information Provision by Large Language Models”, *JAMA Network Open*, 8(4), 2025, e2512796. DOI

---

## Week 9. 심층강화학습(DRL) & 사이버보안 적용·보상조작

| 구분 | 내용 |
|---|---|
| AI 원리 | 심층강화학습(DRL) 알고리즘 계통: DQN, Policy gradient, Actor-Critic, 검증·안전성 |
| 보안 이슈 | 사이버보안 적용(DRL for cyber defense), 보상조작(reward manipulation), 모델 취약성 |
| 학습목표 1 | DRL 핵심 메커니즘을 수학적 관점으로 재정렬 |
| 학습목표 2 | 사이버 도메인에서의 상태·행동·보상 설계 |
| 학습목표 3 | DRL 검증/테스팅 기법을 논문 평가체계로 정형화 |

### 논문 패킷

1. Kai Arulkumaran et al., “Deep Reinforcement Learning: A Brief Survey”, *IEEE Signal Processing Magazine*, 34(6), 2017, pp. 26–38. DOI
2. B. R. Kiran et al., “Deep Reinforcement Learning for Autonomous Driving: A Survey”, *IEEE TITS*, 23(6), 2022, pp. 4909–4926. DOI
3. Ngoc-Tinh Nguyen et al., “Deep Reinforcement Learning for Cyber Security”, *IEEE TNNLS*, 34(8), 2023, pp. 3779–3795. DOI
4. Aditya Adawadkar et al., “Cyber-security and reinforcement learning — A brief survey”, *Engineering Applications of Artificial Intelligence*, 114, 2022, Article 105116. DOI
5. H. Yan et al., “Deep Reinforcement Learning Verification: A Survey”, *ACM Computing Surveys*, 56(2), 2023, Article 27. DOI

---

## Week 10. 연합학습(FL) & FL 위협·방어·정책

| 구분 | 내용 |
|---|---|
| AI 원리 | 연합학습(Federated Learning), 집계(Aggregation), 개인화(Personalization), 강건성 |
| 보안 이슈 | FL 위협: gradient leakage, poisoning, backdoor, privacy attacks, 방어, 정책 |
| 학습목표 1 | FL 구성요소: 클라이언트, 서버, 집계, 통신 분해 |
| 학습목표 2 | 공격–방어–비용 트레이드오프 모델링 |
| 학습목표 3 | FL 프라이버시 공격과 정책경관 연결 |

### 논문 패킷

1. M. Arbaoui et al., “Federated Learning Survey: A Multi-Level Taxonomy of Aggregation Techniques, Experimental Insights and Future Frontiers”, *ACM Computing Surveys*, 57(2), 2024. DOI
2. Viraaji Mothukuri et al., “A survey on security and privacy of federated learning”, *Future Generation Computer Systems*, 115, 2021, pp. 619–640. DOI
3. Nuria Rodríguez-Barroso et al., “Survey on federated learning threats: Concepts, taxonomy on attacks and defences, experimental study and challenges”, *Information Fusion*, 90, 2023, pp. 148–173. DOI
4. J. Zhao et al., “A Survey of Federated Learning Privacy Attacks, Defenses, Applications, and Policy Landscape”, *ACM Computing Surveys*, 57(9), 2025, Article 230. DOI
5. T. D. Nguyen et al., “Backdoor attacks and defenses in federated learning: Survey, challenges and future research directions”, *Engineering Applications of Artificial Intelligence*, 127, 2024, Article 107166. DOI

---

## Week 11. 차등프라이버시(DP) & 멤버십 추론 공격·방어

| 구분 | 내용 |
|---|---|
| AI 원리 | 차등프라이버시(Differential Privacy), 예산(privacy budget), DP-SGD, 프라이버시 회계(accounting) |
| 보안 이슈 | 멤버십 추론(membership inference), 방어기법, 연합학습/LLM 환경에서의 실무적 한계 |
| 학습목표 1 | DP의 수학적 정의와 실무 오해(misuse) 정리 |
| 학습목표 2 | MI 공격과 방어를 threat model로 분해 |
| 학습목표 3 | DP–효용–학습안정성 트레이드오프를 실험설계로 연결 |

### 논문 패킷

1. Alberto Blanco-Justicia et al., “A Critical Review on the Use (and Misuse) of Differential Privacy in Machine Learning”, *ACM Computing Surveys*, 55(8), 2022, Article 166. DOI
2. Jonathan Demelius et al., “Differential Privacy in Centralized Deep Learning: A Survey”, *ACM Computing Surveys*, 57(9), 2025, Article 202. DOI
3. Zizheng Pan et al., “Differential Privacy in Deep Learning: A Literature Survey”, *Neurocomputing*, 2024, Article 128346. DOI
4. Hongsheng Hu et al., “Membership inference attacks on machine learning: a survey”, *ACM Computing Surveys*, 54(11s), 2022, Article 235. DOI
5. Hongsheng Hu et al., “Defenses to Membership Inference Attacks: A Survey”, *ACM Computing Surveys*, 56(7), 2023, Article 144. DOI

---

## Week 12. 신경망 검증·정형방법 & 대적방어·XAI·강건성 트레이드오프

| 구분 | 내용 |
|---|---|
| AI 원리 | 신경망 검증(verification), 추상화(abstraction), 정형방법(formal methods), 강건성 증명 |
| 보안 이슈 | 대적공격의 체계적 방어, XAI 공격면, 강건성–정확도–공정성(trade-off) 최소화 전략 |
| 학습목표 1 | 검증 프레임워크의 가정/완전성/스케일링 병목 해부 |
| 학습목표 2 | 공격–방어–설명가능성의 결합 위협면 모델링 |
| 학습목표 3 | 강건성 트레이드오프를 논문 기여로 전환: 새 지표/새 설정 |

### 논문 패킷

1. Boudardara et al., “A Review of Abstraction Methods Toward Verifying Neural Networks”, *ACM Computing Surveys*, 56(7), 2024, Article 151. DOI
2. Sen Zhou et al., “Adversarial Attacks and Defenses in Deep Learning”, *ACM Computing Surveys*, 55(3), 2022, Article 60. DOI
3. G. Vadillo et al., “Adversarial machine learning attacks against explainable artificial intelligence: A review”, *WIREs Data Mining and Knowledge Discovery*, 15(3), 2025, e1567. DOI
4. Inaki Pérez et al., “Adversarial Robustness of Neural Networks from Lipschitz Regularization: A Survey”, *ACM Computing Surveys*, 56(9), 2024, Article 197. DOI
5. Chih-Hsiang Cheng et al., “The Triangular Trade-off between Robustness, Accuracy, and Fairness”, *ACM Computing Surveys*, 56(10), 2024, Article 214. DOI

---

## Week 13. 모델 지식재산(IP)·모델 도난·모델 추출 위협

| 구분 | 내용 |
|---|---|
| AI 원리 | 모델 지식재산(IP), 모델 도난(model stealing), 모델 추출(model extraction) 위협 |
| 보안 이슈 | 워터마킹/핑거프린팅, 방어가 성능·품질·유틸리티에 미치는 영향 평가 |
| 학습목표 1 | 공개 API/배포 모델의 경제적·기술적 위협 정식화 |
| 학습목표 2 | 워터마킹을 실험설계: 탐지율, 위양성, 품질저하로 재정의 |
| 학습목표 3 | 생성모형(GAN/LLM)에서의 방어가능성 검토 |

### 논문 패킷

1. Daria Oliynyk et al., “I Know What You Trained Last Summer: A Survey on Stealing Machine Learning Models and Defences”, *ACM Computing Surveys*, 56(1), 2023-06-01, Article 7, 35 pages. https://doi.org/10.1145/3595292
2. Y. Ye et al., “A Survey of Watermarking and Fingerprinting Techniques for Deep Learning Models”, *ACM Computing Surveys*, 2024(??), Article TBD. https://doi.org/10.1145/3773028
3. Feng Li et al., “Deep neural network watermarking: Techniques and challenges”, *Neurocomputing*, 461, 2021-11-01, pp. 171–193. https://doi.org/10.1016/j.neucom.2021.07.051
4. Kaiyi Pang et al., “ModelShield: Adaptive and Robust Watermark Against Model Extraction Attack”, *IEEE Transactions on Information Forensics and Security*, 20, 2025-01-01, pp. 1767–1780. https://doi.org/10.1109/TIFS.2025.3530691
5. Cheng Zhang et al., “Generative Adversarial Networks: A Survey on Attack and Defense”, *ACM Computing Surveys*, 56(4), 2023-11-10, Article 91, pp. 1–35. https://doi.org/10.1145/3615336

---

## Week 14. MLOps/DevOps·데이터/모델 파이프라인·모니터링·드리프트·사고대응

| 구분 | 내용 |
|---|---|
| AI 원리 | MLOps/DevOps, 데이터/모델 파이프라인, 모니터링, 드리프트, 사고대응 |
| 보안 이슈 | ML 공급망(supply chain), 운영환경 공격면: 모델 배포/업데이트/로그, 보증사례(assurance case) 작성 |
| 학습목표 1 | 연구용 실험과 운영용 ML 시스템의 평가격차 해소 |
| 학습목표 2 | MLOps 실천항목을 보안통제항목으로 매핑 |
| 학습목표 3 | 논문(학술)과 운영(산업) 레이어의 정합을 학위논문 기여로 정의 |

### 논문 패킷

1. Bayram Eken et al., “A Multivocal Literature Review of MLOps Practices: Emerging Trends, Challenges, and Research Directions”, *ACM Computing Surveys*, 57(7), 2025-05-01, Article 162, 35 pages. https://doi.org/10.1145/3747346
2. Andrei Paleyes et al., “Challenges in Deploying Machine Learning: A Survey of Case Studies”, *ACM Computing Surveys*, 55(13s), 2022-07-01, Article 274, 29 pages. https://doi.org/10.1145/3533378
3. Daniel Diaz-de-Arcaya et al., “A Systematic Survey on MLOps and AIOps: Taxonomy, Challenges, and Future Directions”, *ACM Computing Surveys*, 57(1), 2023-11-01, Article 17, 36 pages. https://doi.org/10.1145/3625289
4. J. Chen et al., “Deep Learning with Edge Computing: A Review”, *Proceedings of the IEEE*, 107(8), 2019-08-01, pp. 1655–1674. https://doi.org/10.1109/JPROC.2019.2921977
5. Xiang Chen et al., “Deep Learning for Software Engineering: A Survey”, *ACM Computing Surveys*, 54(8), 2022-01-01, Article 151, 36 pages. https://doi.org/10.1145/3505243

---

## Week 15. 연구평가·재현성·설명가능성(XAI)·논문 구성

| 구분 | 내용 |
|---|---|
| AI 원리 | 연구평가(evaluation), 재현성, 설명가능성(XAI), 논문 구성: 기여/한계/리비전 전략 |
| 보안 이슈 | 평가 오염(benchmark contamination), 모델 유출, 정책/윤리를 포함한 종합 리스크 |
| 학습목표 1 | 박사논문/저널 논문 평가항목을 체크리스트화 |
| 학습목표 2 | XAI를 보안 관점: 공격/오용으로 재해석 |
| 학습목표 3 | 학기 종료 시점에 각자의 논문 기여(Contribution)를 1–2문장으로 고정 |

### 논문 패킷

1. J. Chang et al., “A Survey on Evaluation of Large Language Models”, *ACM Computing Surveys*, 56(12), 2024-08-01, Article 253, 42 pages. https://doi.org/10.1145/3641289
2. R. Ashmore et al., “Assuring the Machine Learning Lifecycle: Desiderata, Methods, and Challenges”, *ACM Computing Surveys*, 54(5), 2021-05-01, Article 111, pp. 1–39. https://doi.org/10.1145/3453444
3. Vivek Dwivedi et al., “Explainable AI: Core Ideas, Techniques, and Solutions”, *ACM Computing Surveys*, 56(9), 2023-04-01, Article 175, 39 pages. https://doi.org/10.1145/3561048
4. A. B. Arrieta et al., “Explainable Artificial Intelligence (XAI): Concepts, Taxonomies, Opportunities and Challenges toward Responsible AI”, *Information Fusion*, 58, 2020-06-01, pp. 82–115. https://doi.org/10.1016/j.inffus.2019.12.012
5. K. D. et al., “Concept-based Explainable Artificial Intelligence: A Survey”, *ACM Computing Surveys*, 2025(in press). https://doi.org/10.1145/3774643

---

# 7. PPT 구성안

PPT는 “정책(운영/평가)”과 “주차별 목차”를 중심으로 `1슬라이드 = 1메시지` 구조로 작성한다. 권장 분량은 20–30장이다.

| 구성 | 내용 |
|---|---|
| 표지 | 과목명, 교수 프로필, 운영형태: 토요일·100분·온라인 |
| 운영 규정 | Zoom 참여규정: 카메라 ON, 마이크 OFF, 토론 규칙 |
| 교재/보조교재 | 매주 SCI/SCIE 논문 5편, 유료 AI 도구 구독 의무 |
| 평가 | 발표 중심, 익명 집계, 가산점, 불이익, 이의정책, 연락처 |
| 주차별 목차 | Week 1~15: 각 주차 1장, AI 원리 70%, 보안 이슈 30%, 논문패킷 5편 |
| 부록 | 모의실험 결과 요약, 연구기여 포인트 표 |

---

# 8. 모의실험 기반 실습 설계

## 8.1 실습 기준

본 강의의 실습은 “학술 논문 재현성”을 핵심 기준으로 설계한다. 최소 재현 실험은 공개 데이터와 공개 라이브러리만으로 구성한다.

## 8.2 예시 오픈데이터

| 항목 | 내용 |
|---|---|
| 데이터셋 | UCI Optical Recognition of Handwritten Digits |
| 설명 | 8×8 표현 및 전처리 설명 포함 |
| URL | https://archive.ics.uci.edu/ml/datasets/optical+recognition+of+handwritten+digits |

## 8.3 최소 재현 파이프라인

실습용 최소 재현 파이프라인은 scikit-learn의 `load_digits()`로 즉시 구동 가능하다.

| 항목 | 내용 |
|---|---|
| 샘플 수 | 총 1,797개 |
| 입력 형태 | 8×8 이미지 = 64차원 |
| 픽셀값 | 0–16 |
| 예시 모델 | 로지스틱 회귀 기반 분류기 |

---

# 9. 모의실험 결과: 데이터오염 및 백도어 삽입

동일 데이터/모델에서 데이터오염(poisoning) 및 백도어(backdoor) 삽입의 효과를 수치로 확인하기 위한 모의실험 결과이다.

## 9.1 라벨 플리핑(label-flipping) 오염

| 조건 | 설명 | 클린 데이터 테스트 정확도 |
|---|---|---:|
| 정상 학습 | 오염 없음 | 0.9778 |
| 5% 오염 | 라벨 플리핑 5% 적용 | 0.9267 |
| 10% 오염 | 라벨 플리핑 10% 적용 | 0.9000 |
| 20% 오염 | 라벨 플리핑 20% 적용 | 0.8933 |

## 9.2 백도어 공격 결과

| 항목 | 조건/설명 | 결과 |
|---|---|---:|
| 트리거 | 하단 우측 2×2 픽셀 고정 | - |
| 타깃 라벨 | 0 | - |
| 중독 비율 | 훈련데이터 5% 중독 | - |
| 클린 테스트 정확도 | 거의 유지됨(stealth) | 0.9756 |
| 공격 성공률(ASR) | 트리거 삽입 샘플 대상 | 0.9531 |

### 해석

- 클린 정확도 저하가 작아도 백도어 stealth가 유지될 수 있다.
- 트리거 조건부 오분류는 매우 크게 나타날 수 있다.
- 공격/방어 실험 설계 시 다음 세 지표를 함께 보고해야 한다.
  - 클린 성능
  - 공격 성공률(ASR)
  - 탐지회피성(stealth)

---

# 10. 실습 소프트웨어 개발 절차

실습용 소프트웨어는 요구사항–아키텍처–모듈화–테스트–재현성 패키징 순서로 개발한다. 권장 방식은 반복적 증분개발이다.

## 10.1 기능·모듈 분해

| 모듈 | 역할 |
|---|---|
| DataModule | 데이터 로딩, 전처리, 분할, 시드 고정, 메타데이터 기록 |
| ModelModule | 모델 정의: 선형/심층, 학습루프, 체크포인트, 하이퍼파라미터 관리 |
| AttackModule | label-flip poisoning, backdoor trigger injection, 선택적으로 adversarial example 생성 |
| DefenseModule | 데이터 정제, 이상치 탐지, 강건 학습: 정규화, 앙상블, 트리거 스캐닝 등 |
| EvaluationModule | clean accuracy, ASR, confusion matrix, calibration(ECE), 실행시간, 리소스 측정 |
| ReproModule | 실험설정 YAML, 결과 JSON, seed logging, 환경정보: `pip freeze` |
| ReportModule | 표/그림 자동생성, 논문용 결과 서술 템플릿: LaTeX/Markdown 출력 |

## 10.2 Cursor류 IDE 코딩 에이전트 프롬프트 시나리오

### 01. 요구사항

```text
digits 데이터 기반으로 clean 학습 + label-flip poisoning + backdoor 실험이 가능한 재현성 프로젝트를 Python 패키지 구조로 scaffold 해라. seed 고정, config YAML, 결과 JSON 저장을 필수로.
```

### 02. 아키텍처

```text
DataModule/ModelModule/AttackModule/EvaluationModule을 인터페이스 중심으로 설계하고, 각 모듈의 public API와 타입힌트를 먼저 작성해라.
```

### 03. 공격 모듈

```text
label-flip, backdoor(trigger injection)를 구현하고, ASR을 계산하는 함수를 포함해라. 단위테스트를 추가해라.
```

### 04. 실험 러너

```text
config를 읽어 다중 실험(오염률 sweep)을 돌리고, 결과를 csv/json으로 저장하며, 실행 로그를 남겨라.
```

### 05. 리포트

```text
결과 csv/json에서 표와 그래프를 자동생성하고, 논문 결과 섹션 초안(예: Experimental Setup, Threat Model, Results)을 Markdown으로 생성해라.
```

### 06. 확장

```text
동일 파이프라인을 텍스트/LLM 보안(프롬프트 인젝션 사례 실험)으로 확장 가능한 플러그인 구조로 리팩터링해라.
```

---

# 11. 참고문헌 비교표와 연구 기여 포인트

## 11.1 핵심 연구축 비교표

| 연구축 | 공격면(대표) | 방어면(대표) | 평가 핵심지표(예) | 대표 참고 |
|---|---|---|---|---|
| Lifecycle assurance | 데이터→학습→배포 전 단계 취약 | assurance case, 모니터링 | 요구사항 충족, 드리프트 탐지 | Ashmore et al. (2021) |
| Adversarial ML | evasion, transfer, adaptive attack | adversarial training, detection | robust accuracy, attack success | Wang et al. (2023) |
| Data poisoning/backdoor | label-flip, trigger insertion | cleansing, robust aggregation | clean accuracy + ASR + stealth | Tian et al. (2022) |
| Deepfakes | 합성미디어 조작/허위증거 | 검출, 포렌식, 신뢰성 | FPR/FNR, cross-dataset generalization | Mirsky et al. (2021) |
| LLM evaluation | 벤치마크 오염, hidden test leakage | 평가 프로토콜, 데이터 위생 | contamination, reproducibility | Chang et al. (2024) |
| Federated learning security | gradient leakage, poisoning, backdoor | secure aggregation, defense taxonomy | privacy leakage, robustness | Mothukuri et al. (2021) |
| Differential privacy | training-data leakage, MI | DP-SGD, accounting | ε–utility trade-off | Blanco-Justicia et al. (2022) |
| Model IP protection | model stealing/extraction | watermark/fingerprint | utility loss, detectability | Oliynyk et al. (2023) |
| MLOps security | supply chain, drift, logging risk | pipeline control, monitoring | MTTR, drift metrics | Eken et al. (2025) |

## 11.2 박사과정 기여 포인트

### 1) 평가 프로토콜의 과학화

LLM/RAG/Agent 보안 연구는 “공격 성공”만으로는 부족하다. 다음 항목을 포함한 다목적 평가가 필요하다.

- 데이터 오염과 프롬프트 오염의 분리
- 재현가능한 seed/환경 구성
- 오탐/미탐
- 비용
- 품질(utility)
- 안전성 및 정책 준수

이는 LLM 평가 서베이와 보안 서베이를 동일 평가체계로 접합하는 연구로 이어질 수 있다.

### 2) 운영(MLOps)과 공격면의 정합

실전 사고는 모델 자체보다 배포 파이프라인, 권한, 로그, 업데이트 과정에서 발생할 수 있다. 보안 연구를 학습 알고리즘에만 두지 말고 assurance/MLOps 서베이와 공격 서베이를 결합해 운영 지향 위협모형을 제안하면 공헌점이 명확해진다.

### 3) 증명가능한 강건성(verification) 스케일링

정형검증은 대규모 모델에서 병목이 크다. 추상화/검증 서베이가 지적하는 병목을 직접 겨냥한 부분검증 또는 위험기반 검증 연구가 유효하다.

### 4) 프롬프트/에이전트 입력의 프라이버시

프롬프트가 민감정보를 포함하는 현실에서는 privacy-preserving prompting이 DP와 다른 위협모형을 요구한다. 프롬프트 보호 서베이를 기반으로 의료·금융·국방 등 특정 도메인의 데이터 규정과 연결한 실증 연구가 가능하다.

---

# 12. 수강생용 주간 보고서 기본 템플릿

아래 템플릿은 매주 논문 5편을 읽고 발표 또는 토론 준비에 사용할 수 있다.

```markdown
# Week N. [주차 제목] 학습보고서

## 1. 이번 주 핵심 주제
- AI 원리:
- 보안 이슈:
- 핵심 질문:

## 2. 논문별 요약

### Paper 1. [논문명]
- 연구문제:
- 방법론:
- 데이터/실험:
- 핵심 결과:
- 한계:
- 내 연구와의 연결점:

### Paper 2. [논문명]
- 연구문제:
- 방법론:
- 데이터/실험:
- 핵심 결과:
- 한계:
- 내 연구와의 연결점:

### Paper 3. [논문명]
- 연구문제:
- 방법론:
- 데이터/실험:
- 핵심 결과:
- 한계:
- 내 연구와의 연결점:

### Paper 4. [논문명]
- 연구문제:
- 방법론:
- 데이터/실험:
- 핵심 결과:
- 한계:
- 내 연구와의 연결점:

### Paper 5. [논문명]
- 연구문제:
- 방법론:
- 데이터/실험:
- 핵심 결과:
- 한계:
- 내 연구와의 연결점:

## 3. 5편 비교표

| 논문 | 연구문제 | 위협모형 | 평가방법 | 장점 | 한계 | 후속 연구 |
|---|---|---|---|---|---|---|
| Paper 1 |  |  |  |  |  |  |
| Paper 2 |  |  |  |  |  |  |
| Paper 3 |  |  |  |  |  |  |
| Paper 4 |  |  |  |  |  |  |
| Paper 5 |  |  |  |  |  |  |

## 4. 보안 관점 재해석
- 공격자:
- 보호자산:
- 공격면:
- 방어전략:
- 평가 지표:

## 5. 내 논문 주제와의 연결
- 관련성:
- 차별화 가능성:
- 실험 가능성:
- KCI/SCIE 발전 가능성:

## 6. 다음 주까지 할 일
- 읽을 논문:
- 구현/실험:
- 발표 준비:
- AI 도구 활용 Worklog:
```

---

# 13. 발표 준비 체크리스트

| 확인 | 항목 |
|---|---|
| □ | 주차 주제의 AI 원리 70%와 보안 이슈 30%를 분리하여 설명했다. |
| □ | 5편 논문의 연구문제를 각각 한 문장으로 정리했다. |
| □ | 각 논문의 위협모형을 공격자·자산·공격면·방어자로 구분했다. |
| □ | 평가방법의 데이터셋, 지표, 비교대상, 재현성을 확인했다. |
| □ | 논문 간 공통점과 차이점을 표로 정리했다. |
| □ | 기존 연구의 한계와 오픈문제를 제시했다. |
| □ | 내 논문 주제로 발전 가능한 기여점을 1–2문장으로 정리했다. |
| □ | 사용한 AI 도구와 활용 목적을 Worklog로 기록했다. |

---

# 14. 파일 관리 권장 구조

```text

```

---

# 15. 핵심 정리

이 강의계획서는 AI 보안 박사과정생이 논문을 읽고 끝내는 수준을 넘어, 실제 학위논문과 SCI/SCIE 논문으로 발전시킬 수 있도록 다음 흐름을 반복하도록 설계되어 있다.

```text
논문 읽기 → 연구문제 구조화 → 위협모형 정의 → 평가방법 검토 → 재현성 점검 → 한계 도출 → 내 논문 기여로 전환
```

학기 말에는 각자의 연구 기여를 다음 형식으로 고정하는 것이 목표다.

```text
본 연구는 [대상 AI 시스템]에서 발생하는 [보안 위협]을 [방법론/평가체계]로 분석하고, [기존 연구의 한계]를 보완하기 위해 [새로운 지표/프레임워크/실험결과]를 제안한다.
```
