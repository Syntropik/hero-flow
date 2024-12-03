
import os, re
from crewai import Agent, Crew, Process, Task 
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import JSONSearchTool, FileReadTool
from hero_journey.tools.customFileReadTool import CustomFileReadTool
from langchain_openai import ChatOpenAI
from hero_journey.types import (
    AstrologicalProfile,
    CharacterProfile
)


@CrewBase
class AstrologyOutline:
    """AstrologyOutline crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    llm = ChatOpenAI(model="gpt-4o-mini")

    
# Mike nuevo Agent 
    @agent
    def astrology_interpreter(self) -> Agent:
        file_path = "C:\\Users\\pc\\Documents\\Projects\\astroFlow\\hero_journey\\src\\hero_journey\\data\\kai_natal_chart.json"
        print(f"Looking for file at: {file_path}")

        cleaned_file_path = "C:\\Users\\pc\\Documents\\Projects\\astroFlow\\hero_journey\\src\\hero_journey\\data\\cleaned_natal_chart.json"

        with open(file_path, "r", encoding="utf-8", errors="replace") as file:
            content = file.read()

        # Reemplazar caracteres problemáticos
        content = re.sub(r"[^\x00-\x7F]+", " ", content)  # Sustituye caracteres no ASCII por espacio.

        # Guardar el archivo limpio
        with open(cleaned_file_path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"Archivo limpiado y guardado en: {cleaned_file_path}")

        # Inicializar la herramienta con la ruta del archivo
        file_read_tool = FileReadTool(file_path=cleaned_file_path)
        #file_read_tool = CustomFileReadTool()
        return Agent(
            config=self.agents_config['astrology_interpreter'],
            tools=[file_read_tool],
            verbose=True
        )

    @agent 
    def story_consultant(self) -> Agent:
        return Agent(
            config=self.agents_config['story_consultant'],
            verbose=True
        )

    
# Mike nueva Task
    @task
    def create_astrological_profile(self) -> Task:
        return Task(
            config=self.tasks_config['create_astrological_profile'],
            input_pydantic=dict,
            output_pydantic=AstrologicalProfile,
        )

    @task
    def create_character_profile(self) -> Task:
        return Task(
            config=self.tasks_config['create_character_profile'],
            input_pydantic=AstrologicalProfile,
            output_pydantic=CharacterProfile,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AstrologyOutline crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True
        )