from vehicle import vehicle
from parking import Parking

class ParkingDetails:
    def __init__(self, vh: vehicle.Vehicle, parking: Parking):
        self.vh = vh
        self.parking = parking
        self.entry_time = None
        self.exit_time = None