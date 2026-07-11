from app.clients.base_client import BaseClient
from app.config import config
from app.schemas import GenerateRequest, GenerateResponse, ChatRequest
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)

class LLMClient(BaseClient):

    def generate(self, prompt: ChatRequest) -> GenerateResponse:

        logger.info("Received response from LLM")
        return self.post(f"{config.LLM_URL}/generate", GenerateRequest(prompt=prompt.message), GenerateResponse)


