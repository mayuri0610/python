# Hierarchical Inheritance :
# A class inherits its property into multiple sub classes, then such type of inheritance known as hierarchical inheritance.

#               A                           Base class                  parents class
#      <----B       C---->                  Derived class               child class


class Parent:
    def car(self):
        print("BMW")

class child_1(Parent):
    def bick(self):
        print("KTM")

class child_2(Parent):
    def cycle(self):
        print("honda city")

obj1=Parent()
obj1.car()
# obj1.bick()
# obj1.cycle()


obj2=child_1()
obj2.bick()
obj2.car()
# obj2.cycle()


obj3=child_2()
obj3.cycle()
obj3.car()
# obj3.bick()
