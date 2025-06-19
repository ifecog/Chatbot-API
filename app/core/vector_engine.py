import os
import logging

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

logger = logging.getLogger(__name__)
embedding_model = OpenAIEmbeddings(api_key=os.getenv('OPENAI_API_KEY'))
FAISS_PATH = 'faiss_index'

def load_vector_store(faiss_path: str = FAISS_PATH):
    try:
        logger.info(f'Loading vector store from {faiss_path}')
        return FAISS.load_local(faiss_path, embeddings=embedding_model)
    except Exception as e:
        logger.exception(f'Error loading vector store: {str(e)}')
        raise
    
def retrieve_similar_chunks(query: str, k: int = 4):
    try:
        vector_store = load_vector_store()
        results = vector_store.similarity_search(query, k=k)
        logger.info(f'Retrieved {len(results)} chinks from query: {query}')
        return results
    except Exception as e:
        logger.exception(f'Failed to retrieve doocuments: {str(e)}')
        raise
