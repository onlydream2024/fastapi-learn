#!/bin/bash

build() {
    pip install -r requirements.txt
}

dev() {
    export ENVIRONMENT=DEV
    uvicorn app.main:app --host 0.0.0.0 --port 3000 --reload
}

stage() {
    export ENVIRONMENT=STAGE
    uvicorn app.main:app --host 0.0.0.0 --port 3000 --workers 2
}

prod() {
    export ENVIRONMENT=PROD
    uvicorn app.main:app --host 0.0.0.0 --port 3000 --workers 4
}

$1