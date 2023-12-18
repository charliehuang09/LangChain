from cgitb import text
from pydoc import doc
from langchain.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pgvector import PGVector
from langchain.docstore.document import Document
from loader import Loader

from dotenv import load_dotenv
from key import *
from misc import *
from tqdm import tqdm
from langchain.docstore.document import Document
from unstructured.partition.pdf import partition_pdf
import os

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=20)
embeddings = OpenAIEmbeddings()
store = PGVector(
    collection_name=COLLECTION_NAME,
    connection_string=CONNECTION_STRING,
    embedding_function=OpenAIEmbeddings()
)
loader = Loader(PATH)
documents = loader.load()
print(documents)
documents = text_splitter.split_documents(documents)
store.add_documents(documents)