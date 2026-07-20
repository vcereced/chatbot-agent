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

        logger.info("POST %s", url)
        try:

            response = self.client.get(url)

            return self._parse_response(response, response_model)

        except httpx.HTTPStatusError as e:

            raise HttpException(
                status_code=e.response.status_code,
                message=e.response.text,
                url=url,
            )

        except httpx.HTTPError as e:

            raise HttpException(
                status_code=503,
                message=str(e),
                url=url,
            )

    def post(self, url: str, request: BaseModel, response_model: Type[T]) -> T:

        logger.info("POST %s", url)
        try:
            response = self.client.post(
                url,
                json=request.model_dump(),
            )

            return self._parse_response(response, response_model)

            
        except httpx.HTTPStatusError as e:

            raise HttpException(
                status_code=e.response.status_code,
                message=e.response.text,
                url=url,
            )

        except httpx.HTTPError as e:

            raise HttpException(
                status_code=503,
                message=str(e),
                url=url,
            )

    def _parse_response(self, response: httpx.Response, response_model: type[T]) -> T:

        response.raise_for_status()
        logger.info("Response %s", response.status_code)

        return response_model.model_validate(response.json())
        