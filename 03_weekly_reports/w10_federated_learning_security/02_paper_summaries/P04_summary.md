# P04 Summary

## The Federation Strikes Back: A Survey of Federated Learning Privacy Attacks, Defenses, Applications, and Policy Landscape — Joshua C. Zhao et al., ACM Computing Surveys, 2025

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W10 연합학습(FL) & FL 위협·방어·정책 |
| 논문명 | The Federation Strikes Back: A Survey of Federated Learning Privacy Attacks, Defenses, Applications, and Policy Landscape |
| 저자 | Joshua C. Zhao et al. |
| 공식 출판 정보 | ACM Computing Surveys, Vol. 57, No. 9, pp. 1–37, 2025 |
| DOI | https://doi.org/10.1145/3724113 |
| 로컬 PDF | `01_papers/pdf/04_Zhao_et_al_2025_Federation_Strikes_Back.pdf` |
| 검증 상태 | W10 `paper_list.md` 기준 공식 DOI 확인. 수업자료 제목은 `The Federation Strikes Back` 부제가 빠진 축약 표기이며 Article 번호는 추가 대조 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 해당 PDF blob이 존재함을 확인했다. 요약은 로컬 PDF 경로와 W10 `paper_list.md`의 공식 DOI 메타데이터 기준으로 보완했다. |
| 핵심 근거 사용 가능 여부 | 가능. W10에서 FL privacy attacks, defenses, applications, policy landscape를 기술·정책·감사 관점으로 통합하는 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

이 논문은 Federated Learning의 프라이버시 공격과 방어를 **membership inference, gradient inversion/reconstruction, property inference, model update leakage, secure aggregation, differential privacy, cryptographic protection, access control, application domains, policy landscape, governance evidence** 관점에서 정리하며, W10에서 FL 보안을 기술적 방어뿐 아니라 **privacy-utility-governance-compliance-audit** 통합 평가 문제로 확장하는 핵심 문헌이다.

---

## 2. 핵심 연구문제

> Federated Learning은 원본 데이터를 중앙에 모으지 않지만, client update와 gradient, model output, participant metadata를 통해 개인정보와 민감 속성이 노출될 수 있다. 이러한 privacy attack을 어떤 threat model로 분류하고, secure aggregation·differential privacy·정책·감사를 어떻게 결합해 방어할 것인가?

