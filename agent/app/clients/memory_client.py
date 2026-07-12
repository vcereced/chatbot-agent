from app.clients.base_client import BaseClient
from shared.domain.conversation import Conversation
from app.config import config

class MemoryClient(BaseClient):

    def get(self, conversation_id: str) -> Conversation:

        response = self.post(
            f"{config.MEMORY_URL}/conversation/get",
            GetConversationRequest(
                conversation_id=conversation_id,
            ),
            GetConversationResponse,
        )

        return response.conversation
    
    def save(
        self,
        conversation: Conversation,
    ) -> None:

        self.post(
            f"{config.MEMORY_URL}/conversation/save",
            SaveConversationRequest(
                conversation=conversation,
            ),
            SaveConversationResponse,
        )