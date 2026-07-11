from shared.tools.execute import ExecuteToolResponse, ExecuteToolRequest
from app.registry.tool_registry import ToolRegistry


class ToolService:

    def __init__(self):

        self.registry = ToolRegistry()

    def execute(self, request: ExecuteToolRequest) -> ExecuteToolResponse:

        tool = self.registry.get(request.tool)

        result = tool.execute(request.arguments)

        return ExecuteToolResponse(result = result)   