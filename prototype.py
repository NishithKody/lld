import copy

#python has inbuild methods for copy and deep copy. For other languages, look into the copy and deep copy implementation
# copy - gives a clone of the structure in a high level, the nested objects are not cloned
# deep copy - the object and the nested objects are cloned.

class Prototype:
    def __init__(self, name) -> None:
        self.name = name
    
    def clone(self):
        return copy.deepcopy(self)
    
    def display(self):
        print('the name is',self.name)


if(__name__ == '__main__'):
    p1:Prototype = Prototype('first_proto')
    p1.display()

    p2:Prototype = p1.clone()
    p2.display()
