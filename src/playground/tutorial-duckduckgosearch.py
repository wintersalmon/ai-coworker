from langchain_community.tools import DuckDuckGoSearchRun

print('begin')

search = DuckDuckGoSearchRun()

result = search.run("what is the weather like tomorrow in sf")

print(result)

