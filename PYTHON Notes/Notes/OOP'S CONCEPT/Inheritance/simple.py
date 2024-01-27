
#INHERITANCE 

# Extending property from one class to another class is called  inhertances 



# Single Inheritance :

# Single Inheritance :If a class is derived from one base class (Parent Class), it is called Single Inheritance.
# A class inherits its property to another class then such type of inheritance known as single inheritance. 

# Base class or parent class: A class which inherits its property to another is called base class.
# Derived class or sub class : A class in which properties are inherited called as derived class.




class Parent:
    def car(self):
        print("Parents property = Audi")

class Child(Parent):
    def cycle(self):
        print("Child property = Hero")


# child khud ki and parent ki property access kar sakta hai 
obj=Child()
obj.cycle()
obj.car()

#parent sirf apani property access kar sakta hai only
#parent apane child ki property access nahi kar sakta

obj1=Parent()
obj1.car()

# obj1.cycle()


