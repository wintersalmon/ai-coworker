from langchain_community.graphs import Neo4jGraph
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.chat_models import ChatOllama
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_experimental.graph_transformers.llm import LLMGraphTransformer
from langchain_community.document_loaders import TextLoader


from dotenv import load_dotenv

load_dotenv()

from langchain_core.documents import Document

def loadDocumentAboutMarieCurie() -> list[Document]:
    with open('sample-dummytext.txt', 'r') as file:
        text = file.read()

    return [Document(page_content=text)]

def loadDocumentsAboutLLM() -> list[Document]:
    with open('./sample-LLM-Powered-Autonomous-Agents.txt', 'r') as file:
        text = file.read()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_text(text)

    return [Document(page_content=split) for split in splits]


def main():
    try:
        # LLM_MODEL = "gemma2:2b"
        LLM_MODEL = "mistral-nemo"
        documents = loadDocumentsAboutLLM()

        llm = ChatOllama(
            model=LLM_MODEL,
        )

        llm_transformer = LLMGraphTransformer(
            llm=llm,
            # allowed_nodes=["Person", "Country", "Organization"],
            # allowed_relationships=["NATIONALITY", "LOCATED_IN", "WORKED_AT", "SPOUSE"],
            # node_properties=["born_year"],
        )

        graph = Neo4jGraph()

        totalDocuments = len(documents)
        for (index, doc) in enumerate(documents):
            print(f"Document {index+1}/{totalDocuments}")

            try:

                graph_documents = llm_transformer.convert_to_graph_documents([doc])

                print(f"Nodes:{graph_documents[0].nodes}")
                print(f"Relationships:{graph_documents[0].relationships}")

                graph.add_graph_documents(
                    graph_documents,
                    baseEntityLabel=True,
                    include_source=True
                )
            except Exception as e:
                print('error in adding graph documents')
                print(e)
            
            print("Document added to graph")

    except Exception as e:
        print('error in main')
        print(e)


main()