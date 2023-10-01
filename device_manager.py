from scheduler import Schedules
import time
from smart_devices import Light, Door, Thermostat
import schedule
from customize_exception import MyException
from datetime import datetime

class DeviceManager:
    def __init__(self):
        self._devices = {'light': [Light, {}], 'door': [Door, {}], 'thermostat': [Thermostat, {}]}
        self._schedules = {}
        self._actions = {
            'turn_on': self._turn_on,
            'turn_off': self._turn_off,
            'close_door': self._close_door,
            'open_door': self._open_door
        }


    def create_device(self, device_info):
        device_type = device_info.get('type')
        if device_type is None:
            raise MyException('Type is not provided in device info')

        smart_device = self._devices.get(device_type)
        if smart_device is None:
            raise MyException(f"We do not support {device_type} devices right now. Try with another device.")

        device_class = smart_device[0]
        if device_type == 'thermostat':
            temperature = device_info.get('temperature', 70)
            if temperature is None:
                raise MyException(f"Temperature is not given for {device_type}")
            temperature = float(temperature)

        else:
            status = device_info.get('status', 'off')
            if status is None:
                raise  MyException(f"Status is not given for {device_type}")
            
        device_id = len(smart_device[1]) + 1

        if device_type == 'thermostat':
            device = device_class(device_id, self, temperature)
        else:
            device = device_class(device_id, device_type, status)

        self._devices[device_type][1][device_id] = device
        print(f"Info : {device_type.capitalize()} {device_id} has been created!")
        return device
        
    def _get_actions(self):
        return self._actions

    def _get_schedules(self):
        return self._schedules

    def _get_device(self, device_type, device_id):
        if device_type in self._devices:
            if device_id in self._devices[device_type][1]:
                return self._devices[device_type][1][device_id]
        raise MyException(f"No {device_type} found with ID {device_id}.")


    def create_schedule(self, schedule_info):
        if not self._is_valid_time(schedule_info['time']):
            raise MyException("Invalid time format")

        device = schedule_info['device']
        if not any((item['device'][1] == device[1] and item['device'][0] == device[0]) for item in self._schedules.values()):
            schedule = Schedules(self, schedule_info)
            schedule.create_schedule()
        else:
            print(f"Info : A schedule for {device[0]} {device[1]} already exists")

    def run_scheduled_tasks(self):
        if self._schedules:
            print('Info : Waiting for scheduled tasks to finish!')
        while self._schedules:
            schedule.run_pending()
            time.sleep(1)

    def _turn_on(self, device_type, device_id):
        device = self._get_device(device_type, device_id)
        device.turn_on()

    def _open_door(self, device_type, device_id):
        device = self._get_device(device_type, device_id)
        device.open_door()

    def _turn_off(self, device_type, device_id):
        device = self._get_device(device_type, device_id)
        device.turn_off()

    def _close_door(self, device_type, device_id):
        device = self._get_device(device_type, device_id)
        device.close_door()

    def _perform_action(self,action,device_type,device_id):
        self._actions[action](device_type,device_id)

    def _is_valid_time(self, time_str):
        try:
            datetime.strptime(time_str, "%H:%M")
            return True
        except ValueError:
            return False