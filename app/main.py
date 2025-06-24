from fastapi import FastAPI
from dotenv import load_dotenv

from app.logging_config import setup_logging
from app.routes.chat import router as chat_router
from app.routes.upload import router as upload_router
from app.routes.user import router as user_router

load_dotenv()

setup_logging()

app = FastAPI(
    title='Chatbot API',
    description='A simple chatbot using OpenAI GPT-4o  model',
    version='1.0.0'
)

app.include_router(chat_router)
app.include_router(upload_router)
app.include_router(user_router)


@app.get('/')
async def root():
    return {'message': 'Chatbot API is running!'}

@app.get('/health')
async def health_check():
    return {'status': 'healthy!'}