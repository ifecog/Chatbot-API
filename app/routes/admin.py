from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.crud.user import get_user_by_id, get_all_users
from app.schemas.user import UserResponse
from app.utils.auth import require_admin

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get('/users', response_model=UserResponse)
def list_users(db: Session = Depends(get_db), _: str = Depends(require_admin)):
    return get_all_users(db)

@router.get('/users/{user_id}', response_model=UserResponse)
def get_user(user_id: str, db: Session = Depends(get_db), _: str = Depends(require_admin)):
    user = get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user