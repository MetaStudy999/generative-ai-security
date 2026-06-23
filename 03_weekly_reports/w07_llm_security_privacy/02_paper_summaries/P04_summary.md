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
| 강의계획서 표기와 차이 | 강의계획서에는 `Yongtao Yin et al.`로 표기되어 있으나, repo의 공식 확인 정보는 `Shukang Yin et al.`임 |
| 핵심 근거 사용 가능 여부 | 가능. W07의 text-only LLM 보안을 멀티모달 LLM 보안으로 확장하는 핵심 문헌 |

---

## 1. 한 문장 요약

이 논문은 멀티모달 대규모 언어모델을 **visual encoder, projector, LLM backbone, image-text alignment, instruction tuning, multimodal reasoning, benchmark** 관점에서 정리하여, 이미지·비디오·문서·OCR·텍스트가 결합될 때 LLM 보안 공격면이 prompt뿐 아니라 시각 입력과 cross-modal alignment까지 확장됨을 보여주는 핵심 survey 문헌이다.

---

## 2. 핵심 연구문제

> 멀티모달 LLM은 시각·언어 정보를 어떻게 결합하며, 이 결합 구조는 어떤 새로운 보안·프라이버시 위협을 만드는가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | MLLM은 visual encoder, projector, LLM backbone을 어떻게 결합하는가? |
| RQ2 | Image-text alignment와 visual instruction tuning은 모델 성능과 취약성에 어떤 영향을 주는가? |
| RQ3 | 이미지 내부의 텍스트, 문서 캡처, OCR 결과, 표·차트가 prompt injection 경로가 될 수 있는가? |
| RQ4 | 멀티모달 hallucination, grounding failure, visual jailbreak, privacy leakage는 어떤 지표로 평가해야 하는가? |
| RQ5 | W08 RAG 및 W14 MLOps에서 멀티모달 입력의 provenance와 audit log를 어떻게 관리해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W07 연결 |
|---|---|---|
| MLLM 구조 정리 | visual encoder, projector, LLM backbone의 연결 구조 설명 | 멀티모달 위협모형의 시스템 구조 제공 |
| Instruction tuning 분석 | image-text instruction data의 역할과 한계 정리 | fine-tuning data provenance 위험 연결 |
| Benchmark taxonomy | VQA, captioning, grounding, reasoning benchmark 정리 | text-only 평가 지표의 한계 보완 |
| Cross-modal reasoning | 시각 정보와 언어 추론의 결합 설명 | RAG 문서·이미지 입력 보안 연결 |
| 최신 응용 범위 | OCR, chart, document, video, embodied AI로 확장 | W08/W14/W15와 연결 |

---

## 4. 핵심 이론 및 수식

> 아래 수식은 멀티모달 LLM 구조를 W07 보안 보고서에서 설명하기 위한 표준화된 표현이다. 원문 수식의 직접 전사가 아니라 구조 이해와 평가 지표 정의용이다.

### 4.1 멀티모달 투영 구조

시각 입력은 visual encoder와 projector를 거쳐 LLM이 처리할 수 있는 표현으로 변환된다.

$$
h_v=P_\phi(E_v(x_v))
$$

| 기호 | 의미 |
|---|---|
| $x_v$ | 이미지, 비디오, 문서 캡처 등 시각 입력 |
| $E_v$ | visual encoder |
| $P_\phi$ | projector 또는 modality alignment module |
| $h_v$ | LLM context에 주입되는 visual representation |

### 보안적 의미

이미지 안의 텍스트, QR, 표, 차트, 문서 조각이 $h_v$로 변환되어 언어모델의 context에 영향을 준다. 따라서 시각 입력은 단순 첨부파일이 아니라 prompt의 일부로 취급해야 한다.

---

### 4.2 멀티모달 조건부 생성

MLLM 출력은 텍스트 prompt와 시각 표현을 함께 조건으로 사용한다.

$$
y_t\sim p_\theta(y_t\mid h_v,x_{text},y_{<t})
$$

