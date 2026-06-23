# PDF 원문 보관 정책

## 1. 원칙

공개 GitHub 저장소에는 저작권이 있는 논문 원문 PDF를 직접 보관하지 않는 것을 원칙으로 한다.

## 2. 허용

- DOI
- 공식 출판사 landing page URL
- arXiv 등 공개 배포가 허용된 URL
- 개인 로컬 보관 여부 표시
- 논문 요약 및 본인의 분석

## 3. Git 추적 정책

- `03_weekly_reports/**/01_papers/pdf/*.pdf` 아래 논문 PDF 원문은 Git 추적 대상에서 제외한다.
- `.gitignore`의 `*.pdf`, `03_weekly_reports/**/01_papers/pdf/` 규칙으로 신규 PDF 추적을 방지한다.
- 이번 감사 기준 Git 추적 PDF 수: 0개.
- 이미 과거 히스토리에 포함된 PDF의 완전 제거는 별도 이력 정리 작업으로 분리한다.

## 4. 수업 자료 예외

사용자가 직접 제공한 과제 안내문, 강의계획서, 수업자료 PDF는 저작권과 배포 범위를 별도 확인한 뒤 `00_class_materials/`에 보관할 수 있다. 단, 현재 정책은 논문 원문 PDF를 우선적으로 public repo 추적에서 제외하는 데 목적이 있다.

## 5. 대체 관리 방식

논문 원문 대신 다음 파일에서 DOI, 공식 URL, 검증 상태를 관리한다.

- `05_references/doi_index.md`
- `04_final_paper/06_appendices/reference_verification.md`
- 각 주차 `01_papers/doi_check.md`
