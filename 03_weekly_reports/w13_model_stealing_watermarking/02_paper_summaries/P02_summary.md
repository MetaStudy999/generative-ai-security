# P02 Summary

## Securing Large Language Models: A Survey of Watermarking and Fingerprinting Techniques — Peigen Ye et al., ACM Computing Surveys, 2026

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W13 Model Stealing & Watermarking |
| 논문명 | Securing Large Language Models: A Survey of Watermarking and Fingerprinting Techniques |
| DOI | https://doi.org/10.1145/3773028 |
| 검증 상태 | W13 `paper_list.md` 기준 관련 논문 공식 DOI 확인. 로컬 PDF는 Yuqing Liang et al. LLM watermarking survey로 강의자료 표기와 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 LLM watermarking과 fingerprinting을 **text watermark, model fingerprint, ownership verification, robustness, detectability, removal attack, false positive risk** 관점에서 정리하며, W13에서 생성형 AI 모델 IP와 산출물 추적의 핵심 보조 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | LLM watermark와 fingerprint는 각각 무엇을 보호하는가? |
| RQ2 | Watermark는 detectability와 text utility 사이에서 어떤 trade-off를 갖는가? |
| RQ3 | 공격자는 paraphrase, translation, sampling, fine-tuning으로 watermark를 약화시킬 수 있는가? |

---

## 3. 핵심 수식

$$
DetectionScore=\frac{N_{marked}-\mathbb{E}[N_{marked}]}{\sqrt{Var(N_{marked})}}
$$

$$
FPR=\frac{FP}{FP+TN}, \qquad FNR=\frac{FN}{FN+TP}
$$

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | LLM output, model ownership, generated text provenance |
| 공격자 목표 | watermark 제거, false ownership claim, detection evasion |
| 지표 | detection rate, FPR/FNR, robustness under paraphrase, utility drop |
| 재현성 | watermark key, detector version, sampling setting, paraphrase condition 기록 |

---

## 5. 기말논문 연결

P02는 LLM/RAG 서비스에서 생성 텍스트 provenance와 모델 소유권 검증을 평가하는 기준으로 사용한다.

---

## 6. 최종 판단

P02는 관련 문헌으로 사용하되, 강의자료 지정 P02와 로컬 PDF 차이 메모를 유지한다.
