# W14 DOI/URL 검증표

> 최종 판정 우선: 이 문서의 현재 상태는 `논문/관련 논문 최종 반영표`를 우선한다. 상단의 제목·저자·로컬 PDF 차이 메모는 오류 판정이 아니라 검증 이력이며, `관련 논문 / 확인`은 주차 주제에 맞는 공식 확인 논문으로 사용한다.


검증일: 2026-06-23. 검증 근거는 Crossref DOI metadata, DOI URL, arXiv URL, 로컬 PDF 메타데이터/첫 페이지이다. ACM 웹 페이지는 Cloudflare 차단으로 직접 Article 번호까지 확인하지 못했으므로, Article 번호는 `추가 확인 메모`로 둔다.

| ID | DOI/URL | DOI 메타데이터 기준 제목 | 권호/페이지 메타데이터 | 상태 | 남은 검토 사항 |
|---|---|---|---|---|---|
| P01 | https://doi.org/10.1145/3747346, https://arxiv.org/abs/2406.09737 | A Multivocal Review of MLOps Practices, Challenges and Open Issues | ACM Computing Surveys, Vol. 58, Issue 2, pp. 1-35, online 2025-09-08, print 2026-01-31 | 공식 DOI 확인 / 표기 차이 메모 | 수업자료의 `Bayram Eken` 및 긴 제목과 DOI/arXiv/로컬 PDF의 `Beyza Eken` 제목 차이 재확인. Article 번호 추가 확인 메모 |
| P02 | https://doi.org/10.1145/3533378, https://arxiv.org/abs/2011.09926 | Challenges in Deploying Machine Learning: A Survey of Case Studies | ACM Computing Surveys, Vol. 55, Issue 6, pp. 1-29, online 2022-12-07, print 2023-07-31 | 확인 | 수업자료의 권호/Article 번호와 Crossref 권호가 다르므로 ACM 페이지에서 Article 번호 최종 추가 확인 메모 |
| P03 | https://doi.org/10.1145/3625289 | A Joint Study of the Challenges, Opportunities, and Roadmap of MLOps and AIOps: A Systematic Survey | ACM Computing Surveys, Vol. 56, Issue 4, pp. 1-30, online 2023-10-21, print 2024-04-30 | 공식 DOI 확인 / 표기 차이 메모 | 수업자료 제목 `A Systematic Survey on MLOps and AIOps...` 및 `Daniel Diaz-de-Arcaya` 표기와 DOI 메타데이터가 다름. 로컬 PDF는 관련 보조 문헌 파일명으로 기록됨 |
| P04 | https://doi.org/10.1109/JPROC.2019.2921977 | Deep Learning With Edge Computing: A Review | Proceedings of the IEEE, Vol. 107, Issue 8, pp. 1655-1674, 2019-08 | 확인 | 로컬 PDF는 Zhou et al. RELATED이므로 최종 반영표 기준 공식 출판정보로 정리 |
| P05 | https://doi.org/10.1145/3505243 | A Survey on Deep Learning for Software Engineering | ACM Computing Surveys, Vol. 54, Issue 10s, pp. 1-73, print 2022-01-31, online 2022-09-13 | 공식 DOI 확인 / 관련 논문 메모 | 수업자료의 `Xiang Chen et al., Deep Learning for Software Engineering: A Survey`와 DOI/로컬 PDF 기준 Yang/Xia/Lo/Grundy 서지 차이 재확인 |

## 검증 원칙

1. DOI/URL은 확인된 범위만 기록하고, 확인하지 못한 Article 번호나 권호는 임의 생성하지 않는다.
2. `RELATED` 파일명은 관련 보조 문헌 이력이며, 최종 인용은 아래 최종 반영표 기준으로 구분한다.
3. 수업자료 표기와 DOI 메타데이터가 충돌하는 경우, 본 보고서는 DOI 메타데이터와 로컬 PDF 상태를 분리해 보여주고 `추가 확인 메모`를 유지한다.
4. 실험 결과, DOI, URL, 원문 세부 수치는 서로 다른 근거 파일이 있을 때만 확정한다.

## DOI 조회 메모

- P01: Crossref DOI와 arXiv `2406.09737`은 `Beyza Eken` 제목으로 대응된다.
- P02: DOI, 제목, 저자군은 확인되었으나 수업자료 권호/Article 표기와 Crossref 권호가 다르다.
- P03: DOI는 MLOps/AIOps systematic survey이지만 수업자료 제목과 DOI 메타데이터 제목이 다르다.
- P04: DOI/권호/페이지가 확인되었다. 로컬 PDF만 관련 보조 문헌이다.
- P05: DOI는 Yang/Xia/Lo/Grundy 논문으로 확인된다. 수업자료의 Xiang Chen 표기는 추가 확인 메모다.

<!-- AUTO-RELATED-PAPER-REFLECTION:start -->
## 논문/관련 논문 최종 판정 반영표

아래 표는 공식 DOI/arXiv 재검색 결과를 반영한 최종 판정이다. `논문 / 확인`은 공식 서지 기준으로 논문 인용, `관련 논문 / 확인`은 주차 주제 보강용 관련 논문 인용을 뜻한다.

| ID | 구분 | 상태 | 공식 확인 기준 | 보고서 반영 |
|---|---|---|---|---|
| P01 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3747346`; A Multivocal Review of MLOps Practices, Challenges and Open Issues; ACM Computing Surveys; 2025 | 공식 서지 기준으로 논문 인용 |
| P02 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3533378`; Challenges in Deploying Machine Learning: A Survey of Case Studies; ACM Computing Surveys; 2022 | 공식 서지 기준으로 논문 인용 |
| P03 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3625289`; A Joint Study of the Challenges, Opportunities, and Roadmap of MLOps and AIOps: A Systematic Survey; ACM Computing Surveys; 2023 | 공식 서지 기준으로 논문 인용 |
| P04 | 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1109/JPROC.2019.2921977`; Deep Learning With Edge Computing: A Review; Proceedings of the IEEE; 2019 | 공식 서지 기준으로 논문 인용 |
| P05 | 관련 논문 / 확인 | 공식 DOI 확인 | `https://doi.org/10.1145/3505243`; A Survey on Deep Learning for Software Engineering; ACM Computing Surveys; 2022 | 주차 주제 보강용 관련 논문으로 인용 |
<!-- AUTO-RELATED-PAPER-REFLECTION:end -->
