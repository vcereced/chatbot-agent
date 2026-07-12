from pydantic import BaseModel
from shared.domain.conversation import Conversation

class GetConversationRequest(BaseModel):

    conversation_id: str

class GetConversationResponse(BaseModel):

    conversation: Conversation

class SaveConversationRequest(BaseModel):

    conversation: Conversation

class SaveConversationResponse(BaseModel):

    success: bool