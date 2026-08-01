from shared.agent.chat import ChatRequest, ChatResponse
from shared.llm.generate import GenerateRequest, GenerateResponse
from shared.domain.message import Message
from shared.domain.toolresult import ToolResult
from shared.logging.logger import configure_logging

from app.clients.llm_client import LLMClient
from app.clients.tools_client import ToolsClient
from app.clients.memory_client import MemoryClient
from shared.domain.chatresult import ChatResult
from shared.domain.tooldefinition import ToolDefinition

logger = configure_logging(__name__)
        

class ChatService:

    def __init__(self):

        self.memory = MemoryClient()
        self.llm = LLMClient()
        self.tools = ToolsClient()
        

    async def chat(self, conversation_id: str | None, message: str) -> ChatResult:

        logger.info(f"Processing chat id: {conversation_id}, message: {message}")
        conversation = await self.memory.get_or_create(conversation_id)

        conversation.messages.append(
            Message(
                role="user",
                content=message,
            )
        )

        logger.info("Getting list of tools")
        tools = await self.tools.list_tools()

        logger.info(f"Generating LLM response, {conversation}")
        result = await self.llm.generate(conversation, tools)

        if result.tool_call:

            # Guardar la llamada a la herramienta realizada por el LLM
            conversation.messages.append(
                Message(
                    role="assistant",
                    tool_call=result.tool_call,
                )
            )

            logger.info(f"Executing tool {result.tool_call}")

            tool_result = await self.tools.execute(result.tool_call)

            logger.info(f"Executing tool {tool_result}")

            # Guardar el resultado de la herramienta
            conversation.messages.append(
                Message(
                    role="tool",
                    tool_name=tool_result.tool_name,
                    content=str(tool_result.result),
                )
            )

            logger.info("generating llm with tool")

            result = await self.llm.generate(conversation, None)

        conversation.messages.append(
            Message(
                role="assistant",
                content=result.text,
            )
        )

        logger.info("Saving conversation")

        await self.memory.save(conversation)
        logger.info(conversation)
        return ChatResult(
            conversation_id=conversation.id,
            response=result.text,
        )