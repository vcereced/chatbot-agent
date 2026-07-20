from shared.domain.conversation import Conversation
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)


class MemoryService:

    def __init__(self):

        self.storage: dict[str, Conversation] = {}

    def get(self, conversation_id: str) -> Conversation:

        logger.info(f"Retrieving conversation with ID: {conversation_id}")

        if conversation_id not in self.storage:

            raise ConversationNotFound(conversation_id)

        return self.storage[conversation_id]

    def save(self, conversation: Conversation) -> None:

        logger.info(f"Saving conversation with ID: {conversation.id}")

        self.storage[conversation.id] = conversation