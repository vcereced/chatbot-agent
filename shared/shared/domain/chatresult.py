from pydantic import BaseModel
from shared.shared.domain.conversation import Conversation

class ChatResult(BaseModel):

    conversation_id: str

    response: str