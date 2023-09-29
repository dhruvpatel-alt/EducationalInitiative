class TriggerManager:
    def __init__(self, device_manager):
        self.triggers = {}
        self.device_manager = device_manager

    def add_trigger(self, triggerInfo):
        condition=triggerInfo['condition']
        device_type=triggerInfo['device_type']
        device_id=triggerInfo['device_id']
        action=triggerInfo['action']
        devices=self.device_manager.devices
        if device_type in devices:
            if device_id in devices[device_type][1]:
                self.triggers[condition] = (device_type, device_id, action)
                print(f"Triggers for {device_type} with id {device_id} has been added")
            else:
                print(f"There is no {device_type} devices with device_id {device_id} .")
        else:
            print(f"We are not supporting {device_type} devices right now.")

    def check_condition(self, condition, data):
        parts = condition.split()
        if len(parts) == 3:
            left_operand, operator, right_operand = parts
            target=int(data[left_operand])
            if operator == ">" and left_operand in data:
                return target > float(right_operand)
            elif operator == "<" and left_operand in data:
                return target < float(right_operand)
        return False

    def trigger_action_on_device(self, data):
        for condition, action in self.triggers.items():
            device_type, device_id, action_type = action
            device = self.device_manager.devices[device_type][1][device_id]
            if self.check_condition(condition, data):
                print(f"Condition {condition} Trigger for {device_type} {device_id}")
                if action_type == "turn_on":
                    device.turn_on()
                elif action_type == "turn_off":
                    device.turn_off()