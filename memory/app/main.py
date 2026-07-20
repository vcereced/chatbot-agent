from fastapi import FastAPI

from app.api.memory import router as memory_router

from shared.logging.logger import configure_logging

logger = configure_logging(__name__)

app = FastAPI()
register_exception_handlers(app)
app.include_router(memory_router)

logger.info("Memory service started and ready to accept requests.")

@app.get("/")
def root():

    return {
        "status": "ok"
    }