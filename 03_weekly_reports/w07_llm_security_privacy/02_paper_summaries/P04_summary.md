# P04 Summary

## A survey on multimodal large language models — Shukang Yin et al., National Science Review, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W07 LLM 보안·프라이버시 |
| 논문명 | A survey on multimodal large language models |
| 저자 | Shukang Yin et al. |
| 출판 정보 | National Science Review, 11(12), Article nwae403, 2024 |
| DOI | https://doi.org/10.1093/nsr/nwae403 |
| 보조 URL | https://arxiv.org/abs/2306.13549 |
| 검증 상태 | W07 `paper_list.md` 기준 공식 DOI 확인. 강의계획서 `Yongtao Yin` 표기 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 멀티모달 LLM을 **visual encoder, projector, LLM backbone, instruction tuning, image-text alignment, multimodal reasoning, benchmark** 관점에서 정리하고, W07에서 시각 입력·텍스트 입력·도구 호출이 결합될 때 발생하는 보안 공격면을 설명한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | MLLM은 이미지/비디오 입력을 언어모델 context와 어떻게 결합하는가? |
| RQ2 | Visual instruction tuning과 alignment는 어떤 data provenance 위험을 갖는가? |
| RQ3 | 이미지 prompt injection, OCR injection, visual jailbreak는 어떤 위협모형으로 설명되는가? |
| RQ4 | 멀티모달 LLM 평가는 text-only LLM 평가와 어떤 지표 차이를 갖는가? |

---

## 3. 핵심 수식·구조

### 3.1 Multimodal Projection

$$
h_v=P_\phi(E_v(x_v)), \qquad y_t\sim p_\theta(y_t\mid h_v,x_{text},y_{<t})
$$

| 기호 | 의미 |
|---|---|
| $E_v$ | visual encoder |
| $P_\phi$ | projector/alignment module |
| $h_v$ | LLM에 투입되는 visual representation |
| $x_{text}$ | 텍스트 prompt |

### 보안 해석

이미지 안의 텍스트, QR, 표, 문서 조각, 시각적 지시문이 LLM context에 들어가면 prompt injection과 유사한 효과를 낼 수 있다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | 이미지, OCR 텍스트, visual embedding, system prompt, output, tool call |
| 공격자 목표 | visual prompt injection, hallucination, 잘못된 grounding, 개인정보 유출 |
| 공격자 능력 | 이미지 조작, embedded text 삽입, caption 조작, multimodal context poisoning |
| 대표 지표 | VQA accuracy, grounding accuracy, hallucination rate, visual jailbreak ASR, OCR leakage |
| 재현성 | 이미지 hash, prompt, model version, OCR 결과, output log 기록 |

---

## 5. 기말논문 연결

P04는 W07을 text-only LLM 보안에서 멀티모달 LLM 보안으로 확장한다. W08 RAG에서는 이미지·문서·표가 검색 context가 되므로 visual/context injection 평가로 이어진다.

---

## 6. 최종 판단

P04는 W07의 멀티모달 확장 핵심 문헌이다. LLM 보안 평가에 visual input, OCR, image-text alignment, multimodal provenance를 반드시 포함해야 함을 보여준다.
