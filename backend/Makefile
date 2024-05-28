run_test:
	@uvicorn api.main:app --reload --env-file .env.test

run_dev:
	@uvicorn api.main:app --reload --env-file .env.dev

run_prod:
	@uvicorn api.main:app --env-file .env.prod


revision_test:
	ENV=testing alembic revision --autogenerate -m "$(message)"

revision_dev:
	ENV=development alembic revision --autogenerate -m "$(message)"

revision_prod:
	ENV=production alembic revision --autogenerate -m "$(message)"


upgrade_head_test:
	ENV=testing alembic upgrade head

upgrade_head_dev:
	ENV=development alembic upgrade head

upgrade_head_prod:
	ENV=production alembic upgrade head
	

updatabase_test:
	docker-compose --env-file .env.test up -d book_trade_test

updatabase_dev:
	docker-compose --env-file .env.dev up -d book_trade_dev

updatabase_prod:
	docker-compose --env-file .env.prod up -d book_trade_prod

py_test:
	PYTHONPATH=./ pytest -svv api/tests
