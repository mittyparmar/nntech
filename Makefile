# Makefile

.PHONY: run

run:
    pip install -r requirements.txt
    flask db upgrade
    python run.py
