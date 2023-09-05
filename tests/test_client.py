from seamapi import Seam
import os

def test_get_devices(seam: Seam):
    devices_response = seam.devices.list()
    print(f"First device id is {devices_response[0].device_id}")

# def test_create_access_code(seam: Seam): 
#     create_response = seam.access_codes.create(device_id="august_device_1")
#     print(f"Access code status is {create_response.status}")