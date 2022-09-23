install:
	poetry install # Эта команда полезна при первом клонировании репозитория (или после удаления зависимостей).

brain-games:
	poetry run brain-games
build:
	poetry build # собрать пакет и убедиться, что вы его правильно настроили.

package-install:
	python3 -m pip install --user dist/*.whl

publish:
	poetry publish --dry-run
