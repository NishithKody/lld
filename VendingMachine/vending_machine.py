from typing import Dict, List
from product import Product
from inventory import Inventory
from state import State
from idle_state import IdleState
from ready_state import ReadyState

class VendingMachine:
    _instance = None

    def __init__(self) -> None:
        if(VendingMachine._instance is not None):
            raise Exception('The instance is present')
        else:
            VendingMachine._instance = self
            self.inventory = Inventory()
            self.selected_product = None
            self.total_payment = 0
            self.idle_state = IdleState(self)
            self.ready_state = ReadyState(self)
            self.current_state = self.idle_state

    @staticmethod
    def get_instance():
        if(VendingMachine._instance == None):
            VendingMachine()
        return VendingMachine._instance

    def set_state(self, state: State):
        self.current_state = state

    def select_product(self, product):
        self.current_state.select_product(product)
    #collect money

    #restock

