from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
from hero_journey.types import (
    CharacterProfile,
    BookOutline
)


@CrewBase
class NarrativeOutline():
    """NarrativeOutline crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    llm = ChatOpenAI(model="gpt-4o-mini")

    @agent
    def hero_journey_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['hero_journey_expert'],
            llm=self.llm,
            verbose=True
        )

    @task
    def hero_journey_outline(self) -> Task:
        return Task(
            config=self.tasks_config["hero_journey_outline"],
            input_pydantic=CharacterProfile,
            output_pydantic=BookOutline,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the NarrativeOutline crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )