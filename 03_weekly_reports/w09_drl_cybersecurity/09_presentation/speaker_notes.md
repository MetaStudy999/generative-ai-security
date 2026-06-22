# W09 발표자 대본

## 1. 제목 슬라이드

오늘 주제는 심층강화학습과 사이버보안 적용, 특히 보상조작입니다. 핵심 메시지는 DRL 방어 에이전트에서 reward가 흔들리면 높은 점수 뒤에 안전하지 않은 정책이 숨어 있을 수 있다는 점입니다.

## 2. 발표 질문

먼저 DRL 에이전트가 어떤 state를 보고 어떤 action을 선택하며 어떤 reward로 학습하는지 설명합니다. 그 다음 reward manipulation이 정책을 어떻게 왜곡하는지, 마지막으로 안전한 자동 대응을 어떤 지표로 평가할지 보겠습니다.

## 3. AI 원리

W09에서 state는 alert level, 자산 중요도, 취약 여부입니다. action은 monitor, isolate, patch, escalate입니다. reward는 탐지 성공, 운영 비용, 안전 위반을 숫자로 바꾼 것입니다.

## 4. 문헌 역할

P01은 DRL 원리, P02는 안전중요 자동화, P03과 P04는 cyber-defense 적용, P05는 DRL verification을 담당합니다. 이 다섯 편을 합치면 원리에서 검증까지 이어지는 흐름이 생깁니다.

## 5. 위협모형

공격자는 state observation을 조작하거나 reward signal을 왜곡할 수 있습니다. 그러면 자동 대응 action이 공격을 방치하거나 정상 이벤트를 과잉 차단할 수 있습니다.

## 6. 실험 설계

실험은 실제 네트워크가 아니라 synthetic toy cyber-defense state에서 수행했습니다. tabular Q-learning을 사용했고 seed는 42입니다. 조건은 normal reward, manipulated reward, robust reward design입니다.

## 7. 실험 결과

기준 조건은 Average Reward 1.085250, Detection F1 0.840206입니다. 보상조작 조건은 Average Reward 0.521167, F1 0.617512로 떨어지고 Safety Violation Rate가 0.195000으로 올라갑니다. Robust reward는 safety violation을 0으로 낮추지만 F1은 0.780952로 기준보다 낮습니다.

## 8. 해석

핵심은 observed reward와 true security objective를 분리해야 한다는 점입니다. 안전 위반을 줄이면 오탐 비용이 늘 수 있으므로, F1만으로 정책을 평가하면 부족합니다.

## 9. 기말논문 연결

기말논문에서는 DRL 기반 사이버 방어 에이전트의 보상조작 위협과 안전성 평가 프레임워크로 발전시킬 수 있습니다.

## 10. 결론

정리하면 reward integrity를 보호해야 하고, Detection F1과 Safety Violation Rate를 함께 봐야 하며, 수치는 실행 로그와 CSV/JSON에 있을 때만 주장해야 합니다.
