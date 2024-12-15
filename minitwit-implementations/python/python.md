Most essential requirements with regards to versions:

- Python == 3.12
- Python Package: Django  == 4.1.7
- Python Package: psycopg2


# Python
The Python is not compiled, instead the source code is cloned onto the server.

Note, that in order to run Python on Ubuntu, there are some install dependencies, that can be resolved by running the following code:

```bash
apt update
apt upgrade -y

apt install build-essential -y
apt install libsqlite3-dev -y
apt install software-properties-common -y
apt install libpq-dev -y

pip install -r src/requirements.txt
```

## How to Build the Executable
N/A

## How to Transfer the Executable to the Server
Clone this repository: [https://github.com/3-1-research-project/FiveGuys](https://github.com/3-1-research-project/FiveGuys)

## How to Run the Executable
The Python project can be executed using the following commands

```bash
python3 ./manage.py migrate --run-syncdb
python3 ./manage.py collectstatic -n
python3 ./manage.py runserver 0.0.0.0:5000
```

If everything is setup correctly, you can access the MiniTwit application by navigating to the following URL on the controller computer: `http://<server ip>:5000`
