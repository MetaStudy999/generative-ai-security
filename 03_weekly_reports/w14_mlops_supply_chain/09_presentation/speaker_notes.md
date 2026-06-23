# 발표자 노트

## 1. 제목

오늘 발표의 핵심은 MLOps 보안을 모델 성능 문제가 아니라 운영 증거 관리 문제로 보는 것입니다. Accuracy가 높아도 데이터, 모델, config, 로그가 추적되지 않으면 공급망 보안을 설명하기 어렵습니다.

## 2. 오늘의 질문

네 가지 질문을 던집니다. 모델은 어떤 데이터와 config에서 만들어졌는가, 배포된 artifact는 변조되지 않았는가, 운영 입력 분포가 바뀌었는가, 사고 후 로그로 추적할 수 있는가입니다.

## 3. MLOps 원리

DevOps가 코드의 빌드와 배포 자동화에 집중한다면 MLOps는 데이터와 모델이 계속 변한다는 점이 추가됩니다. 그래서 dataset version, model registry, experiment tracking, drift monitoring이 필요합니다.

## 4. 공급망 보안 위협

데이터 파이프라인은 poisoning과 provenance loss, model artifact는 tampering, config와 seed는 재현성 상실, logs와 monitoring은 leakage와 audit gap을 만들 수 있습니다.

## 5. 논문 패킷 역할

P01/P02는 MLOps와 deployment workflow의 큰 구조입니다. P03/P04/P05는 각각 AIOps, edge deployment, DL for SE의 연결부입니다. 단 P03/P04/P05는 로컬 PDF가 대상 논문과 달라 공식 원문 확인이 필요하다고 말합니다.

## 6. Toy Pipeline 설계

실습은 실제 공격이 아니라 통제항목 점검입니다. Synthetic data만 생성하고 toy logistic regression을 학습한 뒤 dataset hash, config hash, model hash, drift score, audit coverage, artifact inventory를 남겼습니다.

## 7. 실행 결과

정상 조건 accuracy는 0.925000, F1은 0.923077입니다. Drift score는 0.307626으로 threshold 0.25를 넘었습니다. Audit coverage와 inventory coverage는 1.000000입니다.

## 8. 해석

Drift score가 threshold를 넘었다고 해서 공격이라고 단정하지 않습니다. 이것은 운영 감시 경보이며 실제 장애 확률도 아닙니다. 다음 단계는 원인 분석, human review, 필요 시 rollback 판단입니다. Audit coverage와 inventory coverage는 toy 필수 필드 충족률이므로 실제 감사 완전성이나 완전한 AI BOM으로 설명하지 않습니다.

## 9. 기말논문 연결

기말 논문에서는 W14를 운영형 AI 시스템의 evidence set으로 사용할 수 있습니다. 최소 지표는 dataset hash, model hash, config hash, drift score, audit coverage, artifact inventory입니다.

## 10. 결론

W14의 결론은 단순합니다. MLOps 공급망 보안은 모델 하나를 잘 만드는 문제가 아니라, 모델이 만들어지고 배포되고 감시되는 전체 증거를 남기는 문제입니다.
