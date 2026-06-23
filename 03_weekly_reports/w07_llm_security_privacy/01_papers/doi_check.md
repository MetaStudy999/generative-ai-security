# W07 DOI/URL 검증표

> 최종 판정 우선: 이 문서의 현재 상태는 `논문/관련 논문 최종 반영표`를 우선한다. 상단의 제목·저자·로컬 PDF 차이 메모는 오류 판정이 아니라 검증 이력이며, `관련 논문 / 확인`은 주차 주제에 맞는 공식 확인 논문으로 사용한다.


| ID | 논문 제목 | 공식 DOI/URL | 출판정보 | 상태 | 남은 검토 사항 |
|---|---|---|---|---|---|
| P01 | A Survey on Evaluation of Large Language Models | `https://doi.org/10.1145/3641289` | ACM Transactions on Intelligent Systems and Technology, 15(3), Article 39, pp. 1-45, 2024 | 부분 검증 | 강의계획서의 ACM Computing Surveys 및 `J. Chang et al.` 표기 차이 추가 확인 메모 |
| P02 | Security and Privacy Challenges of Large Language Models: A Survey | `https://doi.org/10.1145/3712001`; `https://arxiv.org/abs/2402.00888` | ACM Computing Surveys, 57(6), pp. 1-39, 2025; arXiv:2402.00888v2 | 부분 검증 | ACM CSUR 출판판 확인. 강의계획서의 `Ankur Das` 표기는 공식 저자명 `Badhan Chandra Das`와 표기 차이 |
| P03 | A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly | `https://doi.org/10.1016/j.hcc.2024.100211`; `https://arxiv.org/abs/2312.02003` | High-Confidence Computing, 4(2), Article 100211, 2024 | 추가 확인 메모 | 강의계획서의 `Mingzhe Yao et al.`, AI Open, `problems, methods, and opportunities` 논문과 동일 여부 추가 확인 메모 |
| P04 | A survey on multimodal large language models | `https://doi.org/10.1093/nsr/nwae403`; `https://arxiv.org/abs/2306.13549` | National Science Review, 11(12), Article nwae403, 2024 | 부분 검증 | 강의계획서의 `Yongtao Yin` 표기는 공식 저자명 `Shukang Yin`과 표기 차이 |
| P05 | When Software Security Meets Large Language Models: A Survey | `https://doi.org/10.1109/JAS.2024.124971` | IEEE/CAA Journal of Automatica Sinica, 12(2), pp. 317-334, 2025 | 부분 검증 | 강의계획서의 `Shujun Li` 표기는 공식 저자 목록과 표기 차이 |

## 강의계획서 차이 메모

- P01: DOI와 로컬 PDF는 ACM TIST 15(3), Article 39를 가리킨다. 강의계획서의 ACM Computing Surveys 표기는 실제 출판사 기준 정보와 다르다.
- P02: ACM CSUR 2025 출판판은 확인되며 DOI는 `10.1145/3712001`이다. 다만 공식 저자명은 Badhan Chandra Das, M. Hadi Amini, Yanzhao Wu이다.
- P03: 주의: W07의 P03은 현재 arXiv/PDF 기준 논문과 강의계획서 지정 AI Open 논문의 제목·저자 표기가 다르므로, 동일 논문 여부와 공식 출판정보를 추가 확인 메모 상태로 유지한다.
- P04: National Science Review 2024 공식판은 확인되며 DOI는 `10.1093/nsr/nwae403`이다. 다만 공식 저자 목록에는 `Yongtao Yin`이 확인되지 않는다.
- P05: DOI 기준 공식 저자 목록은 Xiaogang Zhu, Wei Zhou, Qing-Long Han, Wanlun Ma, Sheng Wen, Yang Xiang이다. `Shujun Li et al.` 표기는 추가 확인 메모로 유지한다.

## 검증 방법

1. DOI는 `doi.org` 리다이렉트와 Crossref 메타데이터를 우선 확인했다.
2. arXiv 항목은 arXiv API 또는 arXiv 페이지의 제목·저자·버전을 확인했다.
3. 로컬 PDF 표지에 기록된 DOI, 권호, 쪽수, arXiv 식별자를 보조 근거로 사용했다.
4. DOI를 확인하지 못한 정보는 임의 생성하지 않고 `추가 확인 메모`로 남겼다.

<!-- AUTO-RELATED-PAPER-REFLECTION:start -->
## 논문/관련 논문 최종 판정 반영표

아래 표는 공식 DOI/arXiv 재검색 결과를 반영한 최종 판정이다. `논문 / 확인`은 공식 서지 기준으로 논문 인용, `관련 논문 / 확인`은 주차 주제 보강용 관련 논문 인용을 뜻한다.

| ID | 구분 | 상태 | 공식 확인 기준 | 보고서 반영 |
|---|---|---|---|---|
| P01 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3641289`; A Survey on Evaluation of Large Language Models; ACM Transactions on Intelligent Systems and Technology; 2024 | 공식 서지 기준으로 논문 인용 |
| P02 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3712001`; Security and Privacy Challenges of Large Language Models: A Survey; ACM Computing Surveys; 2025 | 공식 서지 기준으로 논문 인용 |
| P03 | 관련 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1016/j.hcc.2024.100211`; A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly; High-Confidence Computing; 2024 | 주차 주제 보강용 관련 논문으로 인용 |
| P04 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1093/nsr/nwae403`; A survey on multimodal large language models; National Science Review; 2024 | 공식 서지 기준으로 논문 인용 |
| P05 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1109/JAS.2024.124971`; When Software Security Meets Large Language Models: A Survey; IEEE/CAA Journal of Automatica Sinica; 2025 | 공식 서지 기준으로 논문 인용 |
<!-- AUTO-RELATED-PAPER-REFLECTION:end -->
