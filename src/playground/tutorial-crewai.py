from crewai import Agent, Task, Crew
from langchain_community.tools import DuckDuckGoSearchRun

from langchain_community.llms import Ollama
ollama_llm = Ollama(model="llama3")

from crewai_tools import tool
@tool("Duck_Duck_Go_Search")
def ddgsearch(question: str) -> str:
    """Clear description for what this tool is useful for, your agent will need this information to use it."""
    # Function logic here
    return DuckDuckGoSearchRun().run(question)

research_topic = "Differences between open source large language models and closed source large language models."

researcher = Agent(
  role='Researcher',
  goal='Search the internet about {research_topic}',
  backstory="""
  You are a researcher. Using the information in the task, you find out some of the most popular facts about the topic along with some of the trending aspects.
  You provide a lot of information thereby allowing a choice in the content selected for the final blog
  """,
  verbose=True,            # want to see the thinking behind
  allow_delegation=False,  # Not allowed to ask any of the other roles
  tools=[DuckDuckGoSearchRun()],
  # tools=[ddgsearch],        # Is allowed to use the following tools to conduct research
  llm=ollama_llm           # local model
)

writer = Agent(
  role='Tech Content Strategist',
  goal='Craft compelling content on a set of information provided by the researcher.',
  backstory="""You are a writer known for your humorous but informative way of explaining. 
  You transform complex concepts into compelling narratives.""",
  verbose=True,            # want to see the thinking behind
  allow_delegation=True,   # can ask the "researcher" for more information
  llm=ollama_llm           # using the local model
)

task1 = Task(
  agent=researcher,
  description=research_topic,
  expected_output="A complete analysis of the {research_topic}, presented as a report.",
)

task2 = Task(
  agent=writer,
  description="""Using the insights provided, develop an engaging blog
  post that highlights the most significant facts and differences between open-source LLMs and closed-source LLMs.
  Your post should be informative yet accessible, catering to a tech-savvy audience.
  Make it sound simple, and avoid complex words so it doesn't sound AI generated.""",
  expected_output="""A article containing a minimum of 4 paragraphs. contains no more than 2500 words but no less than 1500 words.
  The final output will not contain any extra fluff like "Paragraph 1:" or any action the writer should do.""",
)

crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2, # You can set it to 1 or 2 for different logging levels
)

result = crew.kickoff()