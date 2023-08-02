# This file was auto-generated by Fern from our API Definition.

import typing

import httpx


class BaseClientWrapper:
    def __init__(self, *, api_key: str):
        self.api_key = api_key

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {
            "X-Fern-Language": "Python",
            "X-Fern-SDK-Name": "fern-seam",
            "X-Fern-SDK-Version": "0.0.23",
        }
        headers["seam-workspace"] = self.api_key
        return headers


class SyncClientWrapper(BaseClientWrapper):
    def __init__(self, *, api_key: str, httpx_client: httpx.Client):
        super().__init__(api_key=api_key)
        self.httpx_client = httpx_client


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(self, *, api_key: str, httpx_client: httpx.AsyncClient):
        super().__init__(api_key=api_key)
        self.httpx_client = httpx_client
