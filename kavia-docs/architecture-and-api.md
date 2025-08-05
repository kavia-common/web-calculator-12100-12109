# Calculator Backend – Architecture and API Reference

## Project Overview

The _calculator_backend_ is a stateless Django REST API service that provides arithmetic operations (addition, subtraction, multiplication, division) through HTTP endpoints. Its primary goal is to serve as the backend component for a web-based calculator application, exposing operations via a secure and well-documented RESTful interface.

- **Framework**: Django 5.2 with Django REST Framework and drf-yasg for OpenAPI docs
- **Persistence**: No persistent storage, session, or user data—pure functional API
- **API Style**: RESTful (all endpoints under `/api/`)
- **API Schema/Docs**: OpenAPI/Swagger available via `/docs` and `/redoc` routes

---

## Architecture Overview

The application adheres to a standard Django project structure, with a main project (`config`), a dedicated API app (`api`), and automatic OpenAPI docs routing.

### Main Architectural Layers

```mermaid
flowchart TD
    subgraph Django Project "calculator_backend"
        direction TB
        A[config<br/>project root] -->|Defines settings, URLs| B(api app)
        B -->|Defines endpoints| C[Views (views.py)]
        B -->|Exposes urls| D[urls.py (api)]
        A -->|Includes URLs| D2[urls.py (config)]
    end

    F[Client (Frontend/App)] -- HTTP(S) API --> D2
    D2 -.->|Swagger/Redoc| E[Auto-generated OpenAPI docs]
```

### Key Project Components

- **api/views.py**: Contains logic for all arithmetic and health check API endpoints.
- **api/urls.py**: Maps endpoint URLs to view functions.
- **config/urls.py**: Top-level URL routing, including admin and documentation endpoints.
- **config/settings.py**: Project configuration, Django apps, middleware, database setup (uses SQLite but not utilized for storage in this app).

---

## API Endpoints and Usage

All endpoints are mounted under `/api/*`. Endpoints support both `GET` (for browser access via query parameters) and `POST` (for API consumers using JSON).

#### Health Check

- **GET /api/health/**
- **Response**: `{ "message": "Server is up!" }`

#### Addition

- **GET /api/add/?a=5&b=3**
- **POST /api/add/**  with JSON body: `{ "a": 5, "b": 3 }`
- **Response**: `{ "result": 8 }`

#### Subtraction

- **GET /api/subtract/?a=5&b=3**
- **POST /api/subtract/**  with JSON body: `{ "a": 5, "b": 3 }`
- **Response**: `{ "result": 2 }`

#### Multiplication

- **GET /api/multiply/?a=5&b=3**
- **POST /api/multiply/**  with JSON body: `{ "a": 5, "b": 3 }`
- **Response**: `{ "result": 15 }`

#### Division

- **GET /api/divide/?a=6&b=3**
- **POST /api/divide/**  with JSON body: `{ "a": 6, "b": 3 }`
- **Response**: `{ "result": 2 }`
- **Error Response** (if `b=0`): `{ "error": "Division by zero is not allowed." }`

#### Error Responses

All endpoints return error messages and HTTP 400 if either input `a` or `b` is missing or not numeric.

---

## API Documentation (OpenAPI/Swagger)

- **Swagger UI:**  `/docs`
- **Redoc:**      `/redoc`
- **OpenAPI JSON:** `/swagger.json`

Interactive API documentation and schema browsing is enabled with `drf-yasg`, reading definitions from code.

---

## Key Components and Files

| File/Module                                      | Purpose                                                            |
|--------------------------------------------------|--------------------------------------------------------------------|
| `api/views.py`                                   | Defines endpoint logic; validates input, computes responses        |
| `api/urls.py`                                    | Maps API URL paths to corresponding view functions                 |
| `config/urls.py`                                 | Main project URLs (admin, `/api/`, and API documentation routes)   |
| `config/settings.py`                             | Project settings (apps, middleware, database, CORS, etc.)          |
| `interfaces/openapi.json`                        | Auto-generated OpenAPI 2.0 (Swagger) API specification             |
| `api/tests.py`                                   | Example test, currently covers health endpoint                     |
| `manage.py`                                      | Script for running the Django project                              |

_No models are defined. No state or user data is stored._

---

## Setup and Running Instructions

1. **Requirements**
   - Python (typically 3.8+)
   - pip

2. **Install dependencies**  
   From project root:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the development server**  
   From within the `calculator_backend` directory:
   ```bash
   python manage.py runserver
   ```

4. **Access the API**
   - API Endpoints: `http://localhost:8000/api/`
   - API Docs: `http://localhost:8000/docs`
   - Redoc: `http://localhost:8000/redoc`

---

## Example Usage

**GET Example:**  
`curl 'http://localhost:8000/api/add/?a=10&b=5'`  
_Response:_ `{ "result": 15 }`

**POST Example:**  
```bash
curl -X POST 'http://localhost:8000/api/multiply/' \
     -H "Content-Type: application/json" \
     -d '{"a": 3, "b": 7}'
```
_Response:_ `{ "result": 21 }`

---

## Security and CORS

CORS (Cross-Origin Resource Sharing) is enabled for all origins by default in development (`CORS_ALLOW_ALL_ORIGINS = True`). For production environments, review Django and DRF security guidelines.

---

## License and Support

This backend is designed for instructional and testing purposes. No commercial license or support is provided.

---
