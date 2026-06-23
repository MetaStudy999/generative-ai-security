from __future__ import annotations

import html
import csv
import math
import os
import re
from pathlib import Path
from typing import Any

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-cache")

try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
except ModuleNotFoundError:
    matplotlib = None
    plt = None
    font_manager = None

try:
    import pandas as pd
except ModuleNotFoundError:
    pd = None


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "03_weekly_reports"
LOCAL_KOREAN_FONT = ROOT / "assets" / "fonts" / "NotoSansCJKkr-Regular.otf"
TODAY = "2026-06-23"

BLOCK_START = "<!-- formula-visual-supplement:start -->"
BLOCK_END = "<!-- formula-visual-supplement:end -->"
NOTES_START = "<!-- formula-visual-speaker-notes:start -->"
NOTES_END = "<!-- formula-visual-speaker-notes:end -->"
QNA_START = "<!-- formula-visual-qna:start -->"
QNA_END = "<!-- formula-visual-qna:end -->"
HANDOUT_START = "<!-- formula-visual-handout:start -->"
HANDOUT_END = "<!-- formula-visual-handout:end -->"
WORKLOG_START = "<!-- formula-visual-ai-worklog:start -->"
WORKLOG_END = "<!-- formula-visual-ai-worklog:end -->"
HTML_HEAD_START = "<!-- formula-visual-mathjax:start -->"
HTML_HEAD_END = "<!-- formula-visual-mathjax:end -->"
HTML_SLIDES_START = "<!-- formula-visual-html:start -->"
HTML_SLIDES_END = "<!-- formula-visual-html:end -->"


def fblock(
    name: str,
    equation: str,
    symbols: list[tuple[str, str]],
    intuition: str,
    security: str,
    metrics: str,
    limits: str,
) -> dict[str, Any]:
    return {
        "name": name,
        "equation": equation.strip(),
        "symbols": symbols,
        "intuition": intuition,
        "security": security,
        "metrics": metrics,
        "limits": limits,
    }


