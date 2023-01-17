install-poetry:
	curl -sSL https://install.python-poetry.org | python3 -
	echo 'export PATH="$$HOME/.poetry/bin:$$PATH"' >> ~/.bashrc
	source ~/.bashrc

create-env:
	poetry env use python3

install: install-poetry create-env
	poetry install

run:
	poetry run python3 main.py

test:
	export PYTHONPATH=$(PYTHONPATH):$(CURDIR)/src
	poetry run pytest

clean:
	poetry env remove -v

.PHONY: install run test install-poetry create-env clean
