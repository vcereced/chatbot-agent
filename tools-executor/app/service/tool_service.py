from shared.tools.execute import ExecuteToolResponse, ExecuteToolRequest
from shared.domain.toolcall import ToolCall
from shared.domain.toolresult import ToolResult
from app.registry.tool_registry import ToolRegistry
from shared.logging.logger import configure_logging
from shared.domain.tooldefinition import ToolDefinition
from app.config import settings
import time
import asyncio

logger = configure_logging(__name__)

class ToolService:

    def __init__(self):
        self.registry = ToolRegistry()

    async def execute(self, toolcall: ToolCall) -> ToolResult:
        logger.info(f"Executing tool: {toolcall.name} with arguments: {toolcall.arguments}")
        tool = self.registry.get(toolcall.name)

        if not tool:
            logger.warning(f"Tool '{toolcall.name}' not found.")
            # Por ahora retornamos un mensaje simple en el resultado si no existe la tool
            return ToolResult(
                tool_name=toolcall.name,
                success=False,
                error=f"Error: Tool '{toolcall.name}' is not registered."
            )
        start_time = time.perf_counter()
        try:
            result = await asyncio.wait_for(tool.execute(toolcall.arguments), timeout=settings.tool_timeout_seconds)
            elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
            
            logger.info(f"Tool '{toolcall.name}' executed successfully in {elapsed_ms}ms")
            return ToolResult(
                tool_name=toolcall.name,
                success=True,
                result=result,
                execution_time_ms=elapsed_ms
            )
        
        except asyncio.TimeoutError:
            elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
            logger.error(f"Tool '{toolcall.name}' timed out after 30 seconds.")
            return ToolResult(
                tool_name=toolcall.name,
                success=False,
                error="Execution timed out. The tool took too long to respond.",
                execution_time_ms=elapsed_ms
            )

        except TypeError as exc:
            # Captura errores en los argumentos pasados a la función
            elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
            logger.error(f"Invalid arguments for tool '{toolcall.name}': {str(exc)}")
            return ToolResult(
                tool_name=toolcall.name,
                success=False,
                error=f"Invalid arguments provided: {str(exc)}",
                execution_time_ms=elapsed_ms
            )

        except Exception as exc:
            # Captura cualquier excepción no controlada dentro de la herramienta
            elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
            logger.error(f"Error executing tool '{toolcall.name}': {str(exc)}", exc_info=True)
            return ToolResult(
                tool_name=toolcall.name,
                success=False,
                error=f"Execution failed: {str(exc)}",
                execution_time_ms=elapsed_ms
            )
    
    def list_tools(self) -> list[ToolDefinition]:
        logger.info("Listing available tools")
        tools = self.registry.get_definitions()
        logger.info(f"Available tools: {len(tools)}")
        return tools