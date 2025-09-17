from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import List

def create_emdeding(text:List[str]):
    embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    return FAISS.from_texts(text,embedding)

def retrive_relevant_docs(vectorstore:FAISS,query:str,k:int=4):
    return vectorstore.similarity_search(query,k=k)

