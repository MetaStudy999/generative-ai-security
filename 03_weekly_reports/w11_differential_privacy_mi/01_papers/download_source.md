# W11 다운로드 출처 기록

| ID | 로컬 PDF | 확인한 출처/식별자 | 상태 | 비고 |
|---|---|---|---|---|
| P01 | `pdf/01_Blanco_Justicia_et_al_2022_Differential_Privacy_Critical_Review.pdf` | arXiv `2206.04621`; ACM DOI `10.1145/3547139` | 로컬 PDF 확인 | 로컬 파일은 arXiv v2이며 ACM CSUR 최종본은 DOI URL로 별도 확인 |
| P02 | `pdf/02_Demelius_et_al_2025_Centralized_Deep_Learning_DP_Survey.pdf` | arXiv `2309.16398`; ACM DOI `10.1145/3712000` | 로컬 PDF 확인 | 파일명은 2025 ACM CSUR 항목을 가리키지만 PDF 본문은 2023 arXiv preprint |
| P03 | `pdf/03_RELATED_Fu_et_al_2024_Differentially_Private_FL_Review.pdf` | 관련 논문 PDF arXiv `2405.08299`; 지정 논문 DOI `10.1016/j.neucom.2024.127663` | 관련 논문 PDF | 지정 논문은 Neurocomputing `Differential privacy in deep learning: A literature survey`; 로컬 PDF와 표기 차이 |
| P04 | `pdf/04_Hu_et_al_2022_Membership_Inference_Attacks_Survey.pdf` | arXiv `2103.07853`; ACM DOI `10.1145/3523273` | 로컬 PDF 확인 | PDF metadata의 placeholder DOI가 아니라 Crossref/ACM DOI를 기준으로 기록 |
| P05 | `pdf/05_RELATED_Bai_et_al_2024_MIA_Attacks_Defenses_FL_Survey.pdf` | 관련 논문 PDF arXiv `2412.06157`; 지정 논문 DOI `10.1145/3620667` | 관련 논문 PDF | 지정 논문은 ACM CSUR `Defenses to Membership Inference Attacks: A Survey`; 로컬 PDF와 표기 차이 |

## PDF 보관 정책 점검

- `01_papers/pdf/`의 PDF 5개는 현재 Git 추적 대상이다.
- `.gitignore`에는 `03_weekly_reports/**/01_papers/pdf/*.pdf` 규칙이 이미 존재하므로 신규 PDF 추가는 방지된다.
- 단, 이미 커밋된 PDF는 ignore 규칙만으로 제거되지 않는다. public GitHub 저장소라면 출판사 PDF 또는 원문 PDF 보관은 저작권 위험이 있으므로, 사용자의 명시 승인 후 Git 추적 제거와 DOI/URL 중심 관리로 전환하는 것이 필요하다.
- 본 작업에서는 사용자의 삭제 승인 없이 PDF를 삭제하지 않는다.

## 관리 원칙

- 로컬 PDF와 지정 논문이 다르면 제출본에 `관련 논문 PDF`로 명시한다.
- DOI/URL은 확인된 근거를 함께 적고, 모르는 DOI는 임의 생성하지 않는다.
- 기말논문 참고문헌에는 최종 원문 PDF와 공식 DOI가 확인된 항목만 확정 인용한다.
