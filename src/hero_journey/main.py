#!/usr/bin/env python
from pathlib import Path
import asyncio, os
from typing import List, Optional

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start

from hero_journey.crews.astrology_outline_v3.astrology_outline import AstrologyOutline
from hero_journey.crews.narrative_outline.narrative_outline import NarrativeOutline
from hero_journey.crews.book_writer.book_writer import BookWriter

from hero_journey.types import (
    Chapter,
    ChapterOutline,
    CharacterProfile
)


class BookState(BaseModel):
    title: str = "El viaje del héroe"
    book: List[Chapter] = []
    book_outline: List[ChapterOutline] = [] 
    character_profile: Optional[CharacterProfile] = None


class BookFlow(Flow[BookState]):

    @start()
    def generate_astrology_outline(self):
        print("Generating astrology outline")

        # Define el path absoluto aquí
        file_path = "C:\\Users\\pc\\Documents\\Projects\\astroFlow\\hero_journey\\src\\hero_journey\\data\\kai_natal_chart.json"

        if not os.path.exists(file_path):
            print(f"El archivo no existe en: {file_path}")
            raise FileNotFoundError(f"El archivo no se encuentra en {file_path}")
        else:
            print(f"Archivo encontrado en: {file_path}")

        # Ejecuta la tarea con el `file_path` como entrada
        character_profile = AstrologyOutline().crew().kickoff(
            inputs={"file_path": file_path}  # Pasa el path absoluto
        ).pydantic
        self.state.character_profile = character_profile
'''
    @listen(generate_astrology_outline)
    def generate_narrative_outline(self):
        print("Generating narrative outline")
        character_profile = self.state.character_profile
        print(f"Using character profile with name: {character_profile.name}")
        
        output = NarrativeOutline().crew().kickoff(
            inputs={
                "character_profile": character_profile.model_dump()
            }
        )
    
        chapters = output["chapters"]
        print("Chapters: ", chapters)
        
        self.state.book_outline = chapters
        
        return output

    @listen(generate_narrative_outline)
    async def write_book(self):
        print("Writing Book Chapters")
        tasks = []
        
        async def write_single_chapter(chapter_outline):
            character_profile = self.state.character_profile
            print(f"Writing chapter for character: {character_profile.name}")
            
            output = (
                BookWriter()
                .crew()
                .kickoff(
                    inputs={ 
                        "character_profile": character_profile.model_dump(),
                        "chapter_title": chapter_outline.title,
                        "chapter_description": chapter_outline.description,
                        "book_outline": [
                            chapter_outline.model_dump()
                            for chapter_outline in self.state.book_outline
                        ],
                    }
                )
            )
            title = output["title"]
            content = output["content"]
            chapter = Chapter(title=title, content=content)
            return chapter

            
        for chapter_outline in self.state.book_outline:
            print(f"Writing chapter: {chapter_outline.title}")
            print(f"Description: {chapter_outline.description}")
            
            task = asyncio.create_task(write_single_chapter(chapter_outline))
            tasks.append(task)
        
        chapters = await asyncio.gather(*tasks)
        print("Newly written chapters: ", chapters)
        self.state.book.extend(chapters)
        
        print("Book Chapters: ", self.state.book)

    @listen(write_book)
    async def join_and_save_chapter(self):
        print("Joining and saving chapters")
        book_content = ""
        
        expected_order = [
            "El Mundo Ordinario",
            "La Llamada a la Aventura",
            "Encuentro con el Mentor",
            "Cruce del Umbral",
            "Pruebas, Aliados, Enemigos",
            "Enfoque a la Cueva Más Profunda",
            "La Prueba",
            "El Regreso"
        ]

        sorted_chapters = sorted(
            self.state.book,
            key=lambda x: expected_order.index(x.title)
        )
        
        for chapter in sorted_chapters:
            print(f"Processing chapter: {chapter.title}")
            book_content += f"# {chapter.title}\n\n"
            book_content += f"{chapter.content}\n\n"
            
        book_title = self.state.title
        filename = f"{book_title.replace(' ', '_')}.md"
        
        with open(filename, "w", encoding="utf-8") as file:
            file.write(book_content)
            
        print(f"Book saved as {filename}")
'''

def kickoff():
    book_flow = BookFlow()
    book_flow.kickoff()


def plot():
    book_flow = BookFlow()
    book_flow.plot()


if __name__ == "__main__":
    kickoff()
