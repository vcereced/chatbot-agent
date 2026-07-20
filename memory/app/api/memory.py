from fastapi import APIRouter
from app.services.memory_service import MemoryService
from shared.memory.conversation import GetConversationRequest, GetConversationResponse, SaveConversationRequest, SaveConversationResponse
from shared.domain.conversation import Conversation
from shared.errors import ConversationNotFound


router = APIRouter()

service = MemoryService()

@router.get("/conversations/get")
def get_conversation(conversation_id: str) -> GetConversationResponse:
    logger.info("/conversations/get")

    conversation = service.get(conversation_id) #->Conversation #call to MEMORY SERVICE

    return GetConversationResponse(conversation=conversation)

@router.post("/conversations/save")
def save(request: SaveConversationRequest):
    logger.info("/conversation/save")
    service.save(request.conversation)

@app.exception_handler(ConversationNotFound)
async def conversation_not_found_handler(request, exc):

    return JSONResponse(
        status_code=404,
        content={
            "detail": str(exc)
        }
    )