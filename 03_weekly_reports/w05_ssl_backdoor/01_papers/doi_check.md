# W05 DOI/URL 검증표

| ID | 논문 제목 | DOI | URL | 상태 | 비고 |
|---|---|---|---|---|---|
| P01 | A Survey on Self-supervised Learning: Algorithms, Applications, and Future Trends | `10.48550/arXiv.2301.05712` | https://arxiv.org/abs/2301.05712 | arXiv DOI/URL 확인 | PDF 첫 페이지 및 arXiv 기준. IEEE TPAMI 출판 DOI는 미확인 |
| P02 | A Comprehensive Survey on Self-Supervised Learning for Recommendation | `10.1145/3746280` | https://doi.org/10.1145/3746280 | PDF 메타데이터/첫 페이지 DOI 확인 | 프롬프트 제목보다 범위가 좁은 recommendation survey |
| P03 | Self-Supervised Learning for Videos: A Survey | `10.1145/3577925` | https://doi.org/10.1145/3577925 | PDF 메타데이터/첫 페이지 및 arXiv URL 확인 | arXiv URL: https://arxiv.org/abs/2207.00419 |
| P04 | Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems | `10.1145/3538707` | https://doi.org/10.1145/3538707 | PDF 첫 페이지 DOI 확인 | 프롬프트 제목보다 정식 제목이 길다 |
| P05 | A survey of backdoor attacks and defences: From deep neural networks to large language models | `10.1016/j.jnlest.2025.100326` | https://doi.org/10.1016/j.jnlest.2025.100326 | 로컬 PDF DOI 링크 확인 | Crossmark/DOI 링크가 로컬 PDF 문자열에서 확인됨 |

## 검증 원칙

1. DOI는 추측해서 적지 않는다.
2. PDF 파일명과 프롬프트 논문명이 다를 경우 대체 문헌 여부를 먼저 확인한다.
3. 프롬프트 제목과 로컬 PDF/공개 URL 제목이 다를 경우, 제출본에는 PDF 첫 페이지 기준 정식 제목을 우선한다.
4. 최종 논문에는 DOI/URL 검증이 끝난 문헌만 확정 인용한다.

## pdfinfo/pdftotext 확인 메모

| ID | 확인 내용 |
|---|---|
| P01 | `pdfinfo` 기본 Title은 비어 있으나 첫 페이지와 arXiv 제목이 일치함. 23쪽 |
| P02 | `pdfinfo` Title, 첫 페이지, DOI가 `A Comprehensive Survey on Self-Supervised Learning for Recommendation`, `10.1145/3746280`로 일치함. 38쪽 |
| P03 | `pdfinfo` Title과 첫 페이지 제목이 `Self-Supervised Learning for Videos: A Survey`로 확인됨. 33쪽 |
| P04 | `pdfinfo` 기본 Title은 비어 있으나 첫 페이지 제목과 DOI가 `Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems`, `10.1145/3538707`로 확인됨. 36쪽 |
| P05 | `pdfinfo` Title, Subject, XMP metadata에서 DOI `10.1016/j.jnlest.2025.100326` 확인됨. 19쪽 |
