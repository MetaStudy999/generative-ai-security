# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | The Creation and Detection of Deepfakes: A Survey |
| 저자 | Yisroel Mirsky, Wenke Lee |
| 학술지/학회 | ACM Computing Surveys |
| 출판 정보 | Vol. 54, No. 1, pages 1-41, online 2021-01-02, print issue 2022-01-31 |
| 연도 | 2021 online / 2022 print issue |
| DOI/URL | https://doi.org/10.1145/3425780, https://arxiv.org/abs/2004.11138 |
| PDF 파일명 | 04_Mirsky_Lee_2021_Creation_Detection_Deepfakes.pdf |
| 검증 상태 | DOI/URL 확인, Article 번호 확인 필요 |

## 2. 한 문장 요약

> 이 논문은 deepfake의 생성 방식과 탐지 방식을 함께 survey하며, 합성미디어가 허위정보·사칭·명예훼손·증거 조작 위험으로 이어지는 구조와 방어 한계를 정리한다.

## 3. 연구문제

딥페이크는 생성 기술 발전과 공개 도구 확산으로 점점 만들기 쉬워지고 탐지하기 어려워진다. 이 논문은 deepfake가 어떻게 생성되고, 어떤 탐지 접근이 사용되며, 기존 방어가 어떤 상황에서 실패하는지 묻는다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| Face swap/reenactment | 얼굴 정체성 또는 표정·동작을 합성 | 공격 시나리오 |
| Lip sync/audio-visual fake | 음성과 입모양 정합 조작 | 멀티모달 포렌식 |
| Artifact-based detection | 생성 과정의 흔적을 탐지 | detector 한계 분석 |
| Generalization failure | 학습 데이터 밖 조작 방식에서 성능 저하 | cross-domain 실험 |
| Societal harm | 허위정보, 사칭, 협박, 증거 조작 | 보안적 함의 |

## 5. 방법론

Creation과 detection을 함께 다루는 survey이다. W06에서는 이 논문을 위협모형의 중심 문헌으로 삼고, 공격 절차를 재현하지 않은 채 탐지 신뢰성 지표만 안전한 synthetic 실험으로 확인했다.

## 6. 주요 결과

딥페이크 탐지는 조작 종류, 데이터셋, 압축 수준, 생성 방식에 따라 성능이 크게 달라질 수 있다. 따라서 단일 accuracy보다 FPR/FNR, domain shift, human review 기준을 함께 기록해야 한다.

## 7. 보안 관점 분석

포렌식 맥락에서는 false positive가 무고한 사람을 의심하게 만들고, false negative가 실제 조작물을 놓치게 만든다. W06 toy 실험에서 FPR과 FNR을 분리한 이유가 여기에 있다.

## 8. 한계와 오픈문제

Survey 특성상 최신 diffusion 기반 video generation까지 모두 포괄하지는 못한다. 또한 탐지기 성능은 데이터셋과 후처리 조건에 강하게 의존하므로, 실제 적용 전에는 별도 검증이 필요하다.

로컬 PDF 첫 페이지에는 preprint성 placeholder DOI가 남아 있으므로 제출용 참고문헌에는 ACM DOI `10.1145/3425780`을 우선 사용한다. Crossref 제목은 `The Creation and Detection of Deepfakes`로 표시되며, 로컬 PDF와 강의계획서 제목의 `A Survey` 부제와 차이가 있어 최종 서지 형식에서 한 번 더 확인한다.

## 9. 기말 논문에 반영할 부분

딥페이크 위협모형, 보호 자산, 피해 시나리오, 탐지 실패 조건을 기말 논문의 보안 이슈와 평가방법 장에 반영한다.
