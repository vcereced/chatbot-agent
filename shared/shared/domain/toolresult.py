from pydantic import BaseModel


class ToolResult(BaseModel):

    tool_name: str
    
    result: object