from typing import Dict, List

class VendingMachine:
    _instance = None

    def __init__(self) -> None:
        if(VendingMachine._instance is not None):
            raise Exception('The instance is present')
        else:
            VendingMachine._instance = self
            self.product = {}

    @staticmethod
    def get_instance():
        if(VendingMachine._instance == None):
            VendingMachine()
        return VendingMachine._instance

    #collect money

    #restock
    



