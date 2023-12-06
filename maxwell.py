"""
    This script reads pdfs from data/ and encodes them into the database
"""

import os

import pinecone

from dotenv import load_dotenv

from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings

from langchain.text_splitter import TokenTextSplitter

from langchain.vectorstores import Pinecone


def main():
    load_dotenv()
    """
        Loading multiple file types like this isn't ideal, in the future 
        we'd want to make our own DirectoryLoader class that can handle
        multiple filetypes better and can check embeddings against pinecone.
    """
    loader = DirectoryLoader(
        'data/',
        glob='**/*.[pr][ds][ft]',
        use_multithreading=True,
        show_progress=True,
    )

    text_splitter = TokenTextSplitter(chunk_size=500, chunk_overlap=0)

    documents = loader.load()

    split_documents = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment="gcp-starter",
    )

    vector_store = Pinecone(pinecone.Index("chatbot"), embeddings, "text")

    vector_store.add_documents(split_documents)


if __name__ == "__main__":
    main()