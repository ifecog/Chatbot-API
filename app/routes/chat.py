from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.core.chat_engine import chat_engine

router = APIRouter(prefix='/chat', tags=['Chat'])


@router.post('/', response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        ai_response = await chat_engine.get_response(request.message)
        return ChatResponse(response=ai_response)
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f'Error processing chat request: {str(e)}'
        )
