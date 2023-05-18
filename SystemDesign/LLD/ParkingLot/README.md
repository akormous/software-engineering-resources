# Parking Lot

## Use Cases
1. Park a vehicle
2. Get fare for the time vehicle is parked
3. Types of vehicle that can be parked, separate spaces for each type of vehicle

## Constraints
1. Parking space, limited number of vehicles can be parked

## Basic Design
1. Vehicle (interface) -> Bike, Car, Truck (Concrete classes)
2. Track time on entry and exit of a vehicle
3. Different spots for vehicle ( enum )

## Bottlenecks
1. One type of parking gets full, while others could be empty

## Scalability
1. From one floor to multiple floors

```mermaid
classDiagram
direction TB

class VehicleType {
    <<enumeration>>
    Bike
    Car
    Truck
}

class Vehicle {
    <<interface>>
    -string registration
    -VehicleType type
    +getType()
}

class Bike {
    +Bike()
}

class Truck {
    +Truck()
}

class Car {
    +Car()
}

Vehicle <.. VehicleType

Vehicle <-- Bike
Vehicle <-- Car
Vehicle <-- Truck


class ParkingSlotSize {
    <<enumeration>>
    2-Wheeler = [Bike]
    4-Wheeler = [Bike, Car]
    6-Wheeler = [Bike, Car, Truck]
    +isVehicleParkingPossible(Vehicle vehicle)
}

class ParkingSlot {
    -string id PK
    -int floor
    -Vehicle vehicle
    -ParkingSlotSize size
    -string status
    +ParkingSlot()
    +clear()
    +setVehicle()
    +getVehicle()
    +getFloor()
    +parkVehicle()
    +getStatus()
}

class Floor {
    -list<ParkingSlot> slots
    -string id PK
    -int level
    +Floor()
    +clear()
    +getEmptySlot()
}

class Parking {
    -list<Floor> floors
    -string name
    -string address
    +Parking()
}

ParkingSlot <.. ParkingSlotSize
Parking *-- Floor
ParkingSlot --* Floor

ParkingSlot *-- Vehicle

class ParkingDetails {
    -Vehicle vehicle
    -Parking parking
    -DateTime entryTime
    -DateTime exitTime

    ParkingDetails()
}

class FareController {
    -map<Vehicle, ParkingDetails> vehicleParkingDetails
    +onVehicleEntry(Vehicle , Parking)
    +onVehicleExit(Vehicle)
    +getFare(Vehicle)
}

FareController *-- ParkingDetails

```