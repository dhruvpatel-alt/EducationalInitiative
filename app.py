from controllers.Devices import DeviceManager
from controllers.Schedules import ScheduleManager
from controllers.Triggers import  TriggerManager

# Create an instance of the Device Manager
device_manager = DeviceManager()

# Add a light to the system
light_info = {'type': 'light', 'status': 'off'}
light = device_manager.create_device(light_info)

# Add a door to the system
door_info = {'type': 'door', 'status': 'locked'}
door = device_manager.create_device(door_info)

# Add a thermostat to the system
thermostat_info = {'type': 'thermostat', 'temperature': '60','device_manager':device_manager}
thermostat= device_manager.create_device(thermostat_info)

trigger_info={'condition':'temperature < 70','device_type':'light','device_id':1 ,'action':'turn_on'}
thermostat.add_trigger(trigger_info)
schedule_manager = ScheduleManager()

light_turn_on_schedule = {
    'device': light,
    'time': '15:00',
    'action': light.turn_on
}

schedule_manager.create_schedule(light_turn_on_schedule)
schedule_manager.run_scheduled_tasks()
