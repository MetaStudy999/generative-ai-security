# P05 Summary

## Generative Adversarial Networks: A Survey on Attack and Defense Perspective — Chenhan Zhang et al., ACM Computing Surveys, 2023/2024

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W13 Model Stealing & Watermarking |
| 논문명 | Generative Adversarial Networks: A Survey on Attack and Defense Perspective |
| DOI | https://doi.org/10.1145/3615336 |
| 검증 상태 | W13 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 Zhipeng Cai et al. 관련 보조 문헌으로 강의자료 표기와 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 GAN의 공격·방어 관점을 **adversarial generation, privacy/security applications, attack surface, defense taxonomy, synthetic data risk** 관점에서 정리하며, W13에서 생성모형 기반 보안과 모델 IP 보호를 연결하는 관련 문헌이다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | GAN은 공격 생성과 방어 데이터 증강에 어떻게 동시에 사용되는가? |
| RQ2 | 생성모형은 개인정보·저작권·모델 소유권 문제와 어떻게 연결되는가? |
| RQ3 | Watermarking과 provenance는 생성물과 모델 모두에서 어떻게 필요해지는가? |

---

## 3. 핵심 수식

$$
\min_G\max_D \mathbb{E}_{x\sim p_{data}}[\log D(x)]+\mathbb{E}_{z\sim p_z}[\log(1-D(G(z)))]
$$

$$
Risk_{gen}=w_1PrivacyRisk+w_2IPRisk+w_3MisuseRisk-w_4DefenseCoverage
$$

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | 생성모델, 합성물, 학습 데이터, 워터마크, provenance |
| 공격자 목표 | 합성물 악용, watermark 제거, 모델/데이터 소유권 침해 |
| 지표 | generated artifact risk, watermark robustness, detection rate, provenance coverage |

---

## 5. 기말논문 연결

P05는 모델 IP와 생성물 provenance를 함께 보는 보조 문헌이다. W06 딥페이크와 W13 모델 워터마킹을 연결하는 다리 역할을 한다.

---

## 6. 최종 판단

P05는 관련 문헌으로 사용하되, 로컬 PDF 차이와 강의자료 표기 차이 메모를 유지한다.
