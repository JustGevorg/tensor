# Tensor test task
install dependencies via poetry
```bash
cd tensor
poetry install without --linting
```
install dependencies via pip
```bash
cd tensor
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
run tests with dependencies installed via pip
```bash
cd tensor
python -m venv venv
source venv/bin/activate
pytest src/main.py
```
run tests with dependencies installed via poetry
```bash
cd tensor
poetry run pytest src/main.py
```