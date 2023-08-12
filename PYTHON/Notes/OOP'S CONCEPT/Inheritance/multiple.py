# Multiple Inheritance :
# More than one class inherits its property into single derived class, then such type of inheritance known as multiple inheritance.
#
#
#           A       B                     Base class                  parents class
#       <---    c   --->                  Derived class               child class

 


# #1) perent ke function name differnt 


# class parent1:
#     def car1(self):
#         print("Mercedes")

# class parent2:
#     def car2(self):
#         print("audi")

# class child(parent1,parent2):
#     def cycle(self):
#         print("Honda city")


# # child apani property and papa ki aur chacha ki property access kar sakta hai 

# obj1=child()
# obj1.cycle()
# obj1.car1()
# obj1.car2()

# #parent apani apani property access kar sakte hai 
# #but child ki nahi kar sakte aur apane bhai ki property access nahi kar sakte

# obj2=parent1()
# obj2.car1()
# # obj2.car2()
# # obj2.child()

# obj3=parent2()
# obj3.car2()
# # obj3.car1()
# # obj3.child()





#2) Parent ke function name same


class parent1:
    def car(self):
        print("Mercedes")

class parent2:
    def car(self):
        print("audi")

class child(parent1,parent2):
    def cycle(self):
        print("Honda city")


obj1=child()
obj1.cycle()
obj1.car()


#parent apani apani property access kar sakte hai 
#but child ki nahi kar sakte aur apane bhai ki property access nahi kar sakte

obj2=parent1()
obj2.car()
# obj2.child()

obj3=parent2()
obj3.car()
# obj3.child()