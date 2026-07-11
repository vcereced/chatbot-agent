from pydantic import BaseModel
from shared.commom.ToolCall import ToolCall


class ExecuteToolRequest(BaseModel):

    tool_call : ToolCall


class ExecuteToolResponse(BaseModel):

    result: object