from fastapi import APIRouter
from app.services.memory_service import MemoryService
from shared.memory.conversation import GetConversationRequest, GetConversationResponse, SaveConversationRequest, SaveConversationResponse


router = APIRouter()

service = MemoryService()


@router.get("/conversations/get")
def get_conversation(conversation_id: str) -> GetConversationResponse:

    conversation = service.get(conversation_id) #->Conversation #call to MEMORY SERVICE

    return GetConversationResponse(conversation=conversation)

@router.post("/conversations/save")
def save(request: SaveConversationRequest):

    service.save(request.conversation)