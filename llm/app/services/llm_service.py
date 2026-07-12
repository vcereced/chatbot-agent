from app.schemas import GenerateResponse, GenerateRequest
from shared.domain.toolcall import ToolCall
from shared.domain.message import Message
from shared.domain.generate_result import GenerateResult
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)


class LLMService:

    def generate(self, messages: list[Message]) -> GenerateResult:

        logger.info(f"Generating LLM response for messages: {messages}")
        
        last_user_message = next(message for message in reversed(messages) if message.role == "user")

        prompt = last_user_message.content  
        if prompt.startswith("/echo"):

            return GenerateResult(
                tool_call=ToolCall(
                name="echo",
                arguments={
                    "text": prompt[6:].strip()
                }))

        return GenerateResult(text=f"LLM recibido: {prompt}")