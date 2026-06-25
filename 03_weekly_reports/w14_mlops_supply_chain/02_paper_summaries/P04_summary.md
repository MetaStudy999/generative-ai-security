# P04 Summary

## Deep Learning With Edge Computing: A Review — Jiasi Chen, Xukan Ran, Proceedings of the IEEE, 2019

## 0. 문헌 검증 상태

| 항목 | 내용 |
|---|---|
| 주차 | W14 MLOps & AI Supply Chain |
| 공식 논문명 | Deep Learning With Edge Computing: A Review |
| 공식 저자 | Jiasi Chen, Xukan Ran |
| 공식 출판 정보 | Proceedings of the IEEE, Vol. 107, Issue 8, pp. 1655–1674, 2019-08 |
| DOI | https://doi.org/10.1109/JPROC.2019.2921977 |
| 로컬 PDF | `01_papers/pdf/04_RELATED_Zhou_et_al_2019_Edge_Intelligence_Survey.pdf` |
| 로컬 PDF 상태 | W14 `paper_list.md` 기준 로컬 PDF는 Zhou et al., `Edge Intelligence: Paving the Last Mile of Artificial Intelligence with Edge Computing`, arXiv:1905.10083 관련 보조 문헌이다. 공식 P04 DOI 논문과 동일 문헌으로 단정하지 않는다. |
| 검증 상태 | W14 `paper_list.md` 기준 Jiasi Chen and Xukan Ran의 공식 DOI/출판정보 확인. 수업자료 표기와 DOI 메타데이터는 대응되나, 로컬 PDF는 edge intelligence 관련 보조 문헌으로 차이 메모 유지 |
| PDF 확인 메모 | repo의 PDF 폴더에 P04 관련 PDF blob이 존재함을 확인했다. 다만 로컬 PDF는 공식 P04 지정 논문과 다른 edge intelligence 보조 문헌이므로, summary는 공식 DOI 기준 P04를 중심으로 작성하고 로컬 PDF는 edge-cloud AI 운영·resource-aware inference 보완 문헌으로만 해석한다. |
| 핵심 근거 사용 가능 여부 | 가능. W14에서 edge deployment, on-device inference, edge-cloud collaboration, latency/bandwidth/privacy trade-off, device trust, update integrity, edge AI supply chain risk를 설명하는 핵심 문헌으로 사용 |

---

## 1. 한 문장 요약

공식 P04 논문은 deep learning을 edge computing 환경에 배포할 때 발생하는 문제를 **on-device inference, edge-cloud collaboration, latency, bandwidth, energy, resource constraint, privacy preservation, model compression, split computing, federated/edge learning, device heterogeneity, update integrity, edge deployment monitoring, local data governance, AI supply chain risk** 관점에서 정리하며, W14에서 AI 보안을 중앙 클라우드 MLOps에서 **edge device와 update pipeline까지 확장**하는 핵심 문헌이다.

---

## 2. 핵심 연구문제

> Cloud-only AI 배포는 중앙집중 관리가 쉽지만 latency, bandwidth, privacy 문제가 발생한다. Edge AI는 데이터를 장치 가까이에서 처리해 latency와 privacy를 개선할 수 있지만, device heterogeneity, limited compute, model update integrity, local model tampering, monitoring blind spot, edge-cloud configuration drift 같은 새로운 supply-chain risk를 만든다.

| 번호 | 연구질문 |
|---|---|
| RQ1 | Edge 환경에서 deep learning inference/training은 cloud-only 배포와 비교해 latency, bandwidth, privacy, energy 측면에서 어떤 trade-off를 갖는가? |
| RQ2 | On-device inference와 edge-cloud collaboration은 모델 구조, partitioning, compression, caching, communication design을 어떻게 바꾸는가? |
| RQ3 | Edge device의 resource constraint와 heterogeneity는 모델 배포·모니터링·업데이트 자동화에 어떤 문제를 만드는가? |
| RQ4 | Edge model update, device trust, local data storage, inference log는 AI supply-chain security와 어떻게 연결되는가? |
| RQ5 | LLM/RAG 서비스를 edge/on-device 환경에 배포할 때 prompt, retrieval index, embedding cache, model artifact를 어떻게 보호해야 하는가? |

