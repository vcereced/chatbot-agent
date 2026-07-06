from app.clients.llm_client import LLMClient
from app.schemas import ChatResponse
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)


class ChatService:

    def __init__(self):

        self.llm = LLMClient()
        logger.info("ChatService initialized with LLMClient.")

    def chat(self, message: str) -> ChatResponse:
        logger.info(f"Processing chat message: {message}")
        return self.llm.generate(message)

        