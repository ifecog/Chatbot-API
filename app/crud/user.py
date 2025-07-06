from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.user import User, UserRole
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
    
def get_all_users(db: Session):
    return db.query(User).all()
    
def get_user_by_id(user_id: str, db: Session):
    return db.query(User).filter(User.id == user_id).first()
    
def get_user_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()

def update_user(user: User, update: dict, db: Session):
    for key, val in update.items():
        setattr(user, key, val)
    db.commit()
    db.refresh(user)
    return user

def delete_user(user: User, db: Session):
    db.delete(user)
    db.commit()
    
    
# Admin

def admin_exists(db: Session) -> bool:
    return db.query(User).filter(User.role == UserRole.admin).first() is not None

def create_admin_user(user_data: UserCreate, db: Session) -> User:
    hashed_pw = hash_password(user_data.password)
    db_user = User(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        phone_number=user_data.phone_number,
        hashed_password=hashed_pw,
        role=UserRole.admin
    )
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise ValueError("Email or phone number already exists.")
