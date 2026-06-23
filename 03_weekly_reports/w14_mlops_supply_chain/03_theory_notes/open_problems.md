# 한계와 오픈문제

## 1. 문헌 검증 한계

P01과 P02는 로컬 PDF 첫 페이지와 수업자료를 대조했다. P03, P04, P05는 수업자료의 대상 논문 DOI와 로컬 PDF가 서로 다르므로 최종 인용 전 공식 원문 PDF 확보가 필요하다. 현재 보고서에서는 이를 `부분 확인`과 `관련 보조 문헌`으로 명시했다.

## 2. 방법론 한계

이번 toy 실험은 MLOps 보안통제의 최소 증거 구조를 보여주는 목적이다. 실제 registry, CI/CD, Kubernetes, production monitoring, SBOM scanner, vulnerability database를 연결하지 않았다. 따라서 결과는 운영 시스템의 보안성 증명이 아니라 평가 프로토콜 초안이다.

## 3. 재현성 한계

재실행 일관성은 같은 코드, seed, config에서 hash가 같다는 의미다. Python runtime, dependency resolver, container image digest까지 완전히 고정하려면 Docker image digest와 lockfile 검증이 추가로 필요하다.

## 4. 보안 평가 한계

Dataset hash와 model hash는 변경 탐지에는 유용하지만 악성 변경 여부를 자동으로 판정하지 않는다. Drift score 0.307626도 입력 분포 변화의 크기를 보여줄 뿐, 변화 원인이 공격인지 정상 환경 변화인지는 별도 분석이 필요하다. Audit coverage와 inventory coverage도 toy 필수 항목 충족률일 뿐 실제 감사 완전성이나 완전한 AI BOM을 보장하지 않는다.

## 5. 기말 논문으로 남길 질문

1. MLOps 보안통제 프레임워크에서 필수 항목과 선택 항목을 어떻게 나눌 것인가?
2. AI BOM/ML artifact inventory를 기존 SBOM, model card, datasheet와 어떻게 연결할 것인가?
3. Drift monitoring, incident response, assurance case를 하나의 평가표로 통합할 수 있는가?
4. 연구용 toy 실험의 evidence를 운영형 AI 시스템의 보안 평가로 확장할 때 어떤 검증 단계가 추가되어야 하는가?