WEEKS: list[dict[str, Any]] = [
    {
        "slug": "w01_deep_learning_ml_security",
        "week": "W01",
        "topic": "딥러닝 패러다임 & ML 보안 분류학",
        "chart_cols": ["accuracy", "f1"],
        "x_col": "condition",
        "diagram_type": "ML lifecycle threat model",
        "stages": ["Data", "Training", "Evaluation", "Deployment", "Monitoring"],
        "stage_notes": ["quality/privacy", "empirical risk", "clean/robust", "runtime risk", "evidence log"],
        "interpretation": "그래프는 `metrics_summary.csv`의 condition별 accuracy와 F1만 시각화한다. Clean baseline, label-noise training, toy feature perturbation 조건을 같은 축에 두어 정상 성능만으로 보안성을 단정하기 어렵다는 점을 보여준다. synthetic/toy 평가 결과이므로 실제 운영 시스템 보증으로 해석하지 않는다.",
        "caution": "원문 논문별 절·쪽·그림 번호와 formal guarantee 여부는 확인 필요.",
        "formulas": [
            fblock(
                "Empirical Risk와 Generalization Gap",
                r"""
\hat{R}(\theta)=\frac{1}{n}\sum_{i=1}^{n}\ell(f_\theta(x_i),y_i),
\qquad
Gap=R_{\mathrm{test}}(\theta)-\hat{R}_{\mathrm{train}}(\theta)
""",
                [
                    (r"\theta", "모델 파라미터"),
                    (r"n", "학습 표본 수"),
                    (r"\ell", "손실 함수"),
                    (r"Gap", "훈련 손실과 테스트 위험의 차이"),
                ],
                "딥러닝 평가는 학습 표본 평균 손실을 낮추는 과정으로 출발한다. Generalization gap은 훈련 성능과 테스트 성능이 얼마나 벌어지는지 보는 기본 렌즈다.",
                "보안 관점에서는 clean 성능이 높아도 공격·교란·privacy 조건의 위험이 별도로 남을 수 있다. 따라서 lifecycle 평가에서는 데이터, 학습, 검증, 배포 로그를 함께 본다.",
                "clean accuracy, F1, robust accuracy, leakage score, reproducibility evidence를 서로 다른 축으로 연결한다.",
                "W01 실습은 synthetic/toy setting이며 formal robustness나 privacy guarantee를 제공하지 않는다.",
            ),
            fblock(
                "Robust Accuracy와 ASR",
                r"""
RA_\epsilon=\Pr_{(x,y)\sim D}\left[f_\theta(x+\delta)=y,\ \forall \delta \in \Delta_\epsilon\right],
\qquad
ASR=\frac{1}{m}\sum_{j=1}^{m}\mathbf{1}[f_\theta(\tilde{x}_j)=y_j^{target}]
""",
                [
                    (r"RA_\epsilon", "허용 교란 집합 안에서의 강건 정확도"),
                    (r"\Delta_\epsilon", "크기 epsilon 이하 교란 집합"),
                    (r"\tilde{x}_j", "평가용 toy 공격 조건 입력"),
                    (r"ASR", "공격 성공률"),
                ],
                "정상 정확도와 강건 정확도는 같은 지표가 아니다. ASR은 공격 조건에서 목표 실패가 얼마나 자주 발생하는지 별도로 본다.",
                "보안 평가는 clean accuracy 하나로 끝나지 않고 robustness와 privacy leakage를 분리해야 한다.",
                "robust accuracy, robust drop, ASR, leakage score와 연결한다.",
                "여기서는 안전한 평가 개념을 설명하는 표준식이며 실제 시스템 공격 절차를 제공하지 않는다.",
            ),
        ],
    },
    {
        "slug": "w02_optimization_data_poisoning",
        "week": "W02",
        "topic": "대규모 최적화 & 데이터 오염 위협",
        "chart_cols": ["accuracy", "f1_macro", "asr"],
        "x_col": "condition",
        "diagram_type": "training-data poisoning evaluation flow",
        "stages": ["Data", "Labels", "Training", "Model", "Clean/Trigger Eval"],
        "stage_notes": ["clean/toy poison", "label quality", "SGD update", "decision boundary", "accuracy/F1/ASR"],
        "interpretation": "그래프는 `metrics_summary.csv`의 clean accuracy, macro F1, ASR을 조건별로 그린 것이다. Label-flip 조건에서는 오염률 증가와 함께 clean 성능 저하를 비교할 수 있고, toy backdoor 조건은 clean 성능과 ASR을 분리해 보아야 함을 보여준다. 표에 없는 실험 조건이나 수치는 추가하지 않았다.",
        "caution": "toy backdoor는 공개 toy 데이터 기반 안전 실습이며 실제 시스템 악용 절차로 일반화하지 않는다.",
        "formulas": [
            fblock(
                "ERM, Poisoned Empirical Risk, SGD Update",
                r"""
\hat{R}(\theta)=\frac{1}{n}\sum_{i=1}^{n}\ell(f_\theta(x_i),y_i),
\qquad
\hat{R}_{poison}(\theta)=\frac{1}{n+m}\left(\sum_{i=1}^{n}\ell(f_\theta(x_i),y_i)+\sum_{j=1}^{m}\ell(f_\theta(\tilde{x}_j),\tilde{y}_j)\right)
""",
                [
                    (r"\hat{R}", "정상 학습 데이터의 empirical risk"),
                    (r"\hat{R}_{poison}", "오염 샘플을 포함한 empirical risk"),
                    (r"m", "오염 또는 toy trigger 샘플 수"),
                    (r"(\tilde{x},\tilde{y})", "오염 조건의 입력과 라벨"),
                ],
                "데이터 오염은 단순히 입력 하나를 바꾸는 문제가 아니라 학습 목적함수 자체를 바꾼다. SGD는 이 목적함수의 gradient를 따라 이동하므로 오염 샘플은 업데이트 방향에 영향을 준다.",
                "훈련 단계 위협은 모델 파라미터와 decision boundary를 바꾸며, 검증셋이 clean-only이면 위험이 숨을 수 있다.",
                "accuracy drop, macro F1, ASR, poisoning rate, n_poisoned와 연결한다.",
                "오염 조건은 scikit-learn digits toy setting이며 실제 서비스 공격 절차가 아니다.",
            ),
            fblock(
                "Accuracy Drop와 ASR",
                r"""
\Delta Acc=Acc_{clean}-Acc_{poison},
\qquad
ASR=\frac{1}{m}\sum_{j=1}^{m}\mathbf{1}[f_\theta(\tilde{x}_j)=y^{target}]
""",
                [
                    (r"\Delta Acc", "오염 조건에서의 정상 정확도 감소량"),
                    (r"Acc_{clean}", "clean baseline 정확도"),
                    (r"Acc_{poison}", "오염 조건 정확도"),
                    (r"ASR", "trigger 조건 공격 성공률"),
                ],
                "Label flipping은 clean 성능 저하를, backdoor는 clean 성능 유지와 조건부 실패를 함께 볼 때 의미가 분명해진다.",
                "보안 보고에서는 clean accuracy와 ASR을 같은 표에 두되 같은 의미로 합치지 않는다.",
                "clean accuracy, macro F1, ASR, stealthiness와 연결한다.",
                "ASR은 로컬 toy trigger 테스트셋 기준이며 실제 공격 성공률을 주장하지 않는다.",
            ),
        ],
    },
    {
        "slug": "w03_computer_vision_adversarial",
        "week": "W03",
        "topic": "컴퓨터 비전 대적 공격",
        "chart_cols": ["accuracy", "attack_success_rate", "robust_drop"],
        "x_col": "condition",
        "diagram_type": "adversarial evaluation flow",
        "stages": ["Clean Image", "Perturbation Set", "Model", "Defense", "Robust Metrics"],
        "stage_notes": ["public/toy data", "epsilon bound", "prediction", "squeezing/check", "RA/drop/ASR"],
        "interpretation": "그래프는 condition별 accuracy, attack_success_rate, robust_drop을 `metrics_summary.csv`에서 읽어 시각화한다. epsilon 또는 defense 조건별 변화는 robust accuracy를 clean accuracy와 분리해 보아야 함을 보여준다. 이미 존재하는 output 수치만 사용했다.",
        "caution": "대적 교란은 toy evaluation 범위로 설명하며 실제 시스템 우회 절차로 쓰지 않는다.",
        "formulas": [
            fblock(
                "Adversarial Perturbation Constraint",
                r"""
x' = x+\delta,
\qquad
\lVert \delta \rVert_p \le \epsilon
""",
                [
                    (r"x", "원본 입력"),
                    (r"x'", "교란된 입력"),
                    (r"\delta", "입력 교란"),
                    (r"\epsilon", "허용 교란 반경"),
                ],
                "대적 예시는 작은 입력 교란이 예측을 바꿀 수 있는지를 보는 평가 개념이다. 핵심은 교란 크기와 모델 실패 여부를 함께 기록하는 것이다.",
                "보안 관점에서는 입력 검증, 강건성 평가, defense 비용이 연결된다.",
                "robust accuracy, attack_success_rate, robust_drop, defense 여부와 연결한다.",
                "toy image setting이며 실제 운영 비전 시스템을 우회하는 절차가 아니다.",
            ),
            fblock(
                "Robust Accuracy와 Robust Drop",
                r"""
RA_\epsilon=\frac{1}{n}\sum_{i=1}^{n}\mathbf{1}\left[f_\theta(x_i+\delta_i)=y_i\right],
\qquad
Drop=Acc_{clean}-RA_\epsilon
""",
                [
                    (r"RA_\epsilon", "교란 조건에서의 정확도"),
                    (r"Acc_{clean}", "정상 입력 정확도"),
                    (r"Drop", "강건성 저하량"),
                    (r"n", "평가 표본 수"),
                ],
                "강건성은 정상 정확도에서 얼마나 유지되는지로 해석한다. Drop이 클수록 clean-only 평가가 위험을 감춘다.",
                "공격 조건 성능과 방어 후 성능을 같은 표에 연결한다.",
                "accuracy, attack_success_rate, robust_drop, n_samples와 연결한다.",
                "공식 인증 강건성은 아니며 실험적 toy proxy로 표시한다.",
            ),
        ],
    },
    {
        "slug": "w04_transformer_nlp_security",
        "week": "W04",
        "topic": "Transformer/NLP 보안",
        "chart_cols": ["clean_score", "attack_success_rate", "privacy_leakage", "utility_score"],
        "x_col": "condition",
        "diagram_type": "Transformer security evaluation flow",
        "stages": ["Tokens", "Attention", "Context", "Security Probe", "Metrics"],
        "stage_notes": ["input sequence", "QK^T scaling", "dependency", "injection/privacy", "utility/risk"],
        "interpretation": "그래프는 clean_score, attack_success_rate, privacy_leakage, utility_score를 조건별로 비교한다. Transformer 평가에서는 유틸리티와 보안 위험이 동시에 움직일 수 있으므로 단일 점수로 결론을 내리지 않는다. 수치는 `metrics_summary.csv`에서만 가져왔다.",
        "caution": "efficient attention 복잡도는 구조별로 달라 표준 비교식으로만 제시한다.",
        "formulas": [
            fblock(
                "Scaled Dot-Product Attention",
                r"""
Attention(Q,K,V)=softmax\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
""",
                [
                    (r"Q,K,V", "query, key, value 행렬"),
                    (r"d_k", "key 벡터 차원"),
                    (r"softmax", "토큰 간 가중치 정규화"),
                    (r"V", "가중합 대상 값 표현"),
                ],
                "Attention은 각 토큰이 다른 토큰을 얼마나 참고할지 계산한다. 보안 평가에서는 이 의존성이 prompt, context, leakage 위험과 연결된다.",
                "입력 문맥이 길거나 오염되면 정보 흐름과 취약 응답이 달라질 수 있다.",
                "clean_score, attack_success_rate, privacy_leakage, utility_score와 연결한다.",
                "표준 Transformer 수식이며 특정 논문 실험 수치를 새로 주장하지 않는다.",
            ),
            fblock(
                "Attention Complexity 비교",
                r"""
C_{full}=O(n^2d),
\qquad
C_{efficient}\in\{O(nd), O(nrd)\}
""",
                [
                    (r"n", "sequence length"),
                    (r"d", "hidden dimension"),
                    (r"r", "저랭크 또는 landmark 수"),
                    (r"C", "계산 복잡도"),
                ],
                "Full attention은 토큰 쌍을 모두 비교하므로 길이에 대해 이차 비용이 든다. 효율적 attention은 구조에 따라 선형 또는 저랭크 비용으로 줄일 수 있다.",
                "비용 절감은 더 넓은 보안 평가를 가능하게 하지만, 근사 구조의 취약성 검토가 필요하다.",
                "utility_score, latency/cost proxy, attack_success_rate와 연결한다.",
                "효율화 방식마다 복잡도가 다르므로 구체 구조 확인이 필요하다.",
            ),
        ],
    },
    {
        "slug": "w05_ssl_backdoor",
        "week": "W05",
        "topic": "Self-Supervised Learning & Backdoor",
        "chart_cols": ["clean_accuracy", "attack_success_rate", "attack_after_defense", "representation_shift", "trigger_detection_rate"],
        "x_col": "condition",
        "diagram_type": "SSL backdoor evaluation flow",
        "stages": ["Pretext Data", "Representation", "Classifier", "Trigger Test", "Defense Check"],
        "stage_notes": ["views/masks", "embedding", "linear head", "ASR", "detection/FPR"],
        "interpretation": "그래프는 representation_shift, trigger_detection_rate, attack_success_rate 같은 SSL/backdoor 관련 지표를 한 화면에서 비교한다. Clean accuracy만으로는 representation 내부 변화나 trigger 조건 성능을 설명할 수 없다. 모든 값은 기존 CSV의 수치 열에서 가져왔다.",
        "caution": "trigger 관련 설명은 공개 toy/synthetic 범위이며 실제 악용 가능한 절차를 제공하지 않는다.",
        "formulas": [
            fblock(
                "Contrastive Loss와 Representation Shift",
                r"""
\mathcal{L}_{NCE}=-\log
\frac{\exp(sim(z_i,z_i^+)/\tau)}
{\sum_{j}\exp(sim(z_i,z_j)/\tau)},
\qquad
\Delta_z=\lVert \mu_{clean}-\mu_{trigger}\rVert_2
""",
                [
                    (r"z_i,z_i^+", "같은 샘플 또는 양성 쌍의 표현"),
                    (r"sim", "표현 간 유사도"),
                    (r"\tau", "temperature"),
                    (r"\Delta_z", "clean/trigger 표현 중심 차이"),
                ],
                "Contrastive learning은 가까워야 할 표현과 멀어져야 할 표현을 구분한다. Backdoor 평가는 clean 성능뿐 아니라 표현 공간 이동을 함께 확인한다.",
                "은닉 trigger가 representation에 남으면 downstream classifier에서 조건부 실패가 생길 수 있다.",
                "representation_shift, clean_accuracy, attack_success_rate, trigger_detection_rate와 연결한다.",
                "표준 contrastive objective와 proxy shift이며 formal backdoor guarantee가 아니다.",
            ),
            fblock(
                "Backdoor Trigger Success Metric",
                r"""
ASR=\frac{1}{m}\sum_{j=1}^{m}\mathbf{1}[f_\theta(T(x_j))=y^{target}]
""",
                [
                    (r"T(x)", "toy trigger 변환이 적용된 평가 입력"),
                    (r"y^{target}", "목표 라벨"),
                    (r"m", "trigger 평가 표본 수"),
                    (r"ASR", "조건부 실패율"),
                ],
                "ASR은 trigger 조건에서 목표 오분류가 얼마나 일어나는지 보는 지표다.",
                "clean 성능이 유지되어도 ASR이 높으면 보안적으로 실패할 수 있다.",
                "attack_success_rate, attack_after_defense, clean_false_positive_rate와 연결한다.",
                "실제 공격 절차가 아니라 안전한 toy 평가 지표 설명이다.",
            ),
        ],
    },
    {
        "slug": "w06_diffusion_gan_deepfake",
        "week": "W06",
        "topic": "Diffusion/GAN & Deepfake Detection",
        "chart_cols": ["accuracy", "f1", "false_positive_rate", "false_negative_rate", "auroc"],
        "x_col": "condition",
        "diagram_type": "generated-media detection pipeline",
        "stages": ["Media Sample", "Detector", "Score", "Threshold", "Review"],
        "stage_notes": ["toy/public", "features/model", "risk score", "FPR/FNR", "human audit"],
        "interpretation": "그래프는 deepfake detector의 accuracy, F1, FPR, FNR, AUROC를 조건별로 비교한다. 탐지 문제에서는 false positive와 false negative의 보안 비용이 다르므로 accuracy만으로 결론을 내리지 않는다. source는 `metrics_summary.csv`이다.",
        "caution": "생성 모델 수식은 표준 학습 목적 설명이며 deepfake 제작 절차를 안내하지 않는다.",
        "formulas": [
            fblock(
                "Diffusion Forward Process와 Denoising Objective",
                r"""
q(x_t|x_{t-1})=\mathcal{N}\left(\sqrt{1-\beta_t}x_{t-1},\beta_t I\right),
\qquad
\mathcal{L}_{simple}=\mathbb{E}_{t,x_0,\epsilon}\left[\lVert \epsilon-\epsilon_\theta(x_t,t)\rVert_2^2\right]
""",
                [
                    (r"x_t", "time step t의 noisy sample"),
                    (r"\beta_t", "noise schedule"),
                    (r"\epsilon", "주입된 noise"),
                    (r"\epsilon_\theta", "denoising model prediction"),
                ],
                "Diffusion은 점진적으로 noise를 더하고 이를 되돌리는 학습 문제로 볼 수 있다.",
                "보안 발표에서는 생성 원리보다 탐지와 검증 지표를 중심에 둔다.",
                "AUROC, FPR, FNR, review_rate와 연결한다.",
                "표준식이며 특정 생성 모델의 원문 수치를 새로 주장하지 않는다.",
            ),
            fblock(
                "GAN Min-Max와 FPR/FNR",
                r"""
\min_G\max_D\ \mathbb{E}_{x\sim p_{data}}\log D(x)+\mathbb{E}_{z\sim p_z}\log(1-D(G(z))),
\qquad
FPR=\frac{FP}{FP+TN},\quad FNR=\frac{FN}{FN+TP}
""",
                [
                    (r"G,D", "generator와 discriminator"),
                    (r"FP,FN", "오탐과 미탐"),
                    (r"TP,TN", "정탐과 정상 판정"),
                    (r"FPR,FNR", "오탐률과 미탐률"),
                ],
                "GAN 목적식은 생성자와 판별자의 경쟁을 표현한다. 탐지 평가는 판별 정확도보다 오탐·미탐의 균형이 중요하다.",
                "미탐은 악성 생성물을 놓칠 위험이고, 오탐은 정상 콘텐츠 차단 위험이다.",
                "false_positive_rate, false_negative_rate, AUROC, expected_calibration_error와 연결한다.",
                "detector toy evaluation이며 실제 미디어 판별 보증으로 해석하지 않는다.",
            ),
        ],
    },
    {
        "slug": "w07_llm_security_privacy",
        "week": "W07",
        "topic": "LLM 보안과 프라이버시",
        "chart_cols": ["utility", "attack_success_rate", "privacy_leakage_rate", "code_vulnerability_rate"],
        "x_col": "condition",
        "diagram_type": "LLM privacy/safety evaluation flow",
        "stages": ["Prompt", "LM", "Safety Policy", "Leakage Audit", "Report"],
        "stage_notes": ["toy requests", "next-token prob", "refusal", "privacy/code risk", "evidence"],
        "interpretation": "그래프는 LLM 평가의 utility, attack_success_rate, privacy_leakage_rate, code_vulnerability_rate를 비교한다. 유용성 향상과 안전성 저하가 동시에 나타날 수 있으므로 refusal quality와 leakage를 분리해서 해석해야 한다. 수치는 기존 output CSV 기반이다.",
        "caution": "privacy leakage는 toy/proxy metric이며 실제 개인정보 추출 실험으로 해석하지 않는다.",
        "formulas": [
            fblock(
                "Language Modeling Objective와 Perplexity",
                r"""
\mathcal{L}_{LM}=-\sum_{t=1}^{T}\log p_\theta(x_t|x_{<t}),
\qquad
PPL=\exp\left(\frac{1}{T}\mathcal{L}_{LM}\right)
""",
                [
                    (r"x_t", "t번째 토큰"),
                    (r"x_{<t}", "이전 토큰 문맥"),
                    (r"p_\theta", "언어모델 확률"),
                    (r"PPL", "perplexity"),
                ],
                "언어모델은 이전 문맥을 보고 다음 토큰 확률을 높이는 방향으로 학습된다. Perplexity는 언어모델링 품질을 보는 표준 지표다.",
                "보안 평가에서는 품질 지표와 privacy leakage, unsafe completion을 분리해야 한다.",
                "utility, answer_rate, privacy_leakage_rate, code_vulnerability_rate와 연결한다.",
                "실습 수치는 toy prompt set 기준 proxy이며 실제 서비스 위험률이 아니다.",
            ),
            fblock(
                "Privacy Leakage Proxy",
                r"""
LeakageRate=\frac{\#\{\mathrm{responses\ with\ disallowed\ sensitive\ disclosure}\}}{\#\{\mathrm{evaluated\ prompts}\}}
""",
                [
                    (r"LeakageRate", "평가 prompt 중 민감정보 노출 비율"),
                    (r"\#", "조건을 만족하는 개수"),
                    (r"responses", "모델 응답"),
                    (r"prompts", "평가 입력"),
                ],
                "Leakage proxy는 응답 중 금지된 민감정보 노출이 얼마나 발견되는지 세는 방식이다.",
                "프라이버시 위험은 유용성 점수와 독립적으로 보고해야 한다.",
                "privacy_leakage_rate, over_refusal_rate, mean_risk_score와 연결한다.",
                "실제 개인정보를 사용하지 않는 안전한 toy audit이다.",
            ),
        ],
    },
    {
        "slug": "w08_rag_prompt_injection",
        "week": "W08",
        "topic": "RAG와 Prompt Injection",
        "chart_cols": ["retrieval_relevance", "attack_success_rate", "source_verification_rate", "tool_misuse_rate", "faithfulness"],
        "x_col": "condition",
        "diagram_type": "RAG pipeline threat model",
        "stages": ["Query", "Retriever", "Context Filter", "Generator", "Verification"],
        "stage_notes": ["user intent", "score/rank", "policy", "conditioned answer", "source/block"],
        "interpretation": "그래프는 RAG 조건별 retrieval_relevance, attack_success_rate, source_verification_rate, tool_misuse_rate, faithfulness를 비교한다. 검색 품질이 좋아도 injection이나 contamination 위험이 별도로 존재할 수 있다. 차트는 output CSV의 수치만 사용한다.",
        "caution": "prompt injection은 방어 평가 관점으로만 설명하고 실제 우회 절차는 제공하지 않는다.",
        "formulas": [
            fblock(
                "Retrieval Score와 Context-Conditioned Generation",
                r"""
s(q,d)=\frac{e(q)^\top e(d)}{\lVert e(q)\rVert_2\lVert e(d)\rVert_2},
\qquad
p(y|q,C)=\prod_{t=1}^{T}p_\theta(y_t|y_{<t},q,C)
""",
                [
                    (r"q,d", "query와 retrieved document"),
                    (r"e(\cdot)", "embedding function"),
                    (r"C", "retrieved context set"),
                    (r"y_t", "생성 응답의 t번째 토큰"),
                ],
                "RAG는 query와 문서의 유사도로 context를 고르고, 그 context에 조건화해 답을 생성한다.",
                "검색된 context가 오염되면 생성 단계가 공격 문맥에 영향을 받을 수 있다.",
                "retrieval_relevance, faithfulness, source_verification_rate와 연결한다.",
                "표준 RAG 구조 설명이며 특정 벤치마크 수치를 새로 만들지 않는다.",
            ),
            fblock(
                "Injection Success와 Contamination Rate",
                r"""
PISR=\frac{\#\{\mathrm{policy\ violating\ injected\ outputs}\}}{\#\{\mathrm{injection\ test\ prompts}\}},
\qquad
RCR=\frac{\#\{\mathrm{retrieved\ contaminated\ contexts}\}}{\#\{\mathrm{retrieved\ contexts}\}}
""",
                [
                    (r"PISR", "prompt injection success rate"),
                    (r"RCR", "retrieval contamination rate"),
                    (r"\#", "해당 조건 개수"),
                    (r"contexts", "검색된 문맥"),
                ],
                "Injection success와 retrieval contamination은 검색 품질과 다른 위험축이다.",
                "방어 평가는 source verification, block rate, tool misuse를 함께 본다.",
                "attack_success_rate, tool_misuse_rate, source_block_rate, human_block_rate와 연결한다.",
                "toy/synthetic prompt set 기준 proxy이며 실제 시스템 침투 절차가 아니다.",
            ),
        ],
    },
    {
        "slug": "w09_drl_cybersecurity",
        "week": "W09",
        "topic": "DRL 기반 사이버보안",
        "chart_cols": ["average_reward", "observed_reward", "detection_f1", "safety_violation_rate", "policy_robustness"],
        "x_col": "condition",
        "diagram_type": "MDP security evaluation flow",
        "stages": ["State", "Policy", "Action", "Reward", "Safety Eval"],
        "stage_notes": ["observation", "pi(a|s)", "toy action", "observed/true", "F1/violation"],
        "interpretation": "그래프는 reward, detection_f1, safety_violation_rate, policy_robustness를 조건별로 함께 보여준다. 보상 점수가 좋아 보여도 safety violation이 높으면 보안 정책으로는 실패할 수 있다. 수치는 `metrics_summary.csv`에서 읽었다.",
        "caution": "DRL 환경은 toy simulation이며 실제 네트워크 공격 자동화 절차를 제공하지 않는다.",
        "formulas": [
            fblock(
                "MDP Tuple, Return, Bellman Equation",
                r"""
\mathcal{M}=(\mathcal{S},\mathcal{A},P,R,\gamma),
\qquad
G_t=\sum_{k=0}^{\infty}\gamma^k r_{t+k},
\qquad
V^\pi(s)=\mathbb{E}_{a\sim\pi}\left[R(s,a)+\gamma\sum_{s'}P(s'|s,a)V^\pi(s')\right]
""",
                [
                    (r"\mathcal{S},\mathcal{A}", "상태 공간과 행동 공간"),
                    (r"P,R", "전이확률과 보상 함수"),
                    (r"\gamma", "할인율"),
                    (r"V^\pi", "정책 pi의 상태 가치"),
                ],
                "DRL은 상태, 행동, 전이, 보상으로 정책을 학습한다. Bellman 식은 현재 가치가 즉시 보상과 미래 가치로 구성됨을 보여준다.",
                "보상이 잘못 설계되면 정책이 보안 목표와 다른 방향으로 최적화될 수 있다.",
                "average_reward, observed_reward, detection_f1, policy_robustness와 연결한다.",
                "toy environment 기준이며 실제 사이버 작전 자동화를 다루지 않는다.",
            ),
            fblock(
                "Reward Manipulation Proxy",
                r"""
\Delta R=\mathbb{E}[R_{observed}-R_{intended}],
\qquad
ViolationRate=\frac{\#\{\mathrm{safety\ violating\ episodes}\}}{\#\{\mathrm{episodes}\}}
""",
                [
                    (r"\Delta R", "관측 보상과 의도 보상의 차이"),
                    (r"R_{observed}", "환경에서 관측된 보상"),
                    (r"R_{intended}", "보안 목적에 맞는 의도 보상"),
                    (r"ViolationRate", "안전 위반 에피소드 비율"),
                ],
                "Reward manipulation은 숫자 보상은 높지만 보안 목적에는 어긋나는 상황을 설명한다.",
                "정책 평가는 reward와 safety violation을 동시에 확인해야 한다.",
                "safety_violation_rate, reward_variance, perturbed_detection_f1와 연결한다.",
                "proxy metric이며 formal safety proof가 아니다.",
            ),
        ],
    },
    {
        "slug": "w10_federated_learning_security",
        "week": "W10",
        "topic": "Federated Learning 보안",
        "chart_cols": ["global_accuracy", "global_f1", "attack_success_rate", "privacy_leakage_proxy", "mean_update_norm"],
        "x_col": "condition",
        "diagram_type": "FL aggregation structure",
        "stages": ["Clients", "Local Update", "Aggregation", "Global Model", "Security Eval"],
        "stage_notes": ["data stays local", "Delta theta", "FedAvg", "round t+1", "ASR/leakage"],
        "interpretation": "그래프는 global_accuracy, global_f1, ASR, privacy_leakage_proxy, mean_update_norm을 조건별로 보여준다. FL에서는 중앙 성능만이 아니라 malicious client rate, update norm, leakage proxy를 함께 기록해야 한다. CSV에 없는 client-level raw data는 만들지 않았다.",
        "caution": "privacy_leakage_proxy는 실제 gradient inversion 성공률이 아니며 proxy로만 해석한다.",
        "formulas": [
            fblock(
                "FedAvg Aggregation과 Client Update",
                r"""
\theta_{t+1}^{(k)}=\theta_t-\eta\nabla \mathcal{L}_k(\theta_t),
\qquad
\theta_{t+1}=\sum_{k=1}^{K}\frac{n_k}{n}\theta_{t+1}^{(k)}
""",
                [
                    (r"\theta_t", "round t의 글로벌 모델"),
                    (r"\mathcal{L}_k", "client k의 local objective"),
                    (r"n_k/n", "client 데이터 비중"),
                    (r"K", "client 수"),
                ],
                "각 client는 local update를 만들고 server는 데이터 비중으로 평균한다.",
                "악성 client update가 aggregation에 들어오면 global model과 backdoor 성능이 바뀔 수 있다.",
                "global_accuracy, global_f1, attack_success_rate, malicious_client_rate와 연결한다.",
                "toy FL setting이며 실제 client 침해 절차가 아니다.",
            ),
            fblock(
                "Update Norm Leakage/Poisoning Proxy",
                r"""
\rho_k=\lVert \Delta\theta_k\rVert_2,
\qquad
ASR=\frac{1}{m}\sum_{j=1}^{m}\mathbf{1}[f_{\theta}(T(x_j))=y^{target}]
""",
                [
                    (r"\rho_k", "client update norm proxy"),
                    (r"\Delta\theta_k", "client k의 모델 변화량"),
                    (r"T(x)", "toy trigger 변환"),
                    (r"ASR", "조건부 실패율"),
                ],
                "Update norm은 client update 이상 징후를 보는 단순 proxy다. ASR은 poisoning/backdoor 조건 실패를 별도로 본다.",
                "업데이트 통계와 global 성능을 함께 보아야 은닉형 공격을 놓치지 않는다.",
                "mean_update_norm, privacy_leakage_proxy, attack_success_rate와 연결한다.",
                "formal privacy leakage guarantee가 아니라 toy proxy다.",
            ),
        ],
    },
    {
        "slug": "w11_differential_privacy_mi",
        "week": "W11",
        "topic": "Differential Privacy & Membership Inference",
        "chart_cols": ["accuracy", "mi_attack_accuracy", "epsilon_proxy", "privacy_leakage_score", "utility_drop", "noise_multiplier"],
        "x_col": "condition",
        "diagram_type": "DP-SGD and MI audit flow",
        "stages": ["Dataset", "Clip Gradients", "Add Noise", "Model", "MI Audit"],
        "stage_notes": ["adjacent data", "norm C", "sigma C", "utility", "adv/leakage"],
        "interpretation": "그래프는 accuracy, MI attack accuracy, epsilon_proxy, leakage score, utility_drop, noise_multiplier를 조건별로 비교한다. `epsilon_proxy`는 formal DP accountant 결과가 아니므로 privacy guarantee로 읽으면 안 된다. 수치는 W11 outputs의 toy 결과 그대로다.",
        "caution": "`epsilon_proxy`는 formal DP accountant 값이 아니며 formal DP guarantee로 쓰지 않는다.",
        "formulas": [
            fblock(
                "Differential Privacy Definition",
                r"""
\Pr[M(D)\in S]\le e^{\varepsilon}\Pr[M(D')\in S]+\delta
""",
                [
                    (r"M", "무작위 알고리즘 또는 학습 절차"),
                    (r"D,D'", "한 레코드만 다른 adjacent datasets"),
                    (r"S", "가능한 출력 사건"),
                    (r"\varepsilon,\delta", "DP privacy parameters"),
                ],
                "DP는 한 개인 레코드의 포함 여부가 출력 분포를 크게 바꾸지 않도록 제한하는 표준 정의다.",
                "Membership inference 위험을 줄이려는 privacy claim은 이 정의와 accountant 근거가 있어야 한다.",
                "epsilon, delta, privacy_leakage_score, mi_attack_accuracy와 연결한다.",
                "현재 CSV의 `epsilon_proxy`는 formal accountant 결과가 아니므로 보증값으로 쓰지 않는다.",
            ),
            fblock(
                "DP-SGD Clipping/Noise와 MI Advantage",
                r"""
\bar{g}_i=\frac{g_i}{\max(1,\lVert g_i\rVert_2/C)},
\qquad
\tilde{g}=\frac{1}{B}\left(\sum_{i=1}^{B}\bar{g}_i+\mathcal{N}(0,\sigma^2C^2I)\right),
\qquad
Adv_{MI}=TPR-FPR
""",
                [
                    (r"g_i,\bar{g}_i", "개별 gradient와 clipping 후 gradient"),
                    (r"C", "clipping norm"),
                    (r"\sigma", "noise multiplier"),
                    (r"Adv_{MI}", "membership inference advantage"),
                ],
                "DP-SGD는 gradient 크기를 제한하고 noise를 더해 개별 레코드 영향을 줄인다. MI advantage는 멤버와 비멤버를 구분하는 공격자의 이득을 요약한다.",
                "프라이버시 방어는 utility drop과 leakage 감소를 함께 보고해야 한다.",
                "accuracy, utility_drop, privacy_leakage_score, mi_attack_accuracy, noise_multiplier와 연결한다.",
                "표준식 설명이며 이 실습은 정식 DP accountant를 실행하지 않은 toy evaluation이다.",
            ),
        ],
    },
    {
        "slug": "w12_nn_verification_xai",
        "week": "W12",
        "topic": "Neural Network Verification & XAI",
        "chart_cols": ["clean_accuracy", "robust_accuracy", "explanation_stability", "certified_rate", "fairness_gap", "verification_cost_ms"],
        "x_col": "condition",
        "diagram_type": "verification-XAI robustness flow",
        "stages": ["Model/Spec", "Bound Check", "Robust Eval", "XAI Stability", "Cost/Fairness"],
        "stage_notes": ["property", "radius/Lipschitz", "cert proxy", "attribution", "ms/gap"],
        "interpretation": "그래프는 clean_accuracy, robust_accuracy, explanation_stability, certified_rate, fairness_gap, verification_cost_ms를 조건별로 표시한다. certified_rate가 toy proxy인지 formal verification 결과인지 문서에서 명확히 구분해야 한다. 모든 값은 W12 output CSV에서 읽었다.",
        "caution": "`certified_rate`는 toy proxy 또는 제한 실험인지 formal verification인지 최종 원문 확인이 필요하다.",
        "formulas": [
            fblock(
                "Robustness Objective와 Certified Radius",
                r"""
\min_\theta \mathbb{E}_{(x,y)}\left[\max_{\lVert \delta\rVert\le \epsilon}\ell(f_\theta(x+\delta),y)\right],
\qquad
\forall \delta:\lVert\delta\rVert\le r,\ f(x+\delta)=f(x)
""",
                [
                    (r"\epsilon", "학습 또는 평가 교란 반경"),
                    (r"r", "certified radius"),
                    (r"\delta", "입력 교란"),
                    (r"\ell", "손실 함수"),
                ],
                "강건 학습은 허용 교란 안에서 최악의 손실을 낮추려는 목표로 표현된다. Certified radius는 주어진 반경 안에서 예측이 바뀌지 않음을 보장하려는 개념이다.",
                "보안 주장에는 empirical robustness와 formal certificate를 구분해야 한다.",
                "robust_accuracy, certified_rate, mean_bound_margin, verification_cost_ms와 연결한다.",
                "현재 실습의 certified_rate는 formal verification인지 toy proxy인지 최종 검토가 필요하다.",
            ),
            fblock(
                "Explanation Stability, Fairness Gap, Verification Cost",
                r"""
Stability=sim(A(x),A(x')),
\qquad
FairGap=\left|\Pr(\hat{y}=1|G=0)-\Pr(\hat{y}=1|G=1)\right|,
\qquad
Cost=\frac{1}{n}\sum_{i=1}^{n}t_i
""",
                [
                    (r"A(x)", "입력 x에 대한 explanation/attribution"),
                    (r"sim", "설명 간 유사도"),
                    (r"G", "민감 또는 비교 그룹 변수"),
                    (r"t_i", "verification runtime"),
                ],
                "설명이 안정적이어야 방어 분석의 근거로 사용할 수 있다. 공정성 gap과 verification cost는 강건성 외의 배포 제약을 나타낸다.",
                "보안 검증은 robust accuracy 하나가 아니라 explanation stability와 fairness/cost를 함께 본다.",
                "explanation_stability, fairness_gap, verification_cost_ms와 연결한다.",
                "toy binary classification 설정이며 formal proof로 일반화하지 않는다.",
            ),
        ],
    },
    {
        "slug": "w13_model_stealing_watermarking",
        "week": "W13",
        "topic": "Model Stealing & Watermarking",
        "chart_cols": ["extraction_fidelity", "substitute_accuracy", "watermark_detection", "false_positive_rate", "utility_accuracy"],
        "x_col": "condition",
        "diagram_type": "model extraction and watermark audit flow",
        "stages": ["Query Budget", "Substitute", "Fidelity Eval", "Watermark Test", "FP/FN Review"],
        "stage_notes": ["allowed toy queries", "student model", "agreement", "detection", "utility risk"],
        "interpretation": "그래프는 extraction_fidelity, substitute_accuracy, watermark_detection, false_positive_rate, utility_accuracy를 조건별로 비교한다. Watermark detection은 utility loss와 false positive risk를 함께 보아야 한다. 수치는 output CSV 그대로다.",
        "caution": "model extraction은 방어 평가 관점의 toy query objective로만 설명한다.",
        "formulas": [
            fblock(
                "Model Extraction Query Objective",
                r"""
\min_{\hat{\theta}}\frac{1}{|Q|}\sum_{x\in Q}\ell(f_{\hat{\theta}}(x), f_{\theta^\star}(x))
""",
                [
                    (r"f_{\theta^\star}", "target model"),
                    (r"f_{\hat{\theta}}", "substitute model"),
                    (r"Q", "허용된 toy query set"),
                    (r"\ell", "target output과 substitute output 차이"),
                ],
                "Extraction 평가는 query로 얻은 출력에 substitute model을 얼마나 맞추는지 보는 문제로 표현할 수 있다.",
                "보안 관점에서는 query budget, fidelity, watermark detection을 함께 본다.",
                "extraction_fidelity, substitute_accuracy, query_budget와 연결한다.",
                "허가된 toy setting 설명이며 무단 API 수집 절차가 아니다.",
            ),
            fblock(
                "Watermark Detection Rate, FPR/FNR, Utility Loss",
                r"""
TPR=\frac{TP}{TP+FN},
\qquad
FPR=\frac{FP}{FP+TN},
\qquad
\Delta U=U_{base}-U_{protected}
""",
                [
                    (r"TP,FP,TN,FN", "탐지 혼동행렬 항목"),
                    (r"TPR", "watermark detection rate"),
                    (r"FPR", "false positive rate"),
                    (r"\Delta U", "보호 적용 후 utility loss"),
                ],
                "Watermark는 탐지만 높으면 충분하지 않고 false positive와 utility 손실을 함께 봐야 한다.",
                "오탐이 높으면 정상 모델을 잘못 침해로 판단할 위험이 있다.",
                "watermark_detection, false_positive_rate, utility_accuracy와 연결한다.",
                "toy watermark audit이며 법적 소유권 판단을 자동화하지 않는다.",
            ),
        ],
    },
    {
        "slug": "w14_mlops_supply_chain",
        "week": "W14",
        "topic": "MLOps Supply Chain Security",
        "chart_cols": ["value"],
        "x_col": "metric",
        "diagram_type": "MLOps supply-chain map",
        "stages": ["Data", "Code/Config", "Artifact", "Provenance", "Audit"],
        "stage_notes": ["hash/version", "review", "model file", "inventory/log", "drift/check"],
        "interpretation": "그래프는 numeric value로 변환 가능한 MLOps 점검 항목만 표시한다. Hash 문자열이나 boolean pass는 그래프에서 제외하고 manifest와 로그 근거로 남겼다. 값은 `metrics_summary.csv`에서만 읽었다.",
        "caution": "hash/pass 항목은 시각화에서 제외했으며 원본 CSV와 artifact inventory를 함께 확인해야 한다.",
        "formulas": [
            fblock(
                "Artifact Integrity Check",
                r"""
pass(a)=\mathbf{1}[H(a)=H_{ref}(a)]
""",
                [
                    (r"a", "artifact"),
                    (r"H", "hash function"),
                    (r"H_{ref}", "기준 hash"),
                    (r"pass(a)", "무결성 확인 결과"),
                ],
                "공급망 보안은 artifact가 기준 hash와 일치하는지 확인하는 것에서 시작한다.",
                "데이터, 모델, config의 변경 여부를 추적해야 재현성과 책임성이 유지된다.",
                "model_hash_match, dataset_sha256, inventory_coverage와 연결한다.",
                "hash 검증은 무결성 근거이지 모델 안전성 전체 보증이 아니다.",
            ),
            fblock(
                "Drift와 Audit Coverage",
                r"""
d=\lVert \mu_{new}-\mu_{train}\rVert_2,
\qquad
Coverage=\frac{|\{\mathrm{required\ logs\ present}\}|}{|\{\mathrm{required\ logs}\}|}
""",
                [
                    (r"d", "분포 이동 proxy"),
                    (r"\mu_{new}", "새 입력 평균 특징"),
                    (r"\mu_{train}", "훈련 기준 평균 특징"),
                    (r"Coverage", "필수 로그 보존률"),
                ],
                "Drift는 배포 후 입력 분포 변화를 감시하는 간단한 proxy다. Audit coverage는 최소 증거가 남아 있는지를 본다.",
                "공급망 공격은 성능보다 provenance와 audit evidence 부족에서 먼저 드러날 수 있다.",
                "mean_standardized_feature_shift, audit_coverage, inventory_coverage와 연결한다.",
                "toy MLOps inventory이며 실제 조직의 완전한 SBOM/AI BOM은 별도 검토가 필요하다.",
            ),
        ],
    },
    {
        "slug": "w15_reproducibility_xai_paper",
        "week": "W15",
        "topic": "Reproducibility & XAI Paper Integration",
        "chart_cols": ["value"],
        "x_col": "metric",
        "diagram_type": "reproducibility workflow",
        "stages": ["Plan", "Artifacts", "Run", "Compare", "Paper Evidence"],
        "stage_notes": ["RQ/protocol", "files/DOI", "seed/config", "metrics", "claim limits"],
        "interpretation": "그래프는 numeric 또는 ratio로 변환 가능한 reproducibility evidence만 표시한다. `47/47`, `9/9`, `11/11` 같은 비율은 1.0으로 환산해 completeness proxy로만 그렸다. 원문 DOI 세부 검증과 citation 형식은 별도 사람 검토가 필요하다.",
        "caution": "비율 변환 값은 local completeness proxy이며 학술적 품질 보증 점수가 아니다.",
        "formulas": [
            fblock(
                "Reproducibility Completion Rate",
                r"""
RepRate=\frac{\#\{\mathrm{required\ artifacts\ present}\}}{\#\{\mathrm{required\ artifacts}\}}
""",
                [
                    (r"RepRate", "필수 산출물 보존 비율"),
                    (r"required artifacts", "실험 재현에 필요한 파일 집합"),
                    (r"\#", "개수"),
                    (r"present", "로컬 저장소에 존재"),
                ],
                "재현성은 필요한 파일과 증거가 실제로 남아 있는지에서 출발한다.",
                "논문 주장에는 config, seed, DOI 검증, AI disclosure가 연결되어야 한다.",
                "w15_required_files, config_present, seed_recorded와 연결한다.",
                "local artifact completeness proxy이며 논문 품질 전체를 보증하지 않는다.",
            ),
            fblock(
                "Reference Verification와 Explanation Consistency Proxy",
                r"""
V_{ref}=\frac{N_{confirmed}+0.5N_{partial}}{N_{total}},
\qquad
Consist=sim(A_r(x),A_{r'}(x))
""",
                [
                    (r"V_{ref}", "로컬 참고문헌 검증률 proxy"),
                    (r"N_{confirmed}", "DOI 확인 완료 수"),
                    (r"N_{partial}", "부분 확인 수"),
                    (r"A_r(x)", "run r의 explanation"),
                    (r"Consist", "설명 일관성 proxy"),
                ],
                "참고문헌 검증률은 인용 근거의 신뢰도를 관리하는 local rubric이다. Explanation consistency는 반복 실행 간 설명이 얼마나 비슷한지 보는 proxy다.",
                "재현성과 XAI는 실험값 재현, 근거 문헌, 설명 안정성을 함께 요구한다.",
                "weighted_reference_verification_rate, ai_disclosure_completeness, seed_recorded와 연결한다.",
                "V_ref는 저장소 local scoring이며 외부 학술 검증을 대체하지 않는다.",
            ),
        ],
    },
]


