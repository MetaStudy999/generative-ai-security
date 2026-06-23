# DOCX/PDF 변환 메모

## 현재 상태

- 공식 JKAIS HWP 양식 다운로드: 완료
- Markdown 논문 초안 작성: 완료
- DOCX 자동 변환: 완료
- PDF 변환본 생성: 완료

## 생성 파일

- `paper/JKAIS_paper_draft.docx`
- `paper/JKAIS_paper_draft.pdf`

## 변환 방식

시스템 패키지 설치는 `sudo` 비밀번호 요구로 진행하지 못했다. 대신 프로젝트 `.venv`에 `python-docx`와 `reportlab`를 설치하고 [paper/build_docx_pdf.py](/home/ubuntu/generative-ai-security/paper/build_docx_pdf.py)로 DOCX/PDF 초안을 생성했다.

## 수동 절차

1. `submission/journal_template/심사용논문서식-국문(2019).hwp` 또는 `submission/journal_template/최종논문서식-국문[2019].hwp`를 연다.
2. [paper/JKAIS_paper_draft.md](/home/ubuntu/generative-ai-security/paper/JKAIS_paper_draft.md)의 내용을 공식 양식에 맞게 붙여 넣는다.
3. 저자명, 소속, 학번, 교신저자 정보를 입력한다.
4. 표와 그림 제목이 JKAIS 요구대로 영문 제목인지 확인한다.
5. HWP 또는 DOCX 원본을 저장한다.
6. PDF로 내보낸 뒤 표, 그림, 참고문헌, 초록, 키워드의 줄바꿈과 깨짐을 확인한다.

## 자동 변환 명령

다음 명령으로 현재 변환본을 다시 생성할 수 있다.

```bash
paper/build_docx.sh
```

단, 자동 DOCX/PDF는 공식 JKAIS HWP 양식과 다를 수 있으므로 최종 제출본으로 사용하기 전에 반드시 공식 양식으로 수동 검수한다.
