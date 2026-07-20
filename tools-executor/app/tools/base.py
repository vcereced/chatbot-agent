from abc import ABC, abstractmethod
from shared.domain.tooldefinition import ToolDefinition


class BaseTool(ABC):
    
    @abstractmethod
    def get_definition(self) -> ToolDefinition:
        """Descripción de la herramienta."""
        pass

    @abstractmethod
    def execute(self, arguments: dict[str, object]) -> object:
        pass