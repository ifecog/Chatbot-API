import os
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


# def load_and_split_docs(file_path: str):
#     ext = os.path.splitext(file_path)[1].lower()
    
#     if ext == '.pdf':
#         loader = PyPDFLoader(file_path)
#     elif ext == '.txt' or ext == '.md':
#         loader = TextLoader(file_path)
#     else:
#         raise ValueError('Unsupported file format. Only PDF, TXT, and MD filel formats are supported')
    
#     documents = loader.load()
    
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=100
#     )
    
#     split_docs = splitter.split_documents(documents)
#     return split_docs