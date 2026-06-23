.PHONY: build run compose verify check refs submission ai weekly-audit weekly-status run-final-audit

PYTHON ?= python3

build:
	docker build -t aisec-uv-cuda132 .

run:
	docker run --rm -it --gpus all -v "$$PWD":/workspace aisec-uv-cuda132

compose:
	docker compose run --rm aisec

verify:
	docker run --rm -it --gpus all -v "$$PWD":/workspace aisec-uv-cuda132 python scripts/verify_gpu.py

check: refs ai submission
	@echo "All checks completed."

refs:
	$(PYTHON) scripts/check_references.py

submission:
	$(PYTHON) scripts/check_submission.py

ai:
	$(PYTHON) scripts/check_ai_disclosure.py

weekly-audit:
	$(PYTHON) scripts/weekly_audit.py

weekly-status: weekly-audit
	@echo "Weekly status updated: 03_weekly_reports/WEEKLY_STATUS.md"

run-final-audit:
	$(PYTHON) 04_final_paper/04_methodology_experiment/src/run_analysis.py
