from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.user import User
from app.utils.security import hash_password
from app.schemas.user import UserCreate


def create_user(user_data: UserCreate, db: Session):
    hashed_pw = hash_password(user_data.password)
    db_user = User(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        phone_number=user_data.phone_number,
        hashed_password=hashed_pw,
    )
    db.add(db_user)
    
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise ValueError("Email of phone number already exists.")
    
def get_user_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()
    
    
# 4c058ac2-00e4-4e72-a591-a2cd17d320e7