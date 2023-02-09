import parking_slot
from parking_slot_size import ParkingSlotSize
from vehicle import bike, car, truck
from utils import IdGenerator
from parking import Parking
from fare_controller import FareController
import time

gen = IdGenerator()

fareController = FareController()

my_parking = Parking(6, "THE ROCK PARKING", "BEHIND THE BIG ROCK")

for i in range(0, 10):
    tempCar = car.car("HR26" + gen.generateId().upper())
    print(i," Parking ", tempCar.registration)
    try:
        my_parking.floors[0].getEmptySlot().parkVehicle( tempCar )
        fareController.onVehicleEntry(tempCar, my_parking)
    except Exception as e:
        print(e)

time.sleep(5)

for ps in my_parking.floors[0].slots:
    if ps.isEmpty():
        continue
    fare = fareController.onVehicleExit(ps.getVehicle())
    ps.clear()
    print("EXIT ", ps.getVehicle().registration, " Fare = ", fare)

