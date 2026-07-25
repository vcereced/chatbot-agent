from app.tools.echo import EchoTool
from app.tools.calculator import CalculatorTool
from app.tools.datetime import DateTimeTool
from app.tools.base import BaseTool
from shared.domain.tooldefinition import ToolDefinition


class ToolRegistry:

    def __init__(self):
        self._tools: dict[str, BaseTool] = {}
        self.register(EchoTool())
        self.register(CalculatorTool())
        self.register(DateTimeTool())

    def register(self, tool: BaseTool) -> None:
        definition = tool.get_definition()
        self._tools[definition.name] = tool

    def get(self, name: str) -> BaseTool | None:
        """Retorna la herramienta o None si no existe para evitar lanzar excepciones en la búsqueda."""
        return self._tools.get(name)

    def get_definitions(self) -> list[ToolDefinition]:
        return [
            tool.get_definition()
            for tool in self._tools.values()
        ]