# P04 Summary

## A survey on multimodal large language models — Shukang Yin et al., National Science Review, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W07 LLM 보안·프라이버시 |
| 논문명 | A survey on multimodal large language models |
| 저자 | Shukang Yin et al. |
| 공식 출판 정보 | National Science Review, Vol. 11, No. 12, Article nwae403, 2024 |
| DOI | https://doi.org/10.1093/nsr/nwae403 |
| 보조 URL | https://arxiv.org/abs/2306.13549 |
| 로컬 PDF | `01_papers/pdf/04_Yin_et_al_2024_Multimodal_LLMs_Survey.pdf` |
| 검증 상태 | W07 `paper_list.md`와 `download_source.md` 기준 공식 DOI 확인. 강의계획서에는 `Yongtao Yin et al.`로 표기되어 있으나, repo의 공식 확인 정보는 `Shukang Yin et al.`임 |
| PDF 확인 메모 | repo의 PDF 폴더에 P04 관련 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W07 `paper_list.md`, `download_source.md`의 공식 DOI/arXiv 메타데이터 기준으로 보완했다. |
| 수식 호환성 | GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않고, `\mathrm{...}` 또는 짧은 변수명 중심으로 작성했다. 특히 `y_{<t}`처럼 GitHub에서 brace 오류를 낼 수 있는 표현은 `y_{1:t-1}`로 바꿨다. |
| 핵심 근거 사용 가능 여부 | 가능. W07의 text-only LLM 보안을 multimodal LLM 보안으로 확장하는 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 멀티모달 대규모 언어모델을 **visual encoder, projector/alignment module, LLM backbone, image-text alignment, multimodal instruction tuning, visual question answering, grounding, captioning, OCR/document understanding, chart understanding, video understanding, embodied AI, benchmark** 관점에서 정리하며, W07에서는 LLM 보안 공격면이 텍스트 prompt를 넘어 **이미지·문서·OCR·차트·비디오·시각 grounding·cross-modal alignment·tool action**까지 확장됨을 보여주는 핵심 survey 문헌이다.

---

## 2. 핵심 연구문제

> 멀티모달 LLM은 시각 입력과 텍스트 지시를 함께 처리한다. 따라서 이미지 내부 텍스트, 문서 스캔, 표·차트, OCR 결과, 비디오 frame, caption이 모두 prompt의 일부가 될 수 있으며, text-only LLM 보안 지표만으로는 충분하지 않다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | MLLM은 visual encoder, projector, LLM backbone을 어떤 구조로 결합하는가? |
| RQ2 | Image-text alignment와 visual instruction tuning은 성능과 취약성에 어떤 영향을 주는가? |
| RQ3 | 이미지 내부 텍스트, 문서 캡처, OCR 결과, 표·차트가 prompt injection 경로가 될 수 있는가? |
| RQ4 | 멀티모달 hallucination, grounding failure, visual jailbreak, OCR leakage, privacy leakage는 어떤 지표로 평가해야 하는가? |
| RQ5 | W08 RAG 및 W14 MLOps에서 멀티모달 입력의 provenance, hash, OCR log, human review evidence를 어떻게 관리해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W07 연결 |
|---|---|---|
| MLLM 구조 정리 | visual encoder, projector/alignment module, LLM backbone의 연결 구조 설명 | 멀티모달 위협모형의 시스템 구조 제공 |
| Instruction tuning 분석 | image-text instruction data의 역할과 한계 정리 | fine-tuning data provenance 위험 연결 |
| Benchmark taxonomy | VQA, captioning, grounding, reasoning, OCR/document understanding benchmark 정리 | text-only 평가 지표의 한계 보완 |
| Cross-modal reasoning | 시각 정보와 언어 추론의 결합 설명 | RAG 문서·이미지 입력 보안 연결 |
| 최신 응용 범위 | OCR, chart, document, video, embodied AI로 확장 | W08/W14/W15 evidence chain 연결 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | MLLM은 이미지·텍스트 등 여러 modality를 결합해 더 풍부한 이해와 생성을 수행한다. | AI가 글뿐 아니라 그림과 문서도 함께 본다. |
| 2. Architecture | visual encoder, projector, LLM backbone, adapter, cross-attention 구조를 설명한다. | 이미지를 언어모델이 이해할 수 있는 벡터로 바꿔 연결한다. |
| 3. Training and Alignment | image-text pair, instruction tuning, alignment, supervised fine-tuning을 정리한다. | 그림과 설명이 서로 맞도록 학습한다. |
| 4. Capabilities | VQA, captioning, grounding, OCR, document understanding, chart reasoning, video understanding을 다룬다. | 이미지 질문답변, 문서 읽기, 차트 해석까지 가능하다. |
| 5. Benchmarks | 멀티모달 reasoning과 시각 grounding을 측정하는 benchmark를 정리한다. | 그림을 제대로 봤는지 시험하는 기준이다. |
| 6. Challenges | hallucination, grounding failure, alignment error, privacy leakage, visual instruction vulnerability가 남는다. | 이미지를 잘못 보거나 이미지 속 지시에 속을 수 있다. |
| 7. Future Directions | trustworthy MLLM, robust grounding, privacy-aware multimodal learning, auditable deployment가 필요하다. | 멀티모달 AI도 안전하게 기록하고 검증해야 한다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 멀티모달 LLM 구조를 W07 보안 보고서에서 설명하기 위한 표준화된 표현이다. 원문 수식의 직접 전사가 아니라 구조 이해와 평가 지표 정의용이다. GitHub 호환성을 위해 `\operatorname`은 사용하지 않는다.

