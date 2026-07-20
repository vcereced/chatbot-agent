from shared.agent.chat import ChatRequest, ChatResponse
from shared.llm.generate import GenerateRequest, GenerateResponse
from shared.domain.message import Message
from shared.domain.toolresult import ToolResult
from shared.logging.logger import configure_logging

from app.clients.llm_client import LLMClient
from app.clients.tools_client import ToolsClient
from app.clients.memory_client import MemoryClient
from app.schemas import ToolDefinition
from shared.domain.chatresult import ChatResult

logger = configure_logging(__name__)
        

class ChatService:

    def __init__(self):

        self.memory = MemoryClient()
        self.llm = LLMClient()
        self.tools = ToolsClient()
        

    def chat(self, conversation_id: str | None, message: str) -> ChatResult:

        logger.info(f"Processing chat id: {conversation_id}, message: {message}")
        conversation = self.memory.get_or_create(conversation_id) #call to MEMORY CLIENT 

        conversation.messages.append(
            Message(
                role="user",
                content=message,
            )
        )
        logger.info("Getting list of tools")
        tools = self.tools.list_tools() #->list[ToolDefinition] call to TOOLS CLIENT
        logger.info("Generating LLM response")
        result = self.llm.generate(conversation, tools) #->GenerateResult call to LLM CLIENT

        if result.tool_call:#if the LLM response includes a tool call, execute the tool and get the result
            logger.info(f"Executing tool {result.tool_call}")
            tool_result = self.tools.execute(result.tool_call) #->ToolResult #call to TOOLS CLIENT

            conversation.messages.append(
                Message(
                    role="tool",
                    tool_name=tool_result.tool_name,
                    content=str(tool_result.result),
                )
            )
            logger.info("generating llm with tool")
            result = self.llm.generate(conversation.messages) #->GenerateResult #call to LLM CLIENT

        conversation.messages.append(
            Message(
                role="assistant",
                content=result.text,
            )
        )
        logger.info("Saving conversation")
        self.memory.save(conversation) #->NONE #call to MEMORY CLIENT

        return ChatResult(
            conversation_id=conversation.id,
            response=result.text,
        )