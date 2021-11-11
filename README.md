# Airflow POC

Experimenting with airflow by setting up test DAGs with some python scripts.

## Setup

Create a virtual Python environment with `venv`

```sh
python -m venv name-of-env
```

and activate it.

```sh
source name-of-env/bin/activate
```

Install the dependencies

```sh
pip install -r requirements.txt
```

Run the setup script for Airflow `setup-airflow.sh` which will:

- Download and install Airflow 2.2.1
- Initialise a SQLite database
- Create a user
- Start a local Airflow server on http://localhost:8080

Proceed to the local instance of Airflow on the browser and log in with the provided user details on the terminal output of the set up script.
