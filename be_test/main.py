from fastapi import FastAPI

EVENTS = [
    {"id": 1, "title": "Event 1", "description": "Description of Event 1", "location": "Location 1", "featured": True, "image": "https://example.com/event1.jpg", "datelist": ["2024-07-01", "2024-07-02"]},
    {"id": 2, "title": "Event 2", "description": "Description of Event 2", "location": "Location 2", "featured": False, "image": "https://example.com/event2.jpg", "datelist": ["2024-08-01", "2024-08-02"]},
    {"id": 3, "title": "Event 3", "description": "Description of Event 3", "location": "Location 3", "featured": True, "image": "https://example.com/event3.jpg", "datelist": ["2024-09-01", "2024-09-02"]},
    {"id": 4, "title": "Event 4", "description": "Description of Event 4", "location": "Location 4", "featured": False, "image": "https://example.com/event4.jpg", "datelist": ["2024-10-01", "2024-10-02"]},
    {"id": 5, "title": "Event 5", "description": "Description of Event 5", "location": "Location 5", "featured": True, "image": "https://example.com/event5.jpg", "datelist": ["2024-11-01", "2024-11-02"]},
    {"id": 6, "title": "Event 6", "description": "Description of Event 6", "location": "Location 6", "featured": False, "image": "https://example.com/event6.jpg", "datelist": ["2024-12-01", "2024-12-02"]},
    {"id": 7, "title": "Event 7", "description": "Description of Event 7", "location": "Location 7", "featured": True, "image": "https://example.com/event7.jpg", "datelist": ["2025-01-01", "2025-01-02"]},
]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world!"}

@app.get("/events")
async def get_events(limit: int = 10, offset: int = 0):
    return {"data": EVENTS[offset:offset+limit]}

@app.get("/events/{event_id}")
async def get_event(event_id: int):
    for event in EVENTS:
        if event["id"] == event_id:
            break
    return {"data": event}