from pydantic import BaseModel
from shared.shared.domain.conversation import Conversation

class ChatResult(BaseModel):

    conversation: Conversation

    answer: str