from app.schemas import GenerateResponse
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)


class LLMService:

    def generate(self, prompt: str) -> GenerateResponse:

        logger.info(f"Generating LLM response for prompt: {prompt}")
        return GenerateResponse(text=f"LLM recibido: {prompt}")