# W07 DOI/URL 검증표

| ID | 논문 제목 | DOI | URL | 상태 | 비고 |
|---|---|---|---|---|---|
| P01 | A Survey on Evaluation of Large Language Models | `10.1145/3641289` | `https://doi.org/10.1145/3641289` | PDF 기준 확인 | ACM TIST 15(3), Article 39로 PDF에 명시 |
| P02 | Security and Privacy Challenges of Large Language Models: A Survey | 출판사 DOI 미확인 | `https://arxiv.org/abs/2402.00888` | 부분 확인 | 로컬 PDF는 arXiv:2402.00888v2, DOI 자리에 `XXXXXXX` 임시값 표기 |
| P03 | A Survey on Large Language Model (LLM) Security and Privacy: The Good, the Bad, and the Ugly | arXiv DOI 후보: `10.48550/arXiv.2312.02003` | `https://arxiv.org/abs/2312.02003` | 부분 확인 | 로컬 PDF는 arXiv:2312.02003v3, Elsevier 제출 원고 표기 |
| P04 | A Survey on Multimodal Large Language Models | arXiv DOI 후보: `10.48550/arXiv.2306.13549` | `https://arxiv.org/abs/2306.13549` | 부분 확인 | 로컬 PDF는 arXiv:2306.13549v4 및 IEEE T-PAMI 표기, 공식 권호/DOI 재검증 필요 |
| P05 | When Software Security Meets Large Language Models: A Survey | `10.1109/JAS.2024.124971` | `https://doi.org/10.1109/JAS.2024.124971` | PDF 기준 확인 | IEEE/CAA J. Autom. Sinica 12(2), pp. 317-334로 PDF에 명시 |

## 검증 원칙

1. DOI는 PDF 내부 또는 공식 페이지에서 확인되는 값만 확정 DOI로 적는다.
2. arXiv DOI 후보는 출판사 DOI와 구분한다.
3. PDF 파일명과 프롬프트 논문명이 다를 경우 로컬 PDF 기준 서지정보를 우선 표시하고, 최종 원고에서는 공식 출판정보를 재검증한다.
