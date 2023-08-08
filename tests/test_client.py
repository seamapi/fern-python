from seam.client import Seam
import os

seam_client = Seam(api_key=os.environ.get("SEAM_API_KEY"))

def test_get_devices() -> None:
    devices_response = seam_client.devices.list()
    assert len(devices_response.devices) > 0
