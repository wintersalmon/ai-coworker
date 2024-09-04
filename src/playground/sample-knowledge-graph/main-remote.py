from langchain_community.graphs import Neo4jGraph
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.chat_models import ChatOllama
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_experimental.graph_transformers.llm import LLMGraphTransformer
from langchain_community.document_loaders import TextLoader


from dotenv import load_dotenv

load_dotenv()

def main():
    try:
        # Load documents

        loader = TextLoader(file_path="dummytext.txt")
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=24)
        documents = text_splitter.split_documents(documents=docs)

        # Load LLM and convert graph documents

        # llm = ChatOllama(model="llama3.1:8b")


        llm = OllamaFunctions(
            # model="llama3.1:70b",
            model="mixtral:8x22b",
            # model="gemma2:27b",
            format="json",
            base_url="http://192.168.10.2:11434/",
        )

        # llm = OllamaFunctions(
        #     model="llama3.1",
        #     format="json",
        # )

        llm_transformer = LLMGraphTransformer(
            llm=llm,
            allowed_nodes=["Person", "Country", "Organization"],
            allowed_relationships=["NATIONALITY", "LOCATED_IN", "WORKED_AT", "SPOUSE"],
            node_properties=["born_year"],
        )

        graph_documents = llm_transformer.convert_to_graph_documents(documents)

        print(f"Nodes:{graph_documents[0].nodes}")
        print(f"Relationships:{graph_documents[0].relationships}")

        # Load graph

        # graph = Neo4jGraph()
        # graph.add_graph_documents(
        #     graph_documents,
        #     baseEntityLabel=True,
        #     include_source=True
        # )

    except Exception as e:
        print(e)


main()