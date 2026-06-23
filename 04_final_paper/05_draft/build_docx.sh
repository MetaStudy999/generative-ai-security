#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

if [[ -x "${ROOT}/.venv/bin/python" ]]; then
  "${ROOT}/.venv/bin/python" "${SCRIPT_DIR}/build_docx_pdf.py"
else
  python3 "${SCRIPT_DIR}/build_docx_pdf.py"
fi
