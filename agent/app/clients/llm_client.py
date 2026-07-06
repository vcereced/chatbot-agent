from app.clients.base_client import BaseClient
from app.config import LLM_URL
from app.schemas import ChatResponse
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)


class LLMClient(BaseClient):

    def generate(self, prompt: str) -> ChatResponse:

        logger.info(f"Generating LLM response for prompt: {prompt}")
        data = self.post(
            f"{LLM_URL}/generate",
            {
                "prompt": prompt
            }
        )
        logger.info(f"Received response from LLM: {data}")
        return ChatResponse(
            response=data["text"]
        )