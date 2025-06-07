import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

llm = ChatOpenAI(
    model='gpt-4o',
    temperature=0.7,
    openai_api_key=os.getenv('OPENAI_API_KEY')
)

def chat_with_gpt(user_input: str):
    messages = [
        SystemMessage(content='You are a helpful assistant.'),
        HumanMessage(content=user_input)
    ]
    return llm(messages).content