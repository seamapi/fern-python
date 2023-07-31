# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DevicesUnmanagedListRequestDeviceTypesItemDevicesUnmanagedListRequestDeviceTypesItem(str, enum.Enum):
    ECOBEE_THERMOSTAT = "ecobee_thermostat"
    NEST_THERMOSTAT = "nest_thermostat"

    def visit(
        self, ecobee_thermostat: typing.Callable[[], T_Result], nest_thermostat: typing.Callable[[], T_Result]
    ) -> T_Result:
        if (
            self
            is DevicesUnmanagedListRequestDeviceTypesItemDevicesUnmanagedListRequestDeviceTypesItem.ECOBEE_THERMOSTAT
        ):
            return ecobee_thermostat()
        if self is DevicesUnmanagedListRequestDeviceTypesItemDevicesUnmanagedListRequestDeviceTypesItem.NEST_THERMOSTAT:
            return nest_thermostat()
