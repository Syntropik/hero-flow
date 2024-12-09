
import os, re
from crewai import Agent, Crew, Process, Task 
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import JSONSearchTool, FileReadTool
from hero_journey.tools.customFileReadTool import CustomFileReadTool
from langchain_openai import ChatOpenAI
from hero_journey.types import (
    SLAInput,
    SLAOutput,
    StrengthsOutput,
    ConflictsOutput,
    AstrologicalProfile,
    CharacterProfile,
    ArcOutput,
    MentorOutput,
    SymbolismOutput,
    EnvironmentOutput,
    IntegrationOutput,
    ReviewOutput,
    FinalOutput
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
        file_path = "C:\\Users\\pc\\Documents\\Projects\\astroFlow\\hero_journey\\src\\hero_journey\\data\\SLA.json"
        print(f"Looking for file at: {file_path}")

        cleaned_file_path = "C:\\Users\\pc\\Documents\\Projects\\astroFlow\\hero_journey\\src\\hero_journey\\data\\cleaned_SLA.json"

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
    '''
    @agent 
    def story_consultant(self) -> Agent:
        file_path = "C:\\Users\\pc\\Documents\\Projects\\astroFlow\\hero_journey\\src\\hero_journey\\data\\SLA.json"
        file_read_tool = FileReadTool(file_path=file_path)
        return Agent(
            config=self.agents_config['story_consultant'],
            tools=[file_read_tool],
            verbose=True
        )
    @agent 
    def content_reviewer(self) -> Agent:
        file_path = "C:\\Users\\pc\\Documents\\Projects\\astroFlow\\hero_journey\\src\\hero_journey\\data\\SLA.json"
        file_read_tool = FileReadTool(file_path=file_path)
        return Agent(
            config=self.agents_config['content_reviewer'],
            tools=[file_read_tool],
            verbose=True
        )
    @agent 
    def narrative_integrator(self) -> Agent:
        file_path = "C:\\Users\\pc\\Documents\\Projects\\astroFlow\\hero_journey\\src\\hero_journey\\data\\SLA.json"
        file_read_tool = FileReadTool(file_path=file_path)
        return Agent(
            config=self.agents_config['narrative_integrator'],
            tools=[file_read_tool],
            verbose=True
        )
    @agent 
    def output_preparer(self) -> Agent:
        file_path = "C:\\Users\\pc\\Documents\\Projects\\astroFlow\\hero_journey\\src\\hero_journey\\data\\SLA.json"
        file_read_tool = FileReadTool(file_path=file_path)
        return Agent(
            config=self.agents_config['output_preparer'],
            tools=[file_read_tool],
            verbose=True
        )
    '''
   
    # Mike nueva Task
    @task
    def sla_astrological_profile(self) -> Task:
        return Task(
            config=self.tasks_config['sla_astrological_profile'],
            input_pydantic=SLAInput,
            output_pydantic=SLAOutput,
        )
    @task
    def fortalezas_astrological_profile(self) -> Task:
        return Task(
            config=self.tasks_config['fortalezas_astrological_profile'],
            input_pydantic=SLAOutput,
            output_pydantic=StrengthsOutput,
        )
    @task
    def retos_astrological_profile(self) -> Task:
        return Task(
            config=self.tasks_config['retos_astrological_profile'],
            input_pydantic=StrengthsOutput,
            output_pydantic=ConflictsOutput,
        )
    '''
    @task
    def arc_astrological_profile(self) -> Task:
        return Task(
            config=self.tasks_config['arc_astrological_profile'],
            input_pydantic=ConflictsOutput,
            output_pydantic=ArcOutput,
        )
    
    @task
    def environment_design(self) -> Task:
        return Task(
            config=self.tasks_config['environment_design'],
            input_pydantic=ArcOutput,
            output_pydantic=EnvironmentOutput,
        )
    
    @task
    def character_mentor_design(self) -> Task:
        return Task(
            config=self.tasks_config['character_mentor_design'],
            input_pydantic=EnvironmentOutput,
            output_pydantic=MentorOutput,
        )
    
    @task
    def symbolism_design(self) -> Task:
        return Task(
            config=self.tasks_config['symbolism_design'],
            input_pydantic=MentorOutput,
            output_pydantic=SymbolismOutput,
        )
    
    @task
    def integrate_elements(self) -> Task:
        return Task(
            config=self.tasks_config['integrate_elements'],
            input_pydantic=SymbolismOutput,
            output_pydantic=IntegrationOutput,
        )
    
    @task
    def final_review(self) -> Task:
        return Task(
            config=self.tasks_config['final_review'],
            input_pydantic=IntegrationOutput,
            output_pydantic=ReviewOutput,
        )


    @task
    def prepare_final_output(self) -> Task:
        return Task(
            config=self.tasks_config['prepare_final_output'],
            input_pydantic=ReviewOutput,
            output_pydantic=FinalOutput,
        )
    '''
    @crew
    def crew(self) -> Crew:
        """Creates the AstrologyOutline crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True
        )