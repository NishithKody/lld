#good resource - https://pravash-techie.medium.com/python-singleton-pattern-for-effective-object-management-49d62ec3bd9b

class Singleton():

    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("The instance has already been created")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        
        return Singleton.__instance
    

if(__name__=='__main__'):
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()

    if(s1==s2):
        print('There are the same object')
    

