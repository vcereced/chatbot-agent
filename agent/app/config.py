import os

class Config:
    TOOLS_URL = os.getenv("TOOLS_URL", "http://tools-executor:8000")    
    LLM_URL = os.getenv("LLM_URL", "http://llm:8000")
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "30"))

config = Config()