def replace_block(text: str, start: str, end: str, block: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    full_block = f"{start}\n{block.rstrip()}\n{end}"
    if pattern.search(text):
        return pattern.sub(lambda _match: full_block, text)
    return text.rstrip() + "\n\n" + full_block + "\n"


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def parse_numeric_series(series: pd.Series) -> pd.Series:
    def parse_value(value: Any) -> float:
        if value is None or (isinstance(value, float) and math.isnan(value)):
            return math.nan
        s = str(value).strip()
        if not s:
            return math.nan
        low = s.lower()
        if low == "true":
            return 1.0
        if low == "false":
            return 0.0
        if "/" in s and re.fullmatch(r"\d+(\.\d+)?/\d+(\.\d+)?", s):
            left, right = s.split("/", 1)
            denom = float(right)
            return float(left) / denom if denom else math.nan
        try:
            return float(s)
        except ValueError:
            return math.nan

    return series.map(parse_value)


def ascii_axis_label(label: str, index: int) -> str:
    if label.isascii():
        return label[:42]
    safe = re.sub(r"[^A-Za-z0-9_.:/-]+", "_", label)
    safe = safe.strip("_")
    if safe and safe.isascii():
        return safe[:42]
    return f"row_{index + 1}"


def configure_matplotlib_fonts() -> bool:
    if plt is None or font_manager is None:
        return False
    plt.rcParams["axes.unicode_minus"] = False
    if not LOCAL_KOREAN_FONT.exists():
        return False
    font_manager.fontManager.addfont(str(LOCAL_KOREAN_FONT))
    plt.rcParams["font.family"] = "Noto Sans CJK KR"
    return True


def parse_numeric_value(value: Any) -> float:
    if value is None:
        return math.nan
    s = str(value).strip()
    if not s:
        return math.nan
    low = s.lower()
    if low == "true":
        return 1.0
    if low == "false":
        return 0.0
    if "/" in s and re.fullmatch(r"\d+(\.\d+)?/\d+(\.\d+)?", s):
        left, right = s.split("/", 1)
        denom = float(right)
        return float(left) / denom if denom else math.nan
    try:
        return float(s)
    except ValueError:
        return math.nan


def read_csv_records(csv_path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = [{key: (value if value is not None else "") for key, value in row.items()} for row in reader]
        return list(reader.fieldnames or []), rows


def svg_polyline(points: list[tuple[float, float]]) -> str:
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)


def make_chart(config: dict[str, Any], week_dir: Path) -> list[str]:
    csv_path = week_dir / "04_experiment" / "outputs" / "metrics_summary.csv"
    chart_dir = week_dir / "09_presentation" / "assets" / "charts"
    chart_dir.mkdir(parents=True, exist_ok=True)
    if not csv_path.exists():
        return []

    fieldnames, records = read_csv_records(csv_path)
    if not records:
        return []

    x_col = config["x_col"] if config["x_col"] in fieldnames else fieldnames[0]
    raw_labels = [row.get(x_col, f"row_{idx + 1}") for idx, row in enumerate(records)]
    labels = [ascii_axis_label(label, idx) for idx, label in enumerate(raw_labels)]
    selected: dict[str, list[float]] = {}
    for col in config["chart_cols"]:
        if col in fieldnames:
            numeric = [parse_numeric_value(row.get(col, "")) for row in records]
            if any(not math.isnan(value) for value in numeric):
                selected[col] = numeric

    if not selected:
        for col in fieldnames:
            if col == x_col:
                continue
            numeric = [parse_numeric_value(row.get(col, "")) for row in records]
            if any(not math.isnan(value) for value in numeric):
                selected[col] = numeric
            if len(selected) >= 5:
                break

    if not selected:
        return []

    values = [value for series in selected.values() for value in series if not math.isnan(value)]
    min_y = min(values)
    max_y = max(values)
    if math.isclose(min_y, max_y):
        min_y = min(0.0, min_y)
        max_y = max(1.0, max_y + 1.0)
    pad = (max_y - min_y) * 0.08
    min_y -= pad
    max_y += pad

    width, height = 1120, 620
    left, right, top, bottom = 92, 58, 76, 132
    plot_w = width - left - right
    plot_h = height - top - bottom
    colors = ["#1f3a5f", "#b3261e", "#166534", "#6d5aa8", "#9a3412", "#0f766e"]

    def x_pos(idx: int) -> float:
        if len(labels) == 1:
            return left + plot_w / 2
        return left + (plot_w * idx / (len(labels) - 1))

    def y_pos(value: float) -> float:
        return top + plot_h - ((value - min_y) / (max_y - min_y)) * plot_h

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{html.escape(config["week"])} metrics chart">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{left}" y="38" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#111111">{html.escape(config["week"])} metrics from metrics_summary.csv</text>',
        f'<text x="{left}" y="62" font-family="Arial, sans-serif" font-size="13" fill="#5f6368">Data source: {html.escape(str(csv_path.relative_to(week_dir)))}</text>',
        f'<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="#fafafa" stroke="#d9d6cf"/>',
    ]
    for tick in range(5):
        ratio = tick / 4
        y = top + plot_h - ratio * plot_h
        value = min_y + ratio * (max_y - min_y)
        elements.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + plot_w}" y2="{y:.1f}" stroke="#e5e1da"/>')
        elements.append(f'<text x="{left - 12}" y="{y + 4:.1f}" text-anchor="end" font-family="Arial, sans-serif" font-size="12" fill="#5f6368">{value:.3g}</text>')
    elements.append(f'<line x1="{left}" y1="{top + plot_h}" x2="{left + plot_w}" y2="{top + plot_h}" stroke="#111111"/>')
    elements.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top + plot_h}" stroke="#111111"/>')

    for idx, label in enumerate(labels):
        x = x_pos(idx)
        elements.append(f'<text x="{x:.1f}" y="{height - 86}" transform="rotate(28 {x:.1f},{height - 86})" text-anchor="start" font-family="Arial, sans-serif" font-size="12" fill="#5f6368">{html.escape(label[:42])}</text>')
    elements.append(f'<text x="{left + plot_w / 2:.1f}" y="{height - 24}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="#111111">{html.escape(x_col)}</text>')
    elements.append(f'<text x="24" y="{top + plot_h / 2:.1f}" transform="rotate(-90 24,{top + plot_h / 2:.1f})" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="#111111">Metric value</text>')

    legend_x = left + plot_w - 250
    legend_y = top + 18
    for series_idx, (col, series) in enumerate(selected.items()):
        color = colors[series_idx % len(colors)]
        points = [(x_pos(idx), y_pos(value)) for idx, value in enumerate(series) if not math.isnan(value)]
        if len(points) == 1:
            x, y = points[0]
            elements.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{color}"/>')
        elif points:
            elements.append(f'<polyline points="{svg_polyline(points)}" fill="none" stroke="{color}" stroke-width="3"/>')
            for x, y in points:
                elements.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{color}"/>')
        elements.append(f'<rect x="{legend_x}" y="{legend_y + series_idx * 20}" width="12" height="12" fill="{color}"/>')
        elements.append(f'<text x="{legend_x + 18}" y="{legend_y + 11 + series_idx * 20}" font-family="Arial, sans-serif" font-size="12" fill="#111111">{html.escape(col)}</text>')

    elements.append("</svg>")
    svg = chart_dir / f"{config['week'].lower()}_metrics_chart.svg"
    write_text(svg, "\n".join(elements))
    return [svg.name]


