
#   CLASS

#  class is a way which binds data member and its associates function together within a single unit.
#  class is a blueprint for a object.
#  class is hold variables and functions or methods.


# syntax
# class MyClass:
#   x = 5




#   OBJECT 
# It is a instance of class.
# variable and function of a class are accessible by using class object or instance . 

# Everything is in python treated as an object , including variables and functions, list , tuple , dictionary, set .

# Object is a simply a collection of data (variable) and method (function).

# When objects are created, memory is allocated to them in the form of heap memory.     -   use

# The size of memory allocated decided or depend on by the attribute (variable) and method (function) available in that class.

# After the memory block is allocated the special method init() or constructor is called internally initial data is stored into a variable to this method.

# The location of the allocated memory address of the instance is written to the object.

# The memory location is passed to self.



# syntax
# p1 = MyClass()



# class formulas(object):
#     def addition(self,n1,n2) :
#         print(n1+n2)
#     def subtraction(self,n1,n2):
#         print(n1-n2)




# obj=formulas()
# a=int(input("Enter the number="))
# b=int(input("Enter the number="))
# obj.addition(a,b)
# obj.subtraction(a,b)





print("class inside the class")

# can i declear class inside the class  and how

class MyClass(object):

    print("MyClass")

    class MyClass1:
          print("MyClass 1")



obj=MyClass()

obj1=obj.MyClass1()






