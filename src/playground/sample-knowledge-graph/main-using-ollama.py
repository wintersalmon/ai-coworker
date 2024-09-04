from langchain_community.graphs import Neo4jGraph
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.chat_models import ChatOllama
from langchain_experimental.graph_transformers.llm import LLMGraphTransformer
from langchain_community.document_loaders import TextLoader


from dotenv import load_dotenv

load_dotenv()


# Load graph

graph = Neo4jGraph()


# Load documents

docs = """
Marie Curie, born in 1867, was a Polish and naturalised-French physicist and chemist who conducted pioneering research on radioactivity.
She was the first woman to win a Nobel Prize, the first person to win a Nobel Prize twice, and the only person to win a Nobel Prize in two scientific fields.
Her husband, Pierre Curie, was a co-winner of her first Nobel Prize, making them the first-ever married couple to win the Nobel Prize and launching the Curie family legacy of five Nobel Prizes.
She was, in 1906, the first woman to become a professor at the University of Paris.
"""

loader = TextLoader(file_path="dummytext.txt")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=24)
documents = text_splitter.split_documents(documents=docs)


# Load LLM and convert graph documents

llm = ChatOllama(model="llama3.1", temperature=0)
llm_transformer = LLMGraphTransformer(llm=llm)

graph_documents = llm_transformer.convert_to_graph_documents(documents)

graph.add_graph_documents(
    graph_documents,
    baseEntityLabel=True,
    include_source=True
)