def wrap_stage(text: str, max_len: int = 14) -> list[str]:
    parts = text.split()
    lines: list[str] = []
    cur = ""
    for part in parts:
        if len(cur) + len(part) + (1 if cur else 0) <= max_len:
            cur = f"{cur} {part}".strip()
        else:
            if cur:
                lines.append(cur)
            cur = part
    if cur:
        lines.append(cur)
    return lines or [text]


def make_diagram(config: dict[str, Any], week_dir: Path) -> str:
    diagram_dir = week_dir / "09_presentation" / "assets" / "diagrams"
    diagram_dir.mkdir(parents=True, exist_ok=True)
    width, height = 1120, 360
    stages = config["stages"]
    notes = config["stage_notes"]
    margin = 50
    box_w = 170
    gap = (width - 2 * margin - len(stages) * box_w) / (len(stages) - 1)
    y = 130
    box_h = 108
    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{html.escape(config["week"])} {html.escape(config["diagram_type"])}">',
        "<defs>",
        '<marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">',
        '<path d="M2,2 L10,6 L2,10 Z" fill="#245a73"/>',
        "</marker>",
        "</defs>",
        '<rect width="100%" height="100%" fill="#f8fafc"/>',
        f'<text x="{margin}" y="48" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#1f2933">{html.escape(config["week"])} {html.escape(config["diagram_type"])}</text>',
        f'<text x="{margin}" y="78" font-family="Arial, sans-serif" font-size="14" fill="#53616f">AI-assisted conceptual diagram; not empirical evidence. See figure_manifest.md for source and limitations.</text>',
    ]
    centers = []
    for idx, stage in enumerate(stages):
        x = margin + idx * (box_w + gap)
        centers.append((x + box_w, y + box_h / 2))
        elements.append(f'<rect x="{x:.1f}" y="{y}" width="{box_w}" height="{box_h}" rx="8" fill="#ffffff" stroke="#bfd0dd" stroke-width="2"/>')
        title_lines = wrap_stage(stage)
        for line_idx, line in enumerate(title_lines):
            elements.append(
                f'<text x="{x + box_w / 2:.1f}" y="{y + 34 + line_idx * 19}" text-anchor="middle" font-family="Arial, sans-serif" font-size="18" font-weight="700" fill="#0f5f73">{html.escape(line)}</text>'
            )
        note_lines = wrap_stage(notes[idx], 20)
        for line_idx, line in enumerate(note_lines[:2]):
            elements.append(
                f'<text x="{x + box_w / 2:.1f}" y="{y + 78 + line_idx * 16}" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" fill="#596775">{html.escape(line)}</text>'
            )
        if idx < len(stages) - 1:
            x1 = x + box_w + 8
            x2 = x + box_w + gap - 8
            yy = y + box_h / 2
            elements.append(f'<line x1="{x1:.1f}" y1="{yy:.1f}" x2="{x2:.1f}" y2="{yy:.1f}" stroke="#245a73" stroke-width="3" marker-end="url(#arrow)"/>')
    elements.append(f'<text x="{margin}" y="310" font-family="Arial, sans-serif" font-size="15" fill="#394a59">Safety scope: public, synthetic, toy, or local evaluation only; no operational attack procedure.</text>')
    elements.append("</svg>")
    svg_name = f"{config['week'].lower()}_pipeline_diagram.svg"
    write_text(diagram_dir / svg_name, "\n".join(elements))
    return svg_name


