# Infra Backend

## Prerequisites
- Virtual Environment (Linux):
```sh
    python3 -m venv .venv
    source .venv/bin/activate
```

## Running the Project
> Run these commands based on the microservice.

- Install FastAPI and Uvicorn:
```sh
    pip install fastapi uvicorn
```

- On the terminal, run:
```sh
    cd infra/backend/inventory # Edit depending on the microservice
    uvicorn app.main:app --reload --port 8001
```