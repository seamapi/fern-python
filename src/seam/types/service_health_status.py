# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ServiceHealthStatus(str, enum.Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    DOWN = "down"

    def visit(
        self,
        healthy: typing.Callable[[], T_Result],
        degraded: typing.Callable[[], T_Result],
        down: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceHealthStatus.HEALTHY:
            return healthy()
        if self is ServiceHealthStatus.DEGRADED:
            return degraded()
        if self is ServiceHealthStatus.DOWN:
            return down()
