# 논문별 핵심 수식·알고리즘 쉬운 설명 보충표

## 작성 기준

이 문서는 W01-W15 final 보고서를 기말 논문에 연결하기 위한 수식·알고리즘 보충표다. 모든 수식은 원문 수식을 그대로 인용한 것이 아니라, 각 논문을 보고서에서 설명하는 데 필요한 대표 수식, 지표, 또는 알고리즘 형태로 정리한 것이다. survey 논문은 특정 단일 수식보다 개념·평가지표가 중요하므로, 해당 분야에서 널리 쓰이는 표준 수식으로 쉬운 설명을 붙였다. `관련 보조 문헌` 또는 DOI 미확인 문헌은 최종 제출 전 원문 쪽/절 번호를 다시 확인한다.

## W01 딥러닝 패러다임 & ML 보안 분류학

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보고서 연결 |
|---|---|---|---|
| P01 | $h_l=\sigma(W_l h_{l-1}+b_l)$, $\theta \leftarrow \theta-\eta\nabla_\theta L$ | 딥러닝은 층마다 입력을 조금씩 바꾸어 표현을 만들고, 오차가 줄어드는 방향으로 가중치를 고친다. | 표현학습, 역전파, 대적 입력이 내부 표현을 흔드는 이유 |
| P02 | $EC=N_{checked}/N_{required}$ | ML 생명주기 보증은 필요한 증거 중 몇 개를 확인했는지로 관리할 수 있다. | 재현성·보증 evidence chain |
| P03 | $F1=2PR/(P+R)$ | 침입탐지는 정확도만 보면 오탐과 미탐을 놓치므로 precision과 recall을 같이 본다. | 탐지 성능과 보안 데이터 평가 |
| P04 | $\max_{\|\delta\|\le\epsilon} L(f_\theta(x+\delta),y)$ | 공격자는 사람이 보기엔 작은 변화 $\delta$로 모델 손실을 크게 만들려 한다. | adversarial robustness 평가 |
| P05 | $Adv=P(A=1\mid member)-P(A=1\mid nonmember)$ | 멤버십 공격은 학습에 들어간 데이터와 아닌 데이터를 얼마나 잘 구분하는지로 본다. | privacy leakage 평가축 |

## W02 대규모 최적화 & 데이터 오염 위협

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보고서 연결 |
|---|---|---|---|
| P01 | $\min_\theta \frac{1}{n}\sum_i L(f_\theta(x_i),y_i)$, $\theta_{t+1}=\theta_t-\eta\nabla L_B(\theta_t)$ | 학습은 평균 손실을 줄이는 일이고, SGD는 일부 샘플 묶음으로 업데이트 방향을 추정한다. | 데이터 오염이 gradient를 바꾸는 원리 |
| P02 | $CR=Size_{base}/Size_{compressed}$ | 경량화는 모델 크기나 비용을 줄이지만 보안 탐지 능력도 함께 확인해야 한다. | 효율성-보안 trade-off |
| P03 | $\max_{D_p} L_{val}(\theta^*(D\cup D_p))$ | poisoning은 오염 데이터 $D_p$를 넣어 학습된 모델이 검증에서 실패하게 만드는 훈련 단계 공격이다. | poisoning threat model |
| P04 | $Impact=Perf_{clean}-Perf_{poisoned}$ | 데이터 오염의 피해는 정상 학습 대비 성능이 얼마나 떨어졌는지로 먼저 볼 수 있다. | accuracy drop, provenance |
| P05 | $ASR=N_{target}/N_{trigger}$ | backdoor는 정상 성능이 좋아도 trigger 입력에서 목표 오분류가 많으면 실패다. | clean accuracy와 ASR 분리 |

