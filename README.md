## Requirements

```
Python 3
```

### Create Virtual Env

```
cd kunder-workshop-bk-python
python3 -m venv ./.virtualenvs/kunder-workshop-bk-python
```

## Install

```
pip3 install -r requirement.txt
```

## Run

```
cd kunder-workshop-bk-python
source .virtualenvs/kunder-workshop-bk-python/bin/activate

export FLASK_APP=app.py
export FLASK_ENV=development
flask run

```