### 5.1 멀티모달 투영 구조

시각 입력은 visual encoder와 projector를 거쳐 LLM이 처리할 수 있는 표현으로 변환된다.

$$
h_v=P_{\phi}(E_v(x_v))
$$

| 기호 | 의미 |
|---|---|
| $x_v$ | 이미지, 비디오, 문서 캡처 등 시각 입력 |
| $E_v$ | visual encoder |
| $P_{\phi}$ | projector 또는 modality alignment module |
| $h_v$ | LLM context에 주입되는 visual representation |

### 보안적 의미

이미지 안의 텍스트, QR, 표, 차트, 문서 조각이 $h_v$로 변환되어 언어모델의 context에 영향을 준다. 따라서 시각 입력은 단순 첨부파일이 아니라 prompt의 일부로 취급해야 한다.

---

### 5.2 멀티모달 조건부 생성

MLLM 출력은 텍스트 prompt와 시각 표현을 함께 조건으로 사용한다.

$$
y_t \sim p_{\theta}\left(y_t \mid h_v, z, y_{1:t-1}\right)
$$

| 기호 | 의미 |
|---|---|
| $y_t$ | 생성되는 token |
| $h_v$ | 시각 표현 |
| $z$ | 사용자 prompt 또는 system instruction |
| $y_{1:t-1}$ | 이전 생성 token sequence |

### 보안적 의미

텍스트 system instruction과 이미지 내부 지시가 충돌할 수 있다. 문서 이미지 안에 모델 행동을 바꾸려는 문장이 포함되면 visual prompt injection 또는 OCR injection 위험이 생긴다.

---

### 5.3 Grounding Accuracy

시각 질문응답이나 문서 이해에서 모델 응답이 실제 시각 근거와 일치하는지 평가한다.

$$
GroundingAcc=\frac{N_{ground}}{N_{visual}}
$$

| 기호 | 의미 |
|---|---|
| $N_{ground}$ | 시각 근거와 일치한 답변 수 |
| $N_{visual}$ | 시각 정보 기반 질의 수 |

### 보안적 의미

Grounding 실패는 hallucination과 연결된다. 의료 이미지, 계약서, 신분증, 보안 로그 캡처처럼 고위험 문서에서는 근거 없는 시각 해석이 실제 피해로 이어질 수 있다.

