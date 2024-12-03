# types.py
from typing import List
from pydantic import BaseModel

class SLAInput(BaseModel):
    nombre: str
    age: str
    sol: str
    luna: str
    ascendente: str

class SLAOutput(BaseModel):
    name: str
    age: str
    key_positions: List[str]

class StrengthsOutput(BaseModel):
    strengths: List[str]

class ConflictsOutput(BaseModel):
    conflicts: List[str]


class NatalChartInput(BaseModel):
    name: str 
    date: str
    time: str
    longitude: float
    latitude: float

class AstrologicalProfile(BaseModel):
    name: str
    age: str
    birth_location: str
    key_positions: List[str]
    strengths: List[str]
    confliicts: List[str]
    develompent_arc: List[str]
    
# Mike nuevo Type
class AstrologicalCharacterProfile(BaseModel):
    name: str
    personality_traits: List[str]
    background: str
    motivations: List[str]
    conflicts: List[str]
    character_arc: str
    relationships: List[str]


class CharacterProfile(BaseModel):
    name: str
    personality_traits: List[str]
    background: str
    motivations: List[str]
    conflicts: List[str]
    character_arc: str
    relationships: List[str]

class ChapterOutline(BaseModel):
    title: str
    description: str

class Chapter(BaseModel):
    title: str
    content: str
    # TODO: add reflection

class BookOutline(BaseModel):
    chapters: List[ChapterOutline]  
    

