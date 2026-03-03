VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
UVICORN = $(VENV)/bin/uvicorn

install:
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

start:
	$(UVICORN) main:app --host 0.0.0.0 --port 8801 --reload

deploy:
	docker compose up -d --build
