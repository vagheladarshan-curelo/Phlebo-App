# Phlebo-App Backend Setup

This backend is built with FastAPI, PostgreSQL + PostGIS, and Celery + Redis.

## Prerequisites

-   Docker and Docker Compose (recommended)
-   Python 3.11+ (if running locally)
-   PostgreSQL with PostGIS extension
-   Redis

## Getting Started with Docker (Recommended)

1.  Build and start the services:
    ```bash
    docker compose up --build
    ```

2.  Access the API documentation at `http://localhost:8000/docs`.

## Local Development Setup

1.  Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  Install dependencies:
    ```bash
    pip install -r Backend/requirements.txt
    ```

3.  Set up environment variables in `Backend/.env`.

4.  Run the API:
    ```bash
    uvicorn app.main:app --reload
    ```

5.  Run the Celery worker:
    ```bash
    celery -A app.core.celery_app worker --loglevel=info
    ```

## PostGIS Features

The backend includes a `Location` model that uses PostGIS for geographical data.
See `app/models/location.py` for implementation details.

## Background Tasks

Sample tasks are defined in `app/tasks.py`. You can trigger them via the API endpoints.
