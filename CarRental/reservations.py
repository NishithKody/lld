from datetime import date, timedelta
from car import Car

class Reservation:
    def __init__(self, id, customer, car:Car, start_date, end_date) -> None:
        self.id = id
        self.customer = customer
        self.car = car
        self.start_date = start_date
        self.end_date = end_date
        self.total_price = self.cal_price()

    def cal_price(self):
        days = (self.end_date-self.start_date).days + 1
        return self.car.get_price() * days
    
    def get_res_id(self):
        return self.id
    
    def get_car(self):
        return self.car

    def get_start_date(self):
        return self.start_date
    
    def get_end_date(self): 
        return self.end_date
    