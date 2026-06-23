# 예상 질문과 답변

| 질문 | 답변 |
|---|---|
| 워터마크 검출률이 1.000000이면 방어가 성공한 것 아닌가? | 아니다. false positive proxy가 0.600000으로 높아 무관 모델도 우연히 signature와 일치할 가능성이 크다. 검출률과 FPR을 함께 봐야 한다. |
| query 1000의 fidelity가 query 500보다 낮은 이유는 무엇인가? | 본 실험의 substitute는 1-nearest-neighbor toy classifier라 query 분포와 이웃 선택에 따라 단조 증가가 보장되지 않는다. 실제 모델 추출 성능 일반화가 아니라 toy 평가로 해석해야 한다. |
| 이 실험이 실제 API 모델 추출 공격을 재현하는가? | 아니다. synthetic local toy 데이터와 로컬 victim model만 사용했다. 실제 상용 API, 개인정보, 무단 대량 질의, 실제 모델 탈취는 제외했다. |
| P02와 P05는 왜 대체 PDF라고 표시했는가? | 로컬 PDF가 프롬프트 지정 논문과 다르기 때문이다. 최종 제출 전 지정 문헌을 확보하거나 대체 문헌 사용 사유를 참고문헌 검증표에 명시해야 한다. |
| P03은 검증 완료인가? | 로컬 PDF의 DOI는 `10.1016/j.neucom.2021.07.051`로 확인했지만, 강의계획서의 저자명·제목 표기 차이는 사람 검토가 필요하다. |
| PDF 원문을 GitHub에 올려도 되는가? | public 저장소라면 위험하다. 현재 PDF 5개는 이미 git 추적 대상이므로 공개 전 삭제 또는 비공개 보관 전환을 검토해야 한다. |
| 기말논문에서 가장 쓸 만한 기여는 무엇인가? | extraction fidelity, query budget, watermark detection, false positive, utility, reproducibility를 함께 보고하는 모델 IP 보호 평가 프레임워크다. |
