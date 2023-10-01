from abc import ABC, abstractmethod
from  .Triggers import  Trigger

class SmartDevice(ABC):
    def __init__(self, device_id, device_type='', status='off'):
        self._device_id = device_id
        self._status = status
        self._device_type = device_type
        self._triggers = []

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status


    def turn_on(self):
        if self.get_status()== 'off':
            self.set_status('on') 
            print(f"{self._device_type} {self._device_id} is turned on.")
        else:
            print(f"{self._device_type} {self._device_id} is already on.")

    def turn_off(self):
        if self.get_status() == 'on':
            self.set_status('off')
            print(f"{self._device_type} {self._device_id} is turned off.")
        else:
            print(f"{self._device_type} {self._device_id} is already off.")

    def open_door(self):
        if self.get_status()=='close':
            self.set_status('open')
            print(f"{self._device_type} {self._device_id} is Opened.")
        else:
            print(f"{self._device_type} {self._device_id} is already Opened.")

    def close_door(self):
        if self.get_status() == 'open':
            self.set_status('close')
            print(f"{self._device_type} {self._device_id} is Closed")
        else:
            print(f"{self._device_type} {self._device_id} is already Closed.")

    @abstractmethod
    def action(self):
        pass

  

class Light(SmartDevice):
    def action(self):
        pass

class Door(SmartDevice):
    def action(self):
        pass

class Thermostat(SmartDevice):
    def __init__(self, device_id, device_manager, temperature="70"):
        super().__init__(device_id, device_type='thermostat')
        self._temperature = float(temperature)
        self._device_manager = device_manager
        self._trigger = Trigger(device_manager, temperature)

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, new_temperature):
        self._temperature = new_temperature

    def action(self):
        pass

    def update_temperature(self, new_temperature):
        print(f"Temperature updated from {self._temperature} to {new_temperature}")
        self._temperature = new_temperature
        data = {"temperature": self._temperature}
        self._trigger.update_temperature(data, new_temperature)

    def add_trigger(self, trigger_info):
        self._trigger.add_trigger(trigger_info)