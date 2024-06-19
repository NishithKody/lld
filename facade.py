class Subsystem1():
    def start_operation(self):
        print('Subsystem1: Start Operation')

    def execute(self):
        print('Subsystem1: Excute')

class Subsystem2():
    def start_operation(self):
        print('Subsystem2: Start Operation')

    def execute(self):
        print('Subsystem2: Excute')

class Facade():
    def __init__(self, subsystem1, subsystem2) -> None:
        self.subsystem1 = subsystem1
        self.subsystem2 = subsystem2
    
    def do_work(self):
        self.subsystem1.start_operation()
        self.subsystem2.start_operation()

        self.subsystem1.execute()
        self.subsystem2.execute()

def Client():
    sub1 = Subsystem1()
    sub2 = Subsystem2()
    facade = Facade(sub1, sub2)
    facade.do_work()

Client()
