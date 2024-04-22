from crewai import Agent, Crew, Process, Task
from langchain_community.llms import Ollama
from dotenv import load_dotenv
from reddit_scraper.reddit_scraper import reddit_scraper

# Load environment variables from .env file
load_dotenv()

tool = reddit_scraper

# Models
llm = Ollama(model="dolphin-llama3")

tool_tester = Agent(
    role="CrewAi tool tester",
    goal="Test if the " + tool.name + " is working properly",
    backstory="You are an agent that tests if the "
    + tool.name
    + " is working properly. Check if the "
    + tool.name
    + " you are provided with is working properly.",
    verbose=True,
    history=True,
    tools=[tool],
    llm=llm,
)


test = Task(
    description="See if the " + tool.name + " that is provided is working technically",
    expected_output="The number of tries it took to get the "
    + tool.name
    + " to work technically. If the tool is working properly, the output should be 1. If not, the output should be greater than 1 and the tool is not working with the current model.",
    agent=tool_tester,
)


crew = Crew(
    agents=[tool_tester],
    tasks=[
        test,
    ],
    verbose=2,
    process=Process.sequential,
)


result = crew.kickoff()

print("######################")
print(result)
