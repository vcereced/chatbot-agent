from app.schemas import GenerateResponse


class LLMService:

    def generate(self, prompt: str) -> GenerateResponse:

        return GenerateResponse(
            text=f"LLM recibido: {prompt}"
        )