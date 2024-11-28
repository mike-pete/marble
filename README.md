# Notes

create venv
`python3.13 -m venv .venv`

use venv:
`source ./.venv/bin/activate`

check what env you're using:
`echo $VIRTUAL_ENV`

escape venv:
`deactivate`

you might want to update VSCode with the following settings:
```json
"mypy.runUsingActiveInterpreter": true,
```

install requirements
`pip install -r requirements.txt`

Select the Active Interpreter

- Make sure you select the appropriate Python interpreter in VS Code:
- Open Command Palette (Ctrl+Shift+P).
- Search for Python: Select Interpreter.
- Choose the environment where mypy is installed.

run mypy:
`mypy main.py --strict`

`pip freeze > requirements.txt`



`ruff check`

`ruff format`