# Chaos to Clarity – Backend

The Chaos to Clarity backend is a Django REST Framework–based API that accepts unstructured operational input, processes it through a classification service, and exposes structured data for exploration and analytics.

## Overview
This backend accepts unstructured operational inputs, processes them into structured data, and exposes APIs for insights and analytics.

## Core Responsibilities

Accept raw, unstructured text input
Classify input into structured fields (category, severity, tags, confidence)
Persist raw and processed data
Expose clean REST APIs for:
    Data ingestion
    Retrieval & filtering
    Analytics & trends

## Tech Stack
Framework: Django + Django REST Framework
Database: SQLite (development & demo)
API Style: REST (JSON)
Static Handling: WhiteNoise
Deployment: Render
Python Version: 3.10+

## Project Structure
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

## API Endpoints
API Root -> GET /api/
Submit Raw Input -> POST /api/input/
Retrieve Entries -> GET /api/entries/
Analytics -> GET /api/stats/
Returns count of entries per category -> GET /api/trends/

## Data Flow
Raw Text
   ↓
/api/input/
   ↓
Classification Service
   ↓
RawInput + ProcessedEntry Models
   ↓
/api/entries/ | /api/stats/ | /api/trends/

## Models Overview
RawInput
Stores original unstructured text
Preserved for auditing and traceability

ProcessedEntry:
One-to-one relationship with RawInput
Stores classified output:
    Category
    Severity
    Confidence
    Tags
    Timestamp

## Authentication & Permissions

Currently configured with:
    AllowAny permission
    No authentication required
Designed for demo and portfolio usage
Authentication can be added later without breaking API contracts.

## CORS & Frontend Integration
CORS enabled for browser-based frontend
Accepts JSON requests from deployed frontend
Designed to work seamlessly with static frontend hosting

## Deployment Notes
Deployed on Render
Uses Gunicorn as WSGI server
Static files handled via WhiteNoise
Environment-agnostic configuration using python-decouple

## Future Improvements

Token-based authentication (JWT)
Pagination & ordering
PostgreSQL for production
Async classification
Admin analytics dashboard

## Author
Siddhant Rajdeep Chakre
Electronics & Telecommunication Engineer

## Status
Backend implemented and tested locally.
