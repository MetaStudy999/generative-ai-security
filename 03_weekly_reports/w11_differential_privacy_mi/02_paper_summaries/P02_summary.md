# P02 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Recent Advances of Differential Privacy in Centralized Deep Learning: A Systematic Survey |
| 저자 | Lea Demelius, Roman Kern, Andreas Trugler |
| 학술지/학회 | ACM Computing Surveys 57(6), pp. 1-28; online 2025-02-10, print 2025-06-30 |
| 연도 | 로컬 PDF 2023, ACM 최종본 2025 |
| DOI/URL | DOI `10.1145/3712000`; arXiv `2309.16398` |
| PDF 파일명 | `02_Demelius_et_al_2025_Centralized_Deep_Learning_DP_Survey.pdf` |
| 검증 상태 | Crossref/ACM 등록 DOI 확인. 프롬프트의 `Jonathan Demelius`, `57(9), Article 202` 표기는 최종 대조 필요 |

## 2. 한 문장 요약

> 이 논문은 중앙집중형 deep learning에서 DP-DL 연구를 auditing/evaluation, privacy-utility 개선, generative model, 응용 도메인으로 체계화한다.

## 3. 연구문제

딥러닝의 고차원 파라미터, 많은 학습 step, non-convex objective 때문에 DP를 적용할 때 어떤 기술적 병목과 평가 문제가 생기는지를 묻는다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| DP-DL | 딥러닝 학습 과정 또는 산출물에 DP 보장을 결합하는 연구 흐름 | 관련연구 분류 |
| Auditing | DP 모델의 privacy leakage를 실험적으로 점검 | 평가방법 |
| Privacy-utility trade-off | noise와 clipping이 성능과 보호수준에 미치는 상충관계 | 실험 설계 |
| Centralized setting | 데이터가 중앙 학습 파이프라인에 모이는 조건 | W11 실험 범위 |

## 5. 방법론

체계적 문헌조사로 2019년 이후 DP-DL 연구의 초점을 분류한다. W11에서는 이 분류를 DP 평가 프로토콜의 상위 목차로 활용한다.

## 6. 주요 결과

DP-DL 연구는 단순 DP-SGD 적용을 넘어 auditing, privacy accountant, generative model, application-specific DP로 확장된다. 따라서 실험 보고서도 accuracy만이 아니라 leakage와 재현성 기록을 포함해야 한다.

## 7. 보안 관점 분석

P02는 “privacy 보장을 주장하는 모델을 어떻게 감사할 것인가”라는 질문에 연결된다. membership inference는 auditing의 대표 proxy로 사용하되, 실제 개인 대상 공격 절차와 구분해야 한다.

## 8. 한계와 오픈문제

로컬 PDF는 arXiv 버전이며 ACM 최종본과 세부 문구를 대조해야 한다. 주의: W11의 P02는 로컬 PDF 기준 `Lea Demelius, Roman Kern, Andreas Trugler` 및 arXiv:2309.16398로 확인되었고, 공식 DOI는 `10.1145/3712000`으로 확인되었다. 다만 강의계획서의 `Jonathan Demelius et al.` 및 `57(9), Article 202` 표기는 공식 메타데이터와 달라 최종 확인 필요 상태로 유지한다.

## 9. 기말 논문에 반영할 부분

기말 논문 4장 평가방법에서 `accuracy`, `MI attack accuracy`, `privacy leakage score`, `privacy accounting`, `run log`를 함께 기록하는 근거로 반영한다.
