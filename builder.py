from abc import ABC, abstractmethod

class Product:
    def __init__(self) -> None:
        self.parts = []
    
    def add(self,part):
        self.parts.append(part)
    
    def list_parts(self):
        res = ""
        for part in self.parts:
            res= res+part+","
        print(f'Product:{res}')

class Builder:
    def add_part_a(self):
        pass
    
    def add_part_b(self):
        pass

    def add_part_c(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        self.product = Product()
    
    def add_part_a(self):
        self.product.add('PartA')
    
    def add_part_b(self):
        self.product.add('PartB')
    
    def add_part_c(self):
        self.product.add('PartC')
    
    def build(self)->Product:
        return self.product

def Client():
    builder = ConcreteBuilder()
    builder.add_part_a()
    builder.add_part_b()
    product = builder.build()

    product.list_parts()

    builder2 = ConcreteBuilder()
    builder2.add_part_c()
    builder2.add_part_a()

    product2 = builder2.build()
    product2.list_parts()

    
if(__name__=='__main__'):
    Client()