from abc import ABC, abstractmethod

class Receiver():
    def operation(self):
        print('the receiver does the operation')

class Command(ABC):
    @abstractmethod
    def __init__(self, receiver:Receiver):
        pass

    @abstractmethod
    def operation(self):
        pass

# this concrete command will have the different variations, such as cutCommand, copy Command
class ConcreateCommand(Command):
    def __init__(self, receiver: Receiver):
        self.receiver = receiver
    
    def operation(self):
        self.receiver.operation()

class Invoker():
    def __init__(self,cmd) -> None:
        self.cmd = cmd
    
    def execute(self):
        self.cmd.operation()
    
def Client():
    rec = Receiver()
    cmd = ConcreateCommand(rec)
    invoker = Invoker(cmd)

    invoker.execute()

Client()
    
