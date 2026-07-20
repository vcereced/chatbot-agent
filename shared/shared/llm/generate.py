from pydantic import BaseModel
from shared.domain.message import Message
from shared.domain.generate_result import GenerateResult
from shared.domain.tool_definition import ToolDefinition

class GenerateRequest(BaseModel):
    messages: Conversation
    
    tools: list[ToolDefinition]


class GenerateResponse(BaseModel):
    result: GenerateResult