## W03 컴퓨터비전 & 대적 공격

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보고서 연결 |
|---|---|---|---|
| P01 | $y_{i,j,k}=\sigma(\sum_{u,v,c}W_{u,v,c,k}x_{i+u,j+v,c}+b_k)$ | CNN은 작은 필터를 이미지 위로 움직이며 지역 패턴을 찾는다. | 이미지 특징 추출 원리 |
| P02 | $CE=-\sum_c y_c\log p_c$ | 분류 모델은 정답 클래스 확률이 낮을수록 큰 벌점을 받는다. | vision classifier 평가 |
| P03 | $Attn(Q,K,V)=softmax(QK^T/\sqrt d)V$ | multimodal transformer는 서로 관련 있는 시각·텍스트 단서를 더 크게 본다. | multimodal robustness |
| P04 | $z_0=[x_{class};x_1E;\dots;x_NE]+E_{pos}$ | Vision Transformer는 이미지를 패치 토큰으로 바꾼 뒤 Transformer에 넣는다. | vision transformer 구조 |
| P05 | $RA=\frac{1}{n}\sum_i 1[f(x_i+\delta_i)=y_i]$ | robust accuracy는 공격 변형이 들어간 뒤에도 정답을 맞힌 비율이다. | 2D/3D adversarial 안전성 |

