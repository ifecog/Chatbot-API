import uuid

from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from app.models.user import User
from app.models.chat import ChatSession, ChatMessage
from app.schemas.chat import ChatRequest, ChatResponse
from app.core.chat_engine import chat_engine
from app.dependencies import get_db
from app.utils.auth import get_current_user

router = APIRouter(prefix='/api/v1/chat', tags=['Chat'])


@router.post('/new-session')
async def create_new_session(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    
    new_session_id = str(uuid.uuid4())
    session = ChatSession(
        session_id=new_session_id,
        user_id=current_user.id
    )
    
    db.add(session)
    db.commit()
    db.refresh(session)
    
    return {
        'session_id': new_session_id,
        'message': 'New session created. Use this session_id for your conversation.'
    }


@router.post('/', response_model=ChatResponse)
async def chat(
    request: ChatRequest, db: Session = Depends(get_db)
    ):
    session = db.query(ChatSession).filter_by(
        session_id=request.session_id
    ).first()
    if not session:
        raise HTTPException(status_code=404, detail='Session not found.')
    
    user_msg = ChatMessage(
        session_id=request.session_id,
        message_type='human',
        content=request.message
    )
    
    db.add(user_msg)
    db.commit()
    
    try:
        ai_response = await chat_engine.get_response(
            message=request.message,
            session_id=request.session_id,
            db=db
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
async def clear_session(session_id: str, db: Session = Depends(get_db)):
    try:
        success = chat_engine.clear_session(session_id, db)
        return {
            'message': f'Session {session_id} cleared' if success else f'Session {session_id} not found.',
            'success': success 
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error clearing session: {str(e)}"
        )
    
@router.get('/{session_id}/history')
async def get_session_history(session_id: str, db: Session = Depends(get_db)):
    try:
        history = chat_engine.get_session_history(session_id, db)
        return {
            'session_id': session_id,
            'history': history
        }
       
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error getting session history: {str(e)}"
        )