| 기호 | 의미 |
|---|---|
| $y_t$ | 생성되는 토큰 |
| $h_v$ | 시각 표현 |
| $x_{text}$ | 사용자 프롬프트 또는 시스템 지시 |
| $y_{<t}$ | 이전 생성 토큰 |

### 보안적 의미

텍스트 시스템 지시와 이미지 내부 지시가 충돌할 수 있다. 예를 들어 문서 이미지 안에 모델 행동을 바꾸려는 문장이 포함되면 visual prompt injection 또는 OCR injection 위험이 생긴다.

---

### 4.3 Grounding Accuracy

시각 질문응답이나 문서 이해에서 모델 응답이 실제 시각 근거와 일치하는지 평가할 수 있다.

$$
GroundingAcc=\frac{N_{grounded\ answers}}{N_{visual\ questions}}
$$

| 기호 | 의미 |
|---|---|
| $N_{grounded\ answers}$ | 시각 근거와 일치한 답변 수 |
| $N_{visual\ questions}$ | 시각 정보 기반 질의 수 |

### 보안적 의미

Grounding 실패는 hallucination과 연결된다. 특히 의료 이미지, 계약서, 신분증, 보안 로그 캡처처럼 고위험 문서에서는 근거 없는 시각 해석이 실제 피해로 이어질 수 있다.

---

### 4.4 Visual Jailbreak ASR

시각 입력을 이용해 안전정책을 우회하는 공격 성공률은 다음처럼 평가할 수 있다.

$$
ASR_{visual}=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[f_\theta(x_{v,i}^{attack},x_{text,i})\in Y_{unsafe}]
$$

| 기호 | 의미 |
|---|---|
| $x_{v,i}^{attack}$ | 안전성 평가용 변형 시각 입력 |
| $x_{text,i}$ | 함께 제공되는 텍스트 프롬프트 |
| $Y_{unsafe}$ | 위험 또는 정책 위반 응답 집합 |

### 보안적 의미

시각 입력도 jailbreak 경로가 될 수 있다. 단, W07 보고서에서는 실제 유해 이미지 생성·배포가 아니라 안전한 toy 이미지/OCR 문장 기반 평가로 제한한다.

---

## 5. MLLM 보안 공격면

| 공격면 | 설명 | 대표 지표 |
|---|---|---|
| Visual Prompt Injection | 이미지 내부 텍스트가 모델 지시로 작동 | visual jailbreak ASR |
| OCR Injection | 문서·스크린샷의 OCR 텍스트가 context를 오염 | OCR leakage, policy compliance |
| Grounding Failure | 모델이 실제 이미지와 맞지 않는 설명 생성 | grounding accuracy, hallucination rate |
| Multimodal Privacy Leakage | 이미지·문서 속 개인정보가 출력·로그에 노출 | leakage rate |
| Cross-modal Mismatch | 텍스트와 이미지가 서로 다른 의미를 전달 | alignment consistency |
| Tool Misuse | 이미지 해석 결과가 외부 도구 호출로 이어짐 | unsafe tool call rate |

---

## 6. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | 이미지, OCR 텍스트, 문서 스캔, visual embedding, system prompt, user prompt, output, tool call, audit log |
| 공격자 목표 | visual prompt injection, 정책 우회, 잘못된 grounding 유도, 개인정보 추출, tool misuse 유도 |
| 공격자 능력 | 이미지 내부 텍스트 삽입, caption 조작, 문서 이미지 오염, 멀티모달 context 삽입, 반복 질의 |
| 방어자 능력 | OCR 분리, source labeling, visual content filtering, context isolation, human review, output monitoring |
| 제외 범위 | 실제 개인정보 이미지 사용, 유해 이미지 제작, 실제 서비스 대상 우회 실험 |

---

## 7. 평가방법 및 지표

| 지표 | 의미 | W07/P04 활용 |
|---|---|---|
| VQA Accuracy | 이미지 기반 질의응답 정확도 | 기본 utility 평가 |
| Grounding Accuracy | 답변이 시각 근거와 일치하는지 | hallucination 평가 |
| Visual Jailbreak ASR | 시각 입력 기반 우회 성공률 | safety robustness |
| OCR Leakage Rate | 이미지 속 민감정보가 출력되는 비율 | privacy 평가 |
| Alignment Consistency | 이미지와 텍스트 의미 정합성 | cross-modal reliability |
| Source Traceability | 이미지·문서 출처 기록 여부 | W14/W15 auditability |
| Human Review Agreement | 사람 검토와 모델 해석 일치 | high-stakes 평가 |

