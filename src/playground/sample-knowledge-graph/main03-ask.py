from dotenv import load_dotenv

load_dotenv()

from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_community.chat_models import ChatOllama

def main():
    try:
        graphDB = Neo4jGraph()

        LLM_MODEL = "mistral-nemo"
        llm = ChatOllama(
            model=LLM_MODEL,
        )

        graphDB.refresh_schema()

        cypher_chain = GraphCypherQAChain.from_llm(
            graph=graphDB,
            cypher_llm=llm,
            qa_llm=llm,
            validate_cypher=True,
            verbose=True
        )

        q = cypher_chain.run("Who is Marie Curie?")
        print(q)


    finally:
        print('end')
    

if __name__ == '__main__':
    main()
