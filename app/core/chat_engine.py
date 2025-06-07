import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()


class ChatEngine:
    def __init__(self):
        self.llm = ChatOpenAI(
            model='gpt-4o',
            temperature=0.7,
            api_key=os.getenv('OPENAI_API_KEY')
        )
        
    async def get_response(self, message: str):
        try:
            human_message = HumanMessage(content=message)
            ai_response = self.llm.invoke([human_message])
            
            return ai_response.content
        
        except Exception as e:
            raise Exception(f'Error getting AI response: {str(e)}')
        
chat_engine = ChatEngine()



# llm = ChatOpenAI(
#     model='gpt-4o',
#     temperature=0.7,
#     openai_api_key=os.getenv('OPENAI_API_KEY')
# )

# def chat_with_gpt(user_input: str):
#     messages = [
#         SystemMessage(content='You are a helpful assistant.'),
#         HumanMessage(content=user_input)
#     ]
#     return llm(messages).content