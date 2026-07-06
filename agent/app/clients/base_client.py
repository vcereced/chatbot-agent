import httpx

from app.clients.exceptions import ClientError
from app.config import REQUEST_TIMEOUT


class BaseClient:

    def __init__(self):

        self.client = httpx.Client(
            timeout=REQUEST_TIMEOUT
        )

    def post(self, url: str, body: dict) -> dict:

        try:

            response = self.client.post(
                url,
                json=body,
                timeout=REQUEST_TIMEOUT
            )

            response.raise_for_status()

            return response.json()

        except httpx.HTTPError as e:

            raise ClientError(str(e))