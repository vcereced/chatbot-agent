from fastapi import FastAPI
from app.api.execute import router as execute_router
from shared.logging.logger import configure_logging

logger = configure_logging(__name__)


app = FastAPI()
register_exception_handlers(app)
app.include_router(execute_router)

logger.info("tool-executer service started and ready to accept requests.")

@app.get("/")
def root():

    return {
        "status": "ok"
    }