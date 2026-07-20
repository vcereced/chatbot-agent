from app.tools.base_tool import BaseTool

from shared.domain.tooldefinition import (
    ToolDefinition,
    ParameterDefinition,
    PropertyDefinition,
)


class CalculatorTool(BaseTool):

    def get_definition(self) -> ToolDefinition:

        return ToolDefinition(
            name="calculator",
            description="Evaluate a mathematical expression.",
            parameters=ParameterDefinition(
                type="object",
                properties={
                    "expression": PropertyDefinition(
                        type="string",
                        description="Mathematical expression to evaluate.",
                    )
                },
                required=["expression"],
            ),
        )

    def execute(self, arguments: dict[str, object]) -> object:

        expression = arguments["expression"]

        return eval(
            expression,
            {"__builtins__": {}},
            {},
        )