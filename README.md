# Demo

[![Part 1](https://img.youtube.com/vi/K_KQ3GUvKiE/0.jpg)](https://youtu.be/51g3W9bLeeg)

# README - How to run both services - Backend & Frontend

Folders:
```
backend/     # Backend server uses FastAPI
frontend/    # Frontend server uses live-server
```

### Initial set up & Environment
OS - Ubuntu 20.04 LTS
Editor - Visual Studio Code

View & read both readme files in their appropriate folders.
Install all the dependencies required for each component.
To run both services, you must serve the following in order:

1. In the root folder of `/backend/`.
Run:
> uvicorn main:app --reload

To view the Backend Swagger API UI, open your browser:
Note: Port [:8000]
> "http://localhost:8000/docs"


2. In the root folder of `/frontend/`.
Run:
> npx live-server

To view the Frontend UI, open your browser:
Note: Port [:8080]
> "http://localhost:8080/"


3. [Optional] - To run python backend API tests
Run:
> pytest -v

#### Author - [Mohamed Shez](https://github.com/shez1461)
