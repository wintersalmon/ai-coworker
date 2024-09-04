from langchain_community.llms import Ollama
model = Ollama(model="llama3:8b")

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain = model | parser

msg = chain.invoke(messages)

print(msg)

