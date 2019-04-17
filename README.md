# **Store Rest Api - Pony refactored version**

Refactoring of a Python Flask [tutorial](https://www.udemy.com/rest-api-flask-and-python/) using Pony Orm.
See SQLAlchemy version [here](https://github.com/imessias/store-rest-api).

## Requirements
- Python3, install [here](https://www.python.org/downloads/)
- Virtual environments

## Setup
Install requirements
```
virtualenv --python=python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Install using windows cmd
```
virtualenv --python=python3 .venv
".venv/Scripts/activate"
pip install -r requirements.txt
```

## Run
Make sure you are in the virtual environment and run
```
python app.py
```

### Database
Database is sqlite and will be stored in the db file.

## Change log

- **Til 05/04/2019** - Refactored project into api-model-service Model. Implemented the REST Api's. 
- **08/04/2019** - Implemented the Pony database entities. Implemented the Store Service classes. 
- **12/04/2019** - Implemented StoreService unit tests.
