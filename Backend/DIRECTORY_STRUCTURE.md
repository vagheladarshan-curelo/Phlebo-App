# Backend Directory Structure Analysis

This document provides a comprehensive overview of the `Backend` directory, detailing the purpose of each directory and file within the project.

## Directory Overview

- `app/`: Contains the core application logic, including API routes, database models, CRUD operations, and utility functions.
- `migrations/`: Houses Alembic migration scripts used for managing database schema changes.
- `tests/`: Contains unit and integration tests to ensure code quality and functionality.
- `venv/`: (Not documented) Python virtual environment for managing project dependencies.

---

## Root Files

| File | Meaning |
| :--- | :--- |
| `.env` | Stores environment variables like database URLs, secret keys, and configuration settings. |
| `.gitignore` | Specifies files and directories that Git should ignore (e.g., `venv/`, `__pycache__`, `.env`). |
| `Dockerfile` | Defines the instructions to build a Docker image for the backend application. |
| `README.md` | Provides basic information about the backend project, installation, and usage. |
| `alembic.ini` | Configuration file for Alembic, used for managing database migrations. |
| `requirements.txt` | Lists all Python dependencies required to run the backend application. |

---

## `app/` Directory

The heart of the FastAPI application.

### `app/api/` (API Layer)
- `api.py`: The main router that includes all versioned API routers (e.g., `v1`).
- `deps.py`: Contains dependency injection functions, such as getting a database session.
- `v1/`: Version 1 of the API.
    - `api.py`: Combines all endpoint routers for version 1.
    - `endpoints/`: (Currently empty) Intended to house individual API route modules.

### `app/core/` (Core Configuration & Utilities)
- `celery_app.py`: Configures the Celery worker for handling background tasks using Redis.
- `config.py`: Uses Pydantic to manage application settings and environment variables.
- `database.py`: Handles SQLAlchemy engine creation, session management, and the base model class.
- `logging.py`: Configures application-wide logging.
- `security.py`: Provides utilities for password hashing and JWT token creation/verification.

### `app/crud/` (CRUD Operations)
- `base.py`: A generic base class for common CRUD operations (Create, Read, Update, Delete).
- `location.py`: Implements specific CRUD logic for the `Location` model.

### `app/models/` (Database Models)
- `location.py`: Defines the SQLAlchemy model for the `Location` table, including spatial data support via GeoAlchemy2.

### `app/schemas/` (Data Validation & Serialization)
- `base.py`: Contains base Pydantic models used across the application.
- `location.py`: Defines Pydantic schemas for `Location` data validation during creation, update, and retrieval.
- `msg.py`: Simple schema for returning basic messages.

### `app/main.py`
The entry point of the FastAPI application. It initializes the app, adds middleware (like CORS), and includes the API routers.

### `app/tasks.py`
Defines background tasks to be executed by the Celery worker.

---

## `migrations/` Directory (Alembic)

- `env.py`: Configuration script for the Alembic environment.
- `script.py.mako`: Template used by Alembic to generate new migration scripts.
- `versions/`: Directory where all generated migration files are stored.

---

## `tests/` Directory

- `auth/`: Contains tests related to authentication.
    - `test_otp.py`: Specifically tests the One-Time Password (OTP) authentication flow.
