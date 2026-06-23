#!/usr/bin/env bash
set -euo pipefail

if [[ -x ".venv/bin/python" ]]; then
  .venv/bin/python paper/build_docx_pdf.py
else
  python3 paper/build_docx_pdf.py
fi
