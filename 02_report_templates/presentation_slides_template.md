# 발표용 슬라이드 템플릿

슬라이드는 8-10분 발표 기준 10-14장으로 작성한다. 한 장에는 하나의 주장만 둔다. 슬라이드 작성 후 `speaker_notes.md`, `qna.md`, `one_page_handout.md`를 같은 `09_presentation/` 폴더에 함께 작성한다.

HTML 슬라이드(`presentation_slides.html`)에는 모든 주차 공통으로 슬라이드 이동 버튼을 넣는다. 기본 구현은 이 문서 하단의 `HTML 공통 이동 버튼 스니펫` 또는 별도 파일 `02_report_templates/presentation_slide_navigation_snippet.html`을 사용한다.

공통 요구사항:

- 이전/다음 화살표 버튼과 `현재 / 전체` 카운터를 화면에 고정 표시한다.
- 방향키, PageUp/PageDown, Space, Home, End 이동을 지원한다.
- 마우스 스크롤로 이동해도 카운터가 현재 보이는 슬라이드와 동기화되어야 한다.
- 모바일 화면에서 버튼이 본문을 과도하게 가리지 않도록 하단 여백과 반응형 스타일을 둔다.

---

# WXX 주차 제목

## 발표 핵심

이번 주차의 핵심 메시지를 1-2문장으로 작성한다.

---

# 1. 왜 중요한가

- 배경 1
- 배경 2
- 핵심 질문

---

# 2. 발표 로드맵

1. AI 원리
2. 보안 이슈
3. 논문 5편의 역할
4. 위협모형과 평가방법
5. 실습/실험 또는 실행 전 상태
6. 기말논문 연결

---

# 3. AI 원리 70%

- 핵심 개념 1
- 핵심 개념 2
- 핵심 개념 3

---

# 4. 보안 이슈 30%

| 위협 | 공격자 가정 | 대표 지표 |
|---|---|---|
|  |  |  |

---

# 5. 논문 5편의 역할

| ID | 중심 역할 | 발표 활용 |
|---|---|---|
| P01 |  |  |
| P02 |  |  |
| P03 |  |  |
| P04 |  |  |
| P05 |  |  |

---

# 6. 위협모형

보호 자산, 공격자 능력, 공격 경로, 방어자 가정을 도식 또는 표로 정리한다.

---

# 7. 평가 프로토콜

| 평가 항목 | 지표 | 기록 방법 |
|---|---|---|
| Clean performance |  |  |
| Attack impact |  |  |
| Robustness/Leakage |  |  |
| Reproducibility | seed, config, outputs |  |

---

# 8. 실습/실험

실행 전이면 `실행 전`으로 표시한다. 실행 완료 시 `04_experiment/outputs/run_log.md`, `metrics_summary.csv`, `results.json`과 일치하는 값만 쓴다.

---

# 9. 결과와 해석

| 조건 | 주요 지표 | 결과 | 해석 |
|---|---|---|---|
| Clean baseline |  | 실행 전 |  |
| Security scenario |  | 실행 전 |  |
| Defense/check |  | 실행 전 |  |

---

# 10. 한계

- toy/synthetic 평가의 한계
- DOI/URL 또는 원문 검증 상태
- 실제 시스템 일반화 주의

---

# 11. 기말논문 연결

| 기말논문 장 | 연결 내용 |
|---|---|
| 관련연구 |  |
| 위협모형 |  |
| 평가방법 |  |
| 분석/실험 |  |

---

# 12. 결론

- Takeaway 1
- Takeaway 2
- Takeaway 3

---

# HTML 공통 이동 버튼 스니펫

`presentation_slides.html`을 만들 때 아래 스타일, HTML, 스크립트를 함께 넣는다. 슬라이드가 `<section>` 요소로 구성되어 있다는 전제다.

```html
<nav class="slide-nav" aria-label="슬라이드 이동">
  <button id="prevSlide" type="button" title="이전 슬라이드" aria-label="이전 슬라이드">‹</button>
  <span id="slideCounter" class="slide-counter" aria-live="polite">1 / 1</span>
  <button id="nextSlide" type="button" title="다음 슬라이드" aria-label="다음 슬라이드">›</button>
</nav>
```

공통 CSS:

```css
html {
  scroll-behavior: smooth;
  scroll-snap-type: y mandatory;
}
section {
  scroll-snap-align: start;
}
.slide-nav {
  position: fixed;
  right: 24px;
  bottom: 24px;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid #d1d5db;
  border-radius: 999px;
  box-shadow: 0 10px 30px rgba(17, 24, 39, 0.16);
  z-index: 20;
  backdrop-filter: blur(8px);
}
.slide-nav button {
  width: 44px;
  height: 44px;
  border: 1px solid #9ca3af;
  border-radius: 50%;
  background: #111827;
  color: white;
  font-size: 26px;
  line-height: 1;
  cursor: pointer;
}
.slide-nav button:disabled {
  cursor: not-allowed;
  opacity: 0.35;
}
.slide-counter {
  min-width: 62px;
  text-align: center;
  font-size: 16px;
  font-weight: 700;
  color: #111827;
}
@media (max-width: 720px) {
  section { padding-bottom: 14vh; }
  .slide-nav { right: 12px; bottom: 12px; }
}
@media print {
  .slide-nav { display: none; }
}
```

공통 JavaScript:

```html
<script>
  const slides = Array.from(document.querySelectorAll("section"));
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
```
