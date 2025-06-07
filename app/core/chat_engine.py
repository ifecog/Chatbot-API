import os
from collections import defaultdict
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()


class ChatEngine:
    def __init__(self):
        self.llm = ChatOpenAI(
            model='gpt-4o',
            temperature=0.7,
            api_key=os.getenv('OPENAI_API_KEY')
        )
        self.conversations = defaultdict(list)
        
    def _get_conversation_messages(self, session_id: str):
        if session_id not in self.conversations:
            self.conversations[session_id] = []
            
        return self.conversations[session_id]
        
    async def get_response(self, message: str, session_id: str = 'default'):
        try:
            conversation_messages = self._get_conversation_messages(session_id)
            
            current_messages = conversation_messages + [HumanMessage(content=message)]
            
            ai_response = self.llm.invoke(current_messages)
            
            conversation_messages.append(HumanMessage(content=message))
            conversation_messages.append(AIMessage(content=ai_response.content))
            
            return ai_response.content
        
        except Exception as e:
            raise Exception(f'Error getting AI response: {str(e)}')
        
    def clear_session(self, session_id: str):
        if session_id in self.conversations:
            del self.conversations[session_id]
            return True
        return False
    
    def get_session_history(self, session_id: str):
        if session_id in self.conversations and self.conversations[session_id]:
            history = []
            messages = self.conversations[session_id]
            
            for msg in messages:
                if isinstance(msg, HumanMessage):
                    history.append(f'Human: {msg.content}')
                elif isinstance(msg, AIMessage):
                    history.append(f'AI: {msg.content}')
                    
            return '\n'.join(history)
        
        return 'No conversation history found.' 
    
        
chat_engine = ChatEngine()

