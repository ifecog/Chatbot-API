from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.core.chat_engine import chat_engine

router = APIRouter(prefix='/chat', tags=['Chat'])


@router.post('/new-session')
async def create_new_session():
    import uuid
    
    new_session_id = str(uuid.uuid4())
    return {
        'session_id': new_session_id,
        'message': 'New session created. Use this session_id for your conversation.'
    }


@router.post('/', response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        ai_response = await chat_engine.get_response(
            message=request.message,
            session_id=request.session_id
        )
        
        return ChatResponse(
            response=ai_response,
            session_id=request.session_id
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f'Error processing chat request: {str(e)}'
        )

@router.delete('/{session_id}')
async def clear_session(session_id: str):
    success = chat_engine.clear_session(session_id)
    return {
        'message': f'Session {session_id} cleared' if success else f'Session {session_id} not found.',
        'success': success 
    }
    
@router.get('/{session_id}/history')
async def get_session_history(session_id: str):
    history = chat_engine.get_session_history(session_id)
    return {
        'session_id': session_id,
        'history': history
    }