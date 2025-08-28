from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Hotel


router=APIRouter(
    prefix="/hotels",
    tags=["Hotels"]
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency=Annotated[Session, Depends(get_db)]

@router.get("/", status_code=status.HTTP_200_OK)
async def read_all_hotels(db: db_dependency):
    hotel_model=db.query(Hotel).all()
    return hotel_model