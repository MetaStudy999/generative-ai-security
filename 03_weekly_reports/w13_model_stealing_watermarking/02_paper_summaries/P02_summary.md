# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 프롬프트 지정 논문 | A Survey of Watermarking and Fingerprinting Techniques for Deep Learning Models |
| 로컬 PDF 제목 | Watermarking Techniques for Large Language Models: A Survey |
| 로컬 PDF 저자 | Yuqing Liang, Jiancheng Xiao, Wensheng Gan, Philip S. Yu |
| 연도 | 2024 |
| DOI/URL | PDF 표기 arXiv:2409.00089v1, DOI/출판사 URL 확인 필요 |
| PDF 파일명 | 02_SUBSTITUTE_Liang_et_al_2024_LLM_Watermarking_Survey.pdf |
| 검증 상태 | 프롬프트 지정 문헌과 다른 대체 PDF로 확인, 최종 인용 전 교체 여부 결정 필요 |

## 2. 한 문장 요약

> 이 로컬 PDF는 LLM 워터마킹을 전통적 디지털 워터마킹, 텍스트/멀티모달 생성물 추적, IP 보호, 오남용 추적 관점에서 정리하며, W13의 watermarking/fingerprinting 논의를 LLM 출력 추적 문제로 확장한다.

## 3. 연구문제

LLM이 생성한 텍스트, 이미지, 오디오 등에서 출처 추적과 저작권 보호를 어떻게 수행할 수 있는가를 다룬다. 특히 text watermarking의 robustness, semantic invariance, security vulnerability, system consumption 문제가 핵심 한계로 제시된다.

## 4. 핵심 개념

| 개념 | 설명 | 기말 논문 연결 |
|---|---|---|
| LLM watermarking | 생성물 또는 모델 출력에 식별 가능한 신호를 삽입하는 기술 | 생성형 AI IP 보호 |
| Data traceability | 생성물의 출처 모델을 추적하는 기능 | 책임성 평가 |
| Semantic invariance | 워터마크가 의미 품질을 망가뜨리지 않아야 하는 조건 | utility-protection trade-off |
| Multimodal watermarking | 텍스트 외 이미지, 오디오, 비디오 생성물의 추적 | 후속 연구 확장 |

## 5. 방법론

전통적 watermarking에서 LLM watermarking으로 이어지는 기술 계보를 정리하고, modality와 기능별로 연구를 분류한다. 로컬 PDF는 프롬프트 지정 P02와 다르므로 W13에서는 “대체 참고문헌”으로만 사용한다.

## 6. 주요 결과

LLM 워터마킹은 IP 보호와 생성물 추적에 유용하지만, paraphrasing, clipping, semantic shift, 계산 비용, 내부 접근 필요성 같은 문제가 남는다. 이 한계는 W13 실습에서 false positive/false negative와 utility loss를 별도 지표로 둬야 하는 이유가 된다.

## 7. 보안 관점 분석

워터마크는 소유권 입증과 책임성 강화에 도움이 되지만, 삽입 규칙이 알려지거나 출력 품질이 떨어지면 방어 자체가 공격면이 될 수 있다. 따라서 detection rate만이 아니라 false positive, robustness, content quality를 함께 보고해야 한다.

## 8. 한계와 오픈문제

로컬 PDF가 프롬프트 지정 ACM CSUR 문헌과 일치하지 않는다. 최종 제출 전 원래 P02 논문 확보 여부를 확인하고, 대체 문헌을 유지한다면 참고문헌표에 대체 사유를 명시해야 한다.

## 9. 기말 논문에 반영할 부분

LLM 생성물 추적, 워터마크 강건성, 의미 보존, 오탐/미탐 지표를 W13 보안 평가표의 책임성 항목으로 반영한다.
