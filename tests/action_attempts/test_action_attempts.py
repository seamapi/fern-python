from seamapi import Seam
from tests.fixtures.run_august_factory import run_august_factory


def test_action_attempts(seam: Seam):
    some_device = seam.devices.list()[0]
    created_access_code = seam.access_codes.create(
        device_id=some_device.device_id, name="Test code", code="4444"
    )
    delete_action_attempt = seam.access_codes.delete(created_access_code.access_code_id)

    action_attempt = seam.action_attempts.get(delete_action_attempt.action_attempt_id)
    assert action_attempt is not None

    polled_action_attempt = seam.action_attempts.poll_until_ready(
        delete_action_attempt.action_attempt_id
    )
    assert polled_action_attempt is not None
