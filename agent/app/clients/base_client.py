from typing import Type, TypeVar
from app.config import config
import logging
import httpx
from app.clients.exceptions import ClientError

from pydantic import BaseModel

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class BaseClient:

    def __init__(self):

        self.client = httpx.Client(timeout=config.REQUEST_TIMEOUT)

     def get(self, url: str, response_model: type[T]) -> T:

        try:

            response = self.client.get(url)

            return self._parse_response(response, response_model)

        except httpx.HTTPError as e:

            raise ClientError(str(e))

    def post(self, url: str, request: BaseModel, response_model: Type[T]) -> T:

        logger.info("POST %s", url)
        try:
            response = self.client.post(
                url,
                json=request.model_dump(),
            )

            return self._parse_response(response, response_model)

            
        except httpx.HTTPError as e:
            raise ClientError(str(e))

    def _parse_response(self, response: httpx.Response, response_model: type[T]) -> T:

        response.raise_for_status()
        logger.info("Response %s", response.status_code)

        return response_model.model_validate(response.json())
        