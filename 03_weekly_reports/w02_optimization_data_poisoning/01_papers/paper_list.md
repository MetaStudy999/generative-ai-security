# W02 논문 목록

| ID | 논문 제목 | 저자 | 연도 | 출처 | 로컬 PDF | 확인 상태 |
|---|---|---|---:|---|---|---|
| P01 | Optimization Methods for Large-Scale Machine Learning | Léon Bottou, Frank E. Curtis, Jorge Nocedal | 2018 | SIAM Review | `01_Bottou_Curtis_Nocedal_2018_Optimization_Methods_Large_Scale_ML.pdf` | SIAM 출판 링크/DOI 기록 |
| P02 | Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better | Gaurav Menghani | 2021/2023 | arXiv / ACM Computing Surveys 판본 대조 대상 | `02_Menghani_2023_Efficient_Deep_Learning_Survey.pdf` | 로컬 PDF 메타데이터와 arXiv 링크 기록 |
| P03 | A Comprehensive Survey on Poisoning Attacks and Countermeasures in Machine Learning | Zhiyi Tian et al. | 2022/2023 | ACM Computing Surveys | `03_Tian_Cui_Liang_Yu_2023_Comprehensive_Poisoning_Survey.pdf` | PDF 메타데이터 DOI 확인 |
| P04 | Wild Patterns Reloaded: A Survey of Machine Learning Security against Training Data Poisoning | Antonio Emanuele Cinà et al. | 2022/2023 | arXiv / ACM Computing Surveys 판본 대조 대상 | `04_Cina_et_al_2023_Wild_Patterns_Reloaded_Poisoning_Survey.pdf` | 로컬 PDF 메타데이터와 arXiv 링크 기록 |
| P05 | A survey of backdoor attacks and defences: From deep neural networks to large language models | Ling-Xin Jin et al. | 2025 | Journal of Electronic Science and Technology | `05_Jin_et_al_2025_Backdoor_Attacks_and_Defences_Survey.pdf` | PDF 메타데이터 DOI 확인 |

## W02 문헌 구성 의도

W02 문헌 패킷은 AI 원리 문헌 2편과 보안 위협 문헌 3편으로 나누어 읽는다. P01은 대규모 최적화와 stochastic gradient 기반 학습의 배경을 제공하고, P02는 모델 효율화가 정확도뿐 아니라 비용, 지연시간, 배포 제약과 연결된다는 점을 보여준다. P03, P04, P05는 학습 데이터가 조작될 때 모델 무결성, 안전성, 책임성이 어떻게 흔들리는지를 poisoning과 backdoor 관점에서 정리한다.

## 작성 기준

- 로컬 PDF가 존재하는 문헌만 W02 분석 대상으로 포함했다.
- DOI가 PDF 메타데이터에서 확인된 문헌은 `doi_check.md`에 기록했다.
- DOI를 확정하지 못한 문헌은 임의 생성하지 않고 출판 페이지 또는 arXiv URL을 기준으로 관리한다.
- 논문별 세부 수치나 실험값은 원문에서 직접 확인 가능한 경우에만 최종 보고서에 반영한다.