---

## 8. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| 모델 | MLLM 모델명, 버전, visual encoder 정보, projector 설정 가능 여부 |
| 시각 입력 | 이미지 hash, 출처, OCR 결과, 전처리 크기 |
| 텍스트 입력 | system prompt, user prompt, context 분리 |
| 평가 설정 | temperature, max tokens, seed 가능 여부, decoding 설정 |
| 출력 | raw output, grounding 판정, hallucination 여부 |
| 보안 평가 | visual jailbreak ASR, leakage rate, OCR injection 여부 |
| 검토 | human review rubric, 판정 기준, 실패 사례 |
| 한계 | toy image 결과를 실제 MLLM 안전성 보증으로 일반화하지 않음 |

---

## 9. 논문의 고유 기여

1. 멀티모달 LLM의 구조와 학습·평가 흐름을 체계화한다.
2. text-only LLM 보안 평가로는 부족한 시각 입력·OCR·grounding 위험을 드러낸다.
3. W08 RAG에서 문서 이미지, 표, 차트, screenshot이 검색 context로 들어올 때의 보안 평가 근거가 된다.
4. W14/W15에서 시각 입력의 provenance, hash, OCR log, human review를 evidence chain에 포함해야 함을 뒷받침한다.

---

## 10. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 빠른 모델 변화 | MLLM 구조와 benchmark는 빠르게 변한다. | 모델 버전과 평가일 기록 |
| 평가 데이터 복잡성 | 이미지·텍스트·OCR·grounding 정답이 필요하다. | toy dataset과 human review로 제한 |
| privacy 위험 | 실제 문서 이미지에는 민감정보가 포함될 수 있다. | synthetic 이미지와 공개 예시만 사용 |
| defense 일반화 한계 | OCR 필터링만으로 모든 visual injection을 막기 어렵다. | source labeling과 context isolation 병행 |
| 보안 직접성 제한 | MLLM survey이며 공격 전문 논문은 아니다. | P02/P03 보안 문헌 및 W08 prompt injection 문헌과 결합 |

---

## 11. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | LLM 보안이 text-only에서 multimodal context 보안으로 확장된다는 문제의식 |
| 2장 관련연구 | MLLM 구조, visual encoder, instruction tuning, benchmark 정리 |
| 3장 위협모형 | visual prompt injection, OCR leakage, grounding failure 정의 |
| 4장 연구방법 | VQA accuracy, grounding accuracy, visual ASR, OCR leakage rate 지표 설계 |
| 5장 분석 | toy visual/OCR injection 평가와 한계 제시 |
| 6장 보안적 함의 | 문서 이미지·차트·표·스크린샷 사용 시 human review와 source audit 필요성 |

---

## 12. 기말논문 연결 3문장

1. 이 주차에서 기말논문에 반영할 개념: 멀티모달 LLM에서는 이미지와 문서가 단순 입력 자료가 아니라 모델 행동에 영향을 주는 prompt context이므로 보안 자산으로 관리해야 한다.
2. 이 주차에서 기말논문에 반영할 표·그림·실험: MLLM 구조도, multimodal projection 수식, grounding accuracy, visual jailbreak ASR, OCR leakage 평가표를 반영한다.
3. 이 주차가 RAG 문서 오염/LLM 보안 감사 프레임워크와 연결되는 지점: W08 RAG에서 PDF·이미지·표·스크린샷이 검색 근거로 들어오면 W07/P04의 visual provenance와 OCR audit가 필수 통제가 된다.

---

## 13. 최종 판단

P04는 W07의 멀티모달 확장 핵심 문헌이다. LLM 보안 평가가 텍스트 프롬프트만 다루면 불완전하며, 시각 입력·OCR·문서 이미지·grounding·human review를 함께 고려해야 한다.

---

## 14. 변환 호환성 메모

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
