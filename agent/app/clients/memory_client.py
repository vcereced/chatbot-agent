from app.clients.base_client import BaseClient
from shared.domain.conversation import Conversation
from app.config import config
from shared.memory.conversation import GetOrCreateConversationRequest, GetOrCreateConversationResponse, SaveConversationRequest, SaveConversationResponse
from shared.errors import ConversationNotFound
from fastapi import HTTPException
from uuid import uuid4
import httpx
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)


class MemoryClient(BaseClient):

    def get(self, conversation_id: str | None ) -> Conversation:
    
        response = self.post(
            f"{config.MEMORY_URL}/conversations/get_or_create",
            GetOrCreateConversationRequest(
                conversation_id=conversation_id,
            ),
            GetOrCreateConversationResponse,
        )

        return response.conversation

    
    def save(
        self,
        conversation: Conversation,
    ) -> None:

        self.post(
            f"{config.MEMORY_URL}/conversations/save",
            SaveConversationRequest(
                conversation=conversation,
            ),
            SaveConversationResponse,
        )

    def get_or_create(self, conversation_id: str | None) -> Conversation:


        return self.get(conversation_id)
