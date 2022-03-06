install:
	sudo apt-get install docker
	sudo apt-get install python3
	pip install docker-compose

buildAndRun:
	chmod +x ./run_compose
	./run_compose up --build

test:
	./run_compose up
	./run_compose.sh run --rm django pytest

	