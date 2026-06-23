# 한계와 오픈문제

## 1. 문헌 검증 한계

P02와 P05는 프롬프트 지정 논문과 로컬 PDF가 다르다. 최종 제출 전 지정 문헌을 확보할지, 관련 보조 문헌으로 유지할지 결정해야 한다. DOI/URL도 일부는 PDF 표기만 확인했으므로 공식 출판사 또는 arXiv 페이지 대조가 필요하다.

## 2. 방법론 한계

모델 추출 위험은 query budget, 출력 정보량, 공격자의 데이터 분포, 대상 모델 복잡도에 크게 의존한다. W13 실험은 synthetic binary classifier와 1-nearest-neighbor related만 사용했으므로 실제 MLaaS/LLM extraction을 대표하지 않는다.

## 3. 워터마크 검증 한계

toy trigger-set에서 watermark detection은 1.000000까지 올라갔지만 false positive proxy도 0.600000이다. 따라서 단순 trigger 일치만으로 소유권을 강하게 주장할 수 없으며, 무관 모델군, 통계적 유의성, adaptive removal, legal evidentiary 기준이 추가되어야 한다.

## 4. 재현성 한계

실험 산출물은 `outputs/metrics_summary.csv`, `results.json`, `run_log.md`에 남겼다. 다만 `outputs/`가 저장소 정책상 추적되지 않을 수 있으므로 최종 제출 압축본에는 산출물 포함 여부를 별도 확인해야 한다.

## 5. 기말 논문으로 남길 질문

1. 모델 IP 보호 평가에서 false positive 허용 기준은 어떻게 정할 것인가?
2. 워터마크 검출과 모델 utility 사이의 trade-off를 어떤 표준 지표로 보고할 것인가?
3. 실제 API 공격 절차를 배제하면서도 학술적으로 유효한 toy evaluation을 어떻게 설계할 것인가?
4. 프롬프트 지정 문헌과 로컬 PDF 표기 차이를 참고문헌 검증표에서 어떻게 투명하게 처리할 것인가?
