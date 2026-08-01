from pydantic import BaseModel
from typing import Literal

class Message(BaseModel):

    role: Literal[
        "system",
        "user",
        "assistant",
        "tool"
    ]

    content: str | None = None

    tool_name: str | None = None