# W14 MLOps/DevOps·데이터/모델 파이프라인·공급망 보안

운영형 AI 시스템 보안은 accuracy가 아니라 evidence를 요구한다.

---

## 오늘의 질문

- 모델은 어떤 데이터와 config에서 만들어졌는가?
- 배포된 model artifact는 바뀌지 않았는가?
- 운영 입력 분포가 변했는가?
- 사고 후 로그로 추적할 수 있는가?

---

## MLOps 원리

- MLOps는 ML, software engineering, data engineering, operations의 결합이다.
- DevOps보다 dataset, feature, model, monitoring, retraining 변수를 더 많이 가진다.
- 핵심 단위는 모델 파일이 아니라 lifecycle이다.

---

## 공급망 보안 위협

| 자산 | 위협 |
|---|---|
| Data pipeline | poisoning, provenance loss |
| Model artifact | tampering, unauthorized update |
| Config/seed | irreproducible result |
| Logs/monitoring | leakage, missing audit trail |

---

## 논문 패킷 역할

P01은 MLOps practice, P02는 deployment challenge, P03은 AIOps monitoring, P04는 edge deployment, P05는 DL for SE와 software pipeline을 맡는다.

P03/P04/P05는 로컬 PDF가 대체문헌이므로 공식 원문 확인이 필요하다.

---

## Toy Pipeline 설계

- Synthetic binary classification
- Seed 42, train/test 320/160
- Toy logistic regression
- Dataset/config/model hash 기록
- Drift score, audit coverage, artifact inventory 생성

---

## 실행 결과

| 항목 | 값 |
|---|---:|
| Accuracy | 0.925000 |
| F1 | 0.923077 |
| Drift score | 0.307626 |
| Audit coverage | 1.000000 |
| Inventory coverage | 1.000000 |

---

## 해석

Drift score 0.307626은 threshold 0.25를 넘었다. 이는 공격 단정이 아니라 운영 감시 경보이며, 원인 분석과 human review가 필요하다.

---

## 기말논문 연결

W14는 운영형 AI 시스템의 보안·재현성 보증을 위한 evidence set으로 연결된다.

최소 지표: dataset hash, model hash, config hash, drift score, audit coverage, artifact inventory.

---

## 결론

MLOps 공급망 보안은 모델 성능을 넘어 데이터, 모델, config, 로그, 모니터링, 검증 절차를 함께 남기는 문제다.
