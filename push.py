from cgitb import text
from pydoc import doc
from langchain.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pgvector import PGVector
from langchain.docstore.document import Document

from dotenv import load_dotenv
from key import *
from misc import *
from tqdm import tqdm
import os

paths = getFiles(PATH)
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=20)
embeddings = OpenAIEmbeddings()
store = PGVector(
    collection_name=COLLECTION_NAME,
    connection_string=CONNECTION_STRING,
    embedding_function=OpenAIEmbeddings()
)
loader = DirectoryLoader(PATH, 
                         show_progress=True, 
                         use_multithreading=True,
                         glob="**/*.[pr][ds][ft]"
                         )
documents = loader.load()
documents = removeNull(documents)
documents = removeDots(documents)
documents = text_splitter.split_documents(documents)
store.add_documents(documents)