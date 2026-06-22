# P05 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Privacy Preserving Prompt Engineering: A Survey |
| 저자 | Kennedy Edemacu, Xintao Wu |
| 출판 정보 | ACM Computing Surveys, Vol. 57, No. 10, 2025, pp. 1-36 |
| DOI/URL | ACM DOI `10.1145/3729219`; arXiv DOI `10.48550/arXiv.2404.06001`; https://arxiv.org/abs/2404.06001 |
| PDF 파일명 | 05_Edemacu_Wu_2025_Privacy_Preserving_Prompt_Engineering.pdf |
| 검증 상태 | ACM CSUR 2025 출판 DOI 확인. Article 번호는 Crossref/BibTeX 응답에 미제공되어 확인 필요 |

## 2. 한 문장 요약

P05는 prompting과 in-context learning에서 발생하는 민감정보 노출 위험과 privacy-preserving prompt engineering 방식을 정리한 prompt privacy survey이다.

## 3. 연구문제

프롬프트 입력, ICL 예시, 모델 출력, 로그, 외부 도구 호출 인자에서 민감정보가 어떻게 노출될 수 있으며, masking, rewriting, policy control, privacy-preserving prompting으로 이를 어떻게 줄일 수 있는가를 묻는다.

## 4. 핵심 개념

| 개념 | 설명 | W04 연결 |
|---|---|---|
| Prompt privacy | 사용자 입력 프롬프트의 민감정보 보호 문제이다. | W04 핵심 보안 주제 |
| ICL leakage | few-shot 예시나 컨텍스트에 포함된 민감정보가 노출될 수 있다. | W07/W08/W11 연결 |
| Prompt masking | 민감값을 placeholder로 대체한다. | W04 toy defense |
| Policy control | 모델 입력과 출력에 개인정보 처리 원칙을 명시한다. | privacy-preserving wrapper |

## 5. 방법론

LLM prompting과 ICL privacy 문헌을 survey한다. 다양한 privacy protection method를 분류하고, 어떤 평가 자원과 한계가 있는지 정리한다.

## 6. 주요 결과

Prompt privacy는 leakage만 줄이면 끝나는 문제가 아니라 utility, policy compliance, reproducibility evidence를 함께 봐야 한다. 지나친 마스킹은 작업 의도를 훼손할 수 있다.

## 7. 보안 관점 분석

W04의 Prompt masking과 Privacy-preserving prompt 조건은 P05의 큰 문제의식을 synthetic toy protocol로 축소한 것이다. leakage 0.000000은 regex 기반 synthetic check 결과일 뿐 실제 LLM privacy guarantee가 아니다.

## 8. 한계와 오픈문제

출판 DOI는 확인되었지만 ACM Article 번호는 추가 확인이 필요하다. 또한 실제 개인정보, 실제 API, 운영 로그를 사용하지 않았으므로 외적 타당성은 후속 연구에서 별도 검증해야 한다.

## 9. 기말 논문에 반영할 부분

KCI/SCI 후보 주제인 “프롬프트 기반 AI 시스템의 민감정보 보호 평가체계”의 핵심 관련연구로 활용한다.
