from langchain_community.graphs import Neo4jGraph
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.chat_models import ChatOllama
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_experimental.graph_transformers.llm import LLMGraphTransformer, GraphDocument
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
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    splits = text_splitter.split_text(text)

    return [Document(page_content=split) for split in splits]


def generateGraphDocuments(
        documents: list[Document],
        LLM_MODEL: str
    ) -> list[list[GraphDocument]]:

    try:
        # init LLM
        LLM_MODEL = "mistral-nemo"
        llm = ChatOllama(
            model=LLM_MODEL,
        )

        # init graph transformer
        llm_transformer = LLMGraphTransformer(llm=llm)

        result = []
        totalDocuments = len(documents)
        for (index, doc) in enumerate(documents):
            print(f"Document {index+1}/{totalDocuments}")

            try:
                graph_documents = llm_transformer.convert_to_graph_documents([doc])

                print(f"doc: {doc}")
                print(f"Nodes:{graph_documents[0].nodes}")
                print(f"Relationships:{graph_documents[0].relationships}")

                result.append(graph_documents)

            except Exception as e:
                print('[error] in adding graph documents')
                print(e)
            
            print("Document added to graph")

        return result

    except Exception as e:
        print('[error] in generateGraphDocuments')
        print(e)
        return []
        


def main():
    try:
        # LLM_MODEL = "gemma2:2b"
        LLM_MODEL = "mistral-nemo"

        documents = loadDocumentAboutMarieCurie()

        graphDocuments = generateGraphDocuments(documents, LLM_MODEL)

        # init graph
        graphDB = Neo4jGraph()
        for item in graphDocuments:
            try:
                graphDB.add_graph_documents(
                    item,
                    baseEntityLabel=True,
                    include_source=True
                )
            except Exception as e:
                print('[error] in adding graph documents')
                print(e)

    except Exception as e:
        print('[error] in main')
        print(e)


main()