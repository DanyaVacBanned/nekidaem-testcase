from typing import List

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from src.database import get_db
from src.users import models
from src.users import schemas

router = APIRouter(prefix='/users')


@router.post(path='/create', response_model=schemas.User)
def create_user(user_name: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = models.Users(name=user_name.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get('/get', response_model=List[schemas.User])
def get_users(user_id: int | None = None, db: Session = Depends(get_db)):
    if user_id:
        user = db.query(models.Users).filter(models.Users.id == user_id).all()
        return user
    return db.query(models.Users).all()
