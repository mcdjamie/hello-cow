# Introduction
This is a simple example project to convert to using `poetry` for dependency management.


# Requirements
The project requires two top-level packages:
- `cowsay`
- `black` (dev only)

# How to run
- Run the code: `python main.py`
- Format the code: `make format`

# Task
Your task is to convert this project to use `poetry` (https://python-poetry.org/)

## Acceptance criteria:
- install `poetry` locally
- remove `requirements.txt`
- generate files `project.toml` and `poetry.lock` via poetry
- `black` should be split out as a development dependency
- run the two commands above using `poetry`