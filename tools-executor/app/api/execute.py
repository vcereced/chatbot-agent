from fastapi import APIRouter
from shared.tools.execute import ExecuteToolRequest, ExecuteToolResponse
from app.services.tool_service import ToolService

router = APIRouter()

service = ToolService()


@router.post("/execute", response_model=ExecuteToolResponse)
def execute(self, request: ExecuteToolRequest) -> ExecuteToolResponse:

    return service.execute(request)