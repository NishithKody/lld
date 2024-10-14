from parking_spot import ParkingSpot
from vehicle import Vehicle
from typing import List

class Level:
    def __init__(self,level, n) -> None:
        self.level = level
        self.parking_spots:List[ParkingSpot] = []
        for i in range(n):
            self.parking_spots.append(ParkingSpot(i))

    def park_vehicle(self, vehicle:Vehicle)->bool:
        for spot in self.parking_spots:
            if(spot.is_available() and spot.get_vehicle_type()==vehicle.type):
                spot.park_vehicle(vehicle)
                return True
        return False
    
    def unpark_vehicle(self, vehicle:Vehicle) -> bool:
        for spot in self.parking_spots:
            if(spot.get_vehicle() == vehicle):
                spot.unpark()
                return True
        
        return False
    
    def display_avai(self):
        print('the avail at the level ',self.level)
        for spot in self.parking_spots:
            if(spot.is_available()):
                print('spot- ',spot.get_spot_number())
            