from .SmartDevices import Light, Door, Thermostat

# Create a DeviceFactory class
class DeviceFactory:
    def create_device(self, device_info, device_manager):
        device_type = device_info['type'].lower()
        if device_type == 'light':
            return Light(device_info, device_manager)
        elif device_type == 'door':
            return Door(device_info, device_manager)
        elif device_type == 'thermostat':
            return Thermostat(device_info, device_manager)
        else:
            print(f"We are not supporting this {device_type} device right now. Try with another device.")
            return None
