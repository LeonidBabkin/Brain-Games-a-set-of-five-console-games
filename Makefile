install:
	poetry install  # Эта команда полезна при первом клонировании репозитория (или после удаления зависимостей).
brain-games:
	poetry run brain-games
build:
	poetry build  # собрать пакет и убедиться, что вы его правильно настроили.
package-install:
	python3 -m pip install --user dist/*.whl
publish:
	poetry publish --dry-run
lint:
	poetry run flake8 brain_games
reinstall-package:
	pip install --user --force-reinstall dist/*.whl

brain-calc:
	poetry run brain-calc
brain-even:
	poetry run brain-even
brain-gcd:
	poetry run brain-gcd

.PHONY: install brain-games build package-install publish lint reinstall-package brain-calc brain-even brain-gcd
