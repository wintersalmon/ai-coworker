from dotenv import load_dotenv
load_dotenv()

import agentops
agentops.init()

from crewai import Crew

# Create Tasks
from textwrap import dedent
from crewai import Task
def create_test_code_task(agent, requirement_spec):
    description = dedent(f"""\
        Write a Python script to test the following requirements. Make sure to use unittest framework in Python:
        
        requirements
        ------------
        {requirement_spec}

        Please include at least five test cases for each function. Also be sure to include edge cases.

        Your Final answer must be the full python code, only the python code and nothing else.
        """)
    expected_output = "Python test code"

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent
    )

def create_implmenet_code_task(agent, requirement_spec):
    description = dedent(f"""\
        Implement a Python function that meats requirements. Make sure that the code meats exisiting test code:
        
        requirements
        ------------
        {requirement_spec}

        Your Final answer must be the full python code, only the python code and nothing else.
        """)
    expected_output = "Python test code"

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent
    )


def create_append_document_task(agent, requirement_spec):
    description = dedent(f"""\
        Append documentation for the following Python functions using comments, explaining their purpose, parameters, return values, and any edge cases that should be considered. Also, provide short examples of usage:
        
        requirements
        ------------
        {requirement_spec}

        Your Final answer must be the full python code, only the python code and nothing else.
        """)
    expected_output = "Python test code"

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent
    )



# Create Agents
from textwrap import dedent
from crewai import Agent
from langchain_community.llms import Ollama

llm_model_for_code = Ollama(model="mixtral:8x7b")
# llm_model_for_code = Ollama(model="codellama:7b")

def create_senior_engineer_agent(self):
    return Agent(
        role='Senior Software Engineer',
        goal='Create software as needed',
        backstory=dedent("""\
            You are a Senior Software Engineer at a leading tech think tank.
            Your expertise in programming in python. and do your best to
            produce perfect code"""),
        allow_delegation=False,
        verbose=True,
        llm=llm_model_for_code
    )

print('-------------------------------')
print("## Welcome to the Crew")
print('-------------------------------')
with open('documents/othello-srs.md', 'r') as file:
    input_requirements = file.read()
    print(input_requirements)

senior_engineer_agent = create_senior_engineer_agent(self=None)

task_write_test_code = create_test_code_task(senior_engineer_agent, input_requirements)
task_implement_code = create_implmenet_code_task(senior_engineer_agent, input_requirements)
task_implement_documentation = create_append_document_task(senior_engineer_agent, input_requirements)

# Create Crew responsible for Copy
crew = Crew(
	agents=[
		senior_engineer_agent,
	],
	tasks=[
        task_write_test_code,
        # task_implement_code,
        # task_implement_documentation,
	],
	verbose=True
)

result_code = crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("final code:")
print(result_code)