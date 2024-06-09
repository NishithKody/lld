from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def get_desc(self):
        pass
    
    @abstractmethod
    def attack_power(self):
        pass


class BasicComponent:
    def get_desc(self):
        return "Basic character"

    def attack_power(self):
        return 10

class Decorator(Component):
    def __init__(self,component:Component) -> None:
        self.component = component
    
    @abstractmethod
    def get_desc(self):
        pass

    @abstractmethod
    def attack_power(self):
        pass

class FireDecorator(Decorator):
    def get_desc(self):
        return self.component.get_desc()+" and Fire power"

    def attack_power(self):
        return self.component.attack_power()+10

class WindDecorator(Decorator):
    def get_desc(self):
        return self.component.get_desc()+" and Wind power"

    def attack_power(self):
        return self.component.attack_power()+15

def Client():
    base = BasicComponent()
    print(f'Base:{base.get_desc()},{base.attack_power()}')

    fireBase = FireDecorator(base)
    print(f'FireBase:{fireBase.get_desc()},{fireBase.attack_power()}')

    windBase = WindDecorator(base)
    print(f'WindBase:{windBase.get_desc()},{windBase.attack_power()}')

    windFireBase = WindDecorator(fireBase)
    print(f'WindFireBase:{windFireBase.get_desc()},{windFireBase.attack_power()}')

if(__name__=='__main__'):
    Client()