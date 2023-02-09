from . import vehicle_type

class Vehicle:
    def __init__(self, registration: str, v_type: vehicle_type.VehicleType):
        self.registration = registration
        self.v_type = v_type
    
    def get_type(self) -> str:
        return self.v_type
    
