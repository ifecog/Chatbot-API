import os
import logging
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

from app.core.document_loader import load_and_split_docs

load_dotenv()

logger = logging.getLogger(__name__)
embedding_model = OpenAIEmbeddings(api_key=os.getenv('OPENAI_API_KEY'))


def create_vector_store_from_file(file_path: str, faiss_path: str = 'faiss_index'):
    try:
        logger.info(f"Loading file: {file_path}")
        
        docs = load_and_split_docs(file_path)
        logger.info(f"Split into {len(docs)} chunks.")
    
        vector_store = FAISS.from_documents(docs, embedding_model)
        vector_store.save_local(faiss_path)
        logger.info(f"Vector store saved to: {faiss_path}")
        
    except Exception as e:
        logger.exception(f"Failed to create vectore store: {str(e)}")
        raise
