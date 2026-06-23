# P04 Summary

## Deep Learning With Edge Computing: A Review — Jiasi Chen, Xukan Ran, Proceedings of the IEEE, 2019

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W14 MLOps & AI Supply Chain |
| 논문명 | Deep Learning With Edge Computing: A Review |
| 저자 | Jiasi Chen, Xukan Ran |
| 출판 정보 | Proceedings of the IEEE, 107(8), pp. 1655–1674, 2019 |
| DOI | https://doi.org/10.1109/JPROC.2019.2921977 |
| 검증 상태 | W14 `paper_list.md` 기준 공식 DOI 확인. 로컬 PDF는 Zhou et al. Edge Intelligence 관련 보조 문헌으로 차이 메모 유지 |

---

## 1. 한 문장 요약

이 논문은 edge computing 환경에서 deep learning을 배포하는 문제를 **latency, bandwidth, privacy, on-device inference, edge-cloud collaboration, resource constraint** 관점에서 정리하며, W14에서 AI 공급망과 운영 보안의 edge 확장을 설명한다.

---

## 2. 핵심 연구질문

| 번호 | 연구질문 |
|---|---|
| RQ1 | Edge 환경에서 AI 모델 배포는 cloud-only 배포와 어떤 보안·운영 차이가 있는가? |
| RQ2 | On-device inference는 privacy와 latency를 개선하지만 어떤 관리 위험을 만드는가? |
| RQ3 | Edge model update와 device trust는 supply-chain risk와 어떻게 연결되는가? |

---

## 3. 핵심 지표

$$
EdgeRisk = DeviceRisk + UpdateRisk + PrivacyRisk + LatencyRisk
$$

$$
Latency = T_{device}+T_{network}+T_{cloud}
$$

---

## 4. 위협모형·평가지표

| 항목 | 내용 |
|---|---|
| 보호 자산 | edge device, local data, model binary, update channel, inference log |
| 공격자 목표 | device compromise, model tampering, update poisoning, local data leakage |
| 지표 | latency, model size, update integrity, device attestation, privacy leakage |
| 재현성 | device type, model version, update hash, edge/cloud config 기록 |

---

## 5. 기말논문 연결

P04는 W14를 cloud MLOps에서 edge AI supply chain으로 확장한다. 기말논문에서 on-device LLM/RAG 또는 edge inference 보안 통제의 근거로 활용한다.

---

## 6. 최종 판단

P04는 edge deployment 관점의 관련 핵심 문헌이다. AI 보안은 중앙 서버뿐 아니라 edge device와 update pipeline까지 포함해야 한다.
