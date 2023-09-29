from .SmartDevice import Light,Door,Thermostat
class DeviceManager:
    def __init__(self):
        self.devices = {'light':[Light,{}],'door':[Door,{}],'thermostat':[Thermostat,{}]}

    def create_device(self, device_info):
        device_type = device_info['type']
        smartDevice = self.devices.get(device_type)
        if smartDevice==None:
            print(f"We are not supporting this {device_type} device right now. Try with another device.")
            return None
        device_class=smartDevice[0]
        if device_class:
            device_id = len(smartDevice[1]) + 1
            if device_type == 'thermostat':
                temperature = device_info.get('temperature', 70)  # Default temperature is 70 if not specified
                device = device_class(device_id, temperature)
            else:
                status = device_info.get('status', 'off')  # Default status is 'off' if not specified
                device = device_class(device_id, device_type,status)
            self.devices[device_id] = device
            print(f"{device_type.capitalize()} {device_id} has been created!")
            return device