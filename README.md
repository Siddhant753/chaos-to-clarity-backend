# Chaos to Clarity – Backend

A Django REST Framework-based backend that accepts unstructured text input, processes it into structured data (category, severity, tags), and exposes APIs for storage, retrieval, and basic analytics.

## Overview
This is the backend service for the Chaos to Clarity system. It provides RESTful APIs to process unstructured text data and convert it into structured formats, along with persistent storage for traceability.

## Core Responsibilities

- Accept raw, unstructured text input
- Classify input into structured fields (category, severity, tags, confidence)
- Persist raw and processed data
-Expose clean REST APIs for:
  - Data ingestion
  - Retrieval & filtering
  - Analytics & trends

## Tech Stack
- Framework: Django + Django REST Framework
- Database: SQLite (development & demo)
- API Style: REST (JSON)
- Static Handling: WhiteNoise
- Deployment: Render
- Python Version: 3.10+

## Project Structure
```
chaos_backend/
│
├── chaos_backend/        # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/                 # Main application
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── services/
│   │   └── classifier.py
│   └── urls.py
│
├── db.sqlite3
├── requirements.txt
└── README.md
```

## API Endpoints

| Method | Endpoint        | Description                          |
|--------|---------------|--------------------------------------|
| GET    | /api/         | API root                            |
| POST   | /api/input/   | Submit raw text input               |
| GET    | /api/entries/ | Retrieve processed entries          |
| GET    | /api/stats/   | Get category-wise statistics        |
| GET    | /api/trends/  | Get trends over time                |

## Data Flow
```
Raw Text
   ↓
/api/input/
   ↓
Classification Service
   ↓
RawInput + ProcessedEntry Models
   ↓
/api/entries/ | /api/stats/ | /api/trends/
```

## Models Overview
RawInput:
- Stores original unstructured text
- Preserved for auditing and traceability

ProcessedEntry:
- One-to-one relationship with RawInput
- Stores classified output:
  - Category
  - Severity
  - Confidence
  - Tags
  - Timestamp

## Authentication & Permissions
- Currently uses open access (AllowAny) for demonstration purposes  
- Designed to support authentication (e.g., JWT) without breaking API structure  

## CORS & Frontend Integration
CORS enabled for browser-based frontend
Accepts JSON requests from deployed frontend
Designed to work seamlessly with static frontend hosting

## Deployment Notes
Deployed on Render
Uses Gunicorn as WSGI server
Static files handled via WhiteNoise
Environment-agnostic configuration using python-decouple

## Example Request
```
{
  "text": "Motor overheating after 3 hours"
}
```

## Example Response
```
{
    "id": 3,
    "raw_text": "Motor is overheating",
    "category": "Incident",
    "tags": [
        "overheat"
    ],
    "severity": "high",
    "confidence": 0.7,
    "created_at": "2026-03-18T09:45:04.876220Z",
    "raw_input": 3
}
```

## Future Improvements

- Token-based authentication (JWT)
- Pagination & ordering
- PostgreSQL for production
- Async classification
- Admin analytics dashboard

## Author
Siddhant Rajdeep Chakre
Electronics & Telecommunication Engineer

## Status
Backend implemented and tested locally.
