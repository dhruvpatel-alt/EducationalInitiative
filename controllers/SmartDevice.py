from abc import ABC, abstractmethod
from .Triggers import TriggerManager
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
    def __init__(self, device_id,device_manager,temperature="70"):
        super().__init__(device_id, device_type='thermostat')
        self.temperature = temperature
        self.device_manager=device_manager
        self.trigger_manager = TriggerManager(device_manager)
       

    def action(self):
        data = {"temperature": self.temperature}
        self.trigger_manager.trigger_action_on_device(data)

    def add_trigger(self,triggerInfo):
        self.trigger_manager.add_trigger(triggerInfo)
        self.action()