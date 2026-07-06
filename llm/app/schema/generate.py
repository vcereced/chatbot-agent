from pydantic import BaseModel
from shared.schemas import ChatRequest, ChatResponse


class GenerateRequest(BaseModel):
    prompt: str


class GenerateResponse(BaseModel):
    text: str