from seamapi import Seam


def test_get_devices(seam: Seam):
    devices_response = seam.devices.list()
    assert devices_response[0].device_id


def test_create_access_code(seam: Seam):
    access_code = seam.access_codes.create(device_id="august_device_1", code="1234")
    assert access_code.status == "pending"
    assert access_code.code == "1234"


def test_list_access_codes(seam: Seam):
    access_codes = seam.access_codes.list(device_id="august_device_1")
    assert len(access_codes) == 0

    seam.access_codes.create(device_id="august_device_id")
    access_codes = seam.access_codes.list(device_id="august_device_1")
    assert len(access_codes) == 1
