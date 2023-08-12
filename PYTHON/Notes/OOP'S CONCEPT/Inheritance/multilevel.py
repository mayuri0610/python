# Multilevel Inheritance
# A class inherits its property to another class and another class inherits property to next class and so on,
# then such type of inheritance known as Multilevel inheritance.

#            a          Base class                  Grant parents class 
#       <----b          Immediate class             parents class
#       <----c          Derived class               child class


class Baseclass:
    def car(self):
        print("Audi")

class Parent(Baseclass):
    def Bick(self):
        print("Royal Enfield")

class Child(Parent):
    def cycle(self):
        print("Honda City")


obj1=Baseclass()
obj1.car()

obj2=Parent()
obj2.Bick()
obj2.car()

obj3=Child()
obj3.cycle()
obj3.Bick()
obj3.car()
