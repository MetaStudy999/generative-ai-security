# 02_report_templates

이 폴더는 AI 보안 주차별 보고서 작성을 위한 공통 템플릿을 보관한다.

## 템플릿 종류

- 주차별 통합보고서
- 논문요약
- 논문비교표
- 이론정리
- 실습보고서
- 발표용 보고서
- 발표용 슬라이드
- 발표자 대본
- 발표 예상 Q&A
- 1페이지 발표 요약
- 제출용 보고서
- AI 활용기록
- 기말논문 연결표
- 제출 전 체크리스트

## 작성 원칙

- 파일명은 영문, 숫자, 언더바를 사용한다.
- Markdown 본문은 한글로 작성한다.
- 논문 제목, DOI, 저자명은 임의 생성하지 않는다.
- 확인하지 못한 정보는 `확인 필요`로 표시한다.
- 본문 인용과 참고문헌 목록은 서로 대응시킨다.
- 미검증 문헌은 핵심 근거로 사용하지 않는다.
- 실험 결과는 실제 실행 로그가 있을 때만 확정한다.
- 실행 완료 시 `04_experiment/outputs/metrics_summary.csv`, `results.json`, `run_log.md`를 보존하고 관련 보고서와 제출 체크리스트를 함께 갱신한다.
- 실험 실행 명령어, 실행일, seed, Python/package 버전, 주요 config 상태를 기록한다.
- `config.yaml`의 `design_only` 또는 `executed` 상태는 실제 `outputs/` 산출물 존재 여부와 일치시킨다.
- 실제 개인정보, 운영 서비스, 무단 API 질의, 실행 가능한 공격 절차는 실습 범위에서 제외한다.
- 발표자료는 `09_presentation/`에 두고, `presentation_report.md`에는 핵심 주장, 발표 흐름, 실험 근거, 예상 질문을 함께 정리한다.
- 발표 기본 패키지는 `presentation_report.md`, `presentation_report.html`, `presentation_slides.md`, `presentation_slides.html`, `speaker_notes.md`, `qna.md`, `one_page_handout.md`로 구성한다.
- 발표용 슬라이드는 `presentation_slides.md`와 `presentation_slides.html`을 함께 생성한다.
- `presentation_slides.html`에는 공통으로 슬라이드 이동 버튼을 넣는다. 기본 구현은 `presentation_slides_template.md`의 HTML 공통 이동 버튼 스니펫 또는 `presentation_slide_navigation_snippet.html`을 사용한다.
- 슬라이드 이동은 이전/다음 화살표, 현재/전체 카운터, 방향키/PageUp/PageDown/Space/Home/End 키보드 이동을 모두 지원해야 한다.
- 제출용 보고서는 `07_week_submission/`에 Markdown과 HTML을 함께 두며, HTML은 Markdown 제출본과 같은 수치·상태를 유지한다.
- AI 도구를 사용한 경우 사용 도구, 사용 목적, 주요 프롬프트, 반영 위치, 사람 검토와 검증 방식을 `05_ai_worklog/`에 기록한다.
- AI 산출물은 초안으로만 사용하며 최종 내용, 인용, 실험결과, 연구윤리 책임은 작성자에게 있다.
- 기말논문 연결자료에는 주차별 보고서 최소 2개 이상을 어떻게 반영할 수 있는지 추적 가능하게 기록한다.
