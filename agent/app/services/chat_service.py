from shared.agent.chat import ChatRequest, ChatResponse
from shared.llm.generate import GenerateRequest, GenerateResponse
from shared.domain.message import Message
from shared.domain.toolresult import ToolResult
from shared.logging.logger import configure_logging

from app.clients.llm_client import LLMClient
from app.clients.tools_client import ToolsClient
from app.clients.memory_client import MemoryClient
from app.schemas import ToolDefinition


logger = configure_logging(__name__)
        

class ChatService:

    def __init__(self):

        self.memory = MemoryClient()
        self.llm = LLMClient()
        self.tools = ToolsClient()
        

    def chat(self, conversation_id: str, message: str) -> str:

        logger.info(f"Processing chat message: {request.message}")
        conversation = self.memory.get(conversation_id) #call to MEMORY CLIENT 

        conversation.messages.append(
            Message(
                role="user",
                content=message,
            )
        )
        tools = self.tools.list_tools() #->list[ToolDefinition] call to TOOLS CLIENT
        result = self.llm.generate(conversation, tools) #->GenerateResult call to LLM CLIENT

        if result.tool_call:#if the LLM response includes a tool call, execute the tool and get the result

            tool_result = self.tools.execute(result.tool_call) #->ToolResult #call to TOOLS CLIENT

            conversation.messages.append(
                Message(
                    role="tool",
                    tool_name=tool_result.tool_name,
                    content=str(tool_result.result),
                )
            )

            result = self.llm.generate(conversation.messages) #->GenerateResult #call to LLM CLIENT

        conversation.messages.append(
            Message(
                role="assistant",
                content=result.text,
            )
        )

        self.memory.save(conversation) #->NONE #call to MEMORY CLIENT

        return result.text