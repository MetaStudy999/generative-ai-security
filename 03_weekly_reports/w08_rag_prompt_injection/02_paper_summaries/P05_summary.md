# 논문 요약

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 논문 제목 | Vulnerability of Large Language Models to Prompt Injection When Providing Medical Advice |
| 저자 | Ro Woon Lee, Tae Joon Jun, Jeong-Moo Lee, Soo Ick Cho, Hyung Jun Park, Jungyo Suh |
| 학술지/학회 | JAMA Network Open |
| 연도 | 2025 |
| DOI/URL | https://doi.org/10.1001/jamanetworkopen.2025.49963 |
| 권호/Article | JAMA Network Open 2025;8(12):e2549963 |
| PDF 파일명 | 05_Lee_et_al_2025_LLM_Prompt_Injection_Medical_Advice.pdf |
| 강의계획서 표기 | P. Lee et al., "Generative Artificial Intelligence and Prompt Injection Vulnerability in Drug Information Provision by Large Language Models" |
| 로컬 PDF/DOI 표기 | Ro Woon Lee et al., "Vulnerability of Large Language Models to Prompt Injection When Providing Medical Advice" |
| 검증 상태 | DOI/Crossref와 PDF 첫 페이지 확인. 강의계획서 제목과 동일 논문 여부 확인 필요 |

## 2. 한 문장 요약

> 이 논문은 의료 조언 LLM이 prompt injection에 의해 위험한 권고를 생성할 수 있는지를 통제된 patient-LLM dialogue simulation으로 평가하며, safety-critical RAG/LLM 시스템에서 system-level safeguard와 adversarial robustness testing이 필요함을 보인다.

## 3. 연구문제

상용 LLM이 의료 조언 환경에서 prompt injection에 조작되어 금기 치료나 안전하지 않은 권고를 할 수 있는가가 핵심 질문이다. 논문은 client-side injection과 evidence-fabrication injection을 통제된 시뮬레이션으로 평가한다.

## 4. 핵심 개념

| 개념 | 설명 | W08 연결 |
|---|---|---|
| Safety-Critical LLM | 의료처럼 잘못된 답변이 직접 피해로 이어질 수 있는 LLM 적용 |
| Controlled Simulation | 실제 환자나 진료 시스템을 쓰지 않는 통제된 평가 |
| Prompt Injection Success | 모델의 최종 권고가 주입 지시의 영향을 받는 상태 |
| Persistence | 후속 대화 turn에서도 조작 효과가 유지되는 현상 |
| Regulatory Oversight | 안전성 검증과 운영 통제 필요성 |

## 5. 방법론

2025년 1월부터 10월까지 통제된 simulation design을 사용했다. 원문은 12개 clinical scenario와 여러 commercial LLM을 대상으로 injection과 control 조건을 비교하고, primary decision turn과 follow-up persistence를 측정했다.

## 6. 주요 결과

PDF 첫 페이지 기준으로 216개 patient-LLM dialogue 평가에서 injection 성공률이 높게 보고되었고, 후속 대화에서도 조작 효과가 지속되는 사례가 관찰되었다. 특히 high-harm scenario에서 위험한 권고가 유도될 수 있음을 보여준다. W08 보고서에서는 해당 수치를 “의료 LLM 안전성 연구의 원문 결과”로만 인용하며, 실습 수치와 혼동하지 않는다.

## 7. 보안 관점 분석

이 논문은 prompt injection이 단순 정보 품질 문제가 아니라 Safety와 Accountability 문제임을 보여준다. RAG나 agent pipeline이 의료 문서, plugin, middleware와 연결될 경우 indirect injection은 사용자가 알아차리기 어려운 경로로 유입될 수 있다.

## 8. 한계와 오픈문제

본 논문은 의료 도메인에 초점을 둔다. W08 기말 연구로 일반화하려면 의료 조언 세부 payload가 아니라 safety-critical domain에서 필요한 평가 항목, approval gate, source verification, redacted testing 절차를 추출해야 한다.

주의: W08의 P05는 현재 로컬 PDF 기준 제목과 강의계획서 지정 제목이 다르므로, 동일 논문 여부와 최종 JAMA Network Open 서지정보를 확인 필요 상태로 유지한다.

## 9. 기말 논문에 반영할 부분

기말 논문 보안적 함의 장에는 “RAG prompt injection은 Integrity뿐 아니라 Safety 문제로 확대된다”는 근거로 반영한다.
