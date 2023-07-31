# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...environment import SeamEnvironment
from ...errors.bad_request_error import BadRequestError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.thermostats_get_response import ThermostatsGetResponse
from ...types.thermostats_heat_response import ThermostatsHeatResponse
from ...types.thermostats_list_request_device_type import ThermostatsListRequestDeviceType
from ...types.thermostats_list_request_device_types_item import ThermostatsListRequestDeviceTypesItem
from ...types.thermostats_list_request_manufacturer import ThermostatsListRequestManufacturer
from ...types.thermostats_list_response import ThermostatsListResponse
from ...types.thermostats_update_request_default_climate_setting import ThermostatsUpdateRequestDefaultClimateSetting
from ...types.thermostats_update_response import ThermostatsUpdateResponse
from .resources.climate_setting_schedules.client import (
    AsyncClimateSettingSchedulesClient,
    ClimateSettingSchedulesClient,
)

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ThermostatsClient:
    def __init__(self, *, environment: SeamEnvironment = SeamEnvironment.DEFAULT, client_wrapper: SyncClientWrapper):
        self._environment = environment
        self._client_wrapper = client_wrapper
        self.climate_setting_schedules = ClimateSettingSchedulesClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )

    def get(
        self, *, device_id: typing.Optional[str] = OMIT, name: typing.Optional[str] = OMIT
    ) -> ThermostatsGetResponse:
        """
        Parameters:
            - device_id: typing.Optional[str].

            - name: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if device_id is not OMIT:
            _request["device_id"] = device_id
        if name is not OMIT:
            _request["name"] = name
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/get"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsGetResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def heat(
        self,
        *,
        device_id: str,
        heating_set_point_celsius: typing.Optional[float] = OMIT,
        heating_set_point_fahrenheit: typing.Optional[float] = OMIT,
        sync: typing.Optional[bool] = OMIT,
    ) -> ThermostatsHeatResponse:
        """
        Parameters:
            - device_id: str.

            - heating_set_point_celsius: typing.Optional[float].

            - heating_set_point_fahrenheit: typing.Optional[float].

            - sync: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {"device_id": device_id}
        if heating_set_point_celsius is not OMIT:
            _request["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not OMIT:
            _request["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if sync is not OMIT:
            _request["sync"] = sync
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/heat"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsHeatResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(
        self,
        *,
        connected_account_id: typing.Optional[str] = OMIT,
        connected_account_ids: typing.Optional[typing.List[str]] = OMIT,
        connect_webview_id: typing.Optional[str] = OMIT,
        device_type: typing.Optional[ThermostatsListRequestDeviceType] = OMIT,
        device_types: typing.Optional[typing.List[ThermostatsListRequestDeviceTypesItem]] = OMIT,
        manufacturer: typing.Optional[ThermostatsListRequestManufacturer] = OMIT,
        device_ids: typing.Optional[typing.List[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        created_before: typing.Optional[str] = OMIT,
    ) -> ThermostatsListResponse:
        """
        Parameters:
            - connected_account_id: typing.Optional[str].

            - connected_account_ids: typing.Optional[typing.List[str]].

            - connect_webview_id: typing.Optional[str].

            - device_type: typing.Optional[ThermostatsListRequestDeviceType].

            - device_types: typing.Optional[typing.List[ThermostatsListRequestDeviceTypesItem]].

            - manufacturer: typing.Optional[ThermostatsListRequestManufacturer].

            - device_ids: typing.Optional[typing.List[str]].

            - limit: typing.Optional[float].

            - created_before: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if connected_account_id is not OMIT:
            _request["connected_account_id"] = connected_account_id
        if connected_account_ids is not OMIT:
            _request["connected_account_ids"] = connected_account_ids
        if connect_webview_id is not OMIT:
            _request["connect_webview_id"] = connect_webview_id
        if device_type is not OMIT:
            _request["device_type"] = device_type
        if device_types is not OMIT:
            _request["device_types"] = device_types
        if manufacturer is not OMIT:
            _request["manufacturer"] = manufacturer
        if device_ids is not OMIT:
            _request["device_ids"] = device_ids
        if limit is not OMIT:
            _request["limit"] = limit
        if created_before is not OMIT:
            _request["created_before"] = created_before
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/list"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsListResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self, *, device_id: str, default_climate_setting: ThermostatsUpdateRequestDefaultClimateSetting
    ) -> ThermostatsUpdateResponse:
        """
        Parameters:
            - device_id: str.

            - default_climate_setting: ThermostatsUpdateRequestDefaultClimateSetting.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/update"),
            json=jsonable_encoder({"device_id": device_id, "default_climate_setting": default_climate_setting}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsUpdateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncThermostatsClient:
    def __init__(self, *, environment: SeamEnvironment = SeamEnvironment.DEFAULT, client_wrapper: AsyncClientWrapper):
        self._environment = environment
        self._client_wrapper = client_wrapper
        self.climate_setting_schedules = AsyncClimateSettingSchedulesClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )

    async def get(
        self, *, device_id: typing.Optional[str] = OMIT, name: typing.Optional[str] = OMIT
    ) -> ThermostatsGetResponse:
        """
        Parameters:
            - device_id: typing.Optional[str].

            - name: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if device_id is not OMIT:
            _request["device_id"] = device_id
        if name is not OMIT:
            _request["name"] = name
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/get"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsGetResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def heat(
        self,
        *,
        device_id: str,
        heating_set_point_celsius: typing.Optional[float] = OMIT,
        heating_set_point_fahrenheit: typing.Optional[float] = OMIT,
        sync: typing.Optional[bool] = OMIT,
    ) -> ThermostatsHeatResponse:
        """
        Parameters:
            - device_id: str.

            - heating_set_point_celsius: typing.Optional[float].

            - heating_set_point_fahrenheit: typing.Optional[float].

            - sync: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {"device_id": device_id}
        if heating_set_point_celsius is not OMIT:
            _request["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not OMIT:
            _request["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if sync is not OMIT:
            _request["sync"] = sync
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/heat"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsHeatResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(
        self,
        *,
        connected_account_id: typing.Optional[str] = OMIT,
        connected_account_ids: typing.Optional[typing.List[str]] = OMIT,
        connect_webview_id: typing.Optional[str] = OMIT,
        device_type: typing.Optional[ThermostatsListRequestDeviceType] = OMIT,
        device_types: typing.Optional[typing.List[ThermostatsListRequestDeviceTypesItem]] = OMIT,
        manufacturer: typing.Optional[ThermostatsListRequestManufacturer] = OMIT,
        device_ids: typing.Optional[typing.List[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        created_before: typing.Optional[str] = OMIT,
    ) -> ThermostatsListResponse:
        """
        Parameters:
            - connected_account_id: typing.Optional[str].

            - connected_account_ids: typing.Optional[typing.List[str]].

            - connect_webview_id: typing.Optional[str].

            - device_type: typing.Optional[ThermostatsListRequestDeviceType].

            - device_types: typing.Optional[typing.List[ThermostatsListRequestDeviceTypesItem]].

            - manufacturer: typing.Optional[ThermostatsListRequestManufacturer].

            - device_ids: typing.Optional[typing.List[str]].

            - limit: typing.Optional[float].

            - created_before: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if connected_account_id is not OMIT:
            _request["connected_account_id"] = connected_account_id
        if connected_account_ids is not OMIT:
            _request["connected_account_ids"] = connected_account_ids
        if connect_webview_id is not OMIT:
            _request["connect_webview_id"] = connect_webview_id
        if device_type is not OMIT:
            _request["device_type"] = device_type
        if device_types is not OMIT:
            _request["device_types"] = device_types
        if manufacturer is not OMIT:
            _request["manufacturer"] = manufacturer
        if device_ids is not OMIT:
            _request["device_ids"] = device_ids
        if limit is not OMIT:
            _request["limit"] = limit
        if created_before is not OMIT:
            _request["created_before"] = created_before
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/list"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsListResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self, *, device_id: str, default_climate_setting: ThermostatsUpdateRequestDefaultClimateSetting
    ) -> ThermostatsUpdateResponse:
        """
        Parameters:
            - device_id: str.

            - default_climate_setting: ThermostatsUpdateRequestDefaultClimateSetting.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/update"),
            json=jsonable_encoder({"device_id": device_id, "default_climate_setting": default_climate_setting}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsUpdateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
