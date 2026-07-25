from httpx import Client
from shared.domain.tooldefinition import ToolDefinition
from shared.domain.message import Message
from shared.domain.generate_result import GenerateResult
from shared.logging.logger import configure_logging
from app.adapters.ollama_mapper import OllamaMapper
from app.config import SYSTEM_PROMPT
import os

logger = configure_logging(__name__)

class OllamaProvider:

    def __init__(self):

        self.model = os.getenv("OLLAMA_MODEL")
        self.endpoint = os.getenv("OLLAMA_ENDPOINT")
        self.client = Client(
            base_url = os.getenv("OLLAMA_BASE_URL"),
            timeout = float(os.getenv("TIMEOUT", 300)),
        )

    def generate(
        self,
        messages: list[Message],
        tools: list[ToolDefinition],
    ) -> GenerateResult:

        logger.info("before to message XXXXXXXXXXX")
        logger.info(messages)

        messages_for_llm = [
            Message(role="system", content=SYSTEM_PROMPT),
            *messages,
            ]

        payload = {
            "model": self.model,
            "messages": OllamaMapper.to_messages(messages_for_llm),
            "tools": OllamaMapper.to_tools(tools),
            "stream": False,
        }

        logger.debug("OllamaProvider->OllamaMapper = ", payload)
        logger.info("XXXXXXXXXXX")
        logger.info(payload)

        try:
            response = self.client.post(
                self.endpoint,
                json=payload,
            )
            response.raise_for_status()

        except httpx.ConnectError:
            raise HTTPException(
                status_code=503,
                detail="Cannot connect to Ollama."
            )

        except httpx.TimeoutException:
            raise HTTPException(
                status_code=504,
                detail="Ollama request timed out."
            )

        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=e.response.status_code,
                detail=e.response.text,
            )
        logger.info("XXXXXXXXXXXXXXXXXX")
        logger.info(response.json())
        return OllamaMapper.to_generate_result(response.json())