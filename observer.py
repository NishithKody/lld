from abc import ABC, abstractmethod

class Subject:
    def __init__(self) -> None:
        self.observers = []
    
    def add_observer(self, observer):
        self.observers.append(observer)
    
    def remove_observer(self, observer):
        self.observers.remove(observer)
    
    def notify(self, message):
        for obs in self.observers:
            obs.update(message)

class Observer(ABC):
    @abstractmethod
    def update(self,message):
        pass

class ConcreteObserver(Observer):
    def __init__(self,name) -> None:
        self.name = name

    def update(self,message):
        print(f'Observer[{self.name}]: {message}')


def Client():
    observer1 = ConcreteObserver('listener1')
    observer2 = ConcreteObserver('listener2')

    subject = Subject()
    subject.add_observer(observer1)
    subject.add_observer(observer2)

    subject.notify('event1')

if(__name__=='__main__'):
    Client()

