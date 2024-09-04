import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def loadDocumentsAboutLLM() -> list[Document]:
    # Only keep post title, headers, and content from the full HTML.
    bs4_strainer = bs4.SoupStrainer(class_=("post-title", "post-header", "post-content"))
    loader = WebBaseLoader(
        web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",), # LLM Powered Autonomous Agents
        bs_kwargs={"parse_only": bs4_strainer},
    )

    docs = loader.load()

    return docs
    
    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    # splits = text_splitter.split_documents(docs)

    # return splits
