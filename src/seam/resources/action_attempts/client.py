# This file was auto-generated by Fern from our API Definition.

import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import SeamEnvironment
from .types.action_attempt import ActionAttempt
from .types.action_attempt_id import ActionAttemptId


class ActionAttemptsClient:
    def __init__(self, *, environment: SeamEnvironment = SeamEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token

    def get(self, *, action_attempt_id: ActionAttemptId) -> ActionAttempt:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "action_attempts/get"),
            params={"action_attempt_id": jsonable_encoder(action_attempt_id)},
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ActionAttempt, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncActionAttemptsClient:
    def __init__(self, *, environment: SeamEnvironment = SeamEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token

    async def get(self, *, action_attempt_id: ActionAttemptId) -> ActionAttempt:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "action_attempts/get"),
                params={"action_attempt_id": jsonable_encoder(action_attempt_id)},
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ActionAttempt, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)