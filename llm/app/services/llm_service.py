from app.schemas import GenerateResponse, GenerateRequest
from shared.domain.toolcall import ToolCall
from shared.domain.message import Message
from shared.domain.generate_result import GenerateResult
from shared.logging.logger import configure_logging
from app.clients.openai_client import OpenAIAdapter
logger = configure_logging(__name__)


class LLMService:

    def __init__(self):

        self.llm = OpenAIAdapter()

    def generate(self, conversation: Conversation, tools: list[ToolDefinition]) -> GenerateResult:

        logger.info(f"Generating LLM response for messages: {messages}")
        
        messages = OpenAIAdapter.to_messages(conversation)

        tools = OpenAIAdapter.to_tools(tools)

        response = self.client.generate(
            messages,
            tools,
        )
        print(response)
        logger.info(response.model_dump())

            return GenerateResult(
                tool_call=ToolCall(
                name="echo",
                arguments={
                    "text": prompt[6:].strip()
                }))

        return GenerateResult(text=f"LLM recibido: {prompt}")