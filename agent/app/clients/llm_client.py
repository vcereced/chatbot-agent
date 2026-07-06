from app.clients.base_client import BaseClient
from app.config import LLM_URL
from app.schemas import ChatResponse


class LLMClient(BaseClient):

    def generate(self, prompt: str) -> ChatResponse:

        data = self.post(
            f"{LLM_URL}/generate",
            {
                "prompt": prompt
            }
        )

        return ChatResponse(
            response=data["text"]
        )