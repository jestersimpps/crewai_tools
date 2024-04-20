from crewai import Agent, Crew, Process, Task
from langchain_community.llms import Ollama
from dotenv import load_dotenv
from reddit_scraper.reddit_scraper import reddit_scraper

# Load environment variables from .env file
load_dotenv()

# Models
OllamaDolphin = Ollama(model="dolphin-mistral")

tool_tester = Agent(
    role="CrewAi tool tester",
    goal="Test if the tool is working properly",
    backstory="""You are an agent that tests if the tool is working properly. Check if the tool you are provided with is working properly.""",
    verbose=True,
    history=True,
    tools=[reddit_scraper],
    llm=OllamaDolphin,
)


test = Task(
    description="""See if the tool that was provided is working properly""",
    expected_output="A report on the number of tries it took to get the tool to work properly. Also the different errors encountered",
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
