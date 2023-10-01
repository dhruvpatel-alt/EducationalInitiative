from controllers.Schedules import Schedules
import time
from controllers.SmartDevices import Light, Door, Thermostat
import schedule

class DeviceManager:
    def __init__(self):
        self._schedules = {}
        self._actions = {
            'turn_on': self._turn_on,
            'turn_off': self._turn_off,
            'close_door': self._close_door,
            'open_door': self._open_door
        }


    def create_device(self, device_info):
        device_type = device_info['type']
        smart_device = self._devices.get(device_type)
        if smart_device is None:
            print(f"We are not supporting this {device_type} device right now. Try with another device.")
            return None
        device_class = smart_device[0]
        if device_class:
            device_id = len(smart_device[1]) + 1
            if device_type == 'thermostat':
                temperature = float(device_info.get('temperature', 70))
                device = device_class(device_id, self, temperature)
            else:
                status = device_info.get('status', 'off')
                device = device_class(device_id, device_type, status)
            self._devices[device_type][1][device_id] = device
            print(f"{device_type.capitalize()} {device_id} has been created!")
            return device
        
    def _get_actions(self):
        return self._actions

    def _get_schedules(self):
        return self._schedules

    def _get_device(self, device_type, device_id):
        if device_type in self._devices:
            if device_id in self._devices[device_type][1]:
                return self._devices[device_type][1][device_id]
        return None

    def create_schedule(self, schedule_info):
        device = schedule_info['device']
        if not any((item['device'][1] == device[1] and item['device'][0] == device[0]) for item in self._schedules.values()):
            schedule = Schedules(self, schedule_info)
            schedule.create_schedule()
        else:
            print(f"A schedule for {device[0]} {device[1]} already exists")

    def run_scheduled_tasks(self):
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