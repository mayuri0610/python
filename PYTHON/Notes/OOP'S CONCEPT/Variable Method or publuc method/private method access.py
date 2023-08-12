
# Name mangling
# Python provides a magic wand that can be used to call private methods outside the class also, it is known as name mangling. 
# It means that any identifier of the form __geek (at least two leading underscores or at most one trailing underscore) is replaced with _classname__geek,
# where the class name is the current class name with a leading underscore(s) stripped.


class A:
 
    # Declaring public method
    def fun(self):
        print("Public method")
 

    # Declaring private method
    def __fun(self):
        print("Private method")
 

    # Calling private method via another method
    def Help(self):
        self.fun()
        self.__fun()
 
 
# Driver's code
obj = A()
obj.Help()


# *******************************************************************************************************************


class A:
 
    # Declaring public method
    def fun(self):
        print("Public method")
 

    # Declaring private method
    def __fun(self):
        print("Private method")
 
 
# Driver's code
obj = A()
 
# Calling the private member through name mangling
obj._A__fun()













