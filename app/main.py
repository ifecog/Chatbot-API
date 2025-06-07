from fastapi import FastAPI
from dotenv import load_dotenv

from app.routes.chat import router as chat_router

load_dotenv()

app = FastAPI(
    title='Chatbot API',
    description='A simple chatbot using OpenAI GPT-4o',
    version='1.0.0'
)

app.include_router(chat_router)


@app.get('/')
async def root():
    return {'message': 'Chatbot API is running!'}

@app.get('/health')
async def health_check():
    return {'status': 'healty!'}