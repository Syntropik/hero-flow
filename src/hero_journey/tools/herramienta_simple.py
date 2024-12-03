from typing import Type
from crewai.tools import BaseTool, tool
from pydantic import BaseModel, Field

class SimpleToolInput(BaseModel):
    """Esquema de entrada para la herramienta de prueba."""
    message: str = Field(..., description="Un mensaje de prueba para verificar el flujo de datos.")

class SimpleToolOutput(BaseModel):
    """Salida esperada de la herramienta simple."""
    processed_message: str

class SimpleTool(BaseTool):
    """Herramienta de prueba para verificar si los datos se transmiten correctamente."""
    name: str = "simple_tool"
    description: str = "Herramienta de prueba para verificar el paso de variables."
    args_schema: Type[BaseModel] = SimpleToolInput

    def _run(self, message: str) -> str:
        print(f"Mensaje recibido en la herramienta: {message}")
        return {"processed_message": f"Mensaje procesado: {message}"}
