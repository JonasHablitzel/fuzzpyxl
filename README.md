# Fuzzpyxl
When dealing with Excelfiles inside python or pandas it is sometimes hard because not all files follow the same conventions.
This libary should help to deal with these kind of problems.
It enables you to find Excel rows, by value, formatting, color or else and go from there.

Internally it is based on [openpyxl](https://openpyxl.readthedocs.io/en/stable/).

## Documentation
To build the documentation run:
```bash
poetry run mkdocs build --strict --verbose 
```

## Developement
First install a Python interpreter and then [poetry](https://python-poetry.org/)
The following command s can be used for testing linting and other stuff
```bash
# First Setup
poetry install #install all the libaries in a venv for this project

# DEV Workflow
poetry run test # Run test suite
poetry run test_report #Run all the tests and create an coverage.xml file, wich can be inspected with the VSCode Extension coverage-gutters
poetry run black . # format all the files in this dir with black
poetry run lint # run the linter on this project
poetry run typecheck # typecheck this project(mypy)
poetry run python your_script.py # runs your script with the current venv 
poetry export -f requirements.txt --without-hashes --output requirements.txt #create requierements.txt file from the poetry lock
poetry run pytest --cov=fuzzpyxl  --cov-report=xml tests 
```