---

## 3. 논문의 핵심 기여

| 기여 | 설명 | W14 연결 |
|---|---|---|
| Edge DL deployment taxonomy | device-only, edge-assisted, cloud-edge collaboration 구조를 정리 | edge AI 운영 구조 |
| Latency·bandwidth·privacy trade-off | cloud inference와 edge inference의 장단점 비교 | 운영 보안·성능 균형 |
| Resource constraint 분석 | compute, memory, storage, battery, network 제약이 모델 설계에 미치는 영향 정리 | model compression·partitioning 근거 |
| Edge-cloud collaboration | split computing, offloading, distributed inference, edge learning을 설명 | hybrid deployment 설계 |
| Edge supply-chain risk 확장 | 모델 update, device trust, local data, deployment config가 새로운 보호 자산이 됨 | W14 AI supply chain 확장 |

---

## 4. 목차별 핵심 개괄

| 목차 | 핵심 내용 | 비전공자용 이해 |
|---|---|---|
| 1. Introduction | Deep learning은 높은 성능을 보이지만 cloud-only 방식은 latency, bandwidth, privacy 한계가 있어 edge computing이 필요하다. | AI를 중앙 서버에서만 돌리면 느리고 개인정보 이동이 많아질 수 있다. |
| 2. Edge Computing Background | Edge device, edge server, cloud, IoT, mobile, embedded system의 계층 구조를 설명한다. | 사용자 가까이에 작은 서버나 장치가 있어 데이터를 가까운 곳에서 처리한다. |
| 3. Deep Learning on Edge | 모델 압축, 경량화, on-device inference, hardware acceleration, resource-aware scheduling을 다룬다. | 작은 장치에서도 AI가 돌아가도록 모델을 줄이고 최적화한다. |
| 4. Edge-Cloud Collaboration | 일부 계산은 device에서, 일부는 edge/cloud에서 수행하는 split/offloading 방식을 설명한다. | 어려운 계산은 서버에 맡기고, 빠른 계산은 기기에서 한다. |
| 5. Privacy and Security | local data processing은 privacy를 개선할 수 있지만, device compromise와 update poisoning 위험도 만든다. | 데이터를 덜 보내면 개인정보에는 좋지만, 기기 자체가 공격당할 수 있다. |
| 6. Deployment Challenges | heterogeneous devices, intermittent network, resource constraint, monitoring difficulty, update management 문제가 있다. | 모든 기기의 성능과 네트워크가 달라 관리가 어렵다. |
| 7. Applications | 스마트폰, IoT, surveillance, smart city, autonomous system, healthcare 등 edge AI 응용을 정리한다. | 실시간 판단이 필요한 곳에 edge AI가 중요하다. |
| 8. Future Directions | edge intelligence, federated learning, secure update, hardware-aware AI, privacy-preserving inference가 과제로 제시된다. | 앞으로는 작고 안전하고 빠른 AI 운영 체계가 필요하다. |
| 로컬 관련 PDF 메모 | 로컬 PDF는 Zhou et al. Edge Intelligence survey로, official P04와 동일 문헌으로 인용하지 않는다. | PDF가 있다고 해서 공식 지정 논문으로 인용하면 안 된다. |

---

## 5. 핵심 이론 및 수식

> 아래 수식은 edge AI deployment와 supply-chain risk 평가를 W14 보고서에서 설명하기 위한 표준화된 표현이다. 실제 논문의 고유 정량식이라기보다 기말논문 운영 평가표 설계를 위한 지표다.

### 5.1 Edge Risk

Edge AI 운영 위험을 device, update, privacy, latency 요소로 분해한다.

$$
EdgeRisk=DeviceRisk+UpdateRisk+PrivacyRisk+LatencyRisk
$$

| 기호 | 의미 |
|---|---|
| $DeviceRisk$ | edge device compromise, physical access, local tampering 위험 |
| $UpdateRisk$ | model/update package poisoning, rollback failure 위험 |
| $PrivacyRisk$ | local data leakage, inference log leakage 위험 |
| $LatencyRisk$ | 실시간 요구 미충족, network delay 위험 |

