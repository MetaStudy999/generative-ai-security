# AI 원리 70% 정리

## 1. 핵심 이론

W06의 AI 원리는 Diffusion, Score-based model, GAN, 조건부 생성이다. 이 주차에서는 보안 이슈를 먼저 끌어오지 않고, 모델 또는 시스템이 어떤 학습 구조와 평가 구조를 갖는지 이해하는 데 70%의 비중을 둔다.

핵심 항목은 다음과 같다.

- 확률생성모형의 기본 개념
- GAN의 generator-discriminator 구조
- GAN의 학습 안정성 문제
- Diffusion model의 forward process와 reverse process
- Score-based generative model 개념
- 조건부 생성
- 이미지 생성과 비디오 생성의 차이
- 생성 품질, 다양성, 샘플링 비용
- 생성모형 평가 지표의 한계

## 2. 핵심 개념표

| 개념 | 정의 | 직관적 설명 | 관련 논문 |
|---|---|---|---|
| 확률생성모형의 기본 개념 | 확률생성모형(Diffusion/GAN) & 딥페이크 검출에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 1번째 관찰 지점 | P01 |
| GAN의 generator-discriminator 구조 | 확률생성모형(Diffusion/GAN) & 딥페이크 검출에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 2번째 관찰 지점 | P02 |
| GAN의 학습 안정성 문제 | 확률생성모형(Diffusion/GAN) & 딥페이크 검출에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 3번째 관찰 지점 | P03 |
| Diffusion model의 forward process와 reverse process | 확률생성모형(Diffusion/GAN) & 딥페이크 검출에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 4번째 관찰 지점 | P04 |
| Score-based generative model 개념 | 확률생성모형(Diffusion/GAN) & 딥페이크 검출에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 5번째 관찰 지점 | P05 |
| 조건부 생성 | 확률생성모형(Diffusion/GAN) & 딥페이크 검출에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 6번째 관찰 지점 | P05 |
| 이미지 생성과 비디오 생성의 차이 | 확률생성모형(Diffusion/GAN) & 딥페이크 검출에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 7번째 관찰 지점 | P05 |
| 생성 품질, 다양성, 샘플링 비용 | 확률생성모형(Diffusion/GAN) & 딥페이크 검출에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 8번째 관찰 지점 | P05 |
| 생성모형 평가 지표의 한계 | 확률생성모형(Diffusion/GAN) & 딥페이크 검출에서 핵심이 되는 AI 원리 | 모델을 이해하기 위한 9번째 관찰 지점 | P05 |

## 3. 수식 또는 알고리즘

```text
입력/데이터 정의 -> 확률생성모형의 기본 개념 -> GAN의 generator-discriminator 구조 -> GAN의 학습 안정성 문제 -> Diffusion model의 forward process와 reverse process -> 모델 또는 시스템 출력 -> 평가 지표 산출
```

수식 수준에서는 학습 목적함수, 평가 지표, 일반화 또는 효율성 조건을 분리해 기록한다. 세부 수식은 원문 확인 후 최종 논문에 필요한 것만 엄선한다.

## 4. 초보자용 설명

확률생성모형(Diffusion/GAN) 및 딥페이크 검출를 공부할 때 먼저 볼 것은 "모델이 무엇을 입력으로 받고, 무엇을 학습하며, 어떤 기준으로 성공을 판단하는가"이다. 이 구조를 이해해야 공격자가 어느 지점을 건드릴 수 있는지도 보인다.

## 5. 보안 연구와의 연결

AI 원리의 취약 지점은 곧 보안 평가 항목이 된다. 확률생성모형의 기본 개념, GAN의 generator-discriminator 구조, GAN의 학습 안정성 문제를 이해하면 딥페이크 생성과 악용 가능성, 합성미디어 기반 허위증거 위험, 딥페이크 탐지 모델의 일반화 문제가 왜 발생하는지 설명할 수 있다.
