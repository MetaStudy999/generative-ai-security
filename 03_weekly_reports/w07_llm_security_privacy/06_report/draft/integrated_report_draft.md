# W07 LLM 학습·정렬·평가 & LLM 보안·프라이버시 통합보고서

## 0. 메타정보

| 항목 | 내용 |
|---|---|
| 주차 | W07 |
| 주제 | LLM 학습·정렬·평가 & LLM 보안·프라이버시 |
| AI 원리 | LLM 학습, 추론, 정렬, 평가 프레임워크 |
| 보안 이슈 | 데이터 추출, 프롬프트 기반 공격, 소프트웨어 보안 접점 |
| 문서 상태 | 초안: 최종 수치와 제출 기준은 `../final/integrated_report_final.md` 참고 |

## 1. 한 문장 요약

W07는 LLM 학습/정렬/평가 및 LLM 보안/프라이버시를 중심으로 AI 원리와 보안 위협을 함께 정리하고, 기말 논문의 위협모형·평가방법·재현성 설계로 연결한다.

## 2. AI 원리 70% 정리

LLM 학습, 추론, 정렬, 평가 프레임워크를 이해하기 위해 LLM의 기본 구조, Pretraining, instruction tuning, alignment, RLHF와 preference optimization 개념, LLM 추론 구조, Context window와 tokenization, LLM 평가 벤치마크를 핵심 개념으로 정리했다. 이 원리들은 모델 또는 시스템이 어떤 입력과 학습 구조를 갖고 어떤 기준으로 평가되는지 설명한다.

## 3. 보안 이슈 30% 정리

데이터 추출, 프롬프트 기반 공격, 소프트웨어 보안 접점를 중심으로 LLM 보안·프라이버시 위협, Training data extraction, Prompt injection, Jailbreak, System prompt leakage, Sensitive information disclosure를 정리했다. 보안 분석은 공격 절차 자체보다 보호 자산, 공격자 능력, 방어자 가정, 평가 지표를 명확히 하는 방향으로 작성했다.

## 4. 논문 5편 요약

| ID | 논문 | 저자 | 연도 | 검증 상태 |
|---|---|---|---|---|
| P01 | A Survey on Evaluation of Large Language Models | Yupeng Chang et al. | 2024 | DOI PDF 기준 확인 |
| P02 | Security and Privacy Challenges of Large Language Models: A Survey | Badhan Chandra Das et al. | 2024 | arXiv/PDF 기준 확인, 출판정보 재검증 필요 |
| P03 | A Survey on Large Language Model (LLM) Security and Privacy: The Good, the Bad, and the Ugly | Yifan Yao et al. | 2024 | arXiv/PDF 기준 확인, 출판정보 재검증 필요 |
| P04 | A Survey on Multimodal Large Language Models | Shukang Yin et al. | 2024 | arXiv/PDF 기준 확인, 공식 권호/DOI 재검증 필요 |
| P05 | When Software Security Meets Large Language Models: A Survey | Xiaogang Zhu et al. | 2025 | DOI PDF 기준 확인 |

## 5. 논문 5편 비교

다섯 편은 AI 원리 문헌과 보안 문헌을 함께 포함한다. 기말 논문에서는 개별 문헌의 세부 수치보다 분류체계, 위협모형, 평가 프로토콜의 연결 관계를 우선 반영한다.

## 6. Research Track

### 6.1 연구문제

RQ1. LLM 학습/정렬/평가 및 LLM 보안/프라이버시의 생명주기에서 보안 보증을 위해 어떤 평가 항목이 필요한가?

RQ2. LLM 보안·프라이버시 위협, Training data extraction는 어느 단계에서 발생하며 어떤 조건에서 성공하는가?

RQ3. 성능, 보안성, 재현성을 함께 평가하려면 어떤 최소 프로토콜이 필요한가?

### 6.2 위협모형

대상 시스템은 LLM 학습/정렬/평가 및 LLM 보안/프라이버시 기반 AI/ML 시스템이며, 보호 자산은 데이터, 모델, 입력/컨텍스트, 출력, 로그, 평가셋이다. 공격자는 외부 공격자, 내부자, 데이터 제공자, API 남용자 등으로 나뉜다.

### 6.3 평가방법

Clean performance, attack impact, robust performance, privacy/leakage, reproducibility, human review를 기본 평가 항목으로 둔다.

### 6.4 재현성

Docker, pyproject.toml/uv sync, config, seed, 로그, PDF/DOI 검증표를 함께 보존한다. 최종본에는 synthetic toy 실험 실행 결과와 `outputs/` 로그를 반영했다.

### 6.5 한계와 오픈문제

DOI/URL, 원문 세부 수치, 대체 PDF 여부는 최종 확인이 필요하다. 또한 survey 문헌의 분류체계를 toy 실험과 어떻게 연결할지 추가 검토가 필요하다.

## 7. 실습 요약

실습은 synthetic prompt category 기반으로 실행했다. 실제 개인정보, 실제 서비스 침해, 무단 질의, 악용 가능한 절차는 포함하지 않는다.

## 8. AI 활용 기록 요약

Codex를 사용해 구조화 초안을 만들었다. AI 산출물은 사람 검토와 원문 대조를 거쳐 최종본에 반영한다.

## 9. 토론 질문

1. LLM 학습/정렬/평가 및 LLM 보안/프라이버시에서 가장 중요한 보호 자산은 무엇인가?
2. 공격 성공률과 일반 성능을 함께 볼 때 어떤 지표가 가장 설득력 있는가?
3. 원문 검증과 재현성 기록을 어느 수준까지 제출물에 포함해야 하는가?

## 10. 기말 논문 연결

W07는 기말 논문의 관련연구, 위협모형, 평가방법, 보안적 함의 장에 연결된다.

## 11. 참고문헌 검증표

참고문헌은 `01_papers/doi_check.md`에서 DOI/URL 확인 상태를 관리한다.

## 12. 자기 점검

| 항목 | 상태 |
|---|---|
| 논문 5편 요약 | 작성 |
| 비교표 | 작성 |
| AI 원리 70% | 작성 |
| 보안 이슈 30% | 작성 |
| Research Track | 작성 |
| 실험 결과 조작 방지 | 실행 로그 기반 수치만 최종본에 반영 |
| DOI 임의 생성 방지 | PDF 확인값과 arXiv 식별자만 기록 |
| AI 사용 은폐 방지 | AI 활용 고지서 작성 |