### 보안적 의미

Edge AI 보안은 모델 파일뿐 아니라 장치, 업데이트 채널, 로컬 데이터, 네트워크 지연을 함께 관리해야 한다.

---

### 5.2 Latency Decomposition

Edge-cloud inference latency를 device, network, cloud 처리 시간으로 나눌 수 있다.

$$
Latency=T_{device}+T_{network}+T_{edge/cloud}
$$

| 기호 | 의미 |
|---|---|
| $T_{device}$ | device-side preprocessing/inference 시간 |
| $T_{network}$ | 전송 지연 |
| $T_{edge/cloud}$ | edge server 또는 cloud 처리 시간 |

### 보안적 의미

어떤 데이터를 어디서 처리할지 결정할 때 latency와 privacy, bandwidth, trust를 함께 고려해야 한다.

---

### 5.3 Bandwidth Saving

Edge에서 로컬 처리를 수행해 cloud 전송량을 줄이는 정도다.

$$
BandwidthSaving=1-\frac{Bytes_{edge\rightarrow cloud}}{Bytes_{raw\rightarrow cloud}}
$$

### 보안적 의미

전송량이 줄면 bandwidth와 privacy risk가 줄 수 있지만, edge device에 더 많은 민감정보와 모델이 남는다.

---

### 5.4 Model Compression Ratio

Edge 배포를 위해 모델 크기를 얼마나 줄였는지 측정한다.

$$
CompressionRatio=\frac{Size_{compressed}}{Size_{original}}
$$

### 보안적 의미

모델 경량화는 edge 배포에 필요하지만, accuracy·robustness·watermark/fingerprint 유지성에 영향을 줄 수 있다.

---

### 5.5 Update Integrity Score

Edge model update가 무결하게 배포되었는지 확인하는 지표다.

$$
UpdateIntegrity=\frac{N_{verified\ updates}}{N_{total\ updates}}
$$

### 보안적 의미

서명 검증, hash 검증, rollout log가 없으면 edge model update poisoning과 downgrade attack을 탐지하기 어렵다.

---

### 5.6 Device Attestation Coverage

운영 중인 edge device 중 신뢰 상태가 확인된 비율이다.

$$
AttestationCoverage=\frac{N_{attested\ devices}}{N_{active\ devices}}
$$

### 보안적 의미

장치 신뢰 검증이 부족하면 변조된 device가 잘못된 inference를 수행하거나 민감 데이터를 유출할 수 있다.

---

### 5.7 Edge Deployment Readiness Score

Edge AI 배포 준비도를 모델·장치·업데이트·모니터링 기준으로 평가한다.

$$
EdgeReady=\alpha DeviceCheck+\beta ModelCheck+\gamma UpdateIntegrity+\delta MonitorCoverage-\lambda EdgeRisk
$$

### 보안적 의미

Edge deployment는 모델 성능뿐 아니라 device trust, update integrity, monitoring coverage가 충족되어야 승인할 수 있다.

---

## 6. AI 원리 70% 관점 분석

| 원리 항목 | 설명 | W14/P04에서의 의미 |
|---|---|---|
| Edge Computing | 사용자 가까운 장치/서버에서 연산 | latency·privacy 개선 |
| On-device Inference | 모델을 장치에서 직접 실행 | local data 보호·device risk 증가 |
| Edge-cloud Collaboration | device·edge·cloud 분산 처리 | hybrid deployment 설계 |
| Model Compression | pruning, quantization, distillation 등 경량화 | edge resource 대응 |
| Offloading | 계산 일부를 edge/cloud로 전송 | latency/bandwidth trade-off |
| Federated/Edge Learning | 데이터 로컬 유지 후 학습 협력 | privacy와 FL security 연결 |
| Hardware Acceleration | NPU/GPU/TPU/FPGA 활용 | 성능·전력 최적화 |
| Monitoring | edge device와 model 상태 관측 | 운영 보안 핵심 |

---

## 7. 보안 이슈 30% 관점 분석

