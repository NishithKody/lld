from abc import ABC, abstractmethod

class Composition:
    @abstractmethod
    def operation(self):
        pass

class Leaf(Composition):
    def __init__(self, name) -> None:
        self.name = name
    
    def operation(self):
        return f" Leaf: {self.name}"

class Comp(Composition):
    def __init__(self,name) -> None:
        self.name = name
        self.children = []
    
    def add_child(self,child):
        self.children.append(child)
    
    def operation(self):
        res = f" Operation: {self.name}"
        for child in self.children:
            res = res + child.operation()

        return res

def Client():
    leaf1 = Leaf('moon')
    leaf2 = Leaf('earth')

    comp1 = Comp('sun')           
    comp2 = Comp('pluto')

    comp2.add_child(leaf2)
    comp1.add_child(leaf1)
    comp1.add_child(comp2)

    res = comp1.operation()
    print(res)

Client()
        