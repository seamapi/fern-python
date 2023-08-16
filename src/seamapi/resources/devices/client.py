# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...errors.bad_request_error import BadRequestError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.devices_delete_response import DevicesDeleteResponse
from ...types.devices_get_response import DevicesGetResponse
from ...types.devices_list_device_providers_request_provider_category import (
    DevicesListDeviceProvidersRequestProviderCategory,
)
from ...types.devices_list_device_providers_response import DevicesListDeviceProvidersResponse
from ...types.devices_list_request_device_type import DevicesListRequestDeviceType
from ...types.devices_list_request_device_types_item import DevicesListRequestDeviceTypesItem
from ...types.devices_list_request_manufacturer import DevicesListRequestManufacturer
from ...types.devices_list_response import DevicesListResponse
from ...types.devices_update_request_location import DevicesUpdateRequestLocation
from ...types.devices_update_request_properties import DevicesUpdateRequestProperties
from ...types.devices_update_response import DevicesUpdateResponse
from .resources.unmanaged.client import AsyncUnmanagedClient, UnmanagedClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DevicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.unmanaged = UnmanagedClient(client_wrapper=self._client_wrapper)

    def delete(self, *, device_id: str) -> DevicesDeleteResponse:
        """
        Parameters:
            - device_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "devices/delete"),
            json=jsonable_encoder({"device_id": device_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DevicesDeleteResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, *, device_id: typing.Optional[str] = OMIT, name: typing.Optional[str] = OMIT) -> DevicesGetResponse:
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
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "devices/get"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DevicesGetResponse, _response.json())  # type: ignore
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
        device_type: typing.Optional[DevicesListRequestDeviceType] = OMIT,
        device_types: typing.Optional[typing.List[DevicesListRequestDeviceTypesItem]] = OMIT,
        manufacturer: typing.Optional[DevicesListRequestManufacturer] = OMIT,
        device_ids: typing.Optional[typing.List[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        created_before: typing.Optional[dt.datetime] = OMIT,
    ) -> DevicesListResponse:
        """
        Parameters:
            - connected_account_id: typing.Optional[str].

            - connected_account_ids: typing.Optional[typing.List[str]].

            - connect_webview_id: typing.Optional[str].

            - device_type: typing.Optional[DevicesListRequestDeviceType].

            - device_types: typing.Optional[typing.List[DevicesListRequestDeviceTypesItem]].

            - manufacturer: typing.Optional[DevicesListRequestManufacturer].

            - device_ids: typing.Optional[typing.List[str]].

            - limit: typing.Optional[float].

            - created_before: typing.Optional[dt.datetime].
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
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "devices/list"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DevicesListResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_device_providers(
        self, *, provider_category: typing.Optional[DevicesListDeviceProvidersRequestProviderCategory] = OMIT
    ) -> DevicesListDeviceProvidersResponse:
        """
        Parameters:
            - provider_category: typing.Optional[DevicesListDeviceProvidersRequestProviderCategory].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if provider_category is not OMIT:
            _request["provider_category"] = provider_category
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "devices/list_device_providers"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DevicesListDeviceProvidersResponse, _response.json())  # type: ignore
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
        self,
        *,
        device_id: str,
        properties: typing.Optional[DevicesUpdateRequestProperties] = OMIT,
        name: typing.Optional[str] = OMIT,
        location: typing.Optional[DevicesUpdateRequestLocation] = OMIT,
        is_managed: typing.Optional[bool] = OMIT,
    ) -> DevicesUpdateResponse:
        """
        Parameters:
            - device_id: str.

            - properties: typing.Optional[DevicesUpdateRequestProperties].

            - name: typing.Optional[str].

            - location: typing.Optional[DevicesUpdateRequestLocation].

            - is_managed: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {"device_id": device_id}
        if properties is not OMIT:
            _request["properties"] = properties
        if name is not OMIT:
            _request["name"] = name
        if location is not OMIT:
            _request["location"] = location
        if is_managed is not OMIT:
            _request["is_managed"] = is_managed
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "devices/update"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DevicesUpdateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDevicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.unmanaged = AsyncUnmanagedClient(client_wrapper=self._client_wrapper)

    async def delete(self, *, device_id: str) -> DevicesDeleteResponse:
        """
        Parameters:
            - device_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "devices/delete"),
            json=jsonable_encoder({"device_id": device_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DevicesDeleteResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, *, device_id: typing.Optional[str] = OMIT, name: typing.Optional[str] = OMIT
    ) -> DevicesGetResponse:
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
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "devices/get"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DevicesGetResponse, _response.json())  # type: ignore
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
        device_type: typing.Optional[DevicesListRequestDeviceType] = OMIT,
        device_types: typing.Optional[typing.List[DevicesListRequestDeviceTypesItem]] = OMIT,
        manufacturer: typing.Optional[DevicesListRequestManufacturer] = OMIT,
        device_ids: typing.Optional[typing.List[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        created_before: typing.Optional[dt.datetime] = OMIT,
    ) -> DevicesListResponse:
        """
        Parameters:
            - connected_account_id: typing.Optional[str].

            - connected_account_ids: typing.Optional[typing.List[str]].

            - connect_webview_id: typing.Optional[str].

            - device_type: typing.Optional[DevicesListRequestDeviceType].

            - device_types: typing.Optional[typing.List[DevicesListRequestDeviceTypesItem]].

            - manufacturer: typing.Optional[DevicesListRequestManufacturer].

            - device_ids: typing.Optional[typing.List[str]].

            - limit: typing.Optional[float].

            - created_before: typing.Optional[dt.datetime].
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
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "devices/list"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DevicesListResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_device_providers(
        self, *, provider_category: typing.Optional[DevicesListDeviceProvidersRequestProviderCategory] = OMIT
    ) -> DevicesListDeviceProvidersResponse:
        """
        Parameters:
            - provider_category: typing.Optional[DevicesListDeviceProvidersRequestProviderCategory].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if provider_category is not OMIT:
            _request["provider_category"] = provider_category
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "devices/list_device_providers"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DevicesListDeviceProvidersResponse, _response.json())  # type: ignore
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
        self,
        *,
        device_id: str,
        properties: typing.Optional[DevicesUpdateRequestProperties] = OMIT,
        name: typing.Optional[str] = OMIT,
        location: typing.Optional[DevicesUpdateRequestLocation] = OMIT,
        is_managed: typing.Optional[bool] = OMIT,
    ) -> DevicesUpdateResponse:
        """
        Parameters:
            - device_id: str.

            - properties: typing.Optional[DevicesUpdateRequestProperties].

            - name: typing.Optional[str].

            - location: typing.Optional[DevicesUpdateRequestLocation].

            - is_managed: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {"device_id": device_id}
        if properties is not OMIT:
            _request["properties"] = properties
        if name is not OMIT:
            _request["name"] = name
        if location is not OMIT:
            _request["location"] = location
        if is_managed is not OMIT:
            _request["is_managed"] = is_managed
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "devices/update"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DevicesUpdateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)