from  customize_exception import MyException

class Trigger:
    def __init__(self, device_manager, temperature):
        self._device_manager = device_manager
        self._triggers = []
        self._temperature = float(temperature)

    def add_trigger(self, trigger_info):
        condition = trigger_info['condition']
        action = trigger_info['action'][0]
        device_type = trigger_info['action'][1]
        device_id = trigger_info['action'][2]
        # Check if the specified device exists in the manager
        device_to_trigger = self._device_manager._get_device(device_type, device_id)
        if device_to_trigger:
            self._triggers.append((condition, action, device_type, device_id))
            print(f"Info : Trigger added for {device_type} {device_id}")
            data = {"temperature": self._temperature}
            if eval(condition, data):
                self.trigger_action(action, device_type, device_id)
        else:
            raise MyException(f"No {device_type} found with ID {device_id}.")

    def check_condition(self, data):
        for condition, action, device_type, device_id in self._triggers:
            if eval(condition, data):
                self.trigger_action(action, device_type, device_id)

    def trigger_action(self, action, device_type, device_id):
        target_device = self._device_manager._get_device(device_type, device_id)
       
        if target_device:
            if action == 'turn_on':
                target_device.turn_on()
            elif action == 'turn_off':
                target_device.turn_off()
            elif action == "close_door":
                target_device.close_door()
            elif action == "open_door":
                target_device.open_door()

    def update_temperature(self, data, new_temperature):
        self._temperature = new_temperature
        self.check_condition(data)