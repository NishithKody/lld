from vm_state.state import State
from product import Product
from coins import Coin
from cash import Cash

class ReadyState(State):
    def __init__(self, vending_machine) -> None:
        self.vending_machine = vending_machine
        print('change to ready state')
    
    def select_product(self, product:Product):
        print("the product has already been selected")

    def insert_coin(self, coin:Coin):
        self.vending_machine.add_coin(coin)
        self.check_payment_status()

    def insert_cash(self, cash:Cash):
        self.vending_machine.add_cash(cash)
        self.check_payment_status()

    def dispense_product(self):
        print('please pay')

    def return_change(self):
        print('please pay')

    def check_payment_status(self):
        current_total = self.vending_machine.total_payment
        if(current_total>=self.vending_machine.selected_product.value):
            print('payment is complete')
            self.vending_machine.set_state(self.vending_machine.dispense_state)
        else:
            print('payment is not complete')
