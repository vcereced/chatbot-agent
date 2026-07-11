from fastapi import APIRouter
from app.schemas import ChatRequest, ChatResponse
from app.services.chat_service import ChatService
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)

router = APIRouter()

service = ChatService()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    logger.info(f"Received chat request: {request.message}")

    return service.chat(request)