# P01 Summary

## A Review of Abstraction Methods Toward Verifying Neural Networks — Fateh Boudardara et al., ACM TECS, 2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W12 Neural Network Verification & XAI Robustness |
| 논문명 | A Review of Abstraction Methods Toward Verifying Neural Networks |
| 저자 | Fateh Boudardara et al. |
| 출판 정보 | ACM Transactions on Embedded Computing Systems, 2024 |
| DOI | https://doi.org/10.1145/3617508 |
| 검증 상태 | W12 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 관련 보조 문헌이므로 판본 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 신경망 검증을 위한 abstraction 방법을 **state-space abstraction, over-approximation, reachability, safety property, robustness certification** 관점에서 정리하며, W12에서 DNN 보안 주장을 형식적으로 검토하는 핵심 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | 신경망 검증에서 abstraction은 어떤 방식으로 상태공간 폭발을 줄이는가? |
| RQ2 | Over-approximation과 reachability는 safety property 검증에 어떻게 쓰이는가? |
| RQ3 | 형식 검증 결과는 empirical adversarial testing과 어떻게 구분해야 하는가? |
| RQ4 | AI 보안 보고서에서 certification claim을 어떻게 제한적으로 표현해야 하는가? |

---

## 3. 핵심 수식

### 3.1 Robustness Property

$$
\forall x' \in B_\epsilon(x), \quad f(x')=f(x)
$$

### 3.2 Reachable Set Over-approximation

$$
Reach(f, X) \subseteq \widehat{R}
$$

**보안 해석:** 검증은 특정 입력 영역과 명세에 대한 보장이지, 모든 운영 환경 안전성을 자동으로 보장하지 않는다.

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | DNN decision, safety property, input domain, verification certificate |
| 공격자 목표 | 검증되지 않은 입력 영역에서 오분류 유도 |
| 지표 | verified robustness radius, verified rate, verification time, false proof risk |
| 재현성 | model, property, input bounds, solver, timeout, certificate log 기록 |

---

## 5. 기말논문 연결

P01은 AI 보안 주장의 “검증 가능성”을 설명한다. 기말논문에서는 empirical test와 formal certificate를 구분하는 평가표로 반영한다.

---

## 6. 최종 판단

P01은 W12의 formal verification 핵심 문헌이다. 로컬 PDF와 지정 문헌 차이 메모를 유지하고 공식 DOI 기준으로 인용한다.
