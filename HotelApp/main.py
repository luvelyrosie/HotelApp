from fastapi import FastAPI, Depends
from .database import engine, SessionLocal
from .models import Base
from .routers import hotel
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()


origins = [
    "http://localhost:5173",  # Vue frontend
    "http://127.0.0.1:5173",  # just in case 127.0.0.1
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allow Vue frontend
    allow_credentials=True,
    allow_methods=["*"],    # allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],    # allow all headers
)


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