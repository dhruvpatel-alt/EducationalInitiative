from controllers.Devices import DeviceManager

# Create an instance of the Device Manager
device_manager = DeviceManager()

# Add a light to the system
light_info = {'type': 'light', 'status': 'off'}
light = device_manager.create_device(light_info)

# Add a door to the system
door_info = {'type': 'door', 'status': 'locked'}
door = device_manager.create_device(door_info)

# Add a thermostat to the system (only one thermostat)
thermostat_info = {'type': 'thermostat', 'temperature': 90}
thermostat = device_manager.create_device(thermostat_info)

# Create Schedule for light with id 1
schedule_info={'device':['light',1],'time':'15:50','action':'turn_on'}
schedule_info2={'device':['door',1],'time':'15:51','action':'close_door'}
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