---

### 5.4 Visual Jailbreak ASR

시각 입력을 이용해 안전정책을 우회하는 공격 성공률은 다음처럼 평가할 수 있다.

$$
ASR_{visual}=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}\left[f_{\theta}(x_{v,i}^{test},z_i)\in Y_{unsafe}\right]
$$

| 기호 | 의미 |
|---|---|
| $x_{v,i}^{test}$ | 안전성 평가용 toy 시각 입력 |
| $z_i$ | 함께 제공되는 텍스트 prompt |
| $Y_{unsafe}$ | 위험 또는 정책 위반 응답 집합 |

### 보안적 의미

시각 입력도 jailbreak 경로가 될 수 있다. 단, W07 보고서에서는 실제 유해 이미지 생성·배포가 아니라 안전한 toy 이미지/OCR 문장 기반 평가로 제한한다.

---

### 5.5 OCR Leakage Rate

이미지나 문서 속 민감정보가 출력으로 재노출되는 비율이다.

$$
OCRLeakage=\frac{N_{ol}}{N_{or}}
$$

| 기호 | 의미 |
|---|---|
| $N_{or}$ | 민감정보가 포함된 synthetic OCR/privacy-risk 평가 입력 수 |
| $N_{ol}$ | 민감정보가 출력 또는 로그에 노출된 사례 수 |

### 보안적 의미

문서 이미지의 OCR text는 prompt privacy 위험을 만든다. 로그에도 원본 이미지와 OCR 결과가 남을 수 있으므로 safe logging이 필요하다.

---

### 5.6 Alignment Consistency

시각 representation과 텍스트 representation의 의미 일관성을 측정한다.

$$
AlignConsistency=\frac{1}{N}\sum_{i=1}^{N}\mathrm{sim}(h_v^{(i)},h_t^{(i)})
$$

| 기호 | 의미 |
|---|---|
| $h_v^{(i)}$ | $i$번째 시각 representation |
| $h_t^{(i)}$ | $i$번째 텍스트 representation |
| $\mathrm{sim}$ | 유사도 함수 |

### 보안적 의미

Image-text alignment가 낮으면 모델은 시각 근거와 다른 텍스트 답변을 생성할 수 있다. 오염된 caption이나 잘못된 OCR 결과도 alignment를 왜곡할 수 있다.

---

### 5.7 Multimodal Security Risk

MLLM 보안 위험을 시각 입력, 텍스트 prompt, OCR, grounding, 도구 호출, 로그 위험으로 분해한다.

$$
MLLMRisk=VisualRisk+PromptRisk+OCRRisk+GroundingRisk+ToolRisk+LogRisk-MonitoringCoverage
$$

### 보안적 의미

MLLM 보안은 text prompt만 검사해서는 충분하지 않다. 이미지·OCR·문서·tool call·log까지 전체 경로를 점검해야 한다.

---

## 6. MLLM 보안 공격면

