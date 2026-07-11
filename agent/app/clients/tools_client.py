from app.clients.base_client import BaseClient
from app.config import config
from app.schemas import ExecuteToolRequest, ExecuteToolResponse
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)

class ToolsClient(BaseClient):

    def execute(self, request: ExecuteToolRequest) -> ExecuteToolResponse:

        logger.info(f"Sending request to tool-executor: {request.tool} with arguments: {request.arguments}")
        return self.post(f"{config.TOOLS_URL}/execute", request, ExecuteToolResponse)


