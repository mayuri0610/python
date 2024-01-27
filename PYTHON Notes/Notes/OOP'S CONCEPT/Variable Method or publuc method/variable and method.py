
# classmethod and staticmethod decorator use     
# variables ki defination    
# class method defination and their decleratoin 
#  use of self and cls 
# can i access instance variables through instance methods and static methods and class methods and how
# can i access class variables through instance methods and static methods and class methods and how
# can i access local variables through instance methods and static methods and class methods and how



#  Class Variables

# 1)instance variable    -   self
# 2)class / static variable      -   cls
# 3)local variable      



# *************************************************************************************************************************************


#   Class Method 

# 1)instance method
# 2)class method        -@classmethod  decorator
# 3)static method       -@staticmethod  decorator


# *************************************************************************************************************************************



# self KEYWORD 

# self keyword represents the instance in instance methods. 
# By using the “self”  we can access the instance attributes and methods of the class.
# It binds the attributes with the given arguments.


        # USE OF SELF KEYWORD 

# self is used for access instance variables  



# cls KEYWORD 

# cls keyword represents the instance in class methods. 
# By using the "cls"  we can access the class attributes and methods of the class.
# cls is used for access class variables  and Methods .


# *************************************************************************************************************************************



# 1)instance variable  and Method

# instance variable 
# If the value of a variable varies from object to object, then such variables are called instance variables.
# Instance variables are defined within constructor and instance method.

# instance method
# If we use instance variables inside a method, such methods are called instance methods. 
# It must have a self parameter to refer to the current object.


# default constructor

# class Arithmetic:
#     def __init__(self) -> None:
#         self.a="mayuri"
#         self.b="moksh"
#         print(self.a,self.b)
#     def add(self):
#         print(self.a,self.b)

# obj=Arithmetic()
# obj.add()


class Arithmetic:
    def __init__(self,x,y):
        self.a=x                               #instance variable
        self.b=y
        # print(self.a,self.b)
    def add(self):                              #instance method
        print(self.a,self.b)

obj=Arithmetic(10,20)
obj.add()



# *************************************************************************************************************************************


# 2)class variable  and methods

# class variable
# A class variable is a variable that is declared inside of class, but outside of any instance method or __init__() method.

# class method
# A class method is a method that is bound to the class and not the object of the class.




class Arithmetic:
    a=10                        #class variable
    @classmethod                #class method
    def add(cls):
        print(cls.a)


Arithmetic.add()

obj=Arithmetic()
obj.add()




# *************************************************************************************************************************************

# local variable

# Python local variables are those which are defined inside a function and their scope is limited to that function only. 
# local variables are accessible only inside the function.



# *************************************************************************************************************************************


# static method




# *************************************************************************************************************************************












# can i access instance variables through instance methods and static methods and class methods and how
# can i access class variables through instance methods and static methods and class methods and how


# instance method
class Employee:
    office_name = "XYZ Private Limited"
    # def __init__(self):
    #     print(Employee.office_name)
    def add(self):
        print(Employee.office_name)

my_instance = Employee()



# static method


# can i access local variables through instance methods and static methods and class methods and how