| 번호 | 연구질문 |
|---|---|
| RQ1 | FL은 원본 데이터를 공유하지 않음에도 membership inference, gradient inversion, property inference, model inversion에 왜 취약한가? |
| RQ2 | 공격자는 client update, gradient, global model, communication metadata, participant identity를 통해 어떤 정보를 추론할 수 있는가? |
| RQ3 | Secure aggregation, differential privacy, encryption, update clipping, access control, trust management는 각각 어떤 보호 범위와 한계를 갖는가? |
| RQ4 | 의료, 금융, 모바일, IoT, edge computing 등 응용 domain에 따라 privacy requirement와 policy obligation은 어떻게 달라지는가? |
| RQ5 | FL privacy 평가는 leakage rate, MI advantage, reconstruction error, utility drop, privacy budget, compliance evidence를 어떻게 통합해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W10 연결 |
|---|---|---|
| FL privacy attack taxonomy | membership inference, gradient inversion, property inference, model inversion 등 privacy attack을 체계화 | W10 privacy 핵심 축 |
| Defense landscape 정리 | secure aggregation, DP, encryption, clipping, access control, trust management 방어를 비교 | privacy-defense-metric matrix 근거 |
| Application domain 연결 | healthcare, finance, mobile/edge, IoT 등 FL 적용 분야별 privacy risk를 정리 | 기말논문 응용·정책 장 연결 |
| Policy landscape 포함 | 기술적 방어 외에 규제·거버넌스·책임성·감사 요구를 논의 | W14 MLOps·W15 evidence chain 연결 |
| Privacy-utility-governance 통합 | 프라이버시 보호와 성능, 비용, 감사 가능성 사이의 trade-off를 제시 | W10 종합 평가축 구성 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | FL은 데이터를 중앙으로 모으지 않아 privacy-preserving 학습으로 주목받지만, update와 gradient를 통해 정보가 유출될 수 있다. | “데이터를 안 보낸다”는 말이 “아무 정보도 안 샌다”는 뜻은 아니다. |
| 2. Federated Learning Background | FL의 server-client 구조, local update, aggregation, cross-device/cross-silo 환경, privacy assumption을 설명한다. | 여러 기관이 각자 학습하고 결과만 중앙에 보내지만, 그 결과에도 데이터 흔적이 남을 수 있다. |
| 3. Privacy Attacks | Membership inference, gradient inversion, property inference, model inversion, update leakage 등 공격을 분류한다. | 학습 결과를 보고 “이 사람이 학습 데이터에 있었는가”, “어떤 속성을 가진 데이터였는가”를 추정할 수 있다. |
| 4. Defense Mechanisms | Secure aggregation, differential privacy, encryption, clipping, anonymization, access control 등 방어책을 정리한다. | update를 숨기거나, noise를 넣거나, 권한을 제한해 정보 유출을 줄인다. |
| 5. Applications | 의료, 금융, 모바일, IoT, edge 등 민감 데이터가 많은 분야에서 FL privacy 요구가 높다. | 병원·은행·휴대폰처럼 데이터를 모으기 어려운 곳에서 FL은 유용하지만 보호 기준도 더 엄격하다. |
| 6. Policy Landscape | 개인정보 보호법, 데이터 거버넌스, 참여자 동의, 책임성, 감사 가능성 같은 정책 문제를 다룬다. | 기술만으로 끝나지 않고, 누가 책임지고 어떻게 검증할지도 정해야 한다. |
| 7. Challenges and Future Directions | Privacy-utility trade-off, defense cost, scalable privacy, benchmark 부족, compliance evidence 부족이 과제로 남는다. | 더 안전하게 만들수록 성능과 비용이 흔들리므로 균형 있는 평가가 필요하다. |
| 8. Conclusion | FL privacy는 기술적 방어와 정책·감사 체계를 함께 설계해야 하는 문제다. | FL을 안전하게 쓰려면 암호화·DP 같은 기술과 감사 로그·정책 준수가 같이 필요하다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 FL privacy attack/defense와 W10 보안 평가를 설명하기 위한 표준화된 표현이다. 수식은 GitHub, MS Word, PDF 변환 호환성을 위해 Markdown 표 밖의 LaTeX block math로 작성한다.

### 5.1 Privacy Risk Score

FL privacy risk는 여러 공격 위험과 방어 적용 범위를 함께 고려한다.

$$
PrivacyRisk=w_1MI+w_2GI+w_3PI+w_4CommLeak-w_5DefenseCoverage
$$

| 기호 | 의미 |
|---|---|
| $MI$ | membership inference 위험 |
| $GI$ | gradient inversion 또는 gradient leakage 위험 |
| $PI$ | property inference 위험 |
| $CommLeak$ | communication metadata 또는 update 전송 과정 노출 위험 |
| $DefenseCoverage$ | secure aggregation, DP, access control, policy 적용 범위 |

### 비전공자용 설명

FL의 개인정보 위험을 하나만 보면 부족하다. “학습 데이터 포함 여부 추론”, “데이터 복원”, “민감 속성 추론”, “통신 노출”을 함께 보고, 적용된 방어 범위까지 반영해야 한다.

---

### 5.2 Membership Inference Advantage

특정 sample이 client의 학습 데이터에 포함되었는지 추론하는 공격의 이득을 측정한다.

$$
Adv_{MI}=P[A(z)=1\mid z\in D_{train}]-P[A(z)=1\mid z\notin D_{train}]
$$