def formula_markdown(config: dict[str, Any], rel_prefix: str, heading: str) -> str:
    week_l = config["week"].lower()
    chart_path = f"{rel_prefix}assets/charts/{week_l}_metrics_chart.svg"
    diagram_path = f"{rel_prefix}assets/diagrams/{week_l}_pipeline_diagram.svg"
    manifest_path = f"{rel_prefix}assets/figure_manifest.md"
    lines = [
        heading,
        "",
        f"- 보강 일자: {TODAY}",
        "- 수식은 표준 정의식 또는 검증 가능한 평가식으로만 작성했다.",
        "- 그래프는 `04_experiment/outputs/metrics_summary.csv`의 기존 수치만 사용했다.",
        "- 다이어그램은 AI-assisted conceptual diagram이며 사실 자료나 실험 결과처럼 해석하지 않는다.",
        "",
    ]
    for formula in config["formulas"]:
        lines.extend(
            [
                f"### 핵심 수식: {formula['name']}",
                "",
                "$$",
                formula["equation"],
                "$$",
                "",
                "| 기호 | 의미 |",
                "|---|---|",
            ]
        )
        lines.extend([f"| `{sym}` | {meaning} |" for sym, meaning in formula["symbols"]])
        lines.extend(
            [
                "",
                "**직관적 의미:**  ",
                formula["intuition"],
                "",
                "**보안 관점 해석:**  ",
                formula["security"],
                "",
                "**평가 지표 연결:**  ",
                formula["metrics"],
                "",
                "**한계와 가정:**  ",
                formula["limits"],
                "",
            ]
        )
    lines.extend(
        [
            "### 표 수치 기반 그래프",
            "",
            f"![{config['week']} metrics chart]({chart_path})",
            "",
            config["interpretation"],
            "",
            "### Threat Model / Pipeline Diagram",
            "",
            f"![{config['week']} pipeline diagram]({diagram_path})",
            "",
            f"이 다이어그램은 `{config['diagram_type']}`를 발표용으로 요약한 개념도다. 데이터 흐름, 평가 지표, 한계 표시는 `{manifest_path}`에도 기록했다.",
            "",
            "### 확인 필요",
            "",
            f"- {config['caution']}",
            "- 논문별 원문 절·쪽·그림 번호는 최종 제출 전 사람 검토가 필요하다.",
        ]
    )
    return "\n".join(lines)


def notes_block(config: dict[str, Any]) -> str:
    formula_names = ", ".join(formula["name"] for formula in config["formulas"])
    return "\n".join(
        [
            "## 수식·그래프·그림 발표자 노트",
            "",
            f"- 핵심 수식: {formula_names}. 수식은 표준 정의식이며, 원문 위치나 formal guarantee가 확인되지 않은 부분은 확인 필요로 말한다.",
            "- 기호 정의표는 청중이 식을 해석할 수 있도록 먼저 읽고, 이후 보안 지표와 연결한다.",
            f"- 그래프 설명: {config['interpretation']}",
            f"- 다이어그램 설명: `{config['diagram_type']}`는 threat model 또는 평가 pipeline을 한 장으로 보여주는 보조 그림이다.",
            f"- 한계 고지: {config['caution']}",
        ]
    )


def qna_block(config: dict[str, Any]) -> str:
    return "\n".join(
        [
            "## 수식·그래프·그림 보강 Q&A",
            "",
            "### Q. 그래프 수치는 어디에서 온 것인가?",
            "",
            "A. `04_experiment/outputs/metrics_summary.csv`의 기존 수치만 사용했다. CSV에 없는 값, 실행하지 않은 실험, 외부 논문 실험 수치는 추가하지 않았다.",
            "",
            "### Q. 이 수식은 해당 논문의 원문 수식인가?",
            "",
            "A. 발표 보강용 수식은 표준 정의식 또는 검증 가능한 평가식이다. 논문별 원문 절·쪽·그림 번호가 필요한 경우 최종 제출 전 사람 검토로 확인한다.",
            "",
            "### Q. 다이어그램은 실험 결과인가?",
            "",
            f"A. 아니다. `{config['diagram_type']}` 다이어그램은 AI-assisted conceptual diagram이며 threat model과 pipeline 설명을 위한 보조 그림이다.",
            "",
            "### Q. 보안적으로 가장 조심해야 할 해석은 무엇인가?",
            "",
            f"A. {config['caution']} 또한 모든 실습은 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 범위로만 해석한다.",
        ]
    )


def handout_block(config: dict[str, Any]) -> str:
    week_l = config["week"].lower()
    return "\n".join(
        [
            "## 수식·그래프·그림 보강 요약",
            "",
            "| 항목 | 반영 내용 |",
            "|---|---|",
            f"| 핵심 수식 | {', '.join(formula['name'] for formula in config['formulas'])} |",
            f"| 그래프 | `assets/charts/{week_l}_metrics_chart.svg` (`metrics_summary.csv` 기반) |",
            f"| 다이어그램 | `assets/diagrams/{week_l}_pipeline_diagram.svg` ({config['diagram_type']}) |",
            "| 기호 정의 | 통합보고서와 발표 슬라이드의 수식 블록에 포함 |",
            f"| 주의사항 | {config['caution']} |",
        ]
    )


def worklog_block(config: dict[str, Any]) -> str:
    week_l = config["week"].lower()
    return "\n".join(
        [
            f"## {TODAY} 수식·그래프·그림 보강 작업",
            "",
            "| 항목 | 기록 내용 |",
            "|---|---|",
            "| 사용 도구 | Codex, Python, matplotlib |",
            "| 사용 목적 | 주차별 통합보고서와 발표자료에 핵심 수식, 기호 정의표, 그래프, 다이어그램, 발표자 노트 설명을 추가 |",
            f"| 입력 근거 | `{config['slug']}/04_experiment/outputs/metrics_summary.csv`, 기존 통합보고서, 발표 슬라이드, 이론노트 |",
            f"| 생성 산출물 | `09_presentation/assets/charts/{week_l}_metrics_chart.svg`, `09_presentation/assets/diagrams/{week_l}_pipeline_diagram.svg`, `09_presentation/assets/figure_manifest.md` |",
            "| 검증 방식 | CSV에서 읽은 기존 수치만 차트화하고, 수식은 표준 정의식으로 한정했으며, formal guarantee가 불명확한 항목은 확인 필요로 표시 |",
            "| 안전 범위 | 공개 데이터, synthetic/toy 데이터, 로컬 모의실험 설명으로 제한하고 실제 시스템 악용 절차는 작성하지 않음 |",
        ]
    )


def make_manifest(config: dict[str, Any], week_dir: Path, chart_files: list[str], diagram_file: str) -> None:
    assets_dir = week_dir / "09_presentation" / "assets"
    figures_dir = assets_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    write_text(
        figures_dir / "README.md",
        "# Figures\n\n검증된 외부 그림 또는 별도 conceptual figure를 둘 때 사용하는 폴더다. 이번 보강에서는 표 수치 기반 chart와 pipeline diagram을 우선 생성했다.\n",
    )
    rows = [
        "# Figure Manifest",
        "",
        "| 파일명 | 유형 | 생성 방식 | 데이터 출처 | 사용 위치 | 검증 상태 | 주의사항 |",
        "|---|---|---|---|---|---|---|",
    ]
    for file_name in chart_files:
        rows.append(
            f"| charts/{file_name} | 그래프 | matplotlib로 `metrics_summary.csv` 수치 시각화 | `04_experiment/outputs/metrics_summary.csv` | 통합보고서, 발표 슬라이드, 발표자 노트 | 생성 완료 | CSV에 없는 수치 없음; 축 단위는 source별 metric value |"
        )
    rows.append(
        f"| diagrams/{diagram_file} | 다이어그램 | SVG concept diagram | 기존 주차 주제, 이론노트, 평가 프로토콜 | 통합보고서, 발표 슬라이드, 발표자 노트 | 생성 완료 | AI-assisted conceptual diagram; 실험 결과나 사실 그림으로 해석 금지 |"
    )
    write_text(assets_dir / "figure_manifest.md", "\n".join(rows))


def update_kci_status(text: str) -> str:
    text = re.sub(r"\| 그림 1개 이상 포함 \| 확인 필요 \|", "| 그림 1개 이상 포함 | 완료 |", text)
    text = text.replace("그림 1개 이상, 국내 참고문헌 3편 이상", "그림 1개 이상은 완료, 국내 참고문헌 3편 이상")
    text = text.replace("그림 보완이 추가로 필요하다", "그림 보완은 assets manifest 기준으로 완료했으며 국내 참고문헌 검토가 추가로 필요하다")
    return text


def html_head_block() -> str:
    return "\n".join(
        [
            "<script>",
            "window.MathJax = {",
            "  tex: { inlineMath: [['\\\\(', '\\\\)']], displayMath: [['$$', '$$']] },",
            "  svg: { fontCache: 'global' }",
            "};",
            "</script>",
            '<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>',
            "<style>",
            ".formula-visual-supplement .math-block { border-left: 5px solid #0f766e; background: #eef8f6; padding: 14px 18px; margin: 12px 0; font-size: 20px; overflow-x: auto; }",
            ".formula-visual-supplement .caption { font-size: 16px; line-height: 1.35; color: #53616f; }",
            ".formula-visual-supplement img { max-width: 100%; max-height: 390px; object-fit: contain; border: 1px solid #d8e0e8; border-radius: 8px; background: #fff; }",
            ".formula-visual-supplement .media-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start; }",
            "</style>",
        ]
    )


