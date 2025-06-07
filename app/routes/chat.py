from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.core.openai_chain import chat_with_gpt

router = APIRouter()


@router.post('/', response_model=ChatResponse)
async def chat(request: ChatRequest):
    reply = chat_with_gpt(request.message)
    return ChatResponse(response=reply)
