from fastapi import FastAPI, Depends
from .database import engine, SessionLocal
from .models import Base
from .routers import hotel

app=FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@app.get("/")
def home():
    return {"message": "Welcome to Hotel Booking API!"}

app.include_router(hotel.router)