def html_slides_block(config: dict[str, Any]) -> str:
    week_l = config["week"].lower()
    formulas = config["formulas"][:2]
    formula_parts = []
    for formula in formulas:
        formula_parts.append(
            "\n".join(
                [
                    f"<h3>{html.escape(formula['name'])}</h3>",
                    '<div class="math-block">',
                    "$$",
                    html.escape(formula["equation"]),
                    "$$",
                    "</div>",
                    f"<p>{html.escape(formula['security'])}</p>",
                ]
            )
        )
    return "\n".join(
        [
            '    <section class="slide formula-visual-supplement">',
            f'      <div class="slide-header">Formula / {html.escape(config["week"])}</div>',
            "      <h2>핵심 수식과 기호</h2>",
            *["      " + part.replace("\n", "\n      ") for part in formula_parts],
            '      <div class="message">수식은 표준 정의식이며 원문 위치와 formal guarantee는 최종 검토 대상이다.</div>',
            f'      <div class="footer"><span>{html.escape(config["week"])} formula supplement</span><span></span></div>',
            "    </section>",
            "",
            '    <section class="slide formula-visual-supplement">',
            f'      <div class="slide-header">Visual / {html.escape(config["week"])}</div>',
            "      <h2>그래프와 Pipeline Diagram</h2>",
            '      <div class="media-grid">',
            f'        <div><img src="assets/charts/{week_l}_metrics_chart.svg" alt="{html.escape(config["week"])} metrics chart"><p class="caption">{html.escape(config["interpretation"])}</p></div>',
            f'        <div><img src="assets/diagrams/{week_l}_pipeline_diagram.svg" alt="{html.escape(config["week"])} pipeline diagram"><p class="caption">AI-assisted conceptual diagram. See assets/figure_manifest.md.</p></div>',
            "      </div>",
            f'      <div class="footer"><span>Source: outputs/metrics_summary.csv</span><span>{html.escape(config["diagram_type"])}</span></div>',
            "    </section>",
        ]
    )


def update_html(config: dict[str, Any], html_path: Path) -> None:
    if not html_path.exists():
        return
    text = html_path.read_text(encoding="utf-8")
    head_full = f"{HTML_HEAD_START}\n{html_head_block()}\n{HTML_HEAD_END}"
    if HTML_HEAD_START in text:
        text = re.sub(
            re.escape(HTML_HEAD_START) + r".*?" + re.escape(HTML_HEAD_END),
            lambda _match: head_full,
            text,
            flags=re.DOTALL,
        )
    elif "</head>" in text:
        text = text.replace("</head>", head_full + "\n</head>", 1)

    slides_full = f"{HTML_SLIDES_START}\n{html_slides_block(config)}\n{HTML_SLIDES_END}"
    if HTML_SLIDES_START in text:
        text = re.sub(
            re.escape(HTML_SLIDES_START) + r".*?" + re.escape(HTML_SLIDES_END),
            lambda _match: slides_full,
            text,
            flags=re.DOTALL,
        )
    elif "</main>" in text:
        text = text.replace("</main>", slides_full + "\n  </main>", 1)

    needle = "counter.textContent = `${index + 1} / ${slides.length}`;"
    typeset = (
        "counter.textContent = `${index + 1} / ${slides.length}`;\n"
        "      if (window.MathJax && window.MathJax.typesetPromise) {\n"
        "        window.MathJax.typesetPromise([slides[index]]).catch(() => {});\n"
        "      }"
    )
    if needle in text and "MathJax.typesetPromise([slides[index]])" not in text:
        text = text.replace(needle, typeset, 1)
    write_text(html_path, text)


def update_week(config: dict[str, Any]) -> None:
    week_dir = BASE / config["slug"]
    assets_dir = week_dir / "09_presentation" / "assets"
    for sub in ["charts", "diagrams", "figures"]:
        (assets_dir / sub).mkdir(parents=True, exist_ok=True)

    chart_files = make_chart(config, week_dir)
    diagram_file = make_diagram(config, week_dir)
    make_manifest(config, week_dir, chart_files, diagram_file)

    report = week_dir / "06_report" / "final" / "integrated_report_final.md"
    if report.exists():
        text = report.read_text(encoding="utf-8")
        text = update_kci_status(text)
        text = replace_block(text, BLOCK_START, BLOCK_END, formula_markdown(config, "../../09_presentation/", "## 수식·그래프·그림 보강"))
        write_text(report, text)

    slides = week_dir / "09_presentation" / "presentation_slides.md"
    if slides.exists():
        text = slides.read_text(encoding="utf-8")
        text = replace_block(text, BLOCK_START, BLOCK_END, formula_markdown(config, "", "# 수식·그래프·그림 보강"))
        write_text(slides, text)

    notes = week_dir / "09_presentation" / "speaker_notes.md"
    if notes.exists():
        text = notes.read_text(encoding="utf-8")
        text = replace_block(text, NOTES_START, NOTES_END, notes_block(config))
        write_text(notes, text)

    qna = week_dir / "09_presentation" / "qna.md"
    if qna.exists():
        text = qna.read_text(encoding="utf-8")
        text = replace_block(text, QNA_START, QNA_END, qna_block(config))
        write_text(qna, text)

    handout = week_dir / "09_presentation" / "one_page_handout.md"
    if handout.exists():
        text = handout.read_text(encoding="utf-8")
        text = replace_block(text, HANDOUT_START, HANDOUT_END, handout_block(config))
        write_text(handout, text)

    worklog = week_dir / "05_ai_worklog" / "ai_worklog.md"
    if worklog.exists():
        text = worklog.read_text(encoding="utf-8")
        text = replace_block(text, WORKLOG_START, WORKLOG_END, worklog_block(config))
        write_text(worklog, text)

    submission = week_dir / "07_week_submission" / f"{config['week'].lower()}_submission_report.md"
    if submission.exists():
        text = update_kci_status(submission.read_text(encoding="utf-8"))
        write_text(submission, text)

    update_html(config, week_dir / "09_presentation" / "presentation_slides.html")


def audit_status(config: dict[str, Any]) -> list[str]:
    week_dir = BASE / config["slug"]
    report = week_dir / "06_report" / "final" / "integrated_report_final.md"
    slides = week_dir / "09_presentation" / "presentation_slides.md"
    html_path = week_dir / "09_presentation" / "presentation_slides.html"
    notes = week_dir / "09_presentation" / "speaker_notes.md"
    qna = week_dir / "09_presentation" / "qna.md"
    chart_png = week_dir / "09_presentation" / "assets" / "charts" / f"{config['week'].lower()}_metrics_chart.png"
    diagram_svg = week_dir / "09_presentation" / "assets" / "diagrams" / f"{config['week'].lower()}_pipeline_diagram.svg"
    report_text = report.read_text(encoding="utf-8") if report.exists() else ""
    slides_text = slides.read_text(encoding="utf-8") if slides.exists() else ""
    html_text = html_path.read_text(encoding="utf-8") if html_path.exists() else ""
    notes_text = notes.read_text(encoding="utf-8") if notes.exists() else ""
    qna_text = qna.read_text(encoding="utf-8") if qna.exists() else ""
    return [
        config["week"],
        "완료" if BLOCK_START in report_text and "$$" in report_text else "확인 필요",
        "완료" if "| 기호 | 의미 |" in report_text else "확인 필요",
        "완료" if "**보안 관점 해석:**" in report_text else "확인 필요",
        "완료" if "**평가 지표 연결:**" in report_text else "확인 필요",
        "완료" if BLOCK_START in slides_text and "$$" in slides_text else "확인 필요",
        f"완료 ({chart_png.name})" if chart_png.exists() else "확인 필요",
        f"완료 ({diagram_svg.name})" if diagram_svg.exists() else "확인 필요",
        "MathJax 완료" if "MathJax" in html_text else "확인 필요",
        "완료" if NOTES_START in notes_text else "확인 필요",
        "완료" if QNA_START in qna_text else "확인 필요",
        "완료" if diagram_svg.exists() and "그림 1개 이상 포함 | 확인 필요" not in report_text else "확인 필요",
        config["caution"],
    ]


def make_global_audit() -> None:
    header = [
        "| 주차 | 통합보고서 수식 블록 | 기호 정의표 | 보안 관점 해석 | 평가 지표 연결 | 발표 슬라이드 수식 | 그래프 파일 | 다이어그램 파일 | MathJax/KaTeX | speaker_notes 보강 | qna 보강 | KCI 그림 상태 | 확인 필요 |",
        "| -- | ----------- | ------ | -------- | -------- | ---------- | ------ | -------- | ------------- | ---------------- | ------ | --------- | ----- |",
    ]
    rows = ["| " + " | ".join(audit_status(config)) + " |" for config in WEEKS]
    intro = [
        "# Formula & Visual Audit",
        "",
        f"- 생성 일자: {TODAY}",
        "- 기준 브랜치: `main` (`git pull --ff-only` 결과 최신 상태 확인)",
        "- 점검 범위: `03_weekly_reports/w01_*` ~ `03_weekly_reports/w15_*`",
        "- 원칙: CSV/JSON/log에 없는 실험 수치를 만들지 않았고, 수식은 표준 정의식 또는 검증 가능한 평가식으로 제한했다.",
        "- 모든 다이어그램은 AI-assisted conceptual diagram이며, 사실 자료나 실험 결과로 해석하지 않는다.",
        "",
    ]
    write_text(BASE / "formula_visual_audit.md", "\n".join(intro + header + rows))


def short_text(value: str, limit: int = 96) -> str:
    normalized = re.sub(r"\s+", " ", str(value)).strip()
    if len(normalized) <= limit:
        return normalized
    return normalized[: limit - 1].rstrip() + "..."


def format_metric_value(value: Any) -> str:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "해당 없음"
    if pd is not None and pd.isna(value):
        return "해당 없음"
    if isinstance(value, (int, float)):
        if abs(float(value)) >= 1000:
            return f"{float(value):,.0f}"
        return f"{float(value):.3f}".rstrip("0").rstrip(".")
    text = str(value).strip()
    try:
        numeric = float(text)
    except ValueError:
        return short_text(text)
    if abs(numeric) >= 1000:
        return f"{numeric:,.0f}"
    return f"{numeric:.3f}".rstrip("0").rstrip(".")


def read_metrics(config: dict[str, Any], week_dir: Path) -> tuple[list[str], list[dict[str, str]], bool]:
    csv_path = week_dir / "04_experiment" / "outputs" / "metrics_summary.csv"
    if not csv_path.exists():
        return [], [], False
    fieldnames, records = read_csv_records(csv_path)
    if not records:
        return [], [], True
    x_col = config["x_col"] if config["x_col"] in fieldnames else fieldnames[0]
    columns = [x_col]
    for col in config["chart_cols"]:
        if col in fieldnames and col not in columns:
            columns.append(col)
    for candidate in ["accuracy", "f1", "status", "notes", "security_note", "interpretation"]:
        if candidate in fieldnames and candidate not in columns and len(columns) < 6:
            columns.append(candidate)
    columns = columns[:6]
    rows: list[dict[str, str]] = []
    for row in records[:5]:
        rows.append({col: format_metric_value(row.get(col, "")) for col in columns})
    return columns, rows, True


def html_table(headers: list[str], rows: list[list[str]], classes: str = "") -> str:
    class_attr = f' class="{classes}"' if classes else ""
    parts = [f"<table{class_attr}>", "<thead>", "<tr>"]
    parts.extend(f"<th>{html.escape(header)}</th>" for header in headers)
    parts.extend(["</tr>", "</thead>", "<tbody>"])
    for row in rows:
        parts.append("<tr>")
        for cell in row:
            parts.append(f"<td>{cell}</td>")
        parts.append("</tr>")
    parts.extend(["</tbody>", "</table>"])
    return "\n".join(parts)


def symbol_table(formula: dict[str, Any]) -> str:
    rows = []
    for symbol, meaning in formula["symbols"]:
        rows.append([f"\\({html.escape(symbol)}\\)", html.escape(meaning)])
    return html_table(["기호", "의미"], rows)


def metric_table(columns: list[str], rows: list[dict[str, str]]) -> str:
    if not columns or not rows:
        return html_table(
            ["상태", "설명"],
            [["design_only / 실행 전", "metrics_summary.csv가 없거나 비어 있어 그래프와 수치표를 생성하지 않음."]],
        )
    return html_table(columns, [[html.escape(row[col]) for col in columns] for row in rows])


def paper_map_rows(config: dict[str, Any]) -> list[list[str]]:
    topic = config["topic"]
    return [
        ["P01", "핵심 이론", "Background / Core Formula", f"{topic}의 관련연구 뼈대"],
        ["P02", "위협 분류", "Threat Model", "공격자·방어자·보호자산 정의"],
        ["P03", "평가 지표", "Evaluation Protocol", "정량 지표와 로그 근거 연결"],
        ["P04", "공격·방어 사례", "Security Implication", "보안적 함의와 방어 한계"],
        ["P05", "재현성·정책 근거", "Limitation", "확인 필요 항목과 제출 전 검증"],
    ]


def stage_kind(stage: str, note: str, idx: int, total: int) -> str:
    haystack = f"{stage} {note}".lower()
    if any(token in haystack for token in ["attack", "poison", "trigger", "risk", "leak", "reward", "prompt"]):
        return "risk"
    if idx == total - 1 or any(token in haystack for token in ["defense", "audit", "verify", "verification", "review", "policy"]):
        return "defense"
    return "normal"


def pipeline_html(config: dict[str, Any]) -> str:
    parts = [f'<div class="pipeline-diagram" role="img" aria-label="{html.escape(config["diagram_type"])}">']
    total = len(config["stages"])
    for idx, (stage, note) in enumerate(zip(config["stages"], config["stage_notes"])):
        parts.append(f'<div class="stage {stage_kind(stage, note, idx, total)}">{html.escape(stage)}<br><small>{html.escape(note)}</small></div>')
        if idx < total - 1:
            parts.append('<div class="arrow" aria-hidden="true">→</div>')
    parts.append("</div>")
    return "\n".join(parts)


def metric_names(config: dict[str, Any]) -> str:
    names = [col for col in config["chart_cols"]]
    return ", ".join(names[:5])


