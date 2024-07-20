import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, UnstructuredPDFLoader
from langchain_community.vectorstores.pgvector import PGVector
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

loader = DirectoryLoader(
    os.path.abspath(
        "E:/FILE of Trong/GOOUP1/ChatBot_V2/data/data_final.pdf"),
    glob="**/*.pdf",
    use_multithreading=True,
    show_progress=True,
    max_concurrency=50,
    loader_cls=UnstructuredPDFLoader,
)
docs = loader.load()

embeddings = OpenAIEmbeddings(model='text-embedding-ada-002', )

text_splitter = SemanticChunker(
    embeddings=embeddings
)

flattened_docs = [Document(page_content=doc.page_content)
                  for doc in docs if doc.page_content]
chunks = text_splitter.split_documents(flattened_docs)

PGVector.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="ChatBot",
    connection_string=connection_string,
    pre_delete_collection=True,
)
