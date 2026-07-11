class ToolCall(BaseModel):

    name: str

    arguments: dict[str, object]