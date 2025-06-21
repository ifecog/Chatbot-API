from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, Integer

from app.database import Base


class ChatSession(Base):
    __tablename__ = 'chat_sessions'
    
    session_id = Column(String(36), primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
class ChatMessage(Base):
    __tablename__ = 'chat_messages'
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(36), index=True)
    message_type = Column(String(10))
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)    
    