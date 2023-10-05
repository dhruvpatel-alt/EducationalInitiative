import schedule
from datetime import datetime
import calendar  
from  customize_exception import MyException

class Schedules:
    def __init__(self, device_manager, schedule_info):
        self._device_manager = device_manager
        self._schedule_info = schedule_info
        self._schedule_id = None

    def create_schedule(self):
        if not self._schedule_id:
            device = self._schedule_info['device']
            schedule_time = self._schedule_info['time']
            action = self._schedule_info['action']

            if not any((item['device'][1] == device[1] and item['device'][0] == device[0]) for item in self._device_manager._schedules.values()):

            # Create the schedule
                self._schedule_id = len(self._device_manager._get_schedules()) + 1
                self._device_manager._get_schedules()[self._schedule_id] = {
                'time': schedule_time,
                'action': action,
                'device': device,
                'schedule_id': self._schedule_id
            }

                self.execute_schedule(self._schedule_id)
            else:
                raise MyException(f"No {device[0]} found with ID {device[1]}.")
                
    def execute_schedule(self, schedule_id):
        schedule_info = self._schedule_info
        target_time = datetime.strptime(schedule_info['time'], "%H:%M")
        current_time = datetime.now()
        target_time = target_time.replace(year=current_time.year, month=current_time.month, day=current_time.day)
        day = "today"
        if target_time < current_time:
            if current_time.month == 12:  
                target_time = target_time.replace(year=current_time.year + 1, month=1)
            else:
                if current_time.day == calendar.monthrange(current_time.year, current_time.month)[1]:
                    target_time = target_time.replace(month=current_time.month + 1, day=1)
                else:
                    target_time = target_time.replace(day=current_time.day + 1)
            day = "Tomorrow"

        time_until_target = target_time - current_time
        seconds_to_wait = time_until_target.total_seconds()
        device = schedule_info['device']
        print(f"Info : Schedule {schedule_id} has been created for {device[0]} {device[1]}. It will run at {schedule_info['time']} {day}.")
        def action_wrapper():
            if self._schedule_id in self._device_manager._get_schedules():
                device = schedule_info['device']
                type = device[0]
                id = device[1]
                action = schedule_info['action']
                self._device_manager._perform_action(action, type, id)
                print(f"Action : {action} completed for {type} {id}.")
                self.remove_schedule(self._schedule_id)

        schedule.every(seconds_to_wait).seconds.do(action_wrapper)

    def remove_schedule(self, schedule_id):
        if schedule_id in self._device_manager._get_schedules():
            del self._device_manager._get_schedules()[schedule_id]
        else:
            raise MyException(f"Schedule with ID {schedule_id} not found.")
