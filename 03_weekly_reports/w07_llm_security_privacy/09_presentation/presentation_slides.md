# W07 LLM 학습·정렬·평가 & LLM 보안·프라이버시

## 발표 핵심

LLM 보안 평가는 utility, ASR, privacy leakage, refusal quality, code vulnerability risk, 재현성을 함께 기록해야 한다.

---

# 1. 왜 W07이 중요한가

- LLM은 모델 하나가 아니라 prompt, context, output, log, benchmark가 얽힌 시스템이다.
- 평가가 오염되면 성능 해석도 보안 판단도 흔들린다.
- W07의 질문: “LLM 시스템을 보안적으로 믿으려면 무엇을 함께 측정해야 하는가?”

---

# 2. 발표 로드맵

1. LLM 학습·정렬·평가 원리
2. LLM 보안·프라이버시 위협
3. 논문 5편의 역할
4. Synthetic toy 실험
5. 결과와 기말논문 연결

---

# 3. AI 원리 70%

| 개념 | 핵심 | 보안 연결 |
|---|---|---|
| Pretraining | 대규모 데이터 학습 | memorization |
| Instruction tuning | 지시 따르기 | unsafe instruction |
| Alignment/RLHF | 선호와 안전 정책 | refusal quality |
| Context window | 입력과 context 결합 | prompt injection |
| Benchmark | 능력 측정 | contamination |

---

# 4. 평가 원리

- Benchmark score는 모델 능력의 일부만 보여준다.
- Contamination은 평가셋이 학습이나 프롬프트에 노출되는 문제다.
- Evaluation leakage는 hidden test나 기준이 새는 문제다.
- 재현성에는 seed, config, prompt set, output log가 필요하다.

---

# 5. 보안 이슈 30%

| 위협 | 보호 자산 | 대표 지표 |
|---|---|---|
| Data extraction | 학습데이터 | leakage rate |
| Prompt injection | context, tool chain | ASR |
| Prompt leakage | system prompt | leakage flag |
| Insecure code | 코드 산출물 | vulnerability rate |
| Over-refusal | 정상 사용자 workflow | answer rate |

---

# 6. 논문 5편의 역할

| ID | 중심 역할 | W07 활용 |
|---|---|---|
| P01 | LLM evaluation survey | 평가축과 benchmark |
| P02 | security/privacy challenges | 공격·방어 분류 |
| P03 | good/bad/ugly taxonomy | 보안 활용과 취약성 |
| P04 | multimodal LLM survey | MLLM 구조와 hallucination |
| P05 | software security with LLMs | 코드 보안 접점 |

---

# 7. 위협모형

```text
User prompt -> Context window -> LLM response -> Logs / Code / Benchmark
      |              |                 |                 |
 prompt attack   prompt leakage    unsafe output     audit failure
```

- 보호 자산: 데이터, system prompt, context, output, code, logs, benchmark
- 제외 범위: 실제 개인정보 추출, 실제 서비스 공격, exploit instruction

---

# 8. 평가 프로토콜

| 평가 항목 | 지표 | 기록 방법 |
|---|---|---|
| Utility | utility, answer rate | clean prompts |
| Attack success | ASR | synthetic risky prompts |
| Privacy | leakage rate | synthetic privacy-risk prompts |
| Refusal | refusal quality, over-refusal | risk/clean 분리 |
| Code security | vulnerability rate | code security category |
| Reproducibility | seed, config, outputs | CSV/JSON/run log |

---

# 9. Synthetic toy 실험

- 데이터: synthetic prompt categories
- 조건: clean, prompt attack simulation, privacy-risk, code security
- 각 조건: 40개 synthetic sample
- Guard threshold: 0.55
- 실제 LLM/API 호출 없음

---

# 10. 실험 결과

| 조건 | Utility | Answer | ASR | Leakage | Refusal | Over-refusal | Code risk |
|---|---:|---:|---:|---:|---:|---:|---:|
| Clean | 0.866746 | 1.000000 | 0.000000 | 0.000000 | 해당 없음 | 0.000000 | 0.000000 |
| Prompt attack | 0.400908 | 0.150000 | 0.150000 | 0.000000 | 0.850000 | 0.000000 | 0.000000 |
| Privacy-risk | 0.392926 | 0.100000 | 0.100000 | 0.025000 | 0.900000 | 0.000000 | 0.000000 |
| Code security | 0.678267 | 0.650000 | 0.000000 | 0.000000 | 해당 없음 | 0.350000 | 0.200000 |

정량값은 `04_experiment/outputs/run_log.md` 기준이다.

---

# 11. 결과 해석

- Clean utility 0.866746은 정상 질의 지원성을 보여준다.
- Prompt attack simulation의 ASR 0.150000은 toy guard가 일부 synthetic 위험 조건을 놓친다는 뜻이다.
- Privacy-risk leakage 0.025000은 평가표에 privacy 항목을 분리해야 함을 보여준다.
- Code security의 over-refusal 0.350000과 code risk 0.200000은 함께 봐야 한다.
- 이 수치는 실제 LLM의 보안 성능이나 실제 jailbreak 성공률이 아니다.

---

# 12. 기말논문 연결

| 기말논문 장 | 연결 내용 |
|---|---|
| 관련연구 | LLM evaluation/security/privacy/software security |
| 위협모형 | prompt/context/output/log/benchmark |
| 평가방법 | utility, ASR, leakage, refusal, code risk |
| 재현성 | seed, config, CSV/JSON/run log |

Contribution 후보: LLM/RAG 기반 AI 시스템의 보안·프라이버시·재현성 평가 프레임워크.

---

# 13. 결론

W07 결론:

- LLM 보안 평가는 다중지표 문제다.
- 공격 성공률만 보면 utility와 over-refusal을 놓친다.
- Utility만 보면 leakage와 code risk를 놓친다.
- 실행 로그 없는 수치는 주장하지 않는다.
