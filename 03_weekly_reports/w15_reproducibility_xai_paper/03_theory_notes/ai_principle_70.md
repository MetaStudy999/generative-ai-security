# AI 원리 70% 정리

## 1. 핵심 이론

W15의 AI 원리는 Evaluation, reproducibility, XAI, paper structure이다. 이 주차에서는 보안 이슈를 먼저 끌어오지 않고, 모델 또는 시스템이 어떤 학습 구조와 평가 구조를 갖는지 이해하는 데 70%의 비중을 둔다.

핵심 항목은 다음과 같다.

- LLM 평가 프레임워크
- Benchmark contamination
- Evaluation leakage
- Reproducibility의 의미
- ML lifecycle assurance
- XAI의 핵심 개념
- Feature-based explanation
- Concept-based explanation
- Responsible AI와 XAI의 관계

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 |
|---|---|---|---|
| LLM 평가 프레임워크 | 연구평가·재현성·설명가능성(XAI)·논문 구성에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 1번째 관찰 지점 | P01 |
| Benchmark contamination | 연구평가·재현성·설명가능성(XAI)·논문 구성에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 2번째 관찰 지점 | P02 |
| Evaluation leakage | 연구평가·재현성·설명가능성(XAI)·논문 구성에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 3번째 관찰 지점 | P03 |
| Reproducibility의 의미 | 연구평가·재현성·설명가능성(XAI)·논문 구성에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 4번째 관찰 지점 | P04 |
| ML lifecycle assurance | 연구평가·재현성·설명가능성(XAI)·논문 구성에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 5번째 관찰 지점 | P05 |
| XAI의 핵심 개념 | 연구평가·재현성·설명가능성(XAI)·논문 구성에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 6번째 관찰 지점 | P05 |
| Feature-based explanation | 연구평가·재현성·설명가능성(XAI)·논문 구성에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 7번째 관찰 지점 | P05 |
| Concept-based explanation | 연구평가·재현성·설명가능성(XAI)·논문 구성에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 8번째 관찰 지점 | P05 |
| Responsible AI와 XAI의 관계 | 연구평가·재현성·설명가능성(XAI)·논문 구성에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 9번째 관찰 지점 | P05 |

## 3. 수식 또는 알고리즘

```text
입력/데이터 정의 -> LLM 평가 프레임워크 -> Benchmark contamination -> Evaluation leakage -> Reproducibility의 의미 -> 모델 또는 시스템 출력 -> 평가 지표 산출
```

수식 수준에서는 학습 목적함수, 평가 지표, 일반화 또는 효율성 조건을 분리해 기록한다. 세부 수식은 원문 확인 후 최종 논문에 필요한 것만 엄선한다.

## 4. 초보자용 설명

연구평가/재현성/설명가능성(XAI)/논문 구성를 공부할 때 먼저 볼 것은 "모델이 무엇을 입력으로 받고, 무엇을 학습하며, 어떤 기준으로 성공을 판단하는가"이다. 이 구조를 이해해야 공격자가 어느 지점을 건드릴 수 있는지도 보인다.

## 5. 보안 연구와의 연결

AI 원리의 취약 지점은 곧 보안 평가 항목이 된다. LLM 평가 프레임워크, Benchmark contamination, Evaluation leakage를 이해하면 Benchmark contamination, Hidden test leakage, Evaluation reproducibility failure가 왜 발생하는지 설명할 수 있다.
