from vending_machine import VendingMachine
from product import Product

class VendingMachineDemo:
    def run(self):
        prod1 = Product("prod1",10)
        prod2 = Product("prod2",20)

        vmd_inst = VendingMachine()

        vmd_inst.inventory.add_product(prod1,1)
        vmd_inst.inventory.add_product(prod2,10)

        vmd_inst.select_product(prod1)


if(__name__=='__main__'):
    vmd = VendingMachineDemo()
    vmd.run()