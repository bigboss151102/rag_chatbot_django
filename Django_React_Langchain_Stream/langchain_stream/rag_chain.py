import os
from operator import itemgetter
from typing import TypedDict

from dotenv import load_dotenv
from langchain_community.vectorstores.pgvector import PGVector
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

vector_store = PGVector(
    collection_name="ChatBot",
    connection_string=connection_string,
    embedding_function=OpenAIEmbeddings()
)

template = """
Answer given the following context:
{context}

Question: {question}
"""

ANSWER_PROMPT = ChatPromptTemplate.from_template(template)

llm = ChatOpenAI(temperature=0, model='gpt-4-1106-preview', streaming=True)


class RagInput(TypedDict):
    question: str


output_parser = StrOutputParser()
final_chain = (
    {
        "context": (itemgetter("question") | vector_store.as_retriever()),
        "question": itemgetter("question")
    }
    | ANSWER_PROMPT
    | llm
    | output_parser.with_config({"run_name": "Assistant"})
).with_types(input_type=RagInput)
