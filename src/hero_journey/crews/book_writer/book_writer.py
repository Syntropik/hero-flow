from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
from hero_journey.types import (
    BookOutline,
    Chapter
)

@CrewBase
class BookWriter():
    """BookWriter crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    llm = ChatOpenAI(model="gpt-4o-mini")

    @agent
    def creative_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['creative_writer'],
            llm=self.llm,
            verbose=True
        )


    @task
    def write_chapter(self) -> Task:
        return Task(
            config=self.tasks_config['write_chapter'],
            input_pydantic=BookOutline,
            output_pydantic=Chapter
        )



    @crew
    def crew(self) -> Crew:
        """Creates the BookWriter crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
