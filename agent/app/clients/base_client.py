from typing import Type, TypeVar
from app.config import config
import logging
import httpx

from pydantic import BaseModel

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class BaseClient:

    def __init__(self):

        self.client = httpx.Client(timeout=config.REQUEST_TIMEOUT)

    def post(
        self,
        url: str,
        request: BaseModel,
        response_model: Type[T],
    ) -> T:

        logger.info("POST %s", url)

        response = self.client.post(
            url,
            json=request.model_dump(),
        )

        response.raise_for_status()

        logger.info("Response %s", response.status_code)

        return response_model.model_validate(
            response.json()
        )