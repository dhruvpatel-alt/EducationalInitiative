from abc import ABC, abstractmethod
from  trigger import  Trigger
from observer import Observer

class SmartDevice(ABC):
    def __init__(self, device_id, device_type='', status='off'):
        self._device_id = device_id
        self._status = status
        self._device_type = device_type
        self._triggers = []
        self._observers = []

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status
        self.notify_observers({'status': status,'device_name':self._device_type,'device_id':self._device_id})

    def attach(self, observer):
        self._observers.append(observer)

    def notify_observers(self, data):
        for observer in self._observers:
            observer.update(self, data)

    def turn_on(self):
        if self.get_status()== 'off':
            self.set_status('on') 
            print(f"Action : {self._device_type} {self._device_id} is turned on.")
        else:
            print(f"Info : {self._device_type} {self._device_id} is already on.")

    def turn_off(self):
        if self.get_status() == 'on':
            self.set_status('off')
            print(f"Action : {self._device_type} {self._device_id} is turned off.")
        else:
            print(f"Info : {self._device_type} {self._device_id} is already off.")

    def open_door(self):
        if self.get_status()=='close':
            self.set_status('open')
            print(f"Action : {self._device_type} {self._device_id} is Opened.")
        else:
            print(f"Info : {self._device_type} {self._device_id} is already Opened.")

    def close_door(self):
        if self.get_status() == 'open':
            self.set_status('close')
            print(f"Action : {self._device_type} {self._device_id} is Closed")
        else:
            print(f"Info : {self._device_type} {self._device_id} is already Closed.")

    @abstractmethod
    def action(self):
        pass

  

class LightFactory(SmartDevice):
    def action(self):
        pass

class DoorFactory(SmartDevice):
    def action(self):
        pass

class ThermostatFactory(SmartDevice):
    def __init__(self, device_id, device_manager, temperature="70"):
        super().__init__(device_id, device_type='thermostat')
        self._temperature = float(temperature)
        self._device_manager = device_manager
        self._trigger = Trigger(device_manager, temperature)

    def get_temperature(self):
        return self._temperature

    def update_temperature(self, new_temperature):
        print(f"Info: Temperature updated from {self._temperature} to {new_temperature}")
        self._temperature = new_temperature
        data = {"temperature": self._temperature}
        self._trigger.update_temperature(data, new_temperature)
        self.notify_observers({'temperature': new_temperature})


    def get_temperature(self):
        return self._temperature


    def action(self):
        pass

    def add_trigger(self, trigger_info):
        self._trigger.add_trigger(trigger_info)