| 공격면 | 설명 | 대표 지표 |
|---|---|---|
| Visual Prompt Injection | 이미지 내부 텍스트가 모델 지시로 작동 | ASR_visual |
| OCR Injection | 문서·스크린샷의 OCR text가 context를 오염 | OCRLeakage, policy compliance |
| Grounding Failure | 모델이 실제 이미지와 맞지 않는 설명 생성 | GroundingAcc, hallucination rate |
| Multimodal Privacy Leakage | 이미지·문서 속 개인정보가 출력·로그에 노출 | OCRLeakage, LeakageRate |
| Cross-modal Mismatch | 텍스트와 이미지가 서로 다른 의미를 전달 | AlignConsistency |
| Tool Misuse | 이미지 해석 결과가 외부 도구 호출로 이어짐 | unsafe tool call rate |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | MLLM 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | 이미지·문서·OCR 결과에 개인정보·내부정보가 포함될 수 있음 | OCRLeakage, LeakageRate |
| 무결성 | 이미지 내부 지시나 caption 조작이 모델 판단을 왜곡 | ASR_visual, policy compliance |
| 가용성 | 이미지 처리/OCR/grounding 비용이 높아 운영 지연 발생 | latency, review load |
| 프라이버시 | 얼굴, 문서, 위치, OCR text가 prompt/output/log로 재노출 | privacy leakage, safe logging |
| 안전성 | visual jailbreak, grounding failure, hallucinated visual answer 위험 | GroundingAcc, unsafe rate |
| 책임성 | 이미지 출처, hash, OCR result, human review, output log가 필요 | source traceability, audit completeness |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 이미지, OCR text, 문서 스캔, chart, screenshot, visual embedding, system prompt, user prompt, output, tool call, audit log |
| 공격자 목표 | visual prompt injection, 정책 우회, 잘못된 grounding 유도, 개인정보 추출, tool misuse 유도 |
| 공격자 능력 | 이미지 내부 텍스트 삽입, caption 조작, 문서 이미지 오염, 멀티모달 context 삽입, 반복 질의 |
| 공격 경로 | visual input/OCR → visual encoder/projector → LLM context → output/tool call/log |
| 방어자 능력 | OCR 분리, source labeling, visual content filtering, context isolation, human review, output monitoring, safe logging |
| 제외 범위 | 실제 개인정보 이미지 사용, 유해 이미지 제작, 실제 서비스 대상 우회 실험, 공격 이미지 제작 절차 제공 |

---

## 9. 평가방법 및 지표

| 지표 | 의미 | W07/P04 활용 |
|---|---|---|
| VQA Accuracy | 이미지 기반 질의응답 정확도 | 기본 utility 평가 |
| GroundingAcc | 답변이 시각 근거와 일치하는지 | hallucination 평가 |
| ASR_visual | 시각 입력 기반 우회 성공률 | safety robustness |
| OCRLeakage | 이미지 속 민감정보가 출력되는 비율 | privacy 평가 |
| AlignConsistency | 이미지와 텍스트 의미 정합성 | cross-modal reliability |
| SourceTraceability | 이미지·문서 출처 기록 여부 | W14/W15 auditability |
| HumanReviewAgreement | 사람 검토와 모델 해석 일치 | high-stakes 평가 |
| UnsafeToolCallRate | 시각 해석에서 위험한 도구 호출 발생 비율 | agent safety |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | DOI, National Science Review 출판정보, arXiv 판본, 강의계획서 표기 차이, 로컬 PDF 상태 |
| Model | MLLM 모델명, 버전, visual encoder 정보, projector 설정 가능 여부 |
| Visual input | 이미지 hash, 출처, OCR 결과, 전처리 크기, synthetic 여부 |
| Text input | system prompt, user prompt, context 분리 |
| Evaluation setting | temperature, max tokens, seed 가능 여부, decoding 설정 |
| Output | raw output, grounding 판정, hallucination 여부, refusal 여부 |
| Security evaluation | ASR_visual, OCRLeakage, OCR injection 여부, unsafe tool call 여부 |
| Review | human review rubric, 판정 기준, 실패 사례 |
| Evidence | image hash, OCR log, prompt/output log, config, metric table |
| GitHub math | `\operatorname` 사용 금지, `y_{<t}` 대신 `y_{1:t-1}` 사용, 짧은 변수명과 `\mathrm{...}` 형태 사용 |

---

## 11. 논문의 고유 기여

