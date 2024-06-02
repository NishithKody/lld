import copy

class Prototype:
    def __init__(self, name) -> None:
        self.name = name
    
    def clone(self):
        return copy.deepcopy(self)
    
    def display(self):
        print('the name is',self.name)


if(__name__ == '__main__'):
    p1 : Prototype = Prototype('first_proto')
    p1.display()

    p2:Prototype = p1.clone()
    p2.display()
