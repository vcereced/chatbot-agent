from fastapi import APIRouter
from app.services.memory_service import MemoryService
from shared.memory.conversation import GetOrCreateConversationRequest, GetOrCreateConversationResponse, SaveConversationRequest, SaveConversationResponse
from shared.domain.conversation import Conversation
from shared.errors import ConversationNotFound
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)

router = APIRouter()

service = MemoryService()

@router.post("/conversations/get_or_create")
def get_conversation(request: GetOrCreateConversationRequest) -> GetOrCreateConversationResponse:
    logger.info(f"/conversations/get con el id {request.conversation_id}")

    conversation = service.get_or_create(request.conversation_id) #->Conversation #call to MEMORY SERVICE

    return GetOrCreateConversationResponse(conversation=conversation)

@router.post("/conversations/save")
def save(request: SaveConversationRequest):
    logger.info(f"/conversation/save {SaveConversationRequest}")
    success = service.save(request.conversation)
    return SaveConversationResponse(success=success)

