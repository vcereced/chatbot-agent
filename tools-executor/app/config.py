from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- Configuración del Microservicio ---
    log_level: str = Field(default="INFO", description="Nivel de logging (DEBUG, INFO, ERROR)")
    
    # --- Timeouts y Límites ---
    tool_timeout_seconds: float = Field(
        default=30.0, 
        description="Tiempo máximo de ejecución para una herramienta"
    )

# Usamos lru_cache para que la lectura e instanciación de las variables 
# ocurra UNA sola vez en memoria (Patrón Singleton en producción)
@lru_cache()
def get_settings() -> Settings:
    return Settings()


# Exportamos la instancia para uso directo
settings = get_settings()