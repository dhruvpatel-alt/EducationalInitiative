import schedule
from datetime import datetime

class ScheduleManager:
    def __init__(self):
        self.schedules = {}

    def create_schedule(self, schedule_info):
        device = schedule_info['device']
        schedule_time = schedule_info['time']
        action = schedule_info['action']
        schedule_id = len(self.schedules) + 1
        if not any(item['device'].device_id == device.device_id for item in self.schedules.values()):
            self.schedules[schedule_id] = {
                'time': schedule_time,
                'action': action,
                'device': device,
                'schedule_id': schedule_id  
            }
            self.execute_schedule(schedule_id)
        else:
            print(f"A schedule for {device.device_type} {device.device_id} already exists.")

    def execute_schedule(self, schedule_id):
        schedule_info = self.schedules[schedule_id]
        target_time = datetime.strptime(schedule_info['time'], "%H:%M")
        current_time = datetime.now()
        target_time = target_time.replace(year=current_time.year, month=current_time.month, day=current_time.day)
        day="today"
        if target_time < current_time:
            target_time = target_time.replace(day=current_time.day + 1)
            day="Tomorrow"
        time_until_target = target_time - current_time
        seconds_to_wait = time_until_target.total_seconds()
        print(seconds_to_wait)
        device=schedule_info['device']
        print(f"Schedule {schedule_id} has been created for {device.device_type} {device.device_id}. It will run at {schedule_info['time']} {day}.")
        def action_wrapper():
            schedule_info['action']()
            print(f"Action completed for {device.device_type} {device.device_id}.")
            self.remove_schedule(schedule_info['schedule_id'])  

        schedule.every(seconds_to_wait).seconds.do(action_wrapper)

    def remove_schedule(self, schedule_id):
        if schedule_id in self.schedules:
            del self.schedules[schedule_id]
