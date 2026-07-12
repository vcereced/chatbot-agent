from fastapi import APIRouter
from shared.tools.execute import ExecuteToolRequest, ExecuteToolResponse
from app.service.tool_service import ToolService
from shared.domain.toolcall import ToolCall
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)

router = APIRouter()

service = ToolService()


@router.post("/execute", response_model=ExecuteToolResponse)
def execute(request: ExecuteToolRequest) -> ExecuteToolResponse:
    logger.info(f"Executing tool with request: {request.tool_call.name} and arguments: {request.tool_call.arguments}")
    
    tool_result = service.execute(request.tool_call)
   
    return ExecuteToolResponse(tool_result=tool_result)