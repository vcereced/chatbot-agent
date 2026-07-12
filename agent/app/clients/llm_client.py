from app.clients.base_client import BaseClient
from app.config import config
from app.schemas import GenerateRequest, GenerateResponse
from shared.logging.logger import configure_logging
from shared.domain.conversation import Conversation
from shared.llm.generate import GenerateResult

logger = configure_logging(__name__)

class LLMClient(BaseClient):

    def generate(self, conversation: Conversation) -> GenerateResult:

        logger.info("Received response from LLM")

        request = GenerateRequest(messages=conversation.messages)
        response = self.post(f"{config.LLM_URL}/generate", request, GenerateResponse)

        return response.result
