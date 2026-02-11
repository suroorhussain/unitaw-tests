
# Backend Test

A FastAPI event management application with user authentication.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
fastapi dev main.py
```

## API Endpoints

- `POST /register` - Register a new user
- `POST /login` - Login and get access token
- `GET /events` - List events (limit, offset params)
- `POST /events` - Create event (requires authentication)
- `GET /events/{event_id}` - Get specific event

## Environment

Requires Python 3.13
