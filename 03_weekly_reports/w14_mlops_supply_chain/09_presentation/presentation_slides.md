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

Drift score 0.307626은 threshold 0.25를 넘었다. 이는 공격 단정이나 실제 장애 확률이 아니라 운영 감시 경보이며, 원인 분석과 human review가 필요하다.

Audit coverage와 inventory coverage는 toy evidence coverage다. 실제 기업 감사 완전성이나 완전한 AI BOM을 의미하지 않는다.

---

## 기말논문 연결

W14는 운영형 AI 시스템의 보안·재현성 보증을 위한 evidence set으로 연결된다.

최소 지표: dataset hash, model hash, config hash, drift score, audit coverage, artifact inventory.

운영 확장: SBOM, license, vulnerability scan, model registry ACL, approval record.

---

## 결론

MLOps 공급망 보안은 모델 성능을 넘어 데이터, 모델, config, 로그, 모니터링, 검증 절차를 함께 남기는 문제다.

<!-- formula-visual-supplement:start -->
# 수식·그래프·그림 보강

- 보강 일자: 2026-06-23
- 수식은 표준 정의식 또는 검증 가능한 평가식으로만 작성했다.
- 그래프는 `04_experiment/outputs/metrics_summary.csv`의 기존 수치만 사용했다.
- 다이어그램은 AI-assisted conceptual diagram이며 사실 자료나 실험 결과처럼 해석하지 않는다.

### 핵심 수식: Artifact Integrity Check

$$
pass(a)=\mathbf{1}[H(a)=H_{ref}(a)]
$$

| 기호 | 의미 |
|---|---|
| `a` | artifact |
| `H` | hash function |
| `H_{ref}` | 기준 hash |
| `pass(a)` | 무결성 확인 결과 |

**직관적 의미:**  
공급망 보안은 artifact가 기준 hash와 일치하는지 확인하는 것에서 시작한다.

**보안 관점 해석:**  
데이터, 모델, config의 변경 여부를 추적해야 재현성과 책임성이 유지된다.

**평가 지표 연결:**  
model_hash_match, dataset_sha256, inventory_coverage와 연결한다.

**한계와 가정:**  
hash 검증은 무결성 근거이지 모델 안전성 전체 보증이 아니다.

### 핵심 수식: Drift와 Audit Coverage

$$
d=\lVert \mu_{new}-\mu_{train}\rVert_2,
\qquad
Coverage=\frac{|\{\mathrm{required\ logs\ present}\}|}{|\{\mathrm{required\ logs}\}|}
$$

| 기호 | 의미 |
|---|---|
| `d` | 분포 이동 proxy |
| `\mu_{new}` | 새 입력 평균 특징 |
| `\mu_{train}` | 훈련 기준 평균 특징 |
| `Coverage` | 필수 로그 보존률 |

**직관적 의미:**  
Drift는 배포 후 입력 분포 변화를 감시하는 간단한 proxy다. Audit coverage는 최소 증거가 남아 있는지를 본다.

**보안 관점 해석:**  
공급망 공격은 성능보다 provenance와 audit evidence 부족에서 먼저 드러날 수 있다.

**평가 지표 연결:**  
mean_standardized_feature_shift, audit_coverage, inventory_coverage와 연결한다.

**한계와 가정:**  
toy MLOps inventory이며 실제 조직의 완전한 SBOM/AI BOM은 별도 검토가 필요하다.

### 표 수치 기반 그래프

![W14 metrics chart](assets/charts/w14_metrics_chart.png)

그래프는 numeric value로 변환 가능한 MLOps 점검 항목만 표시한다. Hash 문자열이나 boolean pass는 그래프에서 제외하고 manifest와 로그 근거로 남겼다. 값은 `metrics_summary.csv`에서만 읽었다.

### Threat Model / Pipeline Diagram

![W14 pipeline diagram](assets/diagrams/w14_pipeline_diagram.svg)

이 다이어그램은 `MLOps supply-chain map`를 발표용으로 요약한 개념도다. 데이터 흐름, 평가 지표, 한계 표시는 `assets/figure_manifest.md`에도 기록했다.

### 확인 필요

- hash/pass 항목은 시각화에서 제외했으며 원본 CSV와 artifact inventory를 함께 확인해야 한다.
- 논문별 원문 절·쪽·그림 번호는 최종 제출 전 사람 검토가 필요하다.
<!-- formula-visual-supplement:end -->
