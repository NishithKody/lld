#good resource - https://pravash-techie.medium.com/python-singleton-pattern-for-effective-object-management-49d62ec3bd9b

# there are many other ways to implement singleton in python
# three important concepts in singleton
# static private instance, so that it is not accessible from outside the class and can be retreived without instance creation
# static pubic method, which will be called by the client to get the instance
# private constructor, so that new instances are not created and we can internally control the creation of the instance
class Singleton():

    __instance = None

    # this is a virtual private contructor
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
    

