from vehicle import vehicle
import parking_slot_size

class parking_slot:
    def __init__(self, id: str, floor: int, slot_size: parking_slot_size.ParkingSlotSize):
        self.id = id
        self.floor = floor
        self.slot_size = slot_size
        self.vh = None
        self.status = "EMPTY"

    def clear(self):
        self.vehicle = None
        self.status = "EMPTY"

    def setVehicle(self, vh: vehicle.Vehicle):
        self.vh = vh

    def getVehicle(self):
        return self.vh
    
    def getFloor(self):
        return self.floor
    
    def parkVehicle(self, vh: vehicle.Vehicle):
        if self.status == "OCCUPIED":
            raise Exception("This spot is already taken!")
        if vh.get_type() not in self.slot_size.value:
            raise Exception("Vehicle cannot be parked here. It's too big!")
        self.setVehicle(vh)
        self.status = "OCCUPIED"

    def getStatus(self) -> str:
        return "[{}] {}".format(self.id, self.status)

    def getId(self) -> str:
        return self.id

    def isEmpty(self) -> bool:
        return self.status == "EMPTY"
