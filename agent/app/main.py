from fastapi import FastAPI
from app.api.chat import router as chat_router
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)


app = FastAPI()
app.include_router(chat_router)

logger.info("Agent service started and ready to accept requests.")

@app.get("/")
def root():

    return {
        "status": "ok"
    }