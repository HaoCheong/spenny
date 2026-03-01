SHELL := /bin/bash
.ONESHELL:

LOCAL_PATH := /home/hcheong/projects/spenny/env

demo:
	@set -a
	@source env/demo.env
	@set +a

	@docker compose --progress=plain build --no-cache
	@docker compose --env-file env/demo.env \
		-f docker-compose.yml \
		--profile demo \
		up --force-recreate --remove-orphans --renew-anon-volumes -d

	@echo "==================== ACCESS POINTS ($$PROJECT_NAME) ===================="
	@echo "BACKEND URL -> $$BACKEND_CONTAINER_URL"
	@echo "FRONTEND URL -> $$FRONTEND_CONTAINER_URL"

live:
	@set -a && source env/live.env && set +a
	@docker compose build --no-cache
	@docker compose --env-file $(LOCAL_PATH)/live.env -f docker-compose.yml --profile live up --force-recreate --remove-orphans --renew-anon-volumes -d
	@docker compose --env-file `$(LOCAL_PATH)/live.env` up --force-recreate --remove-orphans -d

	@echo "==================== ACCESS POINTS (${PROJECT_NAME}) ===================="
	@echo "BACKEND URL -> $BACKEND_CONTAINER_URL"
	@echo "DB Access -> PGPASSWORD=${SPENNY_DB_PASS} PAGER='less -S' psql -h ${SPENNY_DB_HOST} -p ${SPENNY_DB_PORT} -d ${SPENNY_DB_NAME} -U ${SPENNY_DB_USER}"
	@echo "================================== END =================================="

unit:
	@set -a && source env/demo.env && set +a
	@docker compose build --no-cache
	@docker compose --env-file $(LOCAL_PATH)/test.env -f docker-compose.yml --profile test up --force-recreate --remove-orphans --renew-anon-volumes -d
	@sleep 2
	@cd backend
	@python3 -m pytest $(LOCAL_PATH)/backend/tests/unit/bucket_tests.py
	@python3 -m pytest $(LOCAL_PATH)/backend/tests/unit/event_tests.py
	@python3 -m pytest $(LOCAL_PATH)/backend/tests/unit/log_tests.py

stop:
	@docker compose --env-file $(LOCAL_PATH)/demo.env stop 
	@docker compose --env-file $(LOCAL_PATH)/demo.env down --volumes --remove-orphans
	@docker compose --env-file $(LOCAL_PATH)/live.env stop 
	@docker compose --env-file $(LOCAL_PATH)/live.env down --volumes --remove-orphans
	@docker compose --env-file $(LOCAL_PATH)/test.env stop 
	@docker compose --env-file $(LOCAL_PATH)/test.env down --volumes --remove-orphans