import time
from parking_details import ParkingDetails
from vehicle import vehicle
from parking import Parking

class FareController:
    def __init__(self):
        self.db = {}

    def onVehicleEntry(self, vh: vehicle.Vehicle, parking: Parking):
        self.db[vh] = ParkingDetails(vh, parking)
        self.db[vh].entry_time = time.time()

    def onVehicleExit(self, vh: vehicle.Vehicle):
        self.db[vh].exit_time = time.time()
        fare = self.getFare(self.db[vh].entry_time, self.db[vh].exit_time)
        self.db.pop(vh)
        return fare

    def getFare(self, entry_time, exit_time):
        return (exit_time - entry_time) * 0.01