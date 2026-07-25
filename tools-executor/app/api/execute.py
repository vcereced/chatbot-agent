from fastapi import APIRouter
from shared.tools.execute import ExecuteToolRequest, ExecuteToolResponse
from app.service.tool_service import ToolService
from shared.domain.toolcall import ToolCall
from shared.logging.logger import configure_logging
from shared.tools.list_tools import ListToolsResponse

logger = configure_logging(__name__)

router = APIRouter()

service = ToolService()


@router.post("/execute", response_model=ExecuteToolResponse)
async def execute(request: ExecuteToolRequest) -> ExecuteToolResponse:
    logger.info(f"Executing tool request: {request.tool_call.name}")
    
    tool_result = await service.execute(request.tool_call)
   
    return ExecuteToolResponse(tool_result=tool_result)

@router.get("/tools", response_model=ListToolsResponse)
def list_tools() -> ListToolsResponse:
    logger.info("GET /tools requested")
    tools = service.list_tools()
    return ListToolsResponse(tools=tools)