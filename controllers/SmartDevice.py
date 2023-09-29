from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, device_id, device_type='',status='off'):
        self.device_id = device_id
        self.status = status
        self.device_type = device_type 
    def turn_on(self):
        if self.status == 'off':
            self.status = 'on'
            print(f"{self.device_type} {self.device_id} is turned on.")
        else:
            print(f"{self.device_type} {self.device_id} is already on.")

    def turn_off(self):
        if self.status == 'on':
            self.status = 'off'
            print(f"{self.device_type} {self.device_id} is turned off.")
        else:
            print(f"{self.device_type} {self.device_id} is already off.")

    @abstractmethod
    def action(self):
        pass

class Light(SmartDevice):
    def action(self):
        # Define the specific action for the Light class
        pass

class Door(SmartDevice):
    def action(self):
        # Define the specific action for the Door class
        pass

class Thermostat(SmartDevice):
    def __init__(self, device_id, temperature=70):
        super().__init__(device_id, device_type='thermostat')
        self.temperature = temperature

    def action(self):
        pass