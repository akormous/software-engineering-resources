from enum import Enum
from vehicle import vehicle_type

v = vehicle_type.VehicleType

class ParkingSlotSize(Enum):
    WHEELS_2 = [v.BIKE]
    WHEELS_4 = [v.BIKE, v.CAR]
    WHEELS_6 = [v.BIKE, v.CAR, v.TRUCK]