# P04 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | The Federation Strikes Back: A Survey of Federated Learning Privacy Attacks, Defenses, Applications, and Policy Landscape |
| 저자 | Joshua C. Zhao et al. |
| 공식 출판 정보 | ACM Computing Surveys, 57(9), pp. 1-37, 2025 |
| DOI/URL | https://doi.org/10.1145/3724113 |
| PDF 파일명 | 04_Zhao_et_al_2025_Federation_Strikes_Back.pdf |
| 검증 상태 | DOI 메타데이터 기준 제목, 학술지, volume, issue, page 확인. Article 번호는 추가 확인 필요 |

## 2. 한 문장 요약

이 논문은 FL privacy attack, defense, application, policy landscape를 함께 검토하며, 모델 업데이트 공유가 항상 privacy-preserving이라는 전제가 깨질 수 있음을 정리한다[4].

## 3. 연구문제

FL 모델 업데이트에서 어떤 privacy attack이 가능한지, 어떤 방어와 정책 조건이 필요한지를 다룬다. W10에서는 privacy leakage를 실제 gradient inversion이 아니라 update exposure proxy로 제한해 기록한다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Privacy attack | 모델 업데이트에서 학습 데이터 단서를 추론하는 위협 | privacy leakage proxy |
| Defense method | 업데이트 보호, secure aggregation, DP 등 | 방어 비교 |
| Application lesson | 실제 산업 적용에서 얻은 운영상 제약 | 정책·운영 함의 |
| Policy landscape | 개인정보 보호 규제와 FL 운영 책임 | 기말 논문 보안 함의 |

## 5. 방법론

이 문헌은 privacy attack과 defense를 문헌 기반으로 정리하고, 실제 적용과 정책 환경까지 연결한다. W10 보고서는 이를 privacy 지표를 독립 항목으로 분리해야 하는 근거로 사용한다.

## 6. 보안 관점 분석

P04는 secure aggregation, DP, privacy attack, policy landscape를 연결한다. W10의 Privacy Leakage Proxy는 실제 gradient inversion이나 membership inference 성공률이 아니라 update norm 기반 대용 지표이며, policy discussion을 위한 위험 신호로만 해석한다.

## 7. 한계와 확인 필요

- DOI 등록 메타데이터에서는 pages 1-37이 확인되었으나 별도 Article 번호는 확인되지 않았다.
- 수업자료에는 P04가 Article 230으로 적혀 있으므로 최종 제출 전 ACM 페이지에서 Article 번호를 사람이 확인해야 한다.
- 로컬 PDF는 `Manuscript submitted to ACM CSUR` 성격을 포함하므로 최종 참고문헌에는 DOI 메타데이터를 우선 사용한다.

## 8. 기말 논문에 반영할 부분

P04는 FL privacy와 policy landscape를 기말 논문의 보안적 함의 장에 연결한다. 기술적 방어만으로 부족하고 규제·책임성·검증 로그가 함께 필요하다는 논거가 된다.