1. 멀티모달 LLM의 구조와 학습·평가 흐름을 체계화한다.
2. text-only LLM 보안 평가로는 부족한 시각 입력·OCR·grounding 위험을 드러낸다.
3. W08 RAG에서 문서 이미지, 표, 차트, screenshot이 검색 context로 들어올 때의 보안 평가 근거가 된다.
4. W14/W15에서 시각 입력의 provenance, hash, OCR log, human review를 evidence chain에 포함해야 함을 뒷받침한다.
5. LLM security/privacy 논의를 multimodal privacy, visual prompt injection, visual grounding risk로 확장한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 빠른 모델 변화 | MLLM 구조와 benchmark는 빠르게 변한다. | 모델 버전과 평가일 기록 |
| 평가 데이터 복잡성 | 이미지·텍스트·OCR·grounding 정답이 필요하다. | toy dataset과 human review로 제한 |
| privacy 위험 | 실제 문서 이미지에는 민감정보가 포함될 수 있다. | synthetic 문서 이미지와 placeholder만 사용 |
| 시각 공격 악용 위험 | visual jailbreak 예시를 상세화하면 악용 가능성이 있다. | 방어·평가 중심으로만 기술 |
| 강의계획서 표기 차이 | 강의계획서의 `Yongtao Yin` 표기와 공식 저자 목록이 다르다. | DOI 기준 인용, 차이 메모 유지 |
| 로그 재유출 | 이미지와 OCR 결과를 그대로 저장하면 2차 유출 가능 | hash/OCR placeholder 중심 safe logging |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | LLM 보안이 text-only prompt에서 이미지·문서·OCR·tool workflow로 확장된다는 문제의식 |
| 2장 관련연구 | MLLM 구조, visual encoder, projector, visual instruction tuning survey 정리 |
| 3장 위협모형 | 이미지, OCR text, 문서 스캔, visual embedding, tool call, audit log 보호 자산 정의 |
| 4장 연구방법 | h_v projection, multimodal conditional generation, GroundingAcc, ASR_visual, OCRLeakage, AlignConsistency, MLLMRisk 지표 설계 |
| 5장 분석 | MLLM attack surface matrix와 visual/OCR/privacy evidence table 제시 |
| 6장 보안적 함의 | visual prompt injection, OCR leakage, grounding failure, source traceability, human review 필요성 해석 |
| 부록 | image hash, OCR log, prompt/output log, human review rubric, limitation statement 수록 |

---

## 14. 기말논문 연결 3문장

1. W07에서 기말논문에 반영할 개념: MLLM에서는 이미지와 문서 자체가 prompt의 일부가 되므로 visual prompt injection, OCR injection, grounding failure, multimodal privacy leakage를 별도로 평가해야 한다.
2. W07에서 기말논문에 반영할 표·그림·실험: visual encoder-projector-LLM 구조도, GroundingAcc, ASR_visual, OCRLeakage, AlignConsistency, MLLMRisk 수식표와 MLLM attack surface matrix를 반영한다.
3. W07이 W08/W14/W15와 연결되는 지점: RAG와 agent workflow에 이미지·문서·OCR 입력이 포함될 경우, source traceability, image hash, OCR log, human review, safe logging을 evidence chain으로 남겨야 한다.

---

## 15. 최종 판단

P04는 W07의 멀티모달 LLM 확장 핵심 문헌이다. Text-only LLM 보안 평가는 prompt와 output 중심이지만, MLLM에서는 이미지·OCR·문서·차트·비디오·visual grounding이 모두 공격면이 된다. 따라서 기말논문에서는 P04를 **MLLM 구조, visual prompt injection, OCR leakage, grounding failure, multimodal privacy, source traceability, human review evidence의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. GitHub 수식 호환성 메모

이 파일에서는 GitHub 수식 렌더링 오류 방지를 위해 `\operatorname`을 사용하지 않는다.

| 피해야 할 표현 | 권장 표현 |
|---|---|
| `y_{<t}` | `y_{1:t-1}` |
| `x_{text}` | `z` 또는 표에서 설명한 짧은 변수명 |
| `N_{ocr\ leak}` | `N_{ol}`처럼 짧은 변수명 사용 후 표에서 의미 설명 |
| `\operatorname{softmax}` | `\mathrm{softmax}` |
| `\operatorname{sim}` | `\mathrm{sim}` |
| 긴 영문 subscript | 짧은 변수명 사용 후 표에서 의미 설명 |

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
