import floor
from parking_slot_size import ParkingSlotSize

class Parking:
    def __init__(self, floor_count: int, name: str, address: str):
        self.floor_count = floor_count
        self.name = name
        self.address = address
        self.floors = []
        for i in range(-1, floor_count):
            self.floors.append( floor.Floor(name + str(i), i, 100, ParkingSlotSize.WHEELS_4))

    