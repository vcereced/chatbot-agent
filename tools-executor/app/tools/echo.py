from app.tools.base import BaseTool
from pydantic import BaseModel

class EchoArguments(BaseModel):
    text: str

class EchoTool(BaseTool):

    @property
    def name(self):

        return "echo"

    def execute(self, arguments):

        args = EchoArguments.model_validate(arguments)
        return args.text
        # return "soy el echo"