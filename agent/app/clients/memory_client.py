from app.clients.base_client import BaseClient
from shared.domain.conversation import Conversation
from app.config import config
from shared.memory.conversation import GetConversationRequest, GetConversationResponse, SaveConversationRequest, SaveConversationResponse
from shared.errors import ConversationNotFound

class MemoryClient(BaseClient):

    def get(self, conversation_id: str ) -> Conversation:
        try:
            response = self.post(
                f"{config.MEMORY_URL}/conversation/get",
                GetConversationRequest(
                    conversation_id=conversation_id,
                ),
                GetConversationResponse,
            )

            return response.conversation

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise ConversationNotFound(conversation_id)
            raise
    
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

    def get_or_create(conversation_id: str | None) -> Conversation:

        if conversation_id is None:
            return Conversation(
                id=str(uuid4()),
                messages=[],
                )

        try:
            return self.get(id)

        except HttpException as e:

            if e.status_code == 404:
                return Conversation(
                    id=str(uuid4()),
                    messages=[],
                    )

            raise