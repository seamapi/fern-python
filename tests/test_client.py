
from seam.client import Seam
import os

seam_client = Seam(api_key="YOUR_API_KEY")

def test_get_devices() -> None:
    devices_response = seam_client.devices.list()
    print(f"First device id is {devices_response.devices[0].device_id}")

def test_create_access_code() -> None: 
    create_response = seam_client.access_codes.create(device_id="138520f8-4b7f-4c04-9808-46de5303f0bd")
    print(f"Access code status is {create_response.access_code.status}")
