from calendar import prmonth
from cgitb import text
from pydoc import cli, doc
from urllib import response
from langchain.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pgvector import PGVector
from langchain.docstore.document import Document
from openai import OpenAI
from dotenv import load_dotenv
from key import *
from misc import *
from tqdm import tqdm
import os

client = OpenAI(
    api_key=OPENAI_KEY,
)

embeddings = OpenAIEmbeddings()
store = PGVector(
    collection_name=COLLECTION_NAME,
    connection_string=CONNECTION_STRING,
    embedding_function=OpenAIEmbeddings()
)

prompt = "How do I contribute to FRC971?"
context = store.similarity_search_with_score(prompt, k=8)
prompt = template(context, prompt)

print(prompt + "\n\n")
# exit(0)

response = GPT4(prompt, client)
print(response.choices[0].message.content)


