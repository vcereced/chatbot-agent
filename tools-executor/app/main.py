from fastapi import FastAPI
from app.api.execute import router as execute_router
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)

app = FastAPI()
app.include_router(execute_router)

@app.get("/health", status_code=200)
@app.get("/", status_code=200)
def health_check():
    return {
        "status": "ok",
        "service": "tools-executor"
    }

logger.info("tools-executer service started and ready to accept requests.")