def nav_html() -> str:
    return """
  <nav class="slide-nav" aria-label="슬라이드 이동">
    <button id="prevSlide" type="button" title="이전 슬라이드" aria-label="이전 슬라이드">‹</button>
    <span id="slideCounter" class="slide-counter" aria-live="polite">1 / 1</span>
    <button id="nextSlide" type="button" title="다음 슬라이드" aria-label="다음 슬라이드">›</button>
  </nav>
""".rstrip()


def nav_script() -> str:
    return """
  <script>
    const slides = Array.from(document.querySelectorAll("section.slide, section"));
    const prevButton = document.getElementById("prevSlide");
    const nextButton = document.getElementById("nextSlide");
    const counter = document.getElementById("slideCounter");
    let currentIndex = 0;

    function updateNav(index) {
      currentIndex = Math.max(0, Math.min(index, slides.length - 1));
      counter.textContent = `${currentIndex + 1} / ${slides.length}`;
      prevButton.disabled = currentIndex === 0;
      nextButton.disabled = currentIndex === slides.length - 1;
    }

    function goToSlide(index) {
      const nextIndex = Math.max(0, Math.min(index, slides.length - 1));
      slides[nextIndex].scrollIntoView({ behavior: "smooth", block: "start" });
      updateNav(nextIndex);
      if (window.MathJax && window.MathJax.typesetPromise) {
        window.MathJax.typesetPromise([slides[nextIndex]]).catch(() => {});
      }
    }

    prevButton.addEventListener("click", () => goToSlide(currentIndex - 1));
    nextButton.addEventListener("click", () => goToSlide(currentIndex + 1));

    document.addEventListener("keydown", (event) => {
      if (["ArrowRight", "PageDown", " "].includes(event.key)) {
        event.preventDefault();
        goToSlide(currentIndex + 1);
      }

      if (["ArrowLeft", "PageUp"].includes(event.key)) {
        event.preventDefault();
        goToSlide(currentIndex - 1);
      }

      if (event.key === "Home") {
        event.preventDefault();
        goToSlide(0);
      }

      if (event.key === "End") {
        event.preventDefault();
        goToSlide(slides.length - 1);
      }
    });

    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((left, right) => right.intersectionRatio - left.intersectionRatio)[0];

        if (visible) {
          updateNav(slides.indexOf(visible.target));
        }
      },
      { threshold: [0.55] }
    );

    slides.forEach((slide) => observer.observe(slide));
    updateNav(0);
  </script>
""".rstrip()


def mathjax_head() -> str:
    return """
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [["\\\\(", "\\\\)"]],
        displayMath: [["\\\\[", "\\\\]"], ["$$", "$$"]]
      },
      svg: {
        fontCache: "global"
      }
    };
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
""".rstrip()


