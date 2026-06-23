# W07 논문 목록

## 강의계획서 지정 패킷과 로컬 확인본 대조

| ID | 강의계획서 지정 정보 | 로컬/공식 확인 정보 | DOI/URL | 검증 상태 | 비고 |
|---|---|---|---|---|---|
| P01 | J. Chang et al., *A Survey on Evaluation of Large Language Models*, ACM Computing Surveys, 2024 | Yupeng Chang et al., *A Survey on Evaluation of Large Language Models*, ACM Transactions on Intelligent Systems and Technology 15(3), Article 39, pp. 1-45, 2024 | `https://doi.org/10.1145/3641289` | 부분 검증 | 제목과 DOI 기준 로컬 논문 확인. 강의계획서의 `J. Chang` 및 ACM CSUR 표기는 실제 출판정보와 차이가 있어 메모 유지 |
| P02 | Ankur Das et al., *Security and Privacy Challenges of Large Language Models: A Survey*, ACM Computing Surveys, 2025 | Badhan Chandra Das, M. Hadi Amini, Yanzhao Wu, *Security and Privacy Challenges of Large Language Models: A Survey*, ACM Computing Surveys 57(6), pp. 1-39, 2025 | `https://doi.org/10.1145/3712001`; arXiv `https://arxiv.org/abs/2402.00888` | 부분 검증 | ACM CSUR 2025 출판판 확인. 강의계획서의 `Ankur Das` 표기는 공식 저자명과 불일치하므로 확인 필요 |
| P03 | Mingzhe Yao et al., *A survey on large language model security and privacy: problems, methods, and opportunities*, AI Open, 2024 | Yifan Yao et al., *A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly*, High-Confidence Computing 4(2), Article 100211, 2024 | `https://doi.org/10.1016/j.hcc.2024.100211`; arXiv `https://arxiv.org/abs/2312.02003` | 확인 필요 | 현재 로컬 PDF는 공식 DOI가 확인되지만 강의계획서 지정 AI Open 논문과 제목·저자·출판지가 달라 대체 문헌 가능성 표시 |
| P04 | Yongtao Yin et al., *A survey on multimodal large language models*, National Science Review, 2024 | Shukang Yin, Chaoyou Fu, Sirui Zhao, Ke Li, Xing Sun, Tong Xu, Enhong Chen, *A survey on multimodal large language models*, National Science Review 11(12), Article nwae403, 2024 | `https://doi.org/10.1093/nsr/nwae403`; arXiv `https://arxiv.org/abs/2306.13549` | 부분 검증 | 제목·출판지·연도·DOI 확인. 강의계획서의 `Yongtao Yin` 표기는 공식 저자 목록과 불일치하여 확인 필요 |
| P05 | Shujun Li et al., *When Software Security Meets Large Language Models: A Survey*, IEEE/CAA Journal of Automatica Sinica, 2025 | Xiaogang Zhu, Wei Zhou, Qing-Long Han, Wanlun Ma, Sheng Wen, Yang Xiang, *When Software Security Meets Large Language Models: A Survey*, IEEE/CAA Journal of Automatica Sinica 12(2), pp. 317-334, 2025 | `https://doi.org/10.1109/JAS.2024.124971` | 부분 검증 | 제목·저널·DOI·권호·쪽수 확인. 강의계획서의 `Shujun Li` 표기는 공식 저자 목록과 불일치하여 확인 필요 |

## PDF 보관 및 저작권 메모

- `01_papers/pdf/`에는 5개 PDF 원문 파일이 존재한다.
- `git ls-files` 기준 위 PDF 5개는 현재 저장소 추적 대상이다.
- public GitHub 저장소에는 출판사 PDF 원문 대신 DOI/URL, 서지정보, 요약, 개인 학습용 메모만 남기는 편이 안전하다.
- 루트 `.gitignore`에는 이미 `03_weekly_reports/**/01_papers/pdf/*.pdf` 규칙이 있다. 그러나 이미 추적 중인 PDF는 별도 삭제/이력 정리가 필요하다.
- 사용자 승인 없이 PDF는 삭제하지 않았다.

## 검수 원칙

1. DOI/URL은 DOI, Crossref, arXiv, 로컬 PDF 표지의 확인 정보만 기록한다.
2. 강의계획서 표기와 공식 메타데이터가 다른 경우, 공식 출판정보를 참고문헌 우선값으로 쓰되 차이를 검증 메모에 남긴다.
3. P03처럼 지정 문헌과 로컬 PDF가 다른 경우 대체 문헌 가능성을 명시하고 최종 제출 전 사람이 확인한다.

<!-- AUTO-RELATED-PAPER-REFLECTION:start -->
## 논문/관련 논문 최종 반영표

아래 표는 공식 DOI/arXiv 재검색 결과를 주차 보고서에 반영하기 위한 최종 판정이다. 기존 대조 기록은 보존하고, 보고서 본문과 참고문헌에서는 이 표의 `구분`과 `검증 상태`를 우선 사용한다.

| ID | 구분 | 논문 제목 | 논문 | 저자 | 연도 | 학술지/학회 | 학술지/출처 | DOI/URL | 검증 상태 | 보고서 반영 |
|---|---|---|---|---|---:|---|---|---|---|---|
| P01 | 논문 / 확인 | A Survey on Evaluation of Large Language Models | A Survey on Evaluation of Large Language Models | Yupeng Chang et al. | 2024 | ACM Transactions on Intelligent Systems and Technology | ACM Transactions on Intelligent Systems and Technology | `https://doi.org/10.1145/3641289` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P02 | 논문 / 확인 | Security and Privacy Challenges of Large Language Models: A Survey | Security and Privacy Challenges of Large Language Models: A Survey | Badhan Chandra Das, M. Hadi Amini, Yanzhao Wu | 2025 | ACM Computing Surveys | ACM Computing Surveys | `https://doi.org/10.1145/3712001` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P03 | 관련 논문 / 확인 | A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly | A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly | Yifan Yao et al. | 2024 | High-Confidence Computing | High-Confidence Computing | `https://doi.org/10.1016/j.hcc.2024.100211` | 공식 DOI 확인 | 주차 주제 보강용 관련 논문으로 인용 |
| P04 | 논문 / 확인 | A survey on multimodal large language models | A survey on multimodal large language models | Shukang Yin et al. | 2024 | National Science Review | National Science Review | `https://doi.org/10.1093/nsr/nwae403` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
| P05 | 논문 / 확인 | When Software Security Meets Large Language Models: A Survey | When Software Security Meets Large Language Models: A Survey | Xiaogang Zhu et al. | 2025 | IEEE/CAA Journal of Automatica Sinica | IEEE/CAA Journal of Automatica Sinica | `https://doi.org/10.1109/JAS.2024.124971` | 공식 DOI 확인 | 공식 서지 기준으로 논문 인용 |
<!-- AUTO-RELATED-PAPER-REFLECTION:end -->
