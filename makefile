SHELL := /bin/bash
.ONESHELL:
LOCAL_PATH := /home/hcheong/projects/spenny/env
.PHONY: demo staging
.SHELLFLAGS := -ec   # -e so a failed build aborts instead of ploughing on

demo:
	@set -a && . env/demo.env && set +a
	docker compose --progress=plain build
	docker compose --env-file env/demo.env -f docker-compose.yml --profile demo down --volumes --remove-orphans
	docker compose --env-file env/demo.env -f docker-compose.yml --profile demo \
		up --force-recreate --remove-orphans --renew-anon-volumes -d
	echo "==================== DEMO ACCESS POINTS ($$PROJECT_NAME) ===================="
	echo "BACKEND URL  -> $$BACKEND_URL"
	echo "FRONTEND URL -> $$FRONTEND_CONTAINER_URL"
	echo "================================== END =================================="

staging:
	@set -a && . env/staging.env && set +a
	docker compose build
	docker compose --env-file env/staging.env -f docker-compose.yml --profile staging down --volumes --remove-orphans
	docker compose --env-file env/staging.env -f docker-compose.yml --profile staging \
		up --remove-orphans --renew-anon-volumes -d
	echo "==================== STAGING ACCESS POINTS ($$PROJECT_NAME) ===================="
	echo "BACKEND URL -> $$BACKEND_URL"
	echo "FRONTEND URL -> $$FRONTEND_CONTAINER_URL"
	echo "DB Access -> PGPASSWORD=$$SPENNY_DB_PASS PAGER='less -S' psql -h $$SPENNY_DB_HOST -p $$SPENNY_DB_PORT -d $$SPENNY_DB_NAME -U $$SPENNY_DB_USER"
	echo "================================== END =================================="

stop:
	@for e in demo staging test; do
		docker compose --env-file env/$$e.env -f docker-compose.yml --profile $$e down --volumes --remove-orphans
	done

clean: 
	@for e in demo staging test; do
		docker compose --env-file env/$$e.env down --rmi local --volumes --remove-orphans
	done