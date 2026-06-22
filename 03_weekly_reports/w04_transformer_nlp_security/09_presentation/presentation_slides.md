# W04 Transformer 변형 & NLP 대적공격·프라이버시

## 발표 핵심

프롬프트 기반 NLP 보안 평가는 clean score 하나로 끝나지 않는다. 단어 치환 공격 영향, privacy leakage, utility, 재현성 근거를 분리해야 한다.

---

# 1. 왜 W04가 중요한가

- Transformer는 NLP와 LLM 시스템의 기본 구조다.
- 긴 프롬프트와 ICL 예시는 성능을 높이지만 민감정보 노출면도 넓힌다.
- W04의 질문: “좋은 Transformer 입력 처리”는 프롬프트 보안까지 보장하는가?

---

# 2. 발표 로드맵

1. Transformer와 self-attention 원리
2. Efficient Transformer와 X-former 계열
3. NLP 대적공격과 프롬프트 프라이버시
4. 논문 5편의 역할
5. Synthetic toy 실험과 결과
6. 기말논문 연결

---

# 3. AI 원리 70%: Attention

- Self-attention은 입력 토큰 사이의 관계를 계산한다.
- Query는 찾는 정보, Key는 비교 기준, Value는 전달 정보를 맡는다.
- Multi-head attention은 여러 관계 패턴을 병렬로 본다.
- Positional encoding은 토큰 순서 정보를 보완한다.

핵심 연결: 긴 입력일수록 성능뿐 아니라 보안 평가 비용도 커진다.

---

# 4. AI 원리 70%: Efficient Transformer

| 접근 | 핵심 | 보안 연결 |
|---|---|---|
| Sparse attention | 일부 토큰 관계만 계산 | 긴 프롬프트 평가 비용 절감 |
| Low-rank approximation | attention 행렬 근사 | 효율과 정보 손실 trade-off |
| Kernelized attention | attention 계산식 변환 | 긴 입력 처리 확장 |
| Distillation/Pruning | 모델 경량화 | 방어 로직 배치 비용 감소 |

---

# 5. 보안 이슈 30%

| 위협 | 공격자 능력 | 대표 지표 |
|---|---|---|
| Word substitution | 민감 키워드 우회 표현 사용 | ASR |
| Sentence rewrite | 표면형 변경 | semantic similarity |
| Prompt privacy | 민감정보 입력·로그 노출 | privacy leakage |
| ICL leakage | 예시 안의 민감정보 재노출 | masking success |

---

# 6. 논문 5편의 역할

| ID | 중심 역할 | W04 활용 |
|---|---|---|
| P01 | Efficient Transformer survey | X-former 분류 |
| P02 | Faster/lighter Transformer | 실용적 효율화 trade-off |
| P03 | Transformer taxonomy | 구조·응용 분류 |
| P04 | NLP adversarial defenses | 공격/방어 taxonomy |
| P05 | Prompt privacy survey | ICL과 prompt protection |

---

# 7. 위협모형

```text
User Text / Prompt -> Detector or LLM -> Response -> Log
        |                  |              |         |
 word substitution     wrong risk      leakage   audit gap
 sensitive value       decision        output    missing run
```

- 보호 자산: 입력 문장, 프롬프트, synthetic 민감값, 응답, 로그
- 공격 경로: 단어 치환, 민감정보 삽입, ICL 예시
- 제외 범위: 실제 개인정보, 실제 서비스 공격, 무단 API 질의

---

# 8. 평가 프로토콜

| 평가 항목 | 지표 | 기록 방법 |
|---|---|---|
| Clean performance | clean score | 정상 synthetic 입력 |
| Attack impact | ASR | 단어 치환 후 오분류 |
| Privacy | privacy leakage | 원시 민감값 잔존 여부 |
| Utility | utility score | task intent 유지 여부 |
| Reproducibility | seed, config, outputs | CSV/JSON/run log |

---

# 9. Synthetic toy 실험

- 데이터: synthetic privacy-risk prompts
- 분류기: keyword privacy-risk detector
- 공격: `password`, `ssn`, `token` 우회 표현 치환
- 방어: regex masking + privacy-preserving prompt wrapper
- 출력: `metrics_summary.csv`, `results.json`, `run_log.md`

안전 범위: 실제 개인정보와 실제 서비스 공격 없음.

---

# 10. 실험 결과

| 조건 | Clean Score | ASR | Leakage | Utility |
|---|---:|---:|---:|---:|
| Clean baseline | 1.000000 | 해당 없음 | 해당 없음 | 1.000000 |
| Word substitution | 0.625000 | 0.750000 | 해당 없음 | 1.000000 |
| Prompt masking | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 |
| Privacy-preserving prompt | 해당 없음 | 해당 없음 | 0.000000 | 1.000000 |

정량값은 `04_experiment/outputs/run_log.md` 기준이다.

---

# 11. 결과 해석과 한계

- 단어 치환 후 4개 privacy-risk 입력 중 3개가 benign으로 오분류됐다.
- 마스킹은 synthetic 원시 민감값 패턴을 제거했다.
- 이는 toy 설정의 관찰값이며 실제 LLM 보안 성능으로 일반화하지 않는다.
- 핵심은 수치 자체보다 지표 분리와 재현성 기록 방식이다.

---

# 12. 기말논문 연결

| 기말논문 장 | 연결 내용 |
|---|---|
| 관련연구 | Transformer 효율화와 prompt privacy 문헌 연결 |
| 위협모형 | 입력, ICL 예시, 로그의 민감정보 위험 |
| 평가방법 | clean, ASR, leakage, utility 분리 |
| 분석/실험 | synthetic toy 평가를 통한 지표 구조 예시 |

Contribution 후보: 프롬프트 기반 AI 시스템의 민감정보 보호 평가체계.

---

# 13. 결론

W04 결론:

- Transformer 효율화는 보안성 보장이 아니라 평가 기반 조건이다.
- NLP 공격은 clean 성능과 별도 지표로 봐야 한다.
- Prompt privacy는 leakage와 utility를 함께 봐야 한다.
- DOI/URL, seed, config, outputs가 있어야 제출 수치를 주장할 수 있다.
