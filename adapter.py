# Adapter is a structural design pattern, which allows objects with incompactible interfaces to collaborate

class OldSystem:
    def legacy_work(self):
        return('the old system is doing work')


class Adapter:
    def __init__(self, oldSystem):
        self.oldSystem = oldSystem
    
    def new_operation(self):
        return(f"Adapter:{self.oldSystem.legacy_work()}")

def client_code(adapter:Adapter):
    result = adapter.new_operation()
    print(result)

if(__name__=='__main__'):
    oldSystem = OldSystem()
    adapter = Adapter(oldSystem)
    client_code(adapter)
    
    