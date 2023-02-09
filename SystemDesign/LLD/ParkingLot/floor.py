import parking_slot
import parking_slot_size
from utils import IdGenerator

class Floor:
    def __init__(self, id: str, level: int, slot_count: int, slot_type: parking_slot_size.ParkingSlotSize):
        self.id = id
        self.level = level
        self.slot_count = slot_count
        self.slots = []
        for i in range(0, slot_count):
            self.slots.append( parking_slot.parking_slot(IdGenerator().generateId(), id, slot_type) )
    
    def clear(self):
        for s in self.slots:
            s.clear()

    def getEmptySlot(self):
        for s in self.slots:
            if s.isEmpty():
                return s
        raise Exception("No available parking on this floor, try another floor!")
