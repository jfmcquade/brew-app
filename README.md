## Running the App

- From the root of the repo, run 
        
        python -m app.py

## Virtual Environment
- To create a venv when first pulling this/a python project run `python -m venv .venv` from the root of the repo
  - Your python command may be different eg. py, python3
- To activate a venv run:
  - Windows (in GitBash): `source .venv/Scripts/activate`
  - OSX/Linux: `source .venv/bin/activate`
- To deactivate the venv run `deactivate` in the shell when the venv is active


## Requirements
- Installing requirements
  - After creating/activating the venv run `pip install -r requirements.txt` from the root of the repo
    - Your pip command may be different eg. `pip3`
- Updating requirements
  - The venv should be active. Run `pip freeze > requirements.txt` from the root of your project

## MySQL Database
- Start in background: `docker-compose up -d` to run in the background
- Start in active shell `docker-compose up` to run in the active shell
- Stop: `docker-compose stop`
