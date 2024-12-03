from typing import Type
from crewai.tools import BaseTool, tool
from hero_journey.types import NatalChartInput
from pydantic import BaseModel, Field
import requests, json


class NatalChartAPITool(BaseTool):
    """Herramienta personalizada que llama a una API para obtener datos astrológicos de la carta natal."""
    name: str = "natal_chart_api_tool"
    description: str = "Llama a una API para obtener datos astrológicos de la carta natal basados en los datos del usuario."
    args_schema: Type[BaseModel] = NatalChartInput

    def _run(self, name: str, date: str, time: str, longitude: float, latitude: float) -> str:
        print("input en herramienta", name, date, time, longitude, latitude)
        url = "http://128.140.48.28:8000/natal_chart"
        payload = {
            "name": name,
            "date": date,
            "time": time,
            "longitude": longitude,
            "latitude": latitude,
        }
        try:
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            return f"Error al llamar a la API: {e}"