| 기호 | 의미 |
|---|---|
| $A(z)$ | sample $z$가 학습 데이터에 포함됐다고 판단하는 공격자 |
| $D_{train}$ | 학습 데이터 |

### 보안적 의미

FL에서도 global model이나 update를 보고 특정 사용자가 학습에 포함되었는지 추정할 수 있다. 의료·금융 데이터에서는 membership 자체가 민감정보가 될 수 있다.

---

### 5.3 Gradient Inversion Error

Gradient나 update에서 원본 데이터를 복원하려는 공격의 품질을 측정한다.

$$
ReconError=\frac{1}{N}\sum_{i=1}^{N}\left\|x_i-\hat{x}_i\right\|_2^2
$$

| 기호 | 의미 |
|---|---|
| $x_i$ | 실제 client data |
| $\hat{x}_i$ | 공격자가 gradient/update에서 복원한 추정 data |

### 보안적 의미

ReconError가 낮으면 update가 원본 데이터 정보를 많이 노출한다는 뜻이다. 따라서 gradient clipping, secure aggregation, DP가 필요하다.

---

### 5.4 Property Inference Success

Client 데이터 집합의 민감 속성이나 통계적 특성을 추론한 성공률이다.

$$
PropertyInferenceRate=\frac{N_{properties\ correctly\ inferred}}{N_{property\ inference\ attempts}}
$$

### 보안적 의미

공격자가 특정 client 데이터에 특정 질병, 지역, 행동 패턴, 조직 특성이 포함되어 있음을 추론할 수 있다. 이는 raw data를 직접 보지 않아도 발생한다.

---

### 5.5 Differential Privacy Trade-off

DP 방어 적용 후 모델 성능 손실을 측정한다.

$$
UtilityDrop=Acc_{baseline}-Acc_{DP}
$$

| 기호 | 의미 |
|---|---|
| $Acc_{baseline}$ | privacy defense 없이 학습한 기준 정확도 |
| $Acc_{DP}$ | DP 적용 후 정확도 |

### 보안적 의미

DP는 개인정보 보호를 강화하지만 noise 때문에 정확도와 수렴 속도가 낮아질 수 있다. privacy budget과 utility drop을 함께 기록해야 한다.

---

### 5.6 Defense Coverage

방어가 client, round, update 중 어느 정도 범위에 적용되었는지 측정한다.

$$
DefenseCoverage=\frac{N_{protected\ updates}}{N_{total\ updates}}
$$

### 보안적 의미

일부 client나 일부 round에만 방어가 적용되면 전체 FL 시스템이 안전하다고 보기 어렵다. round별 방어 적용 범위와 실패 사례를 기록해야 한다.

---

### 5.7 Compliance Evidence Score

정책·규정·감사 요구를 얼마나 충족했는지 문서화한다.

$$
ComplianceScore=\frac{|E_{provided}\cap E_{required}|}{|E_{required}|}
$$

| 기호 | 의미 |
|---|---|
| $E_{provided}$ | 실제 제출·기록된 준수 증거 |
| $E_{required}$ | 정책·규정·감사에서 요구하는 증거 |

### 보안적 의미

