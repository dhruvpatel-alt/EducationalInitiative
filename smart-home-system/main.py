from device_manager import DeviceManager
from observer import CustomObserver
device_manager = DeviceManager()
custom_observer = CustomObserver()
device_manager.attach(custom_observer)
# Create a light device
light_info = {'type': 'light', 'status': 'off'}
light = device_manager.create_device(light_info)

# Create a door device
door_info = {'type': 'door', 'status': 'locked'}
door = device_manager.create_device(door_info)

# Create a thermostat device
thermostat_info = {'type': 'thermostat', 'temperature': 90}
thermostat = device_manager.create_device(thermostat_info)

# Create a schedule for the light
schedule_info = {'device': ['light', 1], 'time': '23:10', 'action': 'turn_on'}
schedule_info2 = {'device': ['door', 1], 'time': '23:11', 'action': 'close_door'}
device_manager.create_schedule(schedule_info)
device_manager.create_schedule(schedule_info2)

# Define temperature triggers
trigger_info = {'condition': 'temperature >= 80', 'action': ('turn_on', 'light', 1)}
trigger_info1 = {'condition': 'temperature >= 60', 'action': ('close_door', 'door', 1)}
thermostat.add_trigger(trigger_info)
thermostat.add_trigger(trigger_info1)

# Update the thermostat's temperature
thermostat.update_temperature(50)

# Run scheduled tasks
device_manager.run_scheduled_tasks()
device_manager.get_status()