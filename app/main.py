import os

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv

from app.logging_config import setup_logging
from app.routes.chat import router as chat_router
from app.routes.upload import router as upload_router
from app.routes.auth import router as auth_router
from app.routes.oauth import router as oauth_router
from app.routes.user import router as user_router
from app.routes.admin import router as admin_router

load_dotenv()

setup_logging()

app = FastAPI(
    title='Chatbot API',
    description='A simple chatbot using OpenAI GPT-4o  model',
    version='1.0.0'
)

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv('SESSION_SECRET_KEY')
)

app.include_router(chat_router)
app.include_router(upload_router)
app.include_router(auth_router)
app.include_router(oauth_router)
app.include_router(user_router)
app.include_router(admin_router)


@app.get('/')
async def root():
    return {'message': 'PalChat API is running!'}

@app.get('/health')
async def health_check():
    return {'status': 'PalChat is...wait for it>>> healthy!'}