from fastapi import FastAPI
from dotenv import load_dotenv

from app.routes import chat

load_dotenv()

app = FastAPI(
    title='Chatbot API',
    description='A simpe chatbot using OpenAI GPT-4o'
    version='1.0.0'
)

app.include_router(chat.router, prefix='/chat', tags=['Chat'])


@app.get('/')
async def root():
    return {'message': 'Chatbot API is running!'}

@app.get('/health')
async def health_check():
    return {'status': 'healty!'}