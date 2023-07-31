# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class UnmanagedDeviceCapabilitiesSupportedItem(str, enum.Enum):
    ACCESS_CODE = "access_code"
    LOCK = "lock"
    NOISE_DETECTION = "noise_detection"
    THERMOSTAT = "thermostat"
    BATTERY = "battery"

    def visit(
        self,
        access_code: typing.Callable[[], T_Result],
        lock: typing.Callable[[], T_Result],
        noise_detection: typing.Callable[[], T_Result],
        thermostat: typing.Callable[[], T_Result],
        battery: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UnmanagedDeviceCapabilitiesSupportedItem.ACCESS_CODE:
            return access_code()
        if self is UnmanagedDeviceCapabilitiesSupportedItem.LOCK:
            return lock()
        if self is UnmanagedDeviceCapabilitiesSupportedItem.NOISE_DETECTION:
            return noise_detection()
        if self is UnmanagedDeviceCapabilitiesSupportedItem.THERMOSTAT:
            return thermostat()
        if self is UnmanagedDeviceCapabilitiesSupportedItem.BATTERY:
            return battery()
