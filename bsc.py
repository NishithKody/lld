class Car:
    def __init__(self, name): # self refers to the instance of the class
        self.name = name
    
    def display_info(self):
        print('the info-',self.name)


car = Car("test")
car.display_info()


#Encapsulation

class BankAcc:
    def __init__(self, balance):
        self.__balance = balance
    
    def addAmt(self, amt)->None: # None is the return type
        self.__balance +=amt
    
    def display(self)->None:
        print('the amt',self.__balance) # private variable are declared using __ (double underscore), protected variables are declared using single underscore

acc = BankAcc(100)
acc.addAmt(10)
acc.display()

#Inheritance

class Vehicle:
    def __init__(self, color) -> None:
        self.color = color
    
    def disp(self) -> None:
        print('the color is',self.color)

class Car(Vehicle):             #inheritance, multiple inheritance is also possible
    def __init__(self, color, speed)->None:
        super().__init__(color)
        self.speed = speed
    
    def dispSpeed(self) -> None:
        print('the speed is',self.speed)

c1 = Car("red",10)
c1.disp()
c1.dispSpeed()


from abc import ABC, abstractmethod # ABC is abstract base class

class Shape(ABC):
    @abstractmethod # this is a decorator
    def area(self):
        pass # or we can do : raise NotImpletementedException 

class Rect(Shape):
    def __init__(self, h, b) -> None:
        self.h = h
        self.b = b
    
    def area(self):
        return self.b * self.h

rect = Rect(5,2)
val = rect.area()
print('the area is ',val)



