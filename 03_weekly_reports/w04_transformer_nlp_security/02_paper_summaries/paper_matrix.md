# W04 논문 5편 비교표

| 논문 | 연구문제 | 핵심 방법 | 데이터/실험 | AI 원리 기여 | 보안 위협 연결 | 평가 지표 | 한계 | 내 논문 활용 |
|---|---|---|---|---|---|---|---|---|
| P01 | 긴 시퀀스에서 self-attention의 계산 복잡도 병목을 어떻게 줄일 것인가 | sparse attention, low-rank, kernelized attention, recurrence/memory 등 efficient transformer survey | 문헌조사 중심 | attention 복잡도와 X-former 계열 분류 | 긴 프롬프트·문서 처리 시 비용·로그·민감정보 노출면 확장 | complexity, memory, latency, approximation quality | 보안 위협모형 직접 문헌은 아님 | 긴 입력 LLM/RAG 보안 평가의 비용 축 |
| P02 | Transformer를 더 빠르고 가볍게 만드는 실용 기법은 무엇인가 | distillation, pruning, quantization, efficient architecture, inference optimization | 문헌조사와 실용 분류 | 빠른 추론·경량화 전략 | 보안 필터/마스킹/감사 시스템의 비용과 배포 가능성 | speedup, memory, latency, parameter count | NLP 공격·프라이버시 직접 중심은 아님 | 방어 비용과 utility trade-off |
| P03 | Transformer 계열 구조와 응용은 어떻게 분류되는가 | transformer taxonomy, architecture/application survey | NLP/CV/multimodal 응용 문헌 | Transformer 기본 구조와 변형 전체 지도 | 공격면을 입력·attention·출력·응용별로 분리 가능 | task performance, model complexity | 보안 평가 지표는 별도 필요 | W04 이론 배경과 모델 taxonomy |
| P04 | NLP 모델의 대적공격과 방어는 어떻게 분류되는가 | adversarial attack/defense/robustness survey | text classification, QA, NLI 등 문헌 | semantic-preserving perturbation과 NLP robustness | word substitution, paraphrase, character attack, transfer attack | attack success rate, semantic similarity, robust accuracy | 강의자료 제목/저자 약식 표기와 출판판 표기 차이 확인 필요 | NLP 대적공격 위협모형 핵심 근거 |
| P05 | 프롬프트 입력의 민감정보를 어떻게 보호할 것인가 | prompt privacy, masking, rewriting, policy, privacy-preserving prompt engineering survey | LLM/prompting 문헌 | prompt와 ICL의 민감정보 위험 구조 | prompt leakage, ICL leakage, log retention, tool call exposure | leakage rate, utility, policy compliance | 실제 시스템 보증은 별도 평가 필요 | 프롬프트 프라이버시 KCI/SCI 주제 핵심 근거 |

## 종합 비교

P01-P03은 Transformer 구조·효율화·taxonomy 문헌이다. P01은 attention 계산 복잡도와 X-former 계열을, P02는 실제 배포에서의 속도·메모리·파라미터 절감 전략을, P03은 Transformer 구조와 응용의 전체 지도를 제공한다.

P04는 NLP adversarial robustness 문헌이다. 단어 치환, 문장 재구성, character-level 교란, transfer attack을 attack success rate와 robust accuracy로 분리해서 보아야 함을 알려준다.

P05는 prompt privacy와 ICL privacy 문헌이다. 프롬프트 입력, few-shot 예시, 로그, 외부 도구 호출 인자에서 민감정보가 노출될 수 있음을 보안 자산 관점으로 연결한다.

Efficient Transformer 문헌은 보안 직접 문헌은 아니지만 긴 입력, 로그, 비용, 방어 latency, 감사 가능성과 연결된다. W04 실험은 실제 Transformer 성능 실험이 아니라 synthetic privacy-risk prompt와 keyword privacy-risk detector를 사용한 toy evaluation이다. 따라서 수치는 평가 형식 검증용이며 실제 Transformer, LLM, 상용 NLP 시스템의 강건성 또는 프라이버시 보호 성능으로 일반화하지 않는다.