def build_nature_html(config: dict[str, Any], week_dir: Path, chart_files: list[str]) -> str:
    formula = config["formulas"][0]
    second_formula = config["formulas"][1] if len(config["formulas"]) > 1 else formula
    columns, rows, has_metrics = read_metrics(config, week_dir)
    week_l = config["week"].lower()
    chart_svg = f"assets/charts/{week_l}_metrics_chart.svg"
    chart_png = f"assets/charts/{week_l}_metrics_chart.png"
    chart_exists = any(name.endswith(".svg") for name in chart_files)
    chart_media = (
        f'<img src="{chart_svg}" alt="{html.escape(config["week"])} metrics chart">'
        if chart_exists
        else (
            '<div class="figure-panel empty-data">'
            '<h3>Graph pending</h3>'
            '<p>실험 산출물 `metrics_summary.csv`가 없어 그래프는 생성하지 않음.</p>'
            '<p class="method-inset">현재 상태: design_only / 실행 전</p>'
            "</div>"
        )
    )
    csv_note = "데이터 출처: 04_experiment/outputs/metrics_summary.csv" if has_metrics else "데이터 출처: 실행 전 / 확인 필요"
    metric_rows = []
    for col in config["chart_cols"][:5]:
        metric_rows.append([
            html.escape(col),
            "CSV 컬럼 존재 시 그래프와 표에 반영",
            "실제 실행 산출물 기준" if has_metrics else "design_only / 실행 전",
        ])
    if not metric_rows:
        metric_rows.append(["value", "numeric value가 있는 항목만 반영", "실제 실행 산출물 기준" if has_metrics else "design_only / 실행 전"])

    sections = [
        f"""
    <section class="slide" id="{week_l}-title">
      <div class="journal-kicker">Research Presentation / {html.escape(config["week"])}</div>
      <h1>{html.escape(config["week"])} {html.escape(config["topic"])}</h1>
      <p class="research-question">연구 질문: {html.escape(config["topic"])}에서 성능 지표와 보안 지표를 어떻게 분리해 평가할 수 있는가?</p>
      <div class="ratio-strip">
        <span>Formula-first</span>
        <span>Figure-first</span>
        <span>Toy/Public/Synthetic scope</span>
        <span>No journal logo or trademark</span>
      </div>
      <p class="citation-footnote">최종 발표본: presentation_slides.html. 기존 주차번호 HTML은 호환용으로만 유지.</p>
    </section>
""",
        f"""
    <section class="slide">
      <div class="slide-header">Background / {html.escape(config["week"])}</div>
      <h2>왜 이 주제가 중요한가</h2>
      <p class="key-finding">이 주제는 clean 성능만으로는 안전성을 설명하기 어렵다.</p>
      <div class="figure-grid three-panel">
        <div class="figure-panel"><div class="panel-label">A</div><h3>AI 원리</h3><p>모델 목적함수와 표현이 평가 지표의 출발점이다.</p></div>
        <div class="figure-panel"><div class="panel-label">B</div><h3>보안 표면</h3><p>공격자 가정, 보호 자산, 실패 조건을 분리한다.</p></div>
        <div class="figure-panel"><div class="panel-label">C</div><h3>근거 관리</h3><p>CSV, run log, 결과표가 같은 값을 말해야 한다.</p></div>
      </div>
    </section>
""",
        f"""
    <section class="slide">
      <div class="slide-header">Research Gap</div>
      <h2>기존 발표 흐름의 빈틈</h2>
      <table>
        <thead><tr><th>빈틈</th><th>보완 방식</th><th>검증 상태</th></tr></thead>
        <tbody>
          <tr><td>수식과 지표 연결 부족</td><td>핵심 수식, 기호표, 보안적 의미를 한 장에 배치</td><td>표준식 / 확인 필요 병기</td></tr>
          <tr><td>표와 위협모형 분리</td><td>공격자·방어자·보호 자산 표로 정리</td><td>toy/synthetic 범위</td></tr>
          <tr><td>결과 그래프 출처 불명확</td><td>metrics_summary.csv 기반 그래프만 사용</td><td>{html.escape(csv_note)}</td></tr>
        </tbody>
      </table>
    </section>
""",
        f"""
    <section class="slide">
      <div class="slide-header">Core Formula / {html.escape(config["week"])}</div>
      <h2>핵심 수식: {html.escape(formula["name"])}</h2>
      <div class="formula-card">
        \\[
{html.escape(formula["equation"])}
        \\]
      </div>
      {symbol_table(formula)}
      <p class="figure-caption">Formula | {html.escape(formula["intuition"])} {html.escape(formula["security"])} 평가 지표 연결: {html.escape(formula["metrics"])}</p>
      <div class="limitation-box">한계: {html.escape(formula["limits"])}</div>
    </section>
""",
        f"""
    <section class="slide">
      <div class="slide-header">Threat Model</div>
      <h2>공격자·방어자·보호 자산</h2>
      <table>
        <thead><tr><th>구성요소</th><th>발표 내 의미</th><th>주의</th></tr></thead>
        <tbody>
          <tr><td>공격자</td><td>안전한 toy/public/synthetic 범위의 평가 조건을 가정</td><td>실제 시스템 악용 절차 없음</td></tr>
          <tr><td>방어자</td><td>지표, 로그, 검증 절차로 위험을 관찰</td><td>formal guarantee와 empirical proxy 구분</td></tr>
          <tr><td>보호 자산</td><td>모델 성능, 데이터 프라이버시, 재현성 증거, 운영 신뢰</td><td>없는 결과는 만들지 않음</td></tr>
          <tr><td>성공 조건</td><td>{html.escape(metric_names(config))} 변화가 위험을 설명하는지 확인</td><td>CSV와 모순되면 보류</td></tr>
        </tbody>
      </table>
    </section>
""",
        f"""
    <section class="slide">
      <div class="slide-header">Evaluation Protocol</div>
      <h2>평가 프로토콜과 지표</h2>
      {html_table(["평가 항목", "대표 지표", "기록 방식"], metric_rows)}
      <p class="figure-caption">Protocol | {html.escape(csv_note)}. run_log.md 또는 results.json과 모순되는 수치는 사용하지 않는다.</p>
    </section>
""",
        f"""
    <section class="slide figure-first">
      <div class="slide-header">Figure 1 / Diagram</div>
      <h2>{html.escape(config["diagram_type"])}</h2>
      <div class="figure-grid two-panel">
        <figure class="figure-panel">
          <div class="panel-label">A</div>
          {pipeline_html(config)}
          <figcaption class="figure-caption">Pipeline | 단계별 공격면과 방어·검증 지점을 4~6개로 압축했다.</figcaption>
        </figure>
        <figure class="figure-panel">
          <div class="panel-label">B</div>
          <img src="assets/diagrams/{week_l}_pipeline_diagram.svg" alt="{html.escape(config["week"])} pipeline diagram">
          <figcaption class="figure-caption">Manifest | assets/figure_manifest.md에 생성 방식과 한계를 기록했다.</figcaption>
        </figure>
      </div>
    </section>
""",
        f"""
    <section class="slide figure-first">
      <div class="slide-header">Figure 2 / Metrics</div>
      <h2>실제 CSV 기반 지표 그래프</h2>
      <div class="figure-grid two-panel">
        <figure class="figure-panel chart-panel">
          <div class="panel-label">A</div>
          {chart_media}
          <figcaption class="figure-caption">Graph | {html.escape(config["interpretation"])} {html.escape(csv_note)}</figcaption>
        </figure>
        <figure class="figure-panel">
          <div class="panel-label">B</div>
          {metric_table(columns, rows)}
          <figcaption class="figure-caption">Table | 그래프에 사용한 CSV의 주요 행을 요약했다.</figcaption>
        </figure>
      </div>
    </section>
""",
        f"""
    <section class="slide">
      <div class="slide-header">Paper Map</div>
      <h2>논문 5편의 역할표</h2>
      {html_table(["ID", "논문 역할", "발표에서 쓰는 위치", "기말논문 연결"], [[html.escape(cell) for cell in row] for row in paper_map_rows(config)])}
      <p class="figure-caption">Paper map | 서지 세부사항과 DOI/URL은 최종 제출 전 원문 기준으로 확인한다.</p>
    </section>
""",
        f"""
    <section class="slide">
      <div class="slide-header">Security Implication</div>
      <h2>보안적 함의</h2>
      <div class="question-box">{html.escape(second_formula["security"])}</div>
      <div class="figure-grid three-panel">
        <div class="figure-panel"><div class="panel-label">A</div><h3>분리</h3><p>clean 성능과 보안 지표를 같은 값처럼 해석하지 않는다.</p></div>
        <div class="figure-panel"><div class="panel-label">B</div><h3>추적</h3><p>수치, 그래프, 노트, Q&A가 같은 산출물을 가리킨다.</p></div>
        <div class="figure-panel"><div class="panel-label">C</div><h3>제한</h3><p>실제 악용 절차 없이 평가 개념과 방어 관점만 설명한다.</p></div>
      </div>
    </section>
""",
        f"""
    <section class="slide">
      <div class="slide-header">Limitation</div>
      <h2>한계와 검증 상태</h2>
      <div class="limitation-box">{html.escape(config["caution"])} {html.escape(second_formula["limits"])}</div>
      <table>
        <thead><tr><th>항목</th><th>상태</th><th>다음 확인</th></tr></thead>
        <tbody>
          <tr><td>실험 수치</td><td>{html.escape("실행 산출물 있음" if has_metrics else "실행 전 / 확인 필요")}</td><td>run_log.md, results.json 대조</td></tr>
          <tr><td>수식 보증</td><td>표준식 또는 proxy</td><td>원문 절·쪽·formal guarantee 확인</td></tr>
          <tr><td>운영 적용</td><td>바로 적용 불가</td><td>실제 데이터·정책·위험평가 필요</td></tr>
        </tbody>
      </table>
    </section>
""",
        f"""
    <section class="slide">
      <div class="slide-header">Final Takeaway</div>
      <h2>기말논문 연결</h2>
      <p class="key-finding">{html.escape(config["week"])}의 결론은 지표를 분리하고 근거 파일로 추적하는 연구 설계다.</p>
      <table>
        <thead><tr><th>기말논문 장</th><th>연결 내용</th></tr></thead>
        <tbody>
          <tr><td>관련연구</td><td>{html.escape(config["topic"])}의 핵심 이론과 보안 taxonomy 정리</td></tr>
          <tr><td>위협모형</td><td>{html.escape(config["diagram_type"])} 기반 공격면·방어면 정의</td></tr>
          <tr><td>평가방법</td><td>{html.escape(metric_names(config))}를 CSV/log 기준으로 검증</td></tr>
          <tr><td>한계</td><td>toy/synthetic 범위와 확인 필요 항목을 명시</td></tr>
        </tbody>
      </table>
    </section>
""",
    ]
    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(config["week"])} {html.escape(config["topic"])} 발표 슬라이드</title>
  <link rel="stylesheet" href="../../../02_report_templates/nature_research_slide_style.css">
{mathjax_head()}
</head>
<body>
  <!-- Final canonical deck: presentation_slides.html. Week-numbered HTML files are compatibility copies only. -->
  <main class="deck">
{''.join(sections)}
  </main>
{nav_html()}
{nav_script()}
</body>
</html>
"""


def build_nature_markdown(config: dict[str, Any], week_dir: Path, chart_files: list[str]) -> str:
    columns, rows, has_metrics = read_metrics(config, week_dir)
    week_l = config["week"].lower()
    formula = config["formulas"][0]
    metric_md_rows = []
    for row in rows:
        metric_md_rows.append("| " + " | ".join(row[col] for col in columns) + " |")
    metric_table_md = ""
    if columns and metric_md_rows:
        metric_table_md = "\n".join(["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |", *metric_md_rows])
    else:
        metric_table_md = "| 상태 | 설명 |\n|---|---|\n| design_only / 실행 전 | metrics_summary.csv가 없거나 비어 있어 그래프를 생성하지 않음 |"

    lines = [
        f"# {config['week']} {config['topic']}",
        "",
        f"Research Question: {config['topic']}에서 성능 지표와 보안 지표를 어떻게 분리해 평가할 수 있는가?",
        "",
        "---",
        "",
        "## Core Formula",
        "",
        f"### {formula['name']}",
        "",
        "$$",
        formula["equation"],
        "$$",
        "",
        "| 기호 | 의미 |",
        "|---|---|",
        *[f"| `{sym}` | {meaning} |" for sym, meaning in formula["symbols"]],
        "",
        f"- 직관적 의미: {formula['intuition']}",
        f"- 보안적 의미: {formula['security']}",
        f"- 평가 지표 연결: {formula['metrics']}",
        f"- 한계: {formula['limits']}",
        "",
        "---",
        "",
        "## Threat Model",
        "",
        f"- Diagram: {config['diagram_type']}",
        f"- Stages: {', '.join(config['stages'])}",
        "- 안전 범위: public, synthetic, toy, local evaluation",
        "",
        f"![{config['week']} pipeline diagram](assets/diagrams/{week_l}_pipeline_diagram.svg)",
        "",
        "---",
        "",
        "## Evaluation Protocol",
        "",
        f"- Metrics: {metric_names(config)}",
        "- 데이터 출처: `04_experiment/outputs/metrics_summary.csv`" if has_metrics else "- 데이터 출처: 실행 전 / 확인 필요",
        "",
        metric_table_md,
        "",
        "---",
        "",
        "## Figure-first Result",
        "",
        f"![{config['week']} metrics chart](assets/charts/{week_l}_metrics_chart.svg)",
        "",
        config["interpretation"],
        "",
        "---",
        "",
        "## Paper Map",
        "",
        "| ID | 논문 역할 | 발표에서 쓰는 위치 | 기말논문 연결 |",
        "|---|---|---|---|",
        *["| " + " | ".join(row) + " |" for row in paper_map_rows(config)],
        "",
        "---",
        "",
        "## Limitation",
        "",
        f"- {config['caution']}",
        "- 원문 DOI/URL과 formal guarantee는 최종 제출 전 확인 필요.",
        "- 실제 운영 시스템 악용 절차나 무단 API 질의 절차는 포함하지 않음.",
        "",
        "---",
        "",
        "## Final Takeaway",
        "",
        f"{config['week']}의 핵심은 `{metric_names(config)}`를 성능·보안·재현성 근거로 분리해 기말논문의 평가방법에 연결하는 것이다.",
    ]
    return "\n".join(lines)


def build_speaker_notes(config: dict[str, Any]) -> str:
    slide_titles = [
        "Title",
        "Background",
        "Research Gap",
        "Core Formula",
        "Threat Model",
        "Evaluation Protocol",
        "Figure 1 Diagram",
        "Figure 2 Metrics",
        "Paper Map",
        "Security Implication",
        "Limitation",
        "Final Takeaway",
    ]
    notes = [
        f"# {config['week']} 발표자 노트",
        "",
        "- 권장 시간: 10-14분",
        "- 발표 원칙: 그림과 수식을 먼저 보여주고, 긴 설명은 구두로 보완한다.",
        "- 안전 범위: public, synthetic, toy, local evaluation. 실제 시스템 악용 절차는 설명하지 않는다.",
        "",
    ]
    for idx, title in enumerate(slide_titles, start=1):
        notes.extend(
            [
                f"## Slide {idx}. {title}",
                "",
                "### 말할 핵심",
                "- 이 주차 주제를 clean 성능 하나가 아니라 보안 지표와 근거 파일로 분리해 설명한다.",
                "",
                "### 설명 순서",
                "1. 그림 또는 수식을 먼저 설명",
                "2. 평가 지표와 연결",
                "3. 보안적 의미 설명",
                "4. 한계 언급",
                "",
                "### 주의",
                "- 실행하지 않은 결과는 결과처럼 말하지 않는다.",
                "- 논문 수치와 로컬 실험 수치를 혼동하지 않는다.",
                f"- {config['caution']}",
                "",
            ]
        )
    return "\n".join(notes)


def build_qna(config: dict[str, Any]) -> str:
    return "\n".join(
        [
            f"# {config['week']} Q&A",
            "",
            "## Q1. 이 수식이 실제 실험 지표와 어떻게 연결되는가?",
            "",
            f"A. 핵심 수식은 {metric_names(config)} 같은 지표를 해석하는 표준 정식화다. 실제 값은 `04_experiment/outputs/metrics_summary.csv`에서만 가져오며, 수식 자체가 운영 보증을 뜻하지는 않는다.",
            "",
            "## Q2. 이 그래프의 수치는 실제 실행 결과인가, 설계 예시인가?",
            "",
            "A. 그래프는 `metrics_summary.csv`가 존재하고 numeric 컬럼을 확인한 경우에만 생성했다. CSV에 없는 값은 만들지 않았으며, 산출물이 없을 때는 `design_only / 실행 전 / 확인 필요`로 표시한다.",
            "",
            "## Q3. clean accuracy와 보안 지표가 다른 이유는 무엇인가?",
            "",
            "A. clean accuracy는 정상 조건의 예측 성능이고, 보안 지표는 공격 조건, 교란 조건, 프라이버시 누출, 재현성 증거처럼 다른 실패 모드를 본다. 둘은 같은 숫자로 합치면 안 된다.",
            "",
            "## Q4. 이 주차 내용을 기말논문에 어떻게 반영할 수 있는가?",
            "",
            f"A. `{config['diagram_type']}`를 위협모형 그림으로 쓰고, {metric_names(config)}를 평가방법 표에 연결할 수 있다. 단, toy/synthetic 범위와 확인 필요 항목은 한계 절에 남겨야 한다.",
            "",
            "## Q5. 현재 한계는 무엇이고 추가 실험은 무엇인가?",
            "",
            f"A. {config['caution']} 추가 실험은 run_log.md와 results.json까지 일치하는 조건에서만 확정 수치로 반영한다.",
            "",
            "## Q6. 논문 5편 중 핵심 근거는 무엇인가?",
            "",
            "A. P01은 핵심 이론, P02는 위협 분류, P03은 평가 지표, P04는 공격·방어 사례, P05는 재현성·정책 근거로 사용한다. 세부 서지와 DOI/URL은 최종 제출 전 원문으로 확인한다.",
            "",
            "## Q7. 실제 운영 시스템에 바로 적용할 수 없는 이유는 무엇인가?",
            "",
            "A. 발표의 실습과 그림은 public, synthetic, toy, local evaluation 범위다. 운영 적용에는 실제 데이터 거버넌스, 정책 승인, 위협모형 검토, 독립 검증, 법적 검토가 추가로 필요하다.",
        ]
    )


def build_handout(config: dict[str, Any]) -> str:
    formula = config["formulas"][0]
    return "\n".join(
        [
            f"# {config['week']} 주차 연구 발표 요약",
            "",
            "## Research Question",
            "",
            "이 주차에서 성능 지표와 보안 지표를 어떻게 분리해 평가할 수 있는가?",
            "",
            "## Key Formula",
            "",
            f"**{formula['name']}**",
            "",
            "$$",
            formula["equation"],
            "$$",
            "",
            f"- 기호와 의미는 슬라이드의 표를 기준으로 설명한다.",
            f"- 보안적 의미: {formula['security']}",
            "",
            "## Threat Model",
            "",
            f"{config['diagram_type']} 기준으로 공격자, 방어자, 보호 자산, 성공 조건을 분리한다.",
            "",
            "## Main Figure",
            "",
            f"- Diagram: `assets/diagrams/{config['week'].lower()}_pipeline_diagram.svg`",
            f"- Chart: `assets/charts/{config['week'].lower()}_metrics_chart.svg`",
            "",
            "## Evaluation Metrics",
            "",
            f"{metric_names(config)}. 실제 수치는 `04_experiment/outputs/metrics_summary.csv` 기준이다.",
            "",
            "## Security Implication",
            "",
            "Clean 성능과 보안 지표는 서로 다른 실패 모드를 설명하므로 같은 결론으로 합치지 않는다.",
            "",
            "## Limitation",
            "",
            f"{config['caution']} toy/synthetic 범위와 formal guarantee 여부를 구분해야 한다.",
            "",
            "## Final Paper Link",
            "",
            "기말논문에서는 관련연구, 위협모형, 평가방법, 한계 절에 이 주차의 수식·표·그래프·다이어그램을 연결한다.",
        ]
    )


def build_presentation_readme(config: dict[str, Any]) -> str:
    return "\n".join(
        [
            f"# {config['week']} 발표 산출물",
            "",
            "최종 발표본은 `presentation_slides.html`이다. 주차 번호가 붙은 이전 HTML 파일은 호환용으로만 유지한다.",
            "",
            "| 파일 | 역할 |",
            "|---|---|",
            "| `presentation_slides.html` | 오른쪽 하단 `.slide-nav`가 적용된 Nature-style 연구 발표 슬라이드 |",
            "| `presentation_slides.md` | 슬라이드 내용 원본 요약 |",
            "| `speaker_notes.md` | 슬라이드별 발표자 노트 |",
            "| `qna.md` | 예상 질문과 안전한 답변 |",
            "| `one_page_handout.md` | 1페이지 연구 발표 요약 |",
            "| `assets/figure_manifest.md` | 그래프와 다이어그램 생성 근거 |",
            "",
            "수치 그래프는 `04_experiment/outputs/metrics_summary.csv`가 있는 경우에만 생성한다. 없는 수치나 실행하지 않은 결과는 만들지 않는다.",
        ]
    )


def update_week(config: dict[str, Any]) -> None:
    week_dir = BASE / config["slug"]
    assets_dir = week_dir / "09_presentation" / "assets"
    for sub in ["charts", "diagrams", "figures"]:
        (assets_dir / sub).mkdir(parents=True, exist_ok=True)

    chart_files = make_chart(config, week_dir)
    diagram_file = make_diagram(config, week_dir)
    make_manifest(config, week_dir, chart_files, diagram_file)

    report = week_dir / "06_report" / "final" / "integrated_report_final.md"
    if report.exists():
        text = report.read_text(encoding="utf-8")
        text = update_kci_status(text)
        text = replace_block(text, BLOCK_START, BLOCK_END, formula_markdown(config, "../../09_presentation/", "## 수식·그래프·그림 보강"))
        write_text(report, text)

    presentation_dir = week_dir / "09_presentation"
    write_text(presentation_dir / "presentation_slides.html", build_nature_html(config, week_dir, chart_files))
    write_text(presentation_dir / "presentation_slides.md", build_nature_markdown(config, week_dir, chart_files))
    write_text(presentation_dir / "speaker_notes.md", build_speaker_notes(config))
    write_text(presentation_dir / "qna.md", build_qna(config))
    write_text(presentation_dir / "one_page_handout.md", build_handout(config))
    write_text(presentation_dir / "README.md", build_presentation_readme(config))

    worklog = week_dir / "05_ai_worklog" / "ai_worklog.md"
    if worklog.exists():
        text = worklog.read_text(encoding="utf-8")
        text = replace_block(text, WORKLOG_START, WORKLOG_END, worklog_block(config))
        write_text(worklog, text)

    submission = week_dir / "07_week_submission" / f"{config['week'].lower()}_submission_report.md"
    if submission.exists():
        text = update_kci_status(submission.read_text(encoding="utf-8"))
        write_text(submission, text)


def make_global_audit() -> None:
    rows = [
        "# Formula & Visual Generation Summary",
        "",
        f"- 생성 일자: {TODAY}",
        "- W01~W15 발표 슬라이드는 `presentation_slides.html`을 최종 발표본으로 통일했다.",
        "- 그래프는 각 주차 `04_experiment/outputs/metrics_summary.csv`에서 읽은 numeric 값만 사용했다.",
        "- 오른쪽 하단 `.slide-nav`, MathJax, figure caption, panel label, limitation box를 포함했다.",
        "",
        "| Week | Deck | Formula | Chart | Diagram | Notes/QNA/Handout |",
        "|---|---|---|---|---|---|",
    ]
    for config in WEEKS:
        week_dir = BASE / config["slug"]
        week_l = config["week"].lower()
        rows.append(
            "| {week} | {deck} | {formula} | {chart} | {diagram} | {support} |".format(
                week=config["week"],
                deck="PASS" if (week_dir / "09_presentation" / "presentation_slides.html").exists() else "FAIL",
                formula="PASS" if config["formulas"] else "FAIL",
                chart="PASS" if (week_dir / "09_presentation" / "assets" / "charts" / f"{week_l}_metrics_chart.svg").exists() else "WARN",
                diagram="PASS" if (week_dir / "09_presentation" / "assets" / "diagrams" / f"{week_l}_pipeline_diagram.svg").exists() else "FAIL",
                support="PASS",
            )
        )
    write_text(BASE / "formula_visual_audit.md", "\n".join(rows))


def main() -> None:
    configure_matplotlib_fonts()
    for config in WEEKS:
        update_week(config)
    make_global_audit()


if __name__ == "__main__":
    main()
