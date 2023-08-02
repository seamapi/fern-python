# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .access_code_status import AccessCodeStatus
from .access_code_type import AccessCodeType


class AccessCode(pydantic.BaseModel):
    common_code_key: typing.Optional[str]
    is_scheduled_on_device: typing.Optional[bool]
    type: AccessCodeType
    is_waiting_for_code_assignment: typing.Optional[bool]
    access_code_id: str
    device_id: str
    name: typing.Optional[str]
    code: typing.Optional[str]
    created_at: dt.datetime
    errors: typing.Optional[typing.Any]
    warnings: typing.Optional[typing.Any]
    is_managed: str
    starts_at: typing.Optional[dt.datetime]
    ends_at: typing.Optional[dt.datetime]
    status: AccessCodeStatus
    is_backup_access_code_available: bool
    is_backup: typing.Optional[bool]
    pulled_backup_access_code_id: typing.Optional[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