| 보안 항목 | Edge AI 관점 해석 | 대표 평가 지표 |
|---|---|---|
| 기밀성 | local data, model binary, inference log가 edge device에 남음 | local encryption, access log |
| 무결성 | model update, deployment config, edge binary가 변조될 수 있음 | UpdateIntegrity, checksum |
| 가용성 | network outage, device failure, resource exhaustion이 inference 장애로 연결 | latency, uptime, fallback rate |
| 프라이버시 | on-device 처리는 데이터 전송을 줄이나 device compromise 시 유출 위험 | PrivacyRisk, local retention |
| 안전성 | 실시간 응답 실패나 변조된 model inference가 physical-world harm으로 연결 | latency SLA, attestation |
| 책임성 | 어떤 장치에 어떤 모델과 업데이트가 적용되었는지 추적해야 함 | device/model/update provenance |

---

## 8. 위협모형

| 항목 | 내용 |
|---|---|
| 보호 자산 | edge device, local data, model binary, update package, inference log, deployment config, edge-cloud channel, device identity |
| 공격자 목표 | device compromise, model tampering, update poisoning, downgrade attack, local data leakage, edge-cloud communication interception |
| 공격자 능력 | physical access, local malware, network interception, update channel manipulation, fake device registration, resource exhaustion |
| 위험 경로 | edge device 등록 → model/update 배포 → device compromise 또는 update tampering → 잘못된 inference/데이터 유출 → monitoring blind spot으로 탐지 지연 |
| 방어자 능력 | secure boot, device attestation, signed update, encrypted local storage, monitoring, rollback, edge-cloud access control |
| 제외 범위 | 실제 장치 침투 절차, 펌웨어 악용, 네트워크 공격 코드, credential 탈취, update poisoning 실행 절차 |

---

## 9. 평가방법 및 지표

| 평가축 | 지표 | 의미 | W14/P04 활용 |
|---|---|---|---|
| 성능 | latency, throughput, energy consumption | edge service 품질 | 실시간성 평가 |
| 리소스 | model size, memory, CPU/GPU/NPU usage | 장치 적합성 | 배포 가능성 |
| 네트워크 | bandwidth saving, packet loss, offloading ratio | edge-cloud 효율 | 운영 비용 |
| 프라이버시 | data transfer reduction, local leakage risk | 데이터 보호 수준 | privacy 평가 |
| 업데이트 무결성 | UpdateIntegrity, rollback success | supply chain 보안 | 핵심 보안 평가 |
| 장치 신뢰 | AttestationCoverage, device health | 변조 장치 탐지 | device trust |
| 모니터링 | MonitorCoverage, alert delay | 운영 관측성 | AIOps 연결 |
| 서지 정확성 | official DOI match, local PDF mismatch flag | 참고문헌 정확성 | W15 reference audit |

---

## 10. 재현성 체크리스트

| 항목 | 기록해야 할 내용 |
|---|---|
| Bibliographic status | 공식 DOI 논문과 로컬 PDF 동일 여부, related flag |
| Device | device model, CPU/GPU/NPU, memory, OS, firmware version |
| Model | model architecture, size, compression method, model hash |
| Deployment | edge/cloud split, offloading policy, deployment config, rollout strategy |
| Update | update package hash, signature verification, update channel, rollback artifact |
| Data | local data type, retention policy, preprocessing, privacy control |
| Network | bandwidth, latency, packet loss, edge/cloud endpoint |
| Monitoring | device health, model metric, latency, error rate, alert threshold |
| Security | attestation, secure boot, access control, encryption, signed artifact |
| 한계 | 로컬 PDF는 관련 문헌이고, 특정 edge setting 결과를 모든 device·network·deployment에 일반화하지 않음 |

---

## 11. 논문의 고유 기여

1. Deep learning deployment를 cloud 중심에서 edge device와 edge-cloud collaboration으로 확장한다.
2. Latency, bandwidth, privacy, resource constraint가 AI 운영 설계에 미치는 영향을 체계화한다.
3. Edge model update와 device trust를 AI supply-chain security의 보호 자산으로 확장한다.
4. W14 P01~P03의 MLOps/AIOps 논의를 edge environment와 device-level monitoring으로 연결한다.
5. LLM/RAG의 on-device inference, local embedding cache, edge retrieval, private inference 설계의 보안 근거로 활용 가능하다.

