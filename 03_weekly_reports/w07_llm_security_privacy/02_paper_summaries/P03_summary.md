# 논문 요약: P03

## 1. 서지정보

| 항목 | 내용 |
|---|---|
| 강의계획서 지정 논문 | Mingzhe Yao et al., *A survey on large language model security and privacy: problems, methods, and opportunities*, AI Open, 2024 |
| 로컬/공식 확인 논문 | Yifan Yao et al., *A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly* |
| 출판정보 | High-Confidence Computing, 4(2), Article 100211, 2024 |
| DOI/URL | `https://doi.org/10.1016/j.hcc.2024.100211`; arXiv `https://arxiv.org/abs/2312.02003` |
| 검증 상태 | 로컬 PDF 논문은 DOI 확인. 강의계획서 지정 AI Open 논문과 동일 여부는 확인 필요 |

## 2. 한 문장 요약

LLM은 보안 방어 도구가 될 수도 있지만 공격 자동화, 취약성 확대, prompt/context 위험의 원인이 될 수도 있으므로 good, bad, ugly 관점으로 함께 평가해야 한다[3].

## 3. 연구문제

LLM이 보안과 프라이버시에 긍정적으로 기여하는 경우, 공격적으로 악용되는 경우, 모델 자체 취약성을 드러내는 경우를 어떻게 나눌 수 있는가를 다룬다.

## 4. 핵심 개념

- The Good: vulnerability detection, secure coding support, privacy-preserving assistance.
- The Bad: phishing, social engineering, 공격 자동화 등 악용 가능성.
- The Ugly: prompt injection, data extraction, model extraction, inherent vulnerability.

## 5. 보안 관점 분석

P03은 LLM 보안 논의를 “보안 도구로서의 LLM”과 “공격면으로서의 LLM” 양쪽으로 확장한다. W07에서는 이 관점을 ASR, refusal quality, privacy leakage, code vulnerability rate를 동시에 기록해야 하는 이유로 연결한다.

## 6. 검증 메모

주의: W07의 P03은 현재 arXiv/PDF 기준 논문과 강의계획서 지정 AI Open 논문의 제목·저자 표기가 다르므로, 동일 논문 여부와 공식 출판정보를 확인 필요 상태로 유지한다.

## 7. 기말 논문 활용

공격-방어-평가 연결표를 만들 때 LLM의 양면성, 특히 보안 자동화와 오용 가능성을 동시에 설명하는 근거로 활용한다.
