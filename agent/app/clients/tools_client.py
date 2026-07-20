from app.clients.base_client import BaseClient
from app.config import config
from app.schemas import ExecuteToolRequest, ExecuteToolResponse
from shared.logging.logger import configure_logging
from shared.domain.toolcall import ToolCall
from shared.domain.toolresult import ToolResult


logger = configure_logging(__name__)

class ToolsClient(BaseClient):

    def __init__(self):
        super().__init__()
        self._tools = None     

    def execute(self, tool_call: ToolCall) -> ToolResult:

        logger.info(f"Sending request to tool-executor: {tool_call.name}    with arguments: {tool_call.arguments}   ")
        response = self.post(
            f"{config.TOOLS_URL}/execute",
            ExecuteToolRequest(tool_call=tool_call),
            ExecuteToolResponse,
        )

        return response.tool_result

    def list_tools(self) -> list[ToolDefinition]:

        if self._tools is None:
            self.load_tools()
        return self._tools

    def load_tools(self):
    
        try:
            response = self.get("/tools", ListToolsResponse)
            self._tools = response.tools
    
        except HttpException as e:

            if e.status_code == 404:
                raise ToolNotFound(tool_name)

            raise
    
