from parking_lot import Parking_lot
from car import Car
from truck import Truck
from level import Level

class ParkingLotDemo:
    def run():
        parking_lot = Parking_lot.get_instance()
        # parking_lot.add_level(Level(1,10))
        parking_lot.add_level(Level(1,5))

        car = Car("1A22")
        # truck = Truck('Tr1s22')

        print('avail')
        parking_lot.display_avail()
        res = parking_lot.park_vehicle(car)
        print('park vech res',res)

        print('----------- after park')
        parking_lot.display_avail()
        parking_lot.unpark_vehicle(car)

        print('----------- unpark')
        parking_lot.display_avail()

if(__name__=='__main__'):
    ParkingLotDemo.run()