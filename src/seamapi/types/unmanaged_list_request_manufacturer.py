# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class UnmanagedListRequestManufacturer(str, enum.Enum):
    AKUVOX = "akuvox"
    AUGUST = "august"
    BRIVO = "brivo"
    BUTTERFLYMX = "butterflymx"
    DOORKING = "doorking"
    GENIE = "genie"
    IGLOO = "igloo"
    KEYWE = "keywe"
    KWIKSET = "kwikset"
    LINEAR = "linear"
    LOCKLY = "lockly"
    NUKI = "nuki"
    PHILIA = "philia"
    SALTO = "salto"
    SAMSUNG = "samsung"
    SCHLAGE = "schlage"
    SEAM = "seam"
    UNKNOWN = "unknown"
    YALE = "yale"
    MINUT = "minut"
    TWO_N = "two_n"
    TTLOCK = "ttlock"
    NEST = "nest"
    IGLOOHOME = "igloohome"
    ECOBEE = "ecobee"
    HUBITAT = "hubitat"

    def visit(
        self,
        akuvox: typing.Callable[[], T_Result],
        august: typing.Callable[[], T_Result],
        brivo: typing.Callable[[], T_Result],
        butterflymx: typing.Callable[[], T_Result],
        doorking: typing.Callable[[], T_Result],
        genie: typing.Callable[[], T_Result],
        igloo: typing.Callable[[], T_Result],
        keywe: typing.Callable[[], T_Result],
        kwikset: typing.Callable[[], T_Result],
        linear: typing.Callable[[], T_Result],
        lockly: typing.Callable[[], T_Result],
        nuki: typing.Callable[[], T_Result],
        philia: typing.Callable[[], T_Result],
        salto: typing.Callable[[], T_Result],
        samsung: typing.Callable[[], T_Result],
        schlage: typing.Callable[[], T_Result],
        seam: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        yale: typing.Callable[[], T_Result],
        minut: typing.Callable[[], T_Result],
        two_n: typing.Callable[[], T_Result],
        ttlock: typing.Callable[[], T_Result],
        nest: typing.Callable[[], T_Result],
        igloohome: typing.Callable[[], T_Result],
        ecobee: typing.Callable[[], T_Result],
        hubitat: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UnmanagedListRequestManufacturer.AKUVOX:
            return akuvox()
        if self is UnmanagedListRequestManufacturer.AUGUST:
            return august()
        if self is UnmanagedListRequestManufacturer.BRIVO:
            return brivo()
        if self is UnmanagedListRequestManufacturer.BUTTERFLYMX:
            return butterflymx()
        if self is UnmanagedListRequestManufacturer.DOORKING:
            return doorking()
        if self is UnmanagedListRequestManufacturer.GENIE:
            return genie()
        if self is UnmanagedListRequestManufacturer.IGLOO:
            return igloo()
        if self is UnmanagedListRequestManufacturer.KEYWE:
            return keywe()
        if self is UnmanagedListRequestManufacturer.KWIKSET:
            return kwikset()
        if self is UnmanagedListRequestManufacturer.LINEAR:
            return linear()
        if self is UnmanagedListRequestManufacturer.LOCKLY:
            return lockly()
        if self is UnmanagedListRequestManufacturer.NUKI:
            return nuki()
        if self is UnmanagedListRequestManufacturer.PHILIA:
            return philia()
        if self is UnmanagedListRequestManufacturer.SALTO:
            return salto()
        if self is UnmanagedListRequestManufacturer.SAMSUNG:
            return samsung()
        if self is UnmanagedListRequestManufacturer.SCHLAGE:
            return schlage()
        if self is UnmanagedListRequestManufacturer.SEAM:
            return seam()
        if self is UnmanagedListRequestManufacturer.UNKNOWN:
            return unknown()
        if self is UnmanagedListRequestManufacturer.YALE:
            return yale()
        if self is UnmanagedListRequestManufacturer.MINUT:
            return minut()
        if self is UnmanagedListRequestManufacturer.TWO_N:
            return two_n()
        if self is UnmanagedListRequestManufacturer.TTLOCK:
            return ttlock()
        if self is UnmanagedListRequestManufacturer.NEST:
            return nest()
        if self is UnmanagedListRequestManufacturer.IGLOOHOME:
            return igloohome()
        if self is UnmanagedListRequestManufacturer.ECOBEE:
            return ecobee()
        if self is UnmanagedListRequestManufacturer.HUBITAT:
            return hubitat()