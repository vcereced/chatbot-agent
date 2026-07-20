from fastapi import APIRouter
from app.schemas import GenerateRequest, GenerateResponse
from app.services.llm_service import LLMService
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)

router = APIRouter()
service = LLMService()


@router.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest) -> GenerateResponse:

    logger.info(f"generate request: {request}")
    result = service.generate(request.messages, request.tools)

    return GenerateResponse(result=result)