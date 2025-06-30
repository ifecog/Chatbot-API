import os

from fastapi import APIRouter, Request, Depends, HTTPException
from starlette.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from dotenv import load_dotenv

from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.crud.user import get_user_by_email, create_user
from app.utils.security import create_access_token
from app.schemas.user import UserCreate

load_dotenv()

router = APIRouter(prefix="/auth/google", tags=["OAuth"])


oauth = OAuth()
oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

@router.get('/')
async def login_with_google(request: Request):
    redirect_uri = request.url_for('google_callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get('/callback')
async def google_callback(request: Request, db: Session = Depends(get_db)):
    token = await oauth.google.authorize_access_token(request)
    user_info = await oauth.google.parse_id_token(request, token)
    
    if not user_info:
        raise HTTPException(status_code=400, detail="Failed to retrieve user info")

    user = get_user_by_email(user_info['email'], db)
    if not user:
        new_user = UserCreate(
            first_name=user_info.get("given_name", ""),
            last_name=user_info.get("family_name", ""),
            email=user_info["email"],
            phone_number="",
            password="oauth_google_no_pw"
        )
        
        user = create_user(new_user, db)
        
    access_token = create_access_token({'sub': str(user.id)})
    return {'access_token': access_token, 'token_type': 'bearer'}