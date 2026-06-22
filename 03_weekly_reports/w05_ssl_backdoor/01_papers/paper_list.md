# W05 논문 목록

## 1. 강의계획서 패킷과 로컬 문헌 대조

| ID | 강의계획서 표기 | 로컬/검증 기준 정식 제목 | 저자 | 출판 정보 | DOI/URL | 상태 |
|---|---|---|---|---|---|---|
| P01 | Yan Gui et al., "Self-Supervised Learning: Algorithms, Applications, and Future Trends", IEEE TPAMI, 2024 | A Survey on Self-Supervised Learning: Algorithms, Applications, and Future Trends | Jie Gui, Tuo Chen, Jing Zhang, Qiong Cao, Zhenan Sun, Hao Luo, Dacheng Tao | IEEE Transactions on Pattern Analysis and Machine Intelligence, 46(12), 9052-9071, 2024 | `10.1109/TPAMI.2024.3415112`; arXiv `10.48550/arXiv.2301.05712` | TPAMI DOI 확인. 강의계획서의 `Yan Gui`는 `Jie Gui` 표기 오기 가능성이 있어 사람 최종 확인 필요 |
| P02 | H. Ren et al., "A Comprehensive Survey on Self-Supervised Learning", ACM Computing Surveys, 2025 | A Comprehensive Survey on Self-Supervised Learning for Recommendation | Xubin Ren, Wei Wei, Lianghao Xia, Chao Huang | ACM Computing Surveys, 58(1), Article 22, 1-38, online 2025 | `10.1145/3746280` | 로컬 PDF는 추천 시스템 SSL survey다. 강의계획서 지정 일반 SSL survey와 동일 여부 확인 필요 |
| P03 | "Self-Supervised Learning of Video Representations: A Survey" | Self-Supervised Learning for Videos: A Survey | Madeline C. Schiappa, Yogesh S. Rawat, Mubarak Shah | ACM Computing Surveys, 55(13s), 1-37, 2023 | `10.1145/3577925`; arXiv `2207.00419` | ACM 정식 제목 확인. 강의계획서 제목은 의미상 축약/변형 가능성이 있으나 제목 차이 기록 |
| P04 | Y. Wang et al., "A Survey of Poisoning Attacks and Defenses on Machine Learning", ACM Computing Surveys, 2022 | Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems | Zhibo Wang, Jingjing Ma, Xue Wang, Jiahui Hu, Zhan Qin, Kui Ren | ACM Computing Surveys, 55(7), Article 134, 1-36, 2022 | `10.1145/3538707` | 로컬 PDF 정식 제목/저자 확인. 강의계획서 제목 및 `Y. Wang` 표기와 동일 논문 여부 확인 필요 |
| P05 | Z. Jin et al., "A survey of backdoor attacks and defences: From deep neural networks to large language models", Journal of Electronic Science and Technology, 2025 | A survey of backdoor attacks and defences: From deep neural networks to large language models | Ling-Xin Jin, Wei Jiang, Xiang-Yu Wen, Mei-Yu Lin, Jin-Yu Zhan, Xing-Zhi Zhou, Maregu Assefa Habtie, Naoufel Werghi | Journal of Electronic Science and Technology, 23(3), Article 100326, 2025 | `10.1016/j.jnlest.2025.100326` | DOI/저자/학술지 확인. 강의계획서 `Z. Jin` 표기는 출판사 기준 첫 저자명과 다르므로 확인 필요 |

## 2. P02 주의 문구

주의: W05의 P02는 강의계획서 지정 일반 자기지도학습 종합 서베이와 동일 여부를 최종 확인해야 한다. 현재 로컬 PDF는 추천 시스템 분야의 Self-Supervised Learning survey로 범위가 좁으므로, 최종 제출 전 대체 문헌 사용 여부를 확인한다.

## 3. PDF 보관 위험

`01_papers/pdf/`에는 IEEE/ACM/Elsevier 계열 PDF 원문 5개가 존재하고, 현재 Git 추적 대상이다. public GitHub 저장소에는 원칙적으로 PDF 원문 대신 DOI/URL, 서지정보, 요약만 남겨야 한다. 삭제는 사용자 승인 없이 수행하지 않았으며, 제출 전 `git rm --cached` 또는 저장소 비공개 여부 확인이 필요하다.
