from app.tools.echo import EchoTool
from app.tools.calculator import CalculatorTool
form app.tools.datetime import DatetimeTool


class ToolRegistry:

    def __init__(self):

        self._tools: dict[str, BaseTool] = {}

        self.register(EchoTool())
        self.register(CalculatorTool())
        self.register(DatetimeToolt())

     def register(self, tool: BaseTool) -> None:

        definition = tool.get_definition()

        self.tools[definition.name] = tool

    def get(self, name):

        if name not in self._tools:

            raise ValueError(f"Tool '{name}' is not registered.")

        return self._tools[name]

    def get_definitions(self) -> list[ToolDefinition]:

        return [
            tool.get_definition()
            for tool in self.tools.values()
        ]