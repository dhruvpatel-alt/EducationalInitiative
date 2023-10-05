class Observer:
    def update(self, subject, data):
        pass
    
class CustomObserver(Observer):
    def update(self, subject, data):
        if 'status' in data:
            device_name = data['device_name']
            device_id = data['device_id']
            status = data['status']
            print(f"Observer: {device_name.capitalize()} {device_id} status updated to {status}")

        if 'temperature' in data:
            temperature = data['temperature']
            print(f"Observer: Thermostat temperature updated to {temperature}")