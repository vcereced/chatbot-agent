from app.clients.llm_client import LLMClient
from app.schemas import ChatResponse


class ChatService:

    def __init__(self):

        self.llm = LLMClient()

    def chat(self, message: str) -> ChatResponse:

        return self.llm.generate(message)

        