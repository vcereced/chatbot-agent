from app.tools.base import BaseTool
from pydantic import BaseModel
from shared.domain.tooldefinition import ToolDefinition

class EchoTool(BaseTool):

    def get_definition(self) -> ToolDefinition:

        return ToolDefinition(
            name="echo",
            description="Returns the received text.",
            parameters={
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string"
                    }
                },
                "required": [
                    "text"
                ]
            }
        )

    def execute(self, arguments:dict[str, object]) -> str:

        return arguments.text