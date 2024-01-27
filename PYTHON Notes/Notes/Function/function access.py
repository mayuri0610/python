# Function  :
# A function is a self contained block which design and execute separately.
# A function is a block of code which only runs when it is called.


# Type of Actual Arguments

# Positional Arguments
# Default Arguments
# Keyword Arguments
# Variable Length Arguments
# Keyword Variable Length Arguments




# Actual and Formal Argument

# Formal Argument - Function definition parameters are called as formal arguments
# Actual Argument - Function call arguments are actual arguments 


def add (x, y) :            #formal argument
    c = x + y
    print(c)

add(10, 20)                 #Actual Argument




print("********************************************************************************************************************************************")





# can i declare a class inside a function               --yes
# can i declare a function inside a function            --yes        
# can i declare a class inside a class                  --yes      
# can i declare a function inside a class               --yes       



def outer_function():
    # This is the outer function
    print("This is the outer function")

    # Define a nested class inside the outer function
    class InnerClass:
        def __init__(self):
            print("This is the inner class")
        def add(self):
            print("This is the inner class")

    # Create an instance of the inner class
    inner_instance = InnerClass()
    inner_instance.add()

# Call the outer function
outer_function()





print("********************************************************************************************************************************************")




print("function inside the function  or   nested function")

# can i declear function inside the function  and how
# Function return another Function      --- Ans -YES 


# Return statements can be used to return something from the function. 
# In Python, it is possible to return one or more variables/values.



class MyClass(object):

    def add(self):
        print("Mayuri")

        def sub(self):
            print("moksh")

            def multi(self):
                print("munnu")

            return multi    
        return sub

obj = MyClass()
# obj.add()           #mayuri  
sub= obj.add()      #mayuri         
# sub(obj)            #moksh
multi=sub(obj)      #moksh 
multi(obj)          #munnu



print("********************************************************************************************************************************************")


class MyClass(object):

    def add(self):
        print("Mayuri")

        def sub(self):
            print("moksh")

            def multi(self):
                print("munnu")

            multi(self)

        sub(self)

obj = MyClass()
obj.add()           #mayuri moksh munnu 


print("********************************************************************************************************************************************")




def add():
        print("Mayuri")

        def sub():
            print("moksh")

            def multi():
                print("munnu")

            return multi
         
        return sub



# add()           #mayuri
ans=add()       #mayuri
# ans()           #moksh
ans1=ans()      #moksh 
ans1()          #munnu




print("********************************************************************************************************************************************")



def add():
        print("Mayuri")

        def sub():
            print("moksh")

            def multi():
                print("munnu")

            multi()
         
        sub()

add()           #mayuri moksh munnu





print("********************************************************************************************************************************************")


print("Pass a Function as Parameter")


# Pass a Function as Parameter

# We can pass a function as parameter to another function.
# Ex:-


def disp(sh):
	print("Disp Function  and   " + sh())
	
def show():
	return "Show Function"

disp(show)



print("********************************************************************************************************************************************")


def add(sh):
    print(10+sh())

def show():
    return 20


add(show)


def disp(sh):
	print(10 + sh())
	
def show():
	return 30

disp(show)