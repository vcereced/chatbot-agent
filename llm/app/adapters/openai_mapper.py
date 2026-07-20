from json import loads

from shared.domain.conversation import Conversation
from shared.domain.toolcall import ToolCall
from shared.domain.tooldefinition import ToolDefinition
from shared.llm.generate import GenerateResult


class OpenAIMapper:

    @staticmethod
    def to_messages(conversation: Conversation) -> list[dict]:

        messages = []

        for message in conversation.messages:

            if message.role == "tool":

                messages.append({
                    "role": "tool",
                    "content": message.content,
                    "name": message.tool_name,
                })

            else:

                messages.append({
                    "role": message.role,
                    "content": message.content,
                })

        return messages

    @staticmethod
    def to_tools(tools: list[ToolDefinition]) -> list[dict]:

        return [
            {
                "type": "function",
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.parameters.model_dump(),
            }
            for tool in tools
        ]

    @staticmethod
    def to_generate_result(response) -> GenerateResult:

        # Si el modelo quiere ejecutar una herramienta
        for item in response.output:

            if item.type == "function_call":

                return GenerateResult(
                    tool_call=ToolCall(
                        name=item.name,
                        arguments=loads(item.arguments),
                    )
                )

        # Si devuelve texto
        return GenerateResult(
            text=response.output_text,
        )