run:
	uvicorn app.main:app --reload

dbuild:
	docker-compose up -d --build
	sleep 5
	xdg-open http://0.0.0.0:8000/docs

ddown:
	docker-compose down

dtest:
	docker-compose exec web pytest .