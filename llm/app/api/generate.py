from fastapi import APIRouter

from app.schemas import GenerateRequest, GenerateResponse
from app.services.llm_service import LLMService

router = APIRouter()

service = LLMService()


@router.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):

    return service.generate(request.prompt) 