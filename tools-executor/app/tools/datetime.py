from datetime import datetime

from app.tools.base_tool import BaseTool

from shared.domain.tooldefinition import (
    ToolDefinition,
    ParameterDefinition,
)


class DateTimeTool(BaseTool):

    def get_definition(self) -> ToolDefinition:

        return ToolDefinition(
            name="datetime",
            description="Returns the current date and time.",
            parameters=ParameterDefinition(
                type="object",
                properties={},
                required=[],
            ),
        )

    def execute(self, arguments: dict[str, object]) -> object:

        return datetime.now().isoformat()