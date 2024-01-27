

# CONSTUCTOR

# Constuctor is a special member function of a class which creating and initializing an object at that class . 

# Constuctor call only one times.

# A constructor is a special method inside a class that is atomatically call when object is created .

# Constuctor is generally used for instantiating an object.     - use

# Python the __init__() method is called the constructor and is always called when an object is created.

# 1) default constructor - nothing pass any arguments when we create a new object
# 2) parameter constructor - pass at least one argument when we create a new object




# default constructor

class Arithmetic:
    def __init__(self) -> None:
        self.a="mayuri"
        self.b="moksh"
        print(self.a,self.b)

obj=Arithmetic()


# parameter constructor

class Arithmetic:
    def __init__(self,x,y) -> None:
        self.a=x                               #instance variable
        self.b=y
        print(self.a,self.b)
 

obj=Arithmetic(10,20)

