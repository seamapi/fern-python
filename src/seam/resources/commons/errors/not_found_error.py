# This file was auto-generated by Fern from our API Definition.

import typing

from ....core.api_error import ApiError


class NotFoundError(ApiError):
    def __init__(self, body: typing.Any):
        super().__init__(status_code=404, body=body)
