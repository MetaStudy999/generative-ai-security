# 한계와 오픈문제

## 1. 문헌 검증 한계

논문 제목, 로컬 PDF 파일명, 공개 DOI/URL 상태를 정리했다. P01/P02/P04/P05는 ACM DOI를 확인했고 P03은 AI Open DOI를 확인했다. 다만 ACM Article 번호 일부, P04 강의자료의 `N. Goyal` 표기, 국내 참고문헌, PDF 공개 저장소 보관 여부는 최종 대조가 필요하다.

## 2. 방법론 한계

Transformer 변형 및 NLP 대적공격/프라이버시는 Transformer 기본 구조, Self-attention과 multi-head attention, Query, Key, Value의 역할와 NLP 대적공격, 단어 치환 공격, 문장 재구성 공격가 동시에 얽힌다. 단일 지표만으로 성능과 보안성을 판단하면 연구 결론이 과도하게 단순화될 수 있다.

## 3. 재현성 한계

Docker, seed, config, 데이터 버전, 실행 로그가 모두 보존되어야 한다. W04는 `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md`를 생성했으며, 제출 수치는 이 outputs 기준으로만 사용한다.

## 4. 기말 논문으로 남길 질문

1. 어떤 위협을 기말 논문의 중심 사례로 삼을 것인가?
2. 문헌분석과 toy 실험을 실제 공개 데이터 평가로 어떻게 확장할 것인가?
3. 보안성, 설명가능성, 재현성을 하나의 평가표로 통합할 수 있는가?
