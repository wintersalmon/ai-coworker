from dotenv import load_dotenv
load_dotenv()


from langchain_community.graphs import Neo4jGraph

graph = Neo4jGraph()

from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(temperature=0, model_name="gpt-4o")


from langchain_core.documents import Document
text = """
Marie Curie, born in 1867, was a Polish and naturalised-French physicist and chemist who conducted pioneering research on radioactivity.
She was the first woman to win a Nobel Prize, the first person to win a Nobel Prize twice, and the only person to win a Nobel Prize in two scientific fields.
Her husband, Pierre Curie, was a co-winner of her first Nobel Prize, making them the first-ever married couple to win the Nobel Prize and launching the Curie family legacy of five Nobel Prizes.
She was, in 1906, the first woman to become a professor at the University of Paris.
"""
documents = [Document(page_content=text)]


# llm_transformer = LLMGraphTransformer(llm=llm)
# documents = [Document(page_content=text)]
# graph_documents = llm_transformer.convert_to_graph_documents(documents)
# print(f"Nodes:{graph_documents[0].nodes}")
# print(f"Relationships:{graph_documents[0].relationships}")


llm_transformer_props = LLMGraphTransformer(
    llm=llm,
    allowed_nodes=["Person", "Country", "Organization"],
    allowed_relationships=["NATIONALITY", "LOCATED_IN", "WORKED_AT", "SPOUSE"],
    node_properties=["born_year"],
)
graph_documents_props = llm_transformer_props.convert_to_graph_documents(documents)
print(f"Nodes:{graph_documents_props[0].nodes}")
print(f"Relationships:{graph_documents_props[0].relationships}")

# graph.add_graph_documents(graph_documents_props)

