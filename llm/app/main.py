from fastapi import FastAPI
from app.api.generate import router
from shared.logging.logger import configure_logging


logger = configure_logging(__name__)

app = FastAPI()
register_exception_handlers(app)
app.include_router(router)


@app.get("/")
def root():
    logger.info("Received root request.")

    return {
        "status": "ok"
    }