Privacy-preserving FL을 주장하려면 기술 성능뿐 아니라 동의, 목적 제한, 데이터 최소화, 로그, 접근통제, 삭제·철회 정책 같은 evidence를 남겨야 한다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W10/P04에서의 의미 |
|---|---|---|
| Federated Learning | 원본 데이터를 중앙으로 모으지 않고 local update를 공유 | privacy-preserving potential의 구조적 기반 |
| Gradient/Update | client 데이터로 계산된 학습 정보 | privacy leakage의 주요 통로 |
| Aggregation | 여러 update를 global model로 결합 | 개별 update 보호와 global utility 균형 |
| Secure Aggregation | server가 개별 update를 직접 보지 못하게 함 | gradient leakage 완화, 감사 어려움 발생 |
| Differential Privacy | 개별 데이터 영향 제한 | privacy budget과 utility trade-off |
| Privacy Attack | MI, GI, PI 등 데이터 정보 추론 | FL privacy threat taxonomy |
| Application Domain | 의료·금융·IoT 등 민감 데이터 환경 | 도메인별 규제와 위험 차이 |
| Policy Landscape | 법·규정·동의·감사·책임성 | 기술 방어를 운영체계로 확장 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | FL Privacy 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | gradient/update와 communication metadata가 client data 정보를 누출할 수 있음 | MI advantage, ReconError, LeakageRate |
| 무결성 | privacy defense가 모델 성능·aggregation 동작을 바꿔 부작용을 만들 수 있음 | UtilityDrop, convergence delay |
| 가용성 | encryption/DP/secure aggregation이 통신·계산 지연을 증가시킬 수 있음 | DefenseCost, latency, dropout rate |
| 프라이버시 | 원본 데이터 미공유만으로는 충분하지 않으며 inference attack 방어 필요 | DefenseCoverage, DP budget |
| 책임성 | 개인정보 보호 주장을 뒷받침할 정책·감사 증거가 필요 | ComplianceScore, audit completeness |
| 거버넌스 | 응용 domain별 규제와 책임 주체가 다름 | policy compliance, access-control evidence |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | client update, gradient, participant identity, local data statistics, communication metadata, global model, privacy policy evidence |
| 공격자 목표 | membership inference, gradient reconstruction, property inference, model inversion, communication metadata analysis, policy non-compliance exploitation |
| 공격자 능력 | server 관찰, client update 수집, global model 질의, communication metadata 관찰, 일부 client 장악, auxiliary data 보유 |
| 공격 경로 | client local training → update/gradient generation → communication → aggregation → global model release/query → privacy inference |
| 방어자 능력 | secure aggregation, differential privacy, encryption, update clipping, access control, audit logging, consent/purpose policy |
| 제외 범위 | 실제 개인정보 기반 gradient inversion 실험, 실제 의료·금융 FL 공격, 원본 client 데이터 사용, 공격 코드 제공 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W10/P04 활용 |
|---|---|---|---|
| Privacy attack | MI advantage, ReconError, PropertyInferenceRate | 개인정보 추론 위험 | FL privacy 평가 |
| Defense effect | DefenseCoverage, SecureAggCoverage, DP budget | 방어 적용 범위와 강도 | 방어 효과 평가 |
| Utility | clean accuracy, UtilityDrop, convergence round | 방어 후 모델 성능 | privacy-utility trade-off |
| Cost | communication overhead, computation overhead, latency | 방어 운영 비용 | MLOps 평가 |
| Governance | ComplianceScore, access-control evidence | 정책·규정 준수 증거 | policy landscape 연결 |
| Auditability | round trace, update provenance, consent log | 사고 재현·책임 추적 | W15 evidence chain |
| Domain risk | domain sensitivity score | 의료·금융 등 도메인 위험도 | 응용별 평가 |
| Fairness | per-client accuracy, subgroup leakage risk | client·집단별 영향 | 정책·공정성 연결 |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| FL scenario | cross-device/cross-silo, client 수, server trust assumption |
| Data sensitivity | 의료·금융·IoT 등 domain, 민감 속성, synthetic 여부 |
| Attack model | MI/GI/PI/model inversion 구분, attacker knowledge, auxiliary data 여부 |
| Defense setting | secure aggregation, DP, encryption, clipping, access control 적용 범위 |
| Privacy parameters | DP epsilon/delta, clipping norm, noise multiplier, aggregation protection coverage |
| Utility setting | baseline model, private model, accuracy/loss/convergence round |
| Policy evidence | consent, purpose limitation, access control, retention policy, audit log |
| Evaluation | MI advantage, ReconError, UtilityDrop, DefenseCost, ComplianceScore |
| Logs | client participation, round trace, update hash, privacy defense config, failure case |
| 한계 | toy/synthetic FL privacy 평가를 실제 의료·금융 FL 보안 보증으로 과장하지 않음 |

