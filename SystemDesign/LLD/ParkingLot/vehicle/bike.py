from vehicle import vehicle
from . import vehicle_type

class bike(vehicle.Vehicle):
    def __init__(self, registration: str):
        super().__init__(registration, vehicle_type.VehicleType.BIKE)