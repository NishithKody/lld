from vm_state.state import State
from product import Product
from coins import Coin
from cash import Cash

class ReadyState(State):
    def __init__(self, vending_machine) -> None:
        self.vending_machine = vending_machine
    
    def select_product(self, product:Product):
        print("the product has already been selected")

    def insert_coin(self, coin:Coin):
        print('please select product')

    def insert_cash(self, cash:Cash):
        print('please select product')

    def dispense_product(self):
        print('please pay')

    def return_change(self):
        print('please pay')


    