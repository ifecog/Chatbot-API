from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse, UserLogin, Token
from app.crud.user import create_user, get_user_by_email
from app.dependencies import get_db
from app.utils.security import verify_password, create_access_token

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.post('/signup', response_model=UserResponse)
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        user = create_user(user_data, db)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
        
@router.post('/signin', response_model=Token)
def signin(user_data: UserLogin, db: Session = Depends(get_db)):
    user = get_user_by_email(user_data.email, db)
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail='Invallid credentials')
    
    token = create_access_token({'sub': str(user.id)})
    return {'access_token': token, 'token_type': 'bearer'}
    