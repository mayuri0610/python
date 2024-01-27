

# Abstraction is used to hideing the implementation showing the functionality of the function from the users. 
# The users only interact with the basic implementation of the function, but inner working is hidden. 
# User is familiar with that "what function does" but they don't know "how it does."


# Abtraction is achive through abtract class and abtract method 
# Abtract class : Abtract class is a class that contains one or more abstract methods is called as abtract class.
# Abtract method : An abstract method is a method that has a declaration but does not have an implementation.



# @abstractmethod: abstractmethod is a decorator provided by the abc module that marks a method as abstract. 
# Abstract methods are declared in abstract classes without providing an implementation. 
# Subclasses that inherit from an abstract class must provide concrete implementations for these abstract methods.





# examples:

from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def speed(self):
        pass

    @abstractmethod
    def engin(self):
        pass


class Suzuki:
    
    def speed(self):
        print("Speed is 30 kmph")

    def engin(self):
        print("Engin is ...")

class Marsadies:
    
    def speed(self):
        print("Speed is 70 kmph")


class BMW:
    
    def speed(self):
        print("Speed is 120 kmph")





suzukiobj = Suzuki()
suzukiobj.speed()
suzukiobj.engin()

Marsadiesobj = Marsadies()
Marsadiesobj.speed()

bmwobj = BMW()
bmwobj.speed()






