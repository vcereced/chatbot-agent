from app.clients.llm_client import LLMClient
from app.clients.tools_client import ToolsClient
from app.schemas import ChatResponse, ChatRequest, GenerateResponse
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)


class ChatService:

    def __init__(self):

        self.llm = LLMClient()
        self.tools = ToolsClient()
        # self.memory = MemoryClient()  # Assuming you have a MemoryClient for managing conversation history
        logger.info("ChatService initialized with LLMClient and ToolsClient.")

    def chat(self, request: ChatRequest) -> ChatResponse:
        logger.info(f"Processing chat message: {request.message}")
        
        llm_response: GenerateResponse = self.llm.generate(request)

        if llm_response.tool_call is None:
            logger.info(f"LLM response: {llm_response.text}")
            return ChatResponse(response = llm_response.text)
        else:
            tool_response = self.tools.execute(llm_response.tool_call)
            logger.info(f"Tool response: {tool_response.result}")
            return ChatResponse(response=tool_response.result)
       

        