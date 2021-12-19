
# README - Backend API Service for Quadruplexes - Search for the G's 
A backend service interface using Swagger API with an input to add id, name & sequences, 
POST success data displays the start and end positions of the quadruplex.

Files:
```
main.py         # Runs the backend API service using fastAPI framework
test_main.py    # Executes tests using pytest framework
```

### Prerequisites - Linux Environment
```sh
sudo apt update
sudo apt-get install -y python3 python3-pip python-pytest
pip install httptools==0.1.*
pip install fastapi
pip install pytest
pip install pydantic
pip install "uvicorn[standard]"
pip3 install starlette
pip3 install uvicorn

# Might need the following dependencies & setup if installing for first time
pipenv install tox
sudo apt install pipenv update-alternatives --install /usr/bin/python python /usr/bin/python3 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
```

### Setting up backend & run service
To run this backend service, you must serve from the source folder of `/backend/`.
run:

> uvicorn main:app --reload

To view in Swagger API doc, open your browser:
> "http://127.0.0.1:8000/docs"
> "http://127.0.0.1:8000/redoc"

To test the API's, run:
> pytest

or if your virtualenv not set correctly then:
> python3 -m pytest test_main.py


*Please note:* Test cases are limited and based on few assumptions. Not all corner cases have been tested properly but given more time this can be achieved.

#### Author - [Mohamed Shez](https://github.com/shez1461)