---

## 12. 한계와 오픈문제

| 한계 | 설명 | 내 연구에서 보완할 방법 |
|---|---|---|
| 로컬 PDF 불일치 | P04 로컬 PDF는 공식 DOI 논문이 아니라 Zhou et al. Edge Intelligence survey다. | 공식 DOI/관련 PDF를 분리 표기 |
| 장치 다양성 | edge device별 성능과 OS, hardware accelerator가 다르다. | device profile table 작성 |
| 업데이트 위험 | 분산 장치 업데이트는 무결성·rollback 관리가 어렵다. | signed update와 update hash 기록 |
| 모니터링 공백 | edge device는 네트워크 단절과 제한된 telemetry로 관측이 어려울 수 있다. | monitor coverage와 offline log sync 명시 |
| 프라이버시 역설 | 데이터 전송은 줄지만 local compromise 시 민감정보 유출 위험이 증가한다. | local encryption과 retention policy 반영 |
| LLM/RAG 확장 과제 | 대형 모델은 edge device 리소스에 맞추기 어렵다. | quantization, distillation, hybrid RAG 구조 제안 |

---

## 13. 기말논문 반영 위치

| 기말논문 장 | 반영 내용 |
|---|---|
| 1장 서론 | AI 보안은 cloud MLOps뿐 아니라 edge device와 update pipeline까지 포함해야 한다는 문제의식 |
| 2장 관련연구 | 공식 P04 DOI 논문을 edge DL deployment 핵심 문헌으로 정리하고 로컬 PDF mismatch는 검증표에 기록 |
| 3장 위협모형 | edge device, local data, model binary, update package, inference log, edge-cloud channel 보호 자산 정의 |
| 4장 연구방법 | EdgeRisk, Latency, BandwidthSaving, CompressionRatio, UpdateIntegrity, AttestationCoverage, EdgeReady 지표 설계 |
| 5장 분석 | edge-cloud deployment architecture와 edge AI supply-chain control matrix 제시 |
| 6장 보안적 함의 | device trust, signed update, local privacy, edge monitoring, offline rollback, on-device LLM/RAG 보안 해석 |

---

## 14. 기말논문 연결 3문장

1. W14에서 기말논문에 반영할 개념: Edge AI는 latency와 privacy를 개선하지만, device trust, update integrity, local data leakage, edge monitoring blind spot이라는 새로운 supply-chain risk를 만든다.
2. W14에서 기말논문에 반영할 표·그림·실험: EdgeRisk, Latency, BandwidthSaving, CompressionRatio, UpdateIntegrity, AttestationCoverage, EdgeReady 수식표와 edge-cloud deployment architecture를 반영한다.
3. W14가 W15 최종 논문과 연결되는 지점: W01~W13의 공격·방어 모델이 edge/on-device 환경에 배포될 경우, W15에서는 device profile, model hash, update hash, attestation log, monitoring evidence까지 재현성 표에 포함해야 한다.

---

## 15. 최종 판단

P04는 W14에서 AI supply chain을 cloud MLOps에서 edge deployment와 device-level operation으로 확장하는 핵심 문헌이다. 다만 W14 `paper_list.md` 기준 로컬 PDF는 Zhou et al.의 Edge Intelligence survey이며, 공식 DOI 논문인 Jiasi Chen and Xukan Ran의 Proceedings of the IEEE 논문과 동일하다고 단정하면 안 된다. 기말논문에서는 P04를 **edge AI deployment, latency/privacy trade-off, update integrity, device attestation, edge-cloud monitoring, on-device LLM/RAG 보안 통제의 근거 문헌**으로 사용하는 것이 적절하다.

---

## 16. 변환 호환성 메모

```bash
pandoc P04_summary.md -o P04_summary.docx
pandoc P04_summary.md -o P04_summary.pdf --pdf-engine=xelatex
```
