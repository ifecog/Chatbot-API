from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.crud.user import get_user_by_id, get_all_users, create_admin_user, admin_exists
from app.schemas.user import UserResponse, UserCreate
from app.utils.auth import require_admin

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post('/create', response_model=UserResponse)
def create_admin(user_data: UserCreate, db: Session = Depends(get_db)):
    if admin_exists(db):
        raise HTTPException(
            status_code=403,
            detail='Admin already exists. You must be an admin to create more'
        )
    
    try:
        user = create_admin_user(user_data, db)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get('/users', response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db), _: str = Depends(require_admin)):
    return get_all_users(db)

@router.get('/users/{user_id}', response_model=UserResponse)
def get_user(user_id: str, db: Session = Depends(get_db), _: str = Depends(require_admin)):
    user = get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user