---

## 11. 논문의 고유 기여

1. FL privacy attack과 defense를 기술적 taxonomy와 policy landscape로 함께 정리한다.
2. Membership inference, gradient inversion, property inference 등 FL privacy attack의 주요 축을 비교한다.
3. Secure aggregation과 DP 같은 방어가 privacy를 높이는 동시에 utility, cost, auditability trade-off를 만든다는 점을 강조한다.
4. FL 적용 domain과 정책·규제 환경을 privacy 평가의 일부로 포함한다.
5. W10 기말논문에서 privacy-utility-governance 통합 평가표를 만드는 직접 근거를 제공한다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 기술 방어의 trade-off | secure aggregation, DP, encryption은 보호 범위와 비용이 다르다. | DefenseCoverage, UtilityDrop, DefenseCost 병기 |
| Policy evidence 부족 | 기술 지표만으로 법·정책 준수를 입증하기 어렵다. | ComplianceScore와 감사 로그 포함 |
| Secure aggregation 감사 한계 | 개별 update를 숨기면 악성 update forensic이 어려울 수 있다. | privacy-auditability trade-off 명시 |
| Domain별 요구 차이 | 의료·금융·IoT는 privacy risk와 규제가 다르다. | domain sensitivity를 구분해 평가 |
| 공격자 지식 가정 차이 | auxiliary data와 server 권한에 따라 공격 위험이 달라진다. | attacker knowledge를 threat model에 명시 |
| 실제 데이터 실험 제한 | 개인정보 기반 공격 재현은 윤리·법적 위험이 크다. | synthetic/toy data와 문헌 기반 분석으로 제한 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | FL privacy는 데이터 미공유만이 아니라 update leakage, 정책 준수, 감사 가능성 문제라는 문제의식 |
| 2장 관련연구 | FL privacy attacks, defenses, applications, policy landscape survey 정리 |
| 3장 위협모형 | client update, gradient, identity, local statistics, communication metadata, policy evidence 보호 자산 정의 |
| 4장 연구방법 | MI advantage, ReconError, PropertyInferenceRate, UtilityDrop, DefenseCoverage, ComplianceScore 지표 설계 |
| 5장 분석 | privacy-utility-governance matrix와 domain-specific policy evidence table 제시 |
| 6장 보안적 함의 | secure aggregation, DP, access control, consent, audit log, privacy-auditability trade-off 해석 |

---

## 14. 기말논문 연결 3문장

1. W10에서 기말논문에 반영할 개념: FL은 raw data를 공유하지 않아도 update와 gradient를 통해 membership, property, reconstructed data가 추론될 수 있으므로 privacy attack과 defense를 별도로 평가해야 한다.
2. W10에서 기말논문에 반영할 표·그림·실험: MI advantage, ReconError, PropertyInferenceRate, UtilityDrop, DefenseCoverage, ComplianceScore를 포함한 privacy-utility-governance matrix를 반영한다.
3. W10이 LLM/RAG 보안 감사 프레임워크와 연결되는 지점: 분산 기여형 AI 시스템은 기술적 privacy defense뿐 아니라 consent, access control, update provenance, policy compliance evidence를 W14/W15 evidence chain에 포함해야 한다.

---

## 15. 최종 판단

P04는 W10의 privacy 핵심 문헌이다. P02/P03이 FL의 보안·프라이버시 공격 taxonomy와 실험 설계를 제공한다면, P04는 privacy attack, defense, application, policy landscape를 연결해 기술·정책·감사 통합 평가축을 만든다. 따라서 W10 기말논문 연결에서는 P04를 **FL privacy-utility-governance 통합 평가와 compliance evidence 설계의 중심 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
