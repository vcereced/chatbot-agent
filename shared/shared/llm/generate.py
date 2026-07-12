from pydantic import BaseModel
from shared.domain.message import Message
from shared.domain.generate_result import GenerateResult


class GenerateRequest(BaseModel):
    messages: list[Message]


class GenerateResponse(BaseModel):
    result: GenerateResult