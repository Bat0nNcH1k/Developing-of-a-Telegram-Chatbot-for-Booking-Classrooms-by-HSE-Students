PROJECT_DIR = "hse_nn_bot"

.PHONY: format
format:
	ruff format $(PROJECT_DIR)


.PHONY: run
run:
	python -m $(PROJECT_DIR)


.PHONY: run-prod
run-prod:
	docker-compose up -d --build
	
	
.PHONY: freeze
freeze:
	pip freeze > requirements.txt