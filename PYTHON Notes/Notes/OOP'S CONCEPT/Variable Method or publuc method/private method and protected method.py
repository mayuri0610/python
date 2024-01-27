

# Private methods

# Private methods are those methods that should neither be accessed outside the class nor by any base class. 
# In Python, there is no existence of Private methods that cannot be accessed except inside a class. 
# However, to define a private method prefix the member name with the double underscore “__”. 
# This is what private methods are used for. It is used to hide the inner functionality of any class from the outside world. 



# Protected methods

# protected members of a class can be accessed by other members within the class and are also available to their subclasses.



# Name mangling
# Python provides a magic wand that can be used to call private methods outside the class also, it is known as name mangling. 
# It means that any identifier of the form __geek (at least two leading underscores or at most one trailing underscore) is replaced with _classname__geek,
# where the class name is the current class name with a leading underscore(s) stripped.





print("*********************************************************************************************************************************************")

print("method 1 with simple class")



class A:

    def fun(self):                  # Declaring public method
        print("Public method")
    
    def _fun(self):                     # Declaring Protected method   
        print("Protected method")

    def __fun(self):                 # Declaring private method
        print("Private method")
     
    def Help(self):                 # Calling private method via another method
        self.fun()
        self._fun()
        self.__fun()
 
 
obj = A()
obj.Help()


print("*********************************************************************************************************************************************")


print("method 2 with simple class")


class Base:

    def fun(self):                   # Declaring public method
        print("Public method")

    def _fun(self):                      # Declaring protected method 
        print("Protected method")
    
    def __fun(self):                  # Declaring private method  
        print("Private method")

    def accessPrivateMembers(self):
        self.__fun()
 

obj1 = Base()               # Driver code
obj1.fun()                  # Calling public method
obj1._fun()                 # Calling protected method
# obj1.__fun()              # Uncommenting obj1.__fun() will raise an AttributeError
obj1._Base__fun()           # Calling the private member through name mangling



print("*********************************************************************************************************************************************")

print("method 1 with child class")

# Creating a child class
 
class Derived(Base):

    def call_public(self):                      # Calling public method of base class
        self.fun()

    def call_protected(self):                      # Calling protected method of base class
        self._fun()

    def call_private(self):                     # Calling private method of base class
        self.__fun()
 

obj2 = Derived()
obj2.call_public()
obj2.call_protected()
# obj2.call_private()         # Uncommenting obj1.__fun() will raise an AttributeError 
obj2.accessPrivateMembers()          


# private methods of the class can neither be accessed outside the class nor by any base class.
# However, private methods can be accessed by calling the private methods via public methods. 




