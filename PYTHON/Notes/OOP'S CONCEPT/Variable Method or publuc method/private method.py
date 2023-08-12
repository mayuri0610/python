

# Private methods are those methods that should neither be accessed outside the class nor by any base class. 
# In Python, there is no existence of Private methods that cannot be accessed except inside a class. 
# However, to define a private method prefix the member name with the double underscore “__”. 
# This is what private methods are used for. It is used to hide the inner functionality of any class from the outside world. 



class Base:
 
    # Declaring public method
    def fun(self):
        print("Public method")
 
    # Declaring private method
    def __fun(self):
        print("Private method")
 



# Creating a derived class
 
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of
        # Base class
        Base.__init__(self)


    def call_public(self):
        # Calling public method of base class
        print("\nInside derived class")
        self.fun()
 

    def call_private(self):
        # Calling private method of base class
        self.__fun()
 
 




obj1 = Base()               # Driver code
obj1.fun()                  # Calling public method

# obj1.__fun()                # Uncommenting obj1.__fun() will raise an AttributeError



obj2 = Derived()
obj2.call_public()

# obj2.call_private()         # Uncommenting obj1.__fun() will raise an AttributeError





# private methods of the class can neither be accessed outside the class nor by any base class.
# However, private methods can be accessed by calling the private methods via public methods. 





