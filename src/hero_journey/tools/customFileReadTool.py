from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import os

class CustomFileReadToolInput(BaseModel):
    """Input schema for CustomFileReadTool."""
    file_path: str = Field(..., description="The absolute or relative path to the file to be read.")

class CustomFileReadTool(BaseTool):
    name: str = "custom_file_read_tool"
    description: str = (
        "Reads a file's content with UTF-8 encoding and returns its content as a string. "
        "Useful for handling JSON files with non-ASCII characters."
    )
    args_schema: Type[BaseModel] = CustomFileReadToolInput

    def _run(self, file_path: str) -> str:
        try:
            print(f"Tool está intentando leer el archivo en: {file_path}")
            if not os.path.exists(file_path):
                return f"Error: The file at path {file_path} was not found."
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return f"Error: The file at path {file_path} was not found."
        except UnicodeDecodeError as e:
            return f"Error: Failed to decode file content. Details: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"
