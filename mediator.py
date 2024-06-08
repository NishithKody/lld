from abc import ABC, abstractmethod

class Component:
    def __init__(self,mediator) -> None:
        self.mediator = mediator
    
    def send(self,message):
        self.mediator.notify(message)

    def receive(self,message):
        print(f'Component: received message {message}')

class Metiator:
    @abstractmethod
    def notify(self, message):
        pass

class ConcreteMediator:
    def __init__(self) -> None:
        self.components = []
    
    def add_component(self, component):
        self.components.append(component)
    
    def notify(self, message):
        print(f'Mediator: {message}')
    
    def send(self, message):
        for comp in self.components:
            comp.receive(message)

def Client():
    mediator = ConcreteMediator()

    comp1 = Component(mediator)
    comp2 = Component(mediator)

    mediator.add_component(comp1)
    mediator.add_component(comp2)

    comp1.send('eventA')
    comp2.send('eventB')

    mediator.send('update component')

if(__name__=='__main__'):
    Client()