from app.clients.llm_client import LLMClient
from app.schemas.chat import ChatResponse


class ChatService:

    def __init__(self):

        self.llm = LLMClient()

    def chat(self, message: str) -> ChatResponse:

        answer = self.llm.generate(message)

        return ChatResponse(
            response=answer
        )