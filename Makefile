BOT_DIR = "bot"
API_DIR = "api"
TESTS_DIR = "tests"

.PHONY: format
format:
	ruff format $(BOT_DIR) $(API_DIR)

.PHONY: run-bot
run-bot:
	python -m $(BOT_DIR)

.PHONY: run-api
run-api:
	uvicorn $(API_DIR):app --reload

.PHONY: up
up:
	docker-compose up -d --build
	
.PHONY: freeze
freeze:
	pip freeze > requirements.txt

.PHONY: test
test:
	pytest $(TESTS_DIR) -s -v
