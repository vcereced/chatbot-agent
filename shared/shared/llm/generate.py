from pydantic import BaseModel
from shared.schemas import ChatRequest, ChatResponse
from shared.commom.ToolCall import ToolCall


class GenerateRequest(BaseModel):
    prompt: str


class GenerateResponse(BaseModel):
    text: str | None = None

    tool_call: ToolCall | None = None