## W04 Transformer/NLP 보안

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보고서 연결 |
|---|---|---|---|
| P01 | $Cost_{attn}=O(n^2d)$ | 기본 attention은 토큰 수가 늘면 비용이 제곱으로 커져 긴 문서 처리에 부담이 된다. | efficient transformer 필요성 |
| P02 | $Speedup=T_{base}/T_{efficient}$ | 빠른 모델은 같은 작업을 더 짧은 시간에 처리하지만 정확도와 보안성을 같이 봐야 한다. | 속도·비용 평가 |
| P03 | $Attn(Q,K,V)=softmax(QK^T/\sqrt d)V$ | Transformer는 현재 토큰이 다른 토큰을 얼마나 참고할지 가중합으로 계산한다. | NLP/LLM 공통 원리 |
| P04 | $\max_{x'}L(f(x'),y)\;s.t.\;Sim(x,x')\ge\tau$ | NLP 대적 공격은 의미는 비슷하게 유지하면서 모델 판단만 바꾸려 한다. | semantic-preserving attack |
| P05 | $Leak=N_{sensitive}/N_{tests}$ | 프롬프트 프라이버시는 민감 정보가 출력으로 새어 나온 비율을 별도 기록한다. | prompt privacy 평가 |

## W05 Self-Supervised Learning & Backdoor

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보고서 연결 |
|---|---|---|---|
| P01 | $L_{NCE}=-\log \frac{\exp(sim(z_i,z_j)/\tau)}{\sum_k \exp(sim(z_i,z_k)/\tau)}$ | SSL은 같은 대상의 두 보기끼리는 가깝게, 다른 대상은 멀게 표현을 학습한다. | 표현학습 원리 |
| P02 | $L_{rec}=-\log \sigma(s(u,i)-s(u,j))$ | 추천 SSL은 사용자가 선호한 항목 점수가 덜 선호한 항목보다 높아지도록 학습한다. | 추천 모델 보안 |
| P03 | $L_{temp}=\sum_t \|z_t-z_{t+1}\|$ | 비디오 SSL은 시간적으로 이어진 장면의 표현이 너무 튀지 않게 만든다. | 영상 backdoor/robustness |
| P04 | $\max_{D_p} L_{test}(\theta^*(D\cup D_p))$ | poisoning은 학습 데이터 일부를 바꾸어 최종 모델을 공격자에게 유리하게 만든다. | training-time threat |
| P05 | $ASR=N_{trigger\to target}/N_{trigger}$ | backdoor 방어는 정상 정확도뿐 아니라 trigger 성공률 감소를 봐야 한다. | ASR, stealthiness |

## W06 Diffusion/GAN & Deepfake

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보고서 연결 |
|---|---|---|---|
| P01 | $q(x_t\mid x_{t-1})=\mathcal N(\sqrt{1-\beta_t}x_{t-1},\beta_t I)$, $L=\|\epsilon-\epsilon_\theta(x_t,t)\|^2$ | diffusion은 이미지에 노이즈를 조금씩 섞고, 모델은 그 노이즈를 거꾸로 제거하는 법을 배운다. | 생성모형 원리 |
| P02 | $p(x_{1:T})=\prod_t p(x_t\mid x_{<t},c)$ | 비디오 생성은 한 장면만이 아니라 시간 흐름과 조건을 함께 맞춰야 한다. | temporal consistency |
| P03 | $\min_G\max_D E_x[\log D(x)]+E_z[\log(1-D(G(z)))]$ | GAN은 생성기와 판별기가 서로 겨루며 더 그럴듯한 샘플을 만든다. | 생성·탐지 경쟁 구조 |
| P04 | $Score=\sigma(w^T\phi(x)+b)$ | deepfake 탐지는 영상 특징 $\phi(x)$가 조작 신호를 얼마나 담는지 점수화한다. | deepfake detection |
| P05 | $ECE=\sum_m \frac{\lvert B_m\rvert}{n}\lvert acc(B_m)-conf(B_m)\rvert$ | 신뢰성 평가는 모델의 확신과 실제 정답률이 맞는지도 본다. | reliability, calibration |

## W07 LLM 보안·프라이버시

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보고서 연결 |
|---|---|---|---|
| P01 | $Score=\frac{1}{K}\sum_k s_k$ | LLM 평가는 여러 능력·위험 항목을 나누어 평균 또는 가중합으로 본다. | LLM evaluation taxonomy |
| P02 | $Risk=N_{unsafe}/N_{prompts}$ | 안전하지 않은 답변 비율을 따로 세어야 성능과 위험을 분리할 수 있다. | LLM security/privacy risk |
| P03 | $TotalRisk=\sum_i w_i r_i$ | LLM 보안은 jailbreak, privacy, misuse 같은 여러 위험을 가중합으로 관리할 수 있다. | Good/Bad/Ugly taxonomy |
| P04 | $z=f_{align}(z_{text},z_{image})$ | multimodal LLM은 이미지와 텍스트 표현을 맞추므로 한쪽 입력의 오염이 다른 쪽 판단에 영향을 줄 수 있다. | multimodal attack surface |
| P05 | $VulnRate=N_{vulnerable}/N_{code}$ | 코드 보안 LLM 평가는 생성 코드 중 취약한 산출물 비율을 별도 측정한다. | software security meets LLMs |

## W08 RAG·프롬프트 인젝션

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보고서 연결 |
|---|---|---|---|
| P01 | $TopK(q)=arg\,top_k\,sim(e(q),e(d_i))$ | RAG는 질문과 가장 비슷한 문서를 골라 답변 근거로 넣는다. | retrieval provenance |
| P02 | $Score(v)=\alpha sim(q,v)+(1-\alpha)centrality(v)$ | GraphRAG는 관련성뿐 아니라 graph에서 중요한 노드인지도 고려할 수 있다. | graph source verification |
| P03 | $y=LLM(P_{sys},P_{user},C,T)$ | LLM 앱의 출력은 system prompt, 사용자 입력, 검색 context, tool instruction이 함께 만든다. | prompt boundary 관리 |
| P04 | $ASR=N_{injection\_success}/N_{attack\_tests}$ | prompt injection 평가는 오염 지시가 실제 응답이나 tool action에 반영된 비율로 본다. | ASR/source filter |
| P05 | $UnsafeRate=N_{unsafe\_medical}/N_{medical\_tests}$ | 의료 조언처럼 안전중요 영역에서는 위험 답변 비율을 별도 측정해야 한다. | safety-critical prompt injection |

## W09 DRL & Cybersecurity

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보고서 연결 |
|---|---|---|---|
| P01 | $Q(s,a)\leftarrow Q(s,a)+\alpha[r+\gamma\max_{a'}Q(s',a')-Q(s,a)]$ | 강화학습 에이전트는 행동 뒤 받은 보상으로 다음 선택 가치를 고친다. | DRL 기본 원리 |
| P02 | $J(\pi)=E[\sum_t \gamma^t r_t]$ | 자율주행/제어 DRL은 장기 보상 합이 커지는 정책을 찾는다. | safe policy evaluation |
| P03 | $R=TP-\lambda FP-\mu FN-\rho Cost$ | 사이버 방어 보상은 탐지 성공만 아니라 오탐, 미탐, 비용을 함께 반영해야 한다. | cyber defense reward design |
| P04 | $F1=2PR/(P+R)$ | IDS/IPS는 공격 탐지율과 오탐 관리가 동시에 중요하다. | RL-based IDS 평가 |
| P05 | $P_\pi(\varphi)\ge p$ | DRL 검증은 정책이 안전 속성 $\varphi$를 충분히 높은 확률로 만족하는지 확인한다. | policy verification |

## W10 Federated Learning 보안

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보고서 연결 |
|---|---|---|---|
| P01 | $\theta^{t+1}=\sum_k \frac{n_k}{n}\theta_k^{t+1}$ | FedAvg는 각 클라이언트 모델을 데이터 수 비율로 평균해 전역 모델을 만든다. | FL aggregation |
| P02 | $LeakageProxy=\|g_k-\bar g\|$ | 업데이트가 평균과 얼마나 다른지 보면 노출·이상 징후를 대략 점검할 수 있다. | privacy/security survey |
| P03 | $\theta_j^{t+1}=median_k(\theta_{k,j}^{t+1})$ | coordinate median은 극단적인 악성 업데이트가 평균을 흔드는 일을 줄인다. | robust aggregation |
| P04 | $MIAcc=(TP+TN)/N$ | FL에서도 업데이트나 출력에서 특정 데이터의 포함 여부를 추론할 수 있다. | privacy attack |
| P05 | $ASR=N_{trigger\to target}/N_{trigger}$ | 연합학습 backdoor는 악성 클라이언트 비율과 집계 방식에 따라 달라진다. | FL backdoor 평가 |

## W11 Differential Privacy & Membership Inference

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보고서 연결 |
|---|---|---|---|
| P01 | $Pr[M(D)\in S]\le e^\epsilon Pr[M(D')\in S]+\delta$ | DP는 한 사람의 데이터가 들어가도 결과 분포가 크게 바뀌지 않게 제한한다. | privacy claim 검증 |
| P02 | $\bar g_i=g_i/\max(1,\|g_i\|_2/C)$, $\tilde g=\frac{1}{B}(\sum_i\bar g_i+\mathcal N(0,\sigma^2C^2I))$ | DP-SGD는 각 샘플 gradient를 자르고 노이즈를 더해 개인 영향력을 줄인다. | DP-SGD 원리 |
| P03 | $\epsilon_{total}\approx \sum_t \epsilon_t$ | 여러 학습 step에서 privacy loss가 누적되므로 accountant가 필요하다. | privacy accounting |
| P04 | $MIAdv=TPR-FPR$ | membership inference 공격은 member를 잘 맞히면서 non-member를 덜 오인할수록 강하다. | MI risk |
| P05 | $Tradeoff=(Utility,\ PrivacyRisk)$ | 방어는 하나의 점수가 아니라 성능과 privacy risk를 함께 보고해야 한다. | utility-privacy trade-off |

## W12 Neural Network Verification & XAI

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보고서 연결 |
|---|---|---|---|
| P01 | $\forall x'\in B_\epsilon(x): f(x')=y$ | 검증은 작은 입력 변화 안에서도 모델 예측이 유지되는지 확인한다. | certified robustness |
| P02 | $\delta^*=arg\max_{\|\delta\|\le\epsilon}L(f(x+\delta),y)$ | 공격은 제한된 변화 안에서 손실이 가장 커지는 방향을 찾는다. | adversarial attack |
| P03 | $Stability=1-\|E(x)-E(x')\|/\|x-x'\|$ | 설명 공격은 예측은 비슷한데 설명만 크게 바뀌게 만들 수 있다. | adversarial XAI |
| P04 | $\|f(x)-f(x')\|\le K\|x-x'\|$ | Lipschitz bound는 입력 변화가 출력 변화로 얼마나 커질 수 있는지 제한한다. | robustness regularization |
| P05 | $(Accuracy,\ Robustness,\ FairnessGap)$ | accuracy, robustness, fairness는 한 숫자로 합치기보다 벡터로 함께 보고하는 편이 안전하다. | triangular trade-off |

## W13 Model Stealing & Watermarking

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보고서 연결 |
|---|---|---|---|
| P01 | $Fidelity=\frac{1}{n}\sum_i 1[f_v(x_i)=f_s(x_i)]$ | 추출 모델이 원 모델과 얼마나 같은 답을 내는지로 도난 위험을 본다. | model extraction |
| P02 | $z=\frac{\lvert G\rvert-E[\lvert G\rvert]}{\sqrt{Var(\lvert G\rvert)}}$ | 워터마크 검출은 생성 토큰이 기대보다 많이 특정 집합에 들어가는지 통계적으로 본다. | LLM watermarking |
| P03 | $RobustDetect=N_{detected\ after\ attack}/N_{watermarked}$ | watermark는 pruning, fine-tuning, extraction 뒤에도 검출되어야 의미가 있다. | DNN watermarking |
| P04 | $TPR=N_{wm\ detected}/N_{wm}$, $FPR=N_{clean\ detected}/N_{clean}$ | 소유권 검증은 탐지율이 높아도 위양성이 높으면 강한 증거가 아니다. | ModelShield 평가 |
| P05 | $\min_G\max_D E[\log D(x)]+E[\log(1-D(G(z)))]$ | GAN 보안 문헌은 생성모형이 privacy와 misuse 위험을 함께 가진다는 배경을 준다. | secure/private generative models |

## W14 MLOps·공급망 보안

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보고서 연결 |
|---|---|---|---|
| P01 | $Coverage=N_{artifacts}/N_{required}$ | MLOps 재현성은 코드, config, data, model, log 등 필요한 산출물이 얼마나 남았는지로 본다. | artifact inventory |
| P02 | $DeployRisk=\sum_i P_i\times Impact_i$ | 배포 위험은 발생 가능성과 영향도를 함께 봐야 한다. | deployment challenge |
| P03 | $AnomalyScore=\|x-\hat x\|$ | AIOps는 관측값과 예측/복원값 차이가 클 때 이상으로 본다. | monitoring, rollback |
| P04 | $Latency=T_{upload}+T_{infer}+T_{download}$ | edge AI는 정확도뿐 아니라 통신·추론 지연이 보안 대응에 영향을 준다. | edge deployment |
| P05 | $SEScore=(Accuracy,F1,HumanReview)$ | 소프트웨어공학용 DL은 자동화 품질과 사람 검토를 함께 기록해야 한다. | secure software engineering |

## W15 연구평가·재현성·XAI·논문 구성

| ID | 핵심 수식/알고리즘 | 쉬운 설명 | 보고서 연결 |
|---|---|---|---|
| P01 | $ContamRate=N_{overlap}/N_{eval}$ | 평가셋 오염은 평가 문항이 학습·튜닝에 노출된 비율로 점검할 수 있다. | benchmark contamination |
| P02 | $AssuranceCoverage=N_{evidence}/N_{claims}$ | 연구 주장은 그 주장을 뒷받침하는 증거가 남아 있어야 한다. | lifecycle assurance |
| P03 | $Fidelity=P(f(x)=g(E(x)))$ | 설명이 원 모델 판단을 얼마나 잘 대변하는지 fidelity로 본다. | XAI core ideas, 관련 보조 문헌 원문 주의 |
| P04 | $Stability=1-\frac{1}{n}\sum_i\|E(x_i)-E(x_i')\|$ | 좋은 설명은 작은 입력 변화에 지나치게 흔들리지 않아야 한다. | responsible XAI |
| P05 | $TCAV_{C,k,l}=\frac{\lvert\{x:S_{C,k,l}(x)>0\}\rvert}{n}$ | concept-based XAI는 사람이 이해하는 개념 방향이 특정 클래스 판단에 얼마나 영향을 주는지 본다. | concept-based explanation |
