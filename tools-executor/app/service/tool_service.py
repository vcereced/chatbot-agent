from shared.tools.execute import ExecuteToolResponse, ExecuteToolRequest
from shared.domain.toolcall import ToolCall
from shared.domain.toolresult import ToolResult
from app.registry.tool_registry import ToolRegistry
from shared.logging.logger import configure_logging
from shared.domain.tooldefinition import ToolDefinition

logger = configure_logging(__name__)


class ToolService:

    def __init__(self):

        self.registry = ToolRegistry()

    def execute(self, toolcall: ToolCall) -> ToolResult:

        logger.info(f"Executing tool: {toolcall.name} with arguments: {toolcall.arguments}")
        tool = self.registry.get(toolcall.name)

        result = tool.execute(toolcall.arguments)
        logger.info(f"Tool execution result: {result}")
        
        return ToolResult(tool_name=tool_call.name, result=result)
    
    def list_tools(self) -> list[ToolDefinition]:
        logger.info("Listing available tools")
        tools = self.registry.definitions()
        logger.info(f"Available tools: {tools}")
        return tools