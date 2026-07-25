from shared.domain.conversation import Conversation
from shared.logging.logger import configure_logging
from uuid import uuid4

logger = configure_logging(__name__)


class MemoryService:

    def __init__(self):

        self.storage: dict[str, Conversation] = {}

    def get_or_create(self, conversation_id: str | None) -> Conversation:

        logger.info(f"Retrieving conversation with ID: {conversation_id}")

        if conversation_id is None:
            conversation = Conversation(
                id=str(uuid4()),
                messages=[],
            )
        else:
            conversation = self.storage.get(conversation_id)

            if conversation is None:
                conversation = Conversation(
                    id=conversation_id,
                    messages=[],
                )

        self.storage[conversation.id] = conversation

        return conversation

    def save(self, conversation: Conversation):

        logger.info(f"Saving conversation with ID: {conversation.id}")

        self.storage[conversation.id] = conversation
        

        return True