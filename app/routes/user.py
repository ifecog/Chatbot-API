from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.user import UserResponse
from app.models.user import User
from app.utils.auth import get_current_user

router = APIRouter(prefix="/me", tags=["Profile"])

@router.get("/", response_model=UserResponse)
def get_my_profile(current_user: User = Depends(get_current_user)):
    return current_user
