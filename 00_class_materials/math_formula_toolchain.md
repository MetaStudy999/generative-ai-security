# 수식 작성 및 검증 권장 도구

이 문서는 주차별 보고서와 기말 모의투고 논문에서 수식, 알고리즘, 평가 지표를 작성할 때 사용할 권장 도구와 라이브러리를 정리한다.

## 1. 기본 원칙

수식의 기본 작성 형식은 Markdown 안의 LaTeX 문법으로 통일한다.

| 용도 | 권장 표기 |
|---|---|
| 문장 안 수식 | `$ASR = N_{success}/N_{trials}$` |
| 독립 수식 | `$$ASR = \frac{N_{success}}{N_{trials}}$$` |
| HTML/MathJax 호환 inline | `\(ASR = N_{success}/N_{trials}\)` |
| HTML/MathJax 호환 display | `\[ASR = \frac{N_{success}}{N_{trials}}\]` |

수식을 넣을 때는 수식 자체보다 기호 정의, 직관적 의미, 보안 해석, 평가 지표 연결이 더 중요하다. 원문 확인이 부족하면 `확인 필요`로 표시하고 임의로 만들지 않는다.

## 2. 문서 작성·렌더링 도구

| 도구 | 권장 용도 | 비고 |
|---|---|---|
| Markdown + LaTeX math | 주차별 보고서, 기말논문 초안의 기본 작성 형식 | 저장소 기본 문서 형식과 가장 잘 맞음 |
| Pandoc | Markdown을 HTML, DOCX, PDF로 변환 | `--mathjax`, `--katex` 옵션으로 HTML 수식 렌더링 가능 |
| KaTeX | 발표용 HTML, 웹 문서의 빠른 수식 렌더링 | 빠르고 가벼움. 지원 함수 목록 확인 필요 |
| MathJax | 복잡한 수식 또는 호환성이 중요한 HTML 문서 | LaTeX, MathML, AsciiMath 입력 지원 |
| LaTeX / TeX Live | 최종 PDF 품질이 중요한 논문 작성 | `amsmath`, `amssymb`, `mathtools`, `kotex` 활용 |
| Typst | LaTeX보다 간결한 별도 PDF 작성 흐름이 필요할 때 | 선택 도구. 현재 저장소 기본 형식은 Markdown |

## 3. Python 검산·그림 도구

| 라이브러리 | 권장 용도 | 현재 루트 환경 반영 |
|---|---|---|
| sympy | 수식 전개, 단순화, 미분, LaTeX 출력, 기호 검산 | 선택 설치 권장 |
| numpy | 지표 계산, 배열·행렬 계산 | 반영됨 |
| scipy | 최적화, 통계, 수치해석 | 선택 설치 권장 |
| matplotlib | 그래프와 그림 안의 수식 표기 | 반영됨 |
| pandas | 지표표, 비교표, CSV 결과 정리 | 반영됨 |
| jupyterlab | 수식 설명, 계산, 표·그림 검토를 한 화면에서 수행 | 선택 설치 권장 |

선택 라이브러리는 실제 실험에서 필요할 때만 주차별 `04_experiment/pyproject.toml` 또는 루트 `pyproject.toml`에 추가한다. 의존성을 추가한 경우 lock 파일과 실행 로그를 함께 갱신한다.

## 4. 설치 판단 기준

현재 저장소에서는 수식 관련 라이브러리를 모두 즉시 설치하지 않는다. 기본 보고서 작성은 Markdown + LaTeX math로 충분하며, 루트 공통 환경에는 이미 `numpy`, `pandas`, `matplotlib`이 포함되어 있다.

| 상황 | 설치 판단 | 이유 |
|---|---|---|
| LaTeX 수식을 문서에 쓰기만 함 | 추가 설치 없음 | Markdown 문법으로 작성 가능 |
| ASR, leakage, utility 등 단순 지표 계산 | 추가 설치 없음 | `numpy`, `pandas`로 충분 |
| 그래프 축·범례에 수식 표기 | 추가 설치 없음 | `matplotlib` 포함 |
| 수식 전개, 미분, 단순화, LaTeX 출력 검산 필요 | `sympy` 선택 추가 | 기호 검산이 필요한 경우 |
| 최적화, 통계검정, 분포 계산 필요 | `scipy` 선택 추가 | 수치해석·통계 기능이 필요한 경우 |
| 노트북 기반 분석·수식 검토 필요 | `jupyterlab` 선택 추가 | 대화형 검토가 필요한 경우 |
| Markdown을 DOCX/PDF로 자동 변환 | Pandoc 별도 설치 | Python 패키지가 아닌 문서 변환 도구 |
| 수식이 많은 최종 PDF 작성 | TeX Live 별도 설치 | Python 패키지가 아닌 TeX 배포판 |

권장 순서는 다음과 같다.

1. 처음에는 추가 설치 없이 Markdown + LaTeX math로 작성한다.
2. 수식 검산이 실제로 필요해지면 `sympy`만 먼저 추가한다.
3. 수치해석이나 통계가 필요해지면 `scipy`를 추가한다.
4. 노트북 기반 검토가 필요할 때만 `jupyterlab`을 추가한다.
5. DOCX/PDF 자동 변환 단계에서 Pandoc 또는 TeX Live를 별도 설치한다.

의존성을 추가할 때는 예를 들어 다음 흐름을 사용한다.

```bash
uv add sympy
uv lock
```

주차별 실험 폴더에서만 필요한 경우에는 해당 주차의 `04_experiment/pyproject.toml`에 추가한다. 루트 공통 환경에 추가하는 경우에는 `pyproject.toml`, `uv.lock`, 실행 로그 또는 AI 활용기록에 추가 사유를 함께 남긴다.

## 5. LaTeX 패키지 추천

| 패키지 | 용도 |
|---|---|
| amsmath | 정렬식, 다줄 수식, equation/align 환경 |
| amssymb | 수학 기호 확장 |
| mathtools | amsmath 보완 |
| bm | bold math symbol |
| algorithm2e | 알고리즘 의사코드 작성 |
| algorithmicx | 알고리즘 의사코드 작성 |
| siunitx | 단위와 수치 표기 |
| kotex | 한글 LaTeX 문서 작성 |

## 6. 권장 작업 흐름

1. Markdown에 LaTeX 문법으로 수식을 작성한다.
2. 수식 아래에 기호 정의 표를 둔다.
3. 직관적 설명과 보안 관점 해석을 2-4문장으로 작성한다.
4. 평가 지표와 연결되는 경우 `ASR`, `Robust Accuracy`, `Privacy Leakage`, `Utility`, `Cost` 등과 연결한다.
5. 필요한 경우 `sympy`로 수식 변형이나 계산값을 검산한다.
6. HTML 발표자료는 KaTeX 또는 MathJax로 렌더링한다.
7. DOCX/PDF 제출본은 Pandoc 또는 선택 학회지 양식에서 수식이 깨지지 않는지 확인한다.

## 7. 예시

```markdown
공격 성공률은 다음과 같이 정의한다.

$$
ASR = \frac{N_{success}}{N_{trials}}
$$

| 기호 | 의미 |
|---|---|
| `N_{success}` | 사전에 정의한 실패 조건에 도달한 모의 평가 사례 수 |
| `N_{trials}` | 전체 모의 평가 사례 수 |

이 지표는 공격 절차를 상세히 재현하기 위한 것이 아니라, 안전한 synthetic/toy 평가에서 위험 입력이 정책 우회나 민감정보 노출 같은 실패 조건에 얼마나 자주 도달하는지 기록하기 위한 지표다.
```

## 8. AI 활용 기록

AI 도구로 수식 설명, LaTeX 변환, 기호 정의 초안을 작성한 경우 AI 활용 기록에 다음을 남긴다.

| 항목 | 기록 내용 |
|---|---|
| 사용 목적 | 수식 설명 / LaTeX 변환 / 기호 정의 / 검산 보조 |
| 반영 위치 | 보고서 절 번호 또는 파일명 |
| 검증 방식 | 원문 논문, 교재, 공식 문서, 실행 로그, `sympy` 계산 대조 |
| 주의사항 | AI가 만든 수식, DOI, 정량값은 검증 전까지 확정값으로 쓰지 않음 |
