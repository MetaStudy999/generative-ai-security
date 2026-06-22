# W02 DOI/URL 검증표

검증일: 2026-06-22

| ID | 논문 제목 | 최종 DOI/URL | 검증 근거 | 상태 | 메모 |
|---|---|---|---|---|---|
| P01 | Optimization Methods for Large-Scale Machine Learning | DOI: `10.1137/16M1080173`; `https://doi.org/10.1137/16M1080173` | Crossref 조회: SIAM Review, 60(2), 223-311, 2018, 저자 Leon Bottou/Frank E. Curtis/Jorge Nocedal | 확인 완료 | 강의계획서와 현재 목록 일치 |
| P02 | Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better | DOI: `10.1145/3578938`; `https://doi.org/10.1145/3578938`; arXiv `https://arxiv.org/abs/2106.08962` | DOI content negotiation: ACM Computing Surveys, 55(12), 1-37, 2023, 저자 Gaurav Menghani | 확인 완료 | 강의계획서의 `Gulzar Menghani`는 출판 정보와 불일치. Article 번호는 확인 필요 |
| P03 | A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning | DOI: `10.1145/3551636`; `https://doi.org/10.1145/3551636` | Crossref/DOI content negotiation: ACM Computing Surveys, 55(8), 1-35, 저자 Zhiyi Tian/Lei Cui/Jie Liang/Shui Yu | 확인 완료 | 강의계획서 `Zhipeng Tian`은 출판 정보 기준 `Zhiyi Tian`으로 정리 |
| P04 | Wild Patterns Reloaded: A Survey of Machine Learning Security against Training Data Poisoning | DOI: `10.1145/3585385`; `https://doi.org/10.1145/3585385`; arXiv `https://arxiv.org/abs/2205.01992` | Crossref/DOI content negotiation: ACM Computing Surveys, 55(13s), 1-39, 2023, Antonio Emanuele Cina et al. | 확인 완료 / 대체 여부 확인 필요 | 강의계획서 제목 "Training Data Poisoning Attacks and Defenses: A Systematic Review"와 완전 동일한 제목은 확인하지 못함. 현재 P04는 대체 논문 또는 제목 변경 여부 최종 확인 필요 |
| P05 | A survey of backdoor attacks and defences: From deep neural networks to large language models | DOI: `10.1016/j.jnlest.2025.100326`; `https://doi.org/10.1016/j.jnlest.2025.100326` | Crossref 조회: Journal of Electronic Science and Technology, 23(3), Article 100326, 2025, 저자 Ling-Xin Jin et al. | 확인 완료 | 강의계획서 `Z. Jin et al.`은 제1저자 약식 표기로 추정 |

## P04 주의 문구

주의: W02의 P04는 강의계획서 지정 논문인 "Training Data Poisoning Attacks and Defenses: A Systematic Review"와 현재 로컬 PDF "Wild Patterns Reloaded"의 동일 여부를 최종 확인해야 한다. 최종 제출 전 출판사 DOI와 판본을 재검증한다.

## PDF 보관 정책 점검

| 점검 항목 | 결과 |
|---|---|
| `01_papers/pdf/` PDF 원문 존재 | 존재 |
| PDF 원문 Git 추적 여부 | `git ls-files` 기준 5개 PDF 모두 추적 중 |
| `.gitignore` PDF 규칙 | `03_weekly_reports/**/01_papers/pdf/*.pdf` 규칙 존재 |
| 조치 필요 | 이미 추적 중인 PDF는 공개 GitHub 저장소에서 저작권 위험이 있으므로, 사용자 승인 후 Git 추적 제거 및 DOI/URL 대체 권장 |
| 현재 조치 | 삭제하지 않음. 위험만 표시 |

## 검증 원칙

1. DOI/URL을 확인하지 못한 항목은 `확인 필요`로 표시한다.
2. 제목이 강의계획서와 로컬 PDF에서 다를 경우, 출판사/DOI 메타데이터 제목을 우선 기록하고 차이를 메모로 남긴다.
3. ACM 원문 페이지는 접근 제한이 있을 수 있으므로 Article 번호는 최종 제출 전 학교 네트워크 또는 도서관 접근으로 재확인한다.
