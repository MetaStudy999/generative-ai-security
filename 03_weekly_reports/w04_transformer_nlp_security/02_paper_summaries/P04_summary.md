# P04 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | A Survey of Adversarial Defenses and Robustness in NLP |
| 저자 | Shreya Goyal, Sumanth Doddapaneni, Mitesh M. Khapra, Balaraman Ravindran |
| 출판 정보 | ACM Computing Surveys, Vol. 55, No. 14s, 2023, pp. 1-39 |
| DOI/URL | ACM DOI `10.1145/3593042`; arXiv DOI `10.48550/arXiv.2203.06414`; https://arxiv.org/abs/2203.06414 |
| PDF 파일명 | 04_Goyal_et_al_2023_Adversarial_Defences_Robustness_NLP.pdf |
| 검증 상태 | ACM CSUR 출판 DOI 확인. arXiv 제목은 `Defences`, ACM 제목은 `Defenses`. 강의자료의 `N. Goyal` 표기는 사람 검토 필요 |

## 2. 한 문장 요약

P04는 NLP 모델의 adversarial attack, defense, robustness를 taxonomy로 정리하고, 단어 치환·문장 재구성·문자 단위 교란·transfer attack을 평가하는 기준을 제공한다.

## 3. 연구문제

의미를 크게 유지하는 텍스트 교란이 NLP 모델 판단을 어떻게 바꾸며, 이를 어떤 방어 및 평가 지표로 측정할 수 있는가를 다룬다.

## 4. 핵심 개념

| 개념 | 설명 | W04 연결 |
|---|---|---|
| Word substitution | 의미가 비슷한 단어나 우회 표현으로 입력을 바꾼다. | W04 toy attack |
| Paraphrase attack | 문장 구조를 바꾸어 모델 판단을 흔든다. | semantic preservation |
| Character attack | 오탈자, 문자 삽입/삭제 등 표면형을 교란한다. | keyword detector 우회 가능성 |
| Robust accuracy | 공격 조건에서의 성능을 별도로 기록한다. | clean score와 ASR 분리 |

## 5. 방법론

문헌조사와 공격·방어 taxonomy 정리이다. 실제 공격 절차를 상세 재현하기보다 공격 유형, 방어 방법, 평가 기준을 분류한다.

### 5.1 핵심 수식 또는 알고리즘 설명

| 항목 | 내용 |
|---|---|
| 수식/알고리즘 이름 | NLP Adversarial Risk |
| 원문 위치 | 논문 세부 절/쪽/그림/알고리즘 번호 확인 필요. 로컬 DOI/URL 점검표로 문헌 대응만 확인. |
| 작성 형식 | Markdown + LaTeX math |
| 검산 도구 | 사용 안 함 |
| 수식 또는 절차 | 표준 정의식 / 원문 직접 인용 아님.<br>$$R_{adv}=\mathbb{E}_{(x,y)}\left[\max_{x_{alt}\in\mathcal{N}(x)}\ell(f_\theta(x_{alt}),y)\right]$$ |
| 기호·입력·출력 | \(\mathcal{N}(x)\): 의미 보존 또는 제한된 텍스트 변형 집합, \(x_{alt}\): 변형 입력 |
| 직관적 의미 | NLP Adversarial Risk는 Transformer·NLP 보안 평가에서 핵심 원리나 평가 지표를 정량적으로 해석하기 위한 표준식이다. |
| 보안 관점 해석 | Transformer·NLP 보안 평가에서는 정상 성능과 보안 실패 조건을 분리해 보아야 한다. 이 항목은 공격·방어 원리 또는 운영 통제의 평가 기준을 명시하되, 실제 공격 절차나 무단 적용 단계는 포함하지 않는다. |
| 평가 지표와 연결 | robust accuracy, ASR, semantic similarity, utility |
| 한계와 가정 | 표준 정의식 / 원문 직접 인용 아님. 논문별 변형, 정확한 수식 번호, 실험 설정은 원문 PDF에서 확인 필요다. |
| 기말 논문 반영 여부 | 반영 |

## 6. 주요 결과

NLP robustness는 clean accuracy만으로 설명할 수 없다. Attack success rate, semantic similarity, robust accuracy, transferability를 분리해서 보아야 한다.

## 7. 보안 관점 분석

W04 실험의 word substitution은 P04의 큰 범주를 안전한 toy 형태로 축소한 것이다. ASR 0.750000은 keyword detector의 synthetic toy 결과일 뿐 실제 Transformer 취약성 수치가 아니다.

## 8. 한계와 오픈문제

강의계획서의 제목 `on/Defenses/N. Goyal` 표기와 arXiv/ACM 메타데이터 사이에 차이가 있다. 최종 제출 전 사람 검토가 필요하다.

## 9. 기말 논문에 반영할 부분

프롬프트 보안 평가에서 clean score와 attack success rate를 분리해야 한다는 핵심 근거로 활용한다.
