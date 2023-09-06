from seamapi import Seam
import pytest


def test_access_codes(seam: Seam):
    all_devices = seam.devices.list()
    some_device = all_devices[0]

    created_access_code = seam.access_codes.create(
        device_id=some_device.device_id, name="Test code", code="4444"
    )
    assert created_access_code.name == "Test code"
    assert created_access_code.status == "setting"

    access_codes = seam.access_codes.list(device_id=some_device.device_id)
    assert len(access_codes) == 1

    access_code = seam.access_codes.get(created_access_code.access_code_id)
    assert access_code.code == "4444"

    with pytest.raises(expected_exception=Exception):
        seam.access_codes.create(
            device_id=some_device.device_id, name="Duplicate Access Code", code="4444"
        )

    access_code = seam.access_codes.update(
        access_code_id=access_code.access_code_id, name="Updated name"
    )
    assert access_code.name == "Updated name"

    delete_action_attempt = seam.access_codes.delete(
        access_code_id=created_access_code.access_code_id
    )
    assert delete_action_attempt.status == "pending"

    access_codes = seam.access_codes.create_multiple(
        device_ids=[d.device_id for d in all_devices],
    )
    assert len(access_codes) == len(all_devices)
    assert len(all_devices) > 1
    assert len(set([ac.common_code_key for ac in access_codes])) == 1
