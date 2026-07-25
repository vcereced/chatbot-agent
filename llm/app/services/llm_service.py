from app.schemas import GenerateResponse, GenerateRequest
from shared.domain.toolcall import ToolCall
from shared.domain.message import Message
from shared.domain.generate_result import GenerateResult
from shared.logging.logger import configure_logging
from app.providers.ollama_provider import OllamaProvider
from shared.domain.conversation import Conversation
from shared.domain.tooldefinition import ToolDefinition

logger = configure_logging(__name__)


class LLMService:

    def __init__(self):

        self.llmprovider = OllamaProvider()

    def generate(self, messages: list[Message], tools: list[ToolDefinition]) -> GenerateResult:
        
        logger.info("XXXXXXXXXXX")
        logger.info(f"llm_service: {messages}")
        result = self.llmprovider.generate(
            messages,
            tools,
        )
        logger.debug(result)
        logger.info(result.model_dump())

        return result