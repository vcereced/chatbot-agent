from app.tools.echo import EchoTool


class ToolRegistry:

    def __init__(self):

        self._tools = {}

        self.register(EchoTool())

    def register(self, tool):

        self._tools[tool.name] = tool

    def get(self, name):

        if name not in self._tools:

            raise ValueError(f"Tool '{name}' is not registered.")

        return self._tools[name]