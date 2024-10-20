from typing import List
from reservations import Reservation
from card_payment import CardPayment

class CarRental:

    _instance = None

    def __init__(self) -> None:
        if(CarRental._instance is not None):
            raise Exception("instance is present")
        else:
            CarRental._instance = self
            self.cars = {}
            self.reservations = {}

    @staticmethod
    def get_instance():
        if(CarRental._instance==None):
            CarRental()
        return CarRental._instance

    def add_car(self):
        pass

    def search_car(self,make,model,start_date,end_date):
        pass

    def make_reservatiom(self, car, customer, start_date, end_date):
        pass

    def cancel_reservation